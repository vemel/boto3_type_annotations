from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAccounts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Name: str = None,
        UserEmail: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AccountId: str,
        UserEmail: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
