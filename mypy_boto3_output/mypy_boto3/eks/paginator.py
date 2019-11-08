from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListUpdates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass