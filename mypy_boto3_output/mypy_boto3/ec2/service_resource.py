from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3.ec2.service_resource as ec2_service_resource_scope


class ServiceResource(Boto3ServiceResource):
    classic_addresses: ec2_service_resource_scope.classic_addresses
    dhcp_options_sets: ec2_service_resource_scope.dhcp_options_sets
    images: ec2_service_resource_scope.images
    instances: ec2_service_resource_scope.instances
    internet_gateways: ec2_service_resource_scope.internet_gateways
    key_pairs: ec2_service_resource_scope.key_pairs
    network_acls: ec2_service_resource_scope.network_acls
    network_interfaces: ec2_service_resource_scope.network_interfaces
    placement_groups: ec2_service_resource_scope.placement_groups
    route_tables: ec2_service_resource_scope.route_tables
    security_groups: ec2_service_resource_scope.security_groups
    snapshots: ec2_service_resource_scope.snapshots
    subnets: ec2_service_resource_scope.subnets
    volumes: ec2_service_resource_scope.volumes
    vpc_addresses: ec2_service_resource_scope.vpc_addresses
    vpc_peering_connections: ec2_service_resource_scope.vpc_peering_connections
    vpcs: ec2_service_resource_scope.vpcs

    # pylint: disable=arguments-differ
    def ClassicAddress(
        self, public_ip: str = None
    ) -> ec2_service_resource_scope.ClassicAddress:
        pass

    # pylint: disable=arguments-differ
    def DhcpOptions(self, id: str = None) -> ec2_service_resource_scope.DhcpOptions:
        pass

    # pylint: disable=arguments-differ
    def Image(self, id: str = None) -> ec2_service_resource_scope.Image:
        pass

    # pylint: disable=arguments-differ
    def Instance(self, id: str = None) -> ec2_service_resource_scope.Instance:
        pass

    # pylint: disable=arguments-differ
    def InternetGateway(
        self, id: str = None
    ) -> ec2_service_resource_scope.InternetGateway:
        pass

    # pylint: disable=arguments-differ
    def KeyPair(self, name: str = None) -> ec2_service_resource_scope.KeyPairInfo:
        pass

    # pylint: disable=arguments-differ
    def NetworkAcl(self, id: str = None) -> ec2_service_resource_scope.NetworkAcl:
        pass

    # pylint: disable=arguments-differ
    def NetworkInterface(
        self, id: str = None
    ) -> ec2_service_resource_scope.NetworkInterface:
        pass

    # pylint: disable=arguments-differ
    def NetworkInterfaceAssociation(
        self, id: str = None
    ) -> ec2_service_resource_scope.NetworkInterfaceAssociation:
        pass

    # pylint: disable=arguments-differ
    def PlacementGroup(
        self, name: str = None
    ) -> ec2_service_resource_scope.PlacementGroup:
        pass

    # pylint: disable=arguments-differ
    def Route(
        self, route_table_id: str = None, destination_cidr_block: str = None
    ) -> ec2_service_resource_scope.Route:
        pass

    # pylint: disable=arguments-differ
    def RouteTable(self, id: str = None) -> ec2_service_resource_scope.RouteTable:
        pass

    # pylint: disable=arguments-differ
    def RouteTableAssociation(
        self, id: str = None
    ) -> ec2_service_resource_scope.RouteTableAssociation:
        pass

    # pylint: disable=arguments-differ
    def SecurityGroup(self, id: str = None) -> ec2_service_resource_scope.SecurityGroup:
        pass

    # pylint: disable=arguments-differ
    def Snapshot(self, id: str = None) -> ec2_service_resource_scope.Snapshot:
        pass

    # pylint: disable=arguments-differ
    def Subnet(self, id: str = None) -> ec2_service_resource_scope.Subnet:
        pass

    # pylint: disable=arguments-differ
    def Tag(
        self, resource_id: str = None, key: str = None, value: str = None
    ) -> ec2_service_resource_scope.Tag:
        pass

    # pylint: disable=arguments-differ
    def Volume(self, id: str = None) -> ec2_service_resource_scope.Volume:
        pass

    # pylint: disable=arguments-differ
    def Vpc(self, id: str = None) -> ec2_service_resource_scope.Vpc:
        pass

    # pylint: disable=arguments-differ
    def VpcAddress(
        self, allocation_id: str = None
    ) -> ec2_service_resource_scope.VpcAddress:
        pass

    # pylint: disable=arguments-differ
    def VpcPeeringConnection(
        self, id: str = None
    ) -> ec2_service_resource_scope.VpcPeeringConnection:
        pass

    # pylint: disable=arguments-differ
    def create_dhcp_options(
        self, DhcpConfigurations: List[Any], DryRun: bool = None
    ) -> ec2_service_resource_scope.DhcpOptions:
        pass

    # pylint: disable=arguments-differ
    def create_instances(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_internet_gateway(
        self, DryRun: bool = None
    ) -> ec2_service_resource_scope.InternetGateway:
        pass

    # pylint: disable=arguments-differ
    def create_key_pair(
        self, KeyName: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.KeyPair:
        pass

    # pylint: disable=arguments-differ
    def create_network_acl(
        self, VpcId: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.NetworkAcl:
        pass

    # pylint: disable=arguments-differ
    def create_network_interface(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: str = None,
        PartitionCount: int = None,
    ) -> ec2_service_resource_scope.PlacementGroup:
        pass

    # pylint: disable=arguments-differ
    def create_route_table(
        self, VpcId: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.RouteTable:
        pass

    # pylint: disable=arguments-differ
    def create_security_group(
        self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None
    ) -> ec2_service_resource_scope.SecurityGroup:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        TagSpecifications: List[Any] = None,
        DryRun: bool = None,
    ) -> ec2_service_resource_scope.Snapshot:
        pass

    # pylint: disable=arguments-differ
    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        DryRun: bool = None,
    ) -> ec2_service_resource_scope.Subnet:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Resources: List[Any], Tags: List[Any], DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_volume(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        DryRun: bool = None,
        InstanceTenancy: str = None,
    ) -> ec2_service_resource_scope.Vpc:
        pass

    # pylint: disable=arguments-differ
    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
    ) -> ec2_service_resource_scope.VpcPeeringConnection:
        pass

    # pylint: disable=arguments-differ
    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def import_key_pair(
        self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None
    ) -> ec2_service_resource_scope.KeyPairInfo:
        pass

    # pylint: disable=arguments-differ
    def register_image(
        self,
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
        pass


class ClassicAddress(Boto3ServiceResource):
    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List
    public_ipv4_pool: str
    public_ip: str

    # pylint: disable=arguments-differ
    def associate(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate(self, AssociationId: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def release(self, AllocationId: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class DhcpOptions(Boto3ServiceResource):
    dhcp_configurations: List
    dhcp_options_id: str
    owner_id: str
    tags: List
    id: str

    # pylint: disable=arguments-differ
    def associate_with_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Image(Boto3ServiceResource):
    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    product_codes: List
    ramdisk_id: str
    state: str
    block_device_mappings: List
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict
    tags: List
    virtualization_type: str
    id: str

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def deregister(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_attribute(self, Attribute: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
        ExecutableUsers: List[Any] = None,
        Filters: List[Any] = None,
        Owners: List[Any] = None,
        DryRun: bool = None,
    ) -> None:
        pass


class Instance(Boto3ServiceResource):
    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict
    placement: Dict
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict
    instance_lifecycle: str
    elastic_gpu_associations: List
    elastic_inference_accelerator_associations: List
    network_interfaces_attribute: List
    root_device_name: str
    root_device_type: str
    security_groups: List
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict
    tags: List
    virtualization_type: str
    cpu_options: Dict
    capacity_reservation_id: str
    capacity_reservation_specification: Dict
    hibernation_options: Dict
    licenses: List
    id: str
    volumes: ec2_service_resource_scope.volumes
    vpc_addresses: ec2_service_resource_scope.vpc_addresses

    # pylint: disable=arguments-differ
    def attach_classic_link_vpc(
        self, Groups: List[Any], VpcId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_volume(
        self, Device: str, VolumeId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def console_output(
        self, DryRun: bool = None, Latest: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_image(
        self,
        Name: str,
        BlockDeviceMappings: List[Any] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
    ) -> ec2_service_resource_scope.Image:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(self, DryRun: bool = None, Tags: List[Any] = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_classic_link_vpc(
        self, VpcId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_volume(
        self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def monitor(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def password_data(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reboot(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def report_status(
        self,
        ReasonCodes: List[Any],
        Status: str,
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_attribute(self, Attribute: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_kernel(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_ramdisk(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_source_dest_check(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def terminate(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def unmonitor(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_running(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_stopped(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_terminated(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> None:
        pass


class InternetGateway(Boto3ServiceResource):
    attachments: List
    internet_gateway_id: str
    owner_id: str
    tags: List
    id: str

    # pylint: disable=arguments-differ
    def attach_to_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def detach_from_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class KeyPair(Boto3ServiceResource):
    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass


class KeyPairInfo(Boto3ServiceResource):
    key_fingerprint: str
    key_name: str
    name: str

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class NetworkAcl(Boto3ServiceResource):
    associations: List
    entries: List
    is_default: bool
    network_acl_id: str
    tags: List
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ
    def create_entry(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def replace_association(
        self, AssociationId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def replace_entry(
        self,
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
        pass


class NetworkInterface(Boto3ServiceResource):
    association_attribute: Dict
    attachment: Dict
    availability_zone: str
    description: str
    groups: List
    interface_type: str
    ipv6_addresses: List
    mac_address: str
    network_interface_id: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ
    def assign_private_ip_addresses(
        self,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[Any] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach(
        self, DeviceIndex: int, InstanceId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(
        self, Attribute: str = None, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach(self, DryRun: bool = None, Force: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self,
        Attachment: Dict[str, Any] = None,
        Description: Dict[str, Any] = None,
        DryRun: bool = None,
        Groups: List[Any] = None,
        SourceDestCheck: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def unassign_private_ip_addresses(self, PrivateIpAddresses: List[Any]) -> None:
        pass


class NetworkInterfaceAssociation(Boto3ServiceResource):
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    # pylint: disable=arguments-differ
    def delete(self, PublicIp: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class PlacementGroup(Boto3ServiceResource):
    group_name: str
    state: str
    strategy: str
    partition_count: int
    name: str
    instances: ec2_service_resource_scope.instances

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Route(Boto3ServiceResource):
    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    # pylint: disable=arguments-differ
    def delete(self, DestinationIpv6CidrBlock: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def replace(
        self,
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
        pass


class RouteTable(Boto3ServiceResource):
    associations_attribute: List
    propagating_vgws: List
    route_table_id: str
    routes_attribute: List
    tags: List
    vpc_id: str
    owner_id: str
    id: str

    # pylint: disable=arguments-differ
    def associate_with_subnet(
        self, SubnetId: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.RouteTableAssociation:
        pass

    # pylint: disable=arguments-differ
    def create_route(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class RouteTableAssociation(Boto3ServiceResource):
    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    id: str

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def replace_subnet(
        self, RouteTableId: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.RouteTableAssociation:
        pass


class SecurityGroup(Boto3ServiceResource):
    description: str
    group_name: str
    ip_permissions: List
    owner_id: str
    group_id: str
    ip_permissions_egress: List
    tags: List
    vpc_id: str
    id: str

    # pylint: disable=arguments-differ
    def authorize_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List[Any] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def authorize_ingress(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, GroupName: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def revoke_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List[Any] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def revoke_ingress(
        self,
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
        pass


class Snapshot(Boto3ServiceResource):
    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    tags: List
    id: str

    # pylint: disable=arguments-differ
    def copy(
        self,
        SourceRegion: str,
        Description: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self,
        Attribute: str = None,
        CreateVolumePermission: Dict[str, Any] = None,
        GroupNames: List[Any] = None,
        OperationType: str = None,
        UserIds: List[Any] = None,
        DryRun: bool = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reset_attribute(self, Attribute: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_completed(
        self,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[Any] = None,
        RestorableByUserIds: List[Any] = None,
        DryRun: bool = None,
    ) -> None:
        pass


class Subnet(Boto3ServiceResource):
    availability_zone: str
    availability_zone_id: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    state: str
    subnet_id: str
    vpc_id: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List
    tags: List
    subnet_arn: str
    id: str
    instances: ec2_service_resource_scope.instances
    network_interfaces: ec2_service_resource_scope.network_interfaces

    # pylint: disable=arguments-differ
    def create_instances(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_network_interface(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Tag(Boto3ServiceResource):
    resource_type: str
    resource_id: str
    key: str
    value: str

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Volume(Boto3ServiceResource):
    attachments: List
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List
    volume_type: str
    id: str
    snapshots: ec2_service_resource_scope.snapshots

    # pylint: disable=arguments-differ
    def attach_to_instance(
        self, Device: str, InstanceId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_snapshot(
        self,
        Description: str = None,
        TagSpecifications: List[Any] = None,
        DryRun: bool = None,
    ) -> ec2_service_resource_scope.Snapshot:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_status(
        self,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_from_instance(
        self,
        Device: str = None,
        Force: bool = None,
        InstanceId: str = None,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_io(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self, AutoEnableIO: Dict[str, Any] = None, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class Vpc(Boto3ServiceResource):
    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    owner_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List
    cidr_block_association_set: List
    is_default: bool
    tags: List
    id: str
    accepted_vpc_peering_connections: ec2_service_resource_scope.accepted_vpc_peering_connections
    instances: ec2_service_resource_scope.instances
    internet_gateways: ec2_service_resource_scope.internet_gateways
    network_acls: ec2_service_resource_scope.network_acls
    network_interfaces: ec2_service_resource_scope.network_interfaces
    requested_vpc_peering_connections: ec2_service_resource_scope.requested_vpc_peering_connections
    route_tables: ec2_service_resource_scope.route_tables
    security_groups: ec2_service_resource_scope.security_groups
    subnets: ec2_service_resource_scope.subnets

    # pylint: disable=arguments-differ
    def associate_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def attach_classic_link_instance(
        self, Groups: List[Any], InstanceId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_internet_gateway(
        self, InternetGatewayId: str, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_network_acl(
        self, DryRun: bool = None
    ) -> ec2_service_resource_scope.NetworkAcl:
        pass

    # pylint: disable=arguments-differ
    def create_route_table(
        self, DryRun: bool = None
    ) -> ec2_service_resource_scope.RouteTable:
        pass

    # pylint: disable=arguments-differ
    def create_security_group(
        self, Description: str, GroupName: str, DryRun: bool = None
    ) -> ec2_service_resource_scope.SecurityGroup:
        pass

    # pylint: disable=arguments-differ
    def create_subnet(
        self,
        CidrBlock: str,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        DryRun: bool = None,
    ) -> ec2_service_resource_scope.Subnet:
        pass

    # pylint: disable=arguments-differ
    def create_tags(
        self, Tags: List[Any], DryRun: bool = None
    ) -> List[ec2_service_resource_scope.Tag]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_attribute(self, Attribute: str, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_classic_link_instance(
        self, InstanceId: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_internet_gateway(
        self, InternetGatewayId: str, DryRun: bool = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def disable_classic_link(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_classic_link(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def modify_attribute(
        self,
        EnableDnsHostnames: Dict[str, Any] = None,
        EnableDnsSupport: Dict[str, Any] = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def request_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
    ) -> ec2_service_resource_scope.VpcPeeringConnection:
        pass

    # pylint: disable=arguments-differ
    def wait_until_available(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass


class VpcPeeringConnection(Boto3ServiceResource):
    accepter_vpc_info: Dict
    expiration_time: datetime
    requester_vpc_info: Dict
    status: Dict
    tags: List
    vpc_peering_connection_id: str
    id: str

    # pylint: disable=arguments-differ
    def accept(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def reject(self, DryRun: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def wait_until_exists(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> None:
        pass


class VpcAddress(Boto3ServiceResource):
    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List
    public_ipv4_pool: str
    allocation_id: str

    # pylint: disable=arguments-differ
    def associate(
        self,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ
    def release(self, PublicIp: str = None, DryRun: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def reload(self) -> None:
        pass


class classic_addresses(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.ClassicAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        PublicIps: List[Any] = None,
        AllocationIds: List[Any] = None,
        DryRun: bool = None,
    ) -> List[ec2_service_resource_scope.ClassicAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.ClassicAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.ClassicAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class dhcp_options_sets(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.DhcpOptions]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        DhcpOptionsIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.DhcpOptions]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.DhcpOptions]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.DhcpOptions]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class images(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Image]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        ExecutableUsers: List[Any] = None,
        Filters: List[Any] = None,
        ImageIds: List[Any] = None,
        Owners: List[Any] = None,
        DryRun: bool = None,
    ) -> List[ec2_service_resource_scope.Image]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Image]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Image]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class instances(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Instance]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def create_tags(cls, Tags: List[Any], DryRun: bool = None) -> None:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[ec2_service_resource_scope.Instance]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Instance]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def monitor(cls, DryRun: bool = None) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Instance]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def reboot(cls, DryRun: bool = None) -> None:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def start(cls, AdditionalInfo: str = None, DryRun: bool = None) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def stop(
        cls, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def terminate(cls, DryRun: bool = None) -> Dict[str, Any]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def unmonitor(cls, DryRun: bool = None) -> Dict[str, Any]:
        pass


class internet_gateways(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.InternetGateway]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.InternetGateway]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.InternetGateway]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.InternetGateway]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class key_pairs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.KeyPairInfo]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls, Filters: List[Any] = None, KeyNames: List[Any] = None, DryRun: bool = None
    ) -> List[ec2_service_resource_scope.KeyPairInfo]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.KeyPairInfo]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.KeyPairInfo]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class network_acls(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.NetworkAcl]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NetworkAclIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.NetworkAcl]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.NetworkAcl]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.NetworkAcl]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class network_interfaces(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.NetworkInterface]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.NetworkInterface]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.NetworkInterface]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.NetworkInterface]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class placement_groups(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.PlacementGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        GroupNames: List[Any] = None,
    ) -> List[ec2_service_resource_scope.PlacementGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.PlacementGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.PlacementGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class route_tables(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.RouteTable]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        RouteTableIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.RouteTable]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.RouteTable]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.RouteTable]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class security_groups(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.SecurityGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        GroupIds: List[Any] = None,
        GroupNames: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.SecurityGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.SecurityGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.SecurityGroup]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class snapshots(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Snapshot]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[Any] = None,
        RestorableByUserIds: List[Any] = None,
        SnapshotIds: List[Any] = None,
        DryRun: bool = None,
    ) -> List[ec2_service_resource_scope.Snapshot]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Snapshot]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Snapshot]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class subnets(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Subnet]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        SubnetIds: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.Subnet]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Subnet]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Subnet]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class volumes(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Volume]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> List[ec2_service_resource_scope.Volume]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Volume]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Volume]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class vpc_addresses(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.VpcAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        PublicIps: List[Any] = None,
        AllocationIds: List[Any] = None,
        DryRun: bool = None,
    ) -> List[ec2_service_resource_scope.VpcAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.VpcAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcAddress]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class vpc_peering_connections(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class vpcs(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.Vpc]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        Filters: List[Any] = None,
        VpcIds: List[Any] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.Vpc]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(cls, count: int = None) -> List[ec2_service_resource_scope.Vpc]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(cls, count: int = None) -> List[ec2_service_resource_scope.Vpc]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class accepted_vpc_peering_connections(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass


class requested_vpc_peering_connections(ResourceCollection):
    @classmethod
    # pylint: disable=arguments-differ
    def all(cls) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def filter(
        cls,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def limit(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def page_size(
        cls, count: int = None
    ) -> List[ec2_service_resource_scope.VpcPeeringConnection]:
        pass

    @classmethod
    # pylint: disable=arguments-differ
    def pages(cls) -> List[ServiceResource]:
        pass
