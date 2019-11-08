"Main interface for iam service"

from mypy_boto3.iam.client import Client
from mypy_boto3.iam.service_resource import AccessKey
from mypy_boto3.iam.service_resource import AccessKeyPair
from mypy_boto3.iam.service_resource import AccountPasswordPolicy
from mypy_boto3.iam.service_resource import AccountSummary
from mypy_boto3.iam.service_resource import AssumeRolePolicy
from mypy_boto3.iam.service_resource import CurrentUser
from mypy_boto3.iam.service_resource import Group
from mypy_boto3.iam.service_resource import GroupPolicy
from mypy_boto3.iam.service_resource import InstanceProfile
from mypy_boto3.iam.service_resource import LoginProfile
from mypy_boto3.iam.service_resource import MfaDevice
from mypy_boto3.iam.service_resource import Policy
from mypy_boto3.iam.service_resource import PolicyVersion
from mypy_boto3.iam.service_resource import Role
from mypy_boto3.iam.service_resource import RolePolicy
from mypy_boto3.iam.service_resource import SamlProvider
from mypy_boto3.iam.service_resource import ServerCertificate
from mypy_boto3.iam.service_resource import ServiceResource
from mypy_boto3.iam.service_resource import SigningCertificate
from mypy_boto3.iam.service_resource import User
from mypy_boto3.iam.service_resource import UserPolicy
from mypy_boto3.iam.service_resource import VirtualMfaDevice
from mypy_boto3.iam.service_resource import access_keys
from mypy_boto3.iam.service_resource import attached_groups
from mypy_boto3.iam.service_resource import attached_policies
from mypy_boto3.iam.service_resource import attached_roles
from mypy_boto3.iam.service_resource import attached_users
from mypy_boto3.iam.service_resource import groups
from mypy_boto3.iam.service_resource import instance_profiles
from mypy_boto3.iam.service_resource import mfa_devices
from mypy_boto3.iam.service_resource import policies
from mypy_boto3.iam.service_resource import roles
from mypy_boto3.iam.service_resource import saml_providers
from mypy_boto3.iam.service_resource import server_certificates
from mypy_boto3.iam.service_resource import signing_certificates
from mypy_boto3.iam.service_resource import users
from mypy_boto3.iam.service_resource import versions
from mypy_boto3.iam.service_resource import virtual_mfa_devices

__all__ = (
    "Client",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "ServiceResource",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "access_keys",
    "attached_groups",
    "attached_policies",
    "attached_roles",
    "attached_users",
    "groups",
    "instance_profiles",
    "mfa_devices",
    "policies",
    "roles",
    "saml_providers",
    "server_certificates",
    "signing_certificates",
    "users",
    "versions",
    "virtual_mfa_devices",
)
