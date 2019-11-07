from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListBackups(Paginator):
    def paginate(
        self,
        TableName: Optional[str] = None,
        TimeRangeLowerBound: Optional[datetime] = None,
        TimeRangeUpperBound: Optional[datetime] = None,
        BackupType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTables(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsOfResource(Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class Query(Paginator):
    def paginate(
        self,
        TableName: str,
        IndexName: Optional[str] = None,
        Select: Optional[str] = None,
        AttributesToGet: Optional[List] = None,
        ConsistentRead: Optional[bool] = None,
        KeyConditions: Optional[Dict] = None,
        QueryFilter: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ScanIndexForward: Optional[bool] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        ProjectionExpression: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        KeyConditionExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class Scan(Paginator):
    def paginate(
        self,
        TableName: str,
        IndexName: Optional[str] = None,
        AttributesToGet: Optional[List] = None,
        Select: Optional[str] = None,
        ScanFilter: Optional[Dict] = None,
        ConditionalOperator: Optional[str] = None,
        ReturnConsumedCapacity: Optional[str] = None,
        TotalSegments: Optional[int] = None,
        Segment: Optional[int] = None,
        ProjectionExpression: Optional[str] = None,
        FilterExpression: Optional[str] = None,
        ExpressionAttributeNames: Optional[Dict] = None,
        ExpressionAttributeValues: Optional[Dict] = None,
        ConsistentRead: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

