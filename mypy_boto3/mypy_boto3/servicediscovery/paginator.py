from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListInstances(Paginator):
    def paginate(
        self,
        ServiceId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNamespaces(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOperations(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServices(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

