from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_stream(
        self,
        StreamName: str,
        Tags: Dict,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_stream(
        self,
        StreamName: str,
        ShardCount: int,
    ):
        pass


    def decrease_stream_retention_period(
        self,
        StreamName: str,
        RetentionPeriodHours: int,
    ):
        pass


    def delete_stream(
        self,
        StreamName: str,
        EnforceConsumerDeletion: Optional[bool] = None,
    ):
        pass


    def deregister_stream_consumer(
        self,
        StreamARN: Optional[str] = None,
        ConsumerName: Optional[str] = None,
        ConsumerARN: Optional[str] = None,
    ):
        pass


    def describe_limits(
        self,
    ) -> Dict:
        pass


    def describe_stream(
        self,
        StreamName: str,
        Limit: Optional[int] = None,
        ExclusiveStartShardId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stream_consumer(
        self,
        StreamARN: Optional[str] = None,
        ConsumerName: Optional[str] = None,
        ConsumerARN: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_stream_summary(
        self,
        StreamName: str,
    ) -> Dict:
        pass


    def disable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List,
    ) -> Dict:
        pass


    def enable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_records(
        self,
        ShardIterator: str,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def get_shard_iterator(
        self,
        StreamName: str,
        ShardId: str,
        ShardIteratorType: str,
        StartingSequenceNumber: Optional[str] = None,
        Timestamp: Optional[datetime] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def increase_stream_retention_period(
        self,
        StreamName: str,
        RetentionPeriodHours: int,
    ):
        pass


    def list_shards(
        self,
        StreamName: Optional[str] = None,
        NextToken: Optional[str] = None,
        ExclusiveStartShardId: Optional[str] = None,
        MaxResults: Optional[int] = None,
        StreamCreationTimestamp: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_stream_consumers(
        self,
        StreamARN: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        StreamCreationTimestamp: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_streams(
        self,
        Limit: Optional[int] = None,
        ExclusiveStartStreamName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_stream(
        self,
        StreamName: str,
        ExclusiveStartTagKey: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def merge_shards(
        self,
        StreamName: str,
        ShardToMerge: str,
        AdjacentShardToMerge: str,
    ):
        pass


    def put_record(
        self,
        StreamName: str,
        Data: bytes,
        PartitionKey: str,
        ExplicitHashKey: Optional[str] = None,
        SequenceNumberForOrdering: Optional[str] = None,
    ) -> Dict:
        pass


    def put_records(
        self,
        Records: List,
        StreamName: str,
    ) -> Dict:
        pass


    def register_stream_consumer(
        self,
        StreamARN: str,
        ConsumerName: str,
    ) -> Dict:
        pass


    def remove_tags_from_stream(
        self,
        StreamName: str,
        TagKeys: List,
    ):
        pass


    def split_shard(
        self,
        StreamName: str,
        ShardToSplit: str,
        NewStartingHashKey: str,
    ):
        pass


    def start_stream_encryption(
        self,
        StreamName: str,
        EncryptionType: str,
        KeyId: str,
    ):
        pass


    def stop_stream_encryption(
        self,
        StreamName: str,
        EncryptionType: str,
        KeyId: str,
    ):
        pass


    def subscribe_to_shard(
        self,
        ConsumerARN: str,
        ShardId: str,
        StartingPosition: Dict,
    ) -> Dict:
        pass


    def update_shard_count(
        self,
        StreamName: str,
        TargetShardCount: int,
        ScalingType: str,
    ) -> Dict:
        pass

