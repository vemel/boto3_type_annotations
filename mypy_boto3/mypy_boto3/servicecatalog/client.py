from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def accept_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        PortfolioShareType: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_budget_with_resource(
        self,
        BudgetName: str,
        ResourceId: str,
    ) -> Dict:
        pass


    def associate_principal_with_portfolio(
        self,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_product_with_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        SourcePortfolioId: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_service_action_with_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def associate_tag_option_with_resource(
        self,
        ResourceId: str,
        TagOptionId: str,
    ) -> Dict:
        pass


    def batch_associate_service_action_with_provisioning_artifact(
        self,
        ServiceActionAssociations: List,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        ServiceActionAssociations: List,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def copy_product(
        self,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
        TargetProductId: Optional[str] = None,
        TargetProductName: Optional[str] = None,
        SourceProvisioningArtifactIdentifiers: Optional[List] = None,
        CopyOptions: Optional[List] = None,
    ) -> Dict:
        pass


    def create_constraint(
        self,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
        Description: Optional[str] = None,
    ) -> Dict:
        pass


    def create_portfolio(
        self,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
        Description: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        AccountId: Optional[str] = None,
        OrganizationNode: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_product(
        self,
        Name: str,
        Owner: str,
        ProductType: str,
        ProvisioningArtifactParameters: Dict,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
        Description: Optional[str] = None,
        Distributor: Optional[str] = None,
        SupportDescription: Optional[str] = None,
        SupportEmail: Optional[str] = None,
        SupportUrl: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_provisioned_product_plan(
        self,
        PlanName: str,
        PlanType: str,
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
        NotificationArns: Optional[List] = None,
        PathId: Optional[str] = None,
        ProvisioningParameters: Optional[List] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_provisioning_artifact(
        self,
        ProductId: str,
        Parameters: Dict,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def create_service_action(
        self,
        Name: str,
        DefinitionType: str,
        Definition: Dict,
        IdempotencyToken: str,
        Description: Optional[str] = None,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def create_tag_option(
        self,
        Key: str,
        Value: str,
    ) -> Dict:
        pass


    def delete_constraint(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_portfolio(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        AccountId: Optional[str] = None,
        OrganizationNode: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_product(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_provisioned_product_plan(
        self,
        PlanId: str,
        AcceptLanguage: Optional[str] = None,
        IgnoreErrors: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_service_action(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_tag_option(
        self,
        Id: str,
    ) -> Dict:
        pass


    def describe_constraint(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_copy_product_status(
        self,
        CopyProductToken: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_portfolio(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_portfolio_share_status(
        self,
        PortfolioShareToken: str,
    ) -> Dict:
        pass


    def describe_product(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_product_as_admin(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_product_view(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_provisioned_product(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_provisioned_product_plan(
        self,
        PlanId: str,
        AcceptLanguage: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_provisioning_artifact(
        self,
        ProvisioningArtifactId: str,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
        Verbose: Optional[bool] = None,
    ) -> Dict:
        pass


    def describe_provisioning_parameters(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: Optional[str] = None,
        PathId: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_record(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_service_action(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_service_action_execution_parameters(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_tag_option(
        self,
        Id: str,
    ) -> Dict:
        pass


    def disable_aws_organizations_access(
        self,
    ) -> Dict:
        pass


    def disassociate_budget_from_resource(
        self,
        BudgetName: str,
        ResourceId: str,
    ) -> Dict:
        pass


    def disassociate_principal_from_portfolio(
        self,
        PortfolioId: str,
        PrincipalARN: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_product_from_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_service_action_from_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def disassociate_tag_option_from_resource(
        self,
        ResourceId: str,
        TagOptionId: str,
    ) -> Dict:
        pass


    def enable_aws_organizations_access(
        self,
    ) -> Dict:
        pass


    def execute_provisioned_product_plan(
        self,
        PlanId: str,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def execute_provisioned_product_service_action(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: Optional[str] = None,
        Parameters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_aws_organizations_access_status(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_accepted_portfolio_shares(
        self,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
        PortfolioShareType: Optional[str] = None,
    ) -> Dict:
        pass


    def list_budgets_for_resource(
        self,
        ResourceId: str,
        AcceptLanguage: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_constraints_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        ProductId: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_launch_paths(
        self,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_organization_portfolio_access(
        self,
        PortfolioId: str,
        OrganizationNodeType: str,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_portfolio_access(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def list_portfolios(
        self,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_portfolios_for_product(
        self,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_principals_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_provisioned_product_plans(
        self,
        AcceptLanguage: Optional[str] = None,
        ProvisionProductId: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_provisioning_artifacts(
        self,
        ProductId: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def list_provisioning_artifacts_for_service_action(
        self,
        ServiceActionId: str,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def list_record_history(
        self,
        AcceptLanguage: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        SearchFilter: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_resources_for_tag_option(
        self,
        TagOptionId: str,
        ResourceType: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_service_actions(
        self,
        AcceptLanguage: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_service_actions_for_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def list_stack_instances_for_provisioned_product(
        self,
        ProvisionedProductId: str,
        AcceptLanguage: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tag_options(
        self,
        Filters: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def provision_product(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: Optional[str] = None,
        PathId: Optional[str] = None,
        ProvisioningParameters: Optional[List] = None,
        ProvisioningPreferences: Optional[Dict] = None,
        Tags: Optional[List] = None,
        NotificationArns: Optional[List] = None,
    ) -> Dict:
        pass


    def reject_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: Optional[str] = None,
        PortfolioShareType: Optional[str] = None,
    ) -> Dict:
        pass


    def scan_provisioned_products(
        self,
        AcceptLanguage: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def search_products(
        self,
        AcceptLanguage: Optional[str] = None,
        Filters: Optional[Dict] = None,
        PageSize: Optional[int] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def search_products_as_admin(
        self,
        AcceptLanguage: Optional[str] = None,
        PortfolioId: Optional[str] = None,
        Filters: Optional[Dict] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PageToken: Optional[str] = None,
        PageSize: Optional[int] = None,
        ProductSource: Optional[str] = None,
    ) -> Dict:
        pass


    def search_provisioned_products(
        self,
        AcceptLanguage: Optional[str] = None,
        AccessLevelFilter: Optional[Dict] = None,
        Filters: Optional[Dict] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        PageSize: Optional[int] = None,
        PageToken: Optional[str] = None,
    ) -> Dict:
        pass


    def terminate_provisioned_product(
        self,
        TerminateToken: str,
        ProvisionedProductName: Optional[str] = None,
        ProvisionedProductId: Optional[str] = None,
        IgnoreErrors: Optional[bool] = None,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def update_constraint(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
        Description: Optional[str] = None,
        Parameters: Optional[str] = None,
    ) -> Dict:
        pass


    def update_portfolio(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
        DisplayName: Optional[str] = None,
        Description: Optional[str] = None,
        ProviderName: Optional[str] = None,
        AddTags: Optional[List] = None,
        RemoveTags: Optional[List] = None,
    ) -> Dict:
        pass


    def update_product(
        self,
        Id: str,
        AcceptLanguage: Optional[str] = None,
        Name: Optional[str] = None,
        Owner: Optional[str] = None,
        Description: Optional[str] = None,
        Distributor: Optional[str] = None,
        SupportDescription: Optional[str] = None,
        SupportEmail: Optional[str] = None,
        SupportUrl: Optional[str] = None,
        AddTags: Optional[List] = None,
        RemoveTags: Optional[List] = None,
    ) -> Dict:
        pass


    def update_provisioned_product(
        self,
        UpdateToken: str,
        AcceptLanguage: Optional[str] = None,
        ProvisionedProductName: Optional[str] = None,
        ProvisionedProductId: Optional[str] = None,
        ProductId: Optional[str] = None,
        ProvisioningArtifactId: Optional[str] = None,
        PathId: Optional[str] = None,
        ProvisioningParameters: Optional[List] = None,
        ProvisioningPreferences: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def update_provisioned_product_properties(
        self,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict,
        IdempotencyToken: str,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def update_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: Optional[str] = None,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        Active: Optional[bool] = None,
        Guidance: Optional[str] = None,
    ) -> Dict:
        pass


    def update_service_action(
        self,
        Id: str,
        Name: Optional[str] = None,
        Definition: Optional[Dict] = None,
        Description: Optional[str] = None,
        AcceptLanguage: Optional[str] = None,
    ) -> Dict:
        pass


    def update_tag_option(
        self,
        Id: str,
        Value: Optional[str] = None,
        Active: Optional[bool] = None,
    ) -> Dict:
        pass

