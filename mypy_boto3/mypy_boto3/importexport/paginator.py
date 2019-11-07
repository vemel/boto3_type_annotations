from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(
        self,
        APIVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

