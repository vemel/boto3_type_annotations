from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class Select(Paginator):
    def paginate(
        self,
        SelectExpression: str,
        ConsistentRead: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

