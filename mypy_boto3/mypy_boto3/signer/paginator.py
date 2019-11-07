from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListSigningJobs(Paginator):
    def paginate(
        self,
        status: Optional[str] = None,
        platformId: Optional[str] = None,
        requestedBy: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSigningPlatforms(Paginator):
    def paginate(
        self,
        category: Optional[str] = None,
        partner: Optional[str] = None,
        target: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSigningProfiles(Paginator):
    def paginate(
        self,
        includeCanceled: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

