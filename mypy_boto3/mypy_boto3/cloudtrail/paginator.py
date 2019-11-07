from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListPublicKeys(Paginator):
    def paginate(
        self,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTags(Paginator):
    def paginate(
        self,
        ResourceIdList: List,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTrails(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class LookupEvents(Paginator):
    def paginate(
        self,
        LookupAttributes: Optional[List] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

