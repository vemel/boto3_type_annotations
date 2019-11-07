from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListProjects(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResources(Paginator):
    def paginate(
        self,
        projectId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTeamMembers(Paginator):
    def paginate(
        self,
        projectId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUserProfiles(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

