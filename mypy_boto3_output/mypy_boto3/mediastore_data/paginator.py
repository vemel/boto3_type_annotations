from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListItems(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Path: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
