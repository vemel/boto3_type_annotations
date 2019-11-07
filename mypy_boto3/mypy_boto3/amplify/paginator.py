from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListApps(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListBranches(Paginator):
    def paginate(
        self,
        appId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDomainAssociations(Paginator):
    def paginate(
        self,
        appId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        appId: str,
        branchName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

