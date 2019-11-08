from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetMetricData(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: Dict[str, Any],
        HistoricalMetrics: List[Any],
        Groupings: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListContactFlows(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListHoursOfOperations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPhoneNumbers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[Any] = None,
        PhoneNumberCountryCodes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListQueues(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstanceId: str,
        QueueTypes: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRoutingProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSecurityProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUserHierarchyGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, InstanceId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass
