from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeDBClusters(Paginator):
    def paginate(
        self,
        DBClusterIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDBEngineVersions(Paginator):
    def paginate(
        self,
        Engine: Optional[str] = None,
        EngineVersion: Optional[str] = None,
        DBParameterGroupFamily: Optional[str] = None,
        Filters: Optional[List] = None,
        DefaultOnly: Optional[bool] = None,
        ListSupportedCharacterSets: Optional[bool] = None,
        ListSupportedTimezones: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDBInstances(Paginator):
    def paginate(
        self,
        DBInstanceIdentifier: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeDBSubnetGroups(Paginator):
    def paginate(
        self,
        DBSubnetGroupName: Optional[str] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        SourceIdentifier: Optional[str] = None,
        SourceType: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        Duration: Optional[int] = None,
        EventCategories: Optional[List] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeOrderableDBInstanceOptions(Paginator):
    def paginate(
        self,
        Engine: str,
        EngineVersion: Optional[str] = None,
        DBInstanceClass: Optional[str] = None,
        LicenseModel: Optional[str] = None,
        Vpc: Optional[bool] = None,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

