"Main interface for config service"

from mypy_boto3_config.client import Client
from mypy_boto3_config.helpers import (
    boto3_client,
    get_describe_aggregate_compliance_by_config_rules_paginator,
    get_describe_aggregation_authorizations_paginator,
    get_describe_compliance_by_config_rule_paginator,
    get_describe_compliance_by_resource_paginator,
    get_describe_config_rule_evaluation_status_paginator,
    get_describe_config_rules_paginator,
    get_describe_configuration_aggregator_sources_status_paginator,
    get_describe_configuration_aggregators_paginator,
    get_describe_pending_aggregation_requests_paginator,
    get_describe_remediation_execution_status_paginator,
    get_describe_retention_configurations_paginator,
    get_get_aggregate_compliance_details_by_config_rule_paginator,
    get_get_compliance_details_by_config_rule_paginator,
    get_get_compliance_details_by_resource_paginator,
    get_get_resource_config_history_paginator,
    get_list_aggregate_discovered_resources_paginator,
    get_list_discovered_resources_paginator,
)


__all__ = (
    "Client",
    "boto3_client",
    "get_describe_aggregate_compliance_by_config_rules_paginator",
    "get_describe_aggregation_authorizations_paginator",
    "get_describe_compliance_by_config_rule_paginator",
    "get_describe_compliance_by_resource_paginator",
    "get_describe_config_rule_evaluation_status_paginator",
    "get_describe_config_rules_paginator",
    "get_describe_configuration_aggregator_sources_status_paginator",
    "get_describe_configuration_aggregators_paginator",
    "get_describe_pending_aggregation_requests_paginator",
    "get_describe_remediation_execution_status_paginator",
    "get_describe_retention_configurations_paginator",
    "get_get_aggregate_compliance_details_by_config_rule_paginator",
    "get_get_compliance_details_by_config_rule_paginator",
    "get_get_compliance_details_by_resource_paginator",
    "get_get_resource_config_history_paginator",
    "get_list_aggregate_discovered_resources_paginator",
    "get_list_discovered_resources_paginator",
)
