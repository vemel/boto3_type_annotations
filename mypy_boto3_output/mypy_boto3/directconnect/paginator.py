from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeDirectConnectGatewayAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDirectConnectGatewayAttachments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDirectConnectGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        directConnectGatewayId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
