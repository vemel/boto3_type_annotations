from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListDomains(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class Select(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
