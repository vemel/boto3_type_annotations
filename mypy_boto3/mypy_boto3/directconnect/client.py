from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
    ) -> Dict:
        pass


    def allocate_connection_on_interconnect(
        self,
        bandwidth: str,
        connectionName: str,
        ownerAccount: str,
        interconnectId: str,
        vlan: int,
    ) -> Dict:
        pass


    def allocate_hosted_connection(
        self,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def allocate_private_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: Dict,
    ) -> Dict:
        pass


    def allocate_public_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: Dict,
    ) -> Dict:
        pass


    def allocate_transit_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: Dict,
    ) -> Dict:
        pass


    def associate_connection_with_lag(
        self,
        connectionId: str,
        lagId: str,
    ) -> Dict:
        pass


    def associate_hosted_connection(
        self,
        connectionId: str,
        parentConnectionId: str,
    ) -> Dict:
        pass


    def associate_virtual_interface(
        self,
        virtualInterfaceId: str,
        connectionId: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def confirm_connection(
        self,
        connectionId: str,
    ) -> Dict:
        pass


    def confirm_private_virtual_interface(
        self,
        virtualInterfaceId: str,
        virtualGatewayId: Optional[str] = None,
        directConnectGatewayId: Optional[str] = None,
    ) -> Dict:
        pass


    def confirm_public_virtual_interface(
        self,
        virtualInterfaceId: str,
    ) -> Dict:
        pass


    def confirm_transit_virtual_interface(
        self,
        virtualInterfaceId: str,
        directConnectGatewayId: str,
    ) -> Dict:
        pass


    def create_bgp_peer(
        self,
        virtualInterfaceId: Optional[str] = None,
        newBGPPeer: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_connection(
        self,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: Optional[str] = None,
        tags: Optional[List] = None,
        providerName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_direct_connect_gateway(
        self,
        directConnectGatewayName: str,
        amazonSideAsn: Optional[int] = None,
    ) -> Dict:
        pass


    def create_direct_connect_gateway_association(
        self,
        directConnectGatewayId: str,
        gatewayId: Optional[str] = None,
        addAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
        virtualGatewayId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
        removeAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
    ) -> Dict:
        pass


    def create_interconnect(
        self,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: Optional[str] = None,
        tags: Optional[List] = None,
        providerName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_lag(
        self,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: Optional[str] = None,
        tags: Optional[List] = None,
        childConnectionTags: Optional[List] = None,
        providerName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_private_virtual_interface(
        self,
        connectionId: str,
        newPrivateVirtualInterface: Dict,
    ) -> Dict:
        pass


    def create_public_virtual_interface(
        self,
        connectionId: str,
        newPublicVirtualInterface: Dict,
    ) -> Dict:
        pass


    def create_transit_virtual_interface(
        self,
        connectionId: str,
        newTransitVirtualInterface: Dict,
    ) -> Dict:
        pass


    def delete_bgp_peer(
        self,
        virtualInterfaceId: Optional[str] = None,
        asn: Optional[int] = None,
        customerAddress: Optional[str] = None,
        bgpPeerId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_connection(
        self,
        connectionId: str,
    ) -> Dict:
        pass


    def delete_direct_connect_gateway(
        self,
        directConnectGatewayId: str,
    ) -> Dict:
        pass


    def delete_direct_connect_gateway_association(
        self,
        associationId: Optional[str] = None,
        directConnectGatewayId: Optional[str] = None,
        virtualGatewayId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_direct_connect_gateway_association_proposal(
        self,
        proposalId: str,
    ) -> Dict:
        pass


    def delete_interconnect(
        self,
        interconnectId: str,
    ) -> Dict:
        pass


    def delete_lag(
        self,
        lagId: str,
    ) -> Dict:
        pass


    def delete_virtual_interface(
        self,
        virtualInterfaceId: str,
    ) -> Dict:
        pass


    def describe_connection_loa(
        self,
        connectionId: str,
        providerName: Optional[str] = None,
        loaContentType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_connections(
        self,
        connectionId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_connections_on_interconnect(
        self,
        interconnectId: str,
    ) -> Dict:
        pass


    def describe_direct_connect_gateway_association_proposals(
        self,
        directConnectGatewayId: Optional[str] = None,
        proposalId: Optional[str] = None,
        associatedGatewayId: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_direct_connect_gateway_associations(
        self,
        associationId: Optional[str] = None,
        associatedGatewayId: Optional[str] = None,
        directConnectGatewayId: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
        virtualGatewayId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_direct_connect_gateway_attachments(
        self,
        directConnectGatewayId: Optional[str] = None,
        virtualInterfaceId: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_direct_connect_gateways(
        self,
        directConnectGatewayId: Optional[str] = None,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_hosted_connections(
        self,
        connectionId: str,
    ) -> Dict:
        pass


    def describe_interconnect_loa(
        self,
        interconnectId: str,
        providerName: Optional[str] = None,
        loaContentType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_interconnects(
        self,
        interconnectId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_lags(
        self,
        lagId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_loa(
        self,
        connectionId: str,
        providerName: Optional[str] = None,
        loaContentType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_locations(
        self,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        resourceArns: List,
    ) -> Dict:
        pass


    def describe_virtual_gateways(
        self,
    ) -> Dict:
        pass


    def describe_virtual_interfaces(
        self,
        connectionId: Optional[str] = None,
        virtualInterfaceId: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_connection_from_lag(
        self,
        connectionId: str,
        lagId: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_direct_connect_gateway_association(
        self,
        associationId: Optional[str] = None,
        addAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
        removeAllowedPrefixesToDirectConnectGateway: Optional[List] = None,
    ) -> Dict:
        pass


    def update_lag(
        self,
        lagId: str,
        lagName: Optional[str] = None,
        minimumLinks: Optional[int] = None,
    ) -> Dict:
        pass


    def update_virtual_interface_attributes(
        self,
        virtualInterfaceId: str,
        mtu: Optional[int] = None,
    ) -> Dict:
        pass

