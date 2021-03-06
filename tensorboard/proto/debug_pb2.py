# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/proto/debug.proto

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
  name='tensorboard/proto/debug.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_pb=_b('\n\x1dtensorboard/proto/debug.proto\x12\x0btensorboard\"\x8e\x01\n\x10\x44\x65\x62ugTensorWatch\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x13\n\x0boutput_slot\x18\x02 \x01(\x05\x12\x11\n\tdebug_ops\x18\x03 \x03(\t\x12\x12\n\ndebug_urls\x18\x04 \x03(\t\x12+\n#tolerate_debug_op_creation_failures\x18\x05 \x01(\x08\"c\n\x0c\x44\x65\x62ugOptions\x12>\n\x17\x64\x65\x62ug_tensor_watch_opts\x18\x04 \x03(\x0b\x32\x1d.tensorboard.DebugTensorWatch\x12\x13\n\x0bglobal_step\x18\n \x01(\x03\"j\n\x12\x44\x65\x62uggedSourceFile\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x11\n\tfile_path\x18\x02 \x01(\t\x12\x15\n\rlast_modified\x18\x03 \x01(\x03\x12\r\n\x05\x62ytes\x18\x04 \x01(\x03\x12\r\n\x05lines\x18\x05 \x03(\t\"L\n\x13\x44\x65\x62uggedSourceFiles\x12\x35\n\x0csource_files\x18\x01 \x03(\x0b\x32\x1f.tensorboard.DebuggedSourceFileBj\n\x18org.tensorflow.frameworkB\x0b\x44\x65\x62ugProtosP\x01Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\xf8\x01\x01\x62\x06proto3')
)




_DEBUGTENSORWATCH = _descriptor.Descriptor(
  name='DebugTensorWatch',
  full_name='tensorboard.DebugTensorWatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='tensorboard.DebugTensorWatch.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_slot', full_name='tensorboard.DebugTensorWatch.output_slot', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_ops', full_name='tensorboard.DebugTensorWatch.debug_ops', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_urls', full_name='tensorboard.DebugTensorWatch.debug_urls', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tolerate_debug_op_creation_failures', full_name='tensorboard.DebugTensorWatch.tolerate_debug_op_creation_failures', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=189,
)


_DEBUGOPTIONS = _descriptor.Descriptor(
  name='DebugOptions',
  full_name='tensorboard.DebugOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug_tensor_watch_opts', full_name='tensorboard.DebugOptions.debug_tensor_watch_opts', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_step', full_name='tensorboard.DebugOptions.global_step', index=1,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=290,
)


_DEBUGGEDSOURCEFILE = _descriptor.Descriptor(
  name='DebuggedSourceFile',
  full_name='tensorboard.DebuggedSourceFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='tensorboard.DebuggedSourceFile.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='tensorboard.DebuggedSourceFile.file_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='tensorboard.DebuggedSourceFile.last_modified', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='tensorboard.DebuggedSourceFile.bytes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lines', full_name='tensorboard.DebuggedSourceFile.lines', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=398,
)


_DEBUGGEDSOURCEFILES = _descriptor.Descriptor(
  name='DebuggedSourceFiles',
  full_name='tensorboard.DebuggedSourceFiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_files', full_name='tensorboard.DebuggedSourceFiles.source_files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=476,
)

_DEBUGOPTIONS.fields_by_name['debug_tensor_watch_opts'].message_type = _DEBUGTENSORWATCH
_DEBUGGEDSOURCEFILES.fields_by_name['source_files'].message_type = _DEBUGGEDSOURCEFILE
DESCRIPTOR.message_types_by_name['DebugTensorWatch'] = _DEBUGTENSORWATCH
DESCRIPTOR.message_types_by_name['DebugOptions'] = _DEBUGOPTIONS
DESCRIPTOR.message_types_by_name['DebuggedSourceFile'] = _DEBUGGEDSOURCEFILE
DESCRIPTOR.message_types_by_name['DebuggedSourceFiles'] = _DEBUGGEDSOURCEFILES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebugTensorWatch = _reflection.GeneratedProtocolMessageType('DebugTensorWatch', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGTENSORWATCH,
  __module__ = 'tensorboard.proto.debug_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.DebugTensorWatch)
  ))
_sym_db.RegisterMessage(DebugTensorWatch)

DebugOptions = _reflection.GeneratedProtocolMessageType('DebugOptions', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGOPTIONS,
  __module__ = 'tensorboard.proto.debug_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.DebugOptions)
  ))
_sym_db.RegisterMessage(DebugOptions)

DebuggedSourceFile = _reflection.GeneratedProtocolMessageType('DebuggedSourceFile', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGGEDSOURCEFILE,
  __module__ = 'tensorboard.proto.debug_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.DebuggedSourceFile)
  ))
_sym_db.RegisterMessage(DebuggedSourceFile)

DebuggedSourceFiles = _reflection.GeneratedProtocolMessageType('DebuggedSourceFiles', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGGEDSOURCEFILES,
  __module__ = 'tensorboard.proto.debug_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.DebuggedSourceFiles)
  ))
_sym_db.RegisterMessage(DebuggedSourceFiles)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\013DebugProtosP\001Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\370\001\001'))
# @@protoc_insertion_point(module_scope)
