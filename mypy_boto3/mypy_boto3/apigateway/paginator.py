from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetApiKeys(Paginator):
    def paginate(
        self,
        nameQuery: Optional[str] = None,
        customerId: Optional[str] = None,
        includeValues: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetAuthorizers(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBasePathMappings(Paginator):
    def paginate(
        self,
        domainName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetClientCertificates(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDeployments(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDocumentationParts(Paginator):
    def paginate(
        self,
        restApiId: str,
        type: Optional[str] = None,
        nameQuery: Optional[str] = None,
        path: Optional[str] = None,
        locationStatus: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDocumentationVersions(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetDomainNames(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetGatewayResponses(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetModels(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetRequestValidators(Paginator):
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetResources(Paginator):
    def paginate(
        self,
        restApiId: str,
        embed: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetRestApis(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSdkTypes(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetUsage(Paginator):
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetUsagePlanKeys(Paginator):
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetUsagePlans(Paginator):
    def paginate(
        self,
        keyId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetVpcLinks(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

