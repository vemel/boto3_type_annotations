from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeReservedElasticsearchInstanceOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedElasticsearchInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedElasticsearchInstanceId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetUpgradeHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DomainName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListElasticsearchInstanceTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListElasticsearchVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
