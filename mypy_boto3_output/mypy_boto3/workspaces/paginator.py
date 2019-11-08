from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAccountModifications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeIpGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, GroupIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeWorkspaceBundles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        BundleIds: List[Any] = None,
        Owner: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeWorkspaceDirectories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeWorkspaceImages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ImageIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeWorkspaces(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        WorkspaceIds: List[Any] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeWorkspacesConnectionStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, WorkspaceIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAvailableManagementCidrRanges(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ManagementCidrRangeConstraint: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
