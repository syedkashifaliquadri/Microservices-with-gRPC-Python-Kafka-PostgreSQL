# gRPC-with-Python-and-Kafka-for-Microservices
This repository provides a practical example of buildin a microservices architecture using gRPC with Python and Apache Kafka for asynchronous communication between services. The combination of gRPC and Kafka offers a powerful solution for developing scalable and decoupled microservices that can handle various functionalities independently.

Run gRPC Client and Server:

    1- python server.py
    2- python client.py

Required Commands:
    
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

    .\bin\windows\kafka-server-start.bat .\config\server.properties
    
    kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partition 1 --topic todo
    
    kafka-console-producer.bat --broker-list localhost:9092 --topic todo
    
    kafka-console-consumer.bat --topic todo --bootstrap-server localhost:9092 --from-beginning
    
    .\bin\windows\zookeeper-server-stop.bat .\config\zookeeper.properties
    
    .\bin\windows\kafka-server-stop.bat .\config\server.properties
