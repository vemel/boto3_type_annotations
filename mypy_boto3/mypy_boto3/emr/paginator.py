from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListBootstrapActions(Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClusters(Paginator):
    def paginate(
        self,
        CreatedAfter: Optional[datetime] = None,
        CreatedBefore: Optional[datetime] = None,
        ClusterStates: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstanceFleets(Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstanceGroups(Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstances(Paginator):
    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: Optional[str] = None,
        InstanceGroupTypes: Optional[List] = None,
        InstanceFleetId: Optional[str] = None,
        InstanceFleetType: Optional[str] = None,
        InstanceStates: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSecurityConfigurations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSteps(Paginator):
    def paginate(
        self,
        ClusterId: str,
        StepStates: Optional[List] = None,
        StepIds: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

