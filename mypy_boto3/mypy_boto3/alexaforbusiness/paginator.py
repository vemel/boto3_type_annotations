from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListBusinessReportSchedules(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListConferenceProviders(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeviceEvents(Paginator):
    def paginate(
        self,
        DeviceArn: str,
        EventType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSkills(Paginator):
    def paginate(
        self,
        SkillGroupArn: Optional[str] = None,
        EnablementType: Optional[str] = None,
        SkillType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSkillsStoreCategories(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSkillsStoreSkillsByCategory(Paginator):
    def paginate(
        self,
        CategoryId: int,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSmartHomeAppliances(Paginator):
    def paginate(
        self,
        RoomArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        Arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchDevices(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchProfiles(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchRooms(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchSkillGroups(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchUsers(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

