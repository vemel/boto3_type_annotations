from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListApplicationRevisions(Paginator):
    def paginate(
        self,
        applicationName: str,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        s3Bucket: Optional[str] = None,
        s3KeyPrefix: Optional[str] = None,
        deployed: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListApplications(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeploymentConfigs(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeploymentGroups(Paginator):
    def paginate(
        self,
        applicationName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeploymentInstances(Paginator):
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: Optional[List] = None,
        instanceTypeFilter: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeploymentTargets(Paginator):
    def paginate(
        self,
        deploymentId: Optional[str] = None,
        targetFilters: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeployments(Paginator):
    def paginate(
        self,
        applicationName: Optional[str] = None,
        deploymentGroupName: Optional[str] = None,
        includeOnlyStatuses: Optional[List] = None,
        createTimeRange: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListGitHubAccountTokenNames(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOnPremisesInstances(Paginator):
    def paginate(
        self,
        registrationStatus: Optional[str] = None,
        tagFilters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

