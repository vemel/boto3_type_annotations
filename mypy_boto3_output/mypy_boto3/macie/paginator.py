from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListMemberAccounts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListS3Resources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, memberAccountId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
