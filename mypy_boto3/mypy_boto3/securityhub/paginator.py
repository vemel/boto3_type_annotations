from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetEnabledStandards(Paginator):
    def paginate(
        self,
        StandardsSubscriptionArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetFindings(Paginator):
    def paginate(
        self,
        Filters: Optional[Dict] = None,
        SortCriteria: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetInsights(Paginator):
    def paginate(
        self,
        InsightArns: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEnabledProductsForImport(Paginator):
    def paginate(
        self,
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
        OnlyAssociated: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

