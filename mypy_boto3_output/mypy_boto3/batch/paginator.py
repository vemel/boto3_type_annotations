from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeComputeEnvironments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        computeEnvironments: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeJobDefinitions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        jobDefinitions: List[Any] = None,
        jobDefinitionName: str = None,
        status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeJobQueues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, jobQueues: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
