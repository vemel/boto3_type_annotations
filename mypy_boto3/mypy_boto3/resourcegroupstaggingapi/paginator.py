from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetResources(Paginator):
    def paginate(
        self,
        TagFilters: Optional[List] = None,
        TagsPerPage: Optional[int] = None,
        ResourceTypeFilters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTagKeys(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTagValues(Paginator):
    def paginate(
        self,
        Key: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

