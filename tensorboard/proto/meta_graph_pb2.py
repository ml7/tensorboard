# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/proto/meta_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tensorboard.proto import graph_pb2 as tensorboard_dot_proto_dot_graph__pb2
from tensorboard.proto import op_def_pb2 as tensorboard_dot_proto_dot_op__def__pb2
from tensorboard.proto import tensor_shape_pb2 as tensorboard_dot_proto_dot_tensor__shape__pb2
from tensorboard.proto import types_pb2 as tensorboard_dot_proto_dot_types__pb2
from tensorboard.proto import saver_pb2 as tensorboard_dot_proto_dot_saver__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/proto/meta_graph.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_pb=_b('\n\"tensorboard/proto/meta_graph.proto\x12\x0btensorboard\x1a\x19google/protobuf/any.proto\x1a\x1dtensorboard/proto/graph.proto\x1a\x1etensorboard/proto/op_def.proto\x1a$tensorboard/proto/tensor_shape.proto\x1a\x1dtensorboard/proto/types.proto\x1a\x1dtensorboard/proto/saver.proto\"\xec\x05\n\x0cMetaGraphDef\x12<\n\rmeta_info_def\x18\x01 \x01(\x0b\x32%.tensorboard.MetaGraphDef.MetaInfoDef\x12(\n\tgraph_def\x18\x02 \x01(\x0b\x32\x15.tensorboard.GraphDef\x12(\n\tsaver_def\x18\x03 \x01(\x0b\x32\x15.tensorboard.SaverDef\x12\x44\n\x0e\x63ollection_def\x18\x04 \x03(\x0b\x32,.tensorboard.MetaGraphDef.CollectionDefEntry\x12\x42\n\rsignature_def\x18\x05 \x03(\x0b\x32+.tensorboard.MetaGraphDef.SignatureDefEntry\x12\x31\n\x0e\x61sset_file_def\x18\x06 \x03(\x0b\x32\x19.tensorboard.AssetFileDef\x1a\xea\x01\n\x0bMetaInfoDef\x12\x1a\n\x12meta_graph_version\x18\x01 \x01(\t\x12-\n\x10stripped_op_list\x18\x02 \x01(\x0b\x32\x13.tensorboard.OpList\x12&\n\x08\x61ny_info\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x1a\n\x12tensorflow_version\x18\x05 \x01(\t\x12\x1e\n\x16tensorflow_git_version\x18\x06 \x01(\t\x12\x1e\n\x16stripped_default_attrs\x18\x07 \x01(\x08\x1aP\n\x12\x43ollectionDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.tensorboard.CollectionDef:\x02\x38\x01\x1aN\n\x11SignatureDefEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.tensorboard.SignatureDef:\x02\x38\x01\"\xe4\x03\n\rCollectionDef\x12\x38\n\tnode_list\x18\x01 \x01(\x0b\x32#.tensorboard.CollectionDef.NodeListH\x00\x12:\n\nbytes_list\x18\x02 \x01(\x0b\x32$.tensorboard.CollectionDef.BytesListH\x00\x12:\n\nint64_list\x18\x03 \x01(\x0b\x32$.tensorboard.CollectionDef.Int64ListH\x00\x12:\n\nfloat_list\x18\x04 \x01(\x0b\x32$.tensorboard.CollectionDef.FloatListH\x00\x12\x36\n\x08\x61ny_list\x18\x05 \x01(\x0b\x32\".tensorboard.CollectionDef.AnyListH\x00\x1a\x19\n\x08NodeList\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1a\n\tBytesList\x12\r\n\x05value\x18\x01 \x03(\x0c\x1a\x1e\n\tInt64List\x12\x11\n\x05value\x18\x01 \x03(\x03\x42\x02\x10\x01\x1a\x1e\n\tFloatList\x12\x11\n\x05value\x18\x01 \x03(\x02\x42\x02\x10\x01\x1a.\n\x07\x41nyList\x12#\n\x05value\x18\x01 \x03(\x0b\x32\x14.google.protobuf.AnyB\x06\n\x04kind\"\xa3\x02\n\nTensorInfo\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x37\n\ncoo_sparse\x18\x04 \x01(\x0b\x32!.tensorboard.TensorInfo.CooSparseH\x00\x12$\n\x05\x64type\x18\x02 \x01(\x0e\x32\x15.tensorboard.DataType\x12\x33\n\x0ctensor_shape\x18\x03 \x01(\x0b\x32\x1d.tensorboard.TensorShapeProto\x1a\x65\n\tCooSparse\x12\x1a\n\x12values_tensor_name\x18\x01 \x01(\t\x12\x1b\n\x13indices_tensor_name\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65nse_shape_tensor_name\x18\x03 \x01(\tB\n\n\x08\x65ncoding\"\xa4\x02\n\x0cSignatureDef\x12\x35\n\x06inputs\x18\x01 \x03(\x0b\x32%.tensorboard.SignatureDef.InputsEntry\x12\x37\n\x07outputs\x18\x02 \x03(\x0b\x32&.tensorboard.SignatureDef.OutputsEntry\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x1a\x46\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorboard.TensorInfo:\x02\x38\x01\x1aG\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.tensorboard.TensorInfo:\x02\x38\x01\"N\n\x0c\x41ssetFileDef\x12,\n\x0btensor_info\x18\x01 \x01(\x0b\x32\x17.tensorboard.TensorInfo\x12\x10\n\x08\x66ilename\x18\x02 \x01(\tBn\n\x18org.tensorflow.frameworkB\x0fMetaGraphProtosP\x01Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_graph__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_op__def__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_tensor__shape__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_types__pb2.DESCRIPTOR,tensorboard_dot_proto_dot_saver__pb2.DESCRIPTOR,])




_METAGRAPHDEF_METAINFODEF = _descriptor.Descriptor(
  name='MetaInfoDef',
  full_name='tensorboard.MetaGraphDef.MetaInfoDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_graph_version', full_name='tensorboard.MetaGraphDef.MetaInfoDef.meta_graph_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stripped_op_list', full_name='tensorboard.MetaGraphDef.MetaInfoDef.stripped_op_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='any_info', full_name='tensorboard.MetaGraphDef.MetaInfoDef.any_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='tensorboard.MetaGraphDef.MetaInfoDef.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensorflow_version', full_name='tensorboard.MetaGraphDef.MetaInfoDef.tensorflow_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensorflow_git_version', full_name='tensorboard.MetaGraphDef.MetaInfoDef.tensorflow_git_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stripped_default_attrs', full_name='tensorboard.MetaGraphDef.MetaInfoDef.stripped_default_attrs', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=594,
  serialized_end=828,
)

_METAGRAPHDEF_COLLECTIONDEFENTRY = _descriptor.Descriptor(
  name='CollectionDefEntry',
  full_name='tensorboard.MetaGraphDef.CollectionDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.MetaGraphDef.CollectionDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.MetaGraphDef.CollectionDefEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=830,
  serialized_end=910,
)

_METAGRAPHDEF_SIGNATUREDEFENTRY = _descriptor.Descriptor(
  name='SignatureDefEntry',
  full_name='tensorboard.MetaGraphDef.SignatureDefEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.MetaGraphDef.SignatureDefEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.MetaGraphDef.SignatureDefEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=912,
  serialized_end=990,
)

_METAGRAPHDEF = _descriptor.Descriptor(
  name='MetaGraphDef',
  full_name='tensorboard.MetaGraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_info_def', full_name='tensorboard.MetaGraphDef.meta_info_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='tensorboard.MetaGraphDef.graph_def', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saver_def', full_name='tensorboard.MetaGraphDef.saver_def', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_def', full_name='tensorboard.MetaGraphDef.collection_def', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_def', full_name='tensorboard.MetaGraphDef.signature_def', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_file_def', full_name='tensorboard.MetaGraphDef.asset_file_def', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METAGRAPHDEF_METAINFODEF, _METAGRAPHDEF_COLLECTIONDEFENTRY, _METAGRAPHDEF_SIGNATUREDEFENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=990,
)


_COLLECTIONDEF_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='tensorboard.CollectionDef.NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CollectionDef.NodeList.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1304,
  serialized_end=1329,
)

_COLLECTIONDEF_BYTESLIST = _descriptor.Descriptor(
  name='BytesList',
  full_name='tensorboard.CollectionDef.BytesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CollectionDef.BytesList.value', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=1331,
  serialized_end=1357,
)

_COLLECTIONDEF_INT64LIST = _descriptor.Descriptor(
  name='Int64List',
  full_name='tensorboard.CollectionDef.Int64List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CollectionDef.Int64List.value', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
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
  serialized_start=1359,
  serialized_end=1389,
)

_COLLECTIONDEF_FLOATLIST = _descriptor.Descriptor(
  name='FloatList',
  full_name='tensorboard.CollectionDef.FloatList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CollectionDef.FloatList.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
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
  serialized_start=1391,
  serialized_end=1421,
)

_COLLECTIONDEF_ANYLIST = _descriptor.Descriptor(
  name='AnyList',
  full_name='tensorboard.CollectionDef.AnyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.CollectionDef.AnyList.value', index=0,
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
  serialized_start=1423,
  serialized_end=1469,
)

_COLLECTIONDEF = _descriptor.Descriptor(
  name='CollectionDef',
  full_name='tensorboard.CollectionDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_list', full_name='tensorboard.CollectionDef.node_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_list', full_name='tensorboard.CollectionDef.bytes_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_list', full_name='tensorboard.CollectionDef.int64_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_list', full_name='tensorboard.CollectionDef.float_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='any_list', full_name='tensorboard.CollectionDef.any_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTIONDEF_NODELIST, _COLLECTIONDEF_BYTESLIST, _COLLECTIONDEF_INT64LIST, _COLLECTIONDEF_FLOATLIST, _COLLECTIONDEF_ANYLIST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='tensorboard.CollectionDef.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=993,
  serialized_end=1477,
)


_TENSORINFO_COOSPARSE = _descriptor.Descriptor(
  name='CooSparse',
  full_name='tensorboard.TensorInfo.CooSparse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values_tensor_name', full_name='tensorboard.TensorInfo.CooSparse.values_tensor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indices_tensor_name', full_name='tensorboard.TensorInfo.CooSparse.indices_tensor_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dense_shape_tensor_name', full_name='tensorboard.TensorInfo.CooSparse.dense_shape_tensor_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1658,
  serialized_end=1759,
)

_TENSORINFO = _descriptor.Descriptor(
  name='TensorInfo',
  full_name='tensorboard.TensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorboard.TensorInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coo_sparse', full_name='tensorboard.TensorInfo.coo_sparse', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorboard.TensorInfo.dtype', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='tensorboard.TensorInfo.tensor_shape', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TENSORINFO_COOSPARSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='encoding', full_name='tensorboard.TensorInfo.encoding',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1480,
  serialized_end=1771,
)


_SIGNATUREDEF_INPUTSENTRY = _descriptor.Descriptor(
  name='InputsEntry',
  full_name='tensorboard.SignatureDef.InputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.SignatureDef.InputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.SignatureDef.InputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1923,
  serialized_end=1993,
)

_SIGNATUREDEF_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='tensorboard.SignatureDef.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.SignatureDef.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.SignatureDef.OutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1995,
  serialized_end=2066,
)

_SIGNATUREDEF = _descriptor.Descriptor(
  name='SignatureDef',
  full_name='tensorboard.SignatureDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tensorboard.SignatureDef.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tensorboard.SignatureDef.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='tensorboard.SignatureDef.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREDEF_INPUTSENTRY, _SIGNATUREDEF_OUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1774,
  serialized_end=2066,
)


_ASSETFILEDEF = _descriptor.Descriptor(
  name='AssetFileDef',
  full_name='tensorboard.AssetFileDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_info', full_name='tensorboard.AssetFileDef.tensor_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorboard.AssetFileDef.filename', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2068,
  serialized_end=2146,
)

_METAGRAPHDEF_METAINFODEF.fields_by_name['stripped_op_list'].message_type = tensorboard_dot_proto_dot_op__def__pb2._OPLIST
_METAGRAPHDEF_METAINFODEF.fields_by_name['any_info'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_METAGRAPHDEF_METAINFODEF.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.fields_by_name['value'].message_type = _COLLECTIONDEF
_METAGRAPHDEF_COLLECTIONDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.fields_by_name['value'].message_type = _SIGNATUREDEF
_METAGRAPHDEF_SIGNATUREDEFENTRY.containing_type = _METAGRAPHDEF
_METAGRAPHDEF.fields_by_name['meta_info_def'].message_type = _METAGRAPHDEF_METAINFODEF
_METAGRAPHDEF.fields_by_name['graph_def'].message_type = tensorboard_dot_proto_dot_graph__pb2._GRAPHDEF
_METAGRAPHDEF.fields_by_name['saver_def'].message_type = tensorboard_dot_proto_dot_saver__pb2._SAVERDEF
_METAGRAPHDEF.fields_by_name['collection_def'].message_type = _METAGRAPHDEF_COLLECTIONDEFENTRY
_METAGRAPHDEF.fields_by_name['signature_def'].message_type = _METAGRAPHDEF_SIGNATUREDEFENTRY
_METAGRAPHDEF.fields_by_name['asset_file_def'].message_type = _ASSETFILEDEF
_COLLECTIONDEF_NODELIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_BYTESLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_INT64LIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_FLOATLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF_ANYLIST.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_COLLECTIONDEF_ANYLIST.containing_type = _COLLECTIONDEF
_COLLECTIONDEF.fields_by_name['node_list'].message_type = _COLLECTIONDEF_NODELIST
_COLLECTIONDEF.fields_by_name['bytes_list'].message_type = _COLLECTIONDEF_BYTESLIST
_COLLECTIONDEF.fields_by_name['int64_list'].message_type = _COLLECTIONDEF_INT64LIST
_COLLECTIONDEF.fields_by_name['float_list'].message_type = _COLLECTIONDEF_FLOATLIST
_COLLECTIONDEF.fields_by_name['any_list'].message_type = _COLLECTIONDEF_ANYLIST
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['node_list'])
_COLLECTIONDEF.fields_by_name['node_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['bytes_list'])
_COLLECTIONDEF.fields_by_name['bytes_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['int64_list'])
_COLLECTIONDEF.fields_by_name['int64_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['float_list'])
_COLLECTIONDEF.fields_by_name['float_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_COLLECTIONDEF.oneofs_by_name['kind'].fields.append(
  _COLLECTIONDEF.fields_by_name['any_list'])
_COLLECTIONDEF.fields_by_name['any_list'].containing_oneof = _COLLECTIONDEF.oneofs_by_name['kind']
_TENSORINFO_COOSPARSE.containing_type = _TENSORINFO
_TENSORINFO.fields_by_name['coo_sparse'].message_type = _TENSORINFO_COOSPARSE
_TENSORINFO.fields_by_name['dtype'].enum_type = tensorboard_dot_proto_dot_types__pb2._DATATYPE
_TENSORINFO.fields_by_name['tensor_shape'].message_type = tensorboard_dot_proto_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_TENSORINFO.oneofs_by_name['encoding'].fields.append(
  _TENSORINFO.fields_by_name['name'])
_TENSORINFO.fields_by_name['name'].containing_oneof = _TENSORINFO.oneofs_by_name['encoding']
_TENSORINFO.oneofs_by_name['encoding'].fields.append(
  _TENSORINFO.fields_by_name['coo_sparse'])
_TENSORINFO.fields_by_name['coo_sparse'].containing_oneof = _TENSORINFO.oneofs_by_name['encoding']
_SIGNATUREDEF_INPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_INPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF_OUTPUTSENTRY.fields_by_name['value'].message_type = _TENSORINFO
_SIGNATUREDEF_OUTPUTSENTRY.containing_type = _SIGNATUREDEF
_SIGNATUREDEF.fields_by_name['inputs'].message_type = _SIGNATUREDEF_INPUTSENTRY
_SIGNATUREDEF.fields_by_name['outputs'].message_type = _SIGNATUREDEF_OUTPUTSENTRY
_ASSETFILEDEF.fields_by_name['tensor_info'].message_type = _TENSORINFO
DESCRIPTOR.message_types_by_name['MetaGraphDef'] = _METAGRAPHDEF
DESCRIPTOR.message_types_by_name['CollectionDef'] = _COLLECTIONDEF
DESCRIPTOR.message_types_by_name['TensorInfo'] = _TENSORINFO
DESCRIPTOR.message_types_by_name['SignatureDef'] = _SIGNATUREDEF
DESCRIPTOR.message_types_by_name['AssetFileDef'] = _ASSETFILEDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetaGraphDef = _reflection.GeneratedProtocolMessageType('MetaGraphDef', (_message.Message,), dict(

  MetaInfoDef = _reflection.GeneratedProtocolMessageType('MetaInfoDef', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_METAINFODEF,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.MetaGraphDef.MetaInfoDef)
    ))
  ,

  CollectionDefEntry = _reflection.GeneratedProtocolMessageType('CollectionDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_COLLECTIONDEFENTRY,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.MetaGraphDef.CollectionDefEntry)
    ))
  ,

  SignatureDefEntry = _reflection.GeneratedProtocolMessageType('SignatureDefEntry', (_message.Message,), dict(
    DESCRIPTOR = _METAGRAPHDEF_SIGNATUREDEFENTRY,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.MetaGraphDef.SignatureDefEntry)
    ))
  ,
  DESCRIPTOR = _METAGRAPHDEF,
  __module__ = 'tensorboard.proto.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.MetaGraphDef)
  ))
_sym_db.RegisterMessage(MetaGraphDef)
_sym_db.RegisterMessage(MetaGraphDef.MetaInfoDef)
_sym_db.RegisterMessage(MetaGraphDef.CollectionDefEntry)
_sym_db.RegisterMessage(MetaGraphDef.SignatureDefEntry)

CollectionDef = _reflection.GeneratedProtocolMessageType('CollectionDef', (_message.Message,), dict(

  NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_NODELIST,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef.NodeList)
    ))
  ,

  BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_BYTESLIST,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef.BytesList)
    ))
  ,

  Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_INT64LIST,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef.Int64List)
    ))
  ,

  FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_FLOATLIST,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef.FloatList)
    ))
  ,

  AnyList = _reflection.GeneratedProtocolMessageType('AnyList', (_message.Message,), dict(
    DESCRIPTOR = _COLLECTIONDEF_ANYLIST,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef.AnyList)
    ))
  ,
  DESCRIPTOR = _COLLECTIONDEF,
  __module__ = 'tensorboard.proto.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.CollectionDef)
  ))
_sym_db.RegisterMessage(CollectionDef)
_sym_db.RegisterMessage(CollectionDef.NodeList)
_sym_db.RegisterMessage(CollectionDef.BytesList)
_sym_db.RegisterMessage(CollectionDef.Int64List)
_sym_db.RegisterMessage(CollectionDef.FloatList)
_sym_db.RegisterMessage(CollectionDef.AnyList)

TensorInfo = _reflection.GeneratedProtocolMessageType('TensorInfo', (_message.Message,), dict(

  CooSparse = _reflection.GeneratedProtocolMessageType('CooSparse', (_message.Message,), dict(
    DESCRIPTOR = _TENSORINFO_COOSPARSE,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.TensorInfo.CooSparse)
    ))
  ,
  DESCRIPTOR = _TENSORINFO,
  __module__ = 'tensorboard.proto.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.TensorInfo)
  ))
_sym_db.RegisterMessage(TensorInfo)
_sym_db.RegisterMessage(TensorInfo.CooSparse)

SignatureDef = _reflection.GeneratedProtocolMessageType('SignatureDef', (_message.Message,), dict(

  InputsEntry = _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_INPUTSENTRY,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.SignatureDef.InputsEntry)
    ))
  ,

  OutputsEntry = _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREDEF_OUTPUTSENTRY,
    __module__ = 'tensorboard.proto.meta_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.SignatureDef.OutputsEntry)
    ))
  ,
  DESCRIPTOR = _SIGNATUREDEF,
  __module__ = 'tensorboard.proto.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.SignatureDef)
  ))
_sym_db.RegisterMessage(SignatureDef)
_sym_db.RegisterMessage(SignatureDef.InputsEntry)
_sym_db.RegisterMessage(SignatureDef.OutputsEntry)

AssetFileDef = _reflection.GeneratedProtocolMessageType('AssetFileDef', (_message.Message,), dict(
  DESCRIPTOR = _ASSETFILEDEF,
  __module__ = 'tensorboard.proto.meta_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.AssetFileDef)
  ))
_sym_db.RegisterMessage(AssetFileDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\017MetaGraphProtosP\001Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\370\001\001'))
_METAGRAPHDEF_COLLECTIONDEFENTRY.has_options = True
_METAGRAPHDEF_COLLECTIONDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_METAGRAPHDEF_SIGNATUREDEFENTRY.has_options = True
_METAGRAPHDEF_SIGNATUREDEFENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_COLLECTIONDEF_INT64LIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_INT64LIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_COLLECTIONDEF_FLOATLIST.fields_by_name['value'].has_options = True
_COLLECTIONDEF_FLOATLIST.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_SIGNATUREDEF_INPUTSENTRY.has_options = True
_SIGNATUREDEF_INPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SIGNATUREDEF_OUTPUTSENTRY.has_options = True
_SIGNATUREDEF_OUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
