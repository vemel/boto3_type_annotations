"Main interface for directconnect type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposaloverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    "ClientAllocateConnectionOnInterconnectResponseTypeDef",
    "ClientAllocateHostedConnectionResponsetagsTypeDef",
    "ClientAllocateHostedConnectionResponseTypeDef",
    "ClientAllocateHostedConnectiontagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    "ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    "ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    "ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationTypeDef",
    "ClientAssociateConnectionWithLagResponsetagsTypeDef",
    "ClientAssociateConnectionWithLagResponseTypeDef",
    "ClientAssociateHostedConnectionResponsetagsTypeDef",
    "ClientAssociateHostedConnectionResponseTypeDef",
    "ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAssociateVirtualInterfaceResponsetagsTypeDef",
    "ClientAssociateVirtualInterfaceResponseTypeDef",
    "ClientConfirmConnectionResponseTypeDef",
    "ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    "ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientCreateBgpPeerResponseTypeDef",
    "ClientCreateBgpPeernewBGPPeerTypeDef",
    "ClientCreateConnectionResponsetagsTypeDef",
    "ClientCreateConnectionResponseTypeDef",
    "ClientCreateConnectiontagsTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposaladdAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalremoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientCreateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayResponseTypeDef",
    "ClientCreateInterconnectResponsetagsTypeDef",
    "ClientCreateInterconnectResponseTypeDef",
    "ClientCreateInterconnecttagsTypeDef",
    "ClientCreateLagResponseconnectionstagsTypeDef",
    "ClientCreateLagResponseconnectionsTypeDef",
    "ClientCreateLagResponsetagsTypeDef",
    "ClientCreateLagResponseTypeDef",
    "ClientCreateLagchildConnectionTagsTypeDef",
    "ClientCreateLagtagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    "ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef",
    "ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePublicVirtualInterfaceResponseTypeDef",
    "ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef",
    "ClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponseTypeDef",
    "ClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfacenewTransitVirtualInterfaceTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientDeleteBgpPeerResponseTypeDef",
    "ClientDeleteConnectionResponsetagsTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    "ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayResponseTypeDef",
    "ClientDeleteInterconnectResponseTypeDef",
    "ClientDeleteLagResponseconnectionstagsTypeDef",
    "ClientDeleteLagResponseconnectionsTypeDef",
    "ClientDeleteLagResponsetagsTypeDef",
    "ClientDeleteLagResponseTypeDef",
    "ClientDeleteVirtualInterfaceResponseTypeDef",
    "ClientDescribeConnectionLoaResponseloaTypeDef",
    "ClientDescribeConnectionLoaResponseTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    "ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsResponseconnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    "ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    "ClientDescribeDirectConnectGatewaysResponseTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    "ClientDescribeHostedConnectionsResponseTypeDef",
    "ClientDescribeInterconnectLoaResponseloaTypeDef",
    "ClientDescribeInterconnectLoaResponseTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    "ClientDescribeInterconnectsResponseTypeDef",
    "ClientDescribeLagsResponselagsconnectionstagsTypeDef",
    "ClientDescribeLagsResponselagsconnectionsTypeDef",
    "ClientDescribeLagsResponselagstagsTypeDef",
    "ClientDescribeLagsResponselagsTypeDef",
    "ClientDescribeLagsResponseTypeDef",
    "ClientDescribeLoaResponseTypeDef",
    "ClientDescribeLocationsResponselocationsTypeDef",
    "ClientDescribeLocationsResponseTypeDef",
    "ClientDescribeTagsResponseresourceTagstagsTypeDef",
    "ClientDescribeTagsResponseresourceTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    "ClientDescribeVirtualGatewaysResponseTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    "ClientDescribeVirtualInterfacesResponseTypeDef",
    "ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    "ClientDisassociateConnectionFromLagResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationremoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateLagResponseconnectionstagsTypeDef",
    "ClientUpdateLagResponseconnectionsTypeDef",
    "ClientUpdateLagResponsetagsTypeDef",
    "ClientUpdateLagResponseTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef",
    "DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef",
    "DescribeDirectConnectGatewaysPaginateResponseTypeDef",
)


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociation` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    """
    Type definition for `ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociation` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef
):
    """
    Type definition for `ClientAcceptDirectConnectGatewayAssociationProposalResponse` `directConnectGatewayAssociation`

    Information about an association between a Direct Connect gateway and a virtual private
    gateway or transit gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
      the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
      private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    Type definition for `ClientAcceptDirectConnectGatewayAssociationProposal` `Response`

    - **directConnectGatewayAssociation** *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the associated gateway.

      - **associationState** *(string) --*

        The state of the association. The following are the possible values:

        * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

        * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
        gateway are successfully associated and ready to pass traffic.

        * ``disassociating`` : The initial state after calling
        DeleteDirectConnectGatewayAssociation .

        * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
        the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
        private gateway or transit gateway is stopped.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **associationId** *(string) --*

        The ID of the Direct Connect gateway association.

      - **allowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **virtualGatewayRegion** *(string) --*

        The AWS Region where the virtual private gateway is located.

      - **virtualGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the virtual private gateway.
    """


_ClientAcceptDirectConnectGatewayAssociationProposaloverrideAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposaloverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposaloverrideAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposaloverrideAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientAcceptDirectConnectGatewayAssociationProposal` `overrideAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientAllocateConnectionOnInterconnectResponsetagsTypeDef = TypedDict(
    "_ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateConnectionOnInterconnectResponsetagsTypeDef(
    _ClientAllocateConnectionOnInterconnectResponsetagsTypeDef
):
    """
    Type definition for `ClientAllocateConnectionOnInterconnectResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocateConnectionOnInterconnectResponseTypeDef = TypedDict(
    "_ClientAllocateConnectionOnInterconnectResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientAllocateConnectionOnInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAllocateConnectionOnInterconnectResponseTypeDef(
    _ClientAllocateConnectionOnInterconnectResponseTypeDef
):
    """
    Type definition for `ClientAllocateConnectionOnInterconnect` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientAllocateHostedConnectionResponsetagsTypeDef = TypedDict(
    "_ClientAllocateHostedConnectionResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateHostedConnectionResponsetagsTypeDef(
    _ClientAllocateHostedConnectionResponsetagsTypeDef
):
    """
    Type definition for `ClientAllocateHostedConnectionResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocateHostedConnectionResponseTypeDef = TypedDict(
    "_ClientAllocateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientAllocateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAllocateHostedConnectionResponseTypeDef(
    _ClientAllocateHostedConnectionResponseTypeDef
):
    """
    Type definition for `ClientAllocateHostedConnection` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_RequiredClientAllocateHostedConnectiontagsTypeDef = TypedDict(
    "_RequiredClientAllocateHostedConnectiontagsTypeDef", {"key": str}
)
_OptionalClientAllocateHostedConnectiontagsTypeDef = TypedDict(
    "_OptionalClientAllocateHostedConnectiontagsTypeDef", {"value": str}, total=False
)


class ClientAllocateHostedConnectiontagsTypeDef(
    _RequiredClientAllocateHostedConnectiontagsTypeDef,
    _OptionalClientAllocateHostedConnectiontagsTypeDef,
):
    """
    Type definition for `ClientAllocateHostedConnection` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterfaceResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterfaceResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterfaceResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponseTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterface` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef",
    {"key": str},
)
_OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef",
    {"value": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef(
    _RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef,
    _OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef,
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocation` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": str,
        "customerAddress": str,
        "tags": List[
            ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePrivateVirtualInterfacenewPrivateVirtualInterfaceAllocationTypeDef,
):
    """
    Type definition for `ClientAllocatePrivateVirtualInterface` `newPrivateVirtualInterfaceAllocation`

    Information about the private virtual interface.

    - **virtualInterfaceName** *(string) --* **[REQUIRED]**

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --* **[REQUIRED]**

      The ID of the VLAN.

    - **asn** *(integer) --* **[REQUIRED]**

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **tags** *(list) --*

      The tags associated with the private virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientAllocatePublicVirtualInterfaceResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientAllocatePublicVirtualInterfaceResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef
):
    """
    Type definition for `ClientAllocatePublicVirtualInterfaceResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponseTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientAllocatePublicVirtualInterface` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef(
    _ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocation` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef",
    {"key": str},
)
_OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef",
    {"value": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef(
    _RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef,
    _OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef,
):
    """
    Type definition for `ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocation` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef
        ],
        "tags": List[
            ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePublicVirtualInterfacenewPublicVirtualInterfaceAllocationTypeDef,
):
    """
    Type definition for `ClientAllocatePublicVirtualInterface` `newPublicVirtualInterfaceAllocation`

    Information about the public virtual interface.

    - **virtualInterfaceName** *(string) --* **[REQUIRED]**

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --* **[REQUIRED]**

      The ID of the VLAN.

    - **asn** *(integer) --* **[REQUIRED]**

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border Gateway
        Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **tags** *(list) --*

      The tags associated with the public virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterfaceResponsevirtualInterface` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
      peer can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterfaceResponsevirtualInterface` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterfaceResponsevirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterfaceResponse` `virtualInterface`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner
      of the connection on which it is provisioned, then the virtual interface will remain in
      this state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual
      interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
      interface owner, the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
          peer can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientAllocateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterface": ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponseTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterface` `Response`

    - **virtualInterface** *(dict) --*

      Information about a virtual interface.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.

      - **virtualInterfaceId** *(string) --*

        The ID of the virtual interface.

      - **location** *(string) --*

        The location of the connection.

      - **connectionId** *(string) --*

        The ID of the connection.

      - **virtualInterfaceType** *(string) --*

        The type of virtual interface. The possible values are ``private`` and ``public`` .

      - **virtualInterfaceName** *(string) --*

        The name of the virtual interface assigned by the customer network.

      - **vlan** *(integer) --*

        The ID of the VLAN.

      - **asn** *(integer) --*

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        The valid values are 1-2147483647.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **authKey** *(string) --*

        The authentication key for BGP configuration. This string has a minimum length of 6
        characters and and a maximun lenth of 80 characters.

      - **amazonAddress** *(string) --*

        The IP address assigned to the Amazon interface.

      - **customerAddress** *(string) --*

        The IP address assigned to the customer interface.

      - **addressFamily** *(string) --*

        The address family for the BGP peer.

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:

        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in
        this state until it is confirmed by the virtual interface owner.

        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.

        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.

        * ``available`` : A virtual interface that is able to forward traffic.

        * ``down`` : A virtual interface that is BGP down.

        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.

        * ``deleted`` : A virtual interface that cannot forward traffic.

        * ``rejected`` : The virtual interface owner has declined creation of the virtual
        interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
        interface owner, the virtual interface enters the ``Rejected`` state.

        * ``unknown`` : The state of the virtual interface is not available.

      - **customerRouterConfig** *(string) --*

        The customer router configuration.

      - **mtu** *(integer) --*

        The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
        default value is 1500.

      - **jumboFrameCapable** *(boolean) --*

        Indicates whether jumbo frames (9001 MTU) are supported.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **routeFilterPrefixes** *(list) --*

        The routes to be advertised to the AWS network in this Region. Applies to public virtual
        interfaces.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **bgpPeers** *(list) --*

        The BGP peers configured on this virtual interface.

        - *(dict) --*

          Information about a BGP peer.

          - **bgpPeerId** *(string) --*

            The ID of the BGP peer.

          - **asn** *(integer) --*

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

          - **authKey** *(string) --*

            The authentication key for BGP configuration. This string has a minimum length of 6
            characters and and a maximun lenth of 80 characters.

          - **addressFamily** *(string) --*

            The address family for the BGP peer.

          - **amazonAddress** *(string) --*

            The IP address assigned to the Amazon interface.

          - **customerAddress** *(string) --*

            The IP address assigned to the customer interface.

          - **bgpPeerState** *(string) --*

            The state of the BGP peer. The following are the possible values:

            * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
            peer can be created. This state applies only to public virtual interfaces.

            * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
            be established.

            * ``available`` : The BGP peer is ready to be established.

            * ``deleting`` : The BGP peer is being deleted.

            * ``deleted`` : The BGP peer is deleted and cannot be established.

          - **bgpStatus** *(string) --*

            The status of the BGP peer. The following are the possible values:

            * ``up`` : The BGP peer is established. This state does not indicate the state of the
            routing function. Ensure that you are receiving routes over the BGP session.

            * ``down`` : The BGP peer is down.

            * ``unknown`` : The BGP peer status is not available.

          - **awsDeviceV2** *(string) --*

            The Direct Connect endpoint on which the BGP peer terminates.

      - **region** *(string) --*

        The AWS Region where the virtual interface is located.

      - **awsDeviceV2** *(string) --*

        The Direct Connect endpoint on which the virtual interface terminates.

      - **tags** *(list) --*

        The tags associated with the virtual interface.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key.

          - **value** *(string) --*

            The value.
    """


_RequiredClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_RequiredClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef",
    {"key": str},
)
_OptionalClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_OptionalClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef",
    {"value": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef(
    _RequiredClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef,
    _OptionalClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef,
):
    """
    Type definition for `ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocation` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "tags": List[
            ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationTypeDef(
    _ClientAllocateTransitVirtualInterfacenewTransitVirtualInterfaceAllocationTypeDef
):
    """
    Type definition for `ClientAllocateTransitVirtualInterface` `newTransitVirtualInterfaceAllocation`

    Information about the transit virtual interface.

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **tags** *(list) --*

      The tags associated with the transitive virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientAssociateConnectionWithLagResponsetagsTypeDef = TypedDict(
    "_ClientAssociateConnectionWithLagResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAssociateConnectionWithLagResponsetagsTypeDef(
    _ClientAssociateConnectionWithLagResponsetagsTypeDef
):
    """
    Type definition for `ClientAssociateConnectionWithLagResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAssociateConnectionWithLagResponseTypeDef = TypedDict(
    "_ClientAssociateConnectionWithLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientAssociateConnectionWithLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAssociateConnectionWithLagResponseTypeDef(
    _ClientAssociateConnectionWithLagResponseTypeDef
):
    """
    Type definition for `ClientAssociateConnectionWithLag` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientAssociateHostedConnectionResponsetagsTypeDef = TypedDict(
    "_ClientAssociateHostedConnectionResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAssociateHostedConnectionResponsetagsTypeDef(
    _ClientAssociateHostedConnectionResponsetagsTypeDef
):
    """
    Type definition for `ClientAssociateHostedConnectionResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAssociateHostedConnectionResponseTypeDef = TypedDict(
    "_ClientAssociateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientAssociateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAssociateHostedConnectionResponseTypeDef(
    _ClientAssociateHostedConnectionResponseTypeDef
):
    """
    Type definition for `ClientAssociateHostedConnection` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientAssociateVirtualInterfaceResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientAssociateVirtualInterfaceResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientAssociateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAssociateVirtualInterfaceResponsetagsTypeDef(
    _ClientAssociateVirtualInterfaceResponsetagsTypeDef
):
    """
    Type definition for `ClientAssociateVirtualInterfaceResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientAssociateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAssociateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAssociateVirtualInterfaceResponseTypeDef(
    _ClientAssociateVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientAssociateVirtualInterface` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientConfirmConnectionResponseTypeDef = TypedDict(
    "_ClientConfirmConnectionResponseTypeDef", {"connectionState": str}, total=False
)


class ClientConfirmConnectionResponseTypeDef(_ClientConfirmConnectionResponseTypeDef):
    """
    Type definition for `ClientConfirmConnection` `Response`

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.
    """


_ClientConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    {"virtualInterfaceState": str},
    total=False,
)


class ClientConfirmPrivateVirtualInterfaceResponseTypeDef(
    _ClientConfirmPrivateVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientConfirmPrivateVirtualInterface` `Response`

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    {"virtualInterfaceState": str},
    total=False,
)


class ClientConfirmPublicVirtualInterfaceResponseTypeDef(
    _ClientConfirmPublicVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientConfirmPublicVirtualInterface` `Response`

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    {"virtualInterfaceState": str},
    total=False,
)


class ClientConfirmTransitVirtualInterfaceResponseTypeDef(
    _ClientConfirmTransitVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientConfirmTransitVirtualInterface` `Response`

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef
):
    """
    Type definition for `ClientCreateBgpPeerResponsevirtualInterface` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
      peer can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientCreateBgpPeerResponsevirtualInterface` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef
):
    """
    Type definition for `ClientCreateBgpPeerResponsevirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfaceTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfaceTypeDef
):
    """
    Type definition for `ClientCreateBgpPeerResponse` `virtualInterface`

    The virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner
      of the connection on which it is provisioned, then the virtual interface will remain in
      this state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual
      interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
      interface owner, the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
          peer can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientCreateBgpPeerResponseTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponseTypeDef",
    {"virtualInterface": ClientCreateBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientCreateBgpPeerResponseTypeDef(_ClientCreateBgpPeerResponseTypeDef):
    """
    Type definition for `ClientCreateBgpPeer` `Response`

    - **virtualInterface** *(dict) --*

      The virtual interface.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.

      - **virtualInterfaceId** *(string) --*

        The ID of the virtual interface.

      - **location** *(string) --*

        The location of the connection.

      - **connectionId** *(string) --*

        The ID of the connection.

      - **virtualInterfaceType** *(string) --*

        The type of virtual interface. The possible values are ``private`` and ``public`` .

      - **virtualInterfaceName** *(string) --*

        The name of the virtual interface assigned by the customer network.

      - **vlan** *(integer) --*

        The ID of the VLAN.

      - **asn** *(integer) --*

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        The valid values are 1-2147483647.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **authKey** *(string) --*

        The authentication key for BGP configuration. This string has a minimum length of 6
        characters and and a maximun lenth of 80 characters.

      - **amazonAddress** *(string) --*

        The IP address assigned to the Amazon interface.

      - **customerAddress** *(string) --*

        The IP address assigned to the customer interface.

      - **addressFamily** *(string) --*

        The address family for the BGP peer.

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:

        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in
        this state until it is confirmed by the virtual interface owner.

        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.

        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.

        * ``available`` : A virtual interface that is able to forward traffic.

        * ``down`` : A virtual interface that is BGP down.

        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.

        * ``deleted`` : A virtual interface that cannot forward traffic.

        * ``rejected`` : The virtual interface owner has declined creation of the virtual
        interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
        interface owner, the virtual interface enters the ``Rejected`` state.

        * ``unknown`` : The state of the virtual interface is not available.

      - **customerRouterConfig** *(string) --*

        The customer router configuration.

      - **mtu** *(integer) --*

        The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
        default value is 1500.

      - **jumboFrameCapable** *(boolean) --*

        Indicates whether jumbo frames (9001 MTU) are supported.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **routeFilterPrefixes** *(list) --*

        The routes to be advertised to the AWS network in this Region. Applies to public virtual
        interfaces.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **bgpPeers** *(list) --*

        The BGP peers configured on this virtual interface.

        - *(dict) --*

          Information about a BGP peer.

          - **bgpPeerId** *(string) --*

            The ID of the BGP peer.

          - **asn** *(integer) --*

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

          - **authKey** *(string) --*

            The authentication key for BGP configuration. This string has a minimum length of 6
            characters and and a maximun lenth of 80 characters.

          - **addressFamily** *(string) --*

            The address family for the BGP peer.

          - **amazonAddress** *(string) --*

            The IP address assigned to the Amazon interface.

          - **customerAddress** *(string) --*

            The IP address assigned to the customer interface.

          - **bgpPeerState** *(string) --*

            The state of the BGP peer. The following are the possible values:

            * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
            peer can be created. This state applies only to public virtual interfaces.

            * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
            be established.

            * ``available`` : The BGP peer is ready to be established.

            * ``deleting`` : The BGP peer is being deleted.

            * ``deleted`` : The BGP peer is deleted and cannot be established.

          - **bgpStatus** *(string) --*

            The status of the BGP peer. The following are the possible values:

            * ``up`` : The BGP peer is established. This state does not indicate the state of the
            routing function. Ensure that you are receiving routes over the BGP session.

            * ``down`` : The BGP peer is down.

            * ``unknown`` : The BGP peer status is not available.

          - **awsDeviceV2** *(string) --*

            The Direct Connect endpoint on which the BGP peer terminates.

      - **region** *(string) --*

        The AWS Region where the virtual interface is located.

      - **awsDeviceV2** *(string) --*

        The Direct Connect endpoint on which the virtual interface terminates.

      - **tags** *(list) --*

        The tags associated with the virtual interface.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key.

          - **value** *(string) --*

            The value.
    """


_ClientCreateBgpPeernewBGPPeerTypeDef = TypedDict(
    "_ClientCreateBgpPeernewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)


class ClientCreateBgpPeernewBGPPeerTypeDef(_ClientCreateBgpPeernewBGPPeerTypeDef):
    """
    Type definition for `ClientCreateBgpPeer` `newBGPPeer`

    Information about the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.
    """


_ClientCreateConnectionResponsetagsTypeDef = TypedDict(
    "_ClientCreateConnectionResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateConnectionResponsetagsTypeDef(
    _ClientCreateConnectionResponsetagsTypeDef
):
    """
    Type definition for `ClientCreateConnectionResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateConnectionResponseTypeDef = TypedDict(
    "_ClientCreateConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientCreateConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateConnectionResponseTypeDef(_ClientCreateConnectionResponseTypeDef):
    """
    Type definition for `ClientCreateConnection` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_RequiredClientCreateConnectiontagsTypeDef = TypedDict(
    "_RequiredClientCreateConnectiontagsTypeDef", {"key": str}
)
_OptionalClientCreateConnectiontagsTypeDef = TypedDict(
    "_OptionalClientCreateConnectiontagsTypeDef", {"value": str}, total=False
)


class ClientCreateConnectiontagsTypeDef(
    _RequiredClientCreateConnectiontagsTypeDef,
    _OptionalClientCreateConnectiontagsTypeDef,
):
    """
    Type definition for `ClientCreateConnection` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `existingAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `requestedAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": str,
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposalResponse` `directConnectGatewayAssociationProposal`

    Information about the Direct Connect gateway proposal.

    - **proposalId** *(string) --*

      The ID of the association proposal.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **proposalState** *(string) --*

      The state of the proposal. The following are possible values:

      * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association is
      available to use in this state.

      * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
      Direct Connect gateway association cannot be used in this state.

      * ``requested`` : The proposal has been requested. The Direct Connect gateway association
      cannot be used in this state.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

      The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposal` `Response`

    - **directConnectGatewayAssociationProposal** *(dict) --*

      Information about the Direct Connect gateway proposal.

      - **proposalId** *(string) --*

        The ID of the association proposal.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the Direct Connect gateway.

      - **proposalState** *(string) --*

        The state of the proposal. The following are possible values:

        * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association is
        available to use in this state.

        * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
        Direct Connect gateway association cannot be used in this state.

        * ``requested`` : The proposal has been requested. The Direct Connect gateway association
        cannot be used in this state.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

        The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposaladdAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposaladdAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposaladdAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposaladdAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposal` `addAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalremoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalremoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalremoveAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalremoveAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationProposal` `removeAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociationResponse` `directConnectGatewayAssociation`

    The association to be created.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
      the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
      private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_ClientCreateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponseTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponseTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociation` `Response`

    - **directConnectGatewayAssociation** *(dict) --*

      The association to be created.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the associated gateway.

      - **associationState** *(string) --*

        The state of the association. The following are the possible values:

        * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

        * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
        gateway are successfully associated and ready to pass traffic.

        * ``disassociating`` : The initial state after calling
        DeleteDirectConnectGatewayAssociation .

        * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
        the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
        private gateway or transit gateway is stopped.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **associationId** *(string) --*

        The ID of the Direct Connect gateway association.

      - **allowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **virtualGatewayRegion** *(string) --*

        The AWS Region where the virtual private gateway is located.

      - **virtualGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the virtual private gateway.
    """


_ClientCreateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayAssociation` `addAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": str,
        "stateChangeError": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGatewayResponse` `directConnectGateway`

    The Direct Connect gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayName** *(string) --*

      The name of the Direct Connect gateway.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **directConnectGatewayState** *(string) --*

      The state of the Direct Connect gateway. The following are the possible values:

      * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

      * ``available`` : The Direct Connect gateway is ready for use.

      * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

      * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_ClientCreateDirectConnectGatewayResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayResponseTypeDef",
    {
        "directConnectGateway": ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef
    },
    total=False,
)


class ClientCreateDirectConnectGatewayResponseTypeDef(
    _ClientCreateDirectConnectGatewayResponseTypeDef
):
    """
    Type definition for `ClientCreateDirectConnectGateway` `Response`

    - **directConnectGateway** *(dict) --*

      The Direct Connect gateway.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayName** *(string) --*

        The name of the Direct Connect gateway.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the Direct Connect gateway.

      - **directConnectGatewayState** *(string) --*

        The state of the Direct Connect gateway. The following are the possible values:

        * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

        * ``available`` : The Direct Connect gateway is ready for use.

        * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

        * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.
    """


_ClientCreateInterconnectResponsetagsTypeDef = TypedDict(
    "_ClientCreateInterconnectResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateInterconnectResponsetagsTypeDef(
    _ClientCreateInterconnectResponsetagsTypeDef
):
    """
    Type definition for `ClientCreateInterconnectResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateInterconnectResponseTypeDef = TypedDict(
    "_ClientCreateInterconnectResponseTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientCreateInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateInterconnectResponseTypeDef(_ClientCreateInterconnectResponseTypeDef):
    """
    Type definition for `ClientCreateInterconnect` `Response`

    Information about an interconnect.

    - **interconnectId** *(string) --*

      The ID of the interconnect.

    - **interconnectName** *(string) --*

      The name of the interconnect.

    - **interconnectState** *(string) --*

      The state of the interconnect. The following are the possible values:

      * ``requested`` : The initial state of an interconnect. The interconnect stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The interconnect is approved, and is being initialized.

      * ``available`` : The network link is up, and the interconnect is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The interconnect is being deleted.

      * ``deleted`` : The interconnect is deleted.

      * ``unknown`` : The state of the interconnect is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the interconnect supports a secondary BGP in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the interconnect.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the interconnect.
    """


_RequiredClientCreateInterconnecttagsTypeDef = TypedDict(
    "_RequiredClientCreateInterconnecttagsTypeDef", {"key": str}
)
_OptionalClientCreateInterconnecttagsTypeDef = TypedDict(
    "_OptionalClientCreateInterconnecttagsTypeDef", {"value": str}, total=False
)


class ClientCreateInterconnecttagsTypeDef(
    _RequiredClientCreateInterconnecttagsTypeDef,
    _OptionalClientCreateInterconnecttagsTypeDef,
):
    """
    Type definition for `ClientCreateInterconnect` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientCreateLagResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateLagResponseconnectionstagsTypeDef(
    _ClientCreateLagResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientCreateLagResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateLagResponseconnectionsTypeDef = TypedDict(
    "_ClientCreateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientCreateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateLagResponseconnectionsTypeDef(
    _ClientCreateLagResponseconnectionsTypeDef
):
    """
    Type definition for `ClientCreateLagResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientCreateLagResponsetagsTypeDef = TypedDict(
    "_ClientCreateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateLagResponsetagsTypeDef(_ClientCreateLagResponsetagsTypeDef):
    """
    Type definition for `ClientCreateLagResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateLagResponseTypeDef = TypedDict(
    "_ClientCreateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": str,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientCreateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": str,
        "tags": List[ClientCreateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateLagResponseTypeDef(_ClientCreateLagResponseTypeDef):
    """
    Type definition for `ClientCreateLag` `Response`

    Information about a link aggregation group (LAG).

    - **connectionsBandwidth** *(string) --*

      The individual bandwidth of the physical connections bundled by the LAG. The possible values
      are 1Gbps and 10Gbps.

    - **numberOfConnections** *(integer) --*

      The number of physical connections bundled by the LAG, up to a maximum of 10.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the LAG.

    - **lagName** *(string) --*

      The name of the LAG.

    - **lagState** *(string) --*

      The state of the LAG. The following are the possible values:

      * ``requested`` : The initial state of a LAG. The LAG stays in the requested state until the
      Letter of Authorization (LOA) is available.

      * ``pending`` : The LAG has been approved and is being initialized.

      * ``available`` : The network link is established and the LAG is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The LAG is being deleted.

      * ``deleted`` : The LAG is deleted.

      * ``unknown`` : The state of the LAG is not available.

    - **location** *(string) --*

      The location of the LAG.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **minimumLinks** *(integer) --*

      The minimum number of physical connections that must be operational for the LAG itself to be
      operational.

    - **awsDevice** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **awsDeviceV2** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **connections** *(list) --*

      The connections bundled by the LAG.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.

    - **allowsHostedConnections** *(boolean) --*

      Indicates whether the LAG can host other connections.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the LAG supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the LAG.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the LAG.
    """


_RequiredClientCreateLagchildConnectionTagsTypeDef = TypedDict(
    "_RequiredClientCreateLagchildConnectionTagsTypeDef", {"key": str}
)
_OptionalClientCreateLagchildConnectionTagsTypeDef = TypedDict(
    "_OptionalClientCreateLagchildConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagchildConnectionTagsTypeDef(
    _RequiredClientCreateLagchildConnectionTagsTypeDef,
    _OptionalClientCreateLagchildConnectionTagsTypeDef,
):
    """
    Type definition for `ClientCreateLag` `childConnectionTags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_RequiredClientCreateLagtagsTypeDef = TypedDict(
    "_RequiredClientCreateLagtagsTypeDef", {"key": str}
)
_OptionalClientCreateLagtagsTypeDef = TypedDict(
    "_OptionalClientCreateLagtagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagtagsTypeDef(
    _RequiredClientCreateLagtagsTypeDef, _OptionalClientCreateLagtagsTypeDef
):
    """
    Type definition for `ClientCreateLag` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientCreatePrivateVirtualInterfaceResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientCreatePrivateVirtualInterfaceResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef
):
    """
    Type definition for `ClientCreatePrivateVirtualInterfaceResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponseTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientCreatePrivateVirtualInterface` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef = TypedDict(
    "_RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef",
    {"key": str},
)
_OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef = TypedDict(
    "_OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef(
    _RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef,
    _OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef,
):
    """
    Type definition for `ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "tags": List[
            ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfacetagsTypeDef
        ],
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef(
    _RequiredClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef,
    _OptionalClientCreatePrivateVirtualInterfacenewPrivateVirtualInterfaceTypeDef,
):
    """
    Type definition for `ClientCreatePrivateVirtualInterface` `newPrivateVirtualInterface`

    Information about the private virtual interface.

    - **virtualInterfaceName** *(string) --* **[REQUIRED]**

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --* **[REQUIRED]**

      The ID of the VLAN.

    - **asn** *(integer) --* **[REQUIRED]**

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **tags** *(list) --*

      The tags associated with the private virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientCreatePublicVirtualInterfaceResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientCreatePublicVirtualInterfaceResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponsetagsTypeDef(
    _ClientCreatePublicVirtualInterfaceResponsetagsTypeDef
):
    """
    Type definition for `ClientCreatePublicVirtualInterfaceResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponseTypeDef(
    _ClientCreatePublicVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientCreatePublicVirtualInterface` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientCreatePublicVirtualInterfacenewPublicVirtualInterface` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef = TypedDict(
    "_RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef",
    {"key": str},
)
_OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef = TypedDict(
    "_OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef(
    _RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef,
    _OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef,
):
    """
    Type definition for `ClientCreatePublicVirtualInterfacenewPublicVirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "tags": List[
            ClientCreatePublicVirtualInterfacenewPublicVirtualInterfacetagsTypeDef
        ],
    },
    total=False,
)


class ClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef(
    _RequiredClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef,
    _OptionalClientCreatePublicVirtualInterfacenewPublicVirtualInterfaceTypeDef,
):
    """
    Type definition for `ClientCreatePublicVirtualInterface` `newPublicVirtualInterface`

    Information about the public virtual interface.

    - **virtualInterfaceName** *(string) --* **[REQUIRED]**

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --* **[REQUIRED]**

      The ID of the VLAN.

    - **asn** *(integer) --* **[REQUIRED]**

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border Gateway
        Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **tags** *(list) --*

      The tags associated with the public virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterfaceResponsevirtualInterface` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
      peer can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterfaceResponsevirtualInterface` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterfaceResponsevirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterfaceResponse` `virtualInterface`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner
      of the connection on which it is provisioned, then the virtual interface will remain in
      this state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual
      interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
      interface owner, the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
          peer can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientCreateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterface": ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponseTypeDef(
    _ClientCreateTransitVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterface` `Response`

    - **virtualInterface** *(dict) --*

      Information about a virtual interface.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.

      - **virtualInterfaceId** *(string) --*

        The ID of the virtual interface.

      - **location** *(string) --*

        The location of the connection.

      - **connectionId** *(string) --*

        The ID of the connection.

      - **virtualInterfaceType** *(string) --*

        The type of virtual interface. The possible values are ``private`` and ``public`` .

      - **virtualInterfaceName** *(string) --*

        The name of the virtual interface assigned by the customer network.

      - **vlan** *(integer) --*

        The ID of the VLAN.

      - **asn** *(integer) --*

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        The valid values are 1-2147483647.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **authKey** *(string) --*

        The authentication key for BGP configuration. This string has a minimum length of 6
        characters and and a maximun lenth of 80 characters.

      - **amazonAddress** *(string) --*

        The IP address assigned to the Amazon interface.

      - **customerAddress** *(string) --*

        The IP address assigned to the customer interface.

      - **addressFamily** *(string) --*

        The address family for the BGP peer.

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:

        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in
        this state until it is confirmed by the virtual interface owner.

        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.

        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.

        * ``available`` : A virtual interface that is able to forward traffic.

        * ``down`` : A virtual interface that is BGP down.

        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.

        * ``deleted`` : A virtual interface that cannot forward traffic.

        * ``rejected`` : The virtual interface owner has declined creation of the virtual
        interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
        interface owner, the virtual interface enters the ``Rejected`` state.

        * ``unknown`` : The state of the virtual interface is not available.

      - **customerRouterConfig** *(string) --*

        The customer router configuration.

      - **mtu** *(integer) --*

        The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
        default value is 1500.

      - **jumboFrameCapable** *(boolean) --*

        Indicates whether jumbo frames (9001 MTU) are supported.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **routeFilterPrefixes** *(list) --*

        The routes to be advertised to the AWS network in this Region. Applies to public virtual
        interfaces.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **bgpPeers** *(list) --*

        The BGP peers configured on this virtual interface.

        - *(dict) --*

          Information about a BGP peer.

          - **bgpPeerId** *(string) --*

            The ID of the BGP peer.

          - **asn** *(integer) --*

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

          - **authKey** *(string) --*

            The authentication key for BGP configuration. This string has a minimum length of 6
            characters and and a maximun lenth of 80 characters.

          - **addressFamily** *(string) --*

            The address family for the BGP peer.

          - **amazonAddress** *(string) --*

            The IP address assigned to the Amazon interface.

          - **customerAddress** *(string) --*

            The IP address assigned to the customer interface.

          - **bgpPeerState** *(string) --*

            The state of the BGP peer. The following are the possible values:

            * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
            peer can be created. This state applies only to public virtual interfaces.

            * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
            be established.

            * ``available`` : The BGP peer is ready to be established.

            * ``deleting`` : The BGP peer is being deleted.

            * ``deleted`` : The BGP peer is deleted and cannot be established.

          - **bgpStatus** *(string) --*

            The status of the BGP peer. The following are the possible values:

            * ``up`` : The BGP peer is established. This state does not indicate the state of the
            routing function. Ensure that you are receiving routes over the BGP session.

            * ``down`` : The BGP peer is down.

            * ``unknown`` : The BGP peer status is not available.

          - **awsDeviceV2** *(string) --*

            The Direct Connect endpoint on which the BGP peer terminates.

      - **region** *(string) --*

        The AWS Region where the virtual interface is located.

      - **awsDeviceV2** *(string) --*

        The Direct Connect endpoint on which the virtual interface terminates.

      - **tags** *(list) --*

        The tags associated with the virtual interface.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key.

          - **value** *(string) --*

            The value.
    """


_RequiredClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef = TypedDict(
    "_RequiredClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef",
    {"key": str},
)
_OptionalClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef = TypedDict(
    "_OptionalClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef",
    {"value": str},
    total=False,
)


class ClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef(
    _RequiredClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef,
    _OptionalClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef,
):
    """
    Type definition for `ClientCreateTransitVirtualInterfacenewTransitVirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientCreateTransitVirtualInterfacenewTransitVirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfacenewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "directConnectGatewayId": str,
        "tags": List[
            ClientCreateTransitVirtualInterfacenewTransitVirtualInterfacetagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateTransitVirtualInterfacenewTransitVirtualInterfaceTypeDef(
    _ClientCreateTransitVirtualInterfacenewTransitVirtualInterfaceTypeDef
):
    """
    Type definition for `ClientCreateTransitVirtualInterface` `newTransitVirtualInterface`

    Information about the transit virtual interface.

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6 characters
      and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **tags** *(list) --*

      The tags associated with the transitive virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --* **[REQUIRED]**

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef
):
    """
    Type definition for `ClientDeleteBgpPeerResponsevirtualInterface` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
      peer can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientDeleteBgpPeerResponsevirtualInterface` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef
):
    """
    Type definition for `ClientDeleteBgpPeerResponsevirtualInterface` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef
):
    """
    Type definition for `ClientDeleteBgpPeerResponse` `virtualInterface`

    The virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner
      of the connection on which it is provisioned, then the virtual interface will remain in
      this state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual
      interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
      interface owner, the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
          peer can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientDeleteBgpPeerResponseTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponseTypeDef",
    {"virtualInterface": ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientDeleteBgpPeerResponseTypeDef(_ClientDeleteBgpPeerResponseTypeDef):
    """
    Type definition for `ClientDeleteBgpPeer` `Response`

    - **virtualInterface** *(dict) --*

      The virtual interface.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.

      - **virtualInterfaceId** *(string) --*

        The ID of the virtual interface.

      - **location** *(string) --*

        The location of the connection.

      - **connectionId** *(string) --*

        The ID of the connection.

      - **virtualInterfaceType** *(string) --*

        The type of virtual interface. The possible values are ``private`` and ``public`` .

      - **virtualInterfaceName** *(string) --*

        The name of the virtual interface assigned by the customer network.

      - **vlan** *(integer) --*

        The ID of the VLAN.

      - **asn** *(integer) --*

        The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        The valid values are 1-2147483647.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **authKey** *(string) --*

        The authentication key for BGP configuration. This string has a minimum length of 6
        characters and and a maximun lenth of 80 characters.

      - **amazonAddress** *(string) --*

        The IP address assigned to the Amazon interface.

      - **customerAddress** *(string) --*

        The IP address assigned to the customer interface.

      - **addressFamily** *(string) --*

        The address family for the BGP peer.

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:

        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in
        this state until it is confirmed by the virtual interface owner.

        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.

        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.

        * ``available`` : A virtual interface that is able to forward traffic.

        * ``down`` : A virtual interface that is BGP down.

        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.

        * ``deleted`` : A virtual interface that cannot forward traffic.

        * ``rejected`` : The virtual interface owner has declined creation of the virtual
        interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
        interface owner, the virtual interface enters the ``Rejected`` state.

        * ``unknown`` : The state of the virtual interface is not available.

      - **customerRouterConfig** *(string) --*

        The customer router configuration.

      - **mtu** *(integer) --*

        The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
        default value is 1500.

      - **jumboFrameCapable** *(boolean) --*

        Indicates whether jumbo frames (9001 MTU) are supported.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **routeFilterPrefixes** *(list) --*

        The routes to be advertised to the AWS network in this Region. Applies to public virtual
        interfaces.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **bgpPeers** *(list) --*

        The BGP peers configured on this virtual interface.

        - *(dict) --*

          Information about a BGP peer.

          - **bgpPeerId** *(string) --*

            The ID of the BGP peer.

          - **asn** *(integer) --*

            The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

          - **authKey** *(string) --*

            The authentication key for BGP configuration. This string has a minimum length of 6
            characters and and a maximun lenth of 80 characters.

          - **addressFamily** *(string) --*

            The address family for the BGP peer.

          - **amazonAddress** *(string) --*

            The IP address assigned to the Amazon interface.

          - **customerAddress** *(string) --*

            The IP address assigned to the customer interface.

          - **bgpPeerState** *(string) --*

            The state of the BGP peer. The following are the possible values:

            * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
            peer can be created. This state applies only to public virtual interfaces.

            * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
            be established.

            * ``available`` : The BGP peer is ready to be established.

            * ``deleting`` : The BGP peer is being deleted.

            * ``deleted`` : The BGP peer is deleted and cannot be established.

          - **bgpStatus** *(string) --*

            The status of the BGP peer. The following are the possible values:

            * ``up`` : The BGP peer is established. This state does not indicate the state of the
            routing function. Ensure that you are receiving routes over the BGP session.

            * ``down`` : The BGP peer is down.

            * ``unknown`` : The BGP peer status is not available.

          - **awsDeviceV2** *(string) --*

            The Direct Connect endpoint on which the BGP peer terminates.

      - **region** *(string) --*

        The AWS Region where the virtual interface is located.

      - **awsDeviceV2** *(string) --*

        The Direct Connect endpoint on which the virtual interface terminates.

      - **tags** *(list) --*

        The tags associated with the virtual interface.

        - *(dict) --*

          Information about a tag.

          - **key** *(string) --*

            The key.

          - **value** *(string) --*

            The value.
    """


_ClientDeleteConnectionResponsetagsTypeDef = TypedDict(
    "_ClientDeleteConnectionResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteConnectionResponsetagsTypeDef(
    _ClientDeleteConnectionResponsetagsTypeDef
):
    """
    Type definition for `ClientDeleteConnectionResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDeleteConnectionResponseTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDeleteConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteConnectionResponseTypeDef(_ClientDeleteConnectionResponseTypeDef):
    """
    Type definition for `ClientDeleteConnection` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `existingAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposal` `requestedAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": str,
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationProposalResponse` `directConnectGatewayAssociationProposal`

    The ID of the associated gateway.

    - **proposalId** *(string) --*

      The ID of the association proposal.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **proposalState** *(string) --*

      The state of the proposal. The following are possible values:

      * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association is
      available to use in this state.

      * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
      Direct Connect gateway association cannot be used in this state.

      * ``requested`` : The proposal has been requested. The Direct Connect gateway association
      cannot be used in this state.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

      The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationProposal` `Response`

    - **directConnectGatewayAssociationProposal** *(dict) --*

      The ID of the associated gateway.

      - **proposalId** *(string) --*

        The ID of the association proposal.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the Direct Connect gateway.

      - **proposalState** *(string) --*

        The state of the proposal. The following are possible values:

        * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association is
        available to use in this state.

        * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
        Direct Connect gateway association cannot be used in this state.

        * ``requested`` : The proposal has been requested. The Direct Connect gateway association
        cannot be used in this state.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

        The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.
    """


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociationResponse` `directConnectGatewayAssociation`

    Information about the deleted association.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
      the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
      private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_ClientDeleteDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponseTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponseTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayAssociation` `Response`

    - **directConnectGatewayAssociation** *(dict) --*

      Information about the deleted association.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the associated gateway.

      - **associationState** *(string) --*

        The state of the association. The following are the possible values:

        * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

        * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
        gateway are successfully associated and ready to pass traffic.

        * ``disassociating`` : The initial state after calling
        DeleteDirectConnectGatewayAssociation .

        * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
        the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
        private gateway or transit gateway is stopped.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **associationId** *(string) --*

        The ID of the Direct Connect gateway association.

      - **allowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **virtualGatewayRegion** *(string) --*

        The AWS Region where the virtual private gateway is located.

      - **virtualGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the virtual private gateway.
    """


_ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": str,
        "stateChangeError": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGatewayResponse` `directConnectGateway`

    The Direct Connect gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayName** *(string) --*

      The name of the Direct Connect gateway.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **directConnectGatewayState** *(string) --*

      The state of the Direct Connect gateway. The following are the possible values:

      * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

      * ``available`` : The Direct Connect gateway is ready for use.

      * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

      * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_ClientDeleteDirectConnectGatewayResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayResponseTypeDef",
    {
        "directConnectGateway": ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayResponseTypeDef(
    _ClientDeleteDirectConnectGatewayResponseTypeDef
):
    """
    Type definition for `ClientDeleteDirectConnectGateway` `Response`

    - **directConnectGateway** *(dict) --*

      The Direct Connect gateway.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayName** *(string) --*

        The name of the Direct Connect gateway.

      - **amazonSideAsn** *(integer) --*

        The autonomous system number (ASN) for the Amazon side of the connection.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the Direct Connect gateway.

      - **directConnectGatewayState** *(string) --*

        The state of the Direct Connect gateway. The following are the possible values:

        * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

        * ``available`` : The Direct Connect gateway is ready for use.

        * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

        * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.
    """


_ClientDeleteInterconnectResponseTypeDef = TypedDict(
    "_ClientDeleteInterconnectResponseTypeDef", {"interconnectState": str}, total=False
)


class ClientDeleteInterconnectResponseTypeDef(_ClientDeleteInterconnectResponseTypeDef):
    """
    Type definition for `ClientDeleteInterconnect` `Response`

    - **interconnectState** *(string) --*

      The state of the interconnect. The following are the possible values:

      * ``requested`` : The initial state of an interconnect. The interconnect stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The interconnect is approved, and is being initialized.

      * ``available`` : The network link is up, and the interconnect is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The interconnect is being deleted.

      * ``deleted`` : The interconnect is deleted.

      * ``unknown`` : The state of the interconnect is not available.
    """


_ClientDeleteLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDeleteLagResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteLagResponseconnectionstagsTypeDef(
    _ClientDeleteLagResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientDeleteLagResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDeleteLagResponseconnectionsTypeDef = TypedDict(
    "_ClientDeleteLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDeleteLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteLagResponseconnectionsTypeDef(
    _ClientDeleteLagResponseconnectionsTypeDef
):
    """
    Type definition for `ClientDeleteLagResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDeleteLagResponsetagsTypeDef = TypedDict(
    "_ClientDeleteLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteLagResponsetagsTypeDef(_ClientDeleteLagResponsetagsTypeDef):
    """
    Type definition for `ClientDeleteLagResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDeleteLagResponseTypeDef = TypedDict(
    "_ClientDeleteLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": str,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDeleteLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDeleteLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteLagResponseTypeDef(_ClientDeleteLagResponseTypeDef):
    """
    Type definition for `ClientDeleteLag` `Response`

    Information about a link aggregation group (LAG).

    - **connectionsBandwidth** *(string) --*

      The individual bandwidth of the physical connections bundled by the LAG. The possible values
      are 1Gbps and 10Gbps.

    - **numberOfConnections** *(integer) --*

      The number of physical connections bundled by the LAG, up to a maximum of 10.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the LAG.

    - **lagName** *(string) --*

      The name of the LAG.

    - **lagState** *(string) --*

      The state of the LAG. The following are the possible values:

      * ``requested`` : The initial state of a LAG. The LAG stays in the requested state until the
      Letter of Authorization (LOA) is available.

      * ``pending`` : The LAG has been approved and is being initialized.

      * ``available`` : The network link is established and the LAG is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The LAG is being deleted.

      * ``deleted`` : The LAG is deleted.

      * ``unknown`` : The state of the LAG is not available.

    - **location** *(string) --*

      The location of the LAG.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **minimumLinks** *(integer) --*

      The minimum number of physical connections that must be operational for the LAG itself to be
      operational.

    - **awsDevice** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **awsDeviceV2** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **connections** *(list) --*

      The connections bundled by the LAG.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.

    - **allowsHostedConnections** *(boolean) --*

      Indicates whether the LAG can host other connections.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the LAG supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the LAG.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the LAG.
    """


_ClientDeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualInterfaceResponseTypeDef",
    {"virtualInterfaceState": str},
    total=False,
)


class ClientDeleteVirtualInterfaceResponseTypeDef(
    _ClientDeleteVirtualInterfaceResponseTypeDef
):
    """
    Type definition for `ClientDeleteVirtualInterface` `Response`

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientDescribeConnectionLoaResponseloaTypeDef = TypedDict(
    "_ClientDescribeConnectionLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)


class ClientDescribeConnectionLoaResponseloaTypeDef(
    _ClientDescribeConnectionLoaResponseloaTypeDef
):
    """
    Type definition for `ClientDescribeConnectionLoaResponse` `loa`

    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

    - **loaContent** *(bytes) --*

      The binary contents of the LOA-CFA document.

    - **loaContentType** *(string) --*

      The standard media type for the LOA-CFA document. The only supported value is
      application/pdf.
    """


_ClientDescribeConnectionLoaResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionLoaResponseTypeDef",
    {"loa": ClientDescribeConnectionLoaResponseloaTypeDef},
    total=False,
)


class ClientDescribeConnectionLoaResponseTypeDef(
    _ClientDescribeConnectionLoaResponseTypeDef
):
    """
    Type definition for `ClientDescribeConnectionLoa` `Response`

    - **loa** *(dict) --*

      The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

      - **loaContent** *(bytes) --*

        The binary contents of the LOA-CFA document.

      - **loaContentType** *(string) --*

        The standard media type for the LOA-CFA document. The only supported value is
        application/pdf.
    """


_ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsOnInterconnectResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[
            ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef
        ],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsOnInterconnectResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDescribeConnectionsOnInterconnectResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    {
        "connections": List[
            ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsOnInterconnect` `Response`

    - **connections** *(list) --*

      The connections.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.
    """


_ClientDescribeConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeConnectionsResponseconnectionstagsTypeDef(
    _ClientDescribeConnectionsResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeConnectionsResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDescribeConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeConnectionsResponseconnectionsTypeDef(
    _ClientDescribeConnectionsResponseconnectionsTypeDef
):
    """
    Type definition for `ClientDescribeConnectionsResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeConnectionsResponseconnectionsTypeDef]},
    total=False,
)


class ClientDescribeConnectionsResponseTypeDef(
    _ClientDescribeConnectionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConnections` `Response`

    - **connections** *(list) --*

      The connections.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposals` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposals` `existingAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An
      IPv6 CIDR must use /64 or shorter.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposals` `requestedAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An
      IPv6 CIDR must use /64 or shorter.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": str,
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationProposalsResponse` `directConnectGatewayAssociationProposals`

    Information about the proposal request to attach a virtual private gateway to a Direct
    Connect gateway.

    - **proposalId** *(string) --*

      The ID of the association proposal.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **proposalState** *(string) --*

      The state of the proposal. The following are possible values:

      * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association
      is available to use in this state.

      * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
      Direct Connect gateway association cannot be used in this state.

      * ``requested`` : The proposal has been requested. The Direct Connect gateway association
      cannot be used in this state.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

      The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An
          IPv6 CIDR must use /64 or shorter.

    - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An
          IPv6 CIDR must use /64 or shorter.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationProposals` `Response`

    - **directConnectGatewayAssociationProposals** *(list) --*

      Describes the Direct Connect gateway association proposals.

      - *(dict) --*

        Information about the proposal request to attach a virtual private gateway to a Direct
        Connect gateway.

        - **proposalId** *(string) --*

          The ID of the association proposal.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **directConnectGatewayOwnerAccount** *(string) --*

          The ID of the AWS account that owns the Direct Connect gateway.

        - **proposalState** *(string) --*

          The state of the proposal. The following are possible values:

          * ``accepted`` : The proposal has been accepted. The Direct Connect gateway association
          is available to use in this state.

          * ``deleted`` : The proposal has been deleted by the owner that made the proposal. The
          Direct Connect gateway association cannot be used in this state.

          * ``requested`` : The proposal has been requested. The Direct Connect gateway association
          cannot be used in this state.

        - **associatedGateway** *(dict) --*

          Information about the associated gateway.

          - **id** *(string) --*

            The ID of the associated gateway.

          - **type** *(string) --*

            The type of associated gateway.

          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the associated virtual private gateway or transit
            gateway.

          - **region** *(string) --*

            The Region where the associated gateway is located.

        - **existingAllowedPrefixesToDirectConnectGateway** *(list) --*

          The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

          - *(dict) --*

            Information about a route filter prefix that a customer can advertise through Border
            Gateway Protocol (BGP) over a public virtual interface.

            - **cidr** *(string) --*

              The CIDR block for the advertised route. Separate multiple routes using commas. An
              IPv6 CIDR must use /64 or shorter.

        - **requestedAllowedPrefixesToDirectConnectGateway** *(list) --*

          The Amazon VPC prefixes to advertise to the Direct Connect gateway.

          - *(dict) --*

            Information about a route filter prefix that a customer can advertise through Border
            Gateway Protocol (BGP) over a public virtual interface.

            - **cidr** *(string) --*

              The CIDR block for the advertised route. Separate multiple routes using commas. An
              IPv6 CIDR must use /64 or shorter.

    - **nextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is ``null`` when there are
      no more results to return.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociations` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An
      IPv6 CIDR must use /64 or shorter.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociations` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociationsResponse` `directConnectGatewayAssociations`

    Information about an association between a Direct Connect gateway and a virtual private
    gateway or transit gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling
      CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated
      from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and
      virtual private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An
          IPv6 CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    {
        "directConnectGatewayAssociations": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAssociations` `Response`

    - **directConnectGatewayAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Information about an association between a Direct Connect gateway and a virtual private
        gateway or transit gateway.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **directConnectGatewayOwnerAccount** *(string) --*

          The ID of the AWS account that owns the associated gateway.

        - **associationState** *(string) --*

          The state of the association. The following are the possible values:

          * ``associating`` : The initial state after calling
          CreateDirectConnectGatewayAssociation .

          * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
          gateway are successfully associated and ready to pass traffic.

          * ``disassociating`` : The initial state after calling
          DeleteDirectConnectGatewayAssociation .

          * ``disassociated`` : The virtual private gateway or transit gateway is disassociated
          from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and
          virtual private gateway or transit gateway is stopped.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

        - **associatedGateway** *(dict) --*

          Information about the associated gateway.

          - **id** *(string) --*

            The ID of the associated gateway.

          - **type** *(string) --*

            The type of associated gateway.

          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the associated virtual private gateway or transit
            gateway.

          - **region** *(string) --*

            The Region where the associated gateway is located.

        - **associationId** *(string) --*

          The ID of the Direct Connect gateway association.

        - **allowedPrefixesToDirectConnectGateway** *(list) --*

          The Amazon VPC prefixes to advertise to the Direct Connect gateway.

          - *(dict) --*

            Information about a route filter prefix that a customer can advertise through Border
            Gateway Protocol (BGP) over a public virtual interface.

            - **cidr** *(string) --*

              The CIDR block for the advertised route. Separate multiple routes using commas. An
              IPv6 CIDR must use /64 or shorter.

        - **virtualGatewayId** *(string) --*

          The ID of the virtual private gateway. Applies only to private virtual interfaces.

        - **virtualGatewayRegion** *(string) --*

          The AWS Region where the virtual private gateway is located.

        - **virtualGatewayOwnerAccount** *(string) --*

          The ID of the AWS account that owns the virtual private gateway.

    - **nextToken** *(string) --*

      The token to retrieve the next page.
    """


_ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": str,
        "attachmentType": str,
        "stateChangeError": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef(
    _ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAttachmentsResponse` `directConnectGatewayAttachments`

    Information about an attachment between a Direct Connect gateway and a virtual interface.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **virtualInterfaceRegion** *(string) --*

      The AWS Region where the virtual interface is located.

    - **virtualInterfaceOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **attachmentState** *(string) --*

      The state of the attachment. The following are the possible values:

      * ``attaching`` : The initial state after a virtual interface is created using the Direct
      Connect gateway.

      * ``attached`` : The Direct Connect gateway and virtual interface are attached and ready
      to pass traffic.

      * ``detaching`` : The initial state after calling  DeleteVirtualInterface .

      * ``detached`` : The virtual interface is detached from the Direct Connect gateway.
      Traffic flow between the Direct Connect gateway and virtual interface is stopped.

    - **attachmentType** *(string) --*

      The type of attachment.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    {
        "directConnectGatewayAttachments": List[
            ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewayAttachments` `Response`

    - **directConnectGatewayAttachments** *(list) --*

      The attachments.

      - *(dict) --*

        Information about an attachment between a Direct Connect gateway and a virtual interface.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **virtualInterfaceId** *(string) --*

          The ID of the virtual interface.

        - **virtualInterfaceRegion** *(string) --*

          The AWS Region where the virtual interface is located.

        - **virtualInterfaceOwnerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.

        - **attachmentState** *(string) --*

          The state of the attachment. The following are the possible values:

          * ``attaching`` : The initial state after a virtual interface is created using the Direct
          Connect gateway.

          * ``attached`` : The Direct Connect gateway and virtual interface are attached and ready
          to pass traffic.

          * ``detaching`` : The initial state after calling  DeleteVirtualInterface .

          * ``detached`` : The virtual interface is detached from the Direct Connect gateway.
          Traffic flow between the Direct Connect gateway and virtual interface is stopped.

        - **attachmentType** *(string) --*

          The type of attachment.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

    - **nextToken** *(string) --*

      The token to retrieve the next page.
    """


_ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": str,
        "stateChangeError": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef(
    _ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGatewaysResponse` `directConnectGateways`

    Information about a Direct Connect gateway, which enables you to connect virtual interfaces
    and virtual private gateway or transit gateways.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayName** *(string) --*

      The name of the Direct Connect gateway.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **directConnectGatewayState** *(string) --*

      The state of the Direct Connect gateway. The following are the possible values:

      * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

      * ``available`` : The Direct Connect gateway is ready for use.

      * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

      * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_ClientDescribeDirectConnectGatewaysResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewaysResponseTypeDef",
    {
        "directConnectGateways": List[
            ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewaysResponseTypeDef(
    _ClientDescribeDirectConnectGatewaysResponseTypeDef
):
    """
    Type definition for `ClientDescribeDirectConnectGateways` `Response`

    - **directConnectGateways** *(list) --*

      The Direct Connect gateways.

      - *(dict) --*

        Information about a Direct Connect gateway, which enables you to connect virtual interfaces
        and virtual private gateway or transit gateways.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **directConnectGatewayName** *(string) --*

          The name of the Direct Connect gateway.

        - **amazonSideAsn** *(integer) --*

          The autonomous system number (ASN) for the Amazon side of the connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the Direct Connect gateway.

        - **directConnectGatewayState** *(string) --*

          The state of the Direct Connect gateway. The following are the possible values:

          * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

          * ``available`` : The Direct Connect gateway is ready for use.

          * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

          * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

    - **nextToken** *(string) --*

      The token to retrieve the next page.
    """


_ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef(
    _ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientDescribeHostedConnectionsResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeHostedConnectionsResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeHostedConnectionsResponseconnectionsTypeDef(
    _ClientDescribeHostedConnectionsResponseconnectionsTypeDef
):
    """
    Type definition for `ClientDescribeHostedConnectionsResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDescribeHostedConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeHostedConnectionsResponseconnectionsTypeDef]},
    total=False,
)


class ClientDescribeHostedConnectionsResponseTypeDef(
    _ClientDescribeHostedConnectionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeHostedConnections` `Response`

    - **connections** *(list) --*

      The connections.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.
    """


_ClientDescribeInterconnectLoaResponseloaTypeDef = TypedDict(
    "_ClientDescribeInterconnectLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)


class ClientDescribeInterconnectLoaResponseloaTypeDef(
    _ClientDescribeInterconnectLoaResponseloaTypeDef
):
    """
    Type definition for `ClientDescribeInterconnectLoaResponse` `loa`

    The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

    - **loaContent** *(bytes) --*

      The binary contents of the LOA-CFA document.

    - **loaContentType** *(string) --*

      The standard media type for the LOA-CFA document. The only supported value is
      application/pdf.
    """


_ClientDescribeInterconnectLoaResponseTypeDef = TypedDict(
    "_ClientDescribeInterconnectLoaResponseTypeDef",
    {"loa": ClientDescribeInterconnectLoaResponseloaTypeDef},
    total=False,
)


class ClientDescribeInterconnectLoaResponseTypeDef(
    _ClientDescribeInterconnectLoaResponseTypeDef
):
    """
    Type definition for `ClientDescribeInterconnectLoa` `Response`

    - **loa** *(dict) --*

      The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).

      - **loaContent** *(bytes) --*

        The binary contents of the LOA-CFA document.

      - **loaContentType** *(string) --*

        The standard media type for the LOA-CFA document. The only supported value is
        application/pdf.
    """


_ClientDescribeInterconnectsResponseinterconnectstagsTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeInterconnectsResponseinterconnectstagsTypeDef(
    _ClientDescribeInterconnectsResponseinterconnectstagsTypeDef
):
    """
    Type definition for `ClientDescribeInterconnectsResponseinterconnects` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeInterconnectsResponseinterconnectsTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDescribeInterconnectsResponseinterconnectstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeInterconnectsResponseinterconnectsTypeDef(
    _ClientDescribeInterconnectsResponseinterconnectsTypeDef
):
    """
    Type definition for `ClientDescribeInterconnectsResponse` `interconnects`

    Information about an interconnect.

    - **interconnectId** *(string) --*

      The ID of the interconnect.

    - **interconnectName** *(string) --*

      The name of the interconnect.

    - **interconnectState** *(string) --*

      The state of the interconnect. The following are the possible values:

      * ``requested`` : The initial state of an interconnect. The interconnect stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The interconnect is approved, and is being initialized.

      * ``available`` : The network link is up, and the interconnect is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The interconnect is being deleted.

      * ``deleted`` : The interconnect is deleted.

      * ``unknown`` : The state of the interconnect is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the interconnect supports a secondary BGP in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the interconnect.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the interconnect.
    """


_ClientDescribeInterconnectsResponseTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseTypeDef",
    {"interconnects": List[ClientDescribeInterconnectsResponseinterconnectsTypeDef]},
    total=False,
)


class ClientDescribeInterconnectsResponseTypeDef(
    _ClientDescribeInterconnectsResponseTypeDef
):
    """
    Type definition for `ClientDescribeInterconnects` `Response`

    - **interconnects** *(list) --*

      The interconnects.

      - *(dict) --*

        Information about an interconnect.

        - **interconnectId** *(string) --*

          The ID of the interconnect.

        - **interconnectName** *(string) --*

          The name of the interconnect.

        - **interconnectState** *(string) --*

          The state of the interconnect. The following are the possible values:

          * ``requested`` : The initial state of an interconnect. The interconnect stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The interconnect is approved, and is being initialized.

          * ``available`` : The network link is up, and the interconnect is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The interconnect is being deleted.

          * ``deleted`` : The interconnect is deleted.

          * ``unknown`` : The state of the interconnect is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the interconnect supports a secondary BGP in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the interconnect.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the interconnect.
    """


_ClientDescribeLagsResponselagsconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeLagsResponselagsconnectionstagsTypeDef(
    _ClientDescribeLagsResponselagsconnectionstagsTypeDef
):
    """
    Type definition for `ClientDescribeLagsResponselagsconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeLagsResponselagsconnectionsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDescribeLagsResponselagsconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeLagsResponselagsconnectionsTypeDef(
    _ClientDescribeLagsResponselagsconnectionsTypeDef
):
    """
    Type definition for `ClientDescribeLagsResponselags` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an
      interconnect. The connection stays in the ordering state until the owner of the
      hosted connection confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in
      the requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the
      ``rejected`` state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address
      family (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientDescribeLagsResponselagstagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeLagsResponselagstagsTypeDef(
    _ClientDescribeLagsResponselagstagsTypeDef
):
    """
    Type definition for `ClientDescribeLagsResponselags` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeLagsResponselagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": str,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDescribeLagsResponselagsconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDescribeLagsResponselagstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeLagsResponselagsTypeDef(_ClientDescribeLagsResponselagsTypeDef):
    """
    Type definition for `ClientDescribeLagsResponse` `lags`

    Information about a link aggregation group (LAG).

    - **connectionsBandwidth** *(string) --*

      The individual bandwidth of the physical connections bundled by the LAG. The possible
      values are 1Gbps and 10Gbps.

    - **numberOfConnections** *(integer) --*

      The number of physical connections bundled by the LAG, up to a maximum of 10.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the LAG.

    - **lagName** *(string) --*

      The name of the LAG.

    - **lagState** *(string) --*

      The state of the LAG. The following are the possible values:

      * ``requested`` : The initial state of a LAG. The LAG stays in the requested state until
      the Letter of Authorization (LOA) is available.

      * ``pending`` : The LAG has been approved and is being initialized.

      * ``available`` : The network link is established and the LAG is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The LAG is being deleted.

      * ``deleted`` : The LAG is deleted.

      * ``unknown`` : The state of the LAG is not available.

    - **location** *(string) --*

      The location of the LAG.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **minimumLinks** *(integer) --*

      The minimum number of physical connections that must be operational for the LAG itself to
      be operational.

    - **awsDevice** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **awsDeviceV2** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **connections** *(list) --*

      The connections bundled by the LAG.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an
          interconnect. The connection stays in the ordering state until the owner of the
          hosted connection confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in
          the requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the
          ``rejected`` state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address
          family (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.

    - **allowsHostedConnections** *(boolean) --*

      Indicates whether the LAG can host other connections.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the LAG supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the LAG.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the LAG.
    """


_ClientDescribeLagsResponseTypeDef = TypedDict(
    "_ClientDescribeLagsResponseTypeDef",
    {"lags": List[ClientDescribeLagsResponselagsTypeDef]},
    total=False,
)


class ClientDescribeLagsResponseTypeDef(_ClientDescribeLagsResponseTypeDef):
    """
    Type definition for `ClientDescribeLags` `Response`

    - **lags** *(list) --*

      The LAGs.

      - *(dict) --*

        Information about a link aggregation group (LAG).

        - **connectionsBandwidth** *(string) --*

          The individual bandwidth of the physical connections bundled by the LAG. The possible
          values are 1Gbps and 10Gbps.

        - **numberOfConnections** *(integer) --*

          The number of physical connections bundled by the LAG, up to a maximum of 10.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the LAG.

        - **lagName** *(string) --*

          The name of the LAG.

        - **lagState** *(string) --*

          The state of the LAG. The following are the possible values:

          * ``requested`` : The initial state of a LAG. The LAG stays in the requested state until
          the Letter of Authorization (LOA) is available.

          * ``pending`` : The LAG has been approved and is being initialized.

          * ``available`` : The network link is established and the LAG is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The LAG is being deleted.

          * ``deleted`` : The LAG is deleted.

          * ``unknown`` : The state of the LAG is not available.

        - **location** *(string) --*

          The location of the LAG.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **minimumLinks** *(integer) --*

          The minimum number of physical connections that must be operational for the LAG itself to
          be operational.

        - **awsDevice** *(string) --*

          The AWS Direct Connect endpoint that hosts the LAG.

        - **awsDeviceV2** *(string) --*

          The AWS Direct Connect endpoint that hosts the LAG.

        - **connections** *(list) --*

          The connections bundled by the LAG.

          - *(dict) --*

            Information about an AWS Direct Connect connection.

            - **ownerAccount** *(string) --*

              The ID of the AWS account that owns the connection.

            - **connectionId** *(string) --*

              The ID of the connection.

            - **connectionName** *(string) --*

              The name of the connection.

            - **connectionState** *(string) --*

              The state of the connection. The following are the possible values:

              * ``ordering`` : The initial state of a hosted connection provisioned on an
              interconnect. The connection stays in the ordering state until the owner of the
              hosted connection confirms or declines the connection order.

              * ``requested`` : The initial state of a standard connection. The connection stays in
              the requested state until the Letter of Authorization (LOA) is sent to the customer.

              * ``pending`` : The connection has been approved and is being initialized.

              * ``available`` : The network link is up and the connection is ready for use.

              * ``down`` : The network link is down.

              * ``deleting`` : The connection is being deleted.

              * ``deleted`` : The connection has been deleted.

              * ``rejected`` : A hosted connection in the ``ordering`` state enters the
              ``rejected`` state if it is deleted by the customer.

              * ``unknown`` : The state of the connection is not available.

            - **region** *(string) --*

              The AWS Region where the connection is located.

            - **location** *(string) --*

              The location of the connection.

            - **bandwidth** *(string) --*

              The bandwidth of the connection.

            - **vlan** *(integer) --*

              The ID of the VLAN.

            - **partnerName** *(string) --*

              The name of the AWS Direct Connect service provider associated with the connection.

            - **loaIssueTime** *(datetime) --*

              The time of the most recent call to  DescribeLoa for this connection.

            - **lagId** *(string) --*

              The ID of the LAG.

            - **awsDevice** *(string) --*

              The Direct Connect endpoint on which the physical connection terminates.

            - **jumboFrameCapable** *(boolean) --*

              Indicates whether jumbo frames (9001 MTU) are supported.

            - **awsDeviceV2** *(string) --*

              The Direct Connect endpoint on which the physical connection terminates.

            - **hasLogicalRedundancy** *(string) --*

              Indicates whether the connection supports a secondary BGP peer in the same address
              family (IPv4/IPv6).

            - **tags** *(list) --*

              The tags associated with the connection.

              - *(dict) --*

                Information about a tag.

                - **key** *(string) --*

                  The key.

                - **value** *(string) --*

                  The value.

            - **providerName** *(string) --*

              The name of the service provider associated with the connection.

        - **allowsHostedConnections** *(boolean) --*

          Indicates whether the LAG can host other connections.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the LAG supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the LAG.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the LAG.
    """


_ClientDescribeLoaResponseTypeDef = TypedDict(
    "_ClientDescribeLoaResponseTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)


class ClientDescribeLoaResponseTypeDef(_ClientDescribeLoaResponseTypeDef):
    """
    Type definition for `ClientDescribeLoa` `Response`

    Information about a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a
    connection.

    - **loaContent** *(bytes) --*

      The binary contents of the LOA-CFA document.

    - **loaContentType** *(string) --*

      The standard media type for the LOA-CFA document. The only supported value is application/pdf.
    """


_ClientDescribeLocationsResponselocationsTypeDef = TypedDict(
    "_ClientDescribeLocationsResponselocationsTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
    },
    total=False,
)


class ClientDescribeLocationsResponselocationsTypeDef(
    _ClientDescribeLocationsResponselocationsTypeDef
):
    """
    Type definition for `ClientDescribeLocationsResponse` `locations`

    Information about an AWS Direct Connect location.

    - **locationCode** *(string) --*

      The code for the location.

    - **locationName** *(string) --*

      The name of the location. This includes the name of the colocation partner and the
      physical site of the building.

    - **region** *(string) --*

      The AWS Region for the location.

    - **availablePortSpeeds** *(list) --*

      The available port speeds for the location.

      - *(string) --*

    - **availableProviders** *(list) --*

      The name of the service provider for the location.

      - *(string) --*
    """


_ClientDescribeLocationsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationsResponseTypeDef",
    {"locations": List[ClientDescribeLocationsResponselocationsTypeDef]},
    total=False,
)


class ClientDescribeLocationsResponseTypeDef(_ClientDescribeLocationsResponseTypeDef):
    """
    Type definition for `ClientDescribeLocations` `Response`

    - **locations** *(list) --*

      The locations.

      - *(dict) --*

        Information about an AWS Direct Connect location.

        - **locationCode** *(string) --*

          The code for the location.

        - **locationName** *(string) --*

          The name of the location. This includes the name of the colocation partner and the
          physical site of the building.

        - **region** *(string) --*

          The AWS Region for the location.

        - **availablePortSpeeds** *(list) --*

          The available port speeds for the location.

          - *(string) --*

        - **availableProviders** *(list) --*

          The name of the service provider for the location.

          - *(string) --*
    """


_ClientDescribeTagsResponseresourceTagstagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseresourceTagstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeTagsResponseresourceTagstagsTypeDef(
    _ClientDescribeTagsResponseresourceTagstagsTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponseresourceTags` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeTagsResponseresourceTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseresourceTagsTypeDef",
    {
        "resourceArn": str,
        "tags": List[ClientDescribeTagsResponseresourceTagstagsTypeDef],
    },
    total=False,
)


class ClientDescribeTagsResponseresourceTagsTypeDef(
    _ClientDescribeTagsResponseresourceTagsTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponse` `resourceTags`

    Information about a tag associated with an AWS Direct Connect resource.

    - **resourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **tags** *(list) --*

      The tags.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"resourceTags": List[ClientDescribeTagsResponseresourceTagsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **resourceTags** *(list) --*

      Information about the tags.

      - *(dict) --*

        Information about a tag associated with an AWS Direct Connect resource.

        - **resourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **tags** *(list) --*

          The tags.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.
    """


_ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef = TypedDict(
    "_ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    {"virtualGatewayId": str, "virtualGatewayState": str},
    total=False,
)


class ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef(
    _ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef
):
    """
    Type definition for `ClientDescribeVirtualGatewaysResponse` `virtualGateways`

    Information about a virtual private gateway for a private virtual interface.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway.

    - **virtualGatewayState** *(string) --*

      The state of the virtual private gateway. The following are the possible values:

      * ``pending`` : Initial state after creating the virtual private gateway.

      * ``available`` : Ready for use by a private virtual interface.

      * ``deleting`` : Initial state after deleting the virtual private gateway.

      * ``deleted`` : The virtual private gateway is deleted. The private virtual interface is
      unable to send traffic over this gateway.
    """


_ClientDescribeVirtualGatewaysResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualGatewaysResponseTypeDef",
    {
        "virtualGateways": List[
            ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVirtualGatewaysResponseTypeDef(
    _ClientDescribeVirtualGatewaysResponseTypeDef
):
    """
    Type definition for `ClientDescribeVirtualGateways` `Response`

    - **virtualGateways** *(list) --*

      The virtual private gateways.

      - *(dict) --*

        Information about a virtual private gateway for a private virtual interface.

        - **virtualGatewayId** *(string) --*

          The ID of the virtual private gateway.

        - **virtualGatewayState** *(string) --*

          The state of the virtual private gateway. The following are the possible values:

          * ``pending`` : Initial state after creating the virtual private gateway.

          * ``available`` : Ready for use by a private virtual interface.

          * ``deleting`` : Initial state after deleting the virtual private gateway.

          * ``deleted`` : The virtual private gateway is deleted. The private virtual interface is
          unable to send traffic over this gateway.
    """


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef
):
    """
    Type definition for `ClientDescribeVirtualInterfacesResponsevirtualInterfaces` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
      peer can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready
      to be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientDescribeVirtualInterfacesResponsevirtualInterfaces` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An
      IPv6 CIDR must use /64 or shorter.
    """


_ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef
):
    """
    Type definition for `ClientDescribeVirtualInterfacesResponsevirtualInterfaces` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef
):
    """
    Type definition for `ClientDescribeVirtualInterfacesResponse` `virtualInterfaces`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the
      owner of the connection on which it is provisioned, then the virtual interface will
      remain in this state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public
      virtual interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created
      until the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual
      interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
      interface owner, the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001.
      The default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An
          IPv6 CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
          peer can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready
          to be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_ClientDescribeVirtualInterfacesResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponseTypeDef",
    {
        "virtualInterfaces": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeVirtualInterfacesResponseTypeDef(
    _ClientDescribeVirtualInterfacesResponseTypeDef
):
    """
    Type definition for `ClientDescribeVirtualInterfaces` `Response`

    - **virtualInterfaces** *(list) --*

      The virtual interfaces

      - *(dict) --*

        Information about a virtual interface.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.

        - **virtualInterfaceId** *(string) --*

          The ID of the virtual interface.

        - **location** *(string) --*

          The location of the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **virtualInterfaceType** *(string) --*

          The type of virtual interface. The possible values are ``private`` and ``public`` .

        - **virtualInterfaceName** *(string) --*

          The name of the virtual interface assigned by the customer network.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

          The valid values are 1-2147483647.

        - **amazonSideAsn** *(integer) --*

          The autonomous system number (ASN) for the Amazon side of the connection.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **virtualInterfaceState** *(string) --*

          The state of the virtual interface. The following are the possible values:

          * ``confirming`` : The creation of the virtual interface is pending confirmation from the
          virtual interface owner. If the owner of the virtual interface is different from the
          owner of the connection on which it is provisioned, then the virtual interface will
          remain in this state until it is confirmed by the virtual interface owner.

          * ``verifying`` : This state only applies to public virtual interfaces. Each public
          virtual interface needs validation before the virtual interface can be created.

          * ``pending`` : A virtual interface is in this state from the time that it is created
          until the virtual interface is ready to forward traffic.

          * ``available`` : A virtual interface that is able to forward traffic.

          * ``down`` : A virtual interface that is BGP down.

          * ``deleting`` : A virtual interface is in this state immediately after calling
          DeleteVirtualInterface until it can no longer forward traffic.

          * ``deleted`` : A virtual interface that cannot forward traffic.

          * ``rejected`` : The virtual interface owner has declined creation of the virtual
          interface. If a virtual interface in the ``Confirming`` state is deleted by the virtual
          interface owner, the virtual interface enters the ``Rejected`` state.

          * ``unknown`` : The state of the virtual interface is not available.

        - **customerRouterConfig** *(string) --*

          The customer router configuration.

        - **mtu** *(integer) --*

          The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001.
          The default value is 1500.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **virtualGatewayId** *(string) --*

          The ID of the virtual private gateway. Applies only to private virtual interfaces.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **routeFilterPrefixes** *(list) --*

          The routes to be advertised to the AWS network in this Region. Applies to public virtual
          interfaces.

          - *(dict) --*

            Information about a route filter prefix that a customer can advertise through Border
            Gateway Protocol (BGP) over a public virtual interface.

            - **cidr** *(string) --*

              The CIDR block for the advertised route. Separate multiple routes using commas. An
              IPv6 CIDR must use /64 or shorter.

        - **bgpPeers** *(list) --*

          The BGP peers configured on this virtual interface.

          - *(dict) --*

            Information about a BGP peer.

            - **bgpPeerId** *(string) --*

              The ID of the BGP peer.

            - **asn** *(integer) --*

              The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

            - **authKey** *(string) --*

              The authentication key for BGP configuration. This string has a minimum length of 6
              characters and and a maximun lenth of 80 characters.

            - **addressFamily** *(string) --*

              The address family for the BGP peer.

            - **amazonAddress** *(string) --*

              The IP address assigned to the Amazon interface.

            - **customerAddress** *(string) --*

              The IP address assigned to the customer interface.

            - **bgpPeerState** *(string) --*

              The state of the BGP peer. The following are the possible values:

              * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP
              peer can be created. This state applies only to public virtual interfaces.

              * ``pending`` : The BGP peer is created, and remains in this state until it is ready
              to be established.

              * ``available`` : The BGP peer is ready to be established.

              * ``deleting`` : The BGP peer is being deleted.

              * ``deleted`` : The BGP peer is deleted and cannot be established.

            - **bgpStatus** *(string) --*

              The status of the BGP peer. The following are the possible values:

              * ``up`` : The BGP peer is established. This state does not indicate the state of the
              routing function. Ensure that you are receiving routes over the BGP session.

              * ``down`` : The BGP peer is down.

              * ``unknown`` : The BGP peer status is not available.

            - **awsDeviceV2** *(string) --*

              The Direct Connect endpoint on which the BGP peer terminates.

        - **region** *(string) --*

          The AWS Region where the virtual interface is located.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the virtual interface terminates.

        - **tags** *(list) --*

          The tags associated with the virtual interface.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.
    """


_ClientDisassociateConnectionFromLagResponsetagsTypeDef = TypedDict(
    "_ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDisassociateConnectionFromLagResponsetagsTypeDef(
    _ClientDisassociateConnectionFromLagResponsetagsTypeDef
):
    """
    Type definition for `ClientDisassociateConnectionFromLagResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientDisassociateConnectionFromLagResponseTypeDef = TypedDict(
    "_ClientDisassociateConnectionFromLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientDisassociateConnectionFromLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDisassociateConnectionFromLagResponseTypeDef(
    _ClientDisassociateConnectionFromLagResponseTypeDef
):
    """
    Type definition for `ClientDisassociateConnectionFromLag` `Response`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect. The
      connection stays in the ordering state until the owner of the hosted connection confirms or
      declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
      if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_RequiredClientTagResourcetagsTypeDef = TypedDict(
    "_RequiredClientTagResourcetagsTypeDef", {"key": str}
)
_OptionalClientTagResourcetagsTypeDef = TypedDict(
    "_OptionalClientTagResourcetagsTypeDef", {"value": str}, total=False
)


class ClientTagResourcetagsTypeDef(
    _RequiredClientTagResourcetagsTypeDef, _OptionalClientTagResourcetagsTypeDef
):
    """
    Type definition for `ClientTagResource` `tags`

    Information about a tag.

    - **key** *(string) --* **[REQUIRED]**

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociation` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociationResponse` `directConnectGatewayAssociation`

    Information about an association between a Direct Connect gateway and a virtual private
    gateway or transit gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
      the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
      private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_ClientUpdateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponseTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponseTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociation` `Response`

    - **directConnectGatewayAssociation** *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.

      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.

      - **directConnectGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the associated gateway.

      - **associationState** *(string) --*

        The state of the association. The following are the possible values:

        * ``associating`` : The initial state after calling  CreateDirectConnectGatewayAssociation .

        * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
        gateway are successfully associated and ready to pass traffic.

        * ``disassociating`` : The initial state after calling
        DeleteDirectConnectGatewayAssociation .

        * ``disassociated`` : The virtual private gateway or transit gateway is disassociated from
        the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual
        private gateway or transit gateway is stopped.

      - **stateChangeError** *(string) --*

        The error message if the state of an object failed to advance.

      - **associatedGateway** *(dict) --*

        Information about the associated gateway.

        - **id** *(string) --*

          The ID of the associated gateway.

        - **type** *(string) --*

          The type of associated gateway.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the associated virtual private gateway or transit
          gateway.

        - **region** *(string) --*

          The Region where the associated gateway is located.

      - **associationId** *(string) --*

        The ID of the Direct Connect gateway association.

      - **allowedPrefixesToDirectConnectGateway** *(list) --*

        The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        - *(dict) --*

          Information about a route filter prefix that a customer can advertise through Border
          Gateway Protocol (BGP) over a public virtual interface.

          - **cidr** *(string) --*

            The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
            CIDR must use /64 or shorter.

      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway. Applies only to private virtual interfaces.

      - **virtualGatewayRegion** *(string) --*

        The AWS Region where the virtual private gateway is located.

      - **virtualGatewayOwnerAccount** *(string) --*

        The ID of the AWS account that owns the virtual private gateway.
    """


_ClientUpdateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationaddAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociation` `addAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientUpdateDirectConnectGatewayAssociationremoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationremoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationremoveAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationremoveAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `ClientUpdateDirectConnectGatewayAssociation` `removeAllowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border Gateway
    Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
      must use /64 or shorter.
    """


_ClientUpdateLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientUpdateLagResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateLagResponseconnectionstagsTypeDef(
    _ClientUpdateLagResponseconnectionstagsTypeDef
):
    """
    Type definition for `ClientUpdateLagResponseconnections` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientUpdateLagResponseconnectionsTypeDef = TypedDict(
    "_ClientUpdateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": str,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": str,
        "tags": List[ClientUpdateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientUpdateLagResponseconnectionsTypeDef(
    _ClientUpdateLagResponseconnectionsTypeDef
):
    """
    Type definition for `ClientUpdateLagResponse` `connections`

    Information about an AWS Direct Connect connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **connectionName** *(string) --*

      The name of the connection.

    - **connectionState** *(string) --*

      The state of the connection. The following are the possible values:

      * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
      The connection stays in the ordering state until the owner of the hosted connection
      confirms or declines the connection order.

      * ``requested`` : The initial state of a standard connection. The connection stays in the
      requested state until the Letter of Authorization (LOA) is sent to the customer.

      * ``pending`` : The connection has been approved and is being initialized.

      * ``available`` : The network link is up and the connection is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The connection is being deleted.

      * ``deleted`` : The connection has been deleted.

      * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
      state if it is deleted by the customer.

      * ``unknown`` : The state of the connection is not available.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **location** *(string) --*

      The location of the connection.

    - **bandwidth** *(string) --*

      The bandwidth of the connection.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **partnerName** *(string) --*

      The name of the AWS Direct Connect service provider associated with the connection.

    - **loaIssueTime** *(datetime) --*

      The time of the most recent call to  DescribeLoa for this connection.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **awsDevice** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the physical connection terminates.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the connection supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the connection.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the connection.
    """


_ClientUpdateLagResponsetagsTypeDef = TypedDict(
    "_ClientUpdateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateLagResponsetagsTypeDef(_ClientUpdateLagResponsetagsTypeDef):
    """
    Type definition for `ClientUpdateLagResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientUpdateLagResponseTypeDef = TypedDict(
    "_ClientUpdateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": str,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientUpdateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": str,
        "tags": List[ClientUpdateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientUpdateLagResponseTypeDef(_ClientUpdateLagResponseTypeDef):
    """
    Type definition for `ClientUpdateLag` `Response`

    Information about a link aggregation group (LAG).

    - **connectionsBandwidth** *(string) --*

      The individual bandwidth of the physical connections bundled by the LAG. The possible values
      are 1Gbps and 10Gbps.

    - **numberOfConnections** *(integer) --*

      The number of physical connections bundled by the LAG, up to a maximum of 10.

    - **lagId** *(string) --*

      The ID of the LAG.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the LAG.

    - **lagName** *(string) --*

      The name of the LAG.

    - **lagState** *(string) --*

      The state of the LAG. The following are the possible values:

      * ``requested`` : The initial state of a LAG. The LAG stays in the requested state until the
      Letter of Authorization (LOA) is available.

      * ``pending`` : The LAG has been approved and is being initialized.

      * ``available`` : The network link is established and the LAG is ready for use.

      * ``down`` : The network link is down.

      * ``deleting`` : The LAG is being deleted.

      * ``deleted`` : The LAG is deleted.

      * ``unknown`` : The state of the LAG is not available.

    - **location** *(string) --*

      The location of the LAG.

    - **region** *(string) --*

      The AWS Region where the connection is located.

    - **minimumLinks** *(integer) --*

      The minimum number of physical connections that must be operational for the LAG itself to be
      operational.

    - **awsDevice** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **awsDeviceV2** *(string) --*

      The AWS Direct Connect endpoint that hosts the LAG.

    - **connections** *(list) --*

      The connections bundled by the LAG.

      - *(dict) --*

        Information about an AWS Direct Connect connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the connection.

        - **connectionId** *(string) --*

          The ID of the connection.

        - **connectionName** *(string) --*

          The name of the connection.

        - **connectionState** *(string) --*

          The state of the connection. The following are the possible values:

          * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
          The connection stays in the ordering state until the owner of the hosted connection
          confirms or declines the connection order.

          * ``requested`` : The initial state of a standard connection. The connection stays in the
          requested state until the Letter of Authorization (LOA) is sent to the customer.

          * ``pending`` : The connection has been approved and is being initialized.

          * ``available`` : The network link is up and the connection is ready for use.

          * ``down`` : The network link is down.

          * ``deleting`` : The connection is being deleted.

          * ``deleted`` : The connection has been deleted.

          * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected``
          state if it is deleted by the customer.

          * ``unknown`` : The state of the connection is not available.

        - **region** *(string) --*

          The AWS Region where the connection is located.

        - **location** *(string) --*

          The location of the connection.

        - **bandwidth** *(string) --*

          The bandwidth of the connection.

        - **vlan** *(integer) --*

          The ID of the VLAN.

        - **partnerName** *(string) --*

          The name of the AWS Direct Connect service provider associated with the connection.

        - **loaIssueTime** *(datetime) --*

          The time of the most recent call to  DescribeLoa for this connection.

        - **lagId** *(string) --*

          The ID of the LAG.

        - **awsDevice** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **jumboFrameCapable** *(boolean) --*

          Indicates whether jumbo frames (9001 MTU) are supported.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the physical connection terminates.

        - **hasLogicalRedundancy** *(string) --*

          Indicates whether the connection supports a secondary BGP peer in the same address family
          (IPv4/IPv6).

        - **tags** *(list) --*

          The tags associated with the connection.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key.

            - **value** *(string) --*

              The value.

        - **providerName** *(string) --*

          The name of the service provider associated with the connection.

    - **allowsHostedConnections** *(boolean) --*

      Indicates whether the LAG can host other connections.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **hasLogicalRedundancy** *(string) --*

      Indicates whether the LAG supports a secondary BGP peer in the same address family
      (IPv4/IPv6).

    - **tags** *(list) --*

      The tags associated with the LAG.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.

    - **providerName** *(string) --*

      The name of the service provider associated with the LAG.
    """


_ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": str,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": str,
        "bgpStatus": str,
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef
):
    """
    Type definition for `ClientUpdateVirtualInterfaceAttributesResponse` `bgpPeers`

    Information about a BGP peer.

    - **bgpPeerId** *(string) --*

      The ID of the BGP peer.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **bgpPeerState** *(string) --*

      The state of the BGP peer. The following are the possible values:

      * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
      can be created. This state applies only to public virtual interfaces.

      * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
      be established.

      * ``available`` : The BGP peer is ready to be established.

      * ``deleting`` : The BGP peer is being deleted.

      * ``deleted`` : The BGP peer is deleted and cannot be established.

    - **bgpStatus** *(string) --*

      The status of the BGP peer. The following are the possible values:

      * ``up`` : The BGP peer is established. This state does not indicate the state of the
      routing function. Ensure that you are receiving routes over the BGP session.

      * ``down`` : The BGP peer is down.

      * ``unknown`` : The BGP peer status is not available.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the BGP peer terminates.
    """


_ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef
):
    """
    Type definition for `ClientUpdateVirtualInterfaceAttributesResponse` `routeFilterPrefixes`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
      CIDR must use /64 or shorter.
    """


_ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef
):
    """
    Type definition for `ClientUpdateVirtualInterfaceAttributesResponse` `tags`

    Information about a tag.

    - **key** *(string) --*

      The key.

    - **value** *(string) --*

      The value.
    """


_ClientUpdateVirtualInterfaceAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": str,
        "virtualInterfaceState": str,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef],
    },
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponseTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateVirtualInterfaceAttributes` `Response`

    Information about a virtual interface.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **location** *(string) --*

      The location of the connection.

    - **connectionId** *(string) --*

      The ID of the connection.

    - **virtualInterfaceType** *(string) --*

      The type of virtual interface. The possible values are ``private`` and ``public`` .

    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.

    - **vlan** *(integer) --*

      The ID of the VLAN.

    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

      The valid values are 1-2147483647.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **authKey** *(string) --*

      The authentication key for BGP configuration. This string has a minimum length of 6
      characters and and a maximun lenth of 80 characters.

    - **amazonAddress** *(string) --*

      The IP address assigned to the Amazon interface.

    - **customerAddress** *(string) --*

      The IP address assigned to the customer interface.

    - **addressFamily** *(string) --*

      The address family for the BGP peer.

    - **virtualInterfaceState** *(string) --*

      The state of the virtual interface. The following are the possible values:

      * ``confirming`` : The creation of the virtual interface is pending confirmation from the
      virtual interface owner. If the owner of the virtual interface is different from the owner of
      the connection on which it is provisioned, then the virtual interface will remain in this
      state until it is confirmed by the virtual interface owner.

      * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
      interface needs validation before the virtual interface can be created.

      * ``pending`` : A virtual interface is in this state from the time that it is created until
      the virtual interface is ready to forward traffic.

      * ``available`` : A virtual interface that is able to forward traffic.

      * ``down`` : A virtual interface that is BGP down.

      * ``deleting`` : A virtual interface is in this state immediately after calling
      DeleteVirtualInterface until it can no longer forward traffic.

      * ``deleted`` : A virtual interface that cannot forward traffic.

      * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
      If a virtual interface in the ``Confirming`` state is deleted by the virtual interface owner,
      the virtual interface enters the ``Rejected`` state.

      * ``unknown`` : The state of the virtual interface is not available.

    - **customerRouterConfig** *(string) --*

      The customer router configuration.

    - **mtu** *(integer) --*

      The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The
      default value is 1500.

    - **jumboFrameCapable** *(boolean) --*

      Indicates whether jumbo frames (9001 MTU) are supported.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **routeFilterPrefixes** *(list) --*

      The routes to be advertised to the AWS network in this Region. Applies to public virtual
      interfaces.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6
          CIDR must use /64 or shorter.

    - **bgpPeers** *(list) --*

      The BGP peers configured on this virtual interface.

      - *(dict) --*

        Information about a BGP peer.

        - **bgpPeerId** *(string) --*

          The ID of the BGP peer.

        - **asn** *(integer) --*

          The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

        - **authKey** *(string) --*

          The authentication key for BGP configuration. This string has a minimum length of 6
          characters and and a maximun lenth of 80 characters.

        - **addressFamily** *(string) --*

          The address family for the BGP peer.

        - **amazonAddress** *(string) --*

          The IP address assigned to the Amazon interface.

        - **customerAddress** *(string) --*

          The IP address assigned to the customer interface.

        - **bgpPeerState** *(string) --*

          The state of the BGP peer. The following are the possible values:

          * ``verifying`` : The BGP peering addresses or ASN require validation before the BGP peer
          can be created. This state applies only to public virtual interfaces.

          * ``pending`` : The BGP peer is created, and remains in this state until it is ready to
          be established.

          * ``available`` : The BGP peer is ready to be established.

          * ``deleting`` : The BGP peer is being deleted.

          * ``deleted`` : The BGP peer is deleted and cannot be established.

        - **bgpStatus** *(string) --*

          The status of the BGP peer. The following are the possible values:

          * ``up`` : The BGP peer is established. This state does not indicate the state of the
          routing function. Ensure that you are receiving routes over the BGP session.

          * ``down`` : The BGP peer is down.

          * ``unknown`` : The BGP peer status is not available.

        - **awsDeviceV2** *(string) --*

          The Direct Connect endpoint on which the BGP peer terminates.

    - **region** *(string) --*

      The AWS Region where the virtual interface is located.

    - **awsDeviceV2** *(string) --*

      The Direct Connect endpoint on which the virtual interface terminates.

    - **tags** *(list) --*

      The tags associated with the virtual interface.

      - *(dict) --*

        Information about a tag.

        - **key** *(string) --*

          The key.

        - **value** *(string) --*

          The value.
    """


_DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAssociationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociations` `allowedPrefixesToDirectConnectGateway`

    Information about a route filter prefix that a customer can advertise through Border
    Gateway Protocol (BGP) over a public virtual interface.

    - **cidr** *(string) --*

      The CIDR block for the advertised route. Separate multiple routes using commas. An
      IPv6 CIDR must use /64 or shorter.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    {"id": str, "type": str, "ownerAccount": str, "region": str},
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociations` `associatedGateway`

    Information about the associated gateway.

    - **id** *(string) --*

      The ID of the associated gateway.

    - **type** *(string) --*

      The type of associated gateway.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the associated virtual private gateway or transit
      gateway.

    - **region** *(string) --*

      The Region where the associated gateway is located.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": str,
        "stateChangeError": str,
        "associatedGateway": DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAssociationsPaginateResponse` `directConnectGatewayAssociations`

    Information about an association between a Direct Connect gateway and a virtual private
    gateway or transit gateway.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the associated gateway.

    - **associationState** *(string) --*

      The state of the association. The following are the possible values:

      * ``associating`` : The initial state after calling
      CreateDirectConnectGatewayAssociation .

      * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
      gateway are successfully associated and ready to pass traffic.

      * ``disassociating`` : The initial state after calling
      DeleteDirectConnectGatewayAssociation .

      * ``disassociated`` : The virtual private gateway or transit gateway is disassociated
      from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and
      virtual private gateway or transit gateway is stopped.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.

    - **associatedGateway** *(dict) --*

      Information about the associated gateway.

      - **id** *(string) --*

        The ID of the associated gateway.

      - **type** *(string) --*

        The type of associated gateway.

      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the associated virtual private gateway or transit
        gateway.

      - **region** *(string) --*

        The Region where the associated gateway is located.

    - **associationId** *(string) --*

      The ID of the Direct Connect gateway association.

    - **allowedPrefixesToDirectConnectGateway** *(list) --*

      The Amazon VPC prefixes to advertise to the Direct Connect gateway.

      - *(dict) --*

        Information about a route filter prefix that a customer can advertise through Border
        Gateway Protocol (BGP) over a public virtual interface.

        - **cidr** *(string) --*

          The CIDR block for the advertised route. Separate multiple routes using commas. An
          IPv6 CIDR must use /64 or shorter.

    - **virtualGatewayId** *(string) --*

      The ID of the virtual private gateway. Applies only to private virtual interfaces.

    - **virtualGatewayRegion** *(string) --*

      The AWS Region where the virtual private gateway is located.

    - **virtualGatewayOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual private gateway.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef",
    {
        "directConnectGatewayAssociations": List[
            DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAssociationsPaginate` `Response`

    - **directConnectGatewayAssociations** *(list) --*

      Information about the associations.

      - *(dict) --*

        Information about an association between a Direct Connect gateway and a virtual private
        gateway or transit gateway.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **directConnectGatewayOwnerAccount** *(string) --*

          The ID of the AWS account that owns the associated gateway.

        - **associationState** *(string) --*

          The state of the association. The following are the possible values:

          * ``associating`` : The initial state after calling
          CreateDirectConnectGatewayAssociation .

          * ``associated`` : The Direct Connect gateway and virtual private gateway or transit
          gateway are successfully associated and ready to pass traffic.

          * ``disassociating`` : The initial state after calling
          DeleteDirectConnectGatewayAssociation .

          * ``disassociated`` : The virtual private gateway or transit gateway is disassociated
          from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and
          virtual private gateway or transit gateway is stopped.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

        - **associatedGateway** *(dict) --*

          Information about the associated gateway.

          - **id** *(string) --*

            The ID of the associated gateway.

          - **type** *(string) --*

            The type of associated gateway.

          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the associated virtual private gateway or transit
            gateway.

          - **region** *(string) --*

            The Region where the associated gateway is located.

        - **associationId** *(string) --*

          The ID of the Direct Connect gateway association.

        - **allowedPrefixesToDirectConnectGateway** *(list) --*

          The Amazon VPC prefixes to advertise to the Direct Connect gateway.

          - *(dict) --*

            Information about a route filter prefix that a customer can advertise through Border
            Gateway Protocol (BGP) over a public virtual interface.

            - **cidr** *(string) --*

              The CIDR block for the advertised route. Separate multiple routes using commas. An
              IPv6 CIDR must use /64 or shorter.

        - **virtualGatewayId** *(string) --*

          The ID of the virtual private gateway. Applies only to private virtual interfaces.

        - **virtualGatewayRegion** *(string) --*

          The AWS Region where the virtual private gateway is located.

        - **virtualGatewayOwnerAccount** *(string) --*

          The ID of the AWS account that owns the virtual private gateway.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAttachmentsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": str,
        "attachmentType": str,
        "stateChangeError": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAttachmentsPaginateResponse` `directConnectGatewayAttachments`

    Information about an attachment between a Direct Connect gateway and a virtual interface.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **virtualInterfaceId** *(string) --*

      The ID of the virtual interface.

    - **virtualInterfaceRegion** *(string) --*

      The AWS Region where the virtual interface is located.

    - **virtualInterfaceOwnerAccount** *(string) --*

      The ID of the AWS account that owns the virtual interface.

    - **attachmentState** *(string) --*

      The state of the attachment. The following are the possible values:

      * ``attaching`` : The initial state after a virtual interface is created using the Direct
      Connect gateway.

      * ``attached`` : The Direct Connect gateway and virtual interface are attached and ready
      to pass traffic.

      * ``detaching`` : The initial state after calling  DeleteVirtualInterface .

      * ``detached`` : The virtual interface is detached from the Direct Connect gateway.
      Traffic flow between the Direct Connect gateway and virtual interface is stopped.

    - **attachmentType** *(string) --*

      The type of attachment.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef",
    {
        "directConnectGatewayAttachments": List[
            DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewayAttachmentsPaginate` `Response`

    - **directConnectGatewayAttachments** *(list) --*

      The attachments.

      - *(dict) --*

        Information about an attachment between a Direct Connect gateway and a virtual interface.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **virtualInterfaceId** *(string) --*

          The ID of the virtual interface.

        - **virtualInterfaceRegion** *(string) --*

          The AWS Region where the virtual interface is located.

        - **virtualInterfaceOwnerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.

        - **attachmentState** *(string) --*

          The state of the attachment. The following are the possible values:

          * ``attaching`` : The initial state after a virtual interface is created using the Direct
          Connect gateway.

          * ``attached`` : The Direct Connect gateway and virtual interface are attached and ready
          to pass traffic.

          * ``detaching`` : The initial state after calling  DeleteVirtualInterface .

          * ``detached`` : The virtual interface is detached from the Direct Connect gateway.
          Traffic flow between the Direct Connect gateway and virtual interface is stopped.

        - **attachmentType** *(string) --*

          The type of attachment.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewaysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": str,
        "stateChangeError": str,
    },
    total=False,
)


class DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef(
    _DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewaysPaginateResponse` `directConnectGateways`

    Information about a Direct Connect gateway, which enables you to connect virtual interfaces
    and virtual private gateway or transit gateways.

    - **directConnectGatewayId** *(string) --*

      The ID of the Direct Connect gateway.

    - **directConnectGatewayName** *(string) --*

      The name of the Direct Connect gateway.

    - **amazonSideAsn** *(integer) --*

      The autonomous system number (ASN) for the Amazon side of the connection.

    - **ownerAccount** *(string) --*

      The ID of the AWS account that owns the Direct Connect gateway.

    - **directConnectGatewayState** *(string) --*

      The state of the Direct Connect gateway. The following are the possible values:

      * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

      * ``available`` : The Direct Connect gateway is ready for use.

      * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

      * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

    - **stateChangeError** *(string) --*

      The error message if the state of an object failed to advance.
    """


_DescribeDirectConnectGatewaysPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginateResponseTypeDef",
    {
        "directConnectGateways": List[
            DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewaysPaginateResponseTypeDef(
    _DescribeDirectConnectGatewaysPaginateResponseTypeDef
):
    """
    Type definition for `DescribeDirectConnectGatewaysPaginate` `Response`

    - **directConnectGateways** *(list) --*

      The Direct Connect gateways.

      - *(dict) --*

        Information about a Direct Connect gateway, which enables you to connect virtual interfaces
        and virtual private gateway or transit gateways.

        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.

        - **directConnectGatewayName** *(string) --*

          The name of the Direct Connect gateway.

        - **amazonSideAsn** *(integer) --*

          The autonomous system number (ASN) for the Amazon side of the connection.

        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the Direct Connect gateway.

        - **directConnectGatewayState** *(string) --*

          The state of the Direct Connect gateway. The following are the possible values:

          * ``pending`` : The initial state after calling  CreateDirectConnectGateway .

          * ``available`` : The Direct Connect gateway is ready for use.

          * ``deleting`` : The initial state after calling  DeleteDirectConnectGateway .

          * ``deleted`` : The Direct Connect gateway is deleted and cannot pass traffic.

        - **stateChangeError** *(string) --*

          The error message if the state of an object failed to advance.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
