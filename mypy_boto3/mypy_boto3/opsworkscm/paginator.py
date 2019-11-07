from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(
        self,
        BackupId: Optional[str] = None,
        ServerName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        ServerName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeServers(Paginator):
    def paginate(
        self,
        ServerName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

