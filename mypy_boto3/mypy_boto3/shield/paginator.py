from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAttacks(Paginator):
    def paginate(
        self,
        ResourceArns: Optional[List] = None,
        StartTime: Optional[Dict] = None,
        EndTime: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProtections(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

