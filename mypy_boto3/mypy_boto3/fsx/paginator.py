from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeBackups(Paginator):
    def paginate(
        self,
        BackupIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFileSystems(Paginator):
    def paginate(
        self,
        FileSystemIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        ResourceARN: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

