from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeDirectoryConfigs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DirectoryNames: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeImageBuilders(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeImages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Names: List[Any] = None,
        Arns: List[Any] = None,
        Type: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeStacks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Names: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeUserStackAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AuthenticationType: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAssociatedFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListAssociatedStacks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, FleetName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
