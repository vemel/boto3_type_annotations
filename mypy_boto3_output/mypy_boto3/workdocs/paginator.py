from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeActivities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeComments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDocumentVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFolderContents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: str = None,
        Order: str = None,
        Type: str = None,
        Include: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNotificationSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, OrganizationId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeResourcePermissions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeRootFolders(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AuthenticationToken: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: str = None,
        Order: str = None,
        Sort: str = None,
        Fields: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
