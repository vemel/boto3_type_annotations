from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class GetApiKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetAuthorizers(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetBasePathMappings(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, domainName: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetClientCertificates(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetDeployments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetDocumentationParts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        restApiId: str,
        type: str = None,
        nameQuery: str = None,
        path: str = None,
        locationStatus: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetDocumentationVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetDomainNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetGatewayResponses(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetModels(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetRequestValidators(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, restApiId: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetResources(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        restApiId: str,
        embed: List[Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetRestApis(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetSdkTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class GetUsage(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetUsagePlanKeys(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetUsagePlans(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, keyId: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetVpcLinks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass
