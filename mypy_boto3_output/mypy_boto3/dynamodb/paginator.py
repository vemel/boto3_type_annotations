from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListBackups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TableName: str = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        BackupType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTables(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListTagsOfResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class Query(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        Select: str = None,
        AttributesToGet: List[Any] = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, Any] = None,
        QueryFilter: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ScanIndexForward: bool = None,
        ReturnConsumedCapacity: str = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class Scan(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[Any] = None,
        Select: str = None,
        ScanFilter: Dict[str, Any] = None,
        ConditionalOperator: str = None,
        ReturnConsumedCapacity: str = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, Any] = None,
        ExpressionAttributeValues: Dict[str, Any] = None,
        ConsistentRead: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
