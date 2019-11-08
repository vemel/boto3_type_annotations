from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListComplianceStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PolicyId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListMemberAccounts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
