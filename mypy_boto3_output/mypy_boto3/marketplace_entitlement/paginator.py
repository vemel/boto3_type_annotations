from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetEntitlements(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProductCode: str,
        Filter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
