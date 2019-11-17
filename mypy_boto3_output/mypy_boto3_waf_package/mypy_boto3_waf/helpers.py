"Helper functions for waf service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_waf.client import Client
from mypy_boto3_waf.paginator import (
    GetRateBasedRuleManagedKeysPaginator,
    ListActivatedRulesInRuleGroupPaginator,
    ListByteMatchSetsPaginator,
    ListGeoMatchSetsPaginator,
    ListIPSetsPaginator,
    ListLoggingConfigurationsPaginator,
    ListRateBasedRulesPaginator,
    ListRegexMatchSetsPaginator,
    ListRegexPatternSetsPaginator,
    ListRuleGroupsPaginator,
    ListRulesPaginator,
    ListSizeConstraintSetsPaginator,
    ListSqlInjectionMatchSetsPaginator,
    ListSubscribedRuleGroupsPaginator,
    ListWebACLsPaginator,
    ListXssMatchSetsPaginator,
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
    Equivalent of `boto3.client('waf')`, returns a correct type.
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
        return session.client("waf", **kwargs)
    return boto3.client("waf", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_rate_based_rule_managed_keys_paginator(
    client: Client,
) -> GetRateBasedRuleManagedKeysPaginator:
    """
    Equivalent of `client.get_paginator('get_rate_based_rule_managed_keys')`, returns a correct type.
    """
    return client.get_paginator("get_rate_based_rule_managed_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_activated_rules_in_rule_group_paginator(
    client: Client,
) -> ListActivatedRulesInRuleGroupPaginator:
    """
    Equivalent of `client.get_paginator('list_activated_rules_in_rule_group')`, returns a correct type.
    """
    return client.get_paginator("list_activated_rules_in_rule_group")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_byte_match_sets_paginator(client: Client) -> ListByteMatchSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_byte_match_sets')`, returns a correct type.
    """
    return client.get_paginator("list_byte_match_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_geo_match_sets_paginator(client: Client) -> ListGeoMatchSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_geo_match_sets')`, returns a correct type.
    """
    return client.get_paginator("list_geo_match_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ip_sets_paginator(client: Client) -> ListIPSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_ip_sets')`, returns a correct type.
    """
    return client.get_paginator("list_ip_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_logging_configurations_paginator(
    client: Client,
) -> ListLoggingConfigurationsPaginator:
    """
    Equivalent of `client.get_paginator('list_logging_configurations')`, returns a correct type.
    """
    return client.get_paginator("list_logging_configurations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_rate_based_rules_paginator(client: Client) -> ListRateBasedRulesPaginator:
    """
    Equivalent of `client.get_paginator('list_rate_based_rules')`, returns a correct type.
    """
    return client.get_paginator("list_rate_based_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_regex_match_sets_paginator(client: Client) -> ListRegexMatchSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_regex_match_sets')`, returns a correct type.
    """
    return client.get_paginator("list_regex_match_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_regex_pattern_sets_paginator(
    client: Client,
) -> ListRegexPatternSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_regex_pattern_sets')`, returns a correct type.
    """
    return client.get_paginator("list_regex_pattern_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_rule_groups_paginator(client: Client) -> ListRuleGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_rule_groups')`, returns a correct type.
    """
    return client.get_paginator("list_rule_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_rules_paginator(client: Client) -> ListRulesPaginator:
    """
    Equivalent of `client.get_paginator('list_rules')`, returns a correct type.
    """
    return client.get_paginator("list_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_size_constraint_sets_paginator(
    client: Client,
) -> ListSizeConstraintSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_size_constraint_sets')`, returns a correct type.
    """
    return client.get_paginator("list_size_constraint_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_sql_injection_match_sets_paginator(
    client: Client,
) -> ListSqlInjectionMatchSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_sql_injection_match_sets')`, returns a correct type.
    """
    return client.get_paginator("list_sql_injection_match_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_subscribed_rule_groups_paginator(
    client: Client,
) -> ListSubscribedRuleGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_subscribed_rule_groups')`, returns a correct type.
    """
    return client.get_paginator("list_subscribed_rule_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_web_acls_paginator(client: Client) -> ListWebACLsPaginator:
    """
    Equivalent of `client.get_paginator('list_web_acls')`, returns a correct type.
    """
    return client.get_paginator("list_web_acls")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_xss_match_sets_paginator(client: Client) -> ListXssMatchSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_xss_match_sets')`, returns a correct type.
    """
    return client.get_paginator("list_xss_match_sets")
