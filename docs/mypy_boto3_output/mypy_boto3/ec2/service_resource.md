# ServiceResource

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ec2.service_resource](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ec2](index.md#ec2) / ServiceResource
    - [ClassicAddress](#classicaddress)
        - [ClassicAddress().associate](#classicaddressassociate)
        - [ClassicAddress().disassociate](#classicaddressdisassociate)
        - [ClassicAddress().get_available_subresources](#classicaddressget_available_subresources)
        - [ClassicAddress().load](#classicaddressload)
        - [ClassicAddress().release](#classicaddressrelease)
        - [ClassicAddress().reload](#classicaddressreload)
    - [DhcpOptions](#dhcpoptions)
        - [DhcpOptions().associate_with_vpc](#dhcpoptionsassociate_with_vpc)
        - [DhcpOptions().create_tags](#dhcpoptionscreate_tags)
        - [DhcpOptions().delete](#dhcpoptionsdelete)
        - [DhcpOptions().get_available_subresources](#dhcpoptionsget_available_subresources)
        - [DhcpOptions().load](#dhcpoptionsload)
        - [DhcpOptions().reload](#dhcpoptionsreload)
    - [Image](#image)
        - [Image().create_tags](#imagecreate_tags)
        - [Image().deregister](#imagederegister)
        - [Image().describe_attribute](#imagedescribe_attribute)
        - [Image().get_available_subresources](#imageget_available_subresources)
        - [Image().load](#imageload)
        - [Image().modify_attribute](#imagemodify_attribute)
        - [Image().reload](#imagereload)
        - [Image().reset_attribute](#imagereset_attribute)
        - [Image().wait_until_exists](#imagewait_until_exists)
    - [Instance](#instance)
        - [Instance().attach_classic_link_vpc](#instanceattach_classic_link_vpc)
        - [Instance().attach_volume](#instanceattach_volume)
        - [Instance().console_output](#instanceconsole_output)
        - [Instance().create_image](#instancecreate_image)
        - [Instance().create_tags](#instancecreate_tags)
        - [Instance().delete_tags](#instancedelete_tags)
        - [Instance().describe_attribute](#instancedescribe_attribute)
        - [Instance().detach_classic_link_vpc](#instancedetach_classic_link_vpc)
        - [Instance().detach_volume](#instancedetach_volume)
        - [Instance().get_available_subresources](#instanceget_available_subresources)
        - [Instance().load](#instanceload)
        - [Instance().modify_attribute](#instancemodify_attribute)
        - [Instance().monitor](#instancemonitor)
        - [Instance().password_data](#instancepassword_data)
        - [Instance().reboot](#instancereboot)
        - [Instance().reload](#instancereload)
        - [Instance().report_status](#instancereport_status)
        - [Instance().reset_attribute](#instancereset_attribute)
        - [Instance().reset_kernel](#instancereset_kernel)
        - [Instance().reset_ramdisk](#instancereset_ramdisk)
        - [Instance().reset_source_dest_check](#instancereset_source_dest_check)
        - [Instance().start](#instancestart)
        - [Instance().stop](#instancestop)
        - [Instance().terminate](#instanceterminate)
        - [Instance().unmonitor](#instanceunmonitor)
        - [Instance().wait_until_exists](#instancewait_until_exists)
        - [Instance().wait_until_running](#instancewait_until_running)
        - [Instance().wait_until_stopped](#instancewait_until_stopped)
        - [Instance().wait_until_terminated](#instancewait_until_terminated)
    - [InternetGateway](#internetgateway)
        - [InternetGateway().attach_to_vpc](#internetgatewayattach_to_vpc)
        - [InternetGateway().create_tags](#internetgatewaycreate_tags)
        - [InternetGateway().delete](#internetgatewaydelete)
        - [InternetGateway().detach_from_vpc](#internetgatewaydetach_from_vpc)
        - [InternetGateway().get_available_subresources](#internetgatewayget_available_subresources)
        - [InternetGateway().load](#internetgatewayload)
        - [InternetGateway().reload](#internetgatewayreload)
    - [KeyPair](#keypair)
        - [KeyPair().delete](#keypairdelete)
        - [KeyPair().get_available_subresources](#keypairget_available_subresources)
    - [KeyPairInfo](#keypairinfo)
        - [KeyPairInfo().delete](#keypairinfodelete)
        - [KeyPairInfo().get_available_subresources](#keypairinfoget_available_subresources)
        - [KeyPairInfo().load](#keypairinfoload)
        - [KeyPairInfo().reload](#keypairinforeload)
    - [NetworkAcl](#networkacl)
        - [NetworkAcl().create_entry](#networkaclcreate_entry)
        - [NetworkAcl().create_tags](#networkaclcreate_tags)
        - [NetworkAcl().delete](#networkacldelete)
        - [NetworkAcl().delete_entry](#networkacldelete_entry)
        - [NetworkAcl().get_available_subresources](#networkaclget_available_subresources)
        - [NetworkAcl().load](#networkaclload)
        - [NetworkAcl().reload](#networkaclreload)
        - [NetworkAcl().replace_association](#networkaclreplace_association)
        - [NetworkAcl().replace_entry](#networkaclreplace_entry)
    - [NetworkInterface](#networkinterface)
        - [NetworkInterface().assign_private_ip_addresses](#networkinterfaceassign_private_ip_addresses)
        - [NetworkInterface().attach](#networkinterfaceattach)
        - [NetworkInterface().create_tags](#networkinterfacecreate_tags)
        - [NetworkInterface().delete](#networkinterfacedelete)
        - [NetworkInterface().describe_attribute](#networkinterfacedescribe_attribute)
        - [NetworkInterface().detach](#networkinterfacedetach)
        - [NetworkInterface().get_available_subresources](#networkinterfaceget_available_subresources)
        - [NetworkInterface().load](#networkinterfaceload)
        - [NetworkInterface().modify_attribute](#networkinterfacemodify_attribute)
        - [NetworkInterface().reload](#networkinterfacereload)
        - [NetworkInterface().reset_attribute](#networkinterfacereset_attribute)
        - [NetworkInterface().unassign_private_ip_addresses](#networkinterfaceunassign_private_ip_addresses)
    - [NetworkInterfaceAssociation](#networkinterfaceassociation)
        - [NetworkInterfaceAssociation().delete](#networkinterfaceassociationdelete)
        - [NetworkInterfaceAssociation().get_available_subresources](#networkinterfaceassociationget_available_subresources)
        - [NetworkInterfaceAssociation().load](#networkinterfaceassociationload)
        - [NetworkInterfaceAssociation().reload](#networkinterfaceassociationreload)
    - [PlacementGroup](#placementgroup)
        - [PlacementGroup().delete](#placementgroupdelete)
        - [PlacementGroup().get_available_subresources](#placementgroupget_available_subresources)
        - [PlacementGroup().load](#placementgroupload)
        - [PlacementGroup().reload](#placementgroupreload)
    - [Route](#route)
        - [Route().delete](#routedelete)
        - [Route().get_available_subresources](#routeget_available_subresources)
        - [Route().replace](#routereplace)
    - [RouteTable](#routetable)
        - [RouteTable().associate_with_subnet](#routetableassociate_with_subnet)
        - [RouteTable().create_route](#routetablecreate_route)
        - [RouteTable().create_tags](#routetablecreate_tags)
        - [RouteTable().delete](#routetabledelete)
        - [RouteTable().get_available_subresources](#routetableget_available_subresources)
        - [RouteTable().load](#routetableload)
        - [RouteTable().reload](#routetablereload)
    - [RouteTableAssociation](#routetableassociation)
        - [RouteTableAssociation().delete](#routetableassociationdelete)
        - [RouteTableAssociation().get_available_subresources](#routetableassociationget_available_subresources)
        - [RouteTableAssociation().replace_subnet](#routetableassociationreplace_subnet)
    - [SecurityGroup](#securitygroup)
        - [SecurityGroup().authorize_egress](#securitygroupauthorize_egress)
        - [SecurityGroup().authorize_ingress](#securitygroupauthorize_ingress)
        - [SecurityGroup().create_tags](#securitygroupcreate_tags)
        - [SecurityGroup().delete](#securitygroupdelete)
        - [SecurityGroup().get_available_subresources](#securitygroupget_available_subresources)
        - [SecurityGroup().load](#securitygroupload)
        - [SecurityGroup().reload](#securitygroupreload)
        - [SecurityGroup().revoke_egress](#securitygrouprevoke_egress)
        - [SecurityGroup().revoke_ingress](#securitygrouprevoke_ingress)
    - [ServiceResource](#serviceresource)
        - [ServiceResource().ClassicAddress](#serviceresourceclassicaddress)
        - [ServiceResource().DhcpOptions](#serviceresourcedhcpoptions)
        - [ServiceResource().Image](#serviceresourceimage)
        - [ServiceResource().Instance](#serviceresourceinstance)
        - [ServiceResource().InternetGateway](#serviceresourceinternetgateway)
        - [ServiceResource().KeyPair](#serviceresourcekeypair)
        - [ServiceResource().NetworkAcl](#serviceresourcenetworkacl)
        - [ServiceResource().NetworkInterface](#serviceresourcenetworkinterface)
        - [ServiceResource().NetworkInterfaceAssociation](#serviceresourcenetworkinterfaceassociation)
        - [ServiceResource().PlacementGroup](#serviceresourceplacementgroup)
        - [ServiceResource().Route](#serviceresourceroute)
        - [ServiceResource().RouteTable](#serviceresourceroutetable)
        - [ServiceResource().RouteTableAssociation](#serviceresourceroutetableassociation)
        - [ServiceResource().SecurityGroup](#serviceresourcesecuritygroup)
        - [ServiceResource().Snapshot](#serviceresourcesnapshot)
        - [ServiceResource().Subnet](#serviceresourcesubnet)
        - [ServiceResource().Tag](#serviceresourcetag)
        - [ServiceResource().Volume](#serviceresourcevolume)
        - [ServiceResource().Vpc](#serviceresourcevpc)
        - [ServiceResource().VpcAddress](#serviceresourcevpcaddress)
        - [ServiceResource().VpcPeeringConnection](#serviceresourcevpcpeeringconnection)
        - [ServiceResource().create_dhcp_options](#serviceresourcecreate_dhcp_options)
        - [ServiceResource().create_instances](#serviceresourcecreate_instances)
        - [ServiceResource().create_internet_gateway](#serviceresourcecreate_internet_gateway)
        - [ServiceResource().create_key_pair](#serviceresourcecreate_key_pair)
        - [ServiceResource().create_network_acl](#serviceresourcecreate_network_acl)
        - [ServiceResource().create_network_interface](#serviceresourcecreate_network_interface)
        - [ServiceResource().create_placement_group](#serviceresourcecreate_placement_group)
        - [ServiceResource().create_route_table](#serviceresourcecreate_route_table)
        - [ServiceResource().create_security_group](#serviceresourcecreate_security_group)
        - [ServiceResource().create_snapshot](#serviceresourcecreate_snapshot)
        - [ServiceResource().create_subnet](#serviceresourcecreate_subnet)
        - [ServiceResource().create_tags](#serviceresourcecreate_tags)
        - [ServiceResource().create_volume](#serviceresourcecreate_volume)
        - [ServiceResource().create_vpc](#serviceresourcecreate_vpc)
        - [ServiceResource().create_vpc_peering_connection](#serviceresourcecreate_vpc_peering_connection)
        - [ServiceResource().disassociate_route_table](#serviceresourcedisassociate_route_table)
        - [ServiceResource().get_available_subresources](#serviceresourceget_available_subresources)
        - [ServiceResource().import_key_pair](#serviceresourceimport_key_pair)
        - [ServiceResource().register_image](#serviceresourceregister_image)
    - [Snapshot](#snapshot)
        - [Snapshot().copy](#snapshotcopy)
        - [Snapshot().create_tags](#snapshotcreate_tags)
        - [Snapshot().delete](#snapshotdelete)
        - [Snapshot().describe_attribute](#snapshotdescribe_attribute)
        - [Snapshot().get_available_subresources](#snapshotget_available_subresources)
        - [Snapshot().load](#snapshotload)
        - [Snapshot().modify_attribute](#snapshotmodify_attribute)
        - [Snapshot().reload](#snapshotreload)
        - [Snapshot().reset_attribute](#snapshotreset_attribute)
        - [Snapshot().wait_until_completed](#snapshotwait_until_completed)
    - [Subnet](#subnet)
        - [Subnet().create_instances](#subnetcreate_instances)
        - [Subnet().create_network_interface](#subnetcreate_network_interface)
        - [Subnet().create_tags](#subnetcreate_tags)
        - [Subnet().delete](#subnetdelete)
        - [Subnet().get_available_subresources](#subnetget_available_subresources)
        - [Subnet().load](#subnetload)
        - [Subnet().reload](#subnetreload)
    - [Tag](#tag)
        - [Tag().delete](#tagdelete)
        - [Tag().get_available_subresources](#tagget_available_subresources)
        - [Tag().load](#tagload)
        - [Tag().reload](#tagreload)
    - [Volume](#volume)
        - [Volume().attach_to_instance](#volumeattach_to_instance)
        - [Volume().create_snapshot](#volumecreate_snapshot)
        - [Volume().create_tags](#volumecreate_tags)
        - [Volume().delete](#volumedelete)
        - [Volume().describe_attribute](#volumedescribe_attribute)
        - [Volume().describe_status](#volumedescribe_status)
        - [Volume().detach_from_instance](#volumedetach_from_instance)
        - [Volume().enable_io](#volumeenable_io)
        - [Volume().get_available_subresources](#volumeget_available_subresources)
        - [Volume().load](#volumeload)
        - [Volume().modify_attribute](#volumemodify_attribute)
        - [Volume().reload](#volumereload)
    - [Vpc](#vpc)
        - [Vpc().associate_dhcp_options](#vpcassociate_dhcp_options)
        - [Vpc().attach_classic_link_instance](#vpcattach_classic_link_instance)
        - [Vpc().attach_internet_gateway](#vpcattach_internet_gateway)
        - [Vpc().create_network_acl](#vpccreate_network_acl)
        - [Vpc().create_route_table](#vpccreate_route_table)
        - [Vpc().create_security_group](#vpccreate_security_group)
        - [Vpc().create_subnet](#vpccreate_subnet)
        - [Vpc().create_tags](#vpccreate_tags)
        - [Vpc().delete](#vpcdelete)
        - [Vpc().describe_attribute](#vpcdescribe_attribute)
        - [Vpc().detach_classic_link_instance](#vpcdetach_classic_link_instance)
        - [Vpc().detach_internet_gateway](#vpcdetach_internet_gateway)
        - [Vpc().disable_classic_link](#vpcdisable_classic_link)
        - [Vpc().enable_classic_link](#vpcenable_classic_link)
        - [Vpc().get_available_subresources](#vpcget_available_subresources)
        - [Vpc().load](#vpcload)
        - [Vpc().modify_attribute](#vpcmodify_attribute)
        - [Vpc().reload](#vpcreload)
        - [Vpc().request_vpc_peering_connection](#vpcrequest_vpc_peering_connection)
        - [Vpc().wait_until_available](#vpcwait_until_available)
        - [Vpc().wait_until_exists](#vpcwait_until_exists)
    - [VpcAddress](#vpcaddress)
        - [VpcAddress().associate](#vpcaddressassociate)
        - [VpcAddress().get_available_subresources](#vpcaddressget_available_subresources)
        - [VpcAddress().load](#vpcaddressload)
        - [VpcAddress().release](#vpcaddressrelease)
        - [VpcAddress().reload](#vpcaddressreload)
    - [VpcPeeringConnection](#vpcpeeringconnection)
        - [VpcPeeringConnection().accept](#vpcpeeringconnectionaccept)
        - [VpcPeeringConnection().delete](#vpcpeeringconnectiondelete)
        - [VpcPeeringConnection().get_available_subresources](#vpcpeeringconnectionget_available_subresources)
        - [VpcPeeringConnection().load](#vpcpeeringconnectionload)
        - [VpcPeeringConnection().reject](#vpcpeeringconnectionreject)
        - [VpcPeeringConnection().reload](#vpcpeeringconnectionreload)
        - [VpcPeeringConnection().wait_until_exists](#vpcpeeringconnectionwait_until_exists)
    - [accepted_vpc_peering_connections](#accepted_vpc_peering_connections)
        - [accepted_vpc_peering_connections.all](#accepted_vpc_peering_connectionsall)
        - [accepted_vpc_peering_connections.filter](#accepted_vpc_peering_connectionsfilter)
        - [accepted_vpc_peering_connections.iterator](#accepted_vpc_peering_connectionsiterator)
        - [accepted_vpc_peering_connections.limit](#accepted_vpc_peering_connectionslimit)
        - [accepted_vpc_peering_connections.page_size](#accepted_vpc_peering_connectionspage_size)
        - [accepted_vpc_peering_connections.pages](#accepted_vpc_peering_connectionspages)
    - [classic_addresses](#classic_addresses)
        - [classic_addresses.all](#classic_addressesall)
        - [classic_addresses.filter](#classic_addressesfilter)
        - [classic_addresses.iterator](#classic_addressesiterator)
        - [classic_addresses.limit](#classic_addresseslimit)
        - [classic_addresses.page_size](#classic_addressespage_size)
        - [classic_addresses.pages](#classic_addressespages)
    - [dhcp_options_sets](#dhcp_options_sets)
        - [dhcp_options_sets.all](#dhcp_options_setsall)
        - [dhcp_options_sets.filter](#dhcp_options_setsfilter)
        - [dhcp_options_sets.iterator](#dhcp_options_setsiterator)
        - [dhcp_options_sets.limit](#dhcp_options_setslimit)
        - [dhcp_options_sets.page_size](#dhcp_options_setspage_size)
        - [dhcp_options_sets.pages](#dhcp_options_setspages)
    - [images](#images)
        - [images.all](#imagesall)
        - [images.filter](#imagesfilter)
        - [images.iterator](#imagesiterator)
        - [images.limit](#imageslimit)
        - [images.page_size](#imagespage_size)
        - [images.pages](#imagespages)
    - [instances](#instances)
        - [instances.all](#instancesall)
        - [instances.create_tags](#instancescreate_tags)
        - [instances.filter](#instancesfilter)
        - [instances.iterator](#instancesiterator)
        - [instances.limit](#instanceslimit)
        - [instances.monitor](#instancesmonitor)
        - [instances.page_size](#instancespage_size)
        - [instances.pages](#instancespages)
        - [instances.reboot](#instancesreboot)
        - [instances.start](#instancesstart)
        - [instances.stop](#instancesstop)
        - [instances.terminate](#instancesterminate)
        - [instances.unmonitor](#instancesunmonitor)
    - [internet_gateways](#internet_gateways)
        - [internet_gateways.all](#internet_gatewaysall)
        - [internet_gateways.filter](#internet_gatewaysfilter)
        - [internet_gateways.iterator](#internet_gatewaysiterator)
        - [internet_gateways.limit](#internet_gatewayslimit)
        - [internet_gateways.page_size](#internet_gatewayspage_size)
        - [internet_gateways.pages](#internet_gatewayspages)
    - [key_pairs](#key_pairs)
        - [key_pairs.all](#key_pairsall)
        - [key_pairs.filter](#key_pairsfilter)
        - [key_pairs.iterator](#key_pairsiterator)
        - [key_pairs.limit](#key_pairslimit)
        - [key_pairs.page_size](#key_pairspage_size)
        - [key_pairs.pages](#key_pairspages)
    - [network_acls](#network_acls)
        - [network_acls.all](#network_aclsall)
        - [network_acls.filter](#network_aclsfilter)
        - [network_acls.iterator](#network_aclsiterator)
        - [network_acls.limit](#network_aclslimit)
        - [network_acls.page_size](#network_aclspage_size)
        - [network_acls.pages](#network_aclspages)
    - [network_interfaces](#network_interfaces)
        - [network_interfaces.all](#network_interfacesall)
        - [network_interfaces.filter](#network_interfacesfilter)
        - [network_interfaces.iterator](#network_interfacesiterator)
        - [network_interfaces.limit](#network_interfaceslimit)
        - [network_interfaces.page_size](#network_interfacespage_size)
        - [network_interfaces.pages](#network_interfacespages)
    - [placement_groups](#placement_groups)
        - [placement_groups.all](#placement_groupsall)
        - [placement_groups.filter](#placement_groupsfilter)
        - [placement_groups.iterator](#placement_groupsiterator)
        - [placement_groups.limit](#placement_groupslimit)
        - [placement_groups.page_size](#placement_groupspage_size)
        - [placement_groups.pages](#placement_groupspages)
    - [requested_vpc_peering_connections](#requested_vpc_peering_connections)
        - [requested_vpc_peering_connections.all](#requested_vpc_peering_connectionsall)
        - [requested_vpc_peering_connections.filter](#requested_vpc_peering_connectionsfilter)
        - [requested_vpc_peering_connections.iterator](#requested_vpc_peering_connectionsiterator)
        - [requested_vpc_peering_connections.limit](#requested_vpc_peering_connectionslimit)
        - [requested_vpc_peering_connections.page_size](#requested_vpc_peering_connectionspage_size)
        - [requested_vpc_peering_connections.pages](#requested_vpc_peering_connectionspages)
    - [route_tables](#route_tables)
        - [route_tables.all](#route_tablesall)
        - [route_tables.filter](#route_tablesfilter)
        - [route_tables.iterator](#route_tablesiterator)
        - [route_tables.limit](#route_tableslimit)
        - [route_tables.page_size](#route_tablespage_size)
        - [route_tables.pages](#route_tablespages)
    - [security_groups](#security_groups)
        - [security_groups.all](#security_groupsall)
        - [security_groups.filter](#security_groupsfilter)
        - [security_groups.iterator](#security_groupsiterator)
        - [security_groups.limit](#security_groupslimit)
        - [security_groups.page_size](#security_groupspage_size)
        - [security_groups.pages](#security_groupspages)
    - [snapshots](#snapshots)
        - [snapshots.all](#snapshotsall)
        - [snapshots.filter](#snapshotsfilter)
        - [snapshots.iterator](#snapshotsiterator)
        - [snapshots.limit](#snapshotslimit)
        - [snapshots.page_size](#snapshotspage_size)
        - [snapshots.pages](#snapshotspages)
    - [subnets](#subnets)
        - [subnets.all](#subnetsall)
        - [subnets.filter](#subnetsfilter)
        - [subnets.iterator](#subnetsiterator)
        - [subnets.limit](#subnetslimit)
        - [subnets.page_size](#subnetspage_size)
        - [subnets.pages](#subnetspages)
    - [volumes](#volumes)
        - [volumes.all](#volumesall)
        - [volumes.filter](#volumesfilter)
        - [volumes.iterator](#volumesiterator)
        - [volumes.limit](#volumeslimit)
        - [volumes.page_size](#volumespage_size)
        - [volumes.pages](#volumespages)
    - [vpc_addresses](#vpc_addresses)
        - [vpc_addresses.all](#vpc_addressesall)
        - [vpc_addresses.filter](#vpc_addressesfilter)
        - [vpc_addresses.iterator](#vpc_addressesiterator)
        - [vpc_addresses.limit](#vpc_addresseslimit)
        - [vpc_addresses.page_size](#vpc_addressespage_size)
        - [vpc_addresses.pages](#vpc_addressespages)
    - [vpc_peering_connections](#vpc_peering_connections)
        - [vpc_peering_connections.all](#vpc_peering_connectionsall)
        - [vpc_peering_connections.filter](#vpc_peering_connectionsfilter)
        - [vpc_peering_connections.iterator](#vpc_peering_connectionsiterator)
        - [vpc_peering_connections.limit](#vpc_peering_connectionslimit)
        - [vpc_peering_connections.page_size](#vpc_peering_connectionspage_size)
        - [vpc_peering_connections.pages](#vpc_peering_connectionspages)
    - [vpcs](#vpcs)
        - [vpcs.all](#vpcsall)
        - [vpcs.filter](#vpcsfilter)
        - [vpcs.iterator](#vpcsiterator)
        - [vpcs.limit](#vpcslimit)
        - [vpcs.page_size](#vpcspage_size)
        - [vpcs.pages](#vpcspages)

## ClassicAddress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L339)

```python
class ClassicAddress(Boto3ServiceResource):
```

### ClassicAddress().associate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L352)

```python
def associate(
    AllocationId: str = None,
    InstanceId: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None,
) -> Dict[str, Any]:
```

### ClassicAddress().disassociate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L364)

```python
def disassociate(AssociationId: str = None, DryRun: bool = None) -> None:
```

### ClassicAddress().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L368)

```python
def get_available_subresources() -> List[str]:
```

### ClassicAddress().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L372)

```python
def load() -> None:
```

### ClassicAddress().release

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L376)

```python
def release(AllocationId: str = None, DryRun: bool = None) -> None:
```

### ClassicAddress().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L380)

```python
def reload() -> None:
```

## DhcpOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L384)

```python
class DhcpOptions(Boto3ServiceResource):
```

### DhcpOptions().associate_with_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L392)

```python
def associate_with_vpc(VpcId: str, DryRun: bool = None) -> None:
```

### DhcpOptions().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L396)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### DhcpOptions().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L402)

```python
def delete(DryRun: bool = None) -> None:
```

### DhcpOptions().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L406)

```python
def get_available_subresources() -> List[str]:
```

### DhcpOptions().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L410)

```python
def load() -> None:
```

### DhcpOptions().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L414)

```python
def reload() -> None:
```

## Image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L418)

```python
class Image(Boto3ServiceResource):
```

### Image().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L446)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Image().deregister

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L452)

```python
def deregister(DryRun: bool = None) -> None:
```

### Image().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L456)

```python
def describe_attribute(Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Image().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L460)

```python
def get_available_subresources() -> List[str]:
```

### Image().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L464)

```python
def load() -> None:
```

### Image().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L468)

```python
def modify_attribute(
    Attribute: str = None,
    Description: Dict[str, Any] = None,
    LaunchPermission: Dict[str, Any] = None,
    OperationType: str = None,
    ProductCodes: List[Any] = None,
    UserGroups: List[Any] = None,
    UserIds: List[Any] = None,
    Value: str = None,
    DryRun: bool = None,
) -> None:
```

### Image().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L483)

```python
def reload() -> None:
```

### Image().reset_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L487)

```python
def reset_attribute(Attribute: str, DryRun: bool = None) -> None:
```

### Image().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L491)

```python
def wait_until_exists(
    ExecutableUsers: List[Any] = None,
    Filters: List[Any] = None,
    Owners: List[Any] = None,
    DryRun: bool = None,
) -> None:
```

## Instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L501)

```python
class Instance(Boto3ServiceResource):
```

### Instance().attach_classic_link_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L552)

```python
def attach_classic_link_vpc(
    Groups: List[Any],
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Instance().attach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L558)

```python
def attach_volume(
    Device: str,
    VolumeId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Instance().console_output

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L564)

```python
def console_output(
    DryRun: bool = None,
    Latest: bool = None,
) -> Dict[str, Any]:
```

### Instance().create_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L570)

```python
def create_image(
    Name: str,
    BlockDeviceMappings: List[Any] = None,
    Description: str = None,
    DryRun: bool = None,
    NoReboot: bool = None,
) -> ec2_service_resource_scope.Image:
```

### Instance().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L581)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Instance().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L587)

```python
def delete_tags(DryRun: bool = None, Tags: List[Any] = None) -> None:
```

### Instance().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L591)

```python
def describe_attribute(Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().detach_classic_link_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L595)

```python
def detach_classic_link_vpc(
    VpcId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Instance().detach_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L601)

```python
def detach_volume(
    VolumeId: str,
    Device: str = None,
    Force: bool = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Instance().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L607)

```python
def get_available_subresources() -> List[str]:
```

### Instance().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L611)

```python
def load() -> None:
```

### Instance().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L615)

```python
def modify_attribute(
    SourceDestCheck: Dict[str, Any] = None,
    Attribute: str = None,
    BlockDeviceMappings: List[Any] = None,
    DisableApiTermination: Dict[str, Any] = None,
    DryRun: bool = None,
    EbsOptimized: Dict[str, Any] = None,
    EnaSupport: Dict[str, Any] = None,
    Groups: List[Any] = None,
    InstanceInitiatedShutdownBehavior: Dict[str, Any] = None,
    InstanceType: Dict[str, Any] = None,
    Kernel: Dict[str, Any] = None,
    Ramdisk: Dict[str, Any] = None,
    SriovNetSupport: Dict[str, Any] = None,
    UserData: Dict[str, Any] = None,
    Value: str = None,
) -> None:
```

### Instance().monitor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L636)

```python
def monitor(DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().password_data

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L640)

```python
def password_data(DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().reboot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L644)

```python
def reboot(DryRun: bool = None) -> None:
```

### Instance().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L648)

```python
def reload() -> None:
```

### Instance().report_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L652)

```python
def report_status(
    ReasonCodes: List[Any],
    Status: str,
    Description: str = None,
    DryRun: bool = None,
    EndTime: datetime = None,
    StartTime: datetime = None,
) -> None:
```

### Instance().reset_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L664)

```python
def reset_attribute(Attribute: str, DryRun: bool = None) -> None:
```

### Instance().reset_kernel

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L668)

```python
def reset_kernel(DryRun: bool = None) -> None:
```

### Instance().reset_ramdisk

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L672)

```python
def reset_ramdisk(DryRun: bool = None) -> None:
```

### Instance().reset_source_dest_check

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L676)

```python
def reset_source_dest_check(DryRun: bool = None) -> None:
```

### Instance().start

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L680)

```python
def start(AdditionalInfo: str = None, DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().stop

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L684)

```python
def stop(
    Hibernate: bool = None,
    DryRun: bool = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### Instance().terminate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L690)

```python
def terminate(DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().unmonitor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L694)

```python
def unmonitor(DryRun: bool = None) -> Dict[str, Any]:
```

### Instance().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L698)

```python
def wait_until_exists(
    Filters: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> None:
```

### Instance().wait_until_running

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L708)

```python
def wait_until_running(
    Filters: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> None:
```

### Instance().wait_until_stopped

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L718)

```python
def wait_until_stopped(
    Filters: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> None:
```

### Instance().wait_until_terminated

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L728)

```python
def wait_until_terminated(
    Filters: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> None:
```

## InternetGateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L738)

```python
class InternetGateway(Boto3ServiceResource):
```

### InternetGateway().attach_to_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L746)

```python
def attach_to_vpc(VpcId: str, DryRun: bool = None) -> None:
```

### InternetGateway().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L750)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### InternetGateway().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L756)

```python
def delete(DryRun: bool = None) -> None:
```

### InternetGateway().detach_from_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L760)

```python
def detach_from_vpc(VpcId: str, DryRun: bool = None) -> None:
```

### InternetGateway().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L764)

```python
def get_available_subresources() -> List[str]:
```

### InternetGateway().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L768)

```python
def load() -> None:
```

### InternetGateway().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L772)

```python
def reload() -> None:
```

## KeyPair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L776)

```python
class KeyPair(Boto3ServiceResource):
```

### KeyPair().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L783)

```python
def delete(DryRun: bool = None) -> None:
```

### KeyPair().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L787)

```python
def get_available_subresources() -> List[str]:
```

## KeyPairInfo

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L791)

```python
class KeyPairInfo(Boto3ServiceResource):
```

### KeyPairInfo().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L797)

```python
def delete(DryRun: bool = None) -> None:
```

### KeyPairInfo().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L801)

```python
def get_available_subresources() -> List[str]:
```

### KeyPairInfo().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L805)

```python
def load() -> None:
```

### KeyPairInfo().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L809)

```python
def reload() -> None:
```

## NetworkAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L813)

```python
class NetworkAcl(Boto3ServiceResource):
```

### NetworkAcl().create_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L824)

```python
def create_entry(
    Egress: bool,
    Protocol: str,
    RuleAction: str,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: Dict[str, Any] = None,
    Ipv6CidrBlock: str = None,
    PortRange: Dict[str, Any] = None,
) -> None:
```

### NetworkAcl().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L839)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### NetworkAcl().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L845)

```python
def delete(DryRun: bool = None) -> None:
```

### NetworkAcl().delete_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L849)

```python
def delete_entry(Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
```

### NetworkAcl().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L853)

```python
def get_available_subresources() -> List[str]:
```

### NetworkAcl().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L857)

```python
def load() -> None:
```

### NetworkAcl().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L861)

```python
def reload() -> None:
```

### NetworkAcl().replace_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L865)

```python
def replace_association(
    AssociationId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### NetworkAcl().replace_entry

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L871)

```python
def replace_entry(
    Egress: bool,
    Protocol: str,
    RuleAction: str,
    RuleNumber: int,
    CidrBlock: str = None,
    DryRun: bool = None,
    IcmpTypeCode: Dict[str, Any] = None,
    Ipv6CidrBlock: str = None,
    PortRange: Dict[str, Any] = None,
) -> None:
```

## NetworkInterface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L886)

```python
class NetworkInterface(Boto3ServiceResource):
```

### NetworkInterface().assign_private_ip_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L910)

```python
def assign_private_ip_addresses(
    AllowReassignment: bool = None,
    PrivateIpAddresses: List[Any] = None,
    SecondaryPrivateIpAddressCount: int = None,
) -> Dict[str, Any]:
```

### NetworkInterface().attach

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L919)

```python
def attach(
    DeviceIndex: int,
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### NetworkInterface().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L925)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### NetworkInterface().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L931)

```python
def delete(DryRun: bool = None) -> None:
```

### NetworkInterface().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L935)

```python
def describe_attribute(
    Attribute: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### NetworkInterface().detach

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L941)

```python
def detach(DryRun: bool = None, Force: bool = None) -> None:
```

### NetworkInterface().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L945)

```python
def get_available_subresources() -> List[str]:
```

### NetworkInterface().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L949)

```python
def load() -> None:
```

### NetworkInterface().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L953)

```python
def modify_attribute(
    Attachment: Dict[str, Any] = None,
    Description: Dict[str, Any] = None,
    DryRun: bool = None,
    Groups: List[Any] = None,
    SourceDestCheck: Dict[str, Any] = None,
) -> None:
```

### NetworkInterface().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L964)

```python
def reload() -> None:
```

### NetworkInterface().reset_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L968)

```python
def reset_attribute(DryRun: bool = None, SourceDestCheck: str = None) -> None:
```

### NetworkInterface().unassign_private_ip_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L972)

```python
def unassign_private_ip_addresses(PrivateIpAddresses: List[Any]) -> None:
```

## NetworkInterfaceAssociation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L976)

```python
class NetworkInterfaceAssociation(Boto3ServiceResource):
```

### NetworkInterfaceAssociation().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L983)

```python
def delete(PublicIp: str = None, DryRun: bool = None) -> None:
```

### NetworkInterfaceAssociation().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L987)

```python
def get_available_subresources() -> List[str]:
```

### NetworkInterfaceAssociation().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L991)

```python
def load() -> None:
```

### NetworkInterfaceAssociation().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L995)

```python
def reload() -> None:
```

## PlacementGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L999)

```python
class PlacementGroup(Boto3ServiceResource):
```

### PlacementGroup().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1008)

```python
def delete(DryRun: bool = None) -> None:
```

### PlacementGroup().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1012)

```python
def get_available_subresources() -> List[str]:
```

### PlacementGroup().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1016)

```python
def load() -> None:
```

### PlacementGroup().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1020)

```python
def reload() -> None:
```

## Route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1024)

```python
class Route(Boto3ServiceResource):
```

### Route().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1041)

```python
def delete(DestinationIpv6CidrBlock: str = None, DryRun: bool = None) -> None:
```

### Route().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1045)

```python
def get_available_subresources() -> List[str]:
```

### Route().replace

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1049)

```python
def replace(
    DestinationIpv6CidrBlock: str = None,
    DryRun: bool = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None,
) -> None:
```

## RouteTable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1064)

```python
class RouteTable(Boto3ServiceResource):
```

### RouteTable().associate_with_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1075)

```python
def associate_with_subnet(
    SubnetId: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.RouteTableAssociation:
```

### RouteTable().create_route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1081)

```python
def create_route(
    DestinationCidrBlock: str = None,
    DestinationIpv6CidrBlock: str = None,
    DryRun: bool = None,
    EgressOnlyInternetGatewayId: str = None,
    GatewayId: str = None,
    InstanceId: str = None,
    NatGatewayId: str = None,
    TransitGatewayId: str = None,
    NetworkInterfaceId: str = None,
    VpcPeeringConnectionId: str = None,
) -> ec2_service_resource_scope.Route:
```

### RouteTable().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1097)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### RouteTable().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1103)

```python
def delete(DryRun: bool = None) -> None:
```

### RouteTable().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1107)

```python
def get_available_subresources() -> List[str]:
```

### RouteTable().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1111)

```python
def load() -> None:
```

### RouteTable().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1115)

```python
def reload() -> None:
```

## RouteTableAssociation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1119)

```python
class RouteTableAssociation(Boto3ServiceResource):
```

### RouteTableAssociation().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1127)

```python
def delete(DryRun: bool = None) -> None:
```

### RouteTableAssociation().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1131)

```python
def get_available_subresources() -> List[str]:
```

### RouteTableAssociation().replace_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1135)

```python
def replace_subnet(
    RouteTableId: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.RouteTableAssociation:
```

## SecurityGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1141)

```python
class SecurityGroup(Boto3ServiceResource):
```

### SecurityGroup().authorize_egress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1153)

```python
def authorize_egress(
    DryRun: bool = None,
    IpPermissions: List[Any] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
) -> None:
```

### SecurityGroup().authorize_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1167)

```python
def authorize_ingress(
    CidrIp: str = None,
    FromPort: int = None,
    GroupName: str = None,
    IpPermissions: List[Any] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None,
) -> None:
```

### SecurityGroup().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1182)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### SecurityGroup().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1188)

```python
def delete(GroupName: str = None, DryRun: bool = None) -> None:
```

### SecurityGroup().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1192)

```python
def get_available_subresources() -> List[str]:
```

### SecurityGroup().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1196)

```python
def load() -> None:
```

### SecurityGroup().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1200)

```python
def reload() -> None:
```

### SecurityGroup().revoke_egress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1204)

```python
def revoke_egress(
    DryRun: bool = None,
    IpPermissions: List[Any] = None,
    CidrIp: str = None,
    FromPort: int = None,
    IpProtocol: str = None,
    ToPort: int = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
) -> None:
```

### SecurityGroup().revoke_ingress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1218)

```python
def revoke_ingress(
    CidrIp: str = None,
    FromPort: int = None,
    GroupName: str = None,
    IpPermissions: List[Any] = None,
    IpProtocol: str = None,
    SourceSecurityGroupName: str = None,
    SourceSecurityGroupOwnerId: str = None,
    ToPort: int = None,
    DryRun: bool = None,
) -> None:
```

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L15)

```python
class ServiceResource(Boto3ServiceResource):
```

### ServiceResource().ClassicAddress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L35)

```python
def ClassicAddress(
    public_ip: str = None,
) -> ec2_service_resource_scope.ClassicAddress:
```

### ServiceResource().DhcpOptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L41)

```python
def DhcpOptions(id: str = None) -> ec2_service_resource_scope.DhcpOptions:
```

### ServiceResource().Image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L45)

```python
def Image(id: str = None) -> ec2_service_resource_scope.Image:
```

### ServiceResource().Instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L49)

```python
def Instance(id: str = None) -> ec2_service_resource_scope.Instance:
```

### ServiceResource().InternetGateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L53)

```python
def InternetGateway(
    id: str = None,
) -> ec2_service_resource_scope.InternetGateway:
```

### ServiceResource().KeyPair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L59)

```python
def KeyPair(name: str = None) -> ec2_service_resource_scope.KeyPairInfo:
```

### ServiceResource().NetworkAcl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L63)

```python
def NetworkAcl(id: str = None) -> ec2_service_resource_scope.NetworkAcl:
```

### ServiceResource().NetworkInterface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L67)

```python
def NetworkInterface(
    id: str = None,
) -> ec2_service_resource_scope.NetworkInterface:
```

### ServiceResource().NetworkInterfaceAssociation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L73)

```python
def NetworkInterfaceAssociation(
    id: str = None,
) -> ec2_service_resource_scope.NetworkInterfaceAssociation:
```

### ServiceResource().PlacementGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L79)

```python
def PlacementGroup(
    name: str = None,
) -> ec2_service_resource_scope.PlacementGroup:
```

### ServiceResource().Route

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L85)

```python
def Route(
    route_table_id: str = None,
    destination_cidr_block: str = None,
) -> ec2_service_resource_scope.Route:
```

### ServiceResource().RouteTable

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L91)

```python
def RouteTable(id: str = None) -> ec2_service_resource_scope.RouteTable:
```

### ServiceResource().RouteTableAssociation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L95)

```python
def RouteTableAssociation(
    id: str = None,
) -> ec2_service_resource_scope.RouteTableAssociation:
```

### ServiceResource().SecurityGroup

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L101)

```python
def SecurityGroup(id: str = None) -> ec2_service_resource_scope.SecurityGroup:
```

### ServiceResource().Snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L105)

```python
def Snapshot(id: str = None) -> ec2_service_resource_scope.Snapshot:
```

### ServiceResource().Subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L109)

```python
def Subnet(id: str = None) -> ec2_service_resource_scope.Subnet:
```

### ServiceResource().Tag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L113)

```python
def Tag(
    resource_id: str = None,
    key: str = None,
    value: str = None,
) -> ec2_service_resource_scope.Tag:
```

### ServiceResource().Volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L119)

```python
def Volume(id: str = None) -> ec2_service_resource_scope.Volume:
```

### ServiceResource().Vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L123)

```python
def Vpc(id: str = None) -> ec2_service_resource_scope.Vpc:
```

### ServiceResource().VpcAddress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L127)

```python
def VpcAddress(
    allocation_id: str = None,
) -> ec2_service_resource_scope.VpcAddress:
```

### ServiceResource().VpcPeeringConnection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L133)

```python
def VpcPeeringConnection(
    id: str = None,
) -> ec2_service_resource_scope.VpcPeeringConnection:
```

### ServiceResource().create_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L139)

```python
def create_dhcp_options(
    DhcpConfigurations: List[Any],
    DryRun: bool = None,
) -> ec2_service_resource_scope.DhcpOptions:
```

### ServiceResource().create_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L145)

```python
def create_instances(
    MaxCount: int,
    MinCount: int,
    BlockDeviceMappings: List[Any] = None,
    ImageId: str = None,
    InstanceType: str = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    KernelId: str = None,
    KeyName: str = None,
    Monitoring: Dict[str, Any] = None,
    Placement: Dict[str, Any] = None,
    RamdiskId: str = None,
    SecurityGroupIds: List[Any] = None,
    SecurityGroups: List[Any] = None,
    SubnetId: str = None,
    UserData: str = None,
    AdditionalInfo: str = None,
    ClientToken: str = None,
    DisableApiTermination: bool = None,
    DryRun: bool = None,
    EbsOptimized: bool = None,
    IamInstanceProfile: Dict[str, Any] = None,
    InstanceInitiatedShutdownBehavior: str = None,
    NetworkInterfaces: List[Any] = None,
    PrivateIpAddress: str = None,
    ElasticGpuSpecification: List[Any] = None,
    ElasticInferenceAccelerators: List[Any] = None,
    TagSpecifications: List[Any] = None,
    LaunchTemplate: Dict[str, Any] = None,
    InstanceMarketOptions: Dict[str, Any] = None,
    CreditSpecification: Dict[str, Any] = None,
    CpuOptions: Dict[str, Any] = None,
    CapacityReservationSpecification: Dict[str, Any] = None,
    HibernationOptions: Dict[str, Any] = None,
    LicenseSpecifications: List[Any] = None,
) -> List[ec2_service_resource_scope.Instance]:
```

### ServiceResource().create_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L186)

```python
def create_internet_gateway(
    DryRun: bool = None,
) -> ec2_service_resource_scope.InternetGateway:
```

### ServiceResource().create_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L192)

```python
def create_key_pair(
    KeyName: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.KeyPair:
```

### ServiceResource().create_network_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L198)

```python
def create_network_acl(
    VpcId: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.NetworkAcl:
```

### ServiceResource().create_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L204)

```python
def create_network_interface(
    SubnetId: str,
    Description: str = None,
    DryRun: bool = None,
    Groups: List[Any] = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    PrivateIpAddress: str = None,
    PrivateIpAddresses: List[Any] = None,
    SecondaryPrivateIpAddressCount: int = None,
    InterfaceType: str = None,
) -> ec2_service_resource_scope.NetworkInterface:
```

### ServiceResource().create_placement_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L220)

```python
def create_placement_group(
    DryRun: bool = None,
    GroupName: str = None,
    Strategy: str = None,
    PartitionCount: int = None,
) -> ec2_service_resource_scope.PlacementGroup:
```

### ServiceResource().create_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L230)

```python
def create_route_table(
    VpcId: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.RouteTable:
```

### ServiceResource().create_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L236)

```python
def create_security_group(
    Description: str,
    GroupName: str,
    VpcId: str = None,
    DryRun: bool = None,
) -> ec2_service_resource_scope.SecurityGroup:
```

### ServiceResource().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L242)

```python
def create_snapshot(
    VolumeId: str,
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> ec2_service_resource_scope.Snapshot:
```

### ServiceResource().create_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L252)

```python
def create_subnet(
    CidrBlock: str,
    VpcId: str,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Ipv6CidrBlock: str = None,
    DryRun: bool = None,
) -> ec2_service_resource_scope.Subnet:
```

### ServiceResource().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L264)

```python
def create_tags(
    Resources: List[Any],
    Tags: List[Any],
    DryRun: bool = None,
) -> None:
```

### ServiceResource().create_volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L270)

```python
def create_volume(
    AvailabilityZone: str,
    Encrypted: bool = None,
    Iops: int = None,
    KmsKeyId: str = None,
    Size: int = None,
    SnapshotId: str = None,
    VolumeType: str = None,
    DryRun: bool = None,
    TagSpecifications: List[Any] = None,
) -> ec2_service_resource_scope.Volume:
```

### ServiceResource().create_vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L285)

```python
def create_vpc(
    CidrBlock: str,
    AmazonProvidedIpv6CidrBlock: bool = None,
    DryRun: bool = None,
    InstanceTenancy: str = None,
) -> ec2_service_resource_scope.Vpc:
```

### ServiceResource().create_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L295)

```python
def create_vpc_peering_connection(
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    VpcId: str = None,
    PeerRegion: str = None,
) -> ec2_service_resource_scope.VpcPeeringConnection:
```

### ServiceResource().disassociate_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L306)

```python
def disassociate_route_table(AssociationId: str, DryRun: bool = None) -> None:
```

### ServiceResource().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L310)

```python
def get_available_subresources() -> List[str]:
```

### ServiceResource().import_key_pair

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L314)

```python
def import_key_pair(
    KeyName: str,
    PublicKeyMaterial: bytes,
    DryRun: bool = None,
) -> ec2_service_resource_scope.KeyPairInfo:
```

### ServiceResource().register_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L320)

```python
def register_image(
    Name: str,
    ImageLocation: str = None,
    Architecture: str = None,
    BlockDeviceMappings: List[Any] = None,
    Description: str = None,
    DryRun: bool = None,
    EnaSupport: bool = None,
    KernelId: str = None,
    BillingProducts: List[Any] = None,
    RamdiskId: str = None,
    RootDeviceName: str = None,
    SriovNetSupport: str = None,
    VirtualizationType: str = None,
) -> ec2_service_resource_scope.Image:
```

## Snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1233)

```python
class Snapshot(Boto3ServiceResource):
```

### Snapshot().copy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1251)

```python
def copy(
    SourceRegion: str,
    Description: str = None,
    DestinationRegion: str = None,
    Encrypted: bool = None,
    KmsKeyId: str = None,
    PresignedUrl: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Snapshot().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1264)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Snapshot().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1270)

```python
def delete(DryRun: bool = None) -> None:
```

### Snapshot().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1274)

```python
def describe_attribute(Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Snapshot().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1278)

```python
def get_available_subresources() -> List[str]:
```

### Snapshot().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1282)

```python
def load() -> None:
```

### Snapshot().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1286)

```python
def modify_attribute(
    Attribute: str = None,
    CreateVolumePermission: Dict[str, Any] = None,
    GroupNames: List[Any] = None,
    OperationType: str = None,
    UserIds: List[Any] = None,
    DryRun: bool = None,
) -> None:
```

### Snapshot().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1298)

```python
def reload() -> None:
```

### Snapshot().reset_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1302)

```python
def reset_attribute(Attribute: str, DryRun: bool = None) -> None:
```

### Snapshot().wait_until_completed

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1306)

```python
def wait_until_completed(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    OwnerIds: List[Any] = None,
    RestorableByUserIds: List[Any] = None,
    DryRun: bool = None,
) -> None:
```

## Subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1318)

```python
class Subnet(Boto3ServiceResource):
```

### Subnet().create_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1338)

```python
def create_instances(
    MaxCount: int,
    MinCount: int,
    BlockDeviceMappings: List[Any] = None,
    ImageId: str = None,
    InstanceType: str = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    KernelId: str = None,
    KeyName: str = None,
    Monitoring: Dict[str, Any] = None,
    Placement: Dict[str, Any] = None,
    RamdiskId: str = None,
    SecurityGroupIds: List[Any] = None,
    SecurityGroups: List[Any] = None,
    UserData: str = None,
    AdditionalInfo: str = None,
    ClientToken: str = None,
    DisableApiTermination: bool = None,
    DryRun: bool = None,
    EbsOptimized: bool = None,
    IamInstanceProfile: Dict[str, Any] = None,
    InstanceInitiatedShutdownBehavior: str = None,
    NetworkInterfaces: List[Any] = None,
    PrivateIpAddress: str = None,
    ElasticGpuSpecification: List[Any] = None,
    ElasticInferenceAccelerators: List[Any] = None,
    TagSpecifications: List[Any] = None,
    LaunchTemplate: Dict[str, Any] = None,
    InstanceMarketOptions: Dict[str, Any] = None,
    CreditSpecification: Dict[str, Any] = None,
    CpuOptions: Dict[str, Any] = None,
    CapacityReservationSpecification: Dict[str, Any] = None,
    HibernationOptions: Dict[str, Any] = None,
    LicenseSpecifications: List[Any] = None,
) -> List[ec2_service_resource_scope.Instance]:
```

### Subnet().create_network_interface

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1378)

```python
def create_network_interface(
    Description: str = None,
    DryRun: bool = None,
    Groups: List[Any] = None,
    Ipv6AddressCount: int = None,
    Ipv6Addresses: List[Any] = None,
    PrivateIpAddress: str = None,
    PrivateIpAddresses: List[Any] = None,
    SecondaryPrivateIpAddressCount: int = None,
    InterfaceType: str = None,
) -> ec2_service_resource_scope.NetworkInterface:
```

### Subnet().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1393)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Subnet().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1399)

```python
def delete(DryRun: bool = None) -> None:
```

### Subnet().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1403)

```python
def get_available_subresources() -> List[str]:
```

### Subnet().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1407)

```python
def load() -> None:
```

### Subnet().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1411)

```python
def reload() -> None:
```

## Tag

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1415)

```python
class Tag(Boto3ServiceResource):
```

### Tag().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1422)

```python
def delete(DryRun: bool = None) -> None:
```

### Tag().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1426)

```python
def get_available_subresources() -> List[str]:
```

### Tag().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1430)

```python
def load() -> None:
```

### Tag().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1434)

```python
def reload() -> None:
```

## Volume

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1438)

```python
class Volume(Boto3ServiceResource):
```

### Volume().attach_to_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1455)

```python
def attach_to_instance(
    Device: str,
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Volume().create_snapshot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1461)

```python
def create_snapshot(
    Description: str = None,
    TagSpecifications: List[Any] = None,
    DryRun: bool = None,
) -> ec2_service_resource_scope.Snapshot:
```

### Volume().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1470)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Volume().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1476)

```python
def delete(DryRun: bool = None) -> None:
```

### Volume().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1480)

```python
def describe_attribute(Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Volume().describe_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1484)

```python
def describe_status(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Volume().detach_from_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1494)

```python
def detach_from_instance(
    Device: str = None,
    Force: bool = None,
    InstanceId: str = None,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Volume().enable_io

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1504)

```python
def enable_io(DryRun: bool = None) -> None:
```

### Volume().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1508)

```python
def get_available_subresources() -> List[str]:
```

### Volume().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1512)

```python
def load() -> None:
```

### Volume().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1516)

```python
def modify_attribute(
    AutoEnableIO: Dict[str, Any] = None,
    DryRun: bool = None,
) -> None:
```

### Volume().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1522)

```python
def reload() -> None:
```

## Vpc

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1526)

```python
class Vpc(Boto3ServiceResource):
```

### Vpc().associate_dhcp_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1549)

```python
def associate_dhcp_options(DhcpOptionsId: str, DryRun: bool = None) -> None:
```

### Vpc().attach_classic_link_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1553)

```python
def attach_classic_link_instance(
    Groups: List[Any],
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Vpc().attach_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1559)

```python
def attach_internet_gateway(
    InternetGatewayId: str,
    DryRun: bool = None,
) -> None:
```

### Vpc().create_network_acl

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1565)

```python
def create_network_acl(
    DryRun: bool = None,
) -> ec2_service_resource_scope.NetworkAcl:
```

### Vpc().create_route_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1571)

```python
def create_route_table(
    DryRun: bool = None,
) -> ec2_service_resource_scope.RouteTable:
```

### Vpc().create_security_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1577)

```python
def create_security_group(
    Description: str,
    GroupName: str,
    DryRun: bool = None,
) -> ec2_service_resource_scope.SecurityGroup:
```

### Vpc().create_subnet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1583)

```python
def create_subnet(
    CidrBlock: str,
    AvailabilityZone: str = None,
    AvailabilityZoneId: str = None,
    Ipv6CidrBlock: str = None,
    DryRun: bool = None,
) -> ec2_service_resource_scope.Subnet:
```

### Vpc().create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1594)

```python
def create_tags(
    Tags: List[Any],
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Tag]:
```

### Vpc().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1600)

```python
def delete(DryRun: bool = None) -> None:
```

### Vpc().describe_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1604)

```python
def describe_attribute(Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
```

### Vpc().detach_classic_link_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1608)

```python
def detach_classic_link_instance(
    InstanceId: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Vpc().detach_internet_gateway

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1614)

```python
def detach_internet_gateway(
    InternetGatewayId: str,
    DryRun: bool = None,
) -> None:
```

### Vpc().disable_classic_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1620)

```python
def disable_classic_link(DryRun: bool = None) -> Dict[str, Any]:
```

### Vpc().enable_classic_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1624)

```python
def enable_classic_link(DryRun: bool = None) -> Dict[str, Any]:
```

### Vpc().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1628)

```python
def get_available_subresources() -> List[str]:
```

### Vpc().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1632)

```python
def load() -> None:
```

### Vpc().modify_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1636)

```python
def modify_attribute(
    EnableDnsHostnames: Dict[str, Any] = None,
    EnableDnsSupport: Dict[str, Any] = None,
) -> None:
```

### Vpc().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1644)

```python
def reload() -> None:
```

### Vpc().request_vpc_peering_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1648)

```python
def request_vpc_peering_connection(
    DryRun: bool = None,
    PeerOwnerId: str = None,
    PeerVpcId: str = None,
    PeerRegion: str = None,
) -> ec2_service_resource_scope.VpcPeeringConnection:
```

### Vpc().wait_until_available

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1658)

```python
def wait_until_available(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> None:
```

### Vpc().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1668)

```python
def wait_until_exists(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> None:
```

## VpcAddress

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1722)

```python
class VpcAddress(Boto3ServiceResource):
```

### VpcAddress().associate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1735)

```python
def associate(
    InstanceId: str = None,
    PublicIp: str = None,
    AllowReassociation: bool = None,
    DryRun: bool = None,
    NetworkInterfaceId: str = None,
    PrivateIpAddress: str = None,
) -> Dict[str, Any]:
```

### VpcAddress().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1747)

```python
def get_available_subresources() -> List[str]:
```

### VpcAddress().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1751)

```python
def load() -> None:
```

### VpcAddress().release

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1755)

```python
def release(PublicIp: str = None, DryRun: bool = None) -> None:
```

### VpcAddress().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1759)

```python
def reload() -> None:
```

## VpcPeeringConnection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1678)

```python
class VpcPeeringConnection(Boto3ServiceResource):
```

### VpcPeeringConnection().accept

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1688)

```python
def accept(DryRun: bool = None) -> Dict[str, Any]:
```

### VpcPeeringConnection().delete

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1692)

```python
def delete(DryRun: bool = None) -> Dict[str, Any]:
```

### VpcPeeringConnection().get_available_subresources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1696)

```python
def get_available_subresources() -> List[str]:
```

### VpcPeeringConnection().load

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1700)

```python
def load() -> None:
```

### VpcPeeringConnection().reject

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1704)

```python
def reject(DryRun: bool = None) -> Dict[str, Any]:
```

### VpcPeeringConnection().reload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1708)

```python
def reload() -> None:
```

### VpcPeeringConnection().wait_until_exists

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1712)

```python
def wait_until_exists(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> None:
```

## accepted_vpc_peering_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2487)

```python
class accepted_vpc_peering_connections(ResourceCollection):
```

### accepted_vpc_peering_connections.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2488)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### accepted_vpc_peering_connections.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2493)

```python
@classmethod
def filter(
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### accepted_vpc_peering_connections.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2504)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### accepted_vpc_peering_connections.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2509)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### accepted_vpc_peering_connections.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2516)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### accepted_vpc_peering_connections.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2523)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## classic_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1763)

```python
class classic_addresses(ResourceCollection):
```

### classic_addresses.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1764)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.ClassicAddress]:
```

### classic_addresses.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1769)

```python
@classmethod
def filter(
    PublicIps: List[Any] = None,
    AllocationIds: List[Any] = None,
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.ClassicAddress]:
```

### classic_addresses.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1779)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### classic_addresses.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1784)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.ClassicAddress]:
```

### classic_addresses.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1791)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.ClassicAddress]:
```

### classic_addresses.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1798)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## dhcp_options_sets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1804)

```python
class dhcp_options_sets(ResourceCollection):
```

### dhcp_options_sets.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1805)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.DhcpOptions]:
```

### dhcp_options_sets.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1810)

```python
@classmethod
def filter(
    DhcpOptionsIds: List[Any] = None,
    Filters: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.DhcpOptions]:
```

### dhcp_options_sets.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1822)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### dhcp_options_sets.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1827)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.DhcpOptions]:
```

### dhcp_options_sets.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1832)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.DhcpOptions]:
```

### dhcp_options_sets.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1839)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1845)

```python
class images(ResourceCollection):
```

### images.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1846)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Image]:
```

### images.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1851)

```python
@classmethod
def filter(
    ExecutableUsers: List[Any] = None,
    Filters: List[Any] = None,
    ImageIds: List[Any] = None,
    Owners: List[Any] = None,
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Image]:
```

### images.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1863)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### images.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1868)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Image]:
```

### images.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1873)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Image]:
```

### images.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1878)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1884)

```python
class instances(ResourceCollection):
```

### instances.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1885)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Instance]:
```

### instances.create_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1890)

```python
@classmethod
def create_tags(Tags: List[Any], DryRun: bool = None) -> None:
```

### instances.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1895)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    InstanceIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> List[ec2_service_resource_scope.Instance]:
```

### instances.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1907)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### instances.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1912)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Instance]:
```

### instances.monitor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1917)

```python
@classmethod
def monitor(DryRun: bool = None) -> Dict[str, Any]:
```

### instances.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1922)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Instance]:
```

### instances.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1927)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

### instances.reboot

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1932)

```python
@classmethod
def reboot(DryRun: bool = None) -> None:
```

### instances.start

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1937)

```python
@classmethod
def start(AdditionalInfo: str = None, DryRun: bool = None) -> Dict[str, Any]:
```

### instances.stop

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1942)

```python
@classmethod
def stop(
    Hibernate: bool = None,
    DryRun: bool = None,
    Force: bool = None,
) -> Dict[str, Any]:
```

### instances.terminate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1949)

```python
@classmethod
def terminate(DryRun: bool = None) -> Dict[str, Any]:
```

### instances.unmonitor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1954)

```python
@classmethod
def unmonitor(DryRun: bool = None) -> Dict[str, Any]:
```

## internet_gateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1960)

```python
class internet_gateways(ResourceCollection):
```

### internet_gateways.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1961)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.InternetGateway]:
```

### internet_gateways.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1966)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    InternetGatewayIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.InternetGateway]:
```

### internet_gateways.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1978)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### internet_gateways.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1983)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.InternetGateway]:
```

### internet_gateways.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1990)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.InternetGateway]:
```

### internet_gateways.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L1997)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## key_pairs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2003)

```python
class key_pairs(ResourceCollection):
```

### key_pairs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2004)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.KeyPairInfo]:
```

### key_pairs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2009)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    KeyNames: List[Any] = None,
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.KeyPairInfo]:
```

### key_pairs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2016)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### key_pairs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2021)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.KeyPairInfo]:
```

### key_pairs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2026)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.KeyPairInfo]:
```

### key_pairs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2033)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## network_acls

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2039)

```python
class network_acls(ResourceCollection):
```

### network_acls.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2040)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.NetworkAcl]:
```

### network_acls.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2045)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NetworkAclIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.NetworkAcl]:
```

### network_acls.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2057)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### network_acls.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2062)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.NetworkAcl]:
```

### network_acls.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2067)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.NetworkAcl]:
```

### network_acls.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2074)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## network_interfaces

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2080)

```python
class network_interfaces(ResourceCollection):
```

### network_interfaces.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2081)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.NetworkInterface]:
```

### network_interfaces.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2086)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    NetworkInterfaceIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.NetworkInterface]:
```

### network_interfaces.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2098)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### network_interfaces.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2103)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.NetworkInterface]:
```

### network_interfaces.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2110)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.NetworkInterface]:
```

### network_interfaces.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2117)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## placement_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2123)

```python
class placement_groups(ResourceCollection):
```

### placement_groups.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2124)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.PlacementGroup]:
```

### placement_groups.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2129)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    GroupNames: List[Any] = None,
) -> List[ec2_service_resource_scope.PlacementGroup]:
```

### placement_groups.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2139)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### placement_groups.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2144)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.PlacementGroup]:
```

### placement_groups.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2151)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.PlacementGroup]:
```

### placement_groups.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2158)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## requested_vpc_peering_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2529)

```python
class requested_vpc_peering_connections(ResourceCollection):
```

### requested_vpc_peering_connections.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2530)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### requested_vpc_peering_connections.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2535)

```python
@classmethod
def filter(
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### requested_vpc_peering_connections.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2546)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### requested_vpc_peering_connections.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2551)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### requested_vpc_peering_connections.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2558)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### requested_vpc_peering_connections.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2565)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## route_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2164)

```python
class route_tables(ResourceCollection):
```

### route_tables.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2165)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.RouteTable]:
```

### route_tables.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2170)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    RouteTableIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.RouteTable]:
```

### route_tables.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2182)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### route_tables.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2187)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.RouteTable]:
```

### route_tables.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2192)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.RouteTable]:
```

### route_tables.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2199)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## security_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2205)

```python
class security_groups(ResourceCollection):
```

### security_groups.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2206)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.SecurityGroup]:
```

### security_groups.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2211)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    GroupIds: List[Any] = None,
    GroupNames: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.SecurityGroup]:
```

### security_groups.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2224)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### security_groups.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2229)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.SecurityGroup]:
```

### security_groups.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2234)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.SecurityGroup]:
```

### security_groups.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2241)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## snapshots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2247)

```python
class snapshots(ResourceCollection):
```

### snapshots.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2248)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Snapshot]:
```

### snapshots.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2253)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    OwnerIds: List[Any] = None,
    RestorableByUserIds: List[Any] = None,
    SnapshotIds: List[Any] = None,
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.Snapshot]:
```

### snapshots.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2267)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### snapshots.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2272)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Snapshot]:
```

### snapshots.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2277)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Snapshot]:
```

### snapshots.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2282)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## subnets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2288)

```python
class subnets(ResourceCollection):
```

### subnets.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2289)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Subnet]:
```

### subnets.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2294)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    SubnetIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.Subnet]:
```

### subnets.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2306)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### subnets.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2311)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Subnet]:
```

### subnets.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2316)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Subnet]:
```

### subnets.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2321)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## volumes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2327)

```python
class volumes(ResourceCollection):
```

### volumes.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2328)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Volume]:
```

### volumes.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2333)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    VolumeIds: List[Any] = None,
    DryRun: bool = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> List[ec2_service_resource_scope.Volume]:
```

### volumes.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2345)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### volumes.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2350)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Volume]:
```

### volumes.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2355)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Volume]:
```

### volumes.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2360)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## vpc_addresses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2366)

```python
class vpc_addresses(ResourceCollection):
```

### vpc_addresses.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2367)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.VpcAddress]:
```

### vpc_addresses.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2372)

```python
@classmethod
def filter(
    PublicIps: List[Any] = None,
    AllocationIds: List[Any] = None,
    DryRun: bool = None,
) -> List[ec2_service_resource_scope.VpcAddress]:
```

### vpc_addresses.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2382)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### vpc_addresses.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2387)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.VpcAddress]:
```

### vpc_addresses.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2392)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcAddress]:
```

### vpc_addresses.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2399)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## vpc_peering_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2405)

```python
class vpc_peering_connections(ResourceCollection):
```

### vpc_peering_connections.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2406)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### vpc_peering_connections.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2411)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    DryRun: bool = None,
    VpcPeeringConnectionIds: List[Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### vpc_peering_connections.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2423)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### vpc_peering_connections.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2428)

```python
@classmethod
def limit(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### vpc_peering_connections.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2435)

```python
@classmethod
def page_size(
    count: int = None,
) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
```

### vpc_peering_connections.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2442)

```python
@classmethod
def pages() -> List[ServiceResource]:
```

## vpcs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2448)

```python
class vpcs(ResourceCollection):
```

### vpcs.all

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2449)

```python
@classmethod
def all() -> List[ec2_service_resource_scope.Vpc]:
```

### vpcs.filter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2454)

```python
@classmethod
def filter(
    Filters: List[Any] = None,
    VpcIds: List[Any] = None,
    DryRun: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> List[ec2_service_resource_scope.Vpc]:
```

### vpcs.iterator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2466)

```python
@classmethod
def iterator() -> ResourceCollection:
```

### vpcs.limit

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2471)

```python
@classmethod
def limit(count: int = None) -> List[ec2_service_resource_scope.Vpc]:
```

### vpcs.page_size

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2476)

```python
@classmethod
def page_size(count: int = None) -> List[ec2_service_resource_scope.Vpc]:
```

### vpcs.pages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ec2/service_resource.py#L2481)

```python
@classmethod
def pages() -> List[ServiceResource]:
```
