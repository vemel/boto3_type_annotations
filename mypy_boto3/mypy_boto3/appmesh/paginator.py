from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListMeshes(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRoutes(Paginator):
    def paginate(
        self,
        meshName: str,
        virtualRouterName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVirtualNodes(Paginator):
    def paginate(
        self,
        meshName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVirtualRouters(Paginator):
    def paginate(
        self,
        meshName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVirtualServices(Paginator):
    def paginate(
        self,
        meshName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

