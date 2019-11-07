from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAcceptedPortfolioShares(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        PortfolioShareType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListConstraintsForPortfolio(Paginator):
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        ProductId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLaunchPaths(Paginator):
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOrganizationPortfolioAccess(Paginator):
    def paginate(
        self,
        PortfolioId: str,
        OrganizationNodeType: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPortfolios(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPortfoliosForProduct(Paginator):
    def paginate(
        self,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPrincipalsForPortfolio(Paginator):
    def paginate(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProvisionedProductPlans(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        ProvisionProductId: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProvisioningArtifactsForServiceAction(Paginator):
    def paginate(
        self,
        ServiceActionId: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRecordHistory(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        SearchFilter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListResourcesForTagOption(Paginator):
    def paginate(
        self,
        TagOptionId: str,
        ResourceType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServiceActions(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServiceActionsForProvisioningArtifact(Paginator):
    def paginate(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagOptions(Paginator):
    def paginate(
        self,
        Filters: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ScanProvisionedProducts(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class SearchProductsAsAdmin(Paginator):
    def paginate(
        self,
        AcceptLanguage: Optional[str] = None,
        PortfolioId: Optional[str] = None,
        Filters: Optional[Dict] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        ProductSource: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass

