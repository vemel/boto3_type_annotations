from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeByoipCidrs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, DryRun: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeCapacityReservations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CapacityReservationIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClassicLinkInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        InstanceIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClientVpnAuthorizationRules(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClientVpnConnections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClientVpnEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClientVpnEndpointIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClientVpnRoutes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeClientVpnTargetNetworks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDhcpOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DhcpOptionsIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEgressOnlyInternetGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFleets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        FleetIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFlowLogs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        FlowLogIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeFpgaImages(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[Any] = None,
        Owners: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeHostReservationOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeHostReservations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        HostReservationIdSet: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeHosts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        HostIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeIamInstanceProfileAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AssociationIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeImportImageTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        ImportTaskIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeImportSnapshotTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        ImportTaskIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstanceCreditSpecifications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstanceStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        InstanceIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInternetGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeLaunchTemplateVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[Any] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeLaunchTemplates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[Any] = None,
        LaunchTemplateNames: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeMovingAddresses(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PublicIps: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNatGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        NatGatewayIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNetworkAcls(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NetworkAclIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNetworkInterfacePermissions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        NetworkInterfacePermissionIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeNetworkInterfaces(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePrefixLists(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PrefixListIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePrincipalIdFormat(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Resources: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePublicIpv4Pools(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, PoolIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeReservedInstancesModifications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        ReservedInstancesModificationIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedInstancesOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AvailabilityZone: str = None,
        Filters: List[Any] = None,
        IncludeMarketplace: bool = None,
        InstanceType: str = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: str = None,
        ProductDescription: str = None,
        ReservedInstancesOfferingIds: List[Any] = None,
        DryRun: bool = None,
        InstanceTenancy: str = None,
        OfferingType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeRouteTables(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        RouteTableIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScheduledInstanceAvailability(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        FirstSlotStartTimeRange: Dict[str, Any],
        Recurrence: Dict[str, Any],
        DryRun: bool = None,
        Filters: List[Any] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeScheduledInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        ScheduledInstanceIds: List[Any] = None,
        SlotStartTimeRange: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        GroupIds: List[Any] = None,
        GroupNames: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        OwnerIds: List[Any] = None,
        RestorableByUserIds: List[Any] = None,
        SnapshotIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSpotFleetInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSpotFleetRequests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        SpotFleetRequestIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSpotInstanceRequests(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSpotPriceHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[Any] = None,
        ProductDescriptions: List[Any] = None,
        StartTime: datetime = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeStaleSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, VpcId: str, DryRun: bool = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeSubnets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        SubnetIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTags(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTrafficMirrorFilters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TrafficMirrorFilterIds: List[Any] = None,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTrafficMirrorSessions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TrafficMirrorSessionIds: List[Any] = None,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTrafficMirrorTargets(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TrafficMirrorTargetIds: List[Any] = None,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTransitGatewayAttachments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTransitGatewayRouteTables(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayRouteTableIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTransitGatewayVpcAttachments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayAttachmentIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeTransitGateways(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayIds: List[Any] = None,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVolumeStatus(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVolumes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        VolumeIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVolumesModifications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        VolumeIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcClassicLinkDnsSupport(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, VpcIds: List[Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpointConnectionNotifications(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpointConnections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpointServiceConfigurations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        ServiceIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpointServicePermissions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpointServices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        ServiceNames: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcPeeringConnections(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeVpcs(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Filters: List[Any] = None,
        VpcIds: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTransitGatewayAttachmentPropagations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTransitGatewayRouteTableAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetTransitGatewayRouteTablePropagations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[Any] = None,
        DryRun: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
