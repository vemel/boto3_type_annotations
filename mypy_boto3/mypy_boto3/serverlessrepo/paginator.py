from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListApplicationDependencies(Paginator):
    def paginate(
        self,
        ApplicationId: str,
        SemanticVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListApplicationVersions(Paginator):
    def paginate(
        self,
        ApplicationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListApplications(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

