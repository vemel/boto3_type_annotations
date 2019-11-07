from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeApplicationVersions(Paginator):
    def paginate(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabels: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEnvironmentManagedActionHistory(Paginator):
    def paginate(
        self,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEnvironments(Paginator):
    def paginate(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabel: Optional[str] = None,
        EnvironmentIds: Optional[List] = None,
        EnvironmentNames: Optional[List] = None,
        IncludeDeleted: Optional[bool] = None,
        IncludedDeletedBackTo: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeEvents(Paginator):
    def paginate(
        self,
        ApplicationName: Optional[str] = None,
        VersionLabel: Optional[str] = None,
        TemplateName: Optional[str] = None,
        EnvironmentId: Optional[str] = None,
        EnvironmentName: Optional[str] = None,
        PlatformArn: Optional[str] = None,
        RequestId: Optional[str] = None,
        Severity: Optional[str] = None,
        StartTime: Optional[datetime] = None,
        EndTime: Optional[datetime] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPlatformVersions(Paginator):
    def paginate(
        self,
        Filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

