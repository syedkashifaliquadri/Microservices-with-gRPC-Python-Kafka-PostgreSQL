from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc
import psycopg2
import json
from confluent_kafka import Producer


class MyServicer(todo_pb2_grpc.MyServiceServicer):
    def __init__(self):
        self.data_store = {}  # A simple in-memory data store
        self.connection = psycopg2.connect(
            user="postgres",
            password="kashif",
            host="localhost",
            port="5432",
            database="postgres",
        )

        self.producer = Producer({'bootstrap.servers': 'localhost:9092'})

    def CreateData(self, request, context):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (str(request.data),))
                # inserted_id = cursor.fetchone()[0]

                # Produce a message to the Kafka topic
                self.producer.produce('todo', key='create', value="Data created successfully")

            self.connection.commit()
            return todo_pb2.Response(reply="Data created successfully")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def ReadData(self, request, context):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users;")
                data = cursor.fetchall()
                if data:
                    # Convert the list of tuples to a list of dictionaries
                    dict_data = [{'id': item[0], 'name': item[1]} for item in data]

                    # Convert the list of dictionaries to JSON
                    json_data = json.dumps(dict_data)

                    # Produce a message to the Kafka topic
                    self.producer.produce('todo', key='read', value=json_data)

                    return todo_pb2.Response(reply=json_data)
                else:
                    return todo_pb2.Response(reply="Data not found")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def UpdateData(self, request, context):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE users SET name = %s WHERE id = %s;", (request.data, int(request.id),))

                # Produce a message to the Kafka topic
                self.producer.produce('todo', key='update', value=f'Data updated successfully now name: {request.data}')

            self.connection.commit()

            return todo_pb2.Response(reply=f"Data updated successfully now name: {request.data}")

        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")

    def DeleteData(self, request, context):
        try:
            with self.connection.cursor() as cursor:
                # check_user = cursor.execute("SELECT * FROM users WHERE id = %s;", (int(request.id),))
                # if check_user:
                cursor.execute("DELETE FROM users WHERE id = %s;", (int(request.id),))

                # Produce a message to the Kafka topic
                self.producer.produce('todo', key='delete', value=f"Data deleted successfully against: {str(request.id)}")

            self.connection.commit()

            return todo_pb2.Response(reply=f"Data deleted successfully against: {str(request.id)}")
        except Exception as e:
            return todo_pb2.Response(reply=f"Error: {str(e)}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_MyServiceServicer_to_server(MyServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server Start")
    server.wait_for_termination()
    print("Server terminat")


if __name__ == '__main__':
    serve()
