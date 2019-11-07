from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from boto3.resources.base import ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(base.ServiceResource):
    classic_addresses: 'classic_addresses'
    dhcp_options_sets: 'dhcp_options_sets'
    images: 'images'
    instances: 'instances'
    internet_gateways: 'internet_gateways'
    key_pairs: 'key_pairs'
    network_acls: 'network_acls'
    network_interfaces: 'network_interfaces'
    placement_groups: 'placement_groups'
    route_tables: 'route_tables'
    security_groups: 'security_groups'
    snapshots: 'snapshots'
    subnets: 'subnets'
    volumes: 'volumes'
    vpc_addresses: 'vpc_addresses'
    vpc_peering_connections: 'vpc_peering_connections'
    vpcs: 'vpcs'

    def ClassicAddress(
        self,
        public_ip: Optional[str] = None,
    ) -> 'ClassicAddress':
        pass


    def DhcpOptions(
        self,
        id: Optional[str] = None,
    ) -> 'DhcpOptions':
        pass


    def Image(
        self,
        id: Optional[str] = None,
    ) -> 'Image':
        pass


    def Instance(
        self,
        id: Optional[str] = None,
    ) -> 'Instance':
        pass


    def InternetGateway(
        self,
        id: Optional[str] = None,
    ) -> 'InternetGateway':
        pass


    def KeyPair(
        self,
        name: Optional[str] = None,
    ) -> 'KeyPairInfo':
        pass


    def NetworkAcl(
        self,
        id: Optional[str] = None,
    ) -> 'NetworkAcl':
        pass


    def NetworkInterface(
        self,
        id: Optional[str] = None,
    ) -> 'NetworkInterface':
        pass


    def NetworkInterfaceAssociation(
        self,
        id: Optional[str] = None,
    ) -> 'NetworkInterfaceAssociation':
        pass


    def PlacementGroup(
        self,
        name: Optional[str] = None,
    ) -> 'PlacementGroup':
        pass


    def Route(
        self,
        route_table_id: Optional[str] = None,
        destination_cidr_block: Optional[str] = None,
    ) -> 'Route':
        pass


    def RouteTable(
        self,
        id: Optional[str] = None,
    ) -> 'RouteTable':
        pass


    def RouteTableAssociation(
        self,
        id: Optional[str] = None,
    ) -> 'RouteTableAssociation':
        pass


    def SecurityGroup(
        self,
        id: Optional[str] = None,
    ) -> 'SecurityGroup':
        pass


    def Snapshot(
        self,
        id: Optional[str] = None,
    ) -> 'Snapshot':
        pass


    def Subnet(
        self,
        id: Optional[str] = None,
    ) -> 'Subnet':
        pass


    def Tag(
        self,
        resource_id: Optional[str] = None,
        key: Optional[str] = None,
        value: Optional[str] = None,
    ) -> 'Tag':
        pass


    def Volume(
        self,
        id: Optional[str] = None,
    ) -> 'Volume':
        pass


    def Vpc(
        self,
        id: Optional[str] = None,
    ) -> 'Vpc':
        pass


    def VpcAddress(
        self,
        allocation_id: Optional[str] = None,
    ) -> 'VpcAddress':
        pass


    def VpcPeeringConnection(
        self,
        id: Optional[str] = None,
    ) -> 'VpcPeeringConnection':
        pass


    def create_dhcp_options(
        self,
        DhcpConfigurations: List,
        DryRun: Optional[bool] = None,
    ) -> 'DhcpOptions':
        pass


    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: Optional[List] = None,
        ImageId: Optional[str] = None,
        InstanceType: Optional[str] = None,
        Ipv6AddressCount: Optional[int] = None,
        Ipv6Addresses: Optional[List] = None,
        KernelId: Optional[str] = None,
        KeyName: Optional[str] = None,
        Monitoring: Optional[Dict] = None,
        Placement: Optional[Dict] = None,
        RamdiskId: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        SecurityGroups: Optional[List] = None,
        SubnetId: Optional[str] = None,
        UserData: Optional[str] = None,
        AdditionalInfo: Optional[str] = None,
        ClientToken: Optional[str] = None,
        DisableApiTermination: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        EbsOptimized: Optional[bool] = None,
        IamInstanceProfile: Optional[Dict] = None,
        InstanceInitiatedShutdownBehavior: Optional[str] = None,
        NetworkInterfaces: Optional[List] = None,
        PrivateIpAddress: Optional[str] = None,
        ElasticGpuSpecification: Optional[List] = None,
        ElasticInferenceAccelerators: Optional[List] = None,
        TagSpecifications: Optional[List] = None,
        LaunchTemplate: Optional[Dict] = None,
        InstanceMarketOptions: Optional[Dict] = None,
        CreditSpecification: Optional[Dict] = None,
        CpuOptions: Optional[Dict] = None,
        CapacityReservationSpecification: Optional[Dict] = None,
        HibernationOptions: Optional[Dict] = None,
        LicenseSpecifications: Optional[List] = None,
    ) -> List['Instance']:
        pass


    def create_internet_gateway(
        self,
        DryRun: Optional[bool] = None,
    ) -> 'InternetGateway':
        pass


    def create_key_pair(
        self,
        KeyName: str,
        DryRun: Optional[bool] = None,
    ) -> 'KeyPair':
        pass


    def create_network_acl(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> 'NetworkAcl':
        pass


    def create_network_interface(
        self,
        SubnetId: str,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        Groups: Optional[List] = None,
        Ipv6AddressCount: Optional[int] = None,
        Ipv6Addresses: Optional[List] = None,
        PrivateIpAddress: Optional[str] = None,
        PrivateIpAddresses: Optional[List] = None,
        SecondaryPrivateIpAddressCount: Optional[int] = None,
        InterfaceType: Optional[str] = None,
    ) -> 'NetworkInterface':
        pass


    def create_placement_group(
        self,
        DryRun: Optional[bool] = None,
        GroupName: Optional[str] = None,
        Strategy: Optional[str] = None,
        PartitionCount: Optional[int] = None,
    ) -> 'PlacementGroup':
        pass


    def create_route_table(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> 'RouteTable':
        pass


    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        VpcId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> 'SecurityGroup':
        pass


    def create_snapshot(
        self,
        VolumeId: str,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> 'Snapshot':
        pass


    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: Optional[str] = None,
        AvailabilityZoneId: Optional[str] = None,
        Ipv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> 'Subnet':
        pass


    def create_tags(
        self,
        Resources: List[str],
        Tags: List,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_volume(
        self,
        AvailabilityZone: str,
        Encrypted: Optional[bool] = None,
        Iops: Optional[int] = None,
        KmsKeyId: Optional[str] = None,
        Size: Optional[int] = None,
        SnapshotId: Optional[str] = None,
        VolumeType: Optional[str] = None,
        DryRun: Optional[bool] = None,
        TagSpecifications: Optional[List] = None,
    ) -> 'Volume':
        pass


    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        InstanceTenancy: Optional[str] = None,
    ) -> 'Vpc':
        pass


    def create_vpc_peering_connection(
        self,
        DryRun: Optional[bool] = None,
        PeerOwnerId: Optional[str] = None,
        PeerVpcId: Optional[str] = None,
        VpcId: Optional[str] = None,
        PeerRegion: Optional[str] = None,
    ) -> 'VpcPeeringConnection':
        pass


    def disassociate_route_table(
        self,
        AssociationId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def import_key_pair(
        self,
        KeyName: str,
        PublicKeyMaterial: bytes,
        DryRun: Optional[bool] = None,
    ) -> 'KeyPairInfo':
        pass


    def register_image(
        self,
        Name: str,
        ImageLocation: Optional[str] = None,
        Architecture: Optional[str] = None,
        BlockDeviceMappings: Optional[List] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EnaSupport: Optional[bool] = None,
        KernelId: Optional[str] = None,
        BillingProducts: Optional[List] = None,
        RamdiskId: Optional[str] = None,
        RootDeviceName: Optional[str] = None,
        SriovNetSupport: Optional[str] = None,
        VirtualizationType: Optional[str] = None,
    ) -> 'Image':
        pass



class ClassicAddress(base.ServiceResource):
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

    def associate(
        self,
        AllocationId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        AllowReassociation: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceId: Optional[str] = None,
        PrivateIpAddress: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate(
        self,
        AssociationId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def release(
        self,
        AllocationId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class DhcpOptions(base.ServiceResource):
    dhcp_configurations: List
    dhcp_options_id: str
    owner_id: str
    tags: List
    id: str

    def associate_with_vpc(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Image(base.ServiceResource):
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

    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def deregister(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        Attribute: Optional[str] = None,
        Description: Optional[Dict] = None,
        LaunchPermission: Optional[Dict] = None,
        OperationType: Optional[str] = None,
        ProductCodes: Optional[List] = None,
        UserGroups: Optional[List] = None,
        UserIds: Optional[List] = None,
        Value: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def reset_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def wait_until_exists(
        self,
        ExecutableUsers: Optional[List] = None,
        Filters: Optional[List] = None,
        Owners: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ):
        pass



class Instance(base.ServiceResource):
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
    volumes: 'volumes'
    vpc_addresses: 'vpc_addresses'

    def attach_classic_link_vpc(
        self,
        Groups: List,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def attach_volume(
        self,
        Device: str,
        VolumeId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def console_output(
        self,
        DryRun: Optional[bool] = None,
        Latest: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_image(
        self,
        Name: str,
        BlockDeviceMappings: Optional[List] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        NoReboot: Optional[bool] = None,
    ) -> 'Image':
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete_tags(
        self,
        DryRun: Optional[bool] = None,
        Tags: Optional[List] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_classic_link_vpc(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_volume(
        self,
        VolumeId: str,
        Device: Optional[str] = None,
        Force: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        SourceDestCheck: Optional[Dict] = None,
        Attribute: Optional[str] = None,
        BlockDeviceMappings: Optional[List] = None,
        DisableApiTermination: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
        EbsOptimized: Optional[Dict] = None,
        EnaSupport: Optional[Dict] = None,
        Groups: Optional[List] = None,
        InstanceInitiatedShutdownBehavior: Optional[Dict] = None,
        InstanceType: Optional[Dict] = None,
        Kernel: Optional[Dict] = None,
        Ramdisk: Optional[Dict] = None,
        SriovNetSupport: Optional[Dict] = None,
        UserData: Optional[Dict] = None,
        Value: Optional[str] = None,
    ):
        pass


    def monitor(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def password_data(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reboot(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def report_status(
        self,
        ReasonCodes: List,
        Status: str,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EndTime: Optional[datetime] = None,
        StartTime: Optional[datetime] = None,
    ):
        pass


    def reset_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reset_kernel(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reset_ramdisk(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reset_source_dest_check(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def start(
        self,
        AdditionalInfo: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def stop(
        self,
        Hibernate: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def terminate(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def unmonitor(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def wait_until_exists(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ):
        pass


    def wait_until_running(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ):
        pass


    def wait_until_stopped(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ):
        pass


    def wait_until_terminated(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ):
        pass



class InternetGateway(base.ServiceResource):
    attachments: List
    internet_gateway_id: str
    owner_id: str
    tags: List
    id: str

    def attach_to_vpc(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def detach_from_vpc(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class KeyPair(base.ServiceResource):
    key_fingerprint: str
    key_material: str
    key_name: str
    name: str

    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass



class KeyPairInfo(base.ServiceResource):
    key_fingerprint: str
    key_name: str
    name: str

    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class NetworkAcl(base.ServiceResource):
    associations: List
    entries: List
    is_default: bool
    network_acl_id: str
    tags: List
    vpc_id: str
    owner_id: str
    id: str

    def create_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: str,
        RuleNumber: int,
        CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
        IcmpTypeCode: Optional[Dict] = None,
        Ipv6CidrBlock: Optional[str] = None,
        PortRange: Optional[Dict] = None,
    ):
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_entry(
        self,
        Egress: bool,
        RuleNumber: int,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def replace_association(
        self,
        AssociationId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def replace_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: str,
        RuleNumber: int,
        CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
        IcmpTypeCode: Optional[Dict] = None,
        Ipv6CidrBlock: Optional[str] = None,
        PortRange: Optional[Dict] = None,
    ):
        pass



class NetworkInterface(base.ServiceResource):
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

    def assign_private_ip_addresses(
        self,
        AllowReassignment: Optional[bool] = None,
        PrivateIpAddresses: Optional[List] = None,
        SecondaryPrivateIpAddressCount: Optional[int] = None,
    ) -> Dict:
        pass


    def attach(
        self,
        DeviceIndex: int,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach(
        self,
        DryRun: Optional[bool] = None,
        Force: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        Attachment: Optional[Dict] = None,
        Description: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
        Groups: Optional[List] = None,
        SourceDestCheck: Optional[Dict] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def reset_attribute(
        self,
        DryRun: Optional[bool] = None,
        SourceDestCheck: Optional[str] = None,
    ):
        pass


    def unassign_private_ip_addresses(
        self,
        PrivateIpAddresses: List,
    ):
        pass



class NetworkInterfaceAssociation(base.ServiceResource):
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str

    def delete(
        self,
        PublicIp: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class PlacementGroup(base.ServiceResource):
    group_name: str
    state: str
    strategy: str
    partition_count: int
    name: str
    instances: 'instances'

    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Route(base.ServiceResource):
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

    def delete(
        self,
        DestinationIpv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def replace(
        self,
        DestinationIpv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EgressOnlyInternetGatewayId: Optional[str] = None,
        GatewayId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        NatGatewayId: Optional[str] = None,
        TransitGatewayId: Optional[str] = None,
        NetworkInterfaceId: Optional[str] = None,
        VpcPeeringConnectionId: Optional[str] = None,
    ):
        pass



class RouteTable(base.ServiceResource):
    associations_attribute: List
    propagating_vgws: List
    route_table_id: str
    routes_attribute: List
    tags: List
    vpc_id: str
    owner_id: str
    id: str

    def associate_with_subnet(
        self,
        SubnetId: str,
        DryRun: Optional[bool] = None,
    ) -> 'RouteTableAssociation':
        pass


    def create_route(
        self,
        DestinationCidrBlock: Optional[str] = None,
        DestinationIpv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EgressOnlyInternetGatewayId: Optional[str] = None,
        GatewayId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        NatGatewayId: Optional[str] = None,
        TransitGatewayId: Optional[str] = None,
        NetworkInterfaceId: Optional[str] = None,
        VpcPeeringConnectionId: Optional[str] = None,
    ) -> 'Route':
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class RouteTableAssociation(base.ServiceResource):
    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    id: str

    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def replace_subnet(
        self,
        RouteTableId: str,
        DryRun: Optional[bool] = None,
    ) -> 'RouteTableAssociation':
        pass



class SecurityGroup(base.ServiceResource):
    description: str
    group_name: str
    ip_permissions: List
    owner_id: str
    group_id: str
    ip_permissions_egress: List
    tags: List
    vpc_id: str
    id: str

    def authorize_egress(
        self,
        DryRun: Optional[bool] = None,
        IpPermissions: Optional[List] = None,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        IpProtocol: Optional[str] = None,
        ToPort: Optional[int] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
    ):
        pass


    def authorize_ingress(
        self,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        GroupName: Optional[str] = None,
        IpPermissions: Optional[List] = None,
        IpProtocol: Optional[str] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
        ToPort: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        GroupName: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def revoke_egress(
        self,
        DryRun: Optional[bool] = None,
        IpPermissions: Optional[List] = None,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        IpProtocol: Optional[str] = None,
        ToPort: Optional[int] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
    ):
        pass


    def revoke_ingress(
        self,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        GroupName: Optional[str] = None,
        IpPermissions: Optional[List] = None,
        IpProtocol: Optional[str] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
        ToPort: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ):
        pass



class Snapshot(base.ServiceResource):
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

    def copy(
        self,
        SourceRegion: str,
        Description: Optional[str] = None,
        DestinationRegion: Optional[str] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        PresignedUrl: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        Attribute: Optional[str] = None,
        CreateVolumePermission: Optional[Dict] = None,
        GroupNames: Optional[List] = None,
        OperationType: Optional[str] = None,
        UserIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def reset_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def wait_until_completed(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OwnerIds: Optional[List] = None,
        RestorableByUserIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ):
        pass



class Subnet(base.ServiceResource):
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
    instances: 'instances'
    network_interfaces: 'network_interfaces'

    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: Optional[List] = None,
        ImageId: Optional[str] = None,
        InstanceType: Optional[str] = None,
        Ipv6AddressCount: Optional[int] = None,
        Ipv6Addresses: Optional[List] = None,
        KernelId: Optional[str] = None,
        KeyName: Optional[str] = None,
        Monitoring: Optional[Dict] = None,
        Placement: Optional[Dict] = None,
        RamdiskId: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        SecurityGroups: Optional[List] = None,
        UserData: Optional[str] = None,
        AdditionalInfo: Optional[str] = None,
        ClientToken: Optional[str] = None,
        DisableApiTermination: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        EbsOptimized: Optional[bool] = None,
        IamInstanceProfile: Optional[Dict] = None,
        InstanceInitiatedShutdownBehavior: Optional[str] = None,
        NetworkInterfaces: Optional[List] = None,
        PrivateIpAddress: Optional[str] = None,
        ElasticGpuSpecification: Optional[List] = None,
        ElasticInferenceAccelerators: Optional[List] = None,
        TagSpecifications: Optional[List] = None,
        LaunchTemplate: Optional[Dict] = None,
        InstanceMarketOptions: Optional[Dict] = None,
        CreditSpecification: Optional[Dict] = None,
        CpuOptions: Optional[Dict] = None,
        CapacityReservationSpecification: Optional[Dict] = None,
        HibernationOptions: Optional[Dict] = None,
        LicenseSpecifications: Optional[List] = None,
    ) -> List['Instance']:
        pass


    def create_network_interface(
        self,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        Groups: Optional[List] = None,
        Ipv6AddressCount: Optional[int] = None,
        Ipv6Addresses: Optional[List] = None,
        PrivateIpAddress: Optional[str] = None,
        PrivateIpAddresses: Optional[List] = None,
        SecondaryPrivateIpAddressCount: Optional[int] = None,
        InterfaceType: Optional[str] = None,
    ) -> 'NetworkInterface':
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Tag(base.ServiceResource):
    resource_type: str
    resource_id: str
    key: str
    value: str

    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Volume(base.ServiceResource):
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
    snapshots: 'snapshots'

    def attach_to_instance(
        self,
        Device: str,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_snapshot(
        self,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> 'Snapshot':
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_status(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_from_instance(
        self,
        Device: Optional[str] = None,
        Force: Optional[bool] = None,
        InstanceId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def enable_io(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        AutoEnableIO: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class Vpc(base.ServiceResource):
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
    accepted_vpc_peering_connections: 'accepted_vpc_peering_connections'
    instances: 'instances'
    internet_gateways: 'internet_gateways'
    network_acls: 'network_acls'
    network_interfaces: 'network_interfaces'
    requested_vpc_peering_connections: 'requested_vpc_peering_connections'
    route_tables: 'route_tables'
    security_groups: 'security_groups'
    subnets: 'subnets'

    def associate_dhcp_options(
        self,
        DhcpOptionsId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def attach_classic_link_instance(
        self,
        Groups: List,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def attach_internet_gateway(
        self,
        InternetGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_network_acl(
        self,
        DryRun: Optional[bool] = None,
    ) -> 'NetworkAcl':
        pass


    def create_route_table(
        self,
        DryRun: Optional[bool] = None,
    ) -> 'RouteTable':
        pass


    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        DryRun: Optional[bool] = None,
    ) -> 'SecurityGroup':
        pass


    def create_subnet(
        self,
        CidrBlock: str,
        AvailabilityZone: Optional[str] = None,
        AvailabilityZoneId: Optional[str] = None,
        Ipv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> 'Subnet':
        pass


    def create_tags(
        self,
        Tags: List,
        DryRun: Optional[bool] = None,
    ) -> List['Tag']:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_attribute(
        self,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_classic_link_instance(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_internet_gateway(
        self,
        InternetGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def disable_classic_link(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def enable_classic_link(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def modify_attribute(
        self,
        EnableDnsHostnames: Optional[Dict] = None,
        EnableDnsSupport: Optional[Dict] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass


    def request_vpc_peering_connection(
        self,
        DryRun: Optional[bool] = None,
        PeerOwnerId: Optional[str] = None,
        PeerVpcId: Optional[str] = None,
        PeerRegion: Optional[str] = None,
    ) -> 'VpcPeeringConnection':
        pass


    def wait_until_available(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ):
        pass


    def wait_until_exists(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ):
        pass



class VpcPeeringConnection(base.ServiceResource):
    accepter_vpc_info: Dict
    expiration_time: datetime
    requester_vpc_info: Dict
    status: Dict
    tags: List
    vpc_peering_connection_id: str
    id: str

    def accept(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def reject(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reload(
        self,
    ):
        pass


    def wait_until_exists(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ):
        pass



class VpcAddress(base.ServiceResource):
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

    def associate(
        self,
        InstanceId: Optional[str] = None,
        PublicIp: Optional[str] = None,
        AllowReassociation: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceId: Optional[str] = None,
        PrivateIpAddress: Optional[str] = None,
    ) -> Dict:
        pass


    def get_available_subresources(
        self,
    ) -> List[str]:
        pass


    def load(
        self,
    ):
        pass


    def release(
        self,
        PublicIp: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reload(
        self,
    ):
        pass



class classic_addresses(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['ClassicAddress']:
        pass


    @classmethod
    def filter(
        cls,
        PublicIps: Optional[List] = None,
        AllocationIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> List['ClassicAddress']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['ClassicAddress']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['ClassicAddress']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class dhcp_options_sets(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['DhcpOptions']:
        pass


    @classmethod
    def filter(
        cls,
        DhcpOptionsIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['DhcpOptions']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['DhcpOptions']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['DhcpOptions']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class images(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Image']:
        pass


    @classmethod
    def filter(
        cls,
        ExecutableUsers: Optional[List] = None,
        Filters: Optional[List] = None,
        ImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> List['Image']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Image']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Image']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class instances(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Instance']:
        pass


    @classmethod
    def create_tags(
        cls,
        Tags: List,
        DryRun: Optional[bool] = None,
    ):
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> List['Instance']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Instance']:
        pass


    @classmethod
    def monitor(
        cls,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Instance']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass


    @classmethod
    def reboot(
        cls,
        DryRun: Optional[bool] = None,
    ):
        pass


    @classmethod
    def start(
        cls,
        AdditionalInfo: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    @classmethod
    def stop(
        cls,
        Hibernate: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    @classmethod
    def terminate(
        cls,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    @classmethod
    def unmonitor(
        cls,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass



class internet_gateways(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['InternetGateway']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InternetGatewayIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['InternetGateway']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['InternetGateway']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['InternetGateway']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class key_pairs(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['KeyPairInfo']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        KeyNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> List['KeyPairInfo']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['KeyPairInfo']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['KeyPairInfo']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class network_acls(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['NetworkAcl']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkAclIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['NetworkAcl']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['NetworkAcl']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['NetworkAcl']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class network_interfaces(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['NetworkInterface']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['NetworkInterface']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['NetworkInterface']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['NetworkInterface']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class placement_groups(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['PlacementGroup']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        GroupNames: Optional[List] = None,
    ) -> List['PlacementGroup']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['PlacementGroup']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['PlacementGroup']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class route_tables(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['RouteTable']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        RouteTableIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['RouteTable']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['RouteTable']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['RouteTable']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class security_groups(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['SecurityGroup']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        GroupIds: Optional[List] = None,
        GroupNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['SecurityGroup']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['SecurityGroup']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['SecurityGroup']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class snapshots(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Snapshot']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OwnerIds: Optional[List] = None,
        RestorableByUserIds: Optional[List] = None,
        SnapshotIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> List['Snapshot']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Snapshot']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Snapshot']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class subnets(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Subnet']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['Subnet']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Subnet']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Subnet']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class volumes(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Volume']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> List['Volume']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Volume']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Volume']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class vpc_addresses(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['VpcAddress']:
        pass


    @classmethod
    def filter(
        cls,
        PublicIps: Optional[List] = None,
        AllocationIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> List['VpcAddress']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['VpcAddress']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['VpcAddress']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class vpc_peering_connections(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['VpcPeeringConnection']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['VpcPeeringConnection']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['VpcPeeringConnection']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['VpcPeeringConnection']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass



class vpcs(ResourceCollection):
    @classmethod
    def all(
        cls,
    ) -> List['Vpc']:
        pass


    @classmethod
    def filter(
        cls,
        Filters: Optional[List] = None,
        VpcIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> List['Vpc']:
        pass


    @classmethod
    def iterator(
        cls,
    ) -> ResourceCollection:
        pass


    @classmethod
    def limit(
        cls,
        count: Optional[int] = None,
    ) -> List['Vpc']:
        pass


    @classmethod
    def page_size(
        cls,
        count: Optional[int] = None,
    ) -> List['Vpc']:
        pass


    @classmethod
    def pages(
        cls,
    ) -> List[base.ServiceResource]:
        pass

