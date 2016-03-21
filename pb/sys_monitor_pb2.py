# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sys_monitor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sys_monitor.proto',
  package='',
  serialized_pb=_b('\n\x11sys_monitor.proto\"X\n\x0b\x43onnectStat\x12\"\n\tconn_stat\x18\x01 \x02(\x0e\x32\x0f.ConnectStatDef\x12%\n\x0cwhich_server\x18\x02 \x02(\x0e\x32\x0f.ServerIdentify\"2\n\rServerMessage\x12!\n\x0bserver_info\x18\x01 \x03(\x0b\x32\x0c.ConnectStat\"E\n\tOrderStat\x12\x11\n\torder_qty\x18\x01 \x02(\r\x12%\n\x0cwhich_server\x18\x02 \x02(\x0e\x32\x0f.ServerIdentify*:\n\x0e\x43onnectStatDef\x12\x13\n\x0f\x44ISCONNECT_STAT\x10\x00\x12\x13\n\x0f\x43ONNECTING_STAT\x10\x01*a\n\x0eServerIdentify\x12\t\n\x05ROBOT\x10\x0b\x12\x08\n\x04RISK\x10\x0c\x12\x0c\n\x08STOCKSVR\x10\r\x12\r\n\tFUTURESVR\x10\x0e\x12\r\n\tSTOCK_HSC\x10\x0f\x12\x0e\n\nFUTURE_HSC\x10\x10')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CONNECTSTATDEF = _descriptor.EnumDescriptor(
  name='ConnectStatDef',
  full_name='ConnectStatDef',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCONNECT_STAT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTING_STAT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=234,
  serialized_end=292,
)
_sym_db.RegisterEnumDescriptor(_CONNECTSTATDEF)

ConnectStatDef = enum_type_wrapper.EnumTypeWrapper(_CONNECTSTATDEF)
_SERVERIDENTIFY = _descriptor.EnumDescriptor(
  name='ServerIdentify',
  full_name='ServerIdentify',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROBOT', index=0, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RISK', index=1, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOCKSVR', index=2, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUTURESVR', index=3, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOCK_HSC', index=4, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUTURE_HSC', index=5, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=294,
  serialized_end=391,
)
_sym_db.RegisterEnumDescriptor(_SERVERIDENTIFY)

ServerIdentify = enum_type_wrapper.EnumTypeWrapper(_SERVERIDENTIFY)
DISCONNECT_STAT = 0
CONNECTING_STAT = 1
ROBOT = 11
RISK = 12
STOCKSVR = 13
FUTURESVR = 14
STOCK_HSC = 15
FUTURE_HSC = 16



_CONNECTSTAT = _descriptor.Descriptor(
  name='ConnectStat',
  full_name='ConnectStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conn_stat', full_name='ConnectStat.conn_stat', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='which_server', full_name='ConnectStat.which_server', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=109,
)


_SERVERMESSAGE = _descriptor.Descriptor(
  name='ServerMessage',
  full_name='ServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_info', full_name='ServerMessage.server_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=161,
)


_ORDERSTAT = _descriptor.Descriptor(
  name='OrderStat',
  full_name='OrderStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_qty', full_name='OrderStat.order_qty', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='which_server', full_name='OrderStat.which_server', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=232,
)

_CONNECTSTAT.fields_by_name['conn_stat'].enum_type = _CONNECTSTATDEF
_CONNECTSTAT.fields_by_name['which_server'].enum_type = _SERVERIDENTIFY
_SERVERMESSAGE.fields_by_name['server_info'].message_type = _CONNECTSTAT
_ORDERSTAT.fields_by_name['which_server'].enum_type = _SERVERIDENTIFY
DESCRIPTOR.message_types_by_name['ConnectStat'] = _CONNECTSTAT
DESCRIPTOR.message_types_by_name['ServerMessage'] = _SERVERMESSAGE
DESCRIPTOR.message_types_by_name['OrderStat'] = _ORDERSTAT
DESCRIPTOR.enum_types_by_name['ConnectStatDef'] = _CONNECTSTATDEF
DESCRIPTOR.enum_types_by_name['ServerIdentify'] = _SERVERIDENTIFY

ConnectStat = _reflection.GeneratedProtocolMessageType('ConnectStat', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTSTAT,
  __module__ = 'sys_monitor_pb2'
  # @@protoc_insertion_point(class_scope:ConnectStat)
  ))
_sym_db.RegisterMessage(ConnectStat)

ServerMessage = _reflection.GeneratedProtocolMessageType('ServerMessage', (_message.Message,), dict(
  DESCRIPTOR = _SERVERMESSAGE,
  __module__ = 'sys_monitor_pb2'
  # @@protoc_insertion_point(class_scope:ServerMessage)
  ))
_sym_db.RegisterMessage(ServerMessage)

OrderStat = _reflection.GeneratedProtocolMessageType('OrderStat', (_message.Message,), dict(
  DESCRIPTOR = _ORDERSTAT,
  __module__ = 'sys_monitor_pb2'
  # @@protoc_insertion_point(class_scope:OrderStat)
  ))
_sym_db.RegisterMessage(OrderStat)


# @@protoc_insertion_point(module_scope)