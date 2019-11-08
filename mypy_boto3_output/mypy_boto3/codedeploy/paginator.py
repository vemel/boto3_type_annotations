from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListApplicationRevisions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        applicationName: str,
        sortBy: str = None,
        sortOrder: str = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListApplications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDeploymentConfigs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDeploymentGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, applicationName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListDeploymentInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[Any] = None,
        instanceTypeFilter: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDeploymentTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDeployments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[Any] = None,
        createTimeRange: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListGitHubAccountTokenNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListOnPremisesInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        registrationStatus: str = None,
        tagFilters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
