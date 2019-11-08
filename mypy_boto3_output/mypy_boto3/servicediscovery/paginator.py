from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ServiceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListNamespaces(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
