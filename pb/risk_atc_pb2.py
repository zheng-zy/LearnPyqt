# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: risk_atc.proto

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
  name='risk_atc.proto',
  package='risk_atc',
  serialized_pb=_b('\n\x0erisk_atc.proto\x12\x08risk_atc\"\xaa\x04\n\x12\x61tc_order_set_info\x12&\n\x1e\x61ll_future_order_volume_second\x18\x01 \x01(\r\x12$\n\x1c\x61ll_future_order_volume_most\x18\x02 \x01(\r\x12%\n\x1dIF_future_order_volume_second\x18\x03 \x01(\r\x12#\n\x1bIF_future_order_volume_most\x18\x04 \x01(\r\x12\x1e\n\x16IC_order_volume_second\x18\x05 \x01(\r\x12\x1c\n\x14IC_order_volume_most\x18\x06 \x01(\r\x12\x1e\n\x16IH_order_volume_second\x18\x07 \x01(\r\x12\x1c\n\x14IH_order_volume_most\x18\x08 \x01(\r\x12\"\n\x1a\x63ombin_order_button_second\x18\t \x01(\r\x12!\n\x19\x63ombin_order_button_click\x18\n \x01(\r\x12\"\n\x1a\x63ombin_redem_button_second\x18\x0b \x01(\r\x12!\n\x19\x63ombin_redem_button_click\x18\x0c \x01(\r\x12\x1b\n\x13order_button_second\x18\r \x01(\r\x12\x1a\n\x12order_button_click\x18\x0e \x01(\r\x12\x1b\n\x13redem_button_second\x18\x0f \x01(\r\x12\x1a\n\x12redem_button_click\x18\x10 \x01(\r\"D\n\x11\x41TC_Order_Set_Req\x12/\n\tatc_order\x18\x01 \x02(\x0b\x32\x1c.risk_atc.atc_order_set_info\"3\n\x12\x41TC_Order_Set_Resp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"f\n\x14\x41TC_Order_Query_Info\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12/\n\tatc_order\x18\x02 \x01(\x0b\x32\x1c.risk_atc.atc_order_set_info\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\xfd\x01\n\x13\x61tc_button_set_info\x12\x1b\n\x13\x63ombo_create_second\x18\x01 \x01(\r\x12\x1a\n\x12\x63ombo_create_click\x18\x02 \x01(\r\x12\x1b\n\x13\x63ombo_redeem_second\x18\x03 \x01(\r\x12\x1a\n\x12\x63ombo_redeem_click\x18\x04 \x01(\r\x12\x1c\n\x14\x62utton_create_second\x18\x05 \x01(\r\x12\x1b\n\x13\x62utton_create_click\x18\x06 \x01(\r\x12\x1c\n\x14\x62utton_redeem_second\x18\x07 \x01(\r\x12\x1b\n\x13\x62utton_redeem_click\x18\x08 \x01(\r\"G\n\x12\x41TC_Button_Set_Req\x12\x31\n\natc_button\x18\x01 \x02(\x0b\x32\x1d.risk_atc.atc_button_set_info\"4\n\x13\x41TC_Button_Set_Resp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"i\n\x15\x41TC_Button_Query_Info\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x31\n\natc_button\x18\x02 \x01(\x0b\x32\x1d.risk_atc.atc_button_set_info\x12\x0b\n\x03msg\x18\x03 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATC_ORDER_SET_INFO = _descriptor.Descriptor(
  name='atc_order_set_info',
  full_name='risk_atc.atc_order_set_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_future_order_volume_second', full_name='risk_atc.atc_order_set_info.all_future_order_volume_second', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_future_order_volume_most', full_name='risk_atc.atc_order_set_info.all_future_order_volume_most', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IF_future_order_volume_second', full_name='risk_atc.atc_order_set_info.IF_future_order_volume_second', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IF_future_order_volume_most', full_name='risk_atc.atc_order_set_info.IF_future_order_volume_most', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IC_order_volume_second', full_name='risk_atc.atc_order_set_info.IC_order_volume_second', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IC_order_volume_most', full_name='risk_atc.atc_order_set_info.IC_order_volume_most', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IH_order_volume_second', full_name='risk_atc.atc_order_set_info.IH_order_volume_second', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IH_order_volume_most', full_name='risk_atc.atc_order_set_info.IH_order_volume_most', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combin_order_button_second', full_name='risk_atc.atc_order_set_info.combin_order_button_second', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combin_order_button_click', full_name='risk_atc.atc_order_set_info.combin_order_button_click', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combin_redem_button_second', full_name='risk_atc.atc_order_set_info.combin_redem_button_second', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combin_redem_button_click', full_name='risk_atc.atc_order_set_info.combin_redem_button_click', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_button_second', full_name='risk_atc.atc_order_set_info.order_button_second', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_button_click', full_name='risk_atc.atc_order_set_info.order_button_click', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='redem_button_second', full_name='risk_atc.atc_order_set_info.redem_button_second', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='redem_button_click', full_name='risk_atc.atc_order_set_info.redem_button_click', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=583,
)


_ATC_ORDER_SET_REQ = _descriptor.Descriptor(
  name='ATC_Order_Set_Req',
  full_name='risk_atc.ATC_Order_Set_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='atc_order', full_name='risk_atc.ATC_Order_Set_Req.atc_order', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=585,
  serialized_end=653,
)


_ATC_ORDER_SET_RESP = _descriptor.Descriptor(
  name='ATC_Order_Set_Resp',
  full_name='risk_atc.ATC_Order_Set_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_atc.ATC_Order_Set_Resp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_atc.ATC_Order_Set_Resp.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=655,
  serialized_end=706,
)


_ATC_ORDER_QUERY_INFO = _descriptor.Descriptor(
  name='ATC_Order_Query_Info',
  full_name='risk_atc.ATC_Order_Query_Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_atc.ATC_Order_Query_Info.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atc_order', full_name='risk_atc.ATC_Order_Query_Info.atc_order', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_atc.ATC_Order_Query_Info.msg', index=2,
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
  serialized_start=708,
  serialized_end=810,
)


_ATC_BUTTON_SET_INFO = _descriptor.Descriptor(
  name='atc_button_set_info',
  full_name='risk_atc.atc_button_set_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combo_create_second', full_name='risk_atc.atc_button_set_info.combo_create_second', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combo_create_click', full_name='risk_atc.atc_button_set_info.combo_create_click', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combo_redeem_second', full_name='risk_atc.atc_button_set_info.combo_redeem_second', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combo_redeem_click', full_name='risk_atc.atc_button_set_info.combo_redeem_click', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_create_second', full_name='risk_atc.atc_button_set_info.button_create_second', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_create_click', full_name='risk_atc.atc_button_set_info.button_create_click', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_redeem_second', full_name='risk_atc.atc_button_set_info.button_redeem_second', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_redeem_click', full_name='risk_atc.atc_button_set_info.button_redeem_click', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=813,
  serialized_end=1066,
)


_ATC_BUTTON_SET_REQ = _descriptor.Descriptor(
  name='ATC_Button_Set_Req',
  full_name='risk_atc.ATC_Button_Set_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='atc_button', full_name='risk_atc.ATC_Button_Set_Req.atc_button', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=1068,
  serialized_end=1139,
)


_ATC_BUTTON_SET_RESP = _descriptor.Descriptor(
  name='ATC_Button_Set_Resp',
  full_name='risk_atc.ATC_Button_Set_Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_atc.ATC_Button_Set_Resp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_atc.ATC_Button_Set_Resp.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1141,
  serialized_end=1193,
)


_ATC_BUTTON_QUERY_INFO = _descriptor.Descriptor(
  name='ATC_Button_Query_Info',
  full_name='risk_atc.ATC_Button_Query_Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='risk_atc.ATC_Button_Query_Info.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atc_button', full_name='risk_atc.ATC_Button_Query_Info.atc_button', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='risk_atc.ATC_Button_Query_Info.msg', index=2,
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
  serialized_start=1195,
  serialized_end=1300,
)

_ATC_ORDER_SET_REQ.fields_by_name['atc_order'].message_type = _ATC_ORDER_SET_INFO
_ATC_ORDER_QUERY_INFO.fields_by_name['atc_order'].message_type = _ATC_ORDER_SET_INFO
_ATC_BUTTON_SET_REQ.fields_by_name['atc_button'].message_type = _ATC_BUTTON_SET_INFO
_ATC_BUTTON_QUERY_INFO.fields_by_name['atc_button'].message_type = _ATC_BUTTON_SET_INFO
DESCRIPTOR.message_types_by_name['atc_order_set_info'] = _ATC_ORDER_SET_INFO
DESCRIPTOR.message_types_by_name['ATC_Order_Set_Req'] = _ATC_ORDER_SET_REQ
DESCRIPTOR.message_types_by_name['ATC_Order_Set_Resp'] = _ATC_ORDER_SET_RESP
DESCRIPTOR.message_types_by_name['ATC_Order_Query_Info'] = _ATC_ORDER_QUERY_INFO
DESCRIPTOR.message_types_by_name['atc_button_set_info'] = _ATC_BUTTON_SET_INFO
DESCRIPTOR.message_types_by_name['ATC_Button_Set_Req'] = _ATC_BUTTON_SET_REQ
DESCRIPTOR.message_types_by_name['ATC_Button_Set_Resp'] = _ATC_BUTTON_SET_RESP
DESCRIPTOR.message_types_by_name['ATC_Button_Query_Info'] = _ATC_BUTTON_QUERY_INFO

atc_order_set_info = _reflection.GeneratedProtocolMessageType('atc_order_set_info', (_message.Message,), dict(
  DESCRIPTOR = _ATC_ORDER_SET_INFO,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.atc_order_set_info)
  ))
_sym_db.RegisterMessage(atc_order_set_info)

ATC_Order_Set_Req = _reflection.GeneratedProtocolMessageType('ATC_Order_Set_Req', (_message.Message,), dict(
  DESCRIPTOR = _ATC_ORDER_SET_REQ,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Order_Set_Req)
  ))
_sym_db.RegisterMessage(ATC_Order_Set_Req)

ATC_Order_Set_Resp = _reflection.GeneratedProtocolMessageType('ATC_Order_Set_Resp', (_message.Message,), dict(
  DESCRIPTOR = _ATC_ORDER_SET_RESP,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Order_Set_Resp)
  ))
_sym_db.RegisterMessage(ATC_Order_Set_Resp)

ATC_Order_Query_Info = _reflection.GeneratedProtocolMessageType('ATC_Order_Query_Info', (_message.Message,), dict(
  DESCRIPTOR = _ATC_ORDER_QUERY_INFO,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Order_Query_Info)
  ))
_sym_db.RegisterMessage(ATC_Order_Query_Info)

atc_button_set_info = _reflection.GeneratedProtocolMessageType('atc_button_set_info', (_message.Message,), dict(
  DESCRIPTOR = _ATC_BUTTON_SET_INFO,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.atc_button_set_info)
  ))
_sym_db.RegisterMessage(atc_button_set_info)

ATC_Button_Set_Req = _reflection.GeneratedProtocolMessageType('ATC_Button_Set_Req', (_message.Message,), dict(
  DESCRIPTOR = _ATC_BUTTON_SET_REQ,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Button_Set_Req)
  ))
_sym_db.RegisterMessage(ATC_Button_Set_Req)

ATC_Button_Set_Resp = _reflection.GeneratedProtocolMessageType('ATC_Button_Set_Resp', (_message.Message,), dict(
  DESCRIPTOR = _ATC_BUTTON_SET_RESP,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Button_Set_Resp)
  ))
_sym_db.RegisterMessage(ATC_Button_Set_Resp)

ATC_Button_Query_Info = _reflection.GeneratedProtocolMessageType('ATC_Button_Query_Info', (_message.Message,), dict(
  DESCRIPTOR = _ATC_BUTTON_QUERY_INFO,
  __module__ = 'risk_atc_pb2'
  # @@protoc_insertion_point(class_scope:risk_atc.ATC_Button_Query_Info)
  ))
_sym_db.RegisterMessage(ATC_Button_Query_Info)


# @@protoc_insertion_point(module_scope)
