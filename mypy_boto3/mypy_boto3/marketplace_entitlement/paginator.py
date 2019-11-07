from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetEntitlements(Paginator):
    def paginate(
        self,
        ProductCode: str,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

