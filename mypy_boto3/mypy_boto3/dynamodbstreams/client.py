from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def describe_stream(
        self,
        StreamArn: str,
        Limit: Optional[int] = None,
        ExclusiveStartShardId: Optional[str] = None,
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
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: str,
        SequenceNumber: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_streams(
        self,
        TableName: Optional[str] = None,
        Limit: Optional[int] = None,
        ExclusiveStartStreamArn: Optional[str] = None,
    ) -> Dict:
        pass

