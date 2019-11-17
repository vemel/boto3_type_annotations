"Helper functions for servicecatalog service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_servicecatalog.client import Client
from mypy_boto3_servicecatalog.paginator import (
    ListAcceptedPortfolioSharesPaginator,
    ListConstraintsForPortfolioPaginator,
    ListLaunchPathsPaginator,
    ListOrganizationPortfolioAccessPaginator,
    ListPortfoliosForProductPaginator,
    ListPortfoliosPaginator,
    ListPrincipalsForPortfolioPaginator,
    ListProvisionedProductPlansPaginator,
    ListProvisioningArtifactsForServiceActionPaginator,
    ListRecordHistoryPaginator,
    ListResourcesForTagOptionPaginator,
    ListServiceActionsForProvisioningArtifactPaginator,
    ListServiceActionsPaginator,
    ListTagOptionsPaginator,
    ScanProvisionedProductsPaginator,
    SearchProductsAsAdminPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('servicecatalog')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("servicecatalog", **kwargs)
    return boto3.client("servicecatalog", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_accepted_portfolio_shares_paginator(
    client: Client,
) -> ListAcceptedPortfolioSharesPaginator:
    """
    Equivalent of `client.get_paginator('list_accepted_portfolio_shares')`, returns a correct type.
    """
    return client.get_paginator("list_accepted_portfolio_shares")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_constraints_for_portfolio_paginator(
    client: Client,
) -> ListConstraintsForPortfolioPaginator:
    """
    Equivalent of `client.get_paginator('list_constraints_for_portfolio')`, returns a correct type.
    """
    return client.get_paginator("list_constraints_for_portfolio")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_launch_paths_paginator(client: Client) -> ListLaunchPathsPaginator:
    """
    Equivalent of `client.get_paginator('list_launch_paths')`, returns a correct type.
    """
    return client.get_paginator("list_launch_paths")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_organization_portfolio_access_paginator(
    client: Client,
) -> ListOrganizationPortfolioAccessPaginator:
    """
    Equivalent of `client.get_paginator('list_organization_portfolio_access')`, returns a correct type.
    """
    return client.get_paginator("list_organization_portfolio_access")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_portfolios_paginator(client: Client) -> ListPortfoliosPaginator:
    """
    Equivalent of `client.get_paginator('list_portfolios')`, returns a correct type.
    """
    return client.get_paginator("list_portfolios")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_portfolios_for_product_paginator(
    client: Client,
) -> ListPortfoliosForProductPaginator:
    """
    Equivalent of `client.get_paginator('list_portfolios_for_product')`, returns a correct type.
    """
    return client.get_paginator("list_portfolios_for_product")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_principals_for_portfolio_paginator(
    client: Client,
) -> ListPrincipalsForPortfolioPaginator:
    """
    Equivalent of `client.get_paginator('list_principals_for_portfolio')`, returns a correct type.
    """
    return client.get_paginator("list_principals_for_portfolio")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_provisioned_product_plans_paginator(
    client: Client,
) -> ListProvisionedProductPlansPaginator:
    """
    Equivalent of `client.get_paginator('list_provisioned_product_plans')`, returns a correct type.
    """
    return client.get_paginator("list_provisioned_product_plans")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_provisioning_artifacts_for_service_action_paginator(
    client: Client,
) -> ListProvisioningArtifactsForServiceActionPaginator:
    """
    Equivalent of `client.get_paginator('list_provisioning_artifacts_for_service_action')`, returns a correct type.
    """
    return client.get_paginator("list_provisioning_artifacts_for_service_action")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_record_history_paginator(client: Client) -> ListRecordHistoryPaginator:
    """
    Equivalent of `client.get_paginator('list_record_history')`, returns a correct type.
    """
    return client.get_paginator("list_record_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_resources_for_tag_option_paginator(
    client: Client,
) -> ListResourcesForTagOptionPaginator:
    """
    Equivalent of `client.get_paginator('list_resources_for_tag_option')`, returns a correct type.
    """
    return client.get_paginator("list_resources_for_tag_option")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_service_actions_paginator(client: Client) -> ListServiceActionsPaginator:
    """
    Equivalent of `client.get_paginator('list_service_actions')`, returns a correct type.
    """
    return client.get_paginator("list_service_actions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_service_actions_for_provisioning_artifact_paginator(
    client: Client,
) -> ListServiceActionsForProvisioningArtifactPaginator:
    """
    Equivalent of `client.get_paginator('list_service_actions_for_provisioning_artifact')`, returns a correct type.
    """
    return client.get_paginator("list_service_actions_for_provisioning_artifact")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tag_options_paginator(client: Client) -> ListTagOptionsPaginator:
    """
    Equivalent of `client.get_paginator('list_tag_options')`, returns a correct type.
    """
    return client.get_paginator("list_tag_options")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_scan_provisioned_products_paginator(
    client: Client,
) -> ScanProvisionedProductsPaginator:
    """
    Equivalent of `client.get_paginator('scan_provisioned_products')`, returns a correct type.
    """
    return client.get_paginator("scan_provisioned_products")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_search_products_as_admin_paginator(
    client: Client,
) -> SearchProductsAsAdminPaginator:
    """
    Equivalent of `client.get_paginator('search_products_as_admin')`, returns a correct type.
    """
    return client.get_paginator("search_products_as_admin")
