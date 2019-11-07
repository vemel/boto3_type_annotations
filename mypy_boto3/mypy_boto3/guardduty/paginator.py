from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListDetectors(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFilters(Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFindings(Paginator):
    def paginate(
        self,
        DetectorId: str,
        FindingCriteria: Optional[Dict] = None,
        SortCriteria: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIPSets(Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInvitations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMembers(Paginator):
    def paginate(
        self,
        DetectorId: str,
        OnlyAssociated: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListThreatIntelSets(Paginator):
    def paginate(
        self,
        DetectorId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

