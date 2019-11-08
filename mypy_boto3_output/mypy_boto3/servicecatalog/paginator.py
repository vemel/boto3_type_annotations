from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class ListAcceptedPortfolioShares(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioShareType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListConstraintsForPortfolio(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLaunchPaths(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOrganizationPortfolioAccess(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PortfolioId: str,
        OrganizationNodeType: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPortfolios(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListPortfoliosForProduct(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPrincipalsForPortfolio(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListProvisionedProductPlans(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListProvisioningArtifactsForServiceAction(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ServiceActionId: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListRecordHistory(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        SearchFilter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListResourcesForTagOption(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListServiceActions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, AcceptLanguage: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListServiceActionsForProvisioningArtifact(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListTagOptions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Filters: Dict[str, Any] = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ScanProvisionedProducts(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class SearchProductsAsAdmin(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: str = None,
        ProductSource: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass
