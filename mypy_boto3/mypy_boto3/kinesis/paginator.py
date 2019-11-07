from datetime import datetime
from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeStream(Paginator):
    def paginate(
        self,
        StreamName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListShards(Paginator):
    def paginate(
        self,
        StreamName: Optional[str] = None,
        ExclusiveStartShardId: Optional[str] = None,
        StreamCreationTimestamp: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStreamConsumers(Paginator):
    def paginate(
        self,
        StreamARN: str,
        StreamCreationTimestamp: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStreams(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

