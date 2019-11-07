from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeByoipCidrs(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeCapacityReservations(Paginator):
    def paginate(
        self,
        CapacityReservationIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClassicLinkInstances(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InstanceIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClientVpnAuthorizationRules(Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClientVpnConnections(Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClientVpnEndpoints(Paginator):
    def paginate(
        self,
        ClientVpnEndpointIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClientVpnRoutes(Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeClientVpnTargetNetworks(Paginator):
    def paginate(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDhcpOptions(Paginator):
    def paginate(
        self,
        DhcpOptionsIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEgressOnlyInternetGateways(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        EgressOnlyInternetGatewayIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFleets(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        FleetIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFlowLogs(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        FlowLogIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeFpgaImages(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        FpgaImageIds: Optional[List] = None,
        Owners: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeHostReservationOfferings(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        MaxDuration: Optional[int] = None,
        MinDuration: Optional[int] = None,
        OfferingId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeHostReservations(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        HostReservationIdSet: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeHosts(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        HostIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeIamInstanceProfileAssociations(Paginator):
    def paginate(
        self,
        AssociationIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeImportImageTasks(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ImportTaskIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeImportSnapshotTasks(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ImportTaskIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstanceCreditSpecifications(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstanceStatus(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        IncludeAllInstances: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInstances(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        InstanceIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeInternetGateways(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        InternetGatewayIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLaunchTemplateVersions(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        LaunchTemplateId: Optional[str] = None,
        LaunchTemplateName: Optional[str] = None,
        Versions: Optional[List] = None,
        MinVersion: Optional[str] = None,
        MaxVersion: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeLaunchTemplates(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        LaunchTemplateIds: Optional[List] = None,
        LaunchTemplateNames: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeMovingAddresses(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PublicIps: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNatGateways(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        NatGatewayIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNetworkAcls(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkAclIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNetworkInterfacePermissions(Paginator):
    def paginate(
        self,
        NetworkInterfacePermissionIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeNetworkInterfaces(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        NetworkInterfaceIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePrefixLists(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PrefixListIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePrincipalIdFormat(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Resources: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribePublicIpv4Pools(Paginator):
    def paginate(
        self,
        PoolIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedInstancesModifications(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        ReservedInstancesModificationIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeReservedInstancesOfferings(Paginator):
    def paginate(
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
        OfferingType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRouteTables(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        RouteTableIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScheduledInstanceAvailability(Paginator):
    def paginate(
        self,
        FirstSlotStartTimeRange: Dict,
        Recurrence: Dict,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        MaxSlotDurationInHours: Optional[int] = None,
        MinSlotDurationInHours: Optional[int] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeScheduledInstances(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        ScheduledInstanceIds: Optional[List] = None,
        SlotStartTimeRange: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSecurityGroups(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        GroupIds: Optional[List] = None,
        GroupNames: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSnapshots(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        OwnerIds: Optional[List] = None,
        RestorableByUserIds: Optional[List] = None,
        SnapshotIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSpotFleetInstances(Paginator):
    def paginate(
        self,
        SpotFleetRequestId: str,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSpotFleetRequests(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        SpotFleetRequestIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSpotInstanceRequests(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        SpotInstanceRequestIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSpotPriceHistory(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        AvailabilityZone: Optional[str] = None,
        DryRun: Optional[bool] = None,
        EndTime: Optional[datetime] = None,
        InstanceTypes: Optional[List] = None,
        ProductDescriptions: Optional[List] = None,
        StartTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeStaleSecurityGroups(Paginator):
    def paginate(
        self,
        VpcId: str,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeSubnets(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        SubnetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTags(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTrafficMirrorFilters(Paginator):
    def paginate(
        self,
        TrafficMirrorFilterIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTrafficMirrorSessions(Paginator):
    def paginate(
        self,
        TrafficMirrorSessionIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTrafficMirrorTargets(Paginator):
    def paginate(
        self,
        TrafficMirrorTargetIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTransitGatewayAttachments(Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTransitGatewayRouteTables(Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTransitGatewayVpcAttachments(Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeTransitGateways(Paginator):
    def paginate(
        self,
        TransitGatewayIds: Optional[List] = None,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVolumeStatus(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVolumes(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        VolumeIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVolumesModifications(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        VolumeIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcClassicLinkDnsSupport(Paginator):
    def paginate(
        self,
        VpcIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpointConnectionNotifications(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        ConnectionNotificationId: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpointConnections(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpointServiceConfigurations(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        ServiceIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpointServicePermissions(Paginator):
    def paginate(
        self,
        ServiceId: str,
        DryRun: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpointServices(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        ServiceNames: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcEndpoints(Paginator):
    def paginate(
        self,
        DryRun: Optional[bool] = None,
        VpcEndpointIds: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcPeeringConnections(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        VpcPeeringConnectionIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeVpcs(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        VpcIds: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTransitGatewayAttachmentPropagations(Paginator):
    def paginate(
        self,
        TransitGatewayAttachmentId: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTransitGatewayRouteTableAssociations(Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetTransitGatewayRouteTablePropagations(Paginator):
    def paginate(
        self,
        TransitGatewayRouteTableId: str,
        Filters: Optional[List] = None,
        DryRun: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

