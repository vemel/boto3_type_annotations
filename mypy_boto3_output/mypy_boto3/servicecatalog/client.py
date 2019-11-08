from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def accept_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_budget_with_resource(
        self, BudgetName: str, ResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_principal_with_portfolio(
        self,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_product_with_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str = None,
        SourcePortfolioId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_service_action_with_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def associate_tag_option_with_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_associate_service_action_with_provisioning_artifact(
        self, ServiceActionAssociations: List[Any], AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_disassociate_service_action_from_provisioning_artifact(
        self, ServiceActionAssociations: List[Any], AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def copy_product(
        self,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        TargetProductId: str = None,
        TargetProductName: str = None,
        SourceProvisioningArtifactIdentifiers: List[Any] = None,
        CopyOptions: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_constraint(
        self,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_portfolio(
        self,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_product(
        self,
        Name: str,
        Owner: str,
        ProductType: str,
        ProvisioningArtifactParameters: Dict[str, Any],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_provisioned_product_plan(
        self,
        PlanName: str,
        PlanType: str,
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        NotificationArns: List[Any] = None,
        PathId: str = None,
        ProvisioningParameters: List[Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_provisioning_artifact(
        self,
        ProductId: str,
        Parameters: Dict[str, Any],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_service_action(
        self,
        Name: str,
        DefinitionType: str,
        Definition: Dict[str, Any],
        IdempotencyToken: str,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_tag_option(self, Key: str, Value: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_provisioning_artifact(
        self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_service_action(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tag_option(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_constraint(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_copy_product_status(
        self, CopyProductToken: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_portfolio_share_status(
        self, PortfolioShareToken: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_product(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_product_as_admin(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_product_view(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_provisioned_product(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_provisioned_product_plan(
        self,
        PlanId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_provisioning_artifact(
        self,
        ProvisioningArtifactId: str,
        ProductId: str,
        AcceptLanguage: str = None,
        Verbose: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_provisioning_parameters(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        PathId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_record(
        self,
        Id: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_service_action(
        self, Id: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_service_action_execution_parameters(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tag_option(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_aws_organizations_access(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_budget_from_resource(
        self, BudgetName: str, ResourceId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_principal_from_portfolio(
        self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_product_from_portfolio(
        self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_service_action_from_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disassociate_tag_option_from_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_aws_organizations_access(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def execute_provisioned_product_plan(
        self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def execute_provisioned_product_service_action(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str = None,
        Parameters: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_aws_organizations_access_status(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_accepted_portfolio_shares(
        self,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
        PortfolioShareType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_budgets_for_resource(
        self,
        ResourceId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_constraints_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_launch_paths(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_organization_portfolio_access(
        self,
        PortfolioId: str,
        OrganizationNodeType: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_portfolio_access(
        self, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_portfolios(
        self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_portfolios_for_product(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_principals_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_provisioned_product_plans(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_provisioning_artifacts(
        self, ProductId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_provisioning_artifacts_for_service_action(
        self,
        ServiceActionId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_record_history(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        SearchFilter: Dict[str, Any] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_resources_for_tag_option(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_service_actions(
        self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_service_actions_for_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_stack_instances_for_provisioned_product(
        self,
        ProvisionedProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tag_options(
        self,
        Filters: Dict[str, Any] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def provision_product(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str = None,
        PathId: str = None,
        ProvisioningParameters: List[Any] = None,
        ProvisioningPreferences: Dict[str, Any] = None,
        Tags: List[Any] = None,
        NotificationArns: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reject_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def scan_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_products(
        self,
        AcceptLanguage: str = None,
        Filters: Dict[str, Any] = None,
        PageSize: int = None,
        SortBy: str = None,
        SortOrder: str = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_products_as_admin(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: str = None,
        PageToken: str = None,
        PageSize: int = None,
        ProductSource: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: Dict[str, Any] = None,
        Filters: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def terminate_provisioned_product(
        self,
        TerminateToken: str,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        IgnoreErrors: bool = None,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_constraint(
        self,
        Id: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Parameters: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_portfolio(
        self,
        Id: str,
        AcceptLanguage: str = None,
        DisplayName: str = None,
        Description: str = None,
        ProviderName: str = None,
        AddTags: List[Any] = None,
        RemoveTags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_product(
        self,
        Id: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Owner: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        AddTags: List[Any] = None,
        RemoveTags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_provisioned_product(
        self,
        UpdateToken: str,
        AcceptLanguage: str = None,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        ProductId: str = None,
        ProvisioningArtifactId: str = None,
        PathId: str = None,
        ProvisioningParameters: List[Any] = None,
        ProvisioningPreferences: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_provisioned_product_properties(
        self,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict[str, Any],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Description: str = None,
        Active: bool = None,
        Guidance: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_service_action(
        self,
        Id: str,
        Name: str = None,
        Definition: Dict[str, Any] = None,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_tag_option(
        self, Id: str, Value: str = None, Active: bool = None
    ) -> Dict[str, Any]:
        pass
