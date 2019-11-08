# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.directconnect.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Directconnect](index.md#directconnect) / Client
    - [Client](#client)
        - [Client().accept_direct_connect_gateway_association_proposal](#clientaccept_direct_connect_gateway_association_proposal)
        - [Client().allocate_connection_on_interconnect](#clientallocate_connection_on_interconnect)
        - [Client().allocate_hosted_connection](#clientallocate_hosted_connection)
        - [Client().allocate_private_virtual_interface](#clientallocate_private_virtual_interface)
        - [Client().allocate_public_virtual_interface](#clientallocate_public_virtual_interface)
        - [Client().allocate_transit_virtual_interface](#clientallocate_transit_virtual_interface)
        - [Client().associate_connection_with_lag](#clientassociate_connection_with_lag)
        - [Client().associate_hosted_connection](#clientassociate_hosted_connection)
        - [Client().associate_virtual_interface](#clientassociate_virtual_interface)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().confirm_connection](#clientconfirm_connection)
        - [Client().confirm_private_virtual_interface](#clientconfirm_private_virtual_interface)
        - [Client().confirm_public_virtual_interface](#clientconfirm_public_virtual_interface)
        - [Client().confirm_transit_virtual_interface](#clientconfirm_transit_virtual_interface)
        - [Client().create_bgp_peer](#clientcreate_bgp_peer)
        - [Client().create_connection](#clientcreate_connection)
        - [Client().create_direct_connect_gateway](#clientcreate_direct_connect_gateway)
        - [Client().create_direct_connect_gateway_association](#clientcreate_direct_connect_gateway_association)
        - [Client().create_direct_connect_gateway_association_proposal](#clientcreate_direct_connect_gateway_association_proposal)
        - [Client().create_interconnect](#clientcreate_interconnect)
        - [Client().create_lag](#clientcreate_lag)
        - [Client().create_private_virtual_interface](#clientcreate_private_virtual_interface)
        - [Client().create_public_virtual_interface](#clientcreate_public_virtual_interface)
        - [Client().create_transit_virtual_interface](#clientcreate_transit_virtual_interface)
        - [Client().delete_bgp_peer](#clientdelete_bgp_peer)
        - [Client().delete_connection](#clientdelete_connection)
        - [Client().delete_direct_connect_gateway](#clientdelete_direct_connect_gateway)
        - [Client().delete_direct_connect_gateway_association](#clientdelete_direct_connect_gateway_association)
        - [Client().delete_direct_connect_gateway_association_proposal](#clientdelete_direct_connect_gateway_association_proposal)
        - [Client().delete_interconnect](#clientdelete_interconnect)
        - [Client().delete_lag](#clientdelete_lag)
        - [Client().delete_virtual_interface](#clientdelete_virtual_interface)
        - [Client().describe_connection_loa](#clientdescribe_connection_loa)
        - [Client().describe_connections](#clientdescribe_connections)
        - [Client().describe_connections_on_interconnect](#clientdescribe_connections_on_interconnect)
        - [Client().describe_direct_connect_gateway_association_proposals](#clientdescribe_direct_connect_gateway_association_proposals)
        - [Client().describe_direct_connect_gateway_associations](#clientdescribe_direct_connect_gateway_associations)
        - [Client().describe_direct_connect_gateway_attachments](#clientdescribe_direct_connect_gateway_attachments)
        - [Client().describe_direct_connect_gateways](#clientdescribe_direct_connect_gateways)
        - [Client().describe_hosted_connections](#clientdescribe_hosted_connections)
        - [Client().describe_interconnect_loa](#clientdescribe_interconnect_loa)
        - [Client().describe_interconnects](#clientdescribe_interconnects)
        - [Client().describe_lags](#clientdescribe_lags)
        - [Client().describe_loa](#clientdescribe_loa)
        - [Client().describe_locations](#clientdescribe_locations)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().describe_virtual_gateways](#clientdescribe_virtual_gateways)
        - [Client().describe_virtual_interfaces](#clientdescribe_virtual_interfaces)
        - [Client().disassociate_connection_from_lag](#clientdisassociate_connection_from_lag)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_direct_connect_gateway_association](#clientupdate_direct_connect_gateway_association)
        - [Client().update_lag](#clientupdate_lag)
        - [Client().update_virtual_interface_attributes](#clientupdate_virtual_interface_attributes)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L12)

```python
class Client(BaseClient):
```

### Client().accept_direct_connect_gateway_association_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L15)

```python
def accept_direct_connect_gateway_association_proposal(
    directConnectGatewayId: str,
    proposalId: str,
    associatedGatewayOwnerAccount: str,
    overrideAllowedPrefixesToDirectConnectGateway: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().allocate_connection_on_interconnect

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L25)

```python
def allocate_connection_on_interconnect(
    bandwidth: str,
    connectionName: str,
    ownerAccount: str,
    interconnectId: str,
    vlan: int,
) -> Dict[str, Any]:
```

### Client().allocate_hosted_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L36)

```python
def allocate_hosted_connection(
    connectionId: str,
    ownerAccount: str,
    bandwidth: str,
    connectionName: str,
    vlan: int,
    tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().allocate_private_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L48)

```python
def allocate_private_virtual_interface(
    connectionId: str,
    ownerAccount: str,
    newPrivateVirtualInterfaceAllocation: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().allocate_public_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L57)

```python
def allocate_public_virtual_interface(
    connectionId: str,
    ownerAccount: str,
    newPublicVirtualInterfaceAllocation: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().allocate_transit_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L66)

```python
def allocate_transit_virtual_interface(
    connectionId: str,
    ownerAccount: str,
    newTransitVirtualInterfaceAllocation: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().associate_connection_with_lag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L75)

```python
def associate_connection_with_lag(
    connectionId: str,
    lagId: str,
) -> Dict[str, Any]:
```

### Client().associate_hosted_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L81)

```python
def associate_hosted_connection(
    connectionId: str,
    parentConnectionId: str,
) -> Dict[str, Any]:
```

### Client().associate_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L87)

```python
def associate_virtual_interface(
    virtualInterfaceId: str,
    connectionId: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L93)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().confirm_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L97)

```python
def confirm_connection(connectionId: str) -> Dict[str, Any]:
```

### Client().confirm_private_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L101)

```python
def confirm_private_virtual_interface(
    virtualInterfaceId: str,
    virtualGatewayId: str = None,
    directConnectGatewayId: str = None,
) -> Dict[str, Any]:
```

### Client().confirm_public_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L110)

```python
def confirm_public_virtual_interface(
    virtualInterfaceId: str,
) -> Dict[str, Any]:
```

### Client().confirm_transit_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L116)

```python
def confirm_transit_virtual_interface(
    virtualInterfaceId: str,
    directConnectGatewayId: str,
) -> Dict[str, Any]:
```

### Client().create_bgp_peer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L122)

```python
def create_bgp_peer(
    virtualInterfaceId: str = None,
    newBGPPeer: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L128)

```python
def create_connection(
    location: str,
    bandwidth: str,
    connectionName: str,
    lagId: str = None,
    tags: List[Any] = None,
    providerName: str = None,
) -> Dict[str, Any]:
```

### Client().create_direct_connect_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L140)

```python
def create_direct_connect_gateway(
    directConnectGatewayName: str,
    amazonSideAsn: int = None,
) -> Dict[str, Any]:
```

### Client().create_direct_connect_gateway_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L146)

```python
def create_direct_connect_gateway_association(
    directConnectGatewayId: str,
    gatewayId: str = None,
    addAllowedPrefixesToDirectConnectGateway: List[Any] = None,
    virtualGatewayId: str = None,
) -> Dict[str, Any]:
```

### Client().create_direct_connect_gateway_association_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L156)

```python
def create_direct_connect_gateway_association_proposal(
    directConnectGatewayId: str,
    directConnectGatewayOwnerAccount: str,
    gatewayId: str,
    addAllowedPrefixesToDirectConnectGateway: List[Any] = None,
    removeAllowedPrefixesToDirectConnectGateway: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_interconnect

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L167)

```python
def create_interconnect(
    interconnectName: str,
    bandwidth: str,
    location: str,
    lagId: str = None,
    tags: List[Any] = None,
    providerName: str = None,
) -> Dict[str, Any]:
```

### Client().create_lag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L179)

```python
def create_lag(
    numberOfConnections: int,
    location: str,
    connectionsBandwidth: str,
    lagName: str,
    connectionId: str = None,
    tags: List[Any] = None,
    childConnectionTags: List[Any] = None,
    providerName: str = None,
) -> Dict[str, Any]:
```

### Client().create_private_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L193)

```python
def create_private_virtual_interface(
    connectionId: str,
    newPrivateVirtualInterface: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_public_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L199)

```python
def create_public_virtual_interface(
    connectionId: str,
    newPublicVirtualInterface: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_transit_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L205)

```python
def create_transit_virtual_interface(
    connectionId: str,
    newTransitVirtualInterface: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_bgp_peer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L211)

```python
def delete_bgp_peer(
    virtualInterfaceId: str = None,
    asn: int = None,
    customerAddress: str = None,
    bgpPeerId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L221)

```python
def delete_connection(connectionId: str) -> Dict[str, Any]:
```

### Client().delete_direct_connect_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L225)

```python
def delete_direct_connect_gateway(
    directConnectGatewayId: str,
) -> Dict[str, Any]:
```

### Client().delete_direct_connect_gateway_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L231)

```python
def delete_direct_connect_gateway_association(
    associationId: str = None,
    directConnectGatewayId: str = None,
    virtualGatewayId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_direct_connect_gateway_association_proposal

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L240)

```python
def delete_direct_connect_gateway_association_proposal(
    proposalId: str,
) -> Dict[str, Any]:
```

### Client().delete_interconnect

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L246)

```python
def delete_interconnect(interconnectId: str) -> Dict[str, Any]:
```

### Client().delete_lag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L250)

```python
def delete_lag(lagId: str) -> Dict[str, Any]:
```

### Client().delete_virtual_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L254)

```python
def delete_virtual_interface(virtualInterfaceId: str) -> Dict[str, Any]:
```

### Client().describe_connection_loa

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L258)

```python
def describe_connection_loa(
    connectionId: str,
    providerName: str = None,
    loaContentType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L264)

```python
def describe_connections(connectionId: str = None) -> Dict[str, Any]:
```

### Client().describe_connections_on_interconnect

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L268)

```python
def describe_connections_on_interconnect(
    interconnectId: str,
) -> Dict[str, Any]:
```

### Client().describe_direct_connect_gateway_association_proposals

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L274)

```python
def describe_direct_connect_gateway_association_proposals(
    directConnectGatewayId: str = None,
    proposalId: str = None,
    associatedGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_direct_connect_gateway_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L285)

```python
def describe_direct_connect_gateway_associations(
    associationId: str = None,
    associatedGatewayId: str = None,
    directConnectGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None,
    virtualGatewayId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_direct_connect_gateway_attachments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L297)

```python
def describe_direct_connect_gateway_attachments(
    directConnectGatewayId: str = None,
    virtualInterfaceId: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_direct_connect_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L307)

```python
def describe_direct_connect_gateways(
    directConnectGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().describe_hosted_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L316)

```python
def describe_hosted_connections(connectionId: str) -> Dict[str, Any]:
```

### Client().describe_interconnect_loa

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L320)

```python
def describe_interconnect_loa(
    interconnectId: str,
    providerName: str = None,
    loaContentType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_interconnects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L326)

```python
def describe_interconnects(interconnectId: str = None) -> Dict[str, Any]:
```

### Client().describe_lags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L330)

```python
def describe_lags(lagId: str = None) -> Dict[str, Any]:
```

### Client().describe_loa

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L334)

```python
def describe_loa(
    connectionId: str,
    providerName: str = None,
    loaContentType: str = None,
) -> Dict[str, Any]:
```

### Client().describe_locations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L340)

```python
def describe_locations() -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L344)

```python
def describe_tags(resourceArns: List[Any]) -> Dict[str, Any]:
```

### Client().describe_virtual_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L348)

```python
def describe_virtual_gateways() -> Dict[str, Any]:
```

### Client().describe_virtual_interfaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L352)

```python
def describe_virtual_interfaces(
    connectionId: str = None,
    virtualInterfaceId: str = None,
) -> Dict[str, Any]:
```

### Client().disassociate_connection_from_lag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L358)

```python
def disassociate_connection_from_lag(
    connectionId: str,
    lagId: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L364)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L374)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L378)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L382)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L386)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_direct_connect_gateway_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L390)

```python
def update_direct_connect_gateway_association(
    associationId: str = None,
    addAllowedPrefixesToDirectConnectGateway: List[Any] = None,
    removeAllowedPrefixesToDirectConnectGateway: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_lag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L399)

```python
def update_lag(
    lagId: str,
    lagName: str = None,
    minimumLinks: int = None,
) -> Dict[str, Any]:
```

### Client().update_virtual_interface_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/client.py#L405)

```python
def update_virtual_interface_attributes(
    virtualInterfaceId: str,
    mtu: int = None,
) -> Dict[str, Any]:
```
