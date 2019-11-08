from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, APIVersion: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
