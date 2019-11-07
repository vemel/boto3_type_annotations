from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListJobs(Paginator):
    def paginate(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        statuscode: Optional[str] = None,
        completed: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMultipartUploads(Paginator):
    def paginate(
        self,
        vaultName: str,
        accountId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListParts(Paginator):
    def paginate(
        self,
        vaultName: str,
        uploadId: str,
        accountId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVaults(Paginator):
    def paginate(
        self,
        accountId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

