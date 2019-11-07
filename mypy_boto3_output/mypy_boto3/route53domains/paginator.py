from __future__ import annotations

# builtin imports
from datetime import datetime
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListDomains(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SubmittedSince: datetime = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ViewBilling(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Start: datetime = None,
        End: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
