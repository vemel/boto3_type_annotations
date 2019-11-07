from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetConnectors(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetReplicationJobs(Paginator):
    def paginate(
        self,
        replicationJobId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetReplicationRuns(Paginator):
    def paginate(
        self,
        replicationJobId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetServers(Paginator):
    def paginate(
        self,
        vmServerAddressList: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListApps(Paginator):
    def paginate(
        self,
        appIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

