from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeDirectConnectGatewayAssociations(Paginator):
    def paginate(
        self,
        associationId: Optional[str] = None,
        associatedGatewayId: Optional[str] = None,
        directConnectGatewayId: Optional[str] = None,
        virtualGatewayId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDirectConnectGatewayAttachments(Paginator):
    def paginate(
        self,
        directConnectGatewayId: Optional[str] = None,
        virtualInterfaceId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDirectConnectGateways(Paginator):
    def paginate(
        self,
        directConnectGatewayId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

