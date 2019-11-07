from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_get_item(
        self,
        RequestItems: Dict,
        ReturnConsumedCapacity: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_write_item(
        self,
        RequestItems: Dict,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnItemCollectionMetrics: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_backup(
        self,
        TableName: str,
        BackupName: str,
    ) -> Dict:
        pass


    def create_global_table(
        self,
        GlobalTableName: str,
        ReplicationGroup: List,
    ) -> Dict:
        pass


    def create_table(
        self,
        AttributeDefinitions: List,
        TableName: str,
        KeySchema: List,
        LocalSecondaryIndexes: Optional[List] = None,
        GlobalSecondaryIndexes: Optional[List] = None,
        BillingMode: Optional[str] = None,
        ProvisionedThroughput: Optional[Dict] = None,
        StreamSpecification: Optional[Dict] = None,
        SSESpecification: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_backup(
        self,
        BackupArn: str,
    ) -> Dict:
        pass


    def delete_item(
        self,
        TableName: str,
        Key: Dict,
        Expected: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ReturnValues: Optional[str] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnItemCollectionMetrics: Optional[str] = None,
        ConditionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_table(
        self,
        TableName: str,
    ) -> Dict:
        pass


    def describe_backup(
        self,
        BackupArn: str,
    ) -> Dict:
        pass


    def describe_continuous_backups(
        self,
        TableName: str,
    ) -> Dict:
        pass


    def describe_endpoints(
        self,
    ) -> Dict:
        pass


    def describe_global_table(
        self,
        GlobalTableName: str,
    ) -> Dict:
        pass


    def describe_global_table_settings(
        self,
        GlobalTableName: str,
    ) -> Dict:
        pass


    def describe_limits(
        self,
    ) -> Dict:
        pass


    def describe_table(
        self,
        TableName: str,
    ) -> Dict:
        pass


    def describe_time_to_live(
        self,
        TableName: str,
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


    def get_item(
        self,
        TableName: str,
        Key: Dict,
        AttributesToGet: Optional[List] = None,
        ConsistentRead: Optional[bool] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ProjectionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
    ) -> Dict:
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


    def list_backups(
        self,
        TableName: Optional[str] = None,
        Limit: Optional[int] = None,
        TimeRangeLowerBound: Optional[datetime] = None,
        TimeRangeUpperBound: Optional[datetime] = None,
        ExclusiveStartBackupArn: Optional[str] = None,
        BackupType: Optional[str] = None,
    ) -> Dict:
        pass


    def list_global_tables(
        self,
        ExclusiveStartGlobalTableName: Optional[str] = None,
        Limit: Optional[int] = None,
        RegionName: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tables(
        self,
        ExclusiveStartTableName: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_of_resource(
        self,
        ResourceArn: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_item(
        self,
        TableName: str,
        Item: Dict,
        Expected: Optional[Dict] = None,
        ReturnValues: Optional[str] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnItemCollectionMetrics: Optional[str] = None,
        ConditionalOperator: Optional[str] = None,
        ConditionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
    ) -> Dict:
        pass


    def query(
        self,
        TableName: str,
        IndexName: Optional[str] = None,
        Select: Optional[str] = None,
        AttributesToGet: Optional[List] = None,
        Limit: Optional[int] = None,
        ConsistentRead: Optional[bool] = None,
        KeyConditions: Optional[Dict] = None,
        QueryFilter: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ScanIndexForward: Optional[bool] = None,
        ExclusiveStartKey: Optional[Dict] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ProjectionExpression: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        KeyConditionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
    ) -> Dict:
        pass


    def restore_table_from_backup(
        self,
        TargetTableName: str,
        BackupArn: str,
    ) -> Dict:
        pass


    def restore_table_to_point_in_time(
        self,
        SourceTableName: str,
        TargetTableName: str,
        UseLatestRestorableTime: Optional[bool] = None,
        RestoreDateTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def scan(
        self,
        TableName: str,
        IndexName: Optional[str] = None,
        AttributesToGet: Optional[List] = None,
        Limit: Optional[int] = None,
        Select: Optional[str] = None,
        ScanFilter: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ExclusiveStartKey: Optional[Dict] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        TotalSegments: Optional[int] = None,
        Segment: Optional[int] = None,
        ProjectionExpression: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
        ConsistentRead: Optional[bool] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ):
        pass


    def transact_get_items(
        self,
        TransactItems: List,
        ReturnConsumedCapacity: Optional[str] = None,
    ) -> Dict:
        pass


    def transact_write_items(
        self,
        TransactItems: List,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnItemCollectionMetrics: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ):
        pass


    def update_continuous_backups(
        self,
        TableName: str,
        PointInTimeRecoverySpecification: Dict,
    ) -> Dict:
        pass


    def update_global_table(
        self,
        GlobalTableName: str,
        ReplicaUpdates: List,
    ) -> Dict:
        pass


    def update_global_table_settings(
        self,
        GlobalTableName: str,
        GlobalTableBillingMode: Optional[str] = None,
        GlobalTableProvisionedWriteCapacityUnits: Optional[int] = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[Dict] = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: Optional[List] = None,
        ReplicaSettingsUpdate: Optional[List] = None,
    ) -> Dict:
        pass


    def update_item(
        self,
        TableName: str,
        Key: Dict,
        AttributeUpdates: Optional[Dict] = None,
        Expected: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ReturnValues: Optional[str] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ReturnItemCollectionMetrics: Optional[str] = None,
        UpdateExpression: Optional[str] = None,
        ConditionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_table(
        self,
        TableName: str,
        AttributeDefinitions: Optional[List] = None,
        BillingMode: Optional[str] = None,
        ProvisionedThroughput: Optional[Dict] = None,
        GlobalSecondaryIndexUpdates: Optional[List] = None,
        StreamSpecification: Optional[Dict] = None,
        SSESpecification: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_time_to_live(
        self,
        TableName: str,
        TimeToLiveSpecification: Dict,
    ) -> Dict:
        pass

