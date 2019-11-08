from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TagFilters: List[Any] = None,
        TagsPerPage: int = None,
        ResourceTypeFilters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTagKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetTagValues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Key: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
