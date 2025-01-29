# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: flwr/proto/serverappio.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'flwr/proto/serverappio.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import log_pb2 as flwr_dot_proto_dot_log__pb2
from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66lwr/proto/serverappio.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/log.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x18\x66lwr/proto/message.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\"!\n\x0fGetNodesRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"3\n\x10GetNodesResponse\x12\x1f\n\x05nodes\x18\x01 \x03(\x0b\x32\x10.flwr.proto.Node\"T\n\x16PushInsMessagesRequest\x12*\n\rmessages_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.Message\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\".\n\x17PushInsMessagesResponse\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t\"=\n\x16PullResMessagesRequest\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\"E\n\x17PullResMessagesResponse\x12*\n\rmessages_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.Message\"\x1c\n\x1aPullServerAppInputsRequest\"\x7f\n\x1bPullServerAppInputsResponse\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03run\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\"S\n\x1bPushServerAppOutputsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Context\"\x1e\n\x1cPushServerAppOutputsResponse2\xb1\x07\n\x0bServerAppIo\x12J\n\tCreateRun\x12\x1c.flwr.proto.CreateRunRequest\x1a\x1d.flwr.proto.CreateRunResponse\"\x00\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse\"\x00\x12Y\n\x0cPushMessages\x12\".flwr.proto.PushInsMessagesRequest\x1a#.flwr.proto.PushInsMessagesResponse\"\x00\x12Y\n\x0cPullMessages\x12\".flwr.proto.PullResMessagesRequest\x1a#.flwr.proto.PullResMessagesResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x12\x41\n\x06GetFab\x12\x19.flwr.proto.GetFabRequest\x1a\x1a.flwr.proto.GetFabResponse\"\x00\x12h\n\x13PullServerAppInputs\x12&.flwr.proto.PullServerAppInputsRequest\x1a\'.flwr.proto.PullServerAppInputsResponse\"\x00\x12k\n\x14PushServerAppOutputs\x12\'.flwr.proto.PushServerAppOutputsRequest\x1a(.flwr.proto.PushServerAppOutputsResponse\"\x00\x12\\\n\x0fUpdateRunStatus\x12\".flwr.proto.UpdateRunStatusRequest\x1a#.flwr.proto.UpdateRunStatusResponse\"\x00\x12S\n\x0cGetRunStatus\x12\x1f.flwr.proto.GetRunStatusRequest\x1a .flwr.proto.GetRunStatusResponse\"\x00\x12G\n\x08PushLogs\x12\x1b.flwr.proto.PushLogsRequest\x1a\x1c.flwr.proto.PushLogsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.serverappio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETNODESREQUEST']._serialized_start=159
  _globals['_GETNODESREQUEST']._serialized_end=192
  _globals['_GETNODESRESPONSE']._serialized_start=194
  _globals['_GETNODESRESPONSE']._serialized_end=245
  _globals['_PUSHINSMESSAGESREQUEST']._serialized_start=247
  _globals['_PUSHINSMESSAGESREQUEST']._serialized_end=331
  _globals['_PUSHINSMESSAGESRESPONSE']._serialized_start=333
  _globals['_PUSHINSMESSAGESRESPONSE']._serialized_end=379
  _globals['_PULLRESMESSAGESREQUEST']._serialized_start=381
  _globals['_PULLRESMESSAGESREQUEST']._serialized_end=442
  _globals['_PULLRESMESSAGESRESPONSE']._serialized_start=444
  _globals['_PULLRESMESSAGESRESPONSE']._serialized_end=513
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_start=515
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_end=543
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_start=545
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_end=672
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_start=674
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_end=757
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_start=759
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_end=789
  _globals['_SERVERAPPIO']._serialized_start=792
  _globals['_SERVERAPPIO']._serialized_end=1737
# @@protoc_insertion_point(module_scope)
