from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetMetricData(Paginator):
    def paginate(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: Dict,
        HistoricalMetrics: List,
        Groupings: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListContactFlows(Paginator):
    def paginate(
        self,
        InstanceId: str,
        ContactFlowTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHoursOfOperations(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPhoneNumbers(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PhoneNumberTypes: Optional[List] = None,
        PhoneNumberCountryCodes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListQueues(Paginator):
    def paginate(
        self,
        InstanceId: str,
        QueueTypes: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRoutingProfiles(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSecurityProfiles(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUserHierarchyGroups(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUsers(Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

