"Helper functions for config service"

from typing import Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_config.client import Client
from mypy_boto3_config.paginator import (
    DescribeAggregateComplianceByConfigRulesPaginator,
    DescribeAggregationAuthorizationsPaginator,
    DescribeComplianceByConfigRulePaginator,
    DescribeComplianceByResourcePaginator,
    DescribeConfigRuleEvaluationStatusPaginator,
    DescribeConfigRulesPaginator,
    DescribeConfigurationAggregatorSourcesStatusPaginator,
    DescribeConfigurationAggregatorsPaginator,
    DescribePendingAggregationRequestsPaginator,
    DescribeRemediationExecutionStatusPaginator,
    DescribeRetentionConfigurationsPaginator,
    GetAggregateComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByResourcePaginator,
    GetResourceConfigHistoryPaginator,
    ListAggregateDiscoveredResourcesPaginator,
    ListDiscoveredResourcesPaginator,
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
    Equivalent of `boto3.client('config')`, returns a correct type.
    """
    kwargs = {}
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
        return session.client("config", **kwargs)
    return boto3.client("config", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_aggregate_compliance_by_config_rules_paginator(
    client: Client,
) -> DescribeAggregateComplianceByConfigRulesPaginator:
    """
    Equivalent of `client.get_paginator('describe_aggregate_compliance_by_config_rules')`, returns a correct type.
    """
    return client.get_waiter("describe_aggregate_compliance_by_config_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_aggregation_authorizations_paginator(
    client: Client,
) -> DescribeAggregationAuthorizationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_aggregation_authorizations')`, returns a correct type.
    """
    return client.get_waiter("describe_aggregation_authorizations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_compliance_by_config_rule_paginator(
    client: Client,
) -> DescribeComplianceByConfigRulePaginator:
    """
    Equivalent of `client.get_paginator('describe_compliance_by_config_rule')`, returns a correct type.
    """
    return client.get_waiter("describe_compliance_by_config_rule")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_compliance_by_resource_paginator(
    client: Client,
) -> DescribeComplianceByResourcePaginator:
    """
    Equivalent of `client.get_paginator('describe_compliance_by_resource')`, returns a correct type.
    """
    return client.get_waiter("describe_compliance_by_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_config_rule_evaluation_status_paginator(
    client: Client,
) -> DescribeConfigRuleEvaluationStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_config_rule_evaluation_status')`, returns a correct type.
    """
    return client.get_waiter("describe_config_rule_evaluation_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_config_rules_paginator(client: Client) -> DescribeConfigRulesPaginator:
    """
    Equivalent of `client.get_paginator('describe_config_rules')`, returns a correct type.
    """
    return client.get_waiter("describe_config_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_configuration_aggregator_sources_status_paginator(
    client: Client,
) -> DescribeConfigurationAggregatorSourcesStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_configuration_aggregator_sources_status')`, returns a correct type.
    """
    return client.get_waiter("describe_configuration_aggregator_sources_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_configuration_aggregators_paginator(
    client: Client,
) -> DescribeConfigurationAggregatorsPaginator:
    """
    Equivalent of `client.get_paginator('describe_configuration_aggregators')`, returns a correct type.
    """
    return client.get_waiter("describe_configuration_aggregators")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_pending_aggregation_requests_paginator(
    client: Client,
) -> DescribePendingAggregationRequestsPaginator:
    """
    Equivalent of `client.get_paginator('describe_pending_aggregation_requests')`, returns a correct type.
    """
    return client.get_waiter("describe_pending_aggregation_requests")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_remediation_execution_status_paginator(
    client: Client,
) -> DescribeRemediationExecutionStatusPaginator:
    """
    Equivalent of `client.get_paginator('describe_remediation_execution_status')`, returns a correct type.
    """
    return client.get_waiter("describe_remediation_execution_status")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_retention_configurations_paginator(
    client: Client,
) -> DescribeRetentionConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_retention_configurations')`, returns a correct type.
    """
    return client.get_waiter("describe_retention_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_aggregate_compliance_details_by_config_rule_paginator(
    client: Client,
) -> GetAggregateComplianceDetailsByConfigRulePaginator:
    """
    Equivalent of `client.get_paginator('get_aggregate_compliance_details_by_config_rule')`, returns a correct type.
    """
    return client.get_waiter("get_aggregate_compliance_details_by_config_rule")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_compliance_details_by_config_rule_paginator(
    client: Client,
) -> GetComplianceDetailsByConfigRulePaginator:
    """
    Equivalent of `client.get_paginator('get_compliance_details_by_config_rule')`, returns a correct type.
    """
    return client.get_waiter("get_compliance_details_by_config_rule")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_compliance_details_by_resource_paginator(
    client: Client,
) -> GetComplianceDetailsByResourcePaginator:
    """
    Equivalent of `client.get_paginator('get_compliance_details_by_resource')`, returns a correct type.
    """
    return client.get_waiter("get_compliance_details_by_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_resource_config_history_paginator(
    client: Client,
) -> GetResourceConfigHistoryPaginator:
    """
    Equivalent of `client.get_paginator('get_resource_config_history')`, returns a correct type.
    """
    return client.get_waiter("get_resource_config_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_aggregate_discovered_resources_paginator(
    client: Client,
) -> ListAggregateDiscoveredResourcesPaginator:
    """
    Equivalent of `client.get_paginator('list_aggregate_discovered_resources')`, returns a correct type.
    """
    return client.get_waiter("list_aggregate_discovered_resources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_discovered_resources_paginator(
    client: Client,
) -> ListDiscoveredResourcesPaginator:
    """
    Equivalent of `client.get_paginator('list_discovered_resources')`, returns a correct type.
    """
    return client.get_waiter("list_discovered_resources")