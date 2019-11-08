from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeDirectories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeDomainControllers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryId: str,
        DomainControllerIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSharedDirectories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTrusts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryId: str = None,
        TrustIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListIpRoutes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListLogSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSchemaExtensions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
