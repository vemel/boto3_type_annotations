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
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_dimension_keys(
        self,
        ServiceType: str,
        Identifier: str,
        StartTime: datetime,
        EndTime: datetime,
        Metric: str,
        GroupBy: Dict[str, Any],
        PeriodInSeconds: int = None,
        PartitionBy: Dict[str, Any] = None,
        Filter: Dict[str, Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
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
    def get_resource_metrics(
        self,
        ServiceType: str,
        Identifier: str,
        MetricQueries: List[Any],
        StartTime: datetime,
        EndTime: datetime,
        PeriodInSeconds: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass
