from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags_to_stream(self, StreamName: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_stream(self, StreamName: str, ShardCount: int) -> None:
        pass

    # pylint: disable=arguments-differ
    def decrease_stream_retention_period(
        self, StreamName: str, RetentionPeriodHours: int
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_stream(
        self, StreamName: str, EnforceConsumerDeletion: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def deregister_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_limits(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream(
        self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_stream_summary(self, StreamName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_enhanced_monitoring(
        self, StreamName: str, ShardLevelMetrics: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_enhanced_monitoring(
        self, StreamName: str, ShardLevelMetrics: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_records(self, ShardIterator: str, Limit: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_shard_iterator(
        self,
        StreamName: str,
        ShardId: str,
        ShardIteratorType: str,
        StartingSequenceNumber: str = None,
        Timestamp: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def increase_stream_retention_period(
        self, StreamName: str, RetentionPeriodHours: int
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def list_shards(
        self,
        StreamName: str = None,
        NextToken: str = None,
        ExclusiveStartShardId: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stream_consumers(
        self,
        StreamARN: str,
        NextToken: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_streams(
        self, Limit: int = None, ExclusiveStartStreamName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_stream(
        self, StreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def merge_shards(
        self, StreamName: str, ShardToMerge: str, AdjacentShardToMerge: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_record(
        self,
        StreamName: str,
        Data: bytes,
        PartitionKey: str,
        ExplicitHashKey: str = None,
        SequenceNumberForOrdering: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_records(self, Records: List[Any], StreamName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_stream_consumer(
        self, StreamARN: str, ConsumerName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_stream(self, StreamName: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def split_shard(
        self, StreamName: str, ShardToSplit: str, NewStartingHashKey: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def start_stream_encryption(
        self, StreamName: str, EncryptionType: str, KeyId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_stream_encryption(
        self, StreamName: str, EncryptionType: str, KeyId: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def subscribe_to_shard(
        self, ConsumerARN: str, ShardId: str, StartingPosition: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_shard_count(
        self, StreamName: str, TargetShardCount: int, ScalingType: str
    ) -> Dict[str, Any]:
        pass
