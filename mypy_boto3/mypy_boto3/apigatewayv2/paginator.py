from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetApis(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetAuthorizers(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDeployments(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDomainNames(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetIntegrationResponses(Paginator):
    def paginate(
        self,
        ApiId: str,
        IntegrationId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetIntegrations(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetModels(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetRouteResponses(Paginator):
    def paginate(
        self,
        ApiId: str,
        RouteId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetRoutes(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetStages(Paginator):
    def paginate(
        self,
        ApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

