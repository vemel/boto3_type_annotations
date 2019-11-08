from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: str = None,
        KinesisStreamSourceConfiguration: Dict[str, Any] = None,
        S3DestinationConfiguration: Dict[str, Any] = None,
        ExtendedS3DestinationConfiguration: Dict[str, Any] = None,
        RedshiftDestinationConfiguration: Dict[str, Any] = None,
        ElasticsearchDestinationConfiguration: Dict[str, Any] = None,
        SplunkDestinationConfiguration: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_delivery_stream(self, DeliveryStreamName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_delivery_stream(
        self,
        DeliveryStreamName: str,
        Limit: int = None,
        ExclusiveStartDestinationId: str = None,
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
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_delivery_streams(
        self,
        Limit: int = None,
        DeliveryStreamType: str = None,
        ExclusiveStartDeliveryStreamName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_delivery_stream(
        self,
        DeliveryStreamName: str,
        ExclusiveStartTagKey: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_record(
        self, DeliveryStreamName: str, Record: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_record_batch(
        self, DeliveryStreamName: str, Records: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_delivery_stream_encryption(
        self, DeliveryStreamName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_delivery_stream_encryption(
        self, DeliveryStreamName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_delivery_stream(
        self, DeliveryStreamName: str, Tags: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_delivery_stream(
        self, DeliveryStreamName: str, TagKeys: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: Dict[str, Any] = None,
        ExtendedS3DestinationUpdate: Dict[str, Any] = None,
        RedshiftDestinationUpdate: Dict[str, Any] = None,
        ElasticsearchDestinationUpdate: Dict[str, Any] = None,
        SplunkDestinationUpdate: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
