# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/proto/debug_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorboard.proto import tensor_pb2 as tensorboard_dot_proto_dot_tensor__pb2
from tensorboard.proto import tfprof_log_pb2 as tensorboard_dot_proto_dot_tfprof__log__pb2
from tensorboard.proto import debug_pb2 as tensorboard_dot_proto_dot_debug__pb2
from tensorboard.proto import event_pb2 as tensorboard_dot_proto_dot_event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/proto/debug_service.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_pb=_b('\n%tensorboard/proto/debug_service.proto\x12\x0btensorboard\x1a\x1etensorboard/proto/tensor.proto\x1a\"tensorboard/proto/tfprof_log.proto\x1a\x1dtensorboard/proto/debug.proto\x1a\x1dtensorboard/proto/event.proto\"\xe1\x02\n\nEventReply\x12J\n\x16\x64\x65\x62ug_op_state_changes\x18\x01 \x03(\x0b\x32*.tensorboard.EventReply.DebugOpStateChange\x12(\n\x06tensor\x18\x02 \x01(\x0b\x32\x18.tensorboard.TensorProto\x1a\xdc\x01\n\x12\x44\x65\x62ugOpStateChange\x12?\n\x05state\x18\x01 \x01(\x0e\x32\x30.tensorboard.EventReply.DebugOpStateChange.State\x12\x11\n\tnode_name\x18\x02 \x01(\t\x12\x13\n\x0boutput_slot\x18\x03 \x01(\x05\x12\x10\n\x08\x64\x65\x62ug_op\x18\x04 \x01(\t\"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\r\n\tREAD_ONLY\x10\x02\x12\x0e\n\nREAD_WRITE\x10\x03\"\x9d\x03\n\rCallTraceback\x12\x36\n\tcall_type\x18\x01 \x01(\x0e\x32#.tensorboard.CallTraceback.CallType\x12\x10\n\x08\x63\x61ll_key\x18\x02 \x01(\t\x12*\n\x0corigin_stack\x18\x03 \x01(\x0b\x32\x14.tensorboard.CodeDef\x12M\n\x13origin_id_to_string\x18\x04 \x03(\x0b\x32\x30.tensorboard.CallTraceback.OriginIdToStringEntry\x12\x30\n\x0fgraph_traceback\x18\x05 \x01(\x0b\x32\x17.tensorboard.OpLogProto\x12\x15\n\rgraph_version\x18\x06 \x01(\x03\x1a\x37\n\x15OriginIdToStringEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x08\x43\x61llType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x13\n\x0fGRAPH_EXECUTION\x10\x01\x12\x13\n\x0f\x45\x41GER_EXECUTION\x10\x02\x32\xe3\x01\n\rEventListener\x12=\n\nSendEvents\x12\x12.tensorboard.Event\x1a\x17.tensorboard.EventReply(\x01\x30\x01\x12\x45\n\x0eSendTracebacks\x12\x1a.tensorboard.CallTraceback\x1a\x17.tensorboard.EventReply\x12L\n\x0fSendSourceFiles\x12 .tensorboard.DebuggedSourceFiles\x1a\x17.tensorboard.EventReplyb\x06proto3')
  ,
  dependencies=[tensorboard_dot_proto_dot_tensor__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_tfprof__log__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_debug__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_event__pb2.DESCRIPTOR,])



_EVENTREPLY_DEBUGOPSTATECHANGE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='tensorboard.EventReply.DebugOpStateChange.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_ONLY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=463,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_EVENTREPLY_DEBUGOPSTATECHANGE_STATE)

_CALLTRACEBACK_CALLTYPE = _descriptor.EnumDescriptor(
  name='CallType',
  full_name='tensorboard.CallTraceback.CallType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAPH_EXECUTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EAGER_EXECUTION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=885,
  serialized_end=954,
)
_sym_db.RegisterEnumDescriptor(_CALLTRACEBACK_CALLTYPE)


_EVENTREPLY_DEBUGOPSTATECHANGE = _descriptor.Descriptor(
  name='DebugOpStateChange',
  full_name='tensorboard.EventReply.DebugOpStateChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='tensorboard.EventReply.DebugOpStateChange.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='tensorboard.EventReply.DebugOpStateChange.node_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_slot', full_name='tensorboard.EventReply.DebugOpStateChange.output_slot', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_op', full_name='tensorboard.EventReply.DebugOpStateChange.debug_op', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENTREPLY_DEBUGOPSTATECHANGE_STATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=538,
)

_EVENTREPLY = _descriptor.Descriptor(
  name='EventReply',
  full_name='tensorboard.EventReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug_op_state_changes', full_name='tensorboard.EventReply.debug_op_state_changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tensorboard.EventReply.tensor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENTREPLY_DEBUGOPSTATECHANGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=538,
)


_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY = _descriptor.Descriptor(
  name='OriginIdToStringEntry',
  full_name='tensorboard.CallTraceback.OriginIdToStringEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.CallTraceback.OriginIdToStringEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CallTraceback.OriginIdToStringEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=883,
)

_CALLTRACEBACK = _descriptor.Descriptor(
  name='CallTraceback',
  full_name='tensorboard.CallTraceback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_type', full_name='tensorboard.CallTraceback.call_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='call_key', full_name='tensorboard.CallTraceback.call_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin_stack', full_name='tensorboard.CallTraceback.origin_stack', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin_id_to_string', full_name='tensorboard.CallTraceback.origin_id_to_string', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_traceback', full_name='tensorboard.CallTraceback.graph_traceback', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_version', full_name='tensorboard.CallTraceback.graph_version', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY, ],
  enum_types=[
    _CALLTRACEBACK_CALLTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=954,
)

_EVENTREPLY_DEBUGOPSTATECHANGE.fields_by_name['state'].enum_type = _EVENTREPLY_DEBUGOPSTATECHANGE_STATE
_EVENTREPLY_DEBUGOPSTATECHANGE.containing_type = _EVENTREPLY
_EVENTREPLY_DEBUGOPSTATECHANGE_STATE.containing_type = _EVENTREPLY_DEBUGOPSTATECHANGE
_EVENTREPLY.fields_by_name['debug_op_state_changes'].message_type = _EVENTREPLY_DEBUGOPSTATECHANGE
_EVENTREPLY.fields_by_name['tensor'].message_type = tensorboard_dot_proto_dot_tensor__pb2._TENSORPROTO
_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY.containing_type = _CALLTRACEBACK
_CALLTRACEBACK.fields_by_name['call_type'].enum_type = _CALLTRACEBACK_CALLTYPE
_CALLTRACEBACK.fields_by_name['origin_stack'].message_type = tensorboard_dot_proto_dot_tfprof__log__pb2._CODEDEF
_CALLTRACEBACK.fields_by_name['origin_id_to_string'].message_type = _CALLTRACEBACK_ORIGINIDTOSTRINGENTRY
_CALLTRACEBACK.fields_by_name['graph_traceback'].message_type = tensorboard_dot_proto_dot_tfprof__log__pb2._OPLOGPROTO
_CALLTRACEBACK_CALLTYPE.containing_type = _CALLTRACEBACK
DESCRIPTOR.message_types_by_name['EventReply'] = _EVENTREPLY
DESCRIPTOR.message_types_by_name['CallTraceback'] = _CALLTRACEBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventReply = _reflection.GeneratedProtocolMessageType('EventReply', (_message.Message,), dict(

  DebugOpStateChange = _reflection.GeneratedProtocolMessageType('DebugOpStateChange', (_message.Message,), dict(
    DESCRIPTOR = _EVENTREPLY_DEBUGOPSTATECHANGE,
    __module__ = 'tensorboard.proto.debug_service_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.EventReply.DebugOpStateChange)
    ))
  ,
  DESCRIPTOR = _EVENTREPLY,
  __module__ = 'tensorboard.proto.debug_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.EventReply)
  ))
_sym_db.RegisterMessage(EventReply)
_sym_db.RegisterMessage(EventReply.DebugOpStateChange)

CallTraceback = _reflection.GeneratedProtocolMessageType('CallTraceback', (_message.Message,), dict(

  OriginIdToStringEntry = _reflection.GeneratedProtocolMessageType('OriginIdToStringEntry', (_message.Message,), dict(
    DESCRIPTOR = _CALLTRACEBACK_ORIGINIDTOSTRINGENTRY,
    __module__ = 'tensorboard.proto.debug_service_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CallTraceback.OriginIdToStringEntry)
    ))
  ,
  DESCRIPTOR = _CALLTRACEBACK,
  __module__ = 'tensorboard.proto.debug_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.CallTraceback)
  ))
_sym_db.RegisterMessage(CallTraceback)
_sym_db.RegisterMessage(CallTraceback.OriginIdToStringEntry)


_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY.has_options = True
_CALLTRACEBACK_ORIGINIDTOSTRINGENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_EVENTLISTENER = _descriptor.ServiceDescriptor(
  name='EventListener',
  full_name='tensorboard.EventListener',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=957,
  serialized_end=1184,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendEvents',
    full_name='tensorboard.EventListener.SendEvents',
    index=0,
    containing_service=None,
    input_type=tensorboard_dot_proto_dot_event__pb2._EVENT,
    output_type=_EVENTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendTracebacks',
    full_name='tensorboard.EventListener.SendTracebacks',
    index=1,
    containing_service=None,
    input_type=_CALLTRACEBACK,
    output_type=_EVENTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendSourceFiles',
    full_name='tensorboard.EventListener.SendSourceFiles',
    index=2,
    containing_service=None,
    input_type=tensorboard_dot_proto_dot_debug__pb2._DEBUGGEDSOURCEFILES,
    output_type=_EVENTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTLISTENER)

DESCRIPTOR.services_by_name['EventListener'] = _EVENTLISTENER

# @@protoc_insertion_point(module_scope)
