from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListPublicKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceIdList: List[Any], PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTrails(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class LookupEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        LookupAttributes: List[Any] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
