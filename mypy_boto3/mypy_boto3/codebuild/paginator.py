from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListBuilds(Paginator):
    def paginate(
        self,
        sortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBuildsForProject(Paginator):
    def paginate(
        self,
        projectName: str,
        sortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProjects(Paginator):
    def paginate(
        self,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

