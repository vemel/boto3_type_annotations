from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeApplicationVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabels: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEnvironmentManagedActionHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEnvironments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[Any] = None,
        EnvironmentNames: List[Any] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPlatformVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
