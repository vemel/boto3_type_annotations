from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListPlacements(Paginator):
    def paginate(
        self,
        projectName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProjects(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

