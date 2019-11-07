from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    tables: 'tables'

    def Table(
        self,
        name: Optional[str] = None,
    ) -> 'Table':
        pass


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
    ) -> 'Table':
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class Table(base.ServiceResource):
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

    def batch_writer(
        self,
        overwrite_by_pkeys: Optional[List[str]] = None,
    ):
        pass


    def delete(
        self,
    ) -> Dict:
        pass


    def delete_item(
        self,
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


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def get_item(
        self,
        Key: Dict,
        AttributesToGet: Optional[List] = None,
        ConsistentRead: Optional[bool] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ProjectionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
    ) -> Dict:
        pass


    def load(
        self,
    ):
        pass


    def put_item(
        self,
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


    def reload(
        self,
    ):
        pass


    def scan(
        self,
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


    def update(
        self,
        AttributeDefinitions: Optional[List] = None,
        BillingMode: Optional[str] = None,
        ProvisionedThroughput: Optional[Dict] = None,
        GlobalSecondaryIndexUpdates: Optional[List] = None,
        StreamSpecification: Optional[Dict] = None,
        SSESpecification: Optional[Dict] = None,
    ) -> 'Table':
        pass


    def update_item(
        self,
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


    def wait_until_exists(
        self,
    ):
        pass


    def wait_until_not_exists(
        self,
    ):
        pass



class tables(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Table']:
        pass


    @classmethod
    def filter(
        cls,
        ExclusiveStartTableName: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> List['Table']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Table']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Table']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

