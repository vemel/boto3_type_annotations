from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class DescribeEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Mode: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListJobTemplates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Category: str = None,
        ListBy: str = None,
        Order: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Order: str = None,
        Queue: str = None,
        Status: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPresets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Category: str = None,
        ListBy: str = None,
        Order: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListQueues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ListBy: str = None,
        Order: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
