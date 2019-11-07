from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListChannels(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListHarvestJobs(Paginator):
    def paginate(
        self,
        IncludeChannelId: Optional[str] = None,
        IncludeStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOriginEndpoints(Paginator):
    def paginate(
        self,
        ChannelId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

