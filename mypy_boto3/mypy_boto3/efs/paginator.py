from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeFileSystems(Paginator):
    def paginate(
        self,
        CreationToken: Optional[str] = None,
        FileSystemId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMountTargets(Paginator):
    def paginate(
        self,
        FileSystemId: Optional[str] = None,
        MountTargetId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTags(Paginator):
    def paginate(
        self,
        FileSystemId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

