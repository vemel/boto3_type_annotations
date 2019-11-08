from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class DescribeCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CertificateIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeCustomAvailabilityZones(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusterBacktracks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusterEndpoints(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusterParameterGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusterParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusterSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[Any] = None,
        IncludeShared: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBEngineVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[Any] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBInstanceAutomatedBackups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBLogFiles(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBParameterGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBSecurityGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBSnapshots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[Any] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeDBSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEngineDefaultClusterParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEngineDefaultParameters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEventSubscriptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeEvents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[Any] = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeGlobalClusters(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeInstallationMedia(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        InstallationMediaId: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeOptionGroupOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeOptionGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        OptionGroupName: str = None,
        Filters: List[Any] = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeOrderableDBInstanceOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribePendingMaintenanceActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedDBInstances(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeReservedDBInstancesOfferings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DescribeSourceRegions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        RegionName: str = None,
        Filters: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class DownloadDBLogFilePortion(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
