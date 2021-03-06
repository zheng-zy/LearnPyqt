# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: risk_ban_buysell.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='risk_ban_buysell.proto',
  package='risk_ban_buysell',
  serialized_pb=_b('\n\x16risk_ban_buysell.proto\x12\x10risk_ban_buysell\"8\n\x0cproduct_info\x12\x12\n\nproduct_id\x18\x01 \x02(\t\x12\x14\n\x0cproduct_name\x18\x02 \x02(\t\"\x8a\x03\n\x15\x62\x61n_buy_ban_sell_info\x12>\n\x18\x62\x61sket_not_ban_buy_stock\x18\x01 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\x12?\n\x19\x62\x61sket_not_ban_sell_stock\x18\x02 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\x12:\n\x14\x62\x61sket_ban_buy_stock\x18\x03 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\x12;\n\x15\x62\x61sket_ban_sell_stock\x18\x04 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\x12:\n\x14single_ban_buy_stock\x18\x05 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\x12;\n\x15single_ban_sell_stock\x18\x06 \x03(\x0b\x32\x1c.risk_ban_buysell.stock_info\"!\n\x0bProduct_Req\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"@\n\x0cProduct_Resp\x12\x30\n\x08products\x18\x01 \x03(\x0b\x32\x1e.risk_ban_buysell.product_info\"#\n\rStock_Ban_Req\x12\x12\n\nproduct_id\x18\x01 \x02(\t\"_\n\x0eStock_Ban_Resp\x12\x12\n\nproduct_id\x18\x01 \x02(\t\x12\x39\n\x08\x62\x61n_info\x18\x02 \x01(\x0b\x32\'.risk_ban_buysell.ban_buy_ban_sell_info\"4\n\nstock_info\x12\x12\n\nstock_code\x18\x01 \x02(\t\x12\x12\n\nstock_name\x18\x02 \x02(\t\"b\n\x11Stock_Ban_Add_Req\x12\x12\n\nproduct_id\x18\x01 \x02(\t\x12\x39\n\x08\x62\x61n_info\x18\x02 \x01(\x0b\x32\'.risk_ban_buysell.ban_buy_ban_sell_info\"n\n\x12Stock_Ban_Add_Resp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x39\n\x08\x62\x61n_info\x18\x02 \x01(\x0b\x32\'.risk_ban_buysell.ban_buy_ban_sell_info\x12\x0b\n\x03msg\x18\x03 \x01(\t\"b\n\x11Stock_Ban_Del_Req\x12\x12\n\nproduct_id\x18\x01 \x02(\t\x12\x39\n\x08\x62\x61n_info\x18\x02 \x01(\x0b\x32\'.risk_ban_buysell.ban_buy_ban_sell_info\"n\n\x12Stock_Ban_Del_Resp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x39\n\x08\x62\x61n_info\x18\x02 \x01(\x0b\x32\'.risk_ban_buysell.ban_buy_ban_sell_info\x12\x0b\n\x03msg\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PRODUCT_INFO = _descriptor.Descriptor(
  name='product_info',
  full_name='risk_ban_buysell.product_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.product_info.product_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='risk_ban_buysell.product_info.product_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=44,
  serialized_end=100,
)


_BAN_BUY_BAN_SELL_INFO = _descriptor.Descriptor(
  name='ban_buy_ban_sell_info',
  full_name='risk_ban_buysell.ban_buy_ban_sell_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basket_not_ban_buy_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.basket_not_ban_buy_stock', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basket_not_ban_sell_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.basket_not_ban_sell_stock', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basket_ban_buy_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.basket_ban_buy_stock', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basket_ban_sell_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.basket_ban_sell_stock', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='single_ban_buy_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.single_ban_buy_stock', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='single_ban_sell_stock', full_name='risk_ban_buysell.ban_buy_ban_sell_info.single_ban_sell_stock', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=103,
  serialized_end=497,
)


_PRODUCT_REQ = _descriptor.Descriptor(
  name='Product_Req',
  full_name='risk_ban_buysell.Product_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.Product_Req.product_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=499,
  serialized_end=532,
)


_PRODUCT_RESP = _descriptor.Descriptor(
  name='Product_Resp',
  full_name='risk_ban_buysell.Product_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='products', full_name='risk_ban_buysell.Product_Resp.products', index=0,
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
  serialized_start=534,
  serialized_end=598,
)


_STOCK_BAN_REQ = _descriptor.Descriptor(
  name='Stock_Ban_Req',
  full_name='risk_ban_buysell.Stock_Ban_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.Stock_Ban_Req.product_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=600,
  serialized_end=635,
)


_STOCK_BAN_RESP = _descriptor.Descriptor(
  name='Stock_Ban_Resp',
  full_name='risk_ban_buysell.Stock_Ban_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.Stock_Ban_Resp.product_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ban_info', full_name='risk_ban_buysell.Stock_Ban_Resp.ban_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=637,
  serialized_end=732,
)


_STOCK_INFO = _descriptor.Descriptor(
  name='stock_info',
  full_name='risk_ban_buysell.stock_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stock_code', full_name='risk_ban_buysell.stock_info.stock_code', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stock_name', full_name='risk_ban_buysell.stock_info.stock_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=734,
  serialized_end=786,
)


_STOCK_BAN_ADD_REQ = _descriptor.Descriptor(
  name='Stock_Ban_Add_Req',
  full_name='risk_ban_buysell.Stock_Ban_Add_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.Stock_Ban_Add_Req.product_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ban_info', full_name='risk_ban_buysell.Stock_Ban_Add_Req.ban_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=788,
  serialized_end=886,
)


_STOCK_BAN_ADD_RESP = _descriptor.Descriptor(
  name='Stock_Ban_Add_Resp',
  full_name='risk_ban_buysell.Stock_Ban_Add_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_ban_buysell.Stock_Ban_Add_Resp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ban_info', full_name='risk_ban_buysell.Stock_Ban_Add_Resp.ban_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_ban_buysell.Stock_Ban_Add_Resp.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=888,
  serialized_end=998,
)


_STOCK_BAN_DEL_REQ = _descriptor.Descriptor(
  name='Stock_Ban_Del_Req',
  full_name='risk_ban_buysell.Stock_Ban_Del_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='risk_ban_buysell.Stock_Ban_Del_Req.product_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ban_info', full_name='risk_ban_buysell.Stock_Ban_Del_Req.ban_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1000,
  serialized_end=1098,
)


_STOCK_BAN_DEL_RESP = _descriptor.Descriptor(
  name='Stock_Ban_Del_Resp',
  full_name='risk_ban_buysell.Stock_Ban_Del_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_ban_buysell.Stock_Ban_Del_Resp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ban_info', full_name='risk_ban_buysell.Stock_Ban_Del_Resp.ban_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_ban_buysell.Stock_Ban_Del_Resp.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1100,
  serialized_end=1210,
)

_BAN_BUY_BAN_SELL_INFO.fields_by_name['basket_not_ban_buy_stock'].message_type = _STOCK_INFO
_BAN_BUY_BAN_SELL_INFO.fields_by_name['basket_not_ban_sell_stock'].message_type = _STOCK_INFO
_BAN_BUY_BAN_SELL_INFO.fields_by_name['basket_ban_buy_stock'].message_type = _STOCK_INFO
_BAN_BUY_BAN_SELL_INFO.fields_by_name['basket_ban_sell_stock'].message_type = _STOCK_INFO
_BAN_BUY_BAN_SELL_INFO.fields_by_name['single_ban_buy_stock'].message_type = _STOCK_INFO
_BAN_BUY_BAN_SELL_INFO.fields_by_name['single_ban_sell_stock'].message_type = _STOCK_INFO
_PRODUCT_RESP.fields_by_name['products'].message_type = _PRODUCT_INFO
_STOCK_BAN_RESP.fields_by_name['ban_info'].message_type = _BAN_BUY_BAN_SELL_INFO
_STOCK_BAN_ADD_REQ.fields_by_name['ban_info'].message_type = _BAN_BUY_BAN_SELL_INFO
_STOCK_BAN_ADD_RESP.fields_by_name['ban_info'].message_type = _BAN_BUY_BAN_SELL_INFO
_STOCK_BAN_DEL_REQ.fields_by_name['ban_info'].message_type = _BAN_BUY_BAN_SELL_INFO
_STOCK_BAN_DEL_RESP.fields_by_name['ban_info'].message_type = _BAN_BUY_BAN_SELL_INFO
DESCRIPTOR.message_types_by_name['product_info'] = _PRODUCT_INFO
DESCRIPTOR.message_types_by_name['ban_buy_ban_sell_info'] = _BAN_BUY_BAN_SELL_INFO
DESCRIPTOR.message_types_by_name['Product_Req'] = _PRODUCT_REQ
DESCRIPTOR.message_types_by_name['Product_Resp'] = _PRODUCT_RESP
DESCRIPTOR.message_types_by_name['Stock_Ban_Req'] = _STOCK_BAN_REQ
DESCRIPTOR.message_types_by_name['Stock_Ban_Resp'] = _STOCK_BAN_RESP
DESCRIPTOR.message_types_by_name['stock_info'] = _STOCK_INFO
DESCRIPTOR.message_types_by_name['Stock_Ban_Add_Req'] = _STOCK_BAN_ADD_REQ
DESCRIPTOR.message_types_by_name['Stock_Ban_Add_Resp'] = _STOCK_BAN_ADD_RESP
DESCRIPTOR.message_types_by_name['Stock_Ban_Del_Req'] = _STOCK_BAN_DEL_REQ
DESCRIPTOR.message_types_by_name['Stock_Ban_Del_Resp'] = _STOCK_BAN_DEL_RESP

product_info = _reflection.GeneratedProtocolMessageType('product_info', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT_INFO,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.product_info)
  ))
_sym_db.RegisterMessage(product_info)

ban_buy_ban_sell_info = _reflection.GeneratedProtocolMessageType('ban_buy_ban_sell_info', (_message.Message,), dict(
  DESCRIPTOR = _BAN_BUY_BAN_SELL_INFO,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.ban_buy_ban_sell_info)
  ))
_sym_db.RegisterMessage(ban_buy_ban_sell_info)

Product_Req = _reflection.GeneratedProtocolMessageType('Product_Req', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT_REQ,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Product_Req)
  ))
_sym_db.RegisterMessage(Product_Req)

Product_Resp = _reflection.GeneratedProtocolMessageType('Product_Resp', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCT_RESP,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Product_Resp)
  ))
_sym_db.RegisterMessage(Product_Resp)

Stock_Ban_Req = _reflection.GeneratedProtocolMessageType('Stock_Ban_Req', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_REQ,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Req)
  ))
_sym_db.RegisterMessage(Stock_Ban_Req)

Stock_Ban_Resp = _reflection.GeneratedProtocolMessageType('Stock_Ban_Resp', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_RESP,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Resp)
  ))
_sym_db.RegisterMessage(Stock_Ban_Resp)

stock_info = _reflection.GeneratedProtocolMessageType('stock_info', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_INFO,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.stock_info)
  ))
_sym_db.RegisterMessage(stock_info)

Stock_Ban_Add_Req = _reflection.GeneratedProtocolMessageType('Stock_Ban_Add_Req', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_ADD_REQ,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Add_Req)
  ))
_sym_db.RegisterMessage(Stock_Ban_Add_Req)

Stock_Ban_Add_Resp = _reflection.GeneratedProtocolMessageType('Stock_Ban_Add_Resp', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_ADD_RESP,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Add_Resp)
  ))
_sym_db.RegisterMessage(Stock_Ban_Add_Resp)

Stock_Ban_Del_Req = _reflection.GeneratedProtocolMessageType('Stock_Ban_Del_Req', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_DEL_REQ,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Del_Req)
  ))
_sym_db.RegisterMessage(Stock_Ban_Del_Req)

Stock_Ban_Del_Resp = _reflection.GeneratedProtocolMessageType('Stock_Ban_Del_Resp', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_BAN_DEL_RESP,
  __module__ = 'risk_ban_buysell_pb2'
  # @@protoc_insertion_point(class_scope:risk_ban_buysell.Stock_Ban_Del_Resp)
  ))
_sym_db.RegisterMessage(Stock_Ban_Del_Resp)


# @@protoc_insertion_point(module_scope)
