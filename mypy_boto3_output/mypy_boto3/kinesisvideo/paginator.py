from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListStreams(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        StreamNameCondition: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
