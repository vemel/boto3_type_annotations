from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterNames: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeDefaultParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SourceName: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeParameterGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ParameterGroupNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SubnetGroupNames: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
