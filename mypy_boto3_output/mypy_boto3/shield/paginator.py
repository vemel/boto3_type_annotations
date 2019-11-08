from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAttacks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceArns: List[Any] = None,
        StartTime: Dict[str, Any] = None,
        EndTime: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListProtections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
