from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListBootstrapActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListInstanceFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListInstanceGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ClusterId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Any] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: str = None,
        InstanceStates: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSecurityConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSteps(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClusterId: str,
        StepStates: List[Any] = None,
        StepIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
