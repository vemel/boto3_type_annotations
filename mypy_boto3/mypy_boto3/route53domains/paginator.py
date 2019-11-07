from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOperations(Paginator):
    def paginate(
        self,
        SubmittedSince: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ViewBilling(Paginator):
    def paginate(
        self,
        Start: Optional[datetime] = None,
        End: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

