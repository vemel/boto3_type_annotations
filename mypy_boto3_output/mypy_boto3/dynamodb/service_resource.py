from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.dynamodb.service_resource as dynamodb_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    tables: dynamodb_service_resource_scope.tables

    # pylint: disable=arguments-differ
    def Table(self, name: str = None) -> dynamodb_service_resource_scope.Table:
        pass

    # pylint: disable=arguments-differ
    def batch_get_item(
        self, RequestItems: Dict[str, Any], ReturnConsumedCapacity: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_write_item(
        self,
        RequestItems: Dict[str, Any],
        ReturnConsumedCapacity: str = None,
        ReturnItemCollectionMetrics: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_table(
        self,
        AttributeDefinitions: List[Any],
        TableName: str,
        KeySchema: List[Any],
        LocalSecondaryIndexes: List[Any] = None,
        GlobalSecondaryIndexes: List[Any] = None,
        BillingMode: str = None,
        ProvisionedThroughput: Dict[str, Any] = None,
        StreamSpecification: Dict[str, Any] = None,
        SSESpecification: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> dynamodb_service_resource_scope.Table:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class Table(Boto3ServiceResource):
    attribute_definitions: List
    table_name: str
    key_schema: List
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    billing_mode_summary: Dict
    local_secondary_indexes: List
    global_secondary_indexes: List
    stream_specification: Dict
    latest_stream_label: str
    latest_stream_arn: str
    restore_summary: Dict
    sse_description: Dict
    name: str

    # pylint: disable=arguments-differ
    def batch_writer(self, overwrite_by_pkeys: List[str] = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_item(
        self,
        Key: Dict[str, Any],
        Expected: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ReturnValues: str = None,
        ReturnConsumedCapacity: str = None,
        ReturnItemCollectionMetrics: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def get_item(
        self,
        Key: Dict[str, Any],
        AttributesToGet: List[Any] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: str = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def put_item(
        self,
        Item: Dict[str, Any],
        Expected: Dict[str, Any] = None,
        ReturnValues: str = None,
        ReturnConsumedCapacity: str = None,
        ReturnItemCollectionMetrics: str = None,
        ConditionalOperator: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def query(
        self,
        IndexName: str = None,
        Select: str = None,
        AttributesToGet: List[Any] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, Any] = None,
        QueryFilter: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[str, Any] = None,
        ReturnConsumedCapacity: str = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def scan(
        self,
        IndexName: str = None,
        AttributesToGet: List[Any] = None,
        Limit: int = None,
        Select: str = None,
        ScanFilter: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ExclusiveStartKey: Dict[str, Any] = None,
        ReturnConsumedCapacity: str = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
        ConsistentRead: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update(
        self,
        AttributeDefinitions: List[Any] = None,
        BillingMode: str = None,
        ProvisionedThroughput: Dict[str, Any] = None,
        GlobalSecondaryIndexUpdates: List[Any] = None,
        StreamSpecification: Dict[str, Any] = None,
        SSESpecification: Dict[str, Any] = None,
    ) -> dynamodb_service_resource_scope.Table:
        pass

    # pylint: disable=arguments-differ
    def update_item(
        self,
        Key: Dict[str, Any],
        AttributeUpdates: Dict[str, Any] = None,
        Expected: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ReturnValues: str = None,
        ReturnConsumedCapacity: str = None,
        ReturnItemCollectionMetrics: str = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_not_exists(self) -> None:
        pass


class tables(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[dynamodb_service_resource_scope.Table]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> List[dynamodb_service_resource_scope.Table]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[dynamodb_service_resource_scope.Table]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[dynamodb_service_resource_scope.Table]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
