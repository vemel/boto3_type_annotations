from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetOfferingStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListArtifacts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, type: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDeviceInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDevicePools(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, type: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        arn: str = None,
        filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListInstanceProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListJobs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListNetworkProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, type: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListOfferingPromotions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListOfferingTransactions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListProjects(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRemoteAccessSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListRuns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSamples(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSuites(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUniqueProblems(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUploads(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, arn: str, type: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListVPCEConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
