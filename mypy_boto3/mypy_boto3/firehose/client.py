from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: Optional[str] = None,
        KinesisStreamSourceConfiguration: Optional[Dict] = None,
        S3DestinationConfiguration: Optional[Dict] = None,
        ExtendedS3DestinationConfiguration: Optional[Dict] = None,
        RedshiftDestinationConfiguration: Optional[Dict] = None,
        ElasticsearchDestinationConfiguration: Optional[Dict] = None,
        SplunkDestinationConfiguration: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_delivery_stream(
        self,
        DeliveryStreamName: str,
    ) -> Dict:
        pass


    def describe_delivery_stream(
        self,
        DeliveryStreamName: str,
        Limit: Optional[int] = None,
        ExclusiveStartDestinationId: Optional[str] = None,
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_delivery_streams(
        self,
        Limit: Optional[int] = None,
        DeliveryStreamType: Optional[str] = None,
        ExclusiveStartDeliveryStreamName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_delivery_stream(
        self,
        DeliveryStreamName: str,
        ExclusiveStartTagKey: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def put_record(
        self,
        DeliveryStreamName: str,
        Record: Dict,
    ) -> Dict:
        pass


    def put_record_batch(
        self,
        DeliveryStreamName: str,
        Records: List,
    ) -> Dict:
        pass


    def start_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
    ) -> Dict:
        pass


    def stop_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
    ) -> Dict:
        pass


    def tag_delivery_stream(
        self,
        DeliveryStreamName: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_delivery_stream(
        self,
        DeliveryStreamName: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: Optional[Dict] = None,
        ExtendedS3DestinationUpdate: Optional[Dict] = None,
        RedshiftDestinationUpdate: Optional[Dict] = None,
        ElasticsearchDestinationUpdate: Optional[Dict] = None,
        SplunkDestinationUpdate: Optional[Dict] = None,
    ) -> Dict:
        pass

