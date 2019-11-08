from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeAccountLimits(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class DescribeChangeSet(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeStackEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeStacks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackName: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListChangeSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListExports(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListImports(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ExportName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStackInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StackSetName: str,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStackResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStackSetOperationResults(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StackSetName: str,
        OperationId: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListStackSetOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, StackSetName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStackSets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Status: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStacks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StackStatusFilter: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
