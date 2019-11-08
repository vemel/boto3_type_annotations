from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetConnectors(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetReplicationJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, replicationJobId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetReplicationRuns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, replicationJobId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetServers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        vmServerAddressList: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListApps(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, appIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
