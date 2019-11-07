from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListItems(Paginator):
    def paginate(
        self,
        Path: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

