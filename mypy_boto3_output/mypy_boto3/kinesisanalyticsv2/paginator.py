from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListApplicationSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ApplicationName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
