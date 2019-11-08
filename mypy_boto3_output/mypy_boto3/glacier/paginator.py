from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        vaultName: str,
        accountId: str = None,
        statuscode: str = None,
        completed: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListMultipartUploads(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        vaultName: str,
        accountId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListParts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        vaultName: str,
        uploadId: str,
        accountId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListVaults(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, accountId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
