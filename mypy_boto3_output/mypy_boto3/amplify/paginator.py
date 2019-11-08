from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListApps(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListBranches(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, appId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDomainAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, appId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, appId: str, branchName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
