# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\"\x1d\n\rCreateRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x19\n\x0bReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\")\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x19\n\x08Response\x12\r\n\x05reply\x18\x01 \x01(\t2\xd3\x01\n\tMyService\x12\x31\n\nCreateData\x12\x13.todo.CreateRequest\x1a\x0e.todo.Response\x12-\n\x08ReadData\x12\x11.todo.ReadRequest\x1a\x0e.todo.Response\x12\x31\n\nUpdateData\x12\x13.todo.UpdateRequest\x1a\x0e.todo.Response\x12\x31\n\nDeleteData\x12\x13.todo.DeleteRequest\x1a\x0e.todo.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CREATEREQUEST']._serialized_start=20
  _globals['_CREATEREQUEST']._serialized_end=49
  _globals['_READREQUEST']._serialized_start=51
  _globals['_READREQUEST']._serialized_end=76
  _globals['_UPDATEREQUEST']._serialized_start=78
  _globals['_UPDATEREQUEST']._serialized_end=119
  _globals['_DELETEREQUEST']._serialized_start=121
  _globals['_DELETEREQUEST']._serialized_end=148
  _globals['_RESPONSE']._serialized_start=150
  _globals['_RESPONSE']._serialized_end=175
  _globals['_MYSERVICE']._serialized_start=178
  _globals['_MYSERVICE']._serialized_end=389
# @@protoc_insertion_point(module_scope)