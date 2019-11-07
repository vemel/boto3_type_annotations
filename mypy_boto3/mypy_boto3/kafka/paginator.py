from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListClusterOperations(Paginator):
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClusters(Paginator):
    def paginate(
        self,
        ClusterNameFilter: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListConfigurationRevisions(Paginator):
    def paginate(
        self,
        Arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListConfigurations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNodes(Paginator):
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

