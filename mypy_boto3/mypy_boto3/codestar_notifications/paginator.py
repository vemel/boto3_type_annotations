from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListEventTypes(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNotificationRules(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTargets(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

