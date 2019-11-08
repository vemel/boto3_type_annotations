from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


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


class DescribeDBSubnetGroups(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DBSubnetGroupName: str = None,
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
