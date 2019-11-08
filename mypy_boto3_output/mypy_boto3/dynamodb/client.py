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
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_backup(self, TableName: str, BackupName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_global_table(
        self, GlobalTableName: str, ReplicationGroup: List[Any]
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
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_backup(self, BackupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_item(
        self,
        TableName: str,
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
    def delete_table(self, TableName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_backup(self, BackupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_continuous_backups(self, TableName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoints(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_global_table(self, GlobalTableName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_global_table_settings(self, GlobalTableName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_limits(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_table(self, TableName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_time_to_live(self, TableName: str) -> Dict[str, Any]:
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
    def get_item(
        self,
        TableName: str,
        Key: Dict[str, Any],
        AttributesToGet: List[Any] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: str = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_backups(
        self,
        TableName: str = None,
        Limit: int = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        ExclusiveStartBackupArn: str = None,
        BackupType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_global_tables(
        self,
        ExclusiveStartGlobalTableName: str = None,
        Limit: int = None,
        RegionName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tables(
        self, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_of_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_item(
        self,
        TableName: str,
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
        TableName: str,
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
    def restore_table_from_backup(
        self, TargetTableName: str, BackupArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restore_table_to_point_in_time(
        self,
        SourceTableName: str,
        TargetTableName: str,
        UseLatestRestorableTime: bool = None,
        RestoreDateTime: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def scan(
        self,
        TableName: str,
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
    def tag_resource(self, ResourceArn: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def transact_get_items(
        self, TransactItems: List[Any], ReturnConsumedCapacity: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def transact_write_items(
        self,
        TransactItems: List[Any],
        ReturnConsumedCapacity: str = None,
        ReturnItemCollectionMetrics: str = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_continuous_backups(
        self, TableName: str, PointInTimeRecoverySpecification: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_global_table(
        self, GlobalTableName: str, ReplicaUpdates: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_global_table_settings(
        self,
        GlobalTableName: str,
        GlobalTableBillingMode: str = None,
        GlobalTableProvisionedWriteCapacityUnits: int = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Dict[
            str, Any
        ] = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: List[Any] = None,
        ReplicaSettingsUpdate: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_item(
        self,
        TableName: str,
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
    def update_table(
        self,
        TableName: str,
        AttributeDefinitions: List[Any] = None,
        BillingMode: str = None,
        ProvisionedThroughput: Dict[str, Any] = None,
        GlobalSecondaryIndexUpdates: List[Any] = None,
        StreamSpecification: Dict[str, Any] = None,
        SSESpecification: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_time_to_live(
        self, TableName: str, TimeToLiveSpecification: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass
