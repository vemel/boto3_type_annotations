from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListBusinessReportSchedules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListConferenceProviders(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDeviceEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DeviceArn: str,
        EventType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSkills(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SkillGroupArn: str = None,
        EnablementType: str = None,
        SkillType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListSkillsStoreCategories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSkillsStoreSkillsByCategory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, CategoryId: int, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListSmartHomeAppliances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, RoomArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Arn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class SearchDevices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchProfiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchRooms(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchSkillGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchUsers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SortCriteria: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
