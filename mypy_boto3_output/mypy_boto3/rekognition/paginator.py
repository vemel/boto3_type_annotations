from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListCollections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListFaces(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CollectionId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListStreamProcessors(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
