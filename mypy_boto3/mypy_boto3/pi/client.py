from datetime import datetime
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


    def describe_dimension_keys(
        self,
        ServiceType: str,
        Identifier: str,
        StartTime: datetime,
        EndTime: datetime,
        Metric: str,
        GroupBy: Dict,
        PeriodInSeconds: Optional[int] = None,
        PartitionBy: Optional[Dict] = None,
        Filter: Optional[Dict] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
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


    def get_resource_metrics(
        self,
        ServiceType: str,
        Identifier: str,
        MetricQueries: List,
        StartTime: datetime,
        EndTime: datetime,
        PeriodInSeconds: Optional[int] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass

