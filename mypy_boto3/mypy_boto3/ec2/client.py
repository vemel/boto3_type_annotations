from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List,
        DryRun: Optional[bool] = None,
        TargetConfigurations: Optional[List] = None,
    ) -> Dict:
        pass


    def accept_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def accept_vpc_endpoint_connections(
        self,
        ServiceId: str,
        VpcEndpointIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def accept_vpc_peering_connection(
        self,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionId: Optional[str] = None,
    ) -> Dict:
        pass


    def advertise_byoip_cidr(
        self,
        Cidr: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def allocate_address(
        self,
        Domain: Optional[str] = None,
        Address: Optional[str] = None,
        PublicIpv4Pool: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def allocate_hosts(
        self,
        AvailabilityZone: str,
        InstanceType: str,
        Quantity: int,
        AutoPlacement: Optional[str] = None,
        ClientToken: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        HostRecovery: Optional[str] = None,
    ) -> Dict:
        pass


    def apply_security_groups_to_client_vpn_target_network(
        self,
        ClientVpnEndpointId: str,
        VpcId: str,
        SecurityGroupIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def assign_ipv6_addresses(
        self,
        NetworkInterfaceId: str,
        Ipv6AddressCount: Optional[int] = None,
        Ipv6Addresses: Optional[List] = None,
    ) -> Dict:
        pass


    def assign_private_ip_addresses(
        self,
        NetworkInterfaceId: str,
        AllowReassignment: Optional[bool] = None,
        PrivateIpAddresses: Optional[List] = None,
        SecondaryPrivateIpAddressCount: Optional[int] = None,
    ) -> Dict:
        pass


    def associate_address(
        self,
        AllocationId: Optional[str] = None,
        InstanceId: Optional[str] = None,
        PublicIp: Optional[str] = None,
        AllowReassociation: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceId: Optional[str] = None,
        PrivateIpAddress: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_client_vpn_target_network(
        self,
        ClientVpnEndpointId: str,
        SubnetId: str,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_dhcp_options(
        self,
        DhcpOptionsId: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def associate_iam_instance_profile(
        self,
        IamInstanceProfile: Dict,
        InstanceId: str,
    ) -> Dict:
        pass


    def associate_route_table(
        self,
        RouteTableId: str,
        SubnetId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_subnet_cidr_block(
        self,
        Ipv6CidrBlock: str,
        SubnetId: str,
    ) -> Dict:
        pass


    def associate_transit_gateway_route_table(
        self,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def associate_vpc_cidr_block(
        self,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: Optional[bool] = None,
        CidrBlock: Optional[str] = None,
    ) -> Dict:
        pass


    def attach_classic_link_vpc(
        self,
        Groups: List,
        InstanceId: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def attach_internet_gateway(
        self,
        InternetGatewayId: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def attach_network_interface(
        self,
        DeviceIndex: int,
        InstanceId: str,
        NetworkInterfaceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def attach_volume(
        self,
        Device: str,
        InstanceId: str,
        VolumeId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def attach_vpn_gateway(
        self,
        VpcId: str,
        VpnGatewayId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def authorize_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: Optional[str] = None,
        AuthorizeAllGroups: Optional[bool] = None,
        Description: Optional[str] = None,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def authorize_security_group_egress(
        self,
        GroupId: str,
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


    def authorize_security_group_ingress(
        self,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        GroupId: Optional[str] = None,
        GroupName: Optional[str] = None,
        IpPermissions: Optional[List] = None,
        IpProtocol: Optional[str] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
        ToPort: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def bundle_instance(
        self,
        InstanceId: str,
        Storage: Dict,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_bundle_task(
        self,
        BundleId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def cancel_capacity_reservation(
        self,
        CapacityReservationId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def cancel_conversion_task(
        self,
        ConversionTaskId: str,
        DryRun: Optional[bool] = None,
        ReasonMessage: Optional[str] = None,
    ):
        pass


    def cancel_export_task(
        self,
        ExportTaskId: str,
    ):
        pass


    def cancel_import_task(
        self,
        CancelReason: Optional[str] = None,
        DryRun: Optional[bool] = None,
        ImportTaskId: Optional[str] = None,
    ) -> Dict:
        pass


    def cancel_reserved_instances_listing(
        self,
        ReservedInstancesListingId: str,
    ) -> Dict:
        pass


    def cancel_spot_fleet_requests(
        self,
        SpotFleetRequestIds: List,
        TerminateInstances: bool,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def cancel_spot_instance_requests(
        self,
        SpotInstanceRequestIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def confirm_product_instance(
        self,
        InstanceId: str,
        ProductCode: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def copy_fpga_image(
        self,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: Optional[bool] = None,
        Description: Optional[str] = None,
        Name: Optional[str] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def copy_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def copy_snapshot(
        self,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: Optional[str] = None,
        DestinationRegion: Optional[str] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        PresignedUrl: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_capacity_reservation(
        self,
        InstanceType: str,
        InstancePlatform: str,
        InstanceCount: int,
        ClientToken: Optional[str] = None,
        AvailabilityZone: Optional[str] = None,
        AvailabilityZoneId: Optional[str] = None,
        Tenancy: Optional[str] = None,
        EbsOptimized: Optional[bool] = None,
        EphemeralStorage: Optional[bool] = None,
        EndDate: Optional[datetime] = None,
        EndDateType: Optional[str] = None,
        InstanceMatchCriteria: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_client_vpn_endpoint(
        self,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: List,
        ConnectionLogOptions: Dict,
        DnsServers: Optional[List] = None,
        TransportProtocol: Optional[str] = None,
        Description: Optional[str] = None,
        SplitTunnel: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
    ) -> Dict:
        pass


    def create_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: Optional[str] = None,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_customer_gateway(
        self,
        BgpAsn: int,
        Type: str,
        PublicIp: Optional[str] = None,
        CertificateArn: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_default_subnet(
        self,
        AvailabilityZone: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_default_vpc(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_dhcp_options(
        self,
        DhcpConfigurations: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_egress_only_internet_gateway(
        self,
        VpcId: str,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_fleet(
        self,
        LaunchTemplateConfigs: List,
        TargetCapacitySpecification: Dict,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        SpotOptions: Optional[Dict] = None,
        OnDemandOptions: Optional[Dict] = None,
        ExcessCapacityTerminationPolicy: Optional[str] = None,
        TerminateInstancesWithExpiration: Optional[bool] = None,
        Type: Optional[str] = None,
        ValidFrom: Optional[datetime] = None,
        ValidUntil: Optional[datetime] = None,
        ReplaceUnhealthyInstances: Optional[bool] = None,
        TagSpecifications: Optional[List] = None,
    ) -> Dict:
        pass


    def create_flow_logs(
        self,
        ResourceIds: List,
        ResourceType: str,
        TrafficType: str,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        DeliverLogsPermissionArn: Optional[str] = None,
        LogGroupName: Optional[str] = None,
        LogDestinationType: Optional[str] = None,
        LogDestination: Optional[str] = None,
        LogFormat: Optional[str] = None,
    ) -> Dict:
        pass


    def create_fpga_image(
        self,
        InputStorageLocation: Dict,
        DryRun: Optional[bool] = None,
        LogsStorageLocation: Optional[Dict] = None,
        Description: Optional[str] = None,
        Name: Optional[str] = None,
        ClientToken: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
    ) -> Dict:
        pass


    def create_image(
        self,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: Optional[List] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        NoReboot: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_instance_export_task(
        self,
        InstanceId: str,
        Description: Optional[str] = None,
        ExportToS3Task: Optional[Dict] = None,
        TargetEnvironment: Optional[str] = None,
    ) -> Dict:
        pass


    def create_internet_gateway(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_key_pair(
        self,
        KeyName: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_launch_template(
        self,
        LaunchTemplateName: str,
        LaunchTemplateData: Dict,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        VersionDescription: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
    ) -> Dict:
        pass


    def create_launch_template_version(
        self,
        LaunchTemplateData: Dict,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
        SourceVersion: Optional[str] = None,
        VersionDescription: Optional[str] = None,
    ) -> Dict:
        pass


    def create_nat_gateway(
        self,
        AllocationId: str,
        SubnetId: str,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_network_acl(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
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
    ) -> Dict:
        pass


    def create_network_interface_permission(
        self,
        NetworkInterfaceId: str,
        Permission: str,
        AwsAccountId: Optional[str] = None,
        AwsService: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_placement_group(
        self,
        DryRun: Optional[bool] = None,
        GroupName: Optional[str] = None,
        Strategy: Optional[str] = None,
        PartitionCount: Optional[int] = None,
    ):
        pass


    def create_reserved_instances_listing(
        self,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: List,
        ReservedInstancesId: str,
    ) -> Dict:
        pass


    def create_route(
        self,
        RouteTableId: str,
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
    ) -> Dict:
        pass


    def create_route_table(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        VpcId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_snapshot(
        self,
        VolumeId: str,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_snapshots(
        self,
        InstanceSpecification: Dict,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
        CopyTagsFromSource: Optional[str] = None,
    ) -> Dict:
        pass


    def create_spot_datafeed_subscription(
        self,
        Bucket: str,
        DryRun: Optional[bool] = None,
        Prefix: Optional[str] = None,
    ) -> Dict:
        pass


    def create_subnet(
        self,
        CidrBlock: str,
        VpcId: str,
        AvailabilityZone: Optional[str] = None,
        AvailabilityZoneId: Optional[str] = None,
        Ipv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_tags(
        self,
        Resources: List,
        Tags: List,
        DryRun: Optional[bool] = None,
    ):
        pass


    def create_traffic_mirror_filter(
        self,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterId: str,
        TrafficDirection: str,
        RuleNumber: int,
        RuleAction: str,
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: Optional[Dict] = None,
        SourcePortRange: Optional[Dict] = None,
        Protocol: Optional[int] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_traffic_mirror_session(
        self,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: Optional[int] = None,
        VirtualNetworkId: Optional[int] = None,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_traffic_mirror_target(
        self,
        NetworkInterfaceId: Optional[str] = None,
        NetworkLoadBalancerArn: Optional[str] = None,
        Description: Optional[str] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_transit_gateway(
        self,
        Description: Optional[str] = None,
        Options: Optional[Dict] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: Optional[str] = None,
        Blackhole: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_transit_gateway_route_table(
        self,
        TransitGatewayId: str,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_transit_gateway_vpc_attachment(
        self,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: List,
        Options: Optional[Dict] = None,
        TagSpecifications: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
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
    ) -> Dict:
        pass


    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        InstanceTenancy: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpc_endpoint(
        self,
        VpcId: str,
        ServiceName: str,
        DryRun: Optional[bool] = None,
        VpcEndpointType: Optional[str] = None,
        PolicyDocument: Optional[str] = None,
        RouteTableIds: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        SecurityGroupIds: Optional[List] = None,
        ClientToken: Optional[str] = None,
        PrivateDnsEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationArn: str,
        ConnectionEvents: List,
        DryRun: Optional[bool] = None,
        ServiceId: Optional[str] = None,
        VpcEndpointId: Optional[str] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpc_endpoint_service_configuration(
        self,
        NetworkLoadBalancerArns: List,
        DryRun: Optional[bool] = None,
        AcceptanceRequired: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpc_peering_connection(
        self,
        DryRun: Optional[bool] = None,
        PeerOwnerId: Optional[str] = None,
        PeerVpcId: Optional[str] = None,
        VpcId: Optional[str] = None,
        PeerRegion: Optional[str] = None,
    ) -> Dict:
        pass


    def create_vpn_connection(
        self,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: Optional[str] = None,
        TransitGatewayId: Optional[str] = None,
        DryRun: Optional[bool] = None,
        Options: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_vpn_connection_route(
        self,
        DestinationCidrBlock: str,
        VpnConnectionId: str,
    ):
        pass


    def create_vpn_gateway(
        self,
        Type: str,
        AvailabilityZone: Optional[str] = None,
        AmazonSideAsn: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_client_vpn_endpoint(
        self,
        ClientVpnEndpointId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_customer_gateway(
        self,
        CustomerGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_dhcp_options(
        self,
        DhcpOptionsId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_egress_only_internet_gateway(
        self,
        EgressOnlyInternetGatewayId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_fleets(
        self,
        FleetIds: List,
        TerminateInstances: bool,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_flow_logs(
        self,
        FlowLogIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_fpga_image(
        self,
        FpgaImageId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_internet_gateway(
        self,
        InternetGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_key_pair(
        self,
        KeyName: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_launch_template(
        self,
        DryRun: Optional[bool] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_launch_template_versions(
        self,
        Versions: List,
        DryRun: Optional[bool] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_nat_gateway(
        self,
        NatGatewayId: str,
    ) -> Dict:
        pass


    def delete_network_acl(
        self,
        NetworkAclId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
        RuleNumber: int,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_network_interface(
        self,
        NetworkInterfaceId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_network_interface_permission(
        self,
        NetworkInterfacePermissionId: str,
        Force: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_placement_group(
        self,
        GroupName: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_queued_reserved_instances(
        self,
        ReservedInstancesIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: Optional[str] = None,
        DestinationIpv6CidrBlock: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_route_table(
        self,
        RouteTableId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_security_group(
        self,
        GroupId: Optional[str] = None,
        GroupName: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_snapshot(
        self,
        SnapshotId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_spot_datafeed_subscription(
        self,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_subnet(
        self,
        SubnetId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_tags(
        self,
        Resources: List,
        DryRun: Optional[bool] = None,
        Tags: Optional[List] = None,
    ):
        pass


    def delete_traffic_mirror_filter(
        self,
        TrafficMirrorFilterId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterRuleId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_traffic_mirror_session(
        self,
        TrafficMirrorSessionId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_traffic_mirror_target(
        self,
        TrafficMirrorTargetId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_transit_gateway(
        self,
        TransitGatewayId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_transit_gateway_route(
        self,
        TransitGatewayRouteTableId: str,
        DestinationCidrBlock: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_transit_gateway_route_table(
        self,
        TransitGatewayRouteTableId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_volume(
        self,
        VolumeId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_vpc(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_vpc_endpoint_connection_notifications(
        self,
        ConnectionNotificationIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_vpc_endpoint_service_configurations(
        self,
        ServiceIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_vpc_endpoints(
        self,
        VpcEndpointIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_vpc_peering_connection(
        self,
        VpcPeeringConnectionId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_vpn_connection(
        self,
        VpnConnectionId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def delete_vpn_connection_route(
        self,
        DestinationCidrBlock: str,
        VpnConnectionId: str,
    ):
        pass


    def delete_vpn_gateway(
        self,
        VpnGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def deprovision_byoip_cidr(
        self,
        Cidr: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def deregister_image(
        self,
        ImageId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def describe_account_attributes(
        self,
        AttributeNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_addresses(
        self,
        Filters: Optional[List] = None,
        PublicIps: Optional[List] = None,
        AllocationIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_aggregate_id_format(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_availability_zones(
        self,
        Filters: Optional[List] = None,
        ZoneNames: Optional[List] = None,
        ZoneIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_bundle_tasks(
        self,
        BundleIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_byoip_cidrs(
        self,
        MaxResults: int,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_capacity_reservations(
        self,
        CapacityReservationIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_classic_link_instances(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InstanceIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_client_vpn_authorization_rules(
        self,
        ClientVpnEndpointId: str,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_client_vpn_endpoints(
        self,
        ClientVpnEndpointIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_client_vpn_routes(
        self,
        ClientVpnEndpointId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_client_vpn_target_networks(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_conversion_tasks(
        self,
        ConversionTaskIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_customer_gateways(
        self,
        CustomerGatewayIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_dhcp_options(
        self,
        DhcpOptionsIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_egress_only_internet_gateways(
        self,
        DryRun: Optional[bool] = None,
        EgressOnlyInternetGatewayIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_elastic_gpus(
        self,
        ElasticGpuIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_export_image_tasks(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ExportImageTaskIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_export_tasks(
        self,
        ExportTaskIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_fleet_history(
        self,
        FleetId: str,
        StartTime: datetime,
        DryRun: Optional[bool] = None,
        EventType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fleet_instances(
        self,
        FleetId: str,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_fleets(
        self,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        FleetIds: Optional[List] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_flow_logs(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        FlowLogIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_fpga_image_attribute(
        self,
        FpgaImageId: str,
        Attribute: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_fpga_images(
        self,
        DryRun: Optional[bool] = None,
        FpgaImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_host_reservation_offerings(
        self,
        Filters: Optional[List] = None,
        MaxDuration: Optional[int] = None,
        MaxResults: Optional[int] = None,
        MinDuration: Optional[int] = None,
        NextToken: Optional[str] = None,
        OfferingId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_host_reservations(
        self,
        Filters: Optional[List] = None,
        HostReservationIdSet: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_hosts(
        self,
        Filters: Optional[List] = None,
        HostIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_iam_instance_profile_associations(
        self,
        AssociationIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_id_format(
        self,
        Resource: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_identity_id_format(
        self,
        PrincipalArn: str,
        Resource: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_image_attribute(
        self,
        Attribute: str,
        ImageId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_images(
        self,
        ExecutableUsers: Optional[List] = None,
        Filters: Optional[List] = None,
        ImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_import_image_tasks(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ImportTaskIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_import_snapshot_tasks(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ImportTaskIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instance_attribute(
        self,
        Attribute: str,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_instance_credit_specifications(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_instance_status(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
        IncludeAllInstances: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_instances(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_internet_gateways(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InternetGatewayIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_key_pairs(
        self,
        Filters: Optional[List] = None,
        KeyNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_launch_template_versions(
        self,
        DryRun: Optional[bool] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
        Versions: Optional[List] = None,
        MinVersion: Optional[str] = None,
        MaxVersion: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_launch_templates(
        self,
        DryRun: Optional[bool] = None,
        LaunchTemplateIds: Optional[List] = None,
        LaunchTemplateNames: Optional[List] = None,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_moving_addresses(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        PublicIps: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_nat_gateways(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NatGatewayIds: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_network_acls(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkAclIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attribute: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_network_interface_permissions(
        self,
        NetworkInterfacePermissionIds: Optional[List] = None,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_network_interfaces(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_placement_groups(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        GroupNames: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_prefix_lists(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        PrefixListIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_principal_id_format(
        self,
        DryRun: Optional[bool] = None,
        Resources: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_public_ipv4_pools(
        self,
        PoolIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_regions(
        self,
        Filters: Optional[List] = None,
        RegionNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
        AllRegions: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_reserved_instances(
        self,
        Filters: Optional[List] = None,
        OfferingClass: Optional[str] = None,
        ReservedInstancesIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        OfferingType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_instances_listings(
        self,
        Filters: Optional[List] = None,
        ReservedInstancesId: Optional[str] = None,
        ReservedInstancesListingId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_instances_modifications(
        self,
        Filters: Optional[List] = None,
        ReservedInstancesModificationIds: Optional[List] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_reserved_instances_offerings(
        self,
        AvailabilityZone: Optional[str] = None,
        Filters: Optional[List] = None,
        IncludeMarketplace: Optional[bool] = None,
        InstanceType: Optional[str] = None,
        MaxDuration: Optional[int] = None,
        MaxInstanceCount: Optional[int] = None,
        MinDuration: Optional[int] = None,
        OfferingClass: Optional[str] = None,
        ProductDescription: Optional[str] = None,
        ReservedInstancesOfferingIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InstanceTenancy: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OfferingType: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_route_tables(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        RouteTableIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_scheduled_instance_availability(
        self,
        FirstSlotStartTimeRange: Dict,
        Recurrence: Dict,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        MaxSlotDurationInHours: Optional[int] = None,
        MinSlotDurationInHours: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_scheduled_instances(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        ScheduledInstanceIds: Optional[List] = None,
        SlotStartTimeRange: Optional[Dict] = None,
    ) -> Dict:
        pass


    def describe_security_group_references(
        self,
        GroupId: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_security_groups(
        self,
        Filters: Optional[List] = None,
        GroupIds: Optional[List] = None,
        GroupNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_snapshot_attribute(
        self,
        Attribute: str,
        SnapshotId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_snapshots(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        OwnerIds: Optional[List] = None,
        RestorableByUserIds: Optional[List] = None,
        SnapshotIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_spot_datafeed_subscription(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_spot_fleet_instances(
        self,
        SpotFleetRequestId: str,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_spot_fleet_request_history(
        self,
        SpotFleetRequestId: str,
        StartTime: datetime,
        DryRun: Optional[bool] = None,
        EventType: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_spot_fleet_requests(
        self,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        SpotFleetRequestIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_spot_instance_requests(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        SpotInstanceRequestIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_spot_price_history(
        self,
        Filters: Optional[List] = None,
        AvailabilityZone: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EndTime: Optional[datetime] = None,
        InstanceTypes: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        ProductDescriptions: Optional[List] = None,
        StartTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def describe_stale_security_groups(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_subnets(
        self,
        Filters: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_traffic_mirror_filters(
        self,
        TrafficMirrorFilterIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_traffic_mirror_sessions(
        self,
        TrafficMirrorSessionIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_traffic_mirror_targets(
        self,
        TrafficMirrorTargetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_transit_gateway_attachments(
        self,
        TransitGatewayAttachmentIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_transit_gateway_route_tables(
        self,
        TransitGatewayRouteTableIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_transit_gateway_vpc_attachments(
        self,
        TransitGatewayAttachmentIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_transit_gateways(
        self,
        TransitGatewayIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_volume_attribute(
        self,
        Attribute: str,
        VolumeId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_volume_status(
        self,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_volumes(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_volumes_modifications(
        self,
        DryRun: Optional[bool] = None,
        VolumeIds: Optional[List] = None,
        Filters: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_vpc_attribute(
        self,
        Attribute: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_vpc_classic_link(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_vpc_classic_link_dns_support(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        VpcIds: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoint_connection_notifications(
        self,
        DryRun: Optional[bool] = None,
        ConnectionNotificationId: Optional[str] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoint_connections(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoint_service_configurations(
        self,
        DryRun: Optional[bool] = None,
        ServiceIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoint_services(
        self,
        DryRun: Optional[bool] = None,
        ServiceNames: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_endpoints(
        self,
        DryRun: Optional[bool] = None,
        VpcEndpointIds: Optional[List] = None,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_vpc_peering_connections(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionIds: Optional[List] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_vpcs(
        self,
        Filters: Optional[List] = None,
        VpcIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_vpn_connections(
        self,
        Filters: Optional[List] = None,
        VpnConnectionIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_vpn_gateways(
        self,
        Filters: Optional[List] = None,
        VpnGatewayIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_classic_link_vpc(
        self,
        InstanceId: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_internet_gateway(
        self,
        InternetGatewayId: str,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def detach_network_interface(
        self,
        AttachmentId: str,
        DryRun: Optional[bool] = None,
        Force: Optional[bool] = None,
    ):
        pass


    def detach_volume(
        self,
        VolumeId: str,
        Device: Optional[str] = None,
        Force: Optional[bool] = None,
        InstanceId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def detach_vpn_gateway(
        self,
        VpcId: str,
        VpnGatewayId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def disable_ebs_encryption_by_default(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def disable_transit_gateway_route_table_propagation(
        self,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def disable_vgw_route_propagation(
        self,
        GatewayId: str,
        RouteTableId: str,
    ):
        pass


    def disable_vpc_classic_link(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def disable_vpc_classic_link_dns_support(
        self,
        VpcId: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_address(
        self,
        AssociationId: Optional[str] = None,
        PublicIp: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def disassociate_client_vpn_target_network(
        self,
        ClientVpnEndpointId: str,
        AssociationId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def disassociate_iam_instance_profile(
        self,
        AssociationId: str,
    ) -> Dict:
        pass


    def disassociate_route_table(
        self,
        AssociationId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def disassociate_subnet_cidr_block(
        self,
        AssociationId: str,
    ) -> Dict:
        pass


    def disassociate_transit_gateway_route_table(
        self,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def disassociate_vpc_cidr_block(
        self,
        AssociationId: str,
    ) -> Dict:
        pass


    def enable_ebs_encryption_by_default(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def enable_transit_gateway_route_table_propagation(
        self,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def enable_vgw_route_propagation(
        self,
        GatewayId: str,
        RouteTableId: str,
    ):
        pass


    def enable_volume_io(
        self,
        VolumeId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def enable_vpc_classic_link(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def enable_vpc_classic_link_dns_support(
        self,
        VpcId: Optional[str] = None,
    ) -> Dict:
        pass


    def export_client_vpn_client_certificate_revocation_list(
        self,
        ClientVpnEndpointId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def export_client_vpn_client_configuration(
        self,
        ClientVpnEndpointId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def export_image(
        self,
        DiskImageFormat: str,
        ImageId: str,
        S3ExportLocation: Dict,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        RoleName: Optional[str] = None,
    ) -> Dict:
        pass


    def export_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
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


    def get_capacity_reservation_usage(
        self,
        CapacityReservationId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_console_output(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
        Latest: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_console_screenshot(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
        WakeUp: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_ebs_default_kms_key_id(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_ebs_encryption_by_default(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_host_reservation_purchase_preview(
        self,
        HostIdSet: List,
        OfferingId: str,
    ) -> Dict:
        pass


    def get_launch_template_data(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_password_data(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List,
        DryRun: Optional[bool] = None,
        TargetConfigurations: Optional[List] = None,
    ) -> Dict:
        pass


    def get_transit_gateway_attachment_propagations(
        self,
        TransitGatewayAttachmentId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_transit_gateway_route_table_associations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_transit_gateway_route_table_propagations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def import_client_vpn_client_certificate_revocation_list(
        self,
        ClientVpnEndpointId: str,
        CertificateRevocationList: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def import_image(
        self,
        Architecture: Optional[str] = None,
        ClientData: Optional[Dict] = None,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        DiskContainers: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Encrypted: Optional[bool] = None,
        Hypervisor: Optional[str] = None,
        KmsKeyId: Optional[str] = None,
        LicenseType: Optional[str] = None,
        Platform: Optional[str] = None,
        RoleName: Optional[str] = None,
    ) -> Dict:
        pass


    def import_instance(
        self,
        Platform: str,
        Description: Optional[str] = None,
        DiskImages: Optional[List] = None,
        DryRun: Optional[bool] = None,
        LaunchSpecification: Optional[Dict] = None,
    ) -> Dict:
        pass


    def import_key_pair(
        self,
        KeyName: str,
        PublicKeyMaterial: bytes,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def import_snapshot(
        self,
        ClientData: Optional[Dict] = None,
        ClientToken: Optional[str] = None,
        Description: Optional[str] = None,
        DiskContainer: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
        Encrypted: Optional[bool] = None,
        KmsKeyId: Optional[str] = None,
        RoleName: Optional[str] = None,
    ) -> Dict:
        pass


    def import_volume(
        self,
        AvailabilityZone: str,
        Image: Dict,
        Volume: Dict,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_capacity_reservation(
        self,
        CapacityReservationId: str,
        InstanceCount: Optional[int] = None,
        EndDate: Optional[datetime] = None,
        EndDateType: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_client_vpn_endpoint(
        self,
        ClientVpnEndpointId: str,
        ServerCertificateArn: Optional[str] = None,
        ConnectionLogOptions: Optional[Dict] = None,
        DnsServers: Optional[Dict] = None,
        Description: Optional[str] = None,
        SplitTunnel: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_ebs_default_kms_key_id(
        self,
        KmsKeyId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_fleet(
        self,
        FleetId: str,
        TargetCapacitySpecification: Dict,
        DryRun: Optional[bool] = None,
        ExcessCapacityTerminationPolicy: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_fpga_image_attribute(
        self,
        FpgaImageId: str,
        DryRun: Optional[bool] = None,
        Attribute: Optional[str] = None,
        OperationType: Optional[str] = None,
        UserIds: Optional[List] = None,
        UserGroups: Optional[List] = None,
        ProductCodes: Optional[List] = None,
        LoadPermission: Optional[Dict] = None,
        Description: Optional[str] = None,
        Name: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_hosts(
        self,
        HostIds: List,
        AutoPlacement: Optional[str] = None,
        HostRecovery: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_id_format(
        self,
        Resource: str,
        UseLongIds: bool,
    ):
        pass


    def modify_identity_id_format(
        self,
        PrincipalArn: str,
        Resource: str,
        UseLongIds: bool,
    ):
        pass


    def modify_image_attribute(
        self,
        ImageId: str,
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


    def modify_instance_attribute(
        self,
        InstanceId: str,
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


    def modify_instance_capacity_reservation_attributes(
        self,
        InstanceId: str,
        CapacityReservationSpecification: Dict,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_instance_credit_specification(
        self,
        InstanceCreditSpecifications: List,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_instance_event_start_time(
        self,
        InstanceId: str,
        InstanceEventId: str,
        NotBefore: datetime,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_instance_placement(
        self,
        InstanceId: str,
        Affinity: Optional[str] = None,
        GroupName: Optional[str] = None,
        HostId: Optional[str] = None,
        Tenancy: Optional[str] = None,
        PartitionNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_launch_template(
        self,
        DryRun: Optional[bool] = None,
        ClientToken: Optional[str] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
        DefaultVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attachment: Optional[Dict] = None,
        Description: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
        Groups: Optional[List] = None,
        SourceDestCheck: Optional[Dict] = None,
    ):
        pass


    def modify_reserved_instances(
        self,
        ReservedInstancesIds: List,
        TargetConfigurations: List,
        ClientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def modify_snapshot_attribute(
        self,
        SnapshotId: str,
        Attribute: Optional[str] = None,
        CreateVolumePermission: Optional[Dict] = None,
        GroupNames: Optional[List] = None,
        OperationType: Optional[str] = None,
        UserIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def modify_spot_fleet_request(
        self,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: Optional[str] = None,
        TargetCapacity: Optional[int] = None,
        OnDemandTargetCapacity: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_subnet_attribute(
        self,
        SubnetId: str,
        AssignIpv6AddressOnCreation: Optional[Dict] = None,
        MapPublicIpOnLaunch: Optional[Dict] = None,
    ):
        pass


    def modify_traffic_mirror_filter_network_services(
        self,
        TrafficMirrorFilterId: str,
        AddNetworkServices: Optional[List] = None,
        RemoveNetworkServices: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: Optional[str] = None,
        RuleNumber: Optional[int] = None,
        RuleAction: Optional[str] = None,
        DestinationPortRange: Optional[Dict] = None,
        SourcePortRange: Optional[Dict] = None,
        Protocol: Optional[int] = None,
        DestinationCidrBlock: Optional[str] = None,
        SourceCidrBlock: Optional[str] = None,
        Description: Optional[str] = None,
        RemoveFields: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_traffic_mirror_session(
        self,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: Optional[str] = None,
        TrafficMirrorFilterId: Optional[str] = None,
        PacketLength: Optional[int] = None,
        SessionNumber: Optional[int] = None,
        VirtualNetworkId: Optional[int] = None,
        Description: Optional[str] = None,
        RemoveFields: Optional[List] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: Optional[List] = None,
        RemoveSubnetIds: Optional[List] = None,
        Options: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_volume(
        self,
        VolumeId: str,
        DryRun: Optional[bool] = None,
        Size: Optional[int] = None,
        VolumeType: Optional[str] = None,
        Iops: Optional[int] = None,
    ) -> Dict:
        pass


    def modify_volume_attribute(
        self,
        VolumeId: str,
        AutoEnableIO: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def modify_vpc_attribute(
        self,
        VpcId: str,
        EnableDnsHostnames: Optional[Dict] = None,
        EnableDnsSupport: Optional[Dict] = None,
    ):
        pass


    def modify_vpc_endpoint(
        self,
        VpcEndpointId: str,
        DryRun: Optional[bool] = None,
        ResetPolicy: Optional[bool] = None,
        PolicyDocument: Optional[str] = None,
        AddRouteTableIds: Optional[List] = None,
        RemoveRouteTableIds: Optional[List] = None,
        AddSubnetIds: Optional[List] = None,
        RemoveSubnetIds: Optional[List] = None,
        AddSecurityGroupIds: Optional[List] = None,
        RemoveSecurityGroupIds: Optional[List] = None,
        PrivateDnsEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationId: str,
        DryRun: Optional[bool] = None,
        ConnectionNotificationArn: Optional[str] = None,
        ConnectionEvents: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_vpc_endpoint_service_configuration(
        self,
        ServiceId: str,
        DryRun: Optional[bool] = None,
        AcceptanceRequired: Optional[bool] = None,
        AddNetworkLoadBalancerArns: Optional[List] = None,
        RemoveNetworkLoadBalancerArns: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: Optional[bool] = None,
        AddAllowedPrincipals: Optional[List] = None,
        RemoveAllowedPrincipals: Optional[List] = None,
    ) -> Dict:
        pass


    def modify_vpc_peering_connection_options(
        self,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: Optional[Dict] = None,
        DryRun: Optional[bool] = None,
        RequesterPeeringConnectionOptions: Optional[Dict] = None,
    ) -> Dict:
        pass


    def modify_vpc_tenancy(
        self,
        VpcId: str,
        InstanceTenancy: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_vpn_connection(
        self,
        VpnConnectionId: str,
        TransitGatewayId: Optional[str] = None,
        CustomerGatewayId: Optional[str] = None,
        VpnGatewayId: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_vpn_tunnel_certificate(
        self,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def modify_vpn_tunnel_options(
        self,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: Dict,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def monitor_instances(
        self,
        InstanceIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def move_address_to_vpc(
        self,
        PublicIp: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def provision_byoip_cidr(
        self,
        Cidr: str,
        CidrAuthorizationContext: Optional[Dict] = None,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def purchase_host_reservation(
        self,
        HostIdSet: List,
        OfferingId: str,
        ClientToken: Optional[str] = None,
        CurrencyCode: Optional[str] = None,
        LimitPrice: Optional[str] = None,
    ) -> Dict:
        pass


    def purchase_reserved_instances_offering(
        self,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: Optional[bool] = None,
        LimitPrice: Optional[Dict] = None,
        PurchaseTime: Optional[datetime] = None,
    ) -> Dict:
        pass


    def purchase_scheduled_instances(
        self,
        PurchaseRequests: List,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reboot_instances(
        self,
        InstanceIds: List,
        DryRun: Optional[bool] = None,
    ):
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
    ) -> Dict:
        pass


    def reject_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reject_vpc_endpoint_connections(
        self,
        ServiceId: str,
        VpcEndpointIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reject_vpc_peering_connection(
        self,
        VpcPeeringConnectionId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def release_address(
        self,
        AllocationId: Optional[str] = None,
        PublicIp: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def release_hosts(
        self,
        HostIds: List,
    ) -> Dict:
        pass


    def replace_iam_instance_profile_association(
        self,
        IamInstanceProfile: Dict,
        AssociationId: str,
    ) -> Dict:
        pass


    def replace_network_acl_association(
        self,
        AssociationId: str,
        NetworkAclId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def replace_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
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


    def replace_route(
        self,
        RouteTableId: str,
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
    ):
        pass


    def replace_route_table_association(
        self,
        AssociationId: str,
        RouteTableId: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def replace_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: Optional[str] = None,
        Blackhole: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def report_instance_status(
        self,
        Instances: List,
        ReasonCodes: List,
        Status: str,
        Description: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EndTime: Optional[datetime] = None,
        StartTime: Optional[datetime] = None,
    ):
        pass


    def request_spot_fleet(
        self,
        SpotFleetRequestConfig: Dict,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def request_spot_instances(
        self,
        AvailabilityZoneGroup: Optional[str] = None,
        BlockDurationMinutes: Optional[int] = None,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
        InstanceCount: Optional[int] = None,
        LaunchGroup: Optional[str] = None,
        LaunchSpecification: Optional[Dict] = None,
        SpotPrice: Optional[str] = None,
        Type: Optional[str] = None,
        ValidFrom: Optional[datetime] = None,
        ValidUntil: Optional[datetime] = None,
        InstanceInterruptionBehavior: Optional[str] = None,
    ) -> Dict:
        pass


    def reset_ebs_default_kms_key_id(
        self,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def reset_fpga_image_attribute(
        self,
        FpgaImageId: str,
        DryRun: Optional[bool] = None,
        Attribute: Optional[str] = None,
    ) -> Dict:
        pass


    def reset_image_attribute(
        self,
        Attribute: str,
        ImageId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reset_instance_attribute(
        self,
        Attribute: str,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def reset_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        DryRun: Optional[bool] = None,
        SourceDestCheck: Optional[str] = None,
    ):
        pass


    def reset_snapshot_attribute(
        self,
        Attribute: str,
        SnapshotId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def restore_address_to_classic(
        self,
        PublicIp: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def revoke_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: Optional[str] = None,
        RevokeAllGroups: Optional[bool] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def revoke_security_group_egress(
        self,
        GroupId: str,
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


    def revoke_security_group_ingress(
        self,
        CidrIp: Optional[str] = None,
        FromPort: Optional[int] = None,
        GroupId: Optional[str] = None,
        GroupName: Optional[str] = None,
        IpPermissions: Optional[List] = None,
        IpProtocol: Optional[str] = None,
        SourceSecurityGroupName: Optional[str] = None,
        SourceSecurityGroupOwnerId: Optional[str] = None,
        ToPort: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ):
        pass


    def run_instances(
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
    ) -> Dict:
        pass


    def run_scheduled_instances(
        self,
        LaunchSpecification: Dict,
        ScheduledInstanceId: str,
        ClientToken: Optional[str] = None,
        DryRun: Optional[bool] = None,
        InstanceCount: Optional[int] = None,
    ) -> Dict:
        pass


    def search_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List,
        MaxResults: Optional[int] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def send_diagnostic_interrupt(
        self,
        InstanceId: str,
        DryRun: Optional[bool] = None,
    ):
        pass


    def start_instances(
        self,
        InstanceIds: List,
        AdditionalInfo: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def stop_instances(
        self,
        InstanceIds: List,
        Hibernate: Optional[bool] = None,
        DryRun: Optional[bool] = None,
        Force: Optional[bool] = None,
    ) -> Dict:
        pass


    def terminate_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        ConnectionId: Optional[str] = None,
        Username: Optional[str] = None,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def terminate_instances(
        self,
        InstanceIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def unassign_ipv6_addresses(
        self,
        Ipv6Addresses: List,
        NetworkInterfaceId: str,
    ) -> Dict:
        pass


    def unassign_private_ip_addresses(
        self,
        NetworkInterfaceId: str,
        PrivateIpAddresses: List,
    ):
        pass


    def unmonitor_instances(
        self,
        InstanceIds: List,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_security_group_rule_descriptions_egress(
        self,
        IpPermissions: List,
        DryRun: Optional[bool] = None,
        GroupId: Optional[str] = None,
        GroupName: Optional[str] = None,
    ) -> Dict:
        pass


    def update_security_group_rule_descriptions_ingress(
        self,
        IpPermissions: List,
        DryRun: Optional[bool] = None,
        GroupId: Optional[str] = None,
        GroupName: Optional[str] = None,
    ) -> Dict:
        pass


    def withdraw_byoip_cidr(
        self,
        Cidr: str,
        DryRun: Optional[bool] = None,
    ) -> Dict:
        pass

