from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListApplicationSnapshots(Paginator):
    def paginate(
        self,
        ApplicationName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListApplications(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

