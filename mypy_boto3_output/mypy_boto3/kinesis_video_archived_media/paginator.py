from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListFragments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StreamName: str,
        FragmentSelector: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
