from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAssets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPackagingConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPackagingGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
