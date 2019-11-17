"Helper functions for ec2 service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_ec2.client import Client
from mypy_boto3_ec2.paginator import (
    DescribeByoipCidrsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstancesPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeSubnetsPaginator,
    DescribeTagsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVolumesPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    DescribeVpcsPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
)
from mypy_boto3_ec2.service_resource import ServiceResource
from mypy_boto3_ec2.waiter import (
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageAvailableWaiter,
    ImageExistsWaiter,
    InstanceExistsWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SnapshotCompletedWaiter,
    SpotInstanceRequestFulfilledWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('ec2')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("ec2", **kwargs)
    return boto3.client("ec2", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_resource(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServiceResource:
    """
    Equivalent of `boto3.resource('ec2')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.resource("ec2", **kwargs)
    return boto3.resource("ec2", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_byoip_cidrs_paginator(client: Client) -> DescribeByoipCidrsPaginator:
    """
    Equivalent of `client.get_paginator('describe_byoip_cidrs')`, returns a correct type.
    """
    return client.get_paginator("describe_byoip_cidrs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_capacity_reservations_paginator(
    client: Client,
) -> DescribeCapacityReservationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_capacity_reservations')`, returns a correct type.
    """
    return client.get_paginator("describe_capacity_reservations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_classic_link_instances_paginator(
    client: Client,
) -> DescribeClassicLinkInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_classic_link_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_classic_link_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_client_vpn_authorization_rules_paginator(
    client: Client,
) -> DescribeClientVpnAuthorizationRulesPaginator:
    """
    Equivalent of `client.get_paginator('describe_client_vpn_authorization_rules')`, returns a correct type.
    """
    return client.get_paginator("describe_client_vpn_authorization_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_client_vpn_connections_paginator(
    client: Client,
) -> DescribeClientVpnConnectionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_client_vpn_connections')`, returns a correct type.
    """
    return client.get_paginator("describe_client_vpn_connections")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_client_vpn_endpoints_paginator(
    client: Client,
) -> DescribeClientVpnEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('describe_client_vpn_endpoints')`, returns a correct type.
    """
    return client.get_paginator("describe_client_vpn_endpoints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_client_vpn_routes_paginator(
    client: Client,
) -> DescribeClientVpnRoutesPaginator:
    """
    Equivalent of `client.get_paginator('describe_client_vpn_routes')`, returns a correct type.
    """
    return client.get_paginator("describe_client_vpn_routes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_client_vpn_target_networks_paginator(
    client: Client,
) -> DescribeClientVpnTargetNetworksPaginator:
    """
    Equivalent of `client.get_paginator('describe_client_vpn_target_networks')`, returns a correct type.
    """
    return client.get_paginator("describe_client_vpn_target_networks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_dhcp_options_paginator(client: Client) -> DescribeDhcpOptionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_dhcp_options')`, returns a correct type.
    """
    return client.get_paginator("describe_dhcp_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_egress_only_internet_gateways_paginator(
    client: Client,
) -> DescribeEgressOnlyInternetGatewaysPaginator:
    """
    Equivalent of `client.get_paginator('describe_egress_only_internet_gateways')`, returns a correct type.
    """
    return client.get_paginator("describe_egress_only_internet_gateways")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fleets_paginator(client: Client) -> DescribeFleetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_fleets')`, returns a correct type.
    """
    return client.get_paginator("describe_fleets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_flow_logs_paginator(client: Client) -> DescribeFlowLogsPaginator:
    """
    Equivalent of `client.get_paginator('describe_flow_logs')`, returns a correct type.
    """
    return client.get_paginator("describe_flow_logs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_fpga_images_paginator(client: Client) -> DescribeFpgaImagesPaginator:
    """
    Equivalent of `client.get_paginator('describe_fpga_images')`, returns a correct type.
    """
    return client.get_paginator("describe_fpga_images")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_host_reservation_offerings_paginator(
    client: Client,
) -> DescribeHostReservationOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_host_reservation_offerings')`, returns a correct type.
    """
    return client.get_paginator("describe_host_reservation_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_host_reservations_paginator(
    client: Client,
) -> DescribeHostReservationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_host_reservations')`, returns a correct type.
    """
    return client.get_paginator("describe_host_reservations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_hosts_paginator(client: Client) -> DescribeHostsPaginator:
    """
    Equivalent of `client.get_paginator('describe_hosts')`, returns a correct type.
    """
    return client.get_paginator("describe_hosts")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_iam_instance_profile_associations_paginator(
    client: Client,
) -> DescribeIamInstanceProfileAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_iam_instance_profile_associations')`, returns a correct type.
    """
    return client.get_paginator("describe_iam_instance_profile_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_import_image_tasks_paginator(
    client: Client,
) -> DescribeImportImageTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_import_image_tasks')`, returns a correct type.
    """
    return client.get_paginator("describe_import_image_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_import_snapshot_tasks_paginator(
    client: Client,
) -> DescribeImportSnapshotTasksPaginator:
    """
    Equivalent of `client.get_paginator('describe_import_snapshot_tasks')`, returns a correct type.
    """
    return client.get_paginator("describe_import_snapshot_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_credit_specifications_paginator(
    client: Client,
) -> DescribeInstanceCreditSpecificationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_credit_specifications')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_credit_specifications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instance_status_paginator(
    client: Client,
) -> DescribeInstanceStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_instance_status')`, returns a correct type.
    """
    return client.get_paginator("describe_instance_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_instances_paginator(client: Client) -> DescribeInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_internet_gateways_paginator(
    client: Client,
) -> DescribeInternetGatewaysPaginator:
    """
    Equivalent of `client.get_paginator('describe_internet_gateways')`, returns a correct type.
    """
    return client.get_paginator("describe_internet_gateways")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_launch_template_versions_paginator(
    client: Client,
) -> DescribeLaunchTemplateVersionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_launch_template_versions')`, returns a correct type.
    """
    return client.get_paginator("describe_launch_template_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_launch_templates_paginator(
    client: Client,
) -> DescribeLaunchTemplatesPaginator:
    """
    Equivalent of `client.get_paginator('describe_launch_templates')`, returns a correct type.
    """
    return client.get_paginator("describe_launch_templates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_moving_addresses_paginator(
    client: Client,
) -> DescribeMovingAddressesPaginator:
    """
    Equivalent of `client.get_paginator('describe_moving_addresses')`, returns a correct type.
    """
    return client.get_paginator("describe_moving_addresses")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_nat_gateways_paginator(client: Client) -> DescribeNatGatewaysPaginator:
    """
    Equivalent of `client.get_paginator('describe_nat_gateways')`, returns a correct type.
    """
    return client.get_paginator("describe_nat_gateways")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_network_acls_paginator(client: Client) -> DescribeNetworkAclsPaginator:
    """
    Equivalent of `client.get_paginator('describe_network_acls')`, returns a correct type.
    """
    return client.get_paginator("describe_network_acls")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_network_interface_permissions_paginator(
    client: Client,
) -> DescribeNetworkInterfacePermissionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_network_interface_permissions')`, returns a correct type.
    """
    return client.get_paginator("describe_network_interface_permissions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_network_interfaces_paginator(
    client: Client,
) -> DescribeNetworkInterfacesPaginator:
    """
    Equivalent of `client.get_paginator('describe_network_interfaces')`, returns a correct type.
    """
    return client.get_paginator("describe_network_interfaces")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_prefix_lists_paginator(client: Client) -> DescribePrefixListsPaginator:
    """
    Equivalent of `client.get_paginator('describe_prefix_lists')`, returns a correct type.
    """
    return client.get_paginator("describe_prefix_lists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_principal_id_format_paginator(
    client: Client,
) -> DescribePrincipalIdFormatPaginator:
    """
    Equivalent of `client.get_paginator('describe_principal_id_format')`, returns a correct type.
    """
    return client.get_paginator("describe_principal_id_format")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_public_ipv4_pools_paginator(
    client: Client,
) -> DescribePublicIpv4PoolsPaginator:
    """
    Equivalent of `client.get_paginator('describe_public_ipv4_pools')`, returns a correct type.
    """
    return client.get_paginator("describe_public_ipv4_pools")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_instances_modifications_paginator(
    client: Client,
) -> DescribeReservedInstancesModificationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_instances_modifications')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_instances_modifications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_instances_offerings_paginator(
    client: Client,
) -> DescribeReservedInstancesOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_instances_offerings')`, returns a correct type.
    """
    return client.get_paginator("describe_reserved_instances_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_route_tables_paginator(client: Client) -> DescribeRouteTablesPaginator:
    """
    Equivalent of `client.get_paginator('describe_route_tables')`, returns a correct type.
    """
    return client.get_paginator("describe_route_tables")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scheduled_instance_availability_paginator(
    client: Client,
) -> DescribeScheduledInstanceAvailabilityPaginator:
    """
    Equivalent of `client.get_paginator('describe_scheduled_instance_availability')`, returns a correct type.
    """
    return client.get_paginator("describe_scheduled_instance_availability")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_scheduled_instances_paginator(
    client: Client,
) -> DescribeScheduledInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_scheduled_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_scheduled_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_security_groups_paginator(
    client: Client,
) -> DescribeSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_security_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_snapshots_paginator(client: Client) -> DescribeSnapshotsPaginator:
    """
    Equivalent of `client.get_paginator('describe_snapshots')`, returns a correct type.
    """
    return client.get_paginator("describe_snapshots")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_spot_fleet_instances_paginator(
    client: Client,
) -> DescribeSpotFleetInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_spot_fleet_instances')`, returns a correct type.
    """
    return client.get_paginator("describe_spot_fleet_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_spot_fleet_requests_paginator(
    client: Client,
) -> DescribeSpotFleetRequestsPaginator:
    """
    Equivalent of `client.get_paginator('describe_spot_fleet_requests')`, returns a correct type.
    """
    return client.get_paginator("describe_spot_fleet_requests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_spot_instance_requests_paginator(
    client: Client,
) -> DescribeSpotInstanceRequestsPaginator:
    """
    Equivalent of `client.get_paginator('describe_spot_instance_requests')`, returns a correct type.
    """
    return client.get_paginator("describe_spot_instance_requests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_spot_price_history_paginator(
    client: Client,
) -> DescribeSpotPriceHistoryPaginator:
    """
    Equivalent of `client.get_paginator('describe_spot_price_history')`, returns a correct type.
    """
    return client.get_paginator("describe_spot_price_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_stale_security_groups_paginator(
    client: Client,
) -> DescribeStaleSecurityGroupsPaginator:
    """
    Equivalent of `client.get_paginator('describe_stale_security_groups')`, returns a correct type.
    """
    return client.get_paginator("describe_stale_security_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_subnets_paginator(client: Client) -> DescribeSubnetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_subnets')`, returns a correct type.
    """
    return client.get_paginator("describe_subnets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_tags_paginator(client: Client) -> DescribeTagsPaginator:
    """
    Equivalent of `client.get_paginator('describe_tags')`, returns a correct type.
    """
    return client.get_paginator("describe_tags")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_traffic_mirror_filters_paginator(
    client: Client,
) -> DescribeTrafficMirrorFiltersPaginator:
    """
    Equivalent of `client.get_paginator('describe_traffic_mirror_filters')`, returns a correct type.
    """
    return client.get_paginator("describe_traffic_mirror_filters")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_traffic_mirror_sessions_paginator(
    client: Client,
) -> DescribeTrafficMirrorSessionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_traffic_mirror_sessions')`, returns a correct type.
    """
    return client.get_paginator("describe_traffic_mirror_sessions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_traffic_mirror_targets_paginator(
    client: Client,
) -> DescribeTrafficMirrorTargetsPaginator:
    """
    Equivalent of `client.get_paginator('describe_traffic_mirror_targets')`, returns a correct type.
    """
    return client.get_paginator("describe_traffic_mirror_targets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_transit_gateway_attachments_paginator(
    client: Client,
) -> DescribeTransitGatewayAttachmentsPaginator:
    """
    Equivalent of `client.get_paginator('describe_transit_gateway_attachments')`, returns a correct type.
    """
    return client.get_paginator("describe_transit_gateway_attachments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_transit_gateway_route_tables_paginator(
    client: Client,
) -> DescribeTransitGatewayRouteTablesPaginator:
    """
    Equivalent of `client.get_paginator('describe_transit_gateway_route_tables')`, returns a correct type.
    """
    return client.get_paginator("describe_transit_gateway_route_tables")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_transit_gateway_vpc_attachments_paginator(
    client: Client,
) -> DescribeTransitGatewayVpcAttachmentsPaginator:
    """
    Equivalent of `client.get_paginator('describe_transit_gateway_vpc_attachments')`, returns a correct type.
    """
    return client.get_paginator("describe_transit_gateway_vpc_attachments")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_transit_gateways_paginator(
    client: Client,
) -> DescribeTransitGatewaysPaginator:
    """
    Equivalent of `client.get_paginator('describe_transit_gateways')`, returns a correct type.
    """
    return client.get_paginator("describe_transit_gateways")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_volume_status_paginator(
    client: Client,
) -> DescribeVolumeStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_volume_status')`, returns a correct type.
    """
    return client.get_paginator("describe_volume_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_volumes_paginator(client: Client) -> DescribeVolumesPaginator:
    """
    Equivalent of `client.get_paginator('describe_volumes')`, returns a correct type.
    """
    return client.get_paginator("describe_volumes")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_volumes_modifications_paginator(
    client: Client,
) -> DescribeVolumesModificationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_volumes_modifications')`, returns a correct type.
    """
    return client.get_paginator("describe_volumes_modifications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_classic_link_dns_support_paginator(
    client: Client,
) -> DescribeVpcClassicLinkDnsSupportPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_classic_link_dns_support')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_classic_link_dns_support")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoint_connection_notifications_paginator(
    client: Client,
) -> DescribeVpcEndpointConnectionNotificationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoint_connection_notifications')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoint_connection_notifications")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoint_connections_paginator(
    client: Client,
) -> DescribeVpcEndpointConnectionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoint_connections')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoint_connections")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoint_service_configurations_paginator(
    client: Client,
) -> DescribeVpcEndpointServiceConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoint_service_configurations')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoint_service_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoint_service_permissions_paginator(
    client: Client,
) -> DescribeVpcEndpointServicePermissionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoint_service_permissions')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoint_service_permissions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoint_services_paginator(
    client: Client,
) -> DescribeVpcEndpointServicesPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoint_services')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoint_services")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_endpoints_paginator(
    client: Client,
) -> DescribeVpcEndpointsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_endpoints')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_endpoints")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpc_peering_connections_paginator(
    client: Client,
) -> DescribeVpcPeeringConnectionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpc_peering_connections')`, returns a correct type.
    """
    return client.get_paginator("describe_vpc_peering_connections")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_vpcs_paginator(client: Client) -> DescribeVpcsPaginator:
    """
    Equivalent of `client.get_paginator('describe_vpcs')`, returns a correct type.
    """
    return client.get_paginator("describe_vpcs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_transit_gateway_attachment_propagations_paginator(
    client: Client,
) -> GetTransitGatewayAttachmentPropagationsPaginator:
    """
    Equivalent of `client.get_paginator('get_transit_gateway_attachment_propagations')`, returns a correct type.
    """
    return client.get_paginator("get_transit_gateway_attachment_propagations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_transit_gateway_route_table_associations_paginator(
    client: Client,
) -> GetTransitGatewayRouteTableAssociationsPaginator:
    """
    Equivalent of `client.get_paginator('get_transit_gateway_route_table_associations')`, returns a correct type.
    """
    return client.get_paginator("get_transit_gateway_route_table_associations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_transit_gateway_route_table_propagations_paginator(
    client: Client,
) -> GetTransitGatewayRouteTablePropagationsPaginator:
    """
    Equivalent of `client.get_paginator('get_transit_gateway_route_table_propagations')`, returns a correct type.
    """
    return client.get_paginator("get_transit_gateway_route_table_propagations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_bundle_task_complete_waiter(client: Client) -> BundleTaskCompleteWaiter:
    """
    Equivalent of `client.get_waiter('bundle_task_complete')`, returns a correct type.
    """
    return client.get_waiter("bundle_task_complete")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_conversion_task_cancelled_waiter(
    client: Client,
) -> ConversionTaskCancelledWaiter:
    """
    Equivalent of `client.get_waiter('conversion_task_cancelled')`, returns a correct type.
    """
    return client.get_waiter("conversion_task_cancelled")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_conversion_task_completed_waiter(
    client: Client,
) -> ConversionTaskCompletedWaiter:
    """
    Equivalent of `client.get_waiter('conversion_task_completed')`, returns a correct type.
    """
    return client.get_waiter("conversion_task_completed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_conversion_task_deleted_waiter(client: Client) -> ConversionTaskDeletedWaiter:
    """
    Equivalent of `client.get_waiter('conversion_task_deleted')`, returns a correct type.
    """
    return client.get_waiter("conversion_task_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_customer_gateway_available_waiter(
    client: Client,
) -> CustomerGatewayAvailableWaiter:
    """
    Equivalent of `client.get_waiter('customer_gateway_available')`, returns a correct type.
    """
    return client.get_waiter("customer_gateway_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_export_task_cancelled_waiter(client: Client) -> ExportTaskCancelledWaiter:
    """
    Equivalent of `client.get_waiter('export_task_cancelled')`, returns a correct type.
    """
    return client.get_waiter("export_task_cancelled")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_export_task_completed_waiter(client: Client) -> ExportTaskCompletedWaiter:
    """
    Equivalent of `client.get_waiter('export_task_completed')`, returns a correct type.
    """
    return client.get_waiter("export_task_completed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_image_available_waiter(client: Client) -> ImageAvailableWaiter:
    """
    Equivalent of `client.get_waiter('image_available')`, returns a correct type.
    """
    return client.get_waiter("image_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_image_exists_waiter(client: Client) -> ImageExistsWaiter:
    """
    Equivalent of `client.get_waiter('image_exists')`, returns a correct type.
    """
    return client.get_waiter("image_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_exists_waiter(client: Client) -> InstanceExistsWaiter:
    """
    Equivalent of `client.get_waiter('instance_exists')`, returns a correct type.
    """
    return client.get_waiter("instance_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_running_waiter(client: Client) -> InstanceRunningWaiter:
    """
    Equivalent of `client.get_waiter('instance_running')`, returns a correct type.
    """
    return client.get_waiter("instance_running")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_status_ok_waiter(client: Client) -> InstanceStatusOkWaiter:
    """
    Equivalent of `client.get_waiter('instance_status_ok')`, returns a correct type.
    """
    return client.get_waiter("instance_status_ok")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_stopped_waiter(client: Client) -> InstanceStoppedWaiter:
    """
    Equivalent of `client.get_waiter('instance_stopped')`, returns a correct type.
    """
    return client.get_waiter("instance_stopped")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_terminated_waiter(client: Client) -> InstanceTerminatedWaiter:
    """
    Equivalent of `client.get_waiter('instance_terminated')`, returns a correct type.
    """
    return client.get_waiter("instance_terminated")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_key_pair_exists_waiter(client: Client) -> KeyPairExistsWaiter:
    """
    Equivalent of `client.get_waiter('key_pair_exists')`, returns a correct type.
    """
    return client.get_waiter("key_pair_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_nat_gateway_available_waiter(client: Client) -> NatGatewayAvailableWaiter:
    """
    Equivalent of `client.get_waiter('nat_gateway_available')`, returns a correct type.
    """
    return client.get_waiter("nat_gateway_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_network_interface_available_waiter(
    client: Client,
) -> NetworkInterfaceAvailableWaiter:
    """
    Equivalent of `client.get_waiter('network_interface_available')`, returns a correct type.
    """
    return client.get_waiter("network_interface_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_password_data_available_waiter(client: Client) -> PasswordDataAvailableWaiter:
    """
    Equivalent of `client.get_waiter('password_data_available')`, returns a correct type.
    """
    return client.get_waiter("password_data_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_snapshot_completed_waiter(client: Client) -> SnapshotCompletedWaiter:
    """
    Equivalent of `client.get_waiter('snapshot_completed')`, returns a correct type.
    """
    return client.get_waiter("snapshot_completed")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_spot_instance_request_fulfilled_waiter(
    client: Client,
) -> SpotInstanceRequestFulfilledWaiter:
    """
    Equivalent of `client.get_waiter('spot_instance_request_fulfilled')`, returns a correct type.
    """
    return client.get_waiter("spot_instance_request_fulfilled")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_subnet_available_waiter(client: Client) -> SubnetAvailableWaiter:
    """
    Equivalent of `client.get_waiter('subnet_available')`, returns a correct type.
    """
    return client.get_waiter("subnet_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_system_status_ok_waiter(client: Client) -> SystemStatusOkWaiter:
    """
    Equivalent of `client.get_waiter('system_status_ok')`, returns a correct type.
    """
    return client.get_waiter("system_status_ok")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_volume_available_waiter(client: Client) -> VolumeAvailableWaiter:
    """
    Equivalent of `client.get_waiter('volume_available')`, returns a correct type.
    """
    return client.get_waiter("volume_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_volume_deleted_waiter(client: Client) -> VolumeDeletedWaiter:
    """
    Equivalent of `client.get_waiter('volume_deleted')`, returns a correct type.
    """
    return client.get_waiter("volume_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_volume_in_use_waiter(client: Client) -> VolumeInUseWaiter:
    """
    Equivalent of `client.get_waiter('volume_in_use')`, returns a correct type.
    """
    return client.get_waiter("volume_in_use")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpc_available_waiter(client: Client) -> VpcAvailableWaiter:
    """
    Equivalent of `client.get_waiter('vpc_available')`, returns a correct type.
    """
    return client.get_waiter("vpc_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpc_exists_waiter(client: Client) -> VpcExistsWaiter:
    """
    Equivalent of `client.get_waiter('vpc_exists')`, returns a correct type.
    """
    return client.get_waiter("vpc_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpc_peering_connection_deleted_waiter(
    client: Client,
) -> VpcPeeringConnectionDeletedWaiter:
    """
    Equivalent of `client.get_waiter('vpc_peering_connection_deleted')`, returns a correct type.
    """
    return client.get_waiter("vpc_peering_connection_deleted")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpc_peering_connection_exists_waiter(
    client: Client,
) -> VpcPeeringConnectionExistsWaiter:
    """
    Equivalent of `client.get_waiter('vpc_peering_connection_exists')`, returns a correct type.
    """
    return client.get_waiter("vpc_peering_connection_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpn_connection_available_waiter(client: Client) -> VpnConnectionAvailableWaiter:
    """
    Equivalent of `client.get_waiter('vpn_connection_available')`, returns a correct type.
    """
    return client.get_waiter("vpn_connection_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_vpn_connection_deleted_waiter(client: Client) -> VpnConnectionDeletedWaiter:
    """
    Equivalent of `client.get_waiter('vpn_connection_deleted')`, returns a correct type.
    """
    return client.get_waiter("vpn_connection_deleted")
