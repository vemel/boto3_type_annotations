from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListClusters(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUpdates(Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

