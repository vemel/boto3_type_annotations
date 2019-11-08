from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetActiveNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetBlueprints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetBundles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, includeInactive: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetCloudFormationStackRecords(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetDiskSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetDisks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetDomains(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetExportSnapshotRecords(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetInstanceSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetKeyPairs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetLoadBalancers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetRelationalDatabaseBlueprints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetRelationalDatabaseBundles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetRelationalDatabaseEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetRelationalDatabaseParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, relationalDatabaseName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetRelationalDatabaseSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetRelationalDatabases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetStaticIps(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
