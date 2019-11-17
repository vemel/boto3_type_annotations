"Helper functions for iam service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_iam.client import Client
from mypy_boto3_iam.paginator import (
    GetAccountAuthorizationDetailsPaginator,
    GetGroupPaginator,
    ListAccessKeysPaginator,
    ListAccountAliasesPaginator,
    ListAttachedGroupPoliciesPaginator,
    ListAttachedRolePoliciesPaginator,
    ListAttachedUserPoliciesPaginator,
    ListEntitiesForPolicyPaginator,
    ListGroupPoliciesPaginator,
    ListGroupsForUserPaginator,
    ListGroupsPaginator,
    ListInstanceProfilesForRolePaginator,
    ListInstanceProfilesPaginator,
    ListMFADevicesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListSSHPublicKeysPaginator,
    ListServerCertificatesPaginator,
    ListSigningCertificatesPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
)
from mypy_boto3_iam.service_resource import ServiceResource
from mypy_boto3_iam.waiter import (
    InstanceProfileExistsWaiter,
    PolicyExistsWaiter,
    RoleExistsWaiter,
    UserExistsWaiter,
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
    Equivalent of `boto3.client('iam')`, returns a correct type.
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
        return session.client("iam", **kwargs)
    return boto3.client("iam", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_resource(
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
) -> ServiceResource:
    """
    Equivalent of `boto3.resource('iam')`, returns a correct type.
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
        return session.resource("iam", **kwargs)
    return boto3.resource("iam", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_account_authorization_details_paginator(
    client: Client,
) -> GetAccountAuthorizationDetailsPaginator:
    """
    Equivalent of `client.get_paginator('get_account_authorization_details')`, returns a correct type.
    """
    return client.get_paginator("get_account_authorization_details")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_group_paginator(client: Client) -> GetGroupPaginator:
    """
    Equivalent of `client.get_paginator('get_group')`, returns a correct type.
    """
    return client.get_paginator("get_group")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_access_keys_paginator(client: Client) -> ListAccessKeysPaginator:
    """
    Equivalent of `client.get_paginator('list_access_keys')`, returns a correct type.
    """
    return client.get_paginator("list_access_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_account_aliases_paginator(client: Client) -> ListAccountAliasesPaginator:
    """
    Equivalent of `client.get_paginator('list_account_aliases')`, returns a correct type.
    """
    return client.get_paginator("list_account_aliases")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attached_group_policies_paginator(
    client: Client,
) -> ListAttachedGroupPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_attached_group_policies')`, returns a correct type.
    """
    return client.get_paginator("list_attached_group_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attached_role_policies_paginator(
    client: Client,
) -> ListAttachedRolePoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_attached_role_policies')`, returns a correct type.
    """
    return client.get_paginator("list_attached_role_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_attached_user_policies_paginator(
    client: Client,
) -> ListAttachedUserPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_attached_user_policies')`, returns a correct type.
    """
    return client.get_paginator("list_attached_user_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_entities_for_policy_paginator(
    client: Client,
) -> ListEntitiesForPolicyPaginator:
    """
    Equivalent of `client.get_paginator('list_entities_for_policy')`, returns a correct type.
    """
    return client.get_paginator("list_entities_for_policy")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_group_policies_paginator(client: Client) -> ListGroupPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_group_policies')`, returns a correct type.
    """
    return client.get_paginator("list_group_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_groups_paginator(client: Client) -> ListGroupsPaginator:
    """
    Equivalent of `client.get_paginator('list_groups')`, returns a correct type.
    """
    return client.get_paginator("list_groups")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_groups_for_user_paginator(client: Client) -> ListGroupsForUserPaginator:
    """
    Equivalent of `client.get_paginator('list_groups_for_user')`, returns a correct type.
    """
    return client.get_paginator("list_groups_for_user")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instance_profiles_paginator(
    client: Client,
) -> ListInstanceProfilesPaginator:
    """
    Equivalent of `client.get_paginator('list_instance_profiles')`, returns a correct type.
    """
    return client.get_paginator("list_instance_profiles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_instance_profiles_for_role_paginator(
    client: Client,
) -> ListInstanceProfilesForRolePaginator:
    """
    Equivalent of `client.get_paginator('list_instance_profiles_for_role')`, returns a correct type.
    """
    return client.get_paginator("list_instance_profiles_for_role")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_mfa_devices_paginator(client: Client) -> ListMFADevicesPaginator:
    """
    Equivalent of `client.get_paginator('list_mfa_devices')`, returns a correct type.
    """
    return client.get_paginator("list_mfa_devices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policies_paginator(client: Client) -> ListPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_policies')`, returns a correct type.
    """
    return client.get_paginator("list_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_policy_versions_paginator(client: Client) -> ListPolicyVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_policy_versions')`, returns a correct type.
    """
    return client.get_paginator("list_policy_versions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_role_policies_paginator(client: Client) -> ListRolePoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_role_policies')`, returns a correct type.
    """
    return client.get_paginator("list_role_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_roles_paginator(client: Client) -> ListRolesPaginator:
    """
    Equivalent of `client.get_paginator('list_roles')`, returns a correct type.
    """
    return client.get_paginator("list_roles")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_ssh_public_keys_paginator(client: Client) -> ListSSHPublicKeysPaginator:
    """
    Equivalent of `client.get_paginator('list_ssh_public_keys')`, returns a correct type.
    """
    return client.get_paginator("list_ssh_public_keys")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_server_certificates_paginator(
    client: Client,
) -> ListServerCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('list_server_certificates')`, returns a correct type.
    """
    return client.get_paginator("list_server_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_signing_certificates_paginator(
    client: Client,
) -> ListSigningCertificatesPaginator:
    """
    Equivalent of `client.get_paginator('list_signing_certificates')`, returns a correct type.
    """
    return client.get_paginator("list_signing_certificates")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_user_policies_paginator(client: Client) -> ListUserPoliciesPaginator:
    """
    Equivalent of `client.get_paginator('list_user_policies')`, returns a correct type.
    """
    return client.get_paginator("list_user_policies")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_users_paginator(client: Client) -> ListUsersPaginator:
    """
    Equivalent of `client.get_paginator('list_users')`, returns a correct type.
    """
    return client.get_paginator("list_users")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_virtual_mfa_devices_paginator(
    client: Client,
) -> ListVirtualMFADevicesPaginator:
    """
    Equivalent of `client.get_paginator('list_virtual_mfa_devices')`, returns a correct type.
    """
    return client.get_paginator("list_virtual_mfa_devices")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_simulate_custom_policy_paginator(
    client: Client,
) -> SimulateCustomPolicyPaginator:
    """
    Equivalent of `client.get_paginator('simulate_custom_policy')`, returns a correct type.
    """
    return client.get_paginator("simulate_custom_policy")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_simulate_principal_policy_paginator(
    client: Client,
) -> SimulatePrincipalPolicyPaginator:
    """
    Equivalent of `client.get_paginator('simulate_principal_policy')`, returns a correct type.
    """
    return client.get_paginator("simulate_principal_policy")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_instance_profile_exists_waiter(client: Client) -> InstanceProfileExistsWaiter:
    """
    Equivalent of `client.get_waiter('instance_profile_exists')`, returns a correct type.
    """
    return client.get_waiter("instance_profile_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_policy_exists_waiter(client: Client) -> PolicyExistsWaiter:
    """
    Equivalent of `client.get_waiter('policy_exists')`, returns a correct type.
    """
    return client.get_waiter("policy_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_role_exists_waiter(client: Client) -> RoleExistsWaiter:
    """
    Equivalent of `client.get_waiter('role_exists')`, returns a correct type.
    """
    return client.get_waiter("role_exists")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_user_exists_waiter(client: Client) -> UserExistsWaiter:
    """
    Equivalent of `client.get_waiter('user_exists')`, returns a correct type.
    """
    return client.get_waiter("user_exists")
