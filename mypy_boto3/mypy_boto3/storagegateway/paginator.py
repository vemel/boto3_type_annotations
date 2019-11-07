from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeTapeArchives(Paginator):
    def paginate(
        self,
        TapeARNs: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTapeRecoveryPoints(Paginator):
    def paginate(
        self,
        GatewayARN: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTapes(Paginator):
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVTLDevices(Paginator):
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFileShares(Paginator):
    def paginate(
        self,
        GatewayARN: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGateways(Paginator):
    def paginate(
        self,
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



class ListTapes(Paginator):
    def paginate(
        self,
        TapeARNs: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVolumes(Paginator):
    def paginate(
        self,
        GatewayARN: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

