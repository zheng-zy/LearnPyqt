# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: future_trade.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2
import trade_db_model_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='future_trade.proto',
  package='future_trade',
  serialized_pb=_b('\n\x12\x66uture_trade.proto\x12\x0c\x66uture_trade\x1a\nbase.proto\x1a\x14trade_db_model.proto\"i\n\x0eQueryAssetResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12\x30\n\x0c\x66uture_asset\x18\x03 \x01(\x0b\x32\x1a.liyi.trade_db.FutureAsset\")\n\x10QueryPositionReq\x12\x15\n\rinstrument_id\x18\x01 \x01(\t\"r\n\x11QueryPositionResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12\x36\n\x0f\x66uture_position\x18\x03 \x03(\x0b\x32\x1d.liyi.trade_db.FuturePosition\"&\n\x12QueryOrderKnockReq\x12\x10\n\x08order_no\x18\x01 \x01(\t\"i\n\x0eQueryOrderResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12\x30\n\x0c\x66uture_order\x18\x04 \x03(\x0b\x32\x1a.liyi.trade_db.FutureOrder\"i\n\x0eQueryKnockResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12\x30\n\x0c\x66uture_knock\x18\x04 \x03(\x0b\x32\x1a.liyi.trade_db.FutureKnock\"\x1e\n\x0eSubTradeMsgReq\x12\x0c\n\x04type\x18\x01 \x02(\x05\"8\n\x0fSubTradeMsgResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\"~\n\x13QueryInstrumentResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12@\n\x17\x66uture_instrument_infos\x18\x03 \x03(\x0b\x32\x1f.liyi.trade_db.FutureInstrument\"2\n\tErrNotify\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\"\xd8\x01\n\x0e\x46utureOrderReq\x12\x0c\n\x04\x63ode\x18\x01 \x02(\t\x12\r\n\x05price\x18\x02 \x02(\x03\x12\x0b\n\x03qty\x18\x03 \x02(\r\x12\x0f\n\x07\x62s_flag\x18\x04 \x02(\x05\x12\x1b\n\x0fopen_close_flag\x18\x05 \x01(\x05:\x02-1\x12\x12\n\nprice_type\x18\x06 \x01(\x05\x12\x11\n\tpolicy_id\x18\x07 \x01(\x0c\x12\x11\n\ttrader_id\x18\x08 \x02(\t\x12\x11\n\ttrader_ip\x18\t \x01(\t\x12!\n\x0b\x63lient_type\x18\n \x01(\x0e\x32\x0c.client_type\"^\n\x11\x46utureWithdrawReq\x12\x10\n\x08order_no\x18\x01 \x02(\t\x12\x11\n\tpolicy_id\x18\x02 \x01(\x0c\x12\x11\n\ttrader_id\x18\x03 \x01(\t\x12\x11\n\ttrader_ip\x18\x04 \x01(\t\"]\n\x0f\x46utureOrderResp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\x12\x13\n\x0bret_message\x18\x02 \x01(\t\x12\x10\n\x08order_no\x18\x03 \x01(\t\x12\x11\n\tpolicy_id\x18\x04 \x01(\x0c\"=\n\tPushOrder\x12\x30\n\x0c\x66uture_order\x18\x01 \x03(\x0b\x32\x1a.liyi.trade_db.FutureOrder\"=\n\tPushKnock\x12\x30\n\x0c\x66uture_knock\x18\x01 \x03(\x0b\x32\x1a.liyi.trade_db.FutureKnock\"F\n\x0cPushPosition\x12\x36\n\x0f\x66uture_position\x18\x01 \x03(\x0b\x32\x1d.liyi.trade_db.FuturePosition\"L\n\x0ePushInstrument\x12:\n\x11\x66uture_instrument\x18\x01 \x03(\x0b\x32\x1f.liyi.trade_db.FutureInstrument')
  ,
  dependencies=[base_pb2.DESCRIPTOR,trade_db_model_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_QUERYASSETRESP = _descriptor.Descriptor(
  name='QueryAssetResp',
  full_name='future_trade.QueryAssetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.QueryAssetResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.QueryAssetResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='future_asset', full_name='future_trade.QueryAssetResp.future_asset', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=70,
  serialized_end=175,
)


_QUERYPOSITIONREQ = _descriptor.Descriptor(
  name='QueryPositionReq',
  full_name='future_trade.QueryPositionReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument_id', full_name='future_trade.QueryPositionReq.instrument_id', index=0,
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
  serialized_start=177,
  serialized_end=218,
)


_QUERYPOSITIONRESP = _descriptor.Descriptor(
  name='QueryPositionResp',
  full_name='future_trade.QueryPositionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.QueryPositionResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.QueryPositionResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='future_position', full_name='future_trade.QueryPositionResp.future_position', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=220,
  serialized_end=334,
)


_QUERYORDERKNOCKREQ = _descriptor.Descriptor(
  name='QueryOrderKnockReq',
  full_name='future_trade.QueryOrderKnockReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_no', full_name='future_trade.QueryOrderKnockReq.order_no', index=0,
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
  serialized_start=336,
  serialized_end=374,
)


_QUERYORDERRESP = _descriptor.Descriptor(
  name='QueryOrderResp',
  full_name='future_trade.QueryOrderResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.QueryOrderResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.QueryOrderResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='future_order', full_name='future_trade.QueryOrderResp.future_order', index=2,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=376,
  serialized_end=481,
)


_QUERYKNOCKRESP = _descriptor.Descriptor(
  name='QueryKnockResp',
  full_name='future_trade.QueryKnockResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.QueryKnockResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.QueryKnockResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='future_knock', full_name='future_trade.QueryKnockResp.future_knock', index=2,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=483,
  serialized_end=588,
)


_SUBTRADEMSGREQ = _descriptor.Descriptor(
  name='SubTradeMsgReq',
  full_name='future_trade.SubTradeMsgReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='future_trade.SubTradeMsgReq.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=590,
  serialized_end=620,
)


_SUBTRADEMSGRESP = _descriptor.Descriptor(
  name='SubTradeMsgResp',
  full_name='future_trade.SubTradeMsgResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.SubTradeMsgResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.SubTradeMsgResp.ret_message', index=1,
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
  serialized_start=622,
  serialized_end=678,
)


_QUERYINSTRUMENTRESP = _descriptor.Descriptor(
  name='QueryInstrumentResp',
  full_name='future_trade.QueryInstrumentResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.QueryInstrumentResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.QueryInstrumentResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='future_instrument_infos', full_name='future_trade.QueryInstrumentResp.future_instrument_infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=680,
  serialized_end=806,
)


_ERRNOTIFY = _descriptor.Descriptor(
  name='ErrNotify',
  full_name='future_trade.ErrNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.ErrNotify.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.ErrNotify.ret_message', index=1,
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
  serialized_start=808,
  serialized_end=858,
)


_FUTUREORDERREQ = _descriptor.Descriptor(
  name='FutureOrderReq',
  full_name='future_trade.FutureOrderReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='future_trade.FutureOrderReq.code', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='future_trade.FutureOrderReq.price', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qty', full_name='future_trade.FutureOrderReq.qty', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bs_flag', full_name='future_trade.FutureOrderReq.bs_flag', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_close_flag', full_name='future_trade.FutureOrderReq.open_close_flag', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_type', full_name='future_trade.FutureOrderReq.price_type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_id', full_name='future_trade.FutureOrderReq.policy_id', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trader_id', full_name='future_trade.FutureOrderReq.trader_id', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trader_ip', full_name='future_trade.FutureOrderReq.trader_ip', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='future_trade.FutureOrderReq.client_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
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
  serialized_start=861,
  serialized_end=1077,
)


_FUTUREWITHDRAWREQ = _descriptor.Descriptor(
  name='FutureWithdrawReq',
  full_name='future_trade.FutureWithdrawReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_no', full_name='future_trade.FutureWithdrawReq.order_no', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_id', full_name='future_trade.FutureWithdrawReq.policy_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trader_id', full_name='future_trade.FutureWithdrawReq.trader_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trader_ip', full_name='future_trade.FutureWithdrawReq.trader_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1079,
  serialized_end=1173,
)


_FUTUREORDERRESP = _descriptor.Descriptor(
  name='FutureOrderResp',
  full_name='future_trade.FutureOrderResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='future_trade.FutureOrderResp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret_message', full_name='future_trade.FutureOrderResp.ret_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_no', full_name='future_trade.FutureOrderResp.order_no', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_id', full_name='future_trade.FutureOrderResp.policy_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1175,
  serialized_end=1268,
)


_PUSHORDER = _descriptor.Descriptor(
  name='PushOrder',
  full_name='future_trade.PushOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='future_order', full_name='future_trade.PushOrder.future_order', index=0,
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
  serialized_start=1270,
  serialized_end=1331,
)


_PUSHKNOCK = _descriptor.Descriptor(
  name='PushKnock',
  full_name='future_trade.PushKnock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='future_knock', full_name='future_trade.PushKnock.future_knock', index=0,
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
  serialized_start=1333,
  serialized_end=1394,
)


_PUSHPOSITION = _descriptor.Descriptor(
  name='PushPosition',
  full_name='future_trade.PushPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='future_position', full_name='future_trade.PushPosition.future_position', index=0,
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
  serialized_start=1396,
  serialized_end=1466,
)


_PUSHINSTRUMENT = _descriptor.Descriptor(
  name='PushInstrument',
  full_name='future_trade.PushInstrument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='future_instrument', full_name='future_trade.PushInstrument.future_instrument', index=0,
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
  serialized_start=1468,
  serialized_end=1544,
)

_QUERYASSETRESP.fields_by_name['future_asset'].message_type = trade_db_model_pb2._FUTUREASSET
_QUERYPOSITIONRESP.fields_by_name['future_position'].message_type = trade_db_model_pb2._FUTUREPOSITION
_QUERYORDERRESP.fields_by_name['future_order'].message_type = trade_db_model_pb2._FUTUREORDER
_QUERYKNOCKRESP.fields_by_name['future_knock'].message_type = trade_db_model_pb2._FUTUREKNOCK
_QUERYINSTRUMENTRESP.fields_by_name['future_instrument_infos'].message_type = trade_db_model_pb2._FUTUREINSTRUMENT
_FUTUREORDERREQ.fields_by_name['client_type'].enum_type = base_pb2._CLIENT_TYPE
_PUSHORDER.fields_by_name['future_order'].message_type = trade_db_model_pb2._FUTUREORDER
_PUSHKNOCK.fields_by_name['future_knock'].message_type = trade_db_model_pb2._FUTUREKNOCK
_PUSHPOSITION.fields_by_name['future_position'].message_type = trade_db_model_pb2._FUTUREPOSITION
_PUSHINSTRUMENT.fields_by_name['future_instrument'].message_type = trade_db_model_pb2._FUTUREINSTRUMENT
DESCRIPTOR.message_types_by_name['QueryAssetResp'] = _QUERYASSETRESP
DESCRIPTOR.message_types_by_name['QueryPositionReq'] = _QUERYPOSITIONREQ
DESCRIPTOR.message_types_by_name['QueryPositionResp'] = _QUERYPOSITIONRESP
DESCRIPTOR.message_types_by_name['QueryOrderKnockReq'] = _QUERYORDERKNOCKREQ
DESCRIPTOR.message_types_by_name['QueryOrderResp'] = _QUERYORDERRESP
DESCRIPTOR.message_types_by_name['QueryKnockResp'] = _QUERYKNOCKRESP
DESCRIPTOR.message_types_by_name['SubTradeMsgReq'] = _SUBTRADEMSGREQ
DESCRIPTOR.message_types_by_name['SubTradeMsgResp'] = _SUBTRADEMSGRESP
DESCRIPTOR.message_types_by_name['QueryInstrumentResp'] = _QUERYINSTRUMENTRESP
DESCRIPTOR.message_types_by_name['ErrNotify'] = _ERRNOTIFY
DESCRIPTOR.message_types_by_name['FutureOrderReq'] = _FUTUREORDERREQ
DESCRIPTOR.message_types_by_name['FutureWithdrawReq'] = _FUTUREWITHDRAWREQ
DESCRIPTOR.message_types_by_name['FutureOrderResp'] = _FUTUREORDERRESP
DESCRIPTOR.message_types_by_name['PushOrder'] = _PUSHORDER
DESCRIPTOR.message_types_by_name['PushKnock'] = _PUSHKNOCK
DESCRIPTOR.message_types_by_name['PushPosition'] = _PUSHPOSITION
DESCRIPTOR.message_types_by_name['PushInstrument'] = _PUSHINSTRUMENT

QueryAssetResp = _reflection.GeneratedProtocolMessageType('QueryAssetResp', (_message.Message,), dict(
  DESCRIPTOR = _QUERYASSETRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryAssetResp)
  ))
_sym_db.RegisterMessage(QueryAssetResp)

QueryPositionReq = _reflection.GeneratedProtocolMessageType('QueryPositionReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPOSITIONREQ,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryPositionReq)
  ))
_sym_db.RegisterMessage(QueryPositionReq)

QueryPositionResp = _reflection.GeneratedProtocolMessageType('QueryPositionResp', (_message.Message,), dict(
  DESCRIPTOR = _QUERYPOSITIONRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryPositionResp)
  ))
_sym_db.RegisterMessage(QueryPositionResp)

QueryOrderKnockReq = _reflection.GeneratedProtocolMessageType('QueryOrderKnockReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYORDERKNOCKREQ,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryOrderKnockReq)
  ))
_sym_db.RegisterMessage(QueryOrderKnockReq)

QueryOrderResp = _reflection.GeneratedProtocolMessageType('QueryOrderResp', (_message.Message,), dict(
  DESCRIPTOR = _QUERYORDERRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryOrderResp)
  ))
_sym_db.RegisterMessage(QueryOrderResp)

QueryKnockResp = _reflection.GeneratedProtocolMessageType('QueryKnockResp', (_message.Message,), dict(
  DESCRIPTOR = _QUERYKNOCKRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryKnockResp)
  ))
_sym_db.RegisterMessage(QueryKnockResp)

SubTradeMsgReq = _reflection.GeneratedProtocolMessageType('SubTradeMsgReq', (_message.Message,), dict(
  DESCRIPTOR = _SUBTRADEMSGREQ,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.SubTradeMsgReq)
  ))
_sym_db.RegisterMessage(SubTradeMsgReq)

SubTradeMsgResp = _reflection.GeneratedProtocolMessageType('SubTradeMsgResp', (_message.Message,), dict(
  DESCRIPTOR = _SUBTRADEMSGRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.SubTradeMsgResp)
  ))
_sym_db.RegisterMessage(SubTradeMsgResp)

QueryInstrumentResp = _reflection.GeneratedProtocolMessageType('QueryInstrumentResp', (_message.Message,), dict(
  DESCRIPTOR = _QUERYINSTRUMENTRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.QueryInstrumentResp)
  ))
_sym_db.RegisterMessage(QueryInstrumentResp)

ErrNotify = _reflection.GeneratedProtocolMessageType('ErrNotify', (_message.Message,), dict(
  DESCRIPTOR = _ERRNOTIFY,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.ErrNotify)
  ))
_sym_db.RegisterMessage(ErrNotify)

FutureOrderReq = _reflection.GeneratedProtocolMessageType('FutureOrderReq', (_message.Message,), dict(
  DESCRIPTOR = _FUTUREORDERREQ,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.FutureOrderReq)
  ))
_sym_db.RegisterMessage(FutureOrderReq)

FutureWithdrawReq = _reflection.GeneratedProtocolMessageType('FutureWithdrawReq', (_message.Message,), dict(
  DESCRIPTOR = _FUTUREWITHDRAWREQ,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.FutureWithdrawReq)
  ))
_sym_db.RegisterMessage(FutureWithdrawReq)

FutureOrderResp = _reflection.GeneratedProtocolMessageType('FutureOrderResp', (_message.Message,), dict(
  DESCRIPTOR = _FUTUREORDERRESP,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.FutureOrderResp)
  ))
_sym_db.RegisterMessage(FutureOrderResp)

PushOrder = _reflection.GeneratedProtocolMessageType('PushOrder', (_message.Message,), dict(
  DESCRIPTOR = _PUSHORDER,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.PushOrder)
  ))
_sym_db.RegisterMessage(PushOrder)

PushKnock = _reflection.GeneratedProtocolMessageType('PushKnock', (_message.Message,), dict(
  DESCRIPTOR = _PUSHKNOCK,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.PushKnock)
  ))
_sym_db.RegisterMessage(PushKnock)

PushPosition = _reflection.GeneratedProtocolMessageType('PushPosition', (_message.Message,), dict(
  DESCRIPTOR = _PUSHPOSITION,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.PushPosition)
  ))
_sym_db.RegisterMessage(PushPosition)

PushInstrument = _reflection.GeneratedProtocolMessageType('PushInstrument', (_message.Message,), dict(
  DESCRIPTOR = _PUSHINSTRUMENT,
  __module__ = 'future_trade_pb2'
  # @@protoc_insertion_point(class_scope:future_trade.PushInstrument)
  ))
_sym_db.RegisterMessage(PushInstrument)


# @@protoc_insertion_point(module_scope)
