from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAssets(Paginator):
    def paginate(
        self,
        PackagingGroupId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPackagingConfigurations(Paginator):
    def paginate(
        self,
        PackagingGroupId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPackagingGroups(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

