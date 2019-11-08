from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetClassifiers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetConnections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CatalogId: str = None,
        Filter: Dict[str, Any] = None,
        HidePassword: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetCrawlerMetrics(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CrawlerNameList: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetCrawlers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetDatabases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CatalogId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetDevEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetJobRuns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, JobName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetPartitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetSecurityConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetTableVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTables(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTriggers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DependentJobName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetUserDefinedFunctions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
