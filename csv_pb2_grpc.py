# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import csv_pb2 as csv__pb2


class csvEngineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_next_row = channel.unary_unary(
                '/csvEnginePackage.csvEngine/get_next_row',
                request_serializer=csv__pb2.voidNoParam.SerializeToString,
                response_deserializer=csv__pb2.dataSetRow.FromString,
                )


class csvEngineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_next_row(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_csvEngineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_next_row': grpc.unary_unary_rpc_method_handler(
                    servicer.get_next_row,
                    request_deserializer=csv__pb2.voidNoParam.FromString,
                    response_serializer=csv__pb2.dataSetRow.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'csvEnginePackage.csvEngine', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class csvEngine(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_next_row(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/csvEnginePackage.csvEngine/get_next_row',
            csv__pb2.voidNoParam.SerializeToString,
            csv__pb2.dataSetRow.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
