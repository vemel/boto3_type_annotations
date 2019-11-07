from __future__ import annotations

# builtin imports
from typing import Dict
from typing import Any

# boto3 imports
from botocore.paginate import Paginator


class ListAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, KeyId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListGrants(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, KeyId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListKeyPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, KeyId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
