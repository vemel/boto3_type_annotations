from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeAffectedEntities(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        filter: Dict[str, Any],
        locale: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEventAggregates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        aggregateField: str,
        filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEventTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        filter: Dict[str, Any] = None,
        locale: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        filter: Dict[str, Any] = None,
        locale: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
