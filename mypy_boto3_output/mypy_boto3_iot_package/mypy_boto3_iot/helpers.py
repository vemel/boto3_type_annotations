"Helper functions for iot service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_iot.client import Client
from mypy_boto3_iot.paginator import (
    ListActiveViolationsPaginator,
    ListAttachedPoliciesPaginator,
    ListAuditFindingsPaginator,
    ListAuditTasksPaginator,
    ListAuthorizersPaginator,
    ListBillingGroupsPaginator,
    ListCACertificatesPaginator,
    ListCertificatesByCAPaginator,
    ListCertificatesPaginator,
    ListIndicesPaginator,
    ListJobExecutionsForJobPaginator,
    ListJobExecutionsForThingPaginator,
    ListJobsPaginator,
    ListOTAUpdatesPaginator,
    ListOutgoingCertificatesPaginator,
    ListPoliciesPaginator,
    ListPolicyPrincipalsPaginator,
    ListPrincipalPoliciesPaginator,
    ListPrincipalThingsPaginator,
    ListRoleAliasesPaginator,
    ListScheduledAuditsPaginator,
    ListSecurityProfilesForTargetPaginator,
    ListSecurityProfilesPaginator,
    ListStreamsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
    ListTargetsForSecurityProfilePaginator,
    ListThingGroupsForThingPaginator,
    ListThingGroupsPaginator,
    ListThingRegistrationTasksPaginator,
    ListThingTypesPaginator,
    ListThingsInBillingGroupPaginator,
    ListThingsInThingGroupPaginator,
    ListThingsPaginator,
    ListTopicRulesPaginator,
    ListV2LoggingLevelsPaginator,
    ListViolationEventsPaginator,
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
    Equivalent of `boto3.client('iot')`, returns a correct type.
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
        return session.client("iot", **kwargs)
    return boto3.client("iot", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_active_violations_paginator(
    client: Client,
) -> ListActiveViolationsPaginator:
    """
    Equivalent of `client.get_paginator('list_active_violations')`, returns a correct type.
    """
    return client.get_paginator("list_active_violations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attached_policies_paginator(
    client: Client,
) -> ListAttachedPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_attached_policies')`, returns a correct type.
    """
    return client.get_paginator("list_attached_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_audit_findings_paginator(client: Client) -> ListAuditFindingsPaginator:
    """
    Equivalent of `client.get_paginator('list_audit_findings')`, returns a correct type.
    """
    return client.get_paginator("list_audit_findings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_audit_tasks_paginator(client: Client) -> ListAuditTasksPaginator:
    """
    Equivalent of `client.get_paginator('list_audit_tasks')`, returns a correct type.
    """
    return client.get_paginator("list_audit_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_authorizers_paginator(client: Client) -> ListAuthorizersPaginator:
    """
    Equivalent of `client.get_paginator('list_authorizers')`, returns a correct type.
    """
    return client.get_paginator("list_authorizers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_billing_groups_paginator(client: Client) -> ListBillingGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_billing_groups')`, returns a correct type.
    """
    return client.get_paginator("list_billing_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ca_certificates_paginator(client: Client) -> ListCACertificatesPaginator:
    """
    Equivalent of `client.get_paginator('list_ca_certificates')`, returns a correct type.
    """
    return client.get_paginator("list_ca_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_certificates_paginator(client: Client) -> ListCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('list_certificates')`, returns a correct type.
    """
    return client.get_paginator("list_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_certificates_by_ca_paginator(
    client: Client,
) -> ListCertificatesByCAPaginator:
    """
    Equivalent of `client.get_paginator('list_certificates_by_ca')`, returns a correct type.
    """
    return client.get_paginator("list_certificates_by_ca")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_indices_paginator(client: Client) -> ListIndicesPaginator:
    """
    Equivalent of `client.get_paginator('list_indices')`, returns a correct type.
    """
    return client.get_paginator("list_indices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_job_executions_for_job_paginator(
    client: Client,
) -> ListJobExecutionsForJobPaginator:
    """
    Equivalent of `client.get_paginator('list_job_executions_for_job')`, returns a correct type.
    """
    return client.get_paginator("list_job_executions_for_job")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_job_executions_for_thing_paginator(
    client: Client,
) -> ListJobExecutionsForThingPaginator:
    """
    Equivalent of `client.get_paginator('list_job_executions_for_thing')`, returns a correct type.
    """
    return client.get_paginator("list_job_executions_for_thing")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_jobs_paginator(client: Client) -> ListJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ota_updates_paginator(client: Client) -> ListOTAUpdatesPaginator:
    """
    Equivalent of `client.get_paginator('list_ota_updates')`, returns a correct type.
    """
    return client.get_paginator("list_ota_updates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_outgoing_certificates_paginator(
    client: Client,
) -> ListOutgoingCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('list_outgoing_certificates')`, returns a correct type.
    """
    return client.get_paginator("list_outgoing_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policies_paginator(client: Client) -> ListPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_policies')`, returns a correct type.
    """
    return client.get_paginator("list_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policy_principals_paginator(
    client: Client,
) -> ListPolicyPrincipalsPaginator:
    """
    Equivalent of `client.get_paginator('list_policy_principals')`, returns a correct type.
    """
    return client.get_paginator("list_policy_principals")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_principal_policies_paginator(
    client: Client,
) -> ListPrincipalPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_principal_policies')`, returns a correct type.
    """
    return client.get_paginator("list_principal_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_principal_things_paginator(client: Client) -> ListPrincipalThingsPaginator:
    """
    Equivalent of `client.get_paginator('list_principal_things')`, returns a correct type.
    """
    return client.get_paginator("list_principal_things")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_role_aliases_paginator(client: Client) -> ListRoleAliasesPaginator:
    """
    Equivalent of `client.get_paginator('list_role_aliases')`, returns a correct type.
    """
    return client.get_paginator("list_role_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_scheduled_audits_paginator(client: Client) -> ListScheduledAuditsPaginator:
    """
    Equivalent of `client.get_paginator('list_scheduled_audits')`, returns a correct type.
    """
    return client.get_paginator("list_scheduled_audits")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_security_profiles_paginator(
    client: Client,
) -> ListSecurityProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_security_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_security_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_security_profiles_for_target_paginator(
    client: Client,
) -> ListSecurityProfilesForTargetPaginator:
    """
    Equivalent of `client.get_paginator('list_security_profiles_for_target')`, returns a correct type.
    """
    return client.get_paginator("list_security_profiles_for_target")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_streams_paginator(client: Client) -> ListStreamsPaginator:
    """
    Equivalent of `client.get_paginator('list_streams')`, returns a correct type.
    """
    return client.get_paginator("list_streams")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_tags_for_resource_paginator(
    client: Client,
) -> ListTagsForResourcePaginator:
    """
    Equivalent of `client.get_paginator('list_tags_for_resource')`, returns a correct type.
    """
    return client.get_paginator("list_tags_for_resource")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_targets_for_policy_paginator(
    client: Client,
) -> ListTargetsForPolicyPaginator:
    """
    Equivalent of `client.get_paginator('list_targets_for_policy')`, returns a correct type.
    """
    return client.get_paginator("list_targets_for_policy")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_targets_for_security_profile_paginator(
    client: Client,
) -> ListTargetsForSecurityProfilePaginator:
    """
    Equivalent of `client.get_paginator('list_targets_for_security_profile')`, returns a correct type.
    """
    return client.get_paginator("list_targets_for_security_profile")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_thing_groups_paginator(client: Client) -> ListThingGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_thing_groups')`, returns a correct type.
    """
    return client.get_paginator("list_thing_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_thing_groups_for_thing_paginator(
    client: Client,
) -> ListThingGroupsForThingPaginator:
    """
    Equivalent of `client.get_paginator('list_thing_groups_for_thing')`, returns a correct type.
    """
    return client.get_paginator("list_thing_groups_for_thing")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_thing_registration_tasks_paginator(
    client: Client,
) -> ListThingRegistrationTasksPaginator:
    """
    Equivalent of `client.get_paginator('list_thing_registration_tasks')`, returns a correct type.
    """
    return client.get_paginator("list_thing_registration_tasks")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_thing_types_paginator(client: Client) -> ListThingTypesPaginator:
    """
    Equivalent of `client.get_paginator('list_thing_types')`, returns a correct type.
    """
    return client.get_paginator("list_thing_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_things_paginator(client: Client) -> ListThingsPaginator:
    """
    Equivalent of `client.get_paginator('list_things')`, returns a correct type.
    """
    return client.get_paginator("list_things")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_things_in_billing_group_paginator(
    client: Client,
) -> ListThingsInBillingGroupPaginator:
    """
    Equivalent of `client.get_paginator('list_things_in_billing_group')`, returns a correct type.
    """
    return client.get_paginator("list_things_in_billing_group")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_things_in_thing_group_paginator(
    client: Client,
) -> ListThingsInThingGroupPaginator:
    """
    Equivalent of `client.get_paginator('list_things_in_thing_group')`, returns a correct type.
    """
    return client.get_paginator("list_things_in_thing_group")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_topic_rules_paginator(client: Client) -> ListTopicRulesPaginator:
    """
    Equivalent of `client.get_paginator('list_topic_rules')`, returns a correct type.
    """
    return client.get_paginator("list_topic_rules")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_v2_logging_levels_paginator(
    client: Client,
) -> ListV2LoggingLevelsPaginator:
    """
    Equivalent of `client.get_paginator('list_v2_logging_levels')`, returns a correct type.
    """
    return client.get_paginator("list_v2_logging_levels")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_violation_events_paginator(client: Client) -> ListViolationEventsPaginator:
    """
    Equivalent of `client.get_paginator('list_violation_events')`, returns a correct type.
    """
    return client.get_paginator("list_violation_events")
