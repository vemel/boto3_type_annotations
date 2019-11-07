"Main interface for iam service"

from mypy_boto3.iam.client import Client
from mypy_boto3.iam.service_resource import attached_roles
from mypy_boto3.iam.service_resource import attached_users
from mypy_boto3.iam.service_resource import policies
from mypy_boto3.iam.service_resource import attached_groups
from mypy_boto3.iam.service_resource import CurrentUser
from mypy_boto3.iam.service_resource import access_keys
from mypy_boto3.iam.service_resource import RolePolicy
from mypy_boto3.iam.service_resource import LoginProfile
from mypy_boto3.iam.service_resource import AccessKeyPair
from mypy_boto3.iam.service_resource import MfaDevice
from mypy_boto3.iam.service_resource import GroupPolicy
from mypy_boto3.iam.service_resource import server_certificates
from mypy_boto3.iam.service_resource import virtual_mfa_devices
from mypy_boto3.iam.service_resource import AccountPasswordPolicy
from mypy_boto3.iam.service_resource import SamlProvider
from mypy_boto3.iam.service_resource import versions
from mypy_boto3.iam.service_resource import InstanceProfile
from mypy_boto3.iam.service_resource import groups
from mypy_boto3.iam.service_resource import saml_providers
from mypy_boto3.iam.service_resource import users
from mypy_boto3.iam.service_resource import Policy
from mypy_boto3.iam.service_resource import Role
from mypy_boto3.iam.service_resource import roles
from mypy_boto3.iam.service_resource import AccountSummary
from mypy_boto3.iam.service_resource import UserPolicy
from mypy_boto3.iam.service_resource import mfa_devices
from mypy_boto3.iam.service_resource import attached_policies
from mypy_boto3.iam.service_resource import AssumeRolePolicy
from mypy_boto3.iam.service_resource import signing_certificates
from mypy_boto3.iam.service_resource import AccessKey
from mypy_boto3.iam.service_resource import User
from mypy_boto3.iam.service_resource import SigningCertificate
from mypy_boto3.iam.service_resource import ServiceResource
from mypy_boto3.iam.service_resource import Group
from mypy_boto3.iam.service_resource import PolicyVersion
from mypy_boto3.iam.service_resource import ServerCertificate
from mypy_boto3.iam.service_resource import VirtualMfaDevice
from mypy_boto3.iam.service_resource import instance_profiles

__all__ = (
    "Client",
    "attached_roles",
    "attached_users",
    "policies",
    "attached_groups",
    "CurrentUser",
    "access_keys",
    "RolePolicy",
    "LoginProfile",
    "AccessKeyPair",
    "MfaDevice",
    "GroupPolicy",
    "server_certificates",
    "virtual_mfa_devices",
    "AccountPasswordPolicy",
    "SamlProvider",
    "versions",
    "InstanceProfile",
    "groups",
    "saml_providers",
    "users",
    "Policy",
    "Role",
    "roles",
    "AccountSummary",
    "UserPolicy",
    "mfa_devices",
    "attached_policies",
    "AssumeRolePolicy",
    "signing_certificates",
    "AccessKey",
    "User",
    "SigningCertificate",
    "ServiceResource",
    "Group",
    "PolicyVersion",
    "ServerCertificate",
    "VirtualMfaDevice",
    "instance_profiles",
)
