"Main interface for iam type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAccessKeyResponseAccessKeyTypeDef",
    "ClientCreateAccessKeyResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    "ClientCreateInstanceProfileResponseTypeDef",
    "ClientCreateLoginProfileResponseLoginProfileTypeDef",
    "ClientCreateLoginProfileResponseTypeDef",
    "ClientCreateOpenIdConnectProviderResponseTypeDef",
    "ClientCreatePolicyResponsePolicyTypeDef",
    "ClientCreatePolicyResponseTypeDef",
    "ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    "ClientCreatePolicyVersionResponseTypeDef",
    "ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateRoleResponseRoleTagsTypeDef",
    "ClientCreateRoleResponseRoleTypeDef",
    "ClientCreateRoleResponseTypeDef",
    "ClientCreateRoleTagsTypeDef",
    "ClientCreateSamlProviderResponseTypeDef",
    "ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef",
    "ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    "ClientCreateServiceLinkedRoleResponseTypeDef",
    "ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientCreateServiceSpecificCredentialResponseTypeDef",
    "ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    "ClientCreateUserResponseUserTagsTypeDef",
    "ClientCreateUserResponseUserTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    "ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    "ClientCreateVirtualMfaDeviceResponseTypeDef",
    "ClientDeleteServiceLinkedRoleResponseTypeDef",
    "ClientGenerateCredentialReportResponseTypeDef",
    "ClientGenerateOrganizationsAccessReportResponseTypeDef",
    "ClientGenerateServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    "ClientGetAccessKeyLastUsedResponseTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    "ClientGetAccountAuthorizationDetailsResponseTypeDef",
    "ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    "ClientGetAccountPasswordPolicyResponseTypeDef",
    "ClientGetAccountSummaryResponseTypeDef",
    "ClientGetContextKeysForCustomPolicyResponseTypeDef",
    "ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    "ClientGetCredentialReportResponseTypeDef",
    "ClientGetGroupPolicyResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    "ClientGetGroupResponseUsersTagsTypeDef",
    "ClientGetGroupResponseUsersTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    "ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    "ClientGetInstanceProfileResponseTypeDef",
    "ClientGetLoginProfileResponseLoginProfileTypeDef",
    "ClientGetLoginProfileResponseTypeDef",
    "ClientGetOpenIdConnectProviderResponseTypeDef",
    "ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    "ClientGetOrganizationsAccessReportResponseTypeDef",
    "ClientGetPolicyResponsePolicyTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    "ClientGetPolicyVersionResponseTypeDef",
    "ClientGetRolePolicyResponseTypeDef",
    "ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    "ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    "ClientGetRoleResponseRoleTagsTypeDef",
    "ClientGetRoleResponseRoleTypeDef",
    "ClientGetRoleResponseTypeDef",
    "ClientGetSamlProviderResponseTypeDef",
    "ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    "ClientGetServerCertificateResponseServerCertificateTypeDef",
    "ClientGetServerCertificateResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    "ClientGetServiceLastAccessedDetailsResponseTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    "ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    "ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientGetSshPublicKeyResponseTypeDef",
    "ClientGetUserPolicyResponseTypeDef",
    "ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    "ClientGetUserResponseUserTagsTypeDef",
    "ClientGetUserResponseUserTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    "ClientListAccessKeysResponseTypeDef",
    "ClientListAccountAliasesResponseTypeDef",
    "ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedGroupPoliciesResponseTypeDef",
    "ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedRolePoliciesResponseTypeDef",
    "ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    "ClientListAttachedUserPoliciesResponseTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    "ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    "ClientListEntitiesForPolicyResponseTypeDef",
    "ClientListGroupPoliciesResponseTypeDef",
    "ClientListGroupsForUserResponseGroupsTypeDef",
    "ClientListGroupsForUserResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesForRoleResponseTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    "ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    "ClientListInstanceProfilesResponseTypeDef",
    "ClientListMfaDevicesResponseMFADevicesTypeDef",
    "ClientListMfaDevicesResponseTypeDef",
    "ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    "ClientListOpenIdConnectProvidersResponseTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    "ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    "ClientListPoliciesResponsePoliciesTypeDef",
    "ClientListPoliciesResponseTypeDef",
    "ClientListPolicyVersionsResponseVersionsTypeDef",
    "ClientListPolicyVersionsResponseTypeDef",
    "ClientListRolePoliciesResponseTypeDef",
    "ClientListRoleTagsResponseTagsTypeDef",
    "ClientListRoleTagsResponseTypeDef",
    "ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    "ClientListRolesResponseRolesRoleLastUsedTypeDef",
    "ClientListRolesResponseRolesTagsTypeDef",
    "ClientListRolesResponseRolesTypeDef",
    "ClientListRolesResponseTypeDef",
    "ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    "ClientListSamlProvidersResponseTypeDef",
    "ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    "ClientListServerCertificatesResponseTypeDef",
    "ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    "ClientListServiceSpecificCredentialsResponseTypeDef",
    "ClientListSigningCertificatesResponseCertificatesTypeDef",
    "ClientListSigningCertificatesResponseTypeDef",
    "ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    "ClientListSshPublicKeysResponseTypeDef",
    "ClientListUserPoliciesResponseTypeDef",
    "ClientListUserTagsResponseTagsTypeDef",
    "ClientListUserTagsResponseTypeDef",
    "ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    "ClientListUsersResponseUsersTagsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    "ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    "ClientListVirtualMfaDevicesResponseTypeDef",
    "ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    "ClientResetServiceSpecificCredentialResponseTypeDef",
    "ClientSimulateCustomPolicyContextEntriesTypeDef",
    "ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    "ClientTagRoleTagsTypeDef",
    "ClientTagUserTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTagsTypeDef",
    "ClientUpdateRoleDescriptionResponseRoleTypeDef",
    "ClientUpdateRoleDescriptionResponseTypeDef",
    "ClientUpdateSamlProviderResponseTypeDef",
    "ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    "ClientUploadServerCertificateResponseTypeDef",
    "ClientUploadSigningCertificateResponseCertificateTypeDef",
    "ClientUploadSigningCertificateResponseTypeDef",
    "ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    "ClientUploadSshPublicKeyResponseTypeDef",
    "GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef",
    "GetAccountAuthorizationDetailsPaginateResponseTypeDef",
    "GetGroupPaginatePaginationConfigTypeDef",
    "GetGroupPaginateResponseGroupTypeDef",
    "GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef",
    "GetGroupPaginateResponseUsersTagsTypeDef",
    "GetGroupPaginateResponseUsersTypeDef",
    "GetGroupPaginateResponseTypeDef",
    "InstanceProfileExistsWaitWaiterConfigTypeDef",
    "ListAccessKeysPaginatePaginationConfigTypeDef",
    "ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef",
    "ListAccessKeysPaginateResponseTypeDef",
    "ListAccountAliasesPaginatePaginationConfigTypeDef",
    "ListAccountAliasesPaginateResponseTypeDef",
    "ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedGroupPoliciesPaginateResponseTypeDef",
    "ListAttachedRolePoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedRolePoliciesPaginateResponseTypeDef",
    "ListAttachedUserPoliciesPaginatePaginationConfigTypeDef",
    "ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef",
    "ListAttachedUserPoliciesPaginateResponseTypeDef",
    "ListEntitiesForPolicyPaginatePaginationConfigTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef",
    "ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef",
    "ListEntitiesForPolicyPaginateResponseTypeDef",
    "ListGroupPoliciesPaginatePaginationConfigTypeDef",
    "ListGroupPoliciesPaginateResponseTypeDef",
    "ListGroupsForUserPaginatePaginationConfigTypeDef",
    "ListGroupsForUserPaginateResponseGroupsTypeDef",
    "ListGroupsForUserPaginateResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListInstanceProfilesForRolePaginatePaginationConfigTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef",
    "ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef",
    "ListInstanceProfilesForRolePaginateResponseTypeDef",
    "ListInstanceProfilesPaginatePaginationConfigTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef",
    "ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef",
    "ListInstanceProfilesPaginateResponseTypeDef",
    "ListMFADevicesPaginatePaginationConfigTypeDef",
    "ListMFADevicesPaginateResponseMFADevicesTypeDef",
    "ListMFADevicesPaginateResponseTypeDef",
    "ListPoliciesPaginatePaginationConfigTypeDef",
    "ListPoliciesPaginateResponsePoliciesTypeDef",
    "ListPoliciesPaginateResponseTypeDef",
    "ListPolicyVersionsPaginatePaginationConfigTypeDef",
    "ListPolicyVersionsPaginateResponseVersionsTypeDef",
    "ListPolicyVersionsPaginateResponseTypeDef",
    "ListRolePoliciesPaginatePaginationConfigTypeDef",
    "ListRolePoliciesPaginateResponseTypeDef",
    "ListRolesPaginatePaginationConfigTypeDef",
    "ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef",
    "ListRolesPaginateResponseRolesRoleLastUsedTypeDef",
    "ListRolesPaginateResponseRolesTagsTypeDef",
    "ListRolesPaginateResponseRolesTypeDef",
    "ListRolesPaginateResponseTypeDef",
    "ListSSHPublicKeysPaginatePaginationConfigTypeDef",
    "ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef",
    "ListSSHPublicKeysPaginateResponseTypeDef",
    "ListServerCertificatesPaginatePaginationConfigTypeDef",
    "ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef",
    "ListServerCertificatesPaginateResponseTypeDef",
    "ListSigningCertificatesPaginatePaginationConfigTypeDef",
    "ListSigningCertificatesPaginateResponseCertificatesTypeDef",
    "ListSigningCertificatesPaginateResponseTypeDef",
    "ListUserPoliciesPaginatePaginationConfigTypeDef",
    "ListUserPoliciesPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef",
    "ListUsersPaginateResponseUsersTagsTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
    "ListVirtualMFADevicesPaginatePaginationConfigTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef",
    "ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef",
    "ListVirtualMFADevicesPaginateResponseTypeDef",
    "PolicyExistsWaitWaiterConfigTypeDef",
    "RoleExistsWaitWaiterConfigTypeDef",
    "SamlProviderUpdateResponseTypeDef",
    "ServiceResourceCreateRoleTagsTypeDef",
    "ServiceResourceCreateUserTagsTypeDef",
    "SimulateCustomPolicyPaginateContextEntriesTypeDef",
    "SimulateCustomPolicyPaginatePaginationConfigTypeDef",
    "SimulatePrincipalPolicyPaginateContextEntriesTypeDef",
    "SimulatePrincipalPolicyPaginatePaginationConfigTypeDef",
    "UserCreateTagsTypeDef",
    "UserExistsWaitWaiterConfigTypeDef",
)


_ClientCreateAccessKeyResponseAccessKeyTypeDef = TypedDict(
    "_ClientCreateAccessKeyResponseAccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": str,
        "SecretAccessKey": str,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientCreateAccessKeyResponseAccessKeyTypeDef(
    _ClientCreateAccessKeyResponseAccessKeyTypeDef
):
    """
    Type definition for `ClientCreateAccessKeyResponse` `AccessKey`

    A structure with details about the access key.

    - **UserName** *(string) --*

      The name of the IAM user that the access key is associated with.

    - **AccessKeyId** *(string) --*

      The ID for this access key.

    - **Status** *(string) --*

      The status of the access key. ``Active`` means that the key is valid for API calls, while
      ``Inactive`` means it is not.

    - **SecretAccessKey** *(string) --*

      The secret key used to sign requests.

    - **CreateDate** *(datetime) --*

      The date when the access key was created.
    """


_ClientCreateAccessKeyResponseTypeDef = TypedDict(
    "_ClientCreateAccessKeyResponseTypeDef",
    {"AccessKey": ClientCreateAccessKeyResponseAccessKeyTypeDef},
    total=False,
)


class ClientCreateAccessKeyResponseTypeDef(_ClientCreateAccessKeyResponseTypeDef):
    """
    Type definition for `ClientCreateAccessKey` `Response`

    Contains the response to a successful  CreateAccessKey request.

    - **AccessKey** *(dict) --*

      A structure with details about the access key.

      - **UserName** *(string) --*

        The name of the IAM user that the access key is associated with.

      - **AccessKeyId** *(string) --*

        The ID for this access key.

      - **Status** *(string) --*

        The status of the access key. ``Active`` means that the key is valid for API calls, while
        ``Inactive`` means it is not.

      - **SecretAccessKey** *(string) --*

        The secret key used to sign requests.

      - **CreateDate** *(datetime) --*

        The date when the access key was created.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientCreateGroupResponse` `Group`

    A structure containing details about the new group.

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the group was created.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    Contains the response to a successful  CreateGroup request.

    - **Group** *(dict) --*

      A structure containing details about the new group.

      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **GroupName** *(string) --*

        The friendly name that identifies the group.

      - **GroupId** *(string) --*

        The stable and unique string identifying the group. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
        how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the group was created.
    """


_ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfileResponseInstanceProfileRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used
      as the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfileResponseInstanceProfileRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfileResponseInstanceProfileRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store
        an array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientCreateInstanceProfileResponseInstanceProfileRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientCreateInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfileResponseInstanceProfile` `Roles`

    Contains information about an IAM role. This structure is returned as a response element
    in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used
        as the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store
            an array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientCreateInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientCreateInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)


class ClientCreateInstanceProfileResponseInstanceProfileTypeDef(
    _ClientCreateInstanceProfileResponseInstanceProfileTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfileResponse` `InstanceProfile`

    A structure containing details about the new instance profile.

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information about
      ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response element
        in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used
            as the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store
                an array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ClientCreateInstanceProfileResponseTypeDef = TypedDict(
    "_ClientCreateInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientCreateInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)


class ClientCreateInstanceProfileResponseTypeDef(
    _ClientCreateInstanceProfileResponseTypeDef
):
    """
    Type definition for `ClientCreateInstanceProfile` `Response`

    Contains the response to a successful  CreateInstanceProfile request.

    - **InstanceProfile** *(dict) --*

      A structure containing details about the new instance profile.

      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **InstanceProfileName** *(string) --*

        The name identifying the instance profile.

      - **InstanceProfileId** *(string) --*

        The stable and unique string identifying the instance profile. For more information about
        IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the instance profile. For more information about
        ARNs and how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date when the instance profile was created.

      - **Roles** *(list) --*

        The role associated with the instance profile.

        - *(dict) --*

          Contains information about an IAM role. This structure is returned as a response element
          in several API operations that interact with roles.

          - **Path** *(string) --*

            The path to the role. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **RoleName** *(string) --*

            The friendly name that identifies the role.

          - **RoleId** *(string) --*

            The stable and unique string identifying the role. For more information about IDs, see
            `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
            how to use them in policies, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* guide.

          - **CreateDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the role was created.

          - **AssumeRolePolicyDocument** *(string) --*

            The policy that grants an entity permission to assume the role.

          - **Description** *(string) --*

            A description of the role that you provide.

          - **MaxSessionDuration** *(integer) --*

            The maximum session duration (in seconds) for the specified role. Anyone who uses the
            AWS CLI, or API to assume the role can specify the duration using the optional
            ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

          - **PermissionsBoundary** *(dict) --*

            The ARN of the policy used to set the permissions boundary for the role.

            For more information about permissions boundaries, see `Permissions Boundaries for IAM
            Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
            in the *IAM User Guide* .

            - **PermissionsBoundaryType** *(string) --*

              The permissions boundary usage type that indicates what type of IAM resource is used
              as the permissions boundary for an entity. This data type can only have a value of
              ``Policy`` .

            - **PermissionsBoundaryArn** *(string) --*

              The ARN of the policy used to set the permissions boundary for the user or role.

          - **Tags** *(list) --*

            A list of tags that are attached to the specified role. For more information about
            tagging, see `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - *(dict) --*

              A structure that represents user-provided metadata that can be associated with a
              resource such as an IAM user or role. For more information about tagging, see
              `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - **Key** *(string) --*

                The key name that can be used to look up or retrieve the associated value. For
                example, ``Department`` or ``Cost Center`` are common choices.

              - **Value** *(string) --*

                The value associated with this tag. For example, tags with a key name of
                ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
                ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                consist of the number associated with the different cost centers in your company.
                Typically, many resources have tags with the same key name but with different
                values.

                .. note::

                  AWS always interprets the tag ``Value`` as a single string. If you need to store
                  an array, you can store comma-separated values in the string. However, you must
                  interpret the value in your code.

          - **RoleLastUsed** *(dict) --*

            Contains information about the last time that an IAM role was used. This includes the
            date and time and the Region in which the role was last used. Activity is only reported
            for the trailing 400 days. This period can be shorter if your Region began supporting
            these features within the last year. The role might have been used more than 400 days
            ago. For more information, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

            - **LastUsedDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              that the role was last used.

              This field is null if the role has not been used within the IAM tracking period. For
              more information about the tracking period, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

            - **Region** *(string) --*

              The name of the AWS Region in which the role was last used.
    """


_ClientCreateLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "_ClientCreateLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)


class ClientCreateLoginProfileResponseLoginProfileTypeDef(
    _ClientCreateLoginProfileResponseLoginProfileTypeDef
):
    """
    Type definition for `ClientCreateLoginProfileResponse` `LoginProfile`

    A structure containing the user name and password create date.

    - **UserName** *(string) --*

      The name of the user, which can be used for signing in to the AWS Management Console.

    - **CreateDate** *(datetime) --*

      The date when the password for the user was created.

    - **PasswordResetRequired** *(boolean) --*

      Specifies whether the user is required to set a new password on next sign-in.
    """


_ClientCreateLoginProfileResponseTypeDef = TypedDict(
    "_ClientCreateLoginProfileResponseTypeDef",
    {"LoginProfile": ClientCreateLoginProfileResponseLoginProfileTypeDef},
    total=False,
)


class ClientCreateLoginProfileResponseTypeDef(_ClientCreateLoginProfileResponseTypeDef):
    """
    Type definition for `ClientCreateLoginProfile` `Response`

    Contains the response to a successful  CreateLoginProfile request.

    - **LoginProfile** *(dict) --*

      A structure containing the user name and password create date.

      - **UserName** *(string) --*

        The name of the user, which can be used for signing in to the AWS Management Console.

      - **CreateDate** *(datetime) --*

        The date when the password for the user was created.

      - **PasswordResetRequired** *(boolean) --*

        Specifies whether the user is required to set a new password on next sign-in.
    """


_ClientCreateOpenIdConnectProviderResponseTypeDef = TypedDict(
    "_ClientCreateOpenIdConnectProviderResponseTypeDef",
    {"OpenIDConnectProviderArn": str},
    total=False,
)


class ClientCreateOpenIdConnectProviderResponseTypeDef(
    _ClientCreateOpenIdConnectProviderResponseTypeDef
):
    """
    Type definition for `ClientCreateOpenIdConnectProvider` `Response`

    Contains the response to a successful  CreateOpenIDConnectProvider request.

    - **OpenIDConnectProviderArn** *(string) --*

      The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For
      more information, see  OpenIDConnectProviderListEntry .
    """


_ClientCreatePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientCreatePolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientCreatePolicyResponsePolicyTypeDef(_ClientCreatePolicyResponsePolicyTypeDef):
    """
    Type definition for `ClientCreatePolicyResponse` `Policy`

    A structure containing details about the new policy.

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      in the *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default version.

    - **AttachmentCount** *(integer) --*

      The number of entities (users, groups, and roles) that the policy is attached to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used to set the
      permissions boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

      This element is included in the response to the  GetPolicy operation. It is not included in
      the response to the  ListPolicies operation.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and time
      when the most recent policy version was created.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {"Policy": ClientCreatePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    Type definition for `ClientCreatePolicy` `Response`

    Contains the response to a successful  CreatePolicy request.

    - **Policy** *(dict) --*

      A structure containing details about the new policy.

      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.

      - **PolicyId** *(string) --*

        The stable and unique string identifying the policy.

        For more information about IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

        For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
        Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        in the *AWS General Reference* .

      - **Path** *(string) --*

        The path to the policy.

        For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **DefaultVersionId** *(string) --*

        The identifier for the version of the policy that is set as the default version.

      - **AttachmentCount** *(integer) --*

        The number of entities (users, groups, and roles) that the policy is attached to.

      - **PermissionsBoundaryUsageCount** *(integer) --*

        The number of entities (users and roles) for which the policy is used to set the
        permissions boundary.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

      - **IsAttachable** *(boolean) --*

        Specifies whether the policy can be attached to an IAM user, group, or role.

      - **Description** *(string) --*

        A friendly description of the policy.

        This element is included in the response to the  GetPolicy operation. It is not included in
        the response to the  ListPolicies operation.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy was created.

      - **UpdateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy was last updated.

        When a policy has only one version, this field contains the date and time when the policy
        was created. When a policy has more than one version, this field contains the date and time
        when the most recent policy version was created.
    """


_ClientCreatePolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponsePolicyVersionTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientCreatePolicyVersionResponsePolicyVersionTypeDef(
    _ClientCreatePolicyVersionResponsePolicyVersionTypeDef
):
    """
    Type definition for `ClientCreatePolicyVersionResponse` `PolicyVersion`

    A structure containing details about the new policy version.

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC 3986
      <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
      policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
      method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
      SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
      created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy version was created.
    """


_ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientCreatePolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)


class ClientCreatePolicyVersionResponseTypeDef(
    _ClientCreatePolicyVersionResponseTypeDef
):
    """
    Type definition for `ClientCreatePolicyVersion` `Response`

    Contains the response to a successful  CreatePolicyVersion request.

    - **PolicyVersion** *(dict) --*

      A structure containing details about the new policy version.

      - **Document** *(string) --*

        The policy document.

        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.

        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.

      - **VersionId** *(string) --*

        The identifier for the policy version.

        Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
        created, the first policy version is ``v1`` .

      - **IsDefaultVersion** *(boolean) --*

        Specifies whether the policy version is set as the policy's default version.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy version was created.
    """


_ClientCreateRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientCreateRoleResponseRolePermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientCreateRoleResponseRole` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientCreateRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateRoleResponseRoleRoleLastUsedTypeDef(
    _ClientCreateRoleResponseRoleRoleLastUsedTypeDef
):
    """
    Type definition for `ClientCreateRoleResponseRole` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the date
    and time and the Region in which the role was last used. Activity is only reported for the
    trailing 400 days. This period can be shorter if your Region began supporting these
    features within the last year. The role might have been used more than 400 days ago. For
    more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
      the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For more
      information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientCreateRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRoleResponseRoleTagsTypeDef(_ClientCreateRoleResponseRoleTagsTypeDef):
    """
    Type definition for `ClientCreateRoleResponseRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientCreateRoleResponseRoleTypeDef = TypedDict(
    "_ClientCreateRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateRoleResponseRoleTypeDef(_ClientCreateRoleResponseRoleTypeDef):
    """
    Type definition for `ClientCreateRoleResponse` `Role`

    A structure containing details about the new role.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
      to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about tagging,
      see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the date
      and time and the Region in which the role was last used. Activity is only reported for the
      trailing 400 days. This period can be shorter if your Region began supporting these
      features within the last year. The role might have been used more than 400 days ago. For
      more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
        the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For more
        information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientCreateRoleResponseTypeDef = TypedDict(
    "_ClientCreateRoleResponseTypeDef",
    {"Role": ClientCreateRoleResponseRoleTypeDef},
    total=False,
)


class ClientCreateRoleResponseTypeDef(_ClientCreateRoleResponseTypeDef):
    """
    Type definition for `ClientCreateRole` `Response`

    Contains the response to a successful  CreateRole request.

    - **Role** *(dict) --*

      A structure containing details about the new role.

      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **RoleName** *(string) --*

        The friendly name that identifies the role.

      - **RoleId** *(string) --*

        The stable and unique string identifying the role. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
        to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* guide.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the role was created.

      - **AssumeRolePolicyDocument** *(string) --*

        The policy that grants an entity permission to assume the role.

      - **Description** *(string) --*

        A description of the role that you provide.

      - **MaxSessionDuration** *(integer) --*

        The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
        CLI, or API to assume the role can specify the duration using the optional
        ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the role.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are attached to the specified role. For more information about tagging,
        see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

      - **RoleLastUsed** *(dict) --*

        Contains information about the last time that an IAM role was used. This includes the date
        and time and the Region in which the role was last used. Activity is only reported for the
        trailing 400 days. This period can be shorter if your Region began supporting these
        features within the last year. The role might have been used more than 400 days ago. For
        more information, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

        - **LastUsedDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
          the role was last used.

          This field is null if the role has not been used within the IAM tracking period. For more
          information about the tracking period, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

        - **Region** *(string) --*

          The name of the AWS Region in which the role was last used.
    """


_ClientCreateRoleTagsTypeDef = TypedDict(
    "_ClientCreateRoleTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateRoleTagsTypeDef(_ClientCreateRoleTagsTypeDef):
    """
    Type definition for `ClientCreateRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_ClientCreateSamlProviderResponseTypeDef = TypedDict(
    "_ClientCreateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class ClientCreateSamlProviderResponseTypeDef(_ClientCreateSamlProviderResponseTypeDef):
    """
    Type definition for `ClientCreateSamlProvider` `Response`

    Contains the response to a successful  CreateSAMLProvider request.

    - **SAMLProviderArn** *(string) --*

      The Amazon Resource Name (ARN) of the new SAML provider resource in IAM.
    """


_ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientCreateServiceLinkedRoleResponseRole` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef
):
    """
    Type definition for `ClientCreateServiceLinkedRoleResponseRole` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the date
    and time and the Region in which the role was last used. Activity is only reported for the
    trailing 400 days. This period can be shorter if your Region began supporting these
    features within the last year. The role might have been used more than 400 days ago. For
    more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
      the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For more
      information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef
):
    """
    Type definition for `ClientCreateServiceLinkedRoleResponseRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientCreateServiceLinkedRoleResponseRoleTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientCreateServiceLinkedRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateServiceLinkedRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientCreateServiceLinkedRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientCreateServiceLinkedRoleResponseRoleTypeDef(
    _ClientCreateServiceLinkedRoleResponseRoleTypeDef
):
    """
    Type definition for `ClientCreateServiceLinkedRoleResponse` `Role`

    A  Role object that contains details about the newly created role.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
      to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about tagging,
      see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the date
      and time and the Region in which the role was last used. Activity is only reported for the
      trailing 400 days. This period can be shorter if your Region began supporting these
      features within the last year. The role might have been used more than 400 days ago. For
      more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
        the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For more
        information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientCreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "_ClientCreateServiceLinkedRoleResponseTypeDef",
    {"Role": ClientCreateServiceLinkedRoleResponseRoleTypeDef},
    total=False,
)


class ClientCreateServiceLinkedRoleResponseTypeDef(
    _ClientCreateServiceLinkedRoleResponseTypeDef
):
    """
    Type definition for `ClientCreateServiceLinkedRole` `Response`

    - **Role** *(dict) --*

      A  Role object that contains details about the newly created role.

      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **RoleName** *(string) --*

        The friendly name that identifies the role.

      - **RoleId** *(string) --*

        The stable and unique string identifying the role. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
        to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* guide.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the role was created.

      - **AssumeRolePolicyDocument** *(string) --*

        The policy that grants an entity permission to assume the role.

      - **Description** *(string) --*

        A description of the role that you provide.

      - **MaxSessionDuration** *(integer) --*

        The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
        CLI, or API to assume the role can specify the duration using the optional
        ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the role.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are attached to the specified role. For more information about tagging,
        see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

      - **RoleLastUsed** *(dict) --*

        Contains information about the last time that an IAM role was used. This includes the date
        and time and the Region in which the role was last used. Activity is only reported for the
        trailing 400 days. This period can be shorter if your Region began supporting these
        features within the last year. The role might have been used more than 400 days ago. For
        more information, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

        - **LastUsedDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
          the role was last used.

          This field is null if the role has not been used within the IAM tracking period. For more
          information about the tracking period, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

        - **Region** *(string) --*

          The name of the AWS Region in which the role was last used.
    """


_ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "_ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": str,
    },
    total=False,
)


class ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef(
    _ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
):
    """
    Type definition for `ClientCreateServiceSpecificCredentialResponse` `ServiceSpecificCredential`

    A structure that contains information about the newly created service-specific credential.

    .. warning::

      This is the only time that the password for this credential set is available. It cannot be
      recovered later. Instead, you must reset the password with  ResetServiceSpecificCredential .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the service-specific credential were created.

    - **ServiceName** *(string) --*

      The name of the service associated with the service-specific credential.

    - **ServiceUserName** *(string) --*

      The generated user name for the service-specific credential. This value is generated by
      combining the IAM user's name combined with the ID number of the AWS account, as in
      ``jane-at-123456789012`` , for example. This value cannot be configured by the user.

    - **ServicePassword** *(string) --*

      The generated password for the service-specific credential.

    - **ServiceSpecificCredentialId** *(string) --*

      The unique identifier for the service-specific credential.

    - **UserName** *(string) --*

      The name of the IAM user associated with the service-specific credential.

    - **Status** *(string) --*

      The status of the service-specific credential. ``Active`` means that the key is valid for
      API calls, while ``Inactive`` means it is not.
    """


_ClientCreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "_ClientCreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientCreateServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)


class ClientCreateServiceSpecificCredentialResponseTypeDef(
    _ClientCreateServiceSpecificCredentialResponseTypeDef
):
    """
    Type definition for `ClientCreateServiceSpecificCredential` `Response`

    - **ServiceSpecificCredential** *(dict) --*

      A structure that contains information about the newly created service-specific credential.

      .. warning::

        This is the only time that the password for this credential set is available. It cannot be
        recovered later. Instead, you must reset the password with  ResetServiceSpecificCredential .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the service-specific credential were created.

      - **ServiceName** *(string) --*

        The name of the service associated with the service-specific credential.

      - **ServiceUserName** *(string) --*

        The generated user name for the service-specific credential. This value is generated by
        combining the IAM user's name combined with the ID number of the AWS account, as in
        ``jane-at-123456789012`` , for example. This value cannot be configured by the user.

      - **ServicePassword** *(string) --*

        The generated password for the service-specific credential.

      - **ServiceSpecificCredentialId** *(string) --*

        The unique identifier for the service-specific credential.

      - **UserName** *(string) --*

        The name of the IAM user associated with the service-specific credential.

      - **Status** *(string) --*

        The status of the service-specific credential. ``Active`` means that the key is valid for
        API calls, while ``Inactive`` means it is not.
    """


_ClientCreateUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateUserResponseUserPermissionsBoundaryTypeDef(
    _ClientCreateUserResponseUserPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientCreateUserResponseUser` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientCreateUserResponseUserTagsTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateUserResponseUserTagsTypeDef(_ClientCreateUserResponseUserTagsTypeDef):
    """
    Type definition for `ClientCreateUserResponseUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientCreateUserResponseUserTypeDef = TypedDict(
    "_ClientCreateUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientCreateUserResponseUserTagsTypeDef],
    },
    total=False,
)


class ClientCreateUserResponseUserTypeDef(_ClientCreateUserResponseUserTypeDef):
    """
    Type definition for `ClientCreateUserResponse` `User`

    A structure with details about the new IAM user.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the user's password was last used to sign in to an AWS website. For a list of AWS websites
      that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the
      *IAM User Guide* . If a password is used more than once in a five-minute span, only the
      first use is returned in this field. If the field is null (no value), then it indicates
      that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does not
      currently have a password but had one in the past, then this field contains the date and
      time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef",
    {"User": ClientCreateUserResponseUserTypeDef},
    total=False,
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    Contains the response to a successful  CreateUser request.

    - **User** *(dict) --*

      A structure with details about the new IAM user.

      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **UserName** *(string) --*

        The friendly name identifying the user.

      - **UserId** *(string) --*

        The stable and unique string identifying the user. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
        and how to use ARNs in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the user was created.

      - **PasswordLastUsed** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the user's password was last used to sign in to an AWS website. For a list of AWS websites
        that capture a user's last sign-in time, see the `Credential Reports
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the
        *IAM User Guide* . If a password is used more than once in a five-minute span, only the
        first use is returned in this field. If the field is null (no value), then it indicates
        that they never signed in with a password. This can be because:

        * The user never had a password.

        * A password exists but has not been used since IAM started tracking this information on
        October 20, 2014.

        A null value does not mean that the user *never* had a password. Also, if the user does not
        currently have a password but had one in the past, then this field contains the date and
        time the most recent password was used.

        This value is returned only in the  GetUser and  ListUsers operations.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the user.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are associated with the specified user. For more information about
        tagging, see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.
    """


_ClientCreateUserTagsTypeDef = TypedDict(
    "_ClientCreateUserTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateUserTagsTypeDef(_ClientCreateUserTagsTypeDef):
    """
    Type definition for `ClientCreateUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUser` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef
):
    """
    Type definition for `ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTagsTypeDef
        ],
    },
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef
):
    """
    Type definition for `ClientCreateVirtualMfaDeviceResponseVirtualMFADevice` `User`

    The IAM user associated with this virtual MFA device.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the date
      and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef(
    _ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef
):
    """
    Type definition for `ClientCreateVirtualMfaDeviceResponse` `VirtualMFADevice`

    A structure containing details about the new virtual MFA device.

    - **SerialNumber** *(string) --*

      The serial number associated with ``VirtualMFADevice`` .

    - **Base32StringSeed** *(bytes) --*

      The base32 seed defined as specified in `RFC3548
      <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

    - **QRCodePNG** *(bytes) --*

      A QR code PNG image that encodes
      ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
      ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the user
      name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed in
      base32 format. The ``Base32String`` value is base64-encoded.

    - **User** *(dict) --*

      The IAM user associated with this virtual MFA device.

      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **UserName** *(string) --*

        The friendly name identifying the user.

      - **UserId** *(string) --*

        The stable and unique string identifying the user. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
        and how to use ARNs in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user was created.

      - **PasswordLastUsed** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user's password was last used to sign in to an AWS website. For a list of AWS
        websites that capture a user's last sign-in time, see the `Credential Reports
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
        the *IAM User Guide* . If a password is used more than once in a five-minute span, only
        the first use is returned in this field. If the field is null (no value), then it
        indicates that they never signed in with a password. This can be because:

        * The user never had a password.

        * A password exists but has not been used since IAM started tracking this information on
        October 20, 2014.

        A null value does not mean that the user *never* had a password. Also, if the user does
        not currently have a password but had one in the past, then this field contains the date
        and time the most recent password was used.

        This value is returned only in the  GetUser and  ListUsers operations.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the user.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are associated with the specified user. For more information about
        tagging, see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a
          resource such as an IAM user or role. For more information about tagging, see `Tagging
          IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
          the *IAM User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For
            example, ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of
            ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
            ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
            of the number associated with the different cost centers in your company. Typically,
            many resources have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

    - **EnableDate** *(datetime) --*

      The date and time on which the virtual MFA device was enabled.
    """


_ClientCreateVirtualMfaDeviceResponseTypeDef = TypedDict(
    "_ClientCreateVirtualMfaDeviceResponseTypeDef",
    {"VirtualMFADevice": ClientCreateVirtualMfaDeviceResponseVirtualMFADeviceTypeDef},
    total=False,
)


class ClientCreateVirtualMfaDeviceResponseTypeDef(
    _ClientCreateVirtualMfaDeviceResponseTypeDef
):
    """
    Type definition for `ClientCreateVirtualMfaDevice` `Response`

    Contains the response to a successful  CreateVirtualMFADevice request.

    - **VirtualMFADevice** *(dict) --*

      A structure containing details about the new virtual MFA device.

      - **SerialNumber** *(string) --*

        The serial number associated with ``VirtualMFADevice`` .

      - **Base32StringSeed** *(bytes) --*

        The base32 seed defined as specified in `RFC3548
        <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

      - **QRCodePNG** *(bytes) --*

        A QR code PNG image that encodes
        ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
        ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the user
        name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed in
        base32 format. The ``Base32String`` value is base64-encoded.

      - **User** *(dict) --*

        The IAM user associated with this virtual MFA device.

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
          and how to use ARNs in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **PasswordLastUsed** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user's password was last used to sign in to an AWS website. For a list of AWS
          websites that capture a user's last sign-in time, see the `Credential Reports
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
          the *IAM User Guide* . If a password is used more than once in a five-minute span, only
          the first use is returned in this field. If the field is null (no value), then it
          indicates that they never signed in with a password. This can be because:

          * The user never had a password.

          * A password exists but has not been used since IAM started tracking this information on
          October 20, 2014.

          A null value does not mean that the user *never* had a password. Also, if the user does
          not currently have a password but had one in the past, then this field contains the date
          and time the most recent password was used.

          This value is returned only in the  GetUser and  ListUsers operations.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

      - **EnableDate** *(datetime) --*

        The date and time on which the virtual MFA device was enabled.
    """


_ClientDeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "_ClientDeleteServiceLinkedRoleResponseTypeDef",
    {"DeletionTaskId": str},
    total=False,
)


class ClientDeleteServiceLinkedRoleResponseTypeDef(
    _ClientDeleteServiceLinkedRoleResponseTypeDef
):
    """
    Type definition for `ClientDeleteServiceLinkedRole` `Response`

    - **DeletionTaskId** *(string) --*

      The deletion task identifier that you can use to check the status of the deletion. This
      identifier is returned in the format
      ``task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid>`` .
    """


_ClientGenerateCredentialReportResponseTypeDef = TypedDict(
    "_ClientGenerateCredentialReportResponseTypeDef",
    {"State": str, "Description": str},
    total=False,
)


class ClientGenerateCredentialReportResponseTypeDef(
    _ClientGenerateCredentialReportResponseTypeDef
):
    """
    Type definition for `ClientGenerateCredentialReport` `Response`

    Contains the response to a successful  GenerateCredentialReport request.

    - **State** *(string) --*

      Information about the state of the credential report.

    - **Description** *(string) --*

      Information about the credential report.
    """


_ClientGenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "_ClientGenerateOrganizationsAccessReportResponseTypeDef",
    {"JobId": str},
    total=False,
)


class ClientGenerateOrganizationsAccessReportResponseTypeDef(
    _ClientGenerateOrganizationsAccessReportResponseTypeDef
):
    """
    Type definition for `ClientGenerateOrganizationsAccessReport` `Response`

    - **JobId** *(string) --*

      The job identifier that you can use in the  GetOrganizationsAccessReport operation.
    """


_ClientGenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "_ClientGenerateServiceLastAccessedDetailsResponseTypeDef",
    {"JobId": str},
    total=False,
)


class ClientGenerateServiceLastAccessedDetailsResponseTypeDef(
    _ClientGenerateServiceLastAccessedDetailsResponseTypeDef
):
    """
    Type definition for `ClientGenerateServiceLastAccessedDetails` `Response`

    - **JobId** *(string) --*

      The job ID that you can use in the  GetServiceLastAccessedDetails or
      GetServiceLastAccessedDetailsWithEntities operations.
    """


_ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef = TypedDict(
    "_ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef",
    {"LastUsedDate": datetime, "ServiceName": str, "Region": str},
    total=False,
)


class ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef(
    _ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef
):
    """
    Type definition for `ClientGetAccessKeyLastUsedResponse` `AccessKeyLastUsed`

    Contains information about the last time the access key was used.

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the access key was most recently used. This field is null in the following situations:

      * The user does not have an access key.

      * An access key exists but has not been used since IAM began tracking this information.

      * There is no sign-in data associated with the user.

    - **ServiceName** *(string) --*

      The name of the AWS service with which this access key was most recently used. The value of
      this field is "N/A" in the following situations:

      * The user does not have an access key.

      * An access key exists but has not been used since IAM started tracking this information.

      * There is no sign-in data associated with the user.

    - **Region** *(string) --*

      The AWS Region where this access key was most recently used. The value for this field is
      "N/A" in the following situations:

      * The user does not have an access key.

      * An access key exists but has not been used since IAM began tracking this information.

      * There is no sign-in data associated with the user.

      For more information about AWS Regions, see `Regions and Endpoints
      <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ in the Amazon Web Services
      General Reference.
    """


_ClientGetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "_ClientGetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": ClientGetAccessKeyLastUsedResponseAccessKeyLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccessKeyLastUsedResponseTypeDef(
    _ClientGetAccessKeyLastUsedResponseTypeDef
):
    """
    Type definition for `ClientGetAccessKeyLastUsed` `Response`

    Contains the response to a successful  GetAccessKeyLastUsed request. It is also returned as a
    member of the  AccessKeyMetaData structure returned by the  ListAccessKeys action.

    - **UserName** *(string) --*

      The name of the AWS IAM user that owns this access key.

    - **AccessKeyLastUsed** *(dict) --*

      Contains information about the last time the access key was used.

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the access key was most recently used. This field is null in the following situations:

        * The user does not have an access key.

        * An access key exists but has not been used since IAM began tracking this information.

        * There is no sign-in data associated with the user.

      - **ServiceName** *(string) --*

        The name of the AWS service with which this access key was most recently used. The value of
        this field is "N/A" in the following situations:

        * The user does not have an access key.

        * An access key exists but has not been used since IAM started tracking this information.

        * There is no sign-in data associated with the user.

      - **Region** *(string) --*

        The AWS Region where this access key was most recently used. The value for this field is
        "N/A" in the following situations:

        * The user does not have an access key.

        * An access key exists but has not been used since IAM began tracking this information.

        * There is no sign-in data associated with the user.

        For more information about AWS Regions, see `Regions and Endpoints
        <https://docs.aws.amazon.com/general/latest/gr/rande.html>`__ in the Amazon Web Services
        General Reference.
    """


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseGroupDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseGroupDetailList` `GroupPolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListGroupPolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListAttachedManagedPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponse` `GroupDetailList`

    Contains information about an IAM group, including all of the group's policies.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.

    - **GroupPolicyList** *(list) --*

      A list of the inline policies embedded in the group.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **AttachedManagedPolicies** *(list) --*

      A list of the managed policies attached to the group.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .
    """


_ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponsePolicies` `PolicyVersionList`

    Contains information about a version of a managed policy.

    This data type is used as a response element in the  CreatePolicyVersion ,
    GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC
      3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
      convert the policy back to plain JSON text. For example, if you use Java, you can use
      the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
      Other languages and SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy
      is created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the policy version was created.
    """


_ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[
            ClientGetAccountAuthorizationDetailsResponsePoliciesPolicyVersionListTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponse` `Policies`

    Contains information about a managed policy, including the policy's ARN, versions, and the
    number of principal entities (users, groups, and roles) that the policy is attached to.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    For more information about managed policies, see `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default (operative)
      version.

      For more information about policy versions, see `Versioning for Managed Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in
      the *IAM User Guide* .

    - **AttachmentCount** *(integer) --*

      The number of principal entities (users, groups, and roles) that the policy is attached
      to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used as the permissions
      boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and
      time when the most recent policy version was created.

    - **PolicyVersionList** *(list) --*

      A list containing information about the versions of the policy.

      - *(dict) --*

        Contains information about a version of a managed policy.

        This data type is used as a response element in the  CreatePolicyVersion ,
        GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **Document** *(string) --*

          The policy document.

          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.

          The policy document returned in this structure is URL-encoded compliant with `RFC
          3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
          convert the policy back to plain JSON text. For example, if you use Java, you can use
          the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
          Other languages and SDKs provide similar functionality.

        - **VersionId** *(string) --*

          The identifier for the policy version.

          Policy version identifiers always begin with ``v`` (always lowercase). When a policy
          is created, the first policy version is ``v1`` .

        - **IsDefaultVersion** *(boolean) --*

          Specifies whether the policy version is set as the policy's default version.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the policy version was created.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries
    for IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes
    the date and time and the Region in which the role was last used. Activity is
    only reported for the trailing 400 days. This period can be shorter if your
    Region began supporting these features within the last year. The role might have
    been used more than 400 days ago. For more information, see `Regions Where Data
    Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking
      period. For more information about the tracking period, see `Regions Where Data
      Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with
    a resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value.
      For example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting``
      , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
      that consist of the number associated with the different cost centers in your
      company. Typically, many resources have tags with the same key name but with
      different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string.
        However, you must interpret the value in your code.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileList` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about
      ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses
      the AWS CLI, or API to assume the role can specify the duration using the
      optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries
      for IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information
      about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
      User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with
        a resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value.
          For example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting``
          , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
          that consist of the number associated with the different cost centers in your
          company. Typically, many resources have tags with the same key name but with
          different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string.
            However, you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes
      the date and time and the Region in which the role was last used. Activity is
      only reported for the trailing 400 days. This period can be shorter if your
      Region began supporting these features within the last year. The role might have
      been used more than 400 days ago. For more information, see `Regions Where Data
      Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking
        period. For more information about the tracking period, see `Regions Where Data
        Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListRolesTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `InstanceProfileList`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM
      Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information
      about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about
          ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format
          <http://www.iso.org/iso/iso8601>`__ , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses
          the AWS CLI, or API to assume the role can specify the duration using the
          optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries
          for IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information
          about tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with
            a resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
            User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value.
              For example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting``
              , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
              that consist of the number associated with the different cost centers in your
              company. Typically, many resources have tags with the same key name but with
              different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string.
                However, you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes
          the date and time and the Region in which the role was last used. Activity is
          only reported for the trailing 400 days. This period can be shorter if your
          Region began supporting these features within the last year. The role might have
          been used more than 400 days ago. For more information, see `Regions Where Data
          Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking
            period. For more information about the tracking period, see `Regions Where Data
            Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `RolePolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseRoleDetailList` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListInstanceProfileListTypeDef
        ],
        "RolePolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListRolePolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseRoleDetailListPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListTagsTypeDef
        ],
        "RoleLastUsed": ClientGetAccountAuthorizationDetailsResponseRoleDetailListRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponse` `RoleDetailList`

    Contains information about an IAM role, including all of the role's policies.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The trust policy that grants permission to assume the role.

    - **InstanceProfileList** *(list) --*

      A list of instance profiles that contain this role.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM
          Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information
          about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about
              IDs, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about
              ARNs and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format
              <http://www.iso.org/iso/iso8601>`__ , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses
              the AWS CLI, or API to assume the role can specify the duration using the
              optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries
              for IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information
              about tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
              User Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with
                a resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                User Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value.
                  For example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting``
                  , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
                  that consist of the number associated with the different cost centers in your
                  company. Typically, many resources have tags with the same key name but with
                  different values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string.
                    However, you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes
              the date and time and the Region in which the role was last used. Activity is
              only reported for the trailing 400 days. This period can be shorter if your
              Region began supporting these features within the last year. The role might have
              been used more than 400 days ago. For more information, see `Regions Where Data
              Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking
                period. For more information about the tracking period, see `Regions Where Data
                Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **RolePolicyList** *(list) --*

      A list of inline policies embedded in the role. These policies are the role's access
      (permissions) policies.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **AttachedManagedPolicies** *(list) --*

      A list of managed policies attached to the role. These policies are the role's access
      (permissions) policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseUserDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseUserDetailList` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseUserDetailList` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponseUserDetailList` `UserPolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListUserPolicyListTypeDef
        ],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": ClientGetAccountAuthorizationDetailsResponseUserDetailListPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListTagsTypeDef
        ],
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetailsResponse` `UserDetailList`

    Contains information about an IAM user, including all the user's policies and all the IAM
    groups the user is in.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **UserPolicyList** *(list) --*

      A list of the inline policies embedded in the user.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **GroupList** *(list) --*

      A list of IAM groups that the user is in.

      - *(string) --*

    - **AttachedManagedPolicies** *(list) --*

      A list of the managed policies attached to the user.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientGetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "_ClientGetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List[
            ClientGetAccountAuthorizationDetailsResponseUserDetailListTypeDef
        ],
        "GroupDetailList": List[
            ClientGetAccountAuthorizationDetailsResponseGroupDetailListTypeDef
        ],
        "RoleDetailList": List[
            ClientGetAccountAuthorizationDetailsResponseRoleDetailListTypeDef
        ],
        "Policies": List[ClientGetAccountAuthorizationDetailsResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientGetAccountAuthorizationDetailsResponseTypeDef(
    _ClientGetAccountAuthorizationDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetAccountAuthorizationDetails` `Response`

    Contains the response to a successful  GetAccountAuthorizationDetails request.

    - **UserDetailList** *(list) --*

      A list containing information about IAM users.

      - *(dict) --*

        Contains information about an IAM user, including all the user's policies and all the IAM
        groups the user is in.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **UserPolicyList** *(list) --*

          A list of the inline policies embedded in the user.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **GroupList** *(list) --*

          A list of IAM groups that the user is in.

          - *(string) --*

        - **AttachedManagedPolicies** *(list) --*

          A list of the managed policies attached to the user.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **GroupDetailList** *(list) --*

      A list containing information about IAM groups.

      - *(dict) --*

        Contains information about an IAM group, including all of the group's policies.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

        - **GroupPolicyList** *(list) --*

          A list of the inline policies embedded in the group.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **AttachedManagedPolicies** *(list) --*

          A list of the managed policies attached to the group.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

    - **RoleDetailList** *(list) --*

      A list containing information about IAM roles.

      - *(dict) --*

        Contains information about an IAM role, including all of the role's policies.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The trust policy that grants permission to assume the role.

        - **InstanceProfileList** *(list) --*

          A list of instance profiles that contain this role.

          - *(dict) --*

            Contains information about an instance profile.

            This data type is used as a response element in the following operations:

            *  CreateInstanceProfile

            *  GetInstanceProfile

            *  ListInstanceProfiles

            *  ListInstanceProfilesForRole

            - **Path** *(string) --*

              The path to the instance profile. For more information about paths, see `IAM
              Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **InstanceProfileName** *(string) --*

              The name identifying the instance profile.

            - **InstanceProfileId** *(string) --*

              The stable and unique string identifying the instance profile. For more information
              about IDs, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the instance profile. For more information
              about ARNs and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **CreateDate** *(datetime) --*

              The date when the instance profile was created.

            - **Roles** *(list) --*

              The role associated with the instance profile.

              - *(dict) --*

                Contains information about an IAM role. This structure is returned as a response
                element in several API operations that interact with roles.

                - **Path** *(string) --*

                  The path to the role. For more information about paths, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* .

                - **RoleName** *(string) --*

                  The friendly name that identifies the role.

                - **RoleId** *(string) --*

                  The stable and unique string identifying the role. For more information about
                  IDs, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) specifying the role. For more information about
                  ARNs and how to use them in policies, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* guide.

                - **CreateDate** *(datetime) --*

                  The date and time, in `ISO 8601 date-time format
                  <http://www.iso.org/iso/iso8601>`__ , when the role was created.

                - **AssumeRolePolicyDocument** *(string) --*

                  The policy that grants an entity permission to assume the role.

                - **Description** *(string) --*

                  A description of the role that you provide.

                - **MaxSessionDuration** *(integer) --*

                  The maximum session duration (in seconds) for the specified role. Anyone who uses
                  the AWS CLI, or API to assume the role can specify the duration using the
                  optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

                - **PermissionsBoundary** *(dict) --*

                  The ARN of the policy used to set the permissions boundary for the role.

                  For more information about permissions boundaries, see `Permissions Boundaries
                  for IAM Identities
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
                  in the *IAM User Guide* .

                  - **PermissionsBoundaryType** *(string) --*

                    The permissions boundary usage type that indicates what type of IAM resource is
                    used as the permissions boundary for an entity. This data type can only have a
                    value of ``Policy`` .

                  - **PermissionsBoundaryArn** *(string) --*

                    The ARN of the policy used to set the permissions boundary for the user or role.

                - **Tags** *(list) --*

                  A list of tags that are attached to the specified role. For more information
                  about tagging, see `Tagging IAM Identities
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                  User Guide* .

                  - *(dict) --*

                    A structure that represents user-provided metadata that can be associated with
                    a resource such as an IAM user or role. For more information about tagging, see
                    `Tagging IAM Identities
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                    User Guide* .

                    - **Key** *(string) --*

                      The key name that can be used to look up or retrieve the associated value.
                      For example, ``Department`` or ``Cost Center`` are common choices.

                    - **Value** *(string) --*

                      The value associated with this tag. For example, tags with a key name of
                      ``Department`` could have values such as ``Human Resources`` , ``Accounting``
                      , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
                      that consist of the number associated with the different cost centers in your
                      company. Typically, many resources have tags with the same key name but with
                      different values.

                      .. note::

                        AWS always interprets the tag ``Value`` as a single string. If you need to
                        store an array, you can store comma-separated values in the string.
                        However, you must interpret the value in your code.

                - **RoleLastUsed** *(dict) --*

                  Contains information about the last time that an IAM role was used. This includes
                  the date and time and the Region in which the role was last used. Activity is
                  only reported for the trailing 400 days. This period can be shorter if your
                  Region began supporting these features within the last year. The role might have
                  been used more than 400 days ago. For more information, see `Regions Where Data
                  Is Tracked
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                  in the *IAM User Guide* .

                  - **LastUsedDate** *(datetime) --*

                    The date and time, in `ISO 8601 date-time format
                    <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                    This field is null if the role has not been used within the IAM tracking
                    period. For more information about the tracking period, see `Regions Where Data
                    Is Tracked
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                    in the *IAM User Guide* .

                  - **Region** *(string) --*

                    The name of the AWS Region in which the role was last used.

        - **RolePolicyList** *(list) --*

          A list of inline policies embedded in the role. These policies are the role's access
          (permissions) policies.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **AttachedManagedPolicies** *(list) --*

          A list of managed policies attached to the role. These policies are the role's access
          (permissions) policies.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.

    - **Policies** *(list) --*

      A list containing information about managed policies.

      - *(dict) --*

        Contains information about a managed policy, including the policy's ARN, versions, and the
        number of principal entities (users, groups, and roles) that the policy is attached to.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        For more information about managed policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.

        - **PolicyId** *(string) --*

          The stable and unique string identifying the policy.

          For more information about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **Path** *(string) --*

          The path to the policy.

          For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **DefaultVersionId** *(string) --*

          The identifier for the version of the policy that is set as the default (operative)
          version.

          For more information about policy versions, see `Versioning for Managed Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in
          the *IAM User Guide* .

        - **AttachmentCount** *(integer) --*

          The number of principal entities (users, groups, and roles) that the policy is attached
          to.

        - **PermissionsBoundaryUsageCount** *(integer) --*

          The number of entities (users and roles) for which the policy is used as the permissions
          boundary.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

        - **IsAttachable** *(boolean) --*

          Specifies whether the policy can be attached to an IAM user, group, or role.

        - **Description** *(string) --*

          A friendly description of the policy.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was created.

        - **UpdateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was last updated.

          When a policy has only one version, this field contains the date and time when the policy
          was created. When a policy has more than one version, this field contains the date and
          time when the most recent policy version was created.

        - **PolicyVersionList** *(list) --*

          A list containing information about the versions of the policy.

          - *(dict) --*

            Contains information about a version of a managed policy.

            This data type is used as a response element in the  CreatePolicyVersion ,
            GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **Document** *(string) --*

              The policy document.

              The policy document is returned in the response to the  GetPolicyVersion and
              GetAccountAuthorizationDetails operations. It is not returned in the response to the
              CreatePolicyVersion or  ListPolicyVersions operations.

              The policy document returned in this structure is URL-encoded compliant with `RFC
              3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
              convert the policy back to plain JSON text. For example, if you use Java, you can use
              the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
              Other languages and SDKs provide similar functionality.

            - **VersionId** *(string) --*

              The identifier for the policy version.

              Policy version identifiers always begin with ``v`` (always lowercase). When a policy
              is created, the first policy version is ``v1`` .

            - **IsDefaultVersion** *(boolean) --*

              Specifies whether the policy version is set as the policy's default version.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef = TypedDict(
    "_ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": int,
        "RequireSymbols": bool,
        "RequireNumbers": bool,
        "RequireUppercaseCharacters": bool,
        "RequireLowercaseCharacters": bool,
        "AllowUsersToChangePassword": bool,
        "ExpirePasswords": bool,
        "MaxPasswordAge": int,
        "PasswordReusePrevention": int,
        "HardExpiry": bool,
    },
    total=False,
)


class ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef(
    _ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef
):
    """
    Type definition for `ClientGetAccountPasswordPolicyResponse` `PasswordPolicy`

    A structure that contains details about the account's password policy.

    - **MinimumPasswordLength** *(integer) --*

      Minimum length to require for IAM user passwords.

    - **RequireSymbols** *(boolean) --*

      Specifies whether to require symbols for IAM user passwords.

    - **RequireNumbers** *(boolean) --*

      Specifies whether to require numbers for IAM user passwords.

    - **RequireUppercaseCharacters** *(boolean) --*

      Specifies whether to require uppercase characters for IAM user passwords.

    - **RequireLowercaseCharacters** *(boolean) --*

      Specifies whether to require lowercase characters for IAM user passwords.

    - **AllowUsersToChangePassword** *(boolean) --*

      Specifies whether IAM users are allowed to change their own password.

    - **ExpirePasswords** *(boolean) --*

      Indicates whether passwords in the account expire. Returns true if ``MaxPasswordAge``
      contains a value greater than 0. Returns false if MaxPasswordAge is 0 or not present.

    - **MaxPasswordAge** *(integer) --*

      The number of days that an IAM user password is valid.

    - **PasswordReusePrevention** *(integer) --*

      Specifies the number of previous passwords that IAM users are prevented from reusing.

    - **HardExpiry** *(boolean) --*

      Specifies whether IAM users are prevented from setting a new password after their password
      has expired.
    """


_ClientGetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "_ClientGetAccountPasswordPolicyResponseTypeDef",
    {"PasswordPolicy": ClientGetAccountPasswordPolicyResponsePasswordPolicyTypeDef},
    total=False,
)


class ClientGetAccountPasswordPolicyResponseTypeDef(
    _ClientGetAccountPasswordPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetAccountPasswordPolicy` `Response`

    Contains the response to a successful  GetAccountPasswordPolicy request.

    - **PasswordPolicy** *(dict) --*

      A structure that contains details about the account's password policy.

      - **MinimumPasswordLength** *(integer) --*

        Minimum length to require for IAM user passwords.

      - **RequireSymbols** *(boolean) --*

        Specifies whether to require symbols for IAM user passwords.

      - **RequireNumbers** *(boolean) --*

        Specifies whether to require numbers for IAM user passwords.

      - **RequireUppercaseCharacters** *(boolean) --*

        Specifies whether to require uppercase characters for IAM user passwords.

      - **RequireLowercaseCharacters** *(boolean) --*

        Specifies whether to require lowercase characters for IAM user passwords.

      - **AllowUsersToChangePassword** *(boolean) --*

        Specifies whether IAM users are allowed to change their own password.

      - **ExpirePasswords** *(boolean) --*

        Indicates whether passwords in the account expire. Returns true if ``MaxPasswordAge``
        contains a value greater than 0. Returns false if MaxPasswordAge is 0 or not present.

      - **MaxPasswordAge** *(integer) --*

        The number of days that an IAM user password is valid.

      - **PasswordReusePrevention** *(integer) --*

        Specifies the number of previous passwords that IAM users are prevented from reusing.

      - **HardExpiry** *(boolean) --*

        Specifies whether IAM users are prevented from setting a new password after their password
        has expired.
    """


_ClientGetAccountSummaryResponseTypeDef = TypedDict(
    "_ClientGetAccountSummaryResponseTypeDef",
    {"SummaryMap": Dict[str, int]},
    total=False,
)


class ClientGetAccountSummaryResponseTypeDef(_ClientGetAccountSummaryResponseTypeDef):
    """
    Type definition for `ClientGetAccountSummary` `Response`

    Contains the response to a successful  GetAccountSummary request.

    - **SummaryMap** *(dict) --*

      A set of key–value pairs containing information about IAM entity usage and IAM quotas.

      - *(string) --*

        - *(integer) --*
    """


_ClientGetContextKeysForCustomPolicyResponseTypeDef = TypedDict(
    "_ClientGetContextKeysForCustomPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)


class ClientGetContextKeysForCustomPolicyResponseTypeDef(
    _ClientGetContextKeysForCustomPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetContextKeysForCustomPolicy` `Response`

    Contains the response to a successful  GetContextKeysForPrincipalPolicy or
    GetContextKeysForCustomPolicy request.

    - **ContextKeyNames** *(list) --*

      The list of context keys that are referenced in the input policies.

      - *(string) --*
    """


_ClientGetContextKeysForPrincipalPolicyResponseTypeDef = TypedDict(
    "_ClientGetContextKeysForPrincipalPolicyResponseTypeDef",
    {"ContextKeyNames": List[str]},
    total=False,
)


class ClientGetContextKeysForPrincipalPolicyResponseTypeDef(
    _ClientGetContextKeysForPrincipalPolicyResponseTypeDef
):
    """
    Type definition for `ClientGetContextKeysForPrincipalPolicy` `Response`

    Contains the response to a successful  GetContextKeysForPrincipalPolicy or
    GetContextKeysForCustomPolicy request.

    - **ContextKeyNames** *(list) --*

      The list of context keys that are referenced in the input policies.

      - *(string) --*
    """


_ClientGetCredentialReportResponseTypeDef = TypedDict(
    "_ClientGetCredentialReportResponseTypeDef",
    {"Content": bytes, "ReportFormat": str, "GeneratedTime": datetime},
    total=False,
)


class ClientGetCredentialReportResponseTypeDef(
    _ClientGetCredentialReportResponseTypeDef
):
    """
    Type definition for `ClientGetCredentialReport` `Response`

    Contains the response to a successful  GetCredentialReport request.

    - **Content** *(bytes) --*

      Contains the credential report. The report is Base64-encoded.

    - **ReportFormat** *(string) --*

      The format (MIME type) of the credential report.

    - **GeneratedTime** *(datetime) --*

      The date and time when the credential report was created, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ .
    """


_ClientGetGroupPolicyResponseTypeDef = TypedDict(
    "_ClientGetGroupPolicyResponseTypeDef",
    {"GroupName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetGroupPolicyResponseTypeDef(_ClientGetGroupPolicyResponseTypeDef):
    """
    Type definition for `ClientGetGroupPolicy` `Response`

    Contains the response to a successful  GetGroupPolicy request.

    - **GroupName** *(string) --*

      The group the policy is associated with.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.

      IAM stores policies in JSON format. However, resources that were created using AWS
      CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML
      policy to JSON format before submitting it to IAM.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    Type definition for `ClientGetGroupResponse` `Group`

    A structure that contains details about the group.

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the group was created.
    """


_ClientGetGroupResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetGroupResponseUsersPermissionsBoundaryTypeDef(
    _ClientGetGroupResponseUsersPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetGroupResponseUsers` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetGroupResponseUsersTagsTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetGroupResponseUsersTagsTypeDef(_ClientGetGroupResponseUsersTagsTypeDef):
    """
    Type definition for `ClientGetGroupResponseUsers` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetGroupResponseUsersTypeDef = TypedDict(
    "_ClientGetGroupResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetGroupResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetGroupResponseUsersTagsTypeDef],
    },
    total=False,
)


class ClientGetGroupResponseUsersTypeDef(_ClientGetGroupResponseUsersTypeDef):
    """
    Type definition for `ClientGetGroupResponse` `Users`

    Contains information about an IAM user entity.

    This data type is used as a response element in the following operations:

    *  CreateUser

    *  GetUser

    *  ListUsers

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the date
      and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {
        "Group": ClientGetGroupResponseGroupTypeDef,
        "Users": List[ClientGetGroupResponseUsersTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    Type definition for `ClientGetGroup` `Response`

    Contains the response to a successful  GetGroup request.

    - **Group** *(dict) --*

      A structure that contains details about the group.

      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **GroupName** *(string) --*

        The friendly name that identifies the group.

      - **GroupId** *(string) --*

        The stable and unique string identifying the group. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
        how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the group was created.

    - **Users** *(list) --*

      A list of users in the group.

      - *(dict) --*

        Contains information about an IAM user entity.

        This data type is used as a response element in the following operations:

        *  CreateUser

        *  GetUser

        *  ListUsers

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
          and how to use ARNs in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **PasswordLastUsed** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user's password was last used to sign in to an AWS website. For a list of AWS
          websites that capture a user's last sign-in time, see the `Credential Reports
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
          the *IAM User Guide* . If a password is used more than once in a five-minute span, only
          the first use is returned in this field. If the field is null (no value), then it
          indicates that they never signed in with a password. This can be because:

          * The user never had a password.

          * A password exists but has not been used since IAM started tracking this information on
          October 20, 2014.

          A null value does not mean that the user *never* had a password. Also, if the user does
          not currently have a password but had one in the past, then this field contains the date
          and time the most recent password was used.

          This value is returned only in the  GetUser and  ListUsers operations.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetInstanceProfileResponseInstanceProfileRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used
      as the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientGetInstanceProfileResponseInstanceProfileRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef
):
    """
    Type definition for `ClientGetInstanceProfileResponseInstanceProfileRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store
        an array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetInstanceProfileResponseInstanceProfileRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetInstanceProfileResponseInstanceProfileRolesTagsTypeDef],
        "RoleLastUsed": ClientGetInstanceProfileResponseInstanceProfileRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef
):
    """
    Type definition for `ClientGetInstanceProfileResponseInstanceProfile` `Roles`

    Contains information about an IAM role. This structure is returned as a response element
    in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used
        as the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store
            an array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientGetInstanceProfileResponseInstanceProfileTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseInstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientGetInstanceProfileResponseInstanceProfileRolesTypeDef],
    },
    total=False,
)


class ClientGetInstanceProfileResponseInstanceProfileTypeDef(
    _ClientGetInstanceProfileResponseInstanceProfileTypeDef
):
    """
    Type definition for `ClientGetInstanceProfileResponse` `InstanceProfile`

    A structure containing details about the instance profile.

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information about
      ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response element
        in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used
            as the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store
                an array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ClientGetInstanceProfileResponseTypeDef = TypedDict(
    "_ClientGetInstanceProfileResponseTypeDef",
    {"InstanceProfile": ClientGetInstanceProfileResponseInstanceProfileTypeDef},
    total=False,
)


class ClientGetInstanceProfileResponseTypeDef(_ClientGetInstanceProfileResponseTypeDef):
    """
    Type definition for `ClientGetInstanceProfile` `Response`

    Contains the response to a successful  GetInstanceProfile request.

    - **InstanceProfile** *(dict) --*

      A structure containing details about the instance profile.

      - **Path** *(string) --*

        The path to the instance profile. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **InstanceProfileName** *(string) --*

        The name identifying the instance profile.

      - **InstanceProfileId** *(string) --*

        The stable and unique string identifying the instance profile. For more information about
        IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the instance profile. For more information about
        ARNs and how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date when the instance profile was created.

      - **Roles** *(list) --*

        The role associated with the instance profile.

        - *(dict) --*

          Contains information about an IAM role. This structure is returned as a response element
          in several API operations that interact with roles.

          - **Path** *(string) --*

            The path to the role. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **RoleName** *(string) --*

            The friendly name that identifies the role.

          - **RoleId** *(string) --*

            The stable and unique string identifying the role. For more information about IDs, see
            `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
            how to use them in policies, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* guide.

          - **CreateDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the role was created.

          - **AssumeRolePolicyDocument** *(string) --*

            The policy that grants an entity permission to assume the role.

          - **Description** *(string) --*

            A description of the role that you provide.

          - **MaxSessionDuration** *(integer) --*

            The maximum session duration (in seconds) for the specified role. Anyone who uses the
            AWS CLI, or API to assume the role can specify the duration using the optional
            ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

          - **PermissionsBoundary** *(dict) --*

            The ARN of the policy used to set the permissions boundary for the role.

            For more information about permissions boundaries, see `Permissions Boundaries for IAM
            Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
            in the *IAM User Guide* .

            - **PermissionsBoundaryType** *(string) --*

              The permissions boundary usage type that indicates what type of IAM resource is used
              as the permissions boundary for an entity. This data type can only have a value of
              ``Policy`` .

            - **PermissionsBoundaryArn** *(string) --*

              The ARN of the policy used to set the permissions boundary for the user or role.

          - **Tags** *(list) --*

            A list of tags that are attached to the specified role. For more information about
            tagging, see `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - *(dict) --*

              A structure that represents user-provided metadata that can be associated with a
              resource such as an IAM user or role. For more information about tagging, see
              `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - **Key** *(string) --*

                The key name that can be used to look up or retrieve the associated value. For
                example, ``Department`` or ``Cost Center`` are common choices.

              - **Value** *(string) --*

                The value associated with this tag. For example, tags with a key name of
                ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
                ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                consist of the number associated with the different cost centers in your company.
                Typically, many resources have tags with the same key name but with different
                values.

                .. note::

                  AWS always interprets the tag ``Value`` as a single string. If you need to store
                  an array, you can store comma-separated values in the string. However, you must
                  interpret the value in your code.

          - **RoleLastUsed** *(dict) --*

            Contains information about the last time that an IAM role was used. This includes the
            date and time and the Region in which the role was last used. Activity is only reported
            for the trailing 400 days. This period can be shorter if your Region began supporting
            these features within the last year. The role might have been used more than 400 days
            ago. For more information, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

            - **LastUsedDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              that the role was last used.

              This field is null if the role has not been used within the IAM tracking period. For
              more information about the tracking period, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

            - **Region** *(string) --*

              The name of the AWS Region in which the role was last used.
    """


_ClientGetLoginProfileResponseLoginProfileTypeDef = TypedDict(
    "_ClientGetLoginProfileResponseLoginProfileTypeDef",
    {"UserName": str, "CreateDate": datetime, "PasswordResetRequired": bool},
    total=False,
)


class ClientGetLoginProfileResponseLoginProfileTypeDef(
    _ClientGetLoginProfileResponseLoginProfileTypeDef
):
    """
    Type definition for `ClientGetLoginProfileResponse` `LoginProfile`

    A structure containing the user name and password create date for the user.

    - **UserName** *(string) --*

      The name of the user, which can be used for signing in to the AWS Management Console.

    - **CreateDate** *(datetime) --*

      The date when the password for the user was created.

    - **PasswordResetRequired** *(boolean) --*

      Specifies whether the user is required to set a new password on next sign-in.
    """


_ClientGetLoginProfileResponseTypeDef = TypedDict(
    "_ClientGetLoginProfileResponseTypeDef",
    {"LoginProfile": ClientGetLoginProfileResponseLoginProfileTypeDef},
    total=False,
)


class ClientGetLoginProfileResponseTypeDef(_ClientGetLoginProfileResponseTypeDef):
    """
    Type definition for `ClientGetLoginProfile` `Response`

    Contains the response to a successful  GetLoginProfile request.

    - **LoginProfile** *(dict) --*

      A structure containing the user name and password create date for the user.

      - **UserName** *(string) --*

        The name of the user, which can be used for signing in to the AWS Management Console.

      - **CreateDate** *(datetime) --*

        The date when the password for the user was created.

      - **PasswordResetRequired** *(boolean) --*

        Specifies whether the user is required to set a new password on next sign-in.
    """


_ClientGetOpenIdConnectProviderResponseTypeDef = TypedDict(
    "_ClientGetOpenIdConnectProviderResponseTypeDef",
    {
        "Url": str,
        "ClientIDList": List[str],
        "ThumbprintList": List[str],
        "CreateDate": datetime,
    },
    total=False,
)


class ClientGetOpenIdConnectProviderResponseTypeDef(
    _ClientGetOpenIdConnectProviderResponseTypeDef
):
    """
    Type definition for `ClientGetOpenIdConnectProvider` `Response`

    Contains the response to a successful  GetOpenIDConnectProvider request.

    - **Url** *(string) --*

      The URL that the IAM OIDC provider resource object is associated with. For more information,
      see  CreateOpenIDConnectProvider .

    - **ClientIDList** *(list) --*

      A list of client IDs (also known as audiences) that are associated with the specified IAM
      OIDC provider resource object. For more information, see  CreateOpenIDConnectProvider .

      - *(string) --*

    - **ThumbprintList** *(list) --*

      A list of certificate thumbprints that are associated with the specified IAM OIDC provider
      resource object. For more information, see  CreateOpenIDConnectProvider .

      - *(string) --*

        Contains a thumbprint for an identity provider's server certificate.

        The identity provider's server certificate thumbprint is the hex-encoded SHA-1 hash value
        of the self-signed X.509 certificate. This thumbprint is used by the domain where the
        OpenID Connect provider makes its keys available. The thumbprint is always a 40-character
        string.

    - **CreateDate** *(datetime) --*

      The date and time when the IAM OIDC provider resource object was created in the AWS account.
    """


_ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": str,
        "EntityPath": str,
        "LastAuthenticatedTime": datetime,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)


class ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef(
    _ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef
):
    """
    Type definition for `ClientGetOrganizationsAccessReportResponse` `AccessDetails`

    An object that contains details about when a principal in the reported AWS Organizations
    entity last attempted to access an AWS service. A principal can be an IAM user, an IAM
    role, or the AWS account root user within the reported Organizations entity.

    This data type is a response element in the  GetOrganizationsAccessReport operation.

    - **ServiceName** *(string) --*

      The name of the service in which access was attempted.

    - **ServiceNamespace** *(string) --*

      The namespace of the service in which access was attempted.

      To learn the service namespace of a service, go to `Actions, Resources, and Condition
      Keys for AWS Services
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
      in the *IAM User Guide* . Choose the name of the service to view details for that
      service. In the first paragraph, find the service prefix. For example, ``(service prefix:
      a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *AWS General Reference* .

    - **Region** *(string) --*

      The Region where the last service access attempt occurred.

      This field is null if no principals in the reported Organizations entity attempted to
      access the service within the `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .

    - **EntityPath** *(string) --*

      The path of the Organizations entity (root, organizational unit, or account) from which
      an authenticated principal last attempted to access the service. AWS does not report
      unauthenticated requests.

      This field is null if no principals (IAM users, IAM roles, or root users) in the reported
      Organizations entity attempted to access the service within the `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .

    - **LastAuthenticatedTime** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when an authenticated principal most recently attempted to access the service. AWS does
      not report unauthenticated requests.

      This field is null if no principals in the reported Organizations entity attempted to
      access the service within the `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .

    - **TotalAuthenticatedEntities** *(integer) --*

      The number of accounts with authenticated principals (root users, IAM users, and IAM
      roles) that attempted to access the service in the reporting period.
    """


_ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef(
    _ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef
):
    """
    Type definition for `ClientGetOrganizationsAccessReportResponse` `ErrorDetails`

    Contains information about the reason that the operation failed.

    This data type is used as a response element in the  GetOrganizationsAccessReport ,
    GetServiceLastAccessedDetails , and  GetServiceLastAccessedDetailsWithEntities operations.

    - **Message** *(string) --*

      Detailed information about the reason that the operation failed.

    - **Code** *(string) --*

      The error code associated with the operation failure.
    """


_ClientGetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "_ClientGetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": str,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List[
            ClientGetOrganizationsAccessReportResponseAccessDetailsTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": ClientGetOrganizationsAccessReportResponseErrorDetailsTypeDef,
    },
    total=False,
)


class ClientGetOrganizationsAccessReportResponseTypeDef(
    _ClientGetOrganizationsAccessReportResponseTypeDef
):
    """
    Type definition for `ClientGetOrganizationsAccessReport` `Response`

    - **JobStatus** *(string) --*

      The status of the job.

    - **JobCreationDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the report job was created.

    - **JobCompletionDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the generated report job was completed or failed.

      This field is null if the job is still in progress, as indicated by a job status value of
      ``IN_PROGRESS`` .

    - **NumberOfServicesAccessible** *(integer) --*

      The number of services that the applicable SCPs allow account principals to access.

    - **NumberOfServicesNotAccessed** *(integer) --*

      The number of services that account principals are allowed but did not attempt to access.

    - **AccessDetails** *(list) --*

      An object that contains details about the most recent attempt to access the service.

      - *(dict) --*

        An object that contains details about when a principal in the reported AWS Organizations
        entity last attempted to access an AWS service. A principal can be an IAM user, an IAM
        role, or the AWS account root user within the reported Organizations entity.

        This data type is a response element in the  GetOrganizationsAccessReport operation.

        - **ServiceName** *(string) --*

          The name of the service in which access was attempted.

        - **ServiceNamespace** *(string) --*

          The namespace of the service in which access was attempted.

          To learn the service namespace of a service, go to `Actions, Resources, and Condition
          Keys for AWS Services
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
          in the *IAM User Guide* . Choose the name of the service to view details for that
          service. In the first paragraph, find the service prefix. For example, ``(service prefix:
          a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *AWS General Reference* .

        - **Region** *(string) --*

          The Region where the last service access attempt occurred.

          This field is null if no principals in the reported Organizations entity attempted to
          access the service within the `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

        - **EntityPath** *(string) --*

          The path of the Organizations entity (root, organizational unit, or account) from which
          an authenticated principal last attempted to access the service. AWS does not report
          unauthenticated requests.

          This field is null if no principals (IAM users, IAM roles, or root users) in the reported
          Organizations entity attempted to access the service within the `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

        - **LastAuthenticatedTime** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when an authenticated principal most recently attempted to access the service. AWS does
          not report unauthenticated requests.

          This field is null if no principals in the reported Organizations entity attempted to
          access the service within the `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

        - **TotalAuthenticatedEntities** *(integer) --*

          The number of accounts with authenticated principals (root users, IAM users, and IAM
          roles) that attempted to access the service in the reporting period.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.

    - **ErrorDetails** *(dict) --*

      Contains information about the reason that the operation failed.

      This data type is used as a response element in the  GetOrganizationsAccessReport ,
      GetServiceLastAccessedDetails , and  GetServiceLastAccessedDetailsWithEntities operations.

      - **Message** *(string) --*

        Detailed information about the reason that the operation failed.

      - **Code** *(string) --*

        The error code associated with the operation failure.
    """


_ClientGetPolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetPolicyResponsePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientGetPolicyResponsePolicyTypeDef(_ClientGetPolicyResponsePolicyTypeDef):
    """
    Type definition for `ClientGetPolicyResponse` `Policy`

    A structure containing details about the policy.

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
      in the *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default version.

    - **AttachmentCount** *(integer) --*

      The number of entities (users, groups, and roles) that the policy is attached to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used to set the
      permissions boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

      This element is included in the response to the  GetPolicy operation. It is not included in
      the response to the  ListPolicies operation.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and time
      when the most recent policy version was created.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef",
    {"Policy": ClientGetPolicyResponsePolicyTypeDef},
    total=False,
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    Type definition for `ClientGetPolicy` `Response`

    Contains the response to a successful  GetPolicy request.

    - **Policy** *(dict) --*

      A structure containing details about the policy.

      - **PolicyName** *(string) --*

        The friendly name (not ARN) identifying the policy.

      - **PolicyId** *(string) --*

        The stable and unique string identifying the policy.

        For more information about IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

        For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
        Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
        in the *AWS General Reference* .

      - **Path** *(string) --*

        The path to the policy.

        For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **DefaultVersionId** *(string) --*

        The identifier for the version of the policy that is set as the default version.

      - **AttachmentCount** *(integer) --*

        The number of entities (users, groups, and roles) that the policy is attached to.

      - **PermissionsBoundaryUsageCount** *(integer) --*

        The number of entities (users and roles) for which the policy is used to set the
        permissions boundary.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

      - **IsAttachable** *(boolean) --*

        Specifies whether the policy can be attached to an IAM user, group, or role.

      - **Description** *(string) --*

        A friendly description of the policy.

        This element is included in the response to the  GetPolicy operation. It is not included in
        the response to the  ListPolicies operation.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy was created.

      - **UpdateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy was last updated.

        When a policy has only one version, this field contains the date and time when the policy
        was created. When a policy has more than one version, this field contains the date and time
        when the most recent policy version was created.
    """


_ClientGetPolicyVersionResponsePolicyVersionTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponsePolicyVersionTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientGetPolicyVersionResponsePolicyVersionTypeDef(
    _ClientGetPolicyVersionResponsePolicyVersionTypeDef
):
    """
    Type definition for `ClientGetPolicyVersionResponse` `PolicyVersion`

    A structure containing details about the policy version.

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC 3986
      <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
      policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
      method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
      SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
      created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the policy version was created.
    """


_ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponseTypeDef",
    {"PolicyVersion": ClientGetPolicyVersionResponsePolicyVersionTypeDef},
    total=False,
)


class ClientGetPolicyVersionResponseTypeDef(_ClientGetPolicyVersionResponseTypeDef):
    """
    Type definition for `ClientGetPolicyVersion` `Response`

    Contains the response to a successful  GetPolicyVersion request.

    - **PolicyVersion** *(dict) --*

      A structure containing details about the policy version.

      - **Document** *(string) --*

        The policy document.

        The policy document is returned in the response to the  GetPolicyVersion and
        GetAccountAuthorizationDetails operations. It is not returned in the response to the
        CreatePolicyVersion or  ListPolicyVersions operations.

        The policy document returned in this structure is URL-encoded compliant with `RFC 3986
        <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert the
        policy back to plain JSON text. For example, if you use Java, you can use the ``decode``
        method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other languages and
        SDKs provide similar functionality.

      - **VersionId** *(string) --*

        The identifier for the policy version.

        Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
        created, the first policy version is ``v1`` .

      - **IsDefaultVersion** *(boolean) --*

        Specifies whether the policy version is set as the policy's default version.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the policy version was created.
    """


_ClientGetRolePolicyResponseTypeDef = TypedDict(
    "_ClientGetRolePolicyResponseTypeDef",
    {"RoleName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetRolePolicyResponseTypeDef(_ClientGetRolePolicyResponseTypeDef):
    """
    Type definition for `ClientGetRolePolicy` `Response`

    Contains the response to a successful  GetRolePolicy request.

    - **RoleName** *(string) --*

      The role the policy is associated with.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.

      IAM stores policies in JSON format. However, resources that were created using AWS
      CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML
      policy to JSON format before submitting it to IAM.
    """


_ClientGetRoleResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetRoleResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetRoleResponseRolePermissionsBoundaryTypeDef(
    _ClientGetRoleResponseRolePermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetRoleResponseRole` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetRoleResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientGetRoleResponseRoleRoleLastUsedTypeDef(
    _ClientGetRoleResponseRoleRoleLastUsedTypeDef
):
    """
    Type definition for `ClientGetRoleResponseRole` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the date
    and time and the Region in which the role was last used. Activity is only reported for the
    trailing 400 days. This period can be shorter if your Region began supporting these
    features within the last year. The role might have been used more than 400 days ago. For
    more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
      the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For more
      information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientGetRoleResponseRoleTagsTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetRoleResponseRoleTagsTypeDef(_ClientGetRoleResponseRoleTagsTypeDef):
    """
    Type definition for `ClientGetRoleResponseRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetRoleResponseRoleTypeDef = TypedDict(
    "_ClientGetRoleResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientGetRoleResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientGetRoleResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientGetRoleResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientGetRoleResponseRoleTypeDef(_ClientGetRoleResponseRoleTypeDef):
    """
    Type definition for `ClientGetRoleResponse` `Role`

    A structure containing details about the IAM role.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
      to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about tagging,
      see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the date
      and time and the Region in which the role was last used. Activity is only reported for the
      trailing 400 days. This period can be shorter if your Region began supporting these
      features within the last year. The role might have been used more than 400 days ago. For
      more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
        the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For more
        information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientGetRoleResponseTypeDef = TypedDict(
    "_ClientGetRoleResponseTypeDef",
    {"Role": ClientGetRoleResponseRoleTypeDef},
    total=False,
)


class ClientGetRoleResponseTypeDef(_ClientGetRoleResponseTypeDef):
    """
    Type definition for `ClientGetRole` `Response`

    Contains the response to a successful  GetRole request.

    - **Role** *(dict) --*

      A structure containing details about the IAM role.

      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **RoleName** *(string) --*

        The friendly name that identifies the role.

      - **RoleId** *(string) --*

        The stable and unique string identifying the role. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
        to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* guide.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the role was created.

      - **AssumeRolePolicyDocument** *(string) --*

        The policy that grants an entity permission to assume the role.

      - **Description** *(string) --*

        A description of the role that you provide.

      - **MaxSessionDuration** *(integer) --*

        The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
        CLI, or API to assume the role can specify the duration using the optional
        ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the role.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are attached to the specified role. For more information about tagging,
        see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

      - **RoleLastUsed** *(dict) --*

        Contains information about the last time that an IAM role was used. This includes the date
        and time and the Region in which the role was last used. Activity is only reported for the
        trailing 400 days. This period can be shorter if your Region began supporting these
        features within the last year. The role might have been used more than 400 days ago. For
        more information, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

        - **LastUsedDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
          the role was last used.

          This field is null if the role has not been used within the IAM tracking period. For more
          information about the tracking period, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

        - **Region** *(string) --*

          The name of the AWS Region in which the role was last used.
    """


_ClientGetSamlProviderResponseTypeDef = TypedDict(
    "_ClientGetSamlProviderResponseTypeDef",
    {"SAMLMetadataDocument": str, "CreateDate": datetime, "ValidUntil": datetime},
    total=False,
)


class ClientGetSamlProviderResponseTypeDef(_ClientGetSamlProviderResponseTypeDef):
    """
    Type definition for `ClientGetSamlProvider` `Response`

    Contains the response to a successful  GetSAMLProvider request.

    - **SAMLMetadataDocument** *(string) --*

      The XML metadata document that includes information about an identity provider.

    - **CreateDate** *(datetime) --*

      The date and time when the SAML provider was created.

    - **ValidUntil** *(datetime) --*

      The expiration date and time for the SAML provider.
    """


_ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef(
    _ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef
):
    """
    Type definition for `ClientGetServerCertificateResponseServerCertificate` `ServerCertificateMetadata`

    The meta information of the server certificate, such as its name, path, ID, and ARN.

    - **Path** *(string) --*

      The path to the server certificate. For more information about paths, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
      in the *IAM User Guide* .

    - **ServerCertificateName** *(string) --*

      The name that identifies the server certificate.

    - **ServerCertificateId** *(string) --*

      The stable and unique string identifying the server certificate. For more information
      about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the server certificate. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UploadDate** *(datetime) --*

      The date when the server certificate was uploaded.

    - **Expiration** *(datetime) --*

      The date on which the certificate is set to expire.
    """


_ClientGetServerCertificateResponseServerCertificateTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": ClientGetServerCertificateResponseServerCertificateServerCertificateMetadataTypeDef,
        "CertificateBody": str,
        "CertificateChain": str,
    },
    total=False,
)


class ClientGetServerCertificateResponseServerCertificateTypeDef(
    _ClientGetServerCertificateResponseServerCertificateTypeDef
):
    """
    Type definition for `ClientGetServerCertificateResponse` `ServerCertificate`

    A structure containing details about the server certificate.

    - **ServerCertificateMetadata** *(dict) --*

      The meta information of the server certificate, such as its name, path, ID, and ARN.

      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
        in the *IAM User Guide* .

      - **ServerCertificateName** *(string) --*

        The name that identifies the server certificate.

      - **ServerCertificateId** *(string) --*

        The stable and unique string identifying the server certificate. For more information
        about IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the server certificate. For more information
        about ARNs and how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **UploadDate** *(datetime) --*

        The date when the server certificate was uploaded.

      - **Expiration** *(datetime) --*

        The date on which the certificate is set to expire.

    - **CertificateBody** *(string) --*

      The contents of the public key certificate.

    - **CertificateChain** *(string) --*

      The contents of the public key certificate chain.
    """


_ClientGetServerCertificateResponseTypeDef = TypedDict(
    "_ClientGetServerCertificateResponseTypeDef",
    {"ServerCertificate": ClientGetServerCertificateResponseServerCertificateTypeDef},
    total=False,
)


class ClientGetServerCertificateResponseTypeDef(
    _ClientGetServerCertificateResponseTypeDef
):
    """
    Type definition for `ClientGetServerCertificate` `Response`

    Contains the response to a successful  GetServerCertificate request.

    - **ServerCertificate** *(dict) --*

      A structure containing details about the server certificate.

      - **ServerCertificateMetadata** *(dict) --*

        The meta information of the server certificate, such as its name, path, ID, and ARN.

        - **Path** *(string) --*

          The path to the server certificate. For more information about paths, see `IAM
          Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
          in the *IAM User Guide* .

        - **ServerCertificateName** *(string) --*

          The name that identifies the server certificate.

        - **ServerCertificateId** *(string) --*

          The stable and unique string identifying the server certificate. For more information
          about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the server certificate. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UploadDate** *(datetime) --*

          The date when the server certificate was uploaded.

        - **Expiration** *(datetime) --*

          The date on which the certificate is set to expire.

      - **CertificateBody** *(string) --*

        The contents of the public key certificate.

      - **CertificateChain** *(string) --*

        The contents of the public key certificate chain.
    """


_ClientGetServiceLastAccessedDetailsResponseErrorTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseErrorTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseErrorTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsResponse` `Error`

    An object that contains details about the reason the operation failed.

    - **Message** *(string) --*

      Detailed information about the reason that the operation failed.

    - **Code** *(string) --*

      The error code associated with the operation failure.
    """


_ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef",
    {
        "ServiceName": str,
        "LastAuthenticated": datetime,
        "ServiceNamespace": str,
        "LastAuthenticatedEntity": str,
        "TotalAuthenticatedEntities": int,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsResponse` `ServicesLastAccessed`

    Contains details about the most recent attempt to access the service.

    This data type is used as a response element in the  GetServiceLastAccessedDetails
    operation.

    - **ServiceName** *(string) --*

      The name of the service in which access was attempted.

    - **LastAuthenticated** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when an authenticated entity most recently attempted to access the service. AWS does not
      report unauthenticated requests.

      This field is null if no IAM entities attempted to access the service within the
      `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .

    - **ServiceNamespace** *(string) --*

      The namespace of the service in which access was attempted.

      To learn the service namespace of a service, go to `Actions, Resources, and Condition
      Keys for AWS Services
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
      in the *IAM User Guide* . Choose the name of the service to view details for that
      service. In the first paragraph, find the service prefix. For example, ``(service prefix:
      a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *AWS General Reference* .

    - **LastAuthenticatedEntity** *(string) --*

      The ARN of the authenticated entity (user or role) that last attempted to access the
      service. AWS does not report unauthenticated requests.

      This field is null if no IAM entities attempted to access the service within the
      `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .

    - **TotalAuthenticatedEntities** *(integer) --*

      The total number of authenticated principals (root user, IAM users, or IAM roles) that
      have attempted to access the service.

      This field is null if no principals attempted to access the service within the `reporting
      period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .
    """


_ClientGetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": str,
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List[
            ClientGetServiceLastAccessedDetailsResponseServicesLastAccessedTypeDef
        ],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsResponseErrorTypeDef,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsResponseTypeDef(
    _ClientGetServiceLastAccessedDetailsResponseTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetails` `Response`

    - **JobStatus** *(string) --*

      The status of the job.

    - **JobCreationDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the report job was created.

    - **ServicesLastAccessed** *(list) --*

      A ``ServiceLastAccessed`` object that contains details about the most recent attempt to
      access the service.

      - *(dict) --*

        Contains details about the most recent attempt to access the service.

        This data type is used as a response element in the  GetServiceLastAccessedDetails
        operation.

        - **ServiceName** *(string) --*

          The name of the service in which access was attempted.

        - **LastAuthenticated** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when an authenticated entity most recently attempted to access the service. AWS does not
          report unauthenticated requests.

          This field is null if no IAM entities attempted to access the service within the
          `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

        - **ServiceNamespace** *(string) --*

          The namespace of the service in which access was attempted.

          To learn the service namespace of a service, go to `Actions, Resources, and Condition
          Keys for AWS Services
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
          in the *IAM User Guide* . Choose the name of the service to view details for that
          service. In the first paragraph, find the service prefix. For example, ``(service prefix:
          a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *AWS General Reference* .

        - **LastAuthenticatedEntity** *(string) --*

          The ARN of the authenticated entity (user or role) that last attempted to access the
          service. AWS does not report unauthenticated requests.

          This field is null if no IAM entities attempted to access the service within the
          `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

        - **TotalAuthenticatedEntities** *(integer) --*

          The total number of authenticated principals (root user, IAM users, or IAM roles) that
          have attempted to access the service.

          This field is null if no principals attempted to access the service within the `reporting
          period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

    - **JobCompletionDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the generated report job was completed or failed.

      This field is null if the job is still in progress, as indicated by a job status value of
      ``IN_PROGRESS`` .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.

    - **Error** *(dict) --*

      An object that contains details about the reason the operation failed.

      - **Message** *(string) --*

        Detailed information about the reason that the operation failed.

      - **Code** *(string) --*

        The error code associated with the operation failure.
    """


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef",
    {"Arn": str, "Name": str, "Type": str, "Id": str, "Path": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsList` `EntityInfo`

    The ``EntityInfo`` object that contains details about the entity (user or role).

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **Name** *(string) --*

      The name of the entity (user or role).

    - **Type** *(string) --*

      The type of entity (user or role).

    - **Id** *(string) --*

      The identifier of the entity (user or role).

    - **Path** *(string) --*

      The path to the entity (user or role). For more information about paths, see `IAM
      Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef",
    {
        "EntityInfo": ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListEntityInfoTypeDef,
        "LastAuthenticated": datetime,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsWithEntitiesResponse` `EntityDetailsList`

    An object that contains details about when the IAM entities (users or roles) were last used
    in an attempt to access the specified AWS service.

    This data type is a response element in the  GetServiceLastAccessedDetailsWithEntities
    operation.

    - **EntityInfo** *(dict) --*

      The ``EntityInfo`` object that contains details about the entity (user or role).

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

        For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
        Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
        *AWS General Reference* .

      - **Name** *(string) --*

        The name of the entity (user or role).

      - **Type** *(string) --*

        The type of entity (user or role).

      - **Id** *(string) --*

        The identifier of the entity (user or role).

      - **Path** *(string) --*

        The path to the entity (user or role). For more information about paths, see `IAM
        Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

    - **LastAuthenticated** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the authenticated entity last attempted to access AWS. AWS does not report
      unauthenticated requests.

      This field is null if no IAM entities attempted to access the service within the
      `reporting period
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
      .
    """


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef",
    {"Message": str, "Code": str},
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsWithEntitiesResponse` `Error`

    An object that contains details about the reason the operation failed.

    - **Message** *(string) --*

      Detailed information about the reason that the operation failed.

    - **Code** *(string) --*

      The error code associated with the operation failure.
    """


_ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "_ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": str,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List[
            ClientGetServiceLastAccessedDetailsWithEntitiesResponseEntityDetailsListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
        "Error": ClientGetServiceLastAccessedDetailsWithEntitiesResponseErrorTypeDef,
    },
    total=False,
)


class ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(
    _ClientGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef
):
    """
    Type definition for `ClientGetServiceLastAccessedDetailsWithEntities` `Response`

    - **JobStatus** *(string) --*

      The status of the job.

    - **JobCreationDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the report job was created.

    - **JobCompletionDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the generated report job was completed or failed.

      This field is null if the job is still in progress, as indicated by a job status value of
      ``IN_PROGRESS`` .

    - **EntityDetailsList** *(list) --*

      An ``EntityDetailsList`` object that contains details about when an IAM entity (user or role)
      used group or policy permissions in an attempt to access the specified AWS service.

      - *(dict) --*

        An object that contains details about when the IAM entities (users or roles) were last used
        in an attempt to access the specified AWS service.

        This data type is a response element in the  GetServiceLastAccessedDetailsWithEntities
        operation.

        - **EntityInfo** *(dict) --*

          The ``EntityInfo`` object that contains details about the entity (user or role).

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

            For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
            Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
            *AWS General Reference* .

          - **Name** *(string) --*

            The name of the entity (user or role).

          - **Type** *(string) --*

            The type of entity (user or role).

          - **Id** *(string) --*

            The identifier of the entity (user or role).

          - **Path** *(string) --*

            The path to the entity (user or role). For more information about paths, see `IAM
            Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

        - **LastAuthenticated** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the authenticated entity last attempted to access AWS. AWS does not report
          unauthenticated requests.

          This field is null if no IAM entities attempted to access the service within the
          `reporting period
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period>`__
          .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.

    - **Error** *(dict) --*

      An object that contains details about the reason the operation failed.

      - **Message** *(string) --*

        Detailed information about the reason that the operation failed.

      - **Code** *(string) --*

        The error code associated with the operation failure.
    """


_ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef",
    {"Region": str, "Resources": List[str]},
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
):
    """
    Type definition for `ClientGetServiceLinkedRoleDeletionStatusResponseReason` `RoleUsageList`

    An object that contains details about how a service-linked role is used, if that
    information is returned by the service.

    This data type is used as a response element in the  GetServiceLinkedRoleDeletionStatus
    operation.

    - **Region** *(string) --*

      The name of the Region where the service-linked role is being used.

    - **Resources** *(list) --*

      The name of the resource that is using the service-linked role.

      - *(string) --*

        The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

        For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
        Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
        the *AWS General Reference* .
    """


_ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef",
    {
        "Reason": str,
        "RoleUsageList": List[
            ClientGetServiceLinkedRoleDeletionStatusResponseReasonRoleUsageListTypeDef
        ],
    },
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef
):
    """
    Type definition for `ClientGetServiceLinkedRoleDeletionStatusResponse` `Reason`

    An object that contains details about the reason the deletion failed.

    - **Reason** *(string) --*

      A short description of the reason that the service-linked role deletion failed.

    - **RoleUsageList** *(list) --*

      A list of objects that contains details about the service-linked role deletion failure, if
      that information is returned by the service. If the service-linked role has active sessions
      or if any resources that were used by the role have not been deleted from the linked
      service, the role can't be deleted. This parameter includes a list of the resources that
      are associated with the role and the Region in which the resources are being used.

      - *(dict) --*

        An object that contains details about how a service-linked role is used, if that
        information is returned by the service.

        This data type is used as a response element in the  GetServiceLinkedRoleDeletionStatus
        operation.

        - **Region** *(string) --*

          The name of the Region where the service-linked role is being used.

        - **Resources** *(list) --*

          The name of the resource that is using the service-linked role.

          - *(string) --*

            The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

            For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
            Namespaces
            <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
            the *AWS General Reference* .
    """


_ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "_ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": str,
        "Reason": ClientGetServiceLinkedRoleDeletionStatusResponseReasonTypeDef,
    },
    total=False,
)


class ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef(
    _ClientGetServiceLinkedRoleDeletionStatusResponseTypeDef
):
    """
    Type definition for `ClientGetServiceLinkedRoleDeletionStatus` `Response`

    - **Status** *(string) --*

      The status of the deletion.

    - **Reason** *(dict) --*

      An object that contains details about the reason the deletion failed.

      - **Reason** *(string) --*

        A short description of the reason that the service-linked role deletion failed.

      - **RoleUsageList** *(list) --*

        A list of objects that contains details about the service-linked role deletion failure, if
        that information is returned by the service. If the service-linked role has active sessions
        or if any resources that were used by the role have not been deleted from the linked
        service, the role can't be deleted. This parameter includes a list of the resources that
        are associated with the role and the Region in which the resources are being used.

        - *(dict) --*

          An object that contains details about how a service-linked role is used, if that
          information is returned by the service.

          This data type is used as a response element in the  GetServiceLinkedRoleDeletionStatus
          operation.

          - **Region** *(string) --*

            The name of the Region where the service-linked role is being used.

          - **Resources** *(list) --*

            The name of the resource that is using the service-linked role.

            - *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .
    """


_ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "_ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": str,
        "UploadDate": datetime,
    },
    total=False,
)


class ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef(
    _ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef
):
    """
    Type definition for `ClientGetSshPublicKeyResponse` `SSHPublicKey`

    A structure containing details about the SSH public key.

    - **UserName** *(string) --*

      The name of the IAM user associated with the SSH public key.

    - **SSHPublicKeyId** *(string) --*

      The unique identifier for the SSH public key.

    - **Fingerprint** *(string) --*

      The MD5 message digest of the SSH public key.

    - **SSHPublicKeyBody** *(string) --*

      The SSH public key.

    - **Status** *(string) --*

      The status of the SSH public key. ``Active`` means that the key can be used for
      authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot be
      used.

    - **UploadDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the SSH public key was uploaded.
    """


_ClientGetSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientGetSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientGetSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)


class ClientGetSshPublicKeyResponseTypeDef(_ClientGetSshPublicKeyResponseTypeDef):
    """
    Type definition for `ClientGetSshPublicKey` `Response`

    Contains the response to a successful  GetSSHPublicKey request.

    - **SSHPublicKey** *(dict) --*

      A structure containing details about the SSH public key.

      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.

      - **SSHPublicKeyId** *(string) --*

        The unique identifier for the SSH public key.

      - **Fingerprint** *(string) --*

        The MD5 message digest of the SSH public key.

      - **SSHPublicKeyBody** *(string) --*

        The SSH public key.

      - **Status** *(string) --*

        The status of the SSH public key. ``Active`` means that the key can be used for
        authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot be
        used.

      - **UploadDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the SSH public key was uploaded.
    """


_ClientGetUserPolicyResponseTypeDef = TypedDict(
    "_ClientGetUserPolicyResponseTypeDef",
    {"UserName": str, "PolicyName": str, "PolicyDocument": str},
    total=False,
)


class ClientGetUserPolicyResponseTypeDef(_ClientGetUserPolicyResponseTypeDef):
    """
    Type definition for `ClientGetUserPolicy` `Response`

    Contains the response to a successful  GetUserPolicy request.

    - **UserName** *(string) --*

      The user the policy is associated with.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.

      IAM stores policies in JSON format. However, resources that were created using AWS
      CloudFormation templates can be formatted in YAML. AWS CloudFormation always converts a YAML
      policy to JSON format before submitting it to IAM.
    """


_ClientGetUserResponseUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientGetUserResponseUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientGetUserResponseUserPermissionsBoundaryTypeDef(
    _ClientGetUserResponseUserPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientGetUserResponseUser` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientGetUserResponseUserTagsTypeDef = TypedDict(
    "_ClientGetUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetUserResponseUserTagsTypeDef(_ClientGetUserResponseUserTagsTypeDef):
    """
    Type definition for `ClientGetUserResponseUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientGetUserResponseUserTypeDef = TypedDict(
    "_ClientGetUserResponseUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientGetUserResponseUserPermissionsBoundaryTypeDef,
        "Tags": List[ClientGetUserResponseUserTagsTypeDef],
    },
    total=False,
)


class ClientGetUserResponseUserTypeDef(_ClientGetUserResponseUserTypeDef):
    """
    Type definition for `ClientGetUserResponse` `User`

    A structure containing details about the IAM user.

    .. warning::

      Due to a service issue, password last used data does not include password use from May 3,
      2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects `last sign-in
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html>`__
      dates shown in the IAM console and password last used dates in the `IAM credential report
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html>`__ ,
      and returned by this GetUser API. If users signed in during the affected time, the password
      last used date that is returned is the date the user last signed in before May 3, 2018. For
      users that signed in after May 23, 2018 14:08 PDT, the returned password last used date is
      accurate.

      You can use password last used information to identify unused credentials for deletion. For
      example, you might delete users who did not sign in to AWS in the last 90 days. In cases
      like this, we recommend that you adjust your evaluation window to include dates after May
      23, 2018. Alternatively, if your users use access keys to access AWS programmatically you
      can refer to access key last used information because it is accurate for all dates.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the user's password was last used to sign in to an AWS website. For a list of AWS websites
      that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the
      *IAM User Guide* . If a password is used more than once in a five-minute span, only the
      first use is returned in this field. If the field is null (no value), then it indicates
      that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does not
      currently have a password but had one in the past, then this field contains the date and
      time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef",
    {"User": ClientGetUserResponseUserTypeDef},
    total=False,
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    Type definition for `ClientGetUser` `Response`

    Contains the response to a successful  GetUser request.

    - **User** *(dict) --*

      A structure containing details about the IAM user.

      .. warning::

        Due to a service issue, password last used data does not include password use from May 3,
        2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects `last sign-in
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html>`__
        dates shown in the IAM console and password last used dates in the `IAM credential report
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html>`__ ,
        and returned by this GetUser API. If users signed in during the affected time, the password
        last used date that is returned is the date the user last signed in before May 3, 2018. For
        users that signed in after May 23, 2018 14:08 PDT, the returned password last used date is
        accurate.

        You can use password last used information to identify unused credentials for deletion. For
        example, you might delete users who did not sign in to AWS in the last 90 days. In cases
        like this, we recommend that you adjust your evaluation window to include dates after May
        23, 2018. Alternatively, if your users use access keys to access AWS programmatically you
        can refer to access key last used information because it is accurate for all dates.

      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **UserName** *(string) --*

        The friendly name identifying the user.

      - **UserId** *(string) --*

        The stable and unique string identifying the user. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
        and how to use ARNs in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the user was created.

      - **PasswordLastUsed** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the user's password was last used to sign in to an AWS website. For a list of AWS websites
        that capture a user's last sign-in time, see the `Credential Reports
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in the
        *IAM User Guide* . If a password is used more than once in a five-minute span, only the
        first use is returned in this field. If the field is null (no value), then it indicates
        that they never signed in with a password. This can be because:

        * The user never had a password.

        * A password exists but has not been used since IAM started tracking this information on
        October 20, 2014.

        A null value does not mean that the user *never* had a password. Also, if the user does not
        currently have a password but had one in the past, then this field contains the date and
        time the most recent password was used.

        This value is returned only in the  GetUser and  ListUsers operations.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the user.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are associated with the specified user. For more information about
        tagging, see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.
    """


_ClientListAccessKeysResponseAccessKeyMetadataTypeDef = TypedDict(
    "_ClientListAccessKeysResponseAccessKeyMetadataTypeDef",
    {"UserName": str, "AccessKeyId": str, "Status": str, "CreateDate": datetime},
    total=False,
)


class ClientListAccessKeysResponseAccessKeyMetadataTypeDef(
    _ClientListAccessKeysResponseAccessKeyMetadataTypeDef
):
    """
    Type definition for `ClientListAccessKeysResponse` `AccessKeyMetadata`

    Contains information about an AWS access key, without its secret key.

    This data type is used as a response element in the  ListAccessKeys operation.

    - **UserName** *(string) --*

      The name of the IAM user that the key is associated with.

    - **AccessKeyId** *(string) --*

      The ID for this access key.

    - **Status** *(string) --*

      The status of the access key. ``Active`` means that the key is valid for API calls;
      ``Inactive`` means it is not.

    - **CreateDate** *(datetime) --*

      The date when the access key was created.
    """


_ClientListAccessKeysResponseTypeDef = TypedDict(
    "_ClientListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List[ClientListAccessKeysResponseAccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAccessKeysResponseTypeDef(_ClientListAccessKeysResponseTypeDef):
    """
    Type definition for `ClientListAccessKeys` `Response`

    Contains the response to a successful  ListAccessKeys request.

    - **AccessKeyMetadata** *(list) --*

      A list of objects containing metadata about the access keys.

      - *(dict) --*

        Contains information about an AWS access key, without its secret key.

        This data type is used as a response element in the  ListAccessKeys operation.

        - **UserName** *(string) --*

          The name of the IAM user that the key is associated with.

        - **AccessKeyId** *(string) --*

          The ID for this access key.

        - **Status** *(string) --*

          The status of the access key. ``Active`` means that the key is valid for API calls;
          ``Inactive`` means it is not.

        - **CreateDate** *(datetime) --*

          The date when the access key was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListAccountAliasesResponseTypeDef = TypedDict(
    "_ClientListAccountAliasesResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListAccountAliasesResponseTypeDef(_ClientListAccountAliasesResponseTypeDef):
    """
    Type definition for `ClientListAccountAliases` `Response`

    Contains the response to a successful  ListAccountAliases request.

    - **AccountAliases** *(list) --*

      A list of aliases associated with the account. AWS supports only one alias per account.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ClientListAttachedGroupPoliciesResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ClientListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[
            ClientListAttachedGroupPoliciesResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedGroupPoliciesResponseTypeDef(
    _ClientListAttachedGroupPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListAttachedGroupPolicies` `Response`

    Contains the response to a successful  ListAttachedGroupPolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ClientListAttachedRolePoliciesResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ClientListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[
            ClientListAttachedRolePoliciesResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedRolePoliciesResponseTypeDef(
    _ClientListAttachedRolePoliciesResponseTypeDef
):
    """
    Type definition for `ClientListAttachedRolePolicies` `Response`

    Contains the response to a successful  ListAttachedRolePolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef = TypedDict(
    "_ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef(
    _ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ClientListAttachedUserPoliciesResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ClientListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[
            ClientListAttachedUserPoliciesResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListAttachedUserPoliciesResponseTypeDef(
    _ClientListAttachedUserPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListAttachedUserPolicies` `Response`

    Contains the response to a successful  ListAttachedUserPolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef
):
    """
    Type definition for `ClientListEntitiesForPolicyResponse` `PolicyGroups`

    Contains information about a group that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **GroupName** *(string) --*

      The name (friendly name, not ARN) identifying the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ClientListEntitiesForPolicyResponsePolicyRolesTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyRolesTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyRolesTypeDef
):
    """
    Type definition for `ClientListEntitiesForPolicyResponse` `PolicyRoles`

    Contains information about a role that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **RoleName** *(string) --*

      The name (friendly name, not ARN) identifying the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ClientListEntitiesForPolicyResponsePolicyUsersTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)


class ClientListEntitiesForPolicyResponsePolicyUsersTypeDef(
    _ClientListEntitiesForPolicyResponsePolicyUsersTypeDef
):
    """
    Type definition for `ClientListEntitiesForPolicyResponse` `PolicyUsers`

    Contains information about a user that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **UserName** *(string) --*

      The name (friendly name, not ARN) identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ClientListEntitiesForPolicyResponseTypeDef = TypedDict(
    "_ClientListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[ClientListEntitiesForPolicyResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ClientListEntitiesForPolicyResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ClientListEntitiesForPolicyResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListEntitiesForPolicyResponseTypeDef(
    _ClientListEntitiesForPolicyResponseTypeDef
):
    """
    Type definition for `ClientListEntitiesForPolicy` `Response`

    Contains the response to a successful  ListEntitiesForPolicy request.

    - **PolicyGroups** *(list) --*

      A list of IAM groups that the policy is attached to.

      - *(dict) --*

        Contains information about a group that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **GroupName** *(string) --*

          The name (friendly name, not ARN) identifying the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **PolicyUsers** *(list) --*

      A list of IAM users that the policy is attached to.

      - *(dict) --*

        Contains information about a user that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **UserName** *(string) --*

          The name (friendly name, not ARN) identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **PolicyRoles** *(list) --*

      A list of IAM roles that the policy is attached to.

      - *(dict) --*

        Contains information about a role that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **RoleName** *(string) --*

          The name (friendly name, not ARN) identifying the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListGroupPoliciesResponseTypeDef = TypedDict(
    "_ClientListGroupPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListGroupPoliciesResponseTypeDef(_ClientListGroupPoliciesResponseTypeDef):
    """
    Type definition for `ClientListGroupPolicies` `Response`

    Contains the response to a successful  ListGroupPolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
      string of characters consisting of upper and lowercase alphanumeric characters with no
      spaces. You can also include any of the following characters: _+=,.@-

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsForUserResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientListGroupsForUserResponseGroupsTypeDef(
    _ClientListGroupsForUserResponseGroupsTypeDef
):
    """
    Type definition for `ClientListGroupsForUserResponse` `Groups`

    Contains information about an IAM group entity.

    This data type is used as a response element in the following operations:

    *  CreateGroup

    *  GetGroup

    *  ListGroups

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.
    """


_ClientListGroupsForUserResponseTypeDef = TypedDict(
    "_ClientListGroupsForUserResponseTypeDef",
    {
        "Groups": List[ClientListGroupsForUserResponseGroupsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListGroupsForUserResponseTypeDef(_ClientListGroupsForUserResponseTypeDef):
    """
    Type definition for `ClientListGroupsForUser` `Response`

    Contains the response to a successful  ListGroupsForUser request.

    - **Groups** *(list) --*

      A list of groups.

      - *(dict) --*

        Contains information about an IAM group entity.

        This data type is used as a response element in the following operations:

        *  CreateGroup

        *  GetGroup

        *  ListGroups

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientListGroupsResponse` `Groups`

    Contains information about an IAM group entity.

    This data type is used as a response element in the following operations:

    *  CreateGroup

    *  GetGroup

    *  ListGroups

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {
        "Groups": List[ClientListGroupsResponseGroupsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    Contains the response to a successful  ListGroups request.

    - **Groups** *(list) --*

      A list of groups.

      - *(dict) --*

        Contains information about an IAM group entity.

        This data type is used as a response element in the following operations:

        *  CreateGroup

        *  GetGroup

        *  ListGroups

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRoleResponseInstanceProfilesRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for
    IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRoleResponseInstanceProfilesRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only
    reported for the trailing 400 days. This period can be shorter if your Region began
    supporting these features within the last year. The role might have been used more
    than 400 days ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking period.
      For more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRoleResponseInstanceProfilesRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
      and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string. However,
        you must interpret the value in your code.
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRoleResponseInstanceProfiles` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs,
      see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
      and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for
      IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
          and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string. However,
            you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only
      reported for the trailing 400 days. This period can be shorter if your Region began
      supporting these features within the last year. The role might have been used more
      than 400 days ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking period.
        For more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            ClientListInstanceProfilesForRoleResponseInstanceProfilesRolesTypeDef
        ],
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef(
    _ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRoleResponse` `InstanceProfiles`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs,
          see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
          and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for
          IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
              and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string. However,
                you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only
          reported for the trailing 400 days. This period can be shorter if your Region began
          supporting these features within the last year. The role might have been used more
          than 400 days ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking period.
            For more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "_ClientListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List[
            ClientListInstanceProfilesForRoleResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceProfilesForRoleResponseTypeDef(
    _ClientListInstanceProfilesForRoleResponseTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesForRole` `Response`

    Contains the response to a successful  ListInstanceProfilesForRole request.

    - **InstanceProfiles** *(list) --*

      A list of instance profiles.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about IDs,
              see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
              and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses the
              AWS CLI, or API to assume the role can specify the duration using the optional
              ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries for
              IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information about
              tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with a
                resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
                Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value. For
                  example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
                  and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                  consist of the number associated with the different cost centers in your company.
                  Typically, many resources have tags with the same key name but with different
                  values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string. However,
                    you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes the
              date and time and the Region in which the role was last used. Activity is only
              reported for the trailing 400 days. This period can be shorter if your Region began
              supporting these features within the last year. The role might have been used more
              than 400 days ago. For more information, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking period.
                For more information about the tracking period, see `Regions Where Data Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesResponseInstanceProfilesRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for
    IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesResponseInstanceProfilesRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only
    reported for the trailing 400 days. This period can be shorter if your Region began
    supporting these features within the last year. The role might have been used more
    than 400 days ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking period.
      For more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesResponseInstanceProfilesRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
      and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string. However,
        you must interpret the value in your code.
    """


_ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListInstanceProfilesResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientListInstanceProfilesResponseInstanceProfilesRolesTagsTypeDef
        ],
        "RoleLastUsed": ClientListInstanceProfilesResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesResponseInstanceProfiles` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs,
      see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
      and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for
      IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
          and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string. However,
            you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only
      reported for the trailing 400 days. This period can be shorter if your Region began
      supporting these features within the last year. The role might have been used more
      than 400 days ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking period.
        For more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesResponseInstanceProfilesTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ClientListInstanceProfilesResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ClientListInstanceProfilesResponseInstanceProfilesTypeDef(
    _ClientListInstanceProfilesResponseInstanceProfilesTypeDef
):
    """
    Type definition for `ClientListInstanceProfilesResponse` `InstanceProfiles`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs,
          see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
          and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for
          IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
              and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string. However,
                you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only
          reported for the trailing 400 days. This period can be shorter if your Region began
          supporting these features within the last year. The role might have been used more
          than 400 days ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking period.
            For more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ClientListInstanceProfilesResponseTypeDef = TypedDict(
    "_ClientListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List[
            ClientListInstanceProfilesResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListInstanceProfilesResponseTypeDef(
    _ClientListInstanceProfilesResponseTypeDef
):
    """
    Type definition for `ClientListInstanceProfiles` `Response`

    Contains the response to a successful  ListInstanceProfiles request.

    - **InstanceProfiles** *(list) --*

      A list of instance profiles.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about IDs,
              see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
              and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses the
              AWS CLI, or API to assume the role can specify the duration using the optional
              ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries for
              IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information about
              tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with a
                resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
                Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value. For
                  example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
                  and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                  consist of the number associated with the different cost centers in your company.
                  Typically, many resources have tags with the same key name but with different
                  values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string. However,
                    you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes the
              date and time and the Region in which the role was last used. Activity is only
              reported for the trailing 400 days. This period can be shorter if your Region began
              supporting these features within the last year. The role might have been used more
              than 400 days ago. For more information, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking period.
                For more information about the tracking period, see `Regions Where Data Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListMfaDevicesResponseMFADevicesTypeDef = TypedDict(
    "_ClientListMfaDevicesResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)


class ClientListMfaDevicesResponseMFADevicesTypeDef(
    _ClientListMfaDevicesResponseMFADevicesTypeDef
):
    """
    Type definition for `ClientListMfaDevicesResponse` `MFADevices`

    Contains information about an MFA device.

    This data type is used as a response element in the  ListMFADevices operation.

    - **UserName** *(string) --*

      The user with whom the MFA device is associated.

    - **SerialNumber** *(string) --*

      The serial number that uniquely identifies the MFA device. For virtual MFA devices, the
      serial number is the device ARN.

    - **EnableDate** *(datetime) --*

      The date when the MFA device was enabled for the user.
    """


_ClientListMfaDevicesResponseTypeDef = TypedDict(
    "_ClientListMfaDevicesResponseTypeDef",
    {
        "MFADevices": List[ClientListMfaDevicesResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListMfaDevicesResponseTypeDef(_ClientListMfaDevicesResponseTypeDef):
    """
    Type definition for `ClientListMfaDevices` `Response`

    Contains the response to a successful  ListMFADevices request.

    - **MFADevices** *(list) --*

      A list of MFA devices.

      - *(dict) --*

        Contains information about an MFA device.

        This data type is used as a response element in the  ListMFADevices operation.

        - **UserName** *(string) --*

          The user with whom the MFA device is associated.

        - **SerialNumber** *(string) --*

          The serial number that uniquely identifies the MFA device. For virtual MFA devices, the
          serial number is the device ARN.

        - **EnableDate** *(datetime) --*

          The date when the MFA device was enabled for the user.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef = TypedDict(
    "_ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef",
    {"Arn": str},
    total=False,
)


class ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef(
    _ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
):
    """
    Type definition for `ClientListOpenIdConnectProvidersResponse` `OpenIDConnectProviderList`

    Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ClientListOpenIdConnectProvidersResponseTypeDef = TypedDict(
    "_ClientListOpenIdConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List[
            ClientListOpenIdConnectProvidersResponseOpenIDConnectProviderListTypeDef
        ]
    },
    total=False,
)


class ClientListOpenIdConnectProvidersResponseTypeDef(
    _ClientListOpenIdConnectProvidersResponseTypeDef
):
    """
    Type definition for `ClientListOpenIdConnectProviders` `Response`

    Contains the response to a successful  ListOpenIDConnectProviders request.

    - **OpenIDConnectProviderList** *(list) --*

      The list of IAM OIDC provider resource objects defined in the AWS account.

      - *(dict) --*

        Contains the Amazon Resource Name (ARN) for an IAM OpenID Connect provider.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .
    """


_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyType": str,
        "PolicyArn": str,
        "EntityType": str,
        "EntityName": str,
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
):
    """
    Type definition for `ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccess` `Policies`

    Contains details about the permissions policies that are attached to the specified
    identity (user, group, or role).

    This data type is an element of the  ListPoliciesGrantingServiceAccessEntry object.

    - **PolicyName** *(string) --*

      The policy name.

    - **PolicyType** *(string) --*

      The policy type. For more information about these policy types, see `Managed Policies
      and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
      in the *IAM User Guide* .

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .

    - **EntityType** *(string) --*

      The type of entity (user or role) that used the policy to access the service to which
      the inline policy is attached.

      This field is null for managed policies. For more information about these policy
      types, see `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
      in the *IAM User Guide* .

    - **EntityName** *(string) --*

      The name of the entity (user or role) to which the inline policy is attached.

      This field is null for managed policies. For more information about these policy
      types, see `Managed Policies and Inline Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
      in the *IAM User Guide* .
    """


_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef",
    {
        "ServiceNamespace": str,
        "Policies": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
):
    """
    Type definition for `ClientListPoliciesGrantingServiceAccessResponse` `PoliciesGrantingServiceAccess`

    Contains details about the permissions policies that are attached to the specified identity
    (user, group, or role).

    This data type is used as a response element in the  ListPoliciesGrantingServiceAccess
    operation.

    - **ServiceNamespace** *(string) --*

      The namespace of the service that was accessed.

      To learn the service namespace of a service, go to `Actions, Resources, and Condition
      Keys for AWS Services
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
      in the *IAM User Guide* . Choose the name of the service to view details for that
      service. In the first paragraph, find the service prefix. For example, ``(service prefix:
      a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
      in the *AWS General Reference* .

    - **Policies** *(list) --*

      The ``PoliciesGrantingServiceAccess`` object that contains details about the policy.

      - *(dict) --*

        Contains details about the permissions policies that are attached to the specified
        identity (user, group, or role).

        This data type is an element of the  ListPoliciesGrantingServiceAccessEntry object.

        - **PolicyName** *(string) --*

          The policy name.

        - **PolicyType** *(string) --*

          The policy type. For more information about these policy types, see `Managed Policies
          and Inline Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
          in the *IAM User Guide* .

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .

        - **EntityType** *(string) --*

          The type of entity (user or role) that used the policy to access the service to which
          the inline policy is attached.

          This field is null for managed policies. For more information about these policy
          types, see `Managed Policies and Inline Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
          in the *IAM User Guide* .

        - **EntityName** *(string) --*

          The name of the entity (user or role) to which the inline policy is attached.

          This field is null for managed policies. For more information about these policy
          types, see `Managed Policies and Inline Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
          in the *IAM User Guide* .
    """


_ClientListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "_ClientListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List[
            ClientListPoliciesGrantingServiceAccessResponsePoliciesGrantingServiceAccessTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPoliciesGrantingServiceAccessResponseTypeDef(
    _ClientListPoliciesGrantingServiceAccessResponseTypeDef
):
    """
    Type definition for `ClientListPoliciesGrantingServiceAccess` `Response`

    - **PoliciesGrantingServiceAccess** *(list) --*

      A ``ListPoliciesGrantingServiceAccess`` object that contains details about the permissions
      policies attached to the specified identity (user, group, or role).

      - *(dict) --*

        Contains details about the permissions policies that are attached to the specified identity
        (user, group, or role).

        This data type is used as a response element in the  ListPoliciesGrantingServiceAccess
        operation.

        - **ServiceNamespace** *(string) --*

          The namespace of the service that was accessed.

          To learn the service namespace of a service, go to `Actions, Resources, and Condition
          Keys for AWS Services
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html>`__
          in the *IAM User Guide* . Choose the name of the service to view details for that
          service. In the first paragraph, find the service prefix. For example, ``(service prefix:
          a4b)`` . For more information about service namespaces, see `AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *AWS General Reference* .

        - **Policies** *(list) --*

          The ``PoliciesGrantingServiceAccess`` object that contains details about the policy.

          - *(dict) --*

            Contains details about the permissions policies that are attached to the specified
            identity (user, group, or role).

            This data type is an element of the  ListPoliciesGrantingServiceAccessEntry object.

            - **PolicyName** *(string) --*

              The policy name.

            - **PolicyType** *(string) --*

              The policy type. For more information about these policy types, see `Managed Policies
              and Inline Policies
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
              in the *IAM User Guide* .

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

            - **EntityType** *(string) --*

              The type of entity (user or role) that used the policy to access the service to which
              the inline policy is attached.

              This field is null for managed policies. For more information about these policy
              types, see `Managed Policies and Inline Policies
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
              in the *IAM User Guide* .

            - **EntityName** *(string) --*

              The name of the entity (user or role) to which the inline policy is attached.

              This field is null for managed policies. For more information about these policy
              types, see `Managed Policies and Inline Policies
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html>`__
              in the *IAM User Guide* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. We recommend that you check ``IsTruncated`` after every call to ensure
      that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListPoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ClientListPoliciesResponsePoliciesTypeDef(
    _ClientListPoliciesResponsePoliciesTypeDef
):
    """
    Type definition for `ClientListPoliciesResponse` `Policies`

    Contains information about a managed policy.

    This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
    ListPolicies operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default version.

    - **AttachmentCount** *(integer) --*

      The number of entities (users, groups, and roles) that the policy is attached to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used to set the
      permissions boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

      This element is included in the response to the  GetPolicy operation. It is not included
      in the response to the  ListPolicies operation.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and
      time when the most recent policy version was created.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {
        "Policies": List[ClientListPoliciesResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    Type definition for `ClientListPolicies` `Response`

    Contains the response to a successful  ListPolicies request.

    - **Policies** *(list) --*

      A list of policies.

      - *(dict) --*

        Contains information about a managed policy.

        This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
        ListPolicies operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.

        - **PolicyId** *(string) --*

          The stable and unique string identifying the policy.

          For more information about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **Path** *(string) --*

          The path to the policy.

          For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **DefaultVersionId** *(string) --*

          The identifier for the version of the policy that is set as the default version.

        - **AttachmentCount** *(integer) --*

          The number of entities (users, groups, and roles) that the policy is attached to.

        - **PermissionsBoundaryUsageCount** *(integer) --*

          The number of entities (users and roles) for which the policy is used to set the
          permissions boundary.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

        - **IsAttachable** *(boolean) --*

          Specifies whether the policy can be attached to an IAM user, group, or role.

        - **Description** *(string) --*

          A friendly description of the policy.

          This element is included in the response to the  GetPolicy operation. It is not included
          in the response to the  ListPolicies operation.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was created.

        - **UpdateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was last updated.

          When a policy has only one version, this field contains the date and time when the policy
          was created. When a policy has more than one version, this field contains the date and
          time when the most recent policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListPolicyVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseVersionsTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListPolicyVersionsResponseVersionsTypeDef(
    _ClientListPolicyVersionsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListPolicyVersionsResponse` `Versions`

    Contains information about a version of a managed policy.

    This data type is used as a response element in the  CreatePolicyVersion ,
    GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC 3986
      <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
      the policy back to plain JSON text. For example, if you use Java, you can use the
      ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
      languages and SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
      created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy version was created.
    """


_ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseTypeDef",
    {
        "Versions": List[ClientListPolicyVersionsResponseVersionsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListPolicyVersionsResponseTypeDef(_ClientListPolicyVersionsResponseTypeDef):
    """
    Type definition for `ClientListPolicyVersions` `Response`

    Contains the response to a successful  ListPolicyVersions request.

    - **Versions** *(list) --*

      A list of policy versions.

      For more information about managed policy versions, see `Versioning for Managed Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
      *IAM User Guide* .

      - *(dict) --*

        Contains information about a version of a managed policy.

        This data type is used as a response element in the  CreatePolicyVersion ,
        GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **Document** *(string) --*

          The policy document.

          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.

          The policy document returned in this structure is URL-encoded compliant with `RFC 3986
          <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
          the policy back to plain JSON text. For example, if you use Java, you can use the
          ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
          languages and SDKs provide similar functionality.

        - **VersionId** *(string) --*

          The identifier for the policy version.

          Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
          created, the first policy version is ``v1`` .

        - **IsDefaultVersion** *(boolean) --*

          Specifies whether the policy version is set as the policy's default version.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListRolePoliciesResponseTypeDef = TypedDict(
    "_ClientListRolePoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListRolePoliciesResponseTypeDef(_ClientListRolePoliciesResponseTypeDef):
    """
    Type definition for `ClientListRolePolicies` `Response`

    Contains the response to a successful  ListRolePolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListRoleTagsResponseTagsTypeDef = TypedDict(
    "_ClientListRoleTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListRoleTagsResponseTagsTypeDef(_ClientListRoleTagsResponseTagsTypeDef):
    """
    Type definition for `ClientListRoleTagsResponse` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must interpret
        the value in your code.
    """


_ClientListRoleTagsResponseTypeDef = TypedDict(
    "_ClientListRoleTagsResponseTypeDef",
    {
        "Tags": List[ClientListRoleTagsResponseTagsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListRoleTagsResponseTypeDef(_ClientListRoleTagsResponseTypeDef):
    """
    Type definition for `ClientListRoleTags` `Response`

    - **Tags** *(list) --*

      The list of tags currently that is attached to the role. Each tag consists of a key name and
      an associated value. If no tags are attached to the specified role, the response contains an
      empty list.

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must interpret
            the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can use the ``Marker`` request parameter to make a subsequent pagination request that
      retrieves more items. Note that IAM might return fewer than the ``MaxItems`` number of
      results even when more results are available. Check ``IsTruncated`` after every call to
      ensure that you receive all of your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListRolesResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListRolesResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListRolesResponseRolesPermissionsBoundaryTypeDef(
    _ClientListRolesResponseRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientListRolesResponseRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientListRolesResponseRolesRoleLastUsedTypeDef = TypedDict(
    "_ClientListRolesResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientListRolesResponseRolesRoleLastUsedTypeDef(
    _ClientListRolesResponseRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ClientListRolesResponseRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientListRolesResponseRolesTagsTypeDef = TypedDict(
    "_ClientListRolesResponseRolesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListRolesResponseRolesTagsTypeDef(_ClientListRolesResponseRolesTagsTypeDef):
    """
    Type definition for `ClientListRolesResponseRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientListRolesResponseRolesTypeDef = TypedDict(
    "_ClientListRolesResponseRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientListRolesResponseRolesPermissionsBoundaryTypeDef,
        "Tags": List[ClientListRolesResponseRolesTagsTypeDef],
        "RoleLastUsed": ClientListRolesResponseRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientListRolesResponseRolesTypeDef(_ClientListRolesResponseRolesTypeDef):
    """
    Type definition for `ClientListRolesResponse` `Roles`

    Contains information about an IAM role. This structure is returned as a response element in
    several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientListRolesResponseTypeDef = TypedDict(
    "_ClientListRolesResponseTypeDef",
    {
        "Roles": List[ClientListRolesResponseRolesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListRolesResponseTypeDef(_ClientListRolesResponseTypeDef):
    """
    Type definition for `ClientListRoles` `Response`

    Contains the response to a successful  ListRoles request.

    - **Roles** *(list) --*

      A list of roles.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response element in
        several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
          CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListSamlProvidersResponseSAMLProviderListTypeDef = TypedDict(
    "_ClientListSamlProvidersResponseSAMLProviderListTypeDef",
    {"Arn": str, "ValidUntil": datetime, "CreateDate": datetime},
    total=False,
)


class ClientListSamlProvidersResponseSAMLProviderListTypeDef(
    _ClientListSamlProvidersResponseSAMLProviderListTypeDef
):
    """
    Type definition for `ClientListSamlProvidersResponse` `SAMLProviderList`

    Contains the list of SAML providers for this account.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the SAML provider.

    - **ValidUntil** *(datetime) --*

      The expiration date and time for the SAML provider.

    - **CreateDate** *(datetime) --*

      The date and time when the SAML provider was created.
    """


_ClientListSamlProvidersResponseTypeDef = TypedDict(
    "_ClientListSamlProvidersResponseTypeDef",
    {"SAMLProviderList": List[ClientListSamlProvidersResponseSAMLProviderListTypeDef]},
    total=False,
)


class ClientListSamlProvidersResponseTypeDef(_ClientListSamlProvidersResponseTypeDef):
    """
    Type definition for `ClientListSamlProviders` `Response`

    Contains the response to a successful  ListSAMLProviders request.

    - **SAMLProviderList** *(list) --*

      The list of SAML provider resource objects defined in IAM for this AWS account.

      - *(dict) --*

        Contains the list of SAML providers for this account.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the SAML provider.

        - **ValidUntil** *(datetime) --*

          The expiration date and time for the SAML provider.

        - **CreateDate** *(datetime) --*

          The date and time when the SAML provider was created.
    """


_ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef = TypedDict(
    "_ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef(
    _ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
):
    """
    Type definition for `ClientListServerCertificatesResponse` `ServerCertificateMetadataList`

    Contains information about a server certificate without its certificate body, certificate
    chain, and private key.

    This data type is used as a response element in the  UploadServerCertificate and
    ListServerCertificates operations.

    - **Path** *(string) --*

      The path to the server certificate. For more information about paths, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
      in the *IAM User Guide* .

    - **ServerCertificateName** *(string) --*

      The name that identifies the server certificate.

    - **ServerCertificateId** *(string) --*

      The stable and unique string identifying the server certificate. For more information
      about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the server certificate. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UploadDate** *(datetime) --*

      The date when the server certificate was uploaded.

    - **Expiration** *(datetime) --*

      The date on which the certificate is set to expire.
    """


_ClientListServerCertificatesResponseTypeDef = TypedDict(
    "_ClientListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ClientListServerCertificatesResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListServerCertificatesResponseTypeDef(
    _ClientListServerCertificatesResponseTypeDef
):
    """
    Type definition for `ClientListServerCertificates` `Response`

    Contains the response to a successful  ListServerCertificates request.

    - **ServerCertificateMetadataList** *(list) --*

      A list of server certificates.

      - *(dict) --*

        Contains information about a server certificate without its certificate body, certificate
        chain, and private key.

        This data type is used as a response element in the  UploadServerCertificate and
        ListServerCertificates operations.

        - **Path** *(string) --*

          The path to the server certificate. For more information about paths, see `IAM
          Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
          in the *IAM User Guide* .

        - **ServerCertificateName** *(string) --*

          The name that identifies the server certificate.

        - **ServerCertificateId** *(string) --*

          The stable and unique string identifying the server certificate. For more information
          about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the server certificate. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UploadDate** *(datetime) --*

          The date when the server certificate was uploaded.

        - **Expiration** *(datetime) --*

          The date on which the certificate is set to expire.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef = TypedDict(
    "_ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef",
    {
        "UserName": str,
        "Status": str,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
    total=False,
)


class ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef(
    _ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
):
    """
    Type definition for `ClientListServiceSpecificCredentialsResponse` `ServiceSpecificCredentials`

    Contains additional details about a service-specific credential.

    - **UserName** *(string) --*

      The name of the IAM user associated with the service-specific credential.

    - **Status** *(string) --*

      The status of the service-specific credential. ``Active`` means that the key is valid for
      API calls, while ``Inactive`` means it is not.

    - **ServiceUserName** *(string) --*

      The generated user name for the service-specific credential.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the service-specific credential were created.

    - **ServiceSpecificCredentialId** *(string) --*

      The unique identifier for the service-specific credential.

    - **ServiceName** *(string) --*

      The name of the service associated with the service-specific credential.
    """


_ClientListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "_ClientListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List[
            ClientListServiceSpecificCredentialsResponseServiceSpecificCredentialsTypeDef
        ]
    },
    total=False,
)


class ClientListServiceSpecificCredentialsResponseTypeDef(
    _ClientListServiceSpecificCredentialsResponseTypeDef
):
    """
    Type definition for `ClientListServiceSpecificCredentials` `Response`

    - **ServiceSpecificCredentials** *(list) --*

      A list of structures that each contain details about a service-specific credential.

      - *(dict) --*

        Contains additional details about a service-specific credential.

        - **UserName** *(string) --*

          The name of the IAM user associated with the service-specific credential.

        - **Status** *(string) --*

          The status of the service-specific credential. ``Active`` means that the key is valid for
          API calls, while ``Inactive`` means it is not.

        - **ServiceUserName** *(string) --*

          The generated user name for the service-specific credential.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the service-specific credential were created.

        - **ServiceSpecificCredentialId** *(string) --*

          The unique identifier for the service-specific credential.

        - **ServiceName** *(string) --*

          The name of the service associated with the service-specific credential.
    """


_ClientListSigningCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientListSigningCertificatesResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": str,
        "UploadDate": datetime,
    },
    total=False,
)


class ClientListSigningCertificatesResponseCertificatesTypeDef(
    _ClientListSigningCertificatesResponseCertificatesTypeDef
):
    """
    Type definition for `ClientListSigningCertificatesResponse` `Certificates`

    Contains information about an X.509 signing certificate.

    This data type is used as a response element in the  UploadSigningCertificate and
    ListSigningCertificates operations.

    - **UserName** *(string) --*

      The name of the user the signing certificate is associated with.

    - **CertificateId** *(string) --*

      The ID for the signing certificate.

    - **CertificateBody** *(string) --*

      The contents of the signing certificate.

    - **Status** *(string) --*

      The status of the signing certificate. ``Active`` means that the key is valid for API
      calls, while ``Inactive`` means it is not.

    - **UploadDate** *(datetime) --*

      The date when the signing certificate was uploaded.
    """


_ClientListSigningCertificatesResponseTypeDef = TypedDict(
    "_ClientListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List[ClientListSigningCertificatesResponseCertificatesTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListSigningCertificatesResponseTypeDef(
    _ClientListSigningCertificatesResponseTypeDef
):
    """
    Type definition for `ClientListSigningCertificates` `Response`

    Contains the response to a successful  ListSigningCertificates request.

    - **Certificates** *(list) --*

      A list of the user's signing certificate information.

      - *(dict) --*

        Contains information about an X.509 signing certificate.

        This data type is used as a response element in the  UploadSigningCertificate and
        ListSigningCertificates operations.

        - **UserName** *(string) --*

          The name of the user the signing certificate is associated with.

        - **CertificateId** *(string) --*

          The ID for the signing certificate.

        - **CertificateBody** *(string) --*

          The contents of the signing certificate.

        - **Status** *(string) --*

          The status of the signing certificate. ``Active`` means that the key is valid for API
          calls, while ``Inactive`` means it is not.

        - **UploadDate** *(datetime) --*

          The date when the signing certificate was uploaded.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListSshPublicKeysResponseSSHPublicKeysTypeDef = TypedDict(
    "_ClientListSshPublicKeysResponseSSHPublicKeysTypeDef",
    {"UserName": str, "SSHPublicKeyId": str, "Status": str, "UploadDate": datetime},
    total=False,
)


class ClientListSshPublicKeysResponseSSHPublicKeysTypeDef(
    _ClientListSshPublicKeysResponseSSHPublicKeysTypeDef
):
    """
    Type definition for `ClientListSshPublicKeysResponse` `SSHPublicKeys`

    Contains information about an SSH public key, without the key's body or fingerprint.

    This data type is used as a response element in the  ListSSHPublicKeys operation.

    - **UserName** *(string) --*

      The name of the IAM user associated with the SSH public key.

    - **SSHPublicKeyId** *(string) --*

      The unique identifier for the SSH public key.

    - **Status** *(string) --*

      The status of the SSH public key. ``Active`` means that the key can be used for
      authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot
      be used.

    - **UploadDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the SSH public key was uploaded.
    """


_ClientListSshPublicKeysResponseTypeDef = TypedDict(
    "_ClientListSshPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List[ClientListSshPublicKeysResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListSshPublicKeysResponseTypeDef(_ClientListSshPublicKeysResponseTypeDef):
    """
    Type definition for `ClientListSshPublicKeys` `Response`

    Contains the response to a successful  ListSSHPublicKeys request.

    - **SSHPublicKeys** *(list) --*

      A list of the SSH public keys assigned to IAM user.

      - *(dict) --*

        Contains information about an SSH public key, without the key's body or fingerprint.

        This data type is used as a response element in the  ListSSHPublicKeys operation.

        - **UserName** *(string) --*

          The name of the IAM user associated with the SSH public key.

        - **SSHPublicKeyId** *(string) --*

          The unique identifier for the SSH public key.

        - **Status** *(string) --*

          The status of the SSH public key. ``Active`` means that the key can be used for
          authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot
          be used.

        - **UploadDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the SSH public key was uploaded.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListUserPoliciesResponseTypeDef = TypedDict(
    "_ClientListUserPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "Marker": str},
    total=False,
)


class ClientListUserPoliciesResponseTypeDef(_ClientListUserPoliciesResponseTypeDef):
    """
    Type definition for `ClientListUserPolicies` `Response`

    Contains the response to a successful  ListUserPolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListUserTagsResponseTagsTypeDef = TypedDict(
    "_ClientListUserTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListUserTagsResponseTagsTypeDef(_ClientListUserTagsResponseTagsTypeDef):
    """
    Type definition for `ClientListUserTagsResponse` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must interpret
        the value in your code.
    """


_ClientListUserTagsResponseTypeDef = TypedDict(
    "_ClientListUserTagsResponseTypeDef",
    {
        "Tags": List[ClientListUserTagsResponseTagsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListUserTagsResponseTypeDef(_ClientListUserTagsResponseTypeDef):
    """
    Type definition for `ClientListUserTags` `Response`

    - **Tags** *(list) --*

      The list of tags that are currently attached to the user. Each tag consists of a key name and
      an associated value. If no tags are attached to the specified user, the response contains an
      empty list.

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must interpret
            the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can use the ``Marker`` request parameter to make a subsequent pagination request that
      retrieves more items. Note that IAM might return fewer than the ``MaxItems`` number of
      results even when more results are available. Check ``IsTruncated`` after every call to
      ensure that you receive all of your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListUsersResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListUsersResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListUsersResponseUsersPermissionsBoundaryTypeDef(
    _ClientListUsersResponseUsersPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientListUsersResponseUsers` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientListUsersResponseUsersTagsTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListUsersResponseUsersTagsTypeDef(_ClientListUsersResponseUsersTagsTypeDef):
    """
    Type definition for `ClientListUsersResponseUsers` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListUsersResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ClientListUsersResponseUsersTagsTypeDef],
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    Contains information about an IAM user entity.

    This data type is used as a response element in the following operations:

    *  CreateUser

    *  GetUser

    *  ListUsers

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the date
      and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "Users": List[ClientListUsersResponseUsersTypeDef],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    Contains the response to a successful  ListUsers request.

    - **Users** *(list) --*

      A list of users.

      - *(dict) --*

        Contains information about an IAM user entity.

        This data type is used as a response element in the following operations:

        *  CreateUser

        *  GetUser

        *  ListUsers

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
          and how to use ARNs in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **PasswordLastUsed** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user's password was last used to sign in to an AWS website. For a list of AWS
          websites that capture a user's last sign-in time, see the `Credential Reports
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
          the *IAM User Guide* . If a password is used more than once in a five-minute span, only
          the first use is returned in this field. If the field is null (no value), then it
          indicates that they never signed in with a password. This can be because:

          * The user never had a password.

          * A password exists but has not been used since IAM started tracking this information on
          October 20, 2014.

          A null value does not mean that the user *never* had a password. Also, if the user does
          not currently have a password but had one in the past, then this field contains the date
          and time the most recent password was used.

          This value is returned only in the  GetUser and  ListUsers operations.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientListVirtualMfaDevicesResponseVirtualMFADevicesUser` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used
      as the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef
):
    """
    Type definition for `ClientListVirtualMfaDevicesResponseVirtualMFADevicesUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store
        an array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef,
        "Tags": List[
            ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTagsTypeDef
        ],
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef
):
    """
    Type definition for `ClientListVirtualMfaDevicesResponseVirtualMFADevices` `User`

    The IAM user associated with this virtual MFA device.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about
      ARNs and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information
      on October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the
      date and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used
        as the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store
            an array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ClientListVirtualMfaDevicesResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef(
    _ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef
):
    """
    Type definition for `ClientListVirtualMfaDevicesResponse` `VirtualMFADevices`

    Contains information about a virtual MFA device.

    - **SerialNumber** *(string) --*

      The serial number associated with ``VirtualMFADevice`` .

    - **Base32StringSeed** *(bytes) --*

      The base32 seed defined as specified in `RFC3548
      <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

    - **QRCodePNG** *(bytes) --*

      A QR code PNG image that encodes
      ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
      ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the
      user name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed
      in base32 format. The ``Base32String`` value is base64-encoded.

    - **User** *(dict) --*

      The IAM user associated with this virtual MFA device.

      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **UserName** *(string) --*

        The friendly name identifying the user.

      - **UserId** *(string) --*

        The stable and unique string identifying the user. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the user. For more information about
        ARNs and how to use ARNs in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user was created.

      - **PasswordLastUsed** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user's password was last used to sign in to an AWS website. For a list of AWS
        websites that capture a user's last sign-in time, see the `Credential Reports
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
        the *IAM User Guide* . If a password is used more than once in a five-minute span, only
        the first use is returned in this field. If the field is null (no value), then it
        indicates that they never signed in with a password. This can be because:

        * The user never had a password.

        * A password exists but has not been used since IAM started tracking this information
        on October 20, 2014.

        A null value does not mean that the user *never* had a password. Also, if the user does
        not currently have a password but had one in the past, then this field contains the
        date and time the most recent password was used.

        This value is returned only in the  GetUser and  ListUsers operations.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the user.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
        in the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used
          as the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are associated with the specified user. For more information about
        tagging, see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a
          resource such as an IAM user or role. For more information about tagging, see
          `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For
            example, ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of
            ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
            ``Support`` . Tags with a key name of ``Cost Center`` might have values that
            consist of the number associated with the different cost centers in your company.
            Typically, many resources have tags with the same key name but with different
            values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store
              an array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

    - **EnableDate** *(datetime) --*

      The date and time on which the virtual MFA device was enabled.
    """


_ClientListVirtualMfaDevicesResponseTypeDef = TypedDict(
    "_ClientListVirtualMfaDevicesResponseTypeDef",
    {
        "VirtualMFADevices": List[
            ClientListVirtualMfaDevicesResponseVirtualMFADevicesTypeDef
        ],
        "IsTruncated": bool,
        "Marker": str,
    },
    total=False,
)


class ClientListVirtualMfaDevicesResponseTypeDef(
    _ClientListVirtualMfaDevicesResponseTypeDef
):
    """
    Type definition for `ClientListVirtualMfaDevices` `Response`

    Contains the response to a successful  ListVirtualMFADevices request.

    - **VirtualMFADevices** *(list) --*

      The list of virtual MFA devices in the current account that match the ``AssignmentStatus``
      value that was passed in the request.

      - *(dict) --*

        Contains information about a virtual MFA device.

        - **SerialNumber** *(string) --*

          The serial number associated with ``VirtualMFADevice`` .

        - **Base32StringSeed** *(bytes) --*

          The base32 seed defined as specified in `RFC3548
          <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

        - **QRCodePNG** *(bytes) --*

          A QR code PNG image that encodes
          ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
          ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the
          user name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed
          in base32 format. The ``Base32String`` value is base64-encoded.

        - **User** *(dict) --*

          The IAM user associated with this virtual MFA device.

          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **UserName** *(string) --*

            The friendly name identifying the user.

          - **UserId** *(string) --*

            The stable and unique string identifying the user. For more information about IDs, see
            `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the user. For more information about
            ARNs and how to use ARNs in policies, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **CreateDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the user was created.

          - **PasswordLastUsed** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the user's password was last used to sign in to an AWS website. For a list of AWS
            websites that capture a user's last sign-in time, see the `Credential Reports
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
            the *IAM User Guide* . If a password is used more than once in a five-minute span, only
            the first use is returned in this field. If the field is null (no value), then it
            indicates that they never signed in with a password. This can be because:

            * The user never had a password.

            * A password exists but has not been used since IAM started tracking this information
            on October 20, 2014.

            A null value does not mean that the user *never* had a password. Also, if the user does
            not currently have a password but had one in the past, then this field contains the
            date and time the most recent password was used.

            This value is returned only in the  GetUser and  ListUsers operations.

          - **PermissionsBoundary** *(dict) --*

            The ARN of the policy used to set the permissions boundary for the user.

            For more information about permissions boundaries, see `Permissions Boundaries for IAM
            Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
            in the *IAM User Guide* .

            - **PermissionsBoundaryType** *(string) --*

              The permissions boundary usage type that indicates what type of IAM resource is used
              as the permissions boundary for an entity. This data type can only have a value of
              ``Policy`` .

            - **PermissionsBoundaryArn** *(string) --*

              The ARN of the policy used to set the permissions boundary for the user or role.

          - **Tags** *(list) --*

            A list of tags that are associated with the specified user. For more information about
            tagging, see `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - *(dict) --*

              A structure that represents user-provided metadata that can be associated with a
              resource such as an IAM user or role. For more information about tagging, see
              `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - **Key** *(string) --*

                The key name that can be used to look up or retrieve the associated value. For
                example, ``Department`` or ``Cost Center`` are common choices.

              - **Value** *(string) --*

                The value associated with this tag. For example, tags with a key name of
                ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
                ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                consist of the number associated with the different cost centers in your company.
                Typically, many resources have tags with the same key name but with different
                values.

                .. note::

                  AWS always interprets the tag ``Value`` as a single string. If you need to store
                  an array, you can store comma-separated values in the string. However, you must
                  interpret the value in your code.

        - **EnableDate** *(datetime) --*

          The date and time on which the virtual MFA device was enabled.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **Marker** *(string) --*

      When ``IsTruncated`` is ``true`` , this element is present and contains the value to use for
      the ``Marker`` parameter in a subsequent pagination request.
    """


_ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef = TypedDict(
    "_ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": str,
    },
    total=False,
)


class ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef(
    _ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
):
    """
    Type definition for `ClientResetServiceSpecificCredentialResponse` `ServiceSpecificCredential`

    A structure with details about the updated service-specific credential, including the new
    password.

    .. warning::

      This is the **only** time that you can access the password. You cannot recover the password
      later, but you can reset it again.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the service-specific credential were created.

    - **ServiceName** *(string) --*

      The name of the service associated with the service-specific credential.

    - **ServiceUserName** *(string) --*

      The generated user name for the service-specific credential. This value is generated by
      combining the IAM user's name combined with the ID number of the AWS account, as in
      ``jane-at-123456789012`` , for example. This value cannot be configured by the user.

    - **ServicePassword** *(string) --*

      The generated password for the service-specific credential.

    - **ServiceSpecificCredentialId** *(string) --*

      The unique identifier for the service-specific credential.

    - **UserName** *(string) --*

      The name of the IAM user associated with the service-specific credential.

    - **Status** *(string) --*

      The status of the service-specific credential. ``Active`` means that the key is valid for
      API calls, while ``Inactive`` means it is not.
    """


_ClientResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "_ClientResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ClientResetServiceSpecificCredentialResponseServiceSpecificCredentialTypeDef
    },
    total=False,
)


class ClientResetServiceSpecificCredentialResponseTypeDef(
    _ClientResetServiceSpecificCredentialResponseTypeDef
):
    """
    Type definition for `ClientResetServiceSpecificCredential` `Response`

    - **ServiceSpecificCredential** *(dict) --*

      A structure with details about the updated service-specific credential, including the new
      password.

      .. warning::

        This is the **only** time that you can access the password. You cannot recover the password
        later, but you can reset it again.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the service-specific credential were created.

      - **ServiceName** *(string) --*

        The name of the service associated with the service-specific credential.

      - **ServiceUserName** *(string) --*

        The generated user name for the service-specific credential. This value is generated by
        combining the IAM user's name combined with the ID number of the AWS account, as in
        ``jane-at-123456789012`` , for example. This value cannot be configured by the user.

      - **ServicePassword** *(string) --*

        The generated password for the service-specific credential.

      - **ServiceSpecificCredentialId** *(string) --*

        The unique identifier for the service-specific credential.

      - **UserName** *(string) --*

        The name of the IAM user associated with the service-specific credential.

      - **Status** *(string) --*

        The status of the service-specific credential. ``Active`` means that the key is valid for
        API calls, while ``Inactive`` means it is not.
    """


_ClientSimulateCustomPolicyContextEntriesTypeDef = TypedDict(
    "_ClientSimulateCustomPolicyContextEntriesTypeDef",
    {"ContextKeyName": str, "ContextKeyValues": List[str], "ContextKeyType": str},
    total=False,
)


class ClientSimulateCustomPolicyContextEntriesTypeDef(
    _ClientSimulateCustomPolicyContextEntriesTypeDef
):
    """
    Type definition for `ClientSimulateCustomPolicy` `ContextEntries`

    Contains information about a condition context key. It includes the name of the key and
    specifies the value (or values, if the context key supports multiple values) to use in the
    simulation. This information is used when evaluating the ``Condition`` elements of the input
    policies.

    This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
    SimulatePrincipalPolicy `` .

    - **ContextKeyName** *(string) --*

      The full name of a condition context key, including the service prefix. For example,
      ``aws:SourceIp`` or ``s3:VersionId`` .

    - **ContextKeyValues** *(list) --*

      The value (or values, if the condition context key supports multiple values) to provide to
      the simulation when the key is referenced by a ``Condition`` element in an input policy.

      - *(string) --*

    - **ContextKeyType** *(string) --*

      The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
    """


_ClientSimulatePrincipalPolicyContextEntriesTypeDef = TypedDict(
    "_ClientSimulatePrincipalPolicyContextEntriesTypeDef",
    {"ContextKeyName": str, "ContextKeyValues": List[str], "ContextKeyType": str},
    total=False,
)


class ClientSimulatePrincipalPolicyContextEntriesTypeDef(
    _ClientSimulatePrincipalPolicyContextEntriesTypeDef
):
    """
    Type definition for `ClientSimulatePrincipalPolicy` `ContextEntries`

    Contains information about a condition context key. It includes the name of the key and
    specifies the value (or values, if the context key supports multiple values) to use in the
    simulation. This information is used when evaluating the ``Condition`` elements of the input
    policies.

    This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
    SimulatePrincipalPolicy `` .

    - **ContextKeyName** *(string) --*

      The full name of a condition context key, including the service prefix. For example,
      ``aws:SourceIp`` or ``s3:VersionId`` .

    - **ContextKeyValues** *(list) --*

      The value (or values, if the condition context key supports multiple values) to provide to
      the simulation when the key is referenced by a ``Condition`` element in an input policy.

      - *(string) --*

    - **ContextKeyType** *(string) --*

      The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
    """


_ClientTagRoleTagsTypeDef = TypedDict(
    "_ClientTagRoleTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagRoleTagsTypeDef(_ClientTagRoleTagsTypeDef):
    """
    Type definition for `ClientTagRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_ClientTagUserTagsTypeDef = TypedDict(
    "_ClientTagUserTagsTypeDef", {"Key": str, "Value": str}
)


class ClientTagUserTagsTypeDef(_ClientTagUserTagsTypeDef):
    """
    Type definition for `ClientTagUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef(
    _ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef
):
    """
    Type definition for `ClientUpdateRoleDescriptionResponseRole` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef
):
    """
    Type definition for `ClientUpdateRoleDescriptionResponseRole` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the date
    and time and the Region in which the role was last used. Activity is only reported for the
    trailing 400 days. This period can be shorter if your Region began supporting these
    features within the last year. The role might have been used more than 400 days ago. For
    more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
      the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For more
      information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ClientUpdateRoleDescriptionResponseRoleTagsTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateRoleDescriptionResponseRoleTagsTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleTagsTypeDef
):
    """
    Type definition for `ClientUpdateRoleDescriptionResponseRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource
    such as an IAM user or role. For more information about tagging, see `Tagging IAM
    Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of ``Department``
      could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
      with a key name of ``Cost Center`` might have values that consist of the number
      associated with the different cost centers in your company. Typically, many resources
      have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ClientUpdateRoleDescriptionResponseRoleTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseRoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ClientUpdateRoleDescriptionResponseRolePermissionsBoundaryTypeDef,
        "Tags": List[ClientUpdateRoleDescriptionResponseRoleTagsTypeDef],
        "RoleLastUsed": ClientUpdateRoleDescriptionResponseRoleRoleLastUsedTypeDef,
    },
    total=False,
)


class ClientUpdateRoleDescriptionResponseRoleTypeDef(
    _ClientUpdateRoleDescriptionResponseRoleTypeDef
):
    """
    Type definition for `ClientUpdateRoleDescriptionResponse` `Role`

    A structure that contains details about the modified role.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
      to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about tagging,
      see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a resource
        such as an IAM user or role. For more information about tagging, see `Tagging IAM
        Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For example,
          ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of ``Department``
          could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
          with a key name of ``Cost Center`` might have values that consist of the number
          associated with the different cost centers in your company. Typically, many resources
          have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the date
      and time and the Region in which the role was last used. Activity is only reported for the
      trailing 400 days. This period can be shorter if your Region began supporting these
      features within the last year. The role might have been used more than 400 days ago. For
      more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
        the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For more
        information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ClientUpdateRoleDescriptionResponseTypeDef = TypedDict(
    "_ClientUpdateRoleDescriptionResponseTypeDef",
    {"Role": ClientUpdateRoleDescriptionResponseRoleTypeDef},
    total=False,
)


class ClientUpdateRoleDescriptionResponseTypeDef(
    _ClientUpdateRoleDescriptionResponseTypeDef
):
    """
    Type definition for `ClientUpdateRoleDescription` `Response`

    - **Role** *(dict) --*

      A structure that contains details about the modified role.

      - **Path** *(string) --*

        The path to the role. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **RoleName** *(string) --*

        The friendly name that identifies the role.

      - **RoleId** *(string) --*

        The stable and unique string identifying the role. For more information about IDs, see `IAM
        Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
        the *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how
        to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* guide.

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the role was created.

      - **AssumeRolePolicyDocument** *(string) --*

        The policy that grants an entity permission to assume the role.

      - **Description** *(string) --*

        A description of the role that you provide.

      - **MaxSessionDuration** *(integer) --*

        The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
        CLI, or API to assume the role can specify the duration using the optional
        ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the role.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
        the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used as
          the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are attached to the specified role. For more information about tagging,
        see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a resource
          such as an IAM user or role. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For example,
            ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of ``Department``
            could have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags
            with a key name of ``Cost Center`` might have values that consist of the number
            associated with the different cost centers in your company. Typically, many resources
            have tags with the same key name but with different values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store an
              array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

      - **RoleLastUsed** *(dict) --*

        Contains information about the last time that an IAM role was used. This includes the date
        and time and the Region in which the role was last used. Activity is only reported for the
        trailing 400 days. This period can be shorter if your Region began supporting these
        features within the last year. The role might have been used more than 400 days ago. For
        more information, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

        - **LastUsedDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ that
          the role was last used.

          This field is null if the role has not been used within the IAM tracking period. For more
          information about the tracking period, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

        - **Region** *(string) --*

          The name of the AWS Region in which the role was last used.
    """


_ClientUpdateSamlProviderResponseTypeDef = TypedDict(
    "_ClientUpdateSamlProviderResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class ClientUpdateSamlProviderResponseTypeDef(_ClientUpdateSamlProviderResponseTypeDef):
    """
    Type definition for `ClientUpdateSamlProvider` `Response`

    Contains the response to a successful  UpdateSAMLProvider request.

    - **SAMLProviderArn** *(string) --*

      The Amazon Resource Name (ARN) of the SAML provider that was updated.
    """


_ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef = TypedDict(
    "_ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef(
    _ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
):
    """
    Type definition for `ClientUploadServerCertificateResponse` `ServerCertificateMetadata`

    The meta information of the uploaded server certificate without its certificate body,
    certificate chain, and private key.

    - **Path** *(string) --*

      The path to the server certificate. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **ServerCertificateName** *(string) --*

      The name that identifies the server certificate.

    - **ServerCertificateId** *(string) --*

      The stable and unique string identifying the server certificate. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the server certificate. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UploadDate** *(datetime) --*

      The date when the server certificate was uploaded.

    - **Expiration** *(datetime) --*

      The date on which the certificate is set to expire.
    """


_ClientUploadServerCertificateResponseTypeDef = TypedDict(
    "_ClientUploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": ClientUploadServerCertificateResponseServerCertificateMetadataTypeDef
    },
    total=False,
)


class ClientUploadServerCertificateResponseTypeDef(
    _ClientUploadServerCertificateResponseTypeDef
):
    """
    Type definition for `ClientUploadServerCertificate` `Response`

    Contains the response to a successful  UploadServerCertificate request.

    - **ServerCertificateMetadata** *(dict) --*

      The meta information of the uploaded server certificate without its certificate body,
      certificate chain, and private key.

      - **Path** *(string) --*

        The path to the server certificate. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **ServerCertificateName** *(string) --*

        The name that identifies the server certificate.

      - **ServerCertificateId** *(string) --*

        The stable and unique string identifying the server certificate. For more information about
        IDs, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the server certificate. For more information
        about ARNs and how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **UploadDate** *(datetime) --*

        The date when the server certificate was uploaded.

      - **Expiration** *(datetime) --*

        The date on which the certificate is set to expire.
    """


_ClientUploadSigningCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientUploadSigningCertificateResponseCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": str,
        "UploadDate": datetime,
    },
    total=False,
)


class ClientUploadSigningCertificateResponseCertificateTypeDef(
    _ClientUploadSigningCertificateResponseCertificateTypeDef
):
    """
    Type definition for `ClientUploadSigningCertificateResponse` `Certificate`

    Information about the certificate.

    - **UserName** *(string) --*

      The name of the user the signing certificate is associated with.

    - **CertificateId** *(string) --*

      The ID for the signing certificate.

    - **CertificateBody** *(string) --*

      The contents of the signing certificate.

    - **Status** *(string) --*

      The status of the signing certificate. ``Active`` means that the key is valid for API
      calls, while ``Inactive`` means it is not.

    - **UploadDate** *(datetime) --*

      The date when the signing certificate was uploaded.
    """


_ClientUploadSigningCertificateResponseTypeDef = TypedDict(
    "_ClientUploadSigningCertificateResponseTypeDef",
    {"Certificate": ClientUploadSigningCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientUploadSigningCertificateResponseTypeDef(
    _ClientUploadSigningCertificateResponseTypeDef
):
    """
    Type definition for `ClientUploadSigningCertificate` `Response`

    Contains the response to a successful  UploadSigningCertificate request.

    - **Certificate** *(dict) --*

      Information about the certificate.

      - **UserName** *(string) --*

        The name of the user the signing certificate is associated with.

      - **CertificateId** *(string) --*

        The ID for the signing certificate.

      - **CertificateBody** *(string) --*

        The contents of the signing certificate.

      - **Status** *(string) --*

        The status of the signing certificate. ``Active`` means that the key is valid for API
        calls, while ``Inactive`` means it is not.

      - **UploadDate** *(datetime) --*

        The date when the signing certificate was uploaded.
    """


_ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef = TypedDict(
    "_ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": str,
        "UploadDate": datetime,
    },
    total=False,
)


class ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef(
    _ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef
):
    """
    Type definition for `ClientUploadSshPublicKeyResponse` `SSHPublicKey`

    Contains information about the SSH public key.

    - **UserName** *(string) --*

      The name of the IAM user associated with the SSH public key.

    - **SSHPublicKeyId** *(string) --*

      The unique identifier for the SSH public key.

    - **Fingerprint** *(string) --*

      The MD5 message digest of the SSH public key.

    - **SSHPublicKeyBody** *(string) --*

      The SSH public key.

    - **Status** *(string) --*

      The status of the SSH public key. ``Active`` means that the key can be used for
      authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot be
      used.

    - **UploadDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the SSH public key was uploaded.
    """


_ClientUploadSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientUploadSshPublicKeyResponseTypeDef",
    {"SSHPublicKey": ClientUploadSshPublicKeyResponseSSHPublicKeyTypeDef},
    total=False,
)


class ClientUploadSshPublicKeyResponseTypeDef(_ClientUploadSshPublicKeyResponseTypeDef):
    """
    Type definition for `ClientUploadSshPublicKey` `Response`

    Contains the response to a successful  UploadSSHPublicKey request.

    - **SSHPublicKey** *(dict) --*

      Contains information about the SSH public key.

      - **UserName** *(string) --*

        The name of the IAM user associated with the SSH public key.

      - **SSHPublicKeyId** *(string) --*

        The unique identifier for the SSH public key.

      - **Fingerprint** *(string) --*

        The MD5 message digest of the SSH public key.

      - **SSHPublicKeyBody** *(string) --*

        The SSH public key.

      - **Status** *(string) --*

        The status of the SSH public key. ``Active`` means that the key can be used for
        authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot be
        used.

      - **UploadDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the SSH public key was uploaded.
    """


_GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef(
    _GetAccountAuthorizationDetailsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseGroupDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseGroupDetailList` `GroupPolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
        "GroupPolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListGroupPolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListAttachedManagedPoliciesTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponse` `GroupDetailList`

    Contains information about an IAM group, including all of the group's policies.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.

    - **GroupPolicyList** *(list) --*

      A list of the inline policies embedded in the group.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **AttachedManagedPolicies** *(list) --*

      A list of the managed policies attached to the group.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .
    """


_GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponsePolicies` `PolicyVersionList`

    Contains information about a version of a managed policy.

    This data type is used as a response element in the  CreatePolicyVersion ,
    GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC
      3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
      convert the policy back to plain JSON text. For example, if you use Java, you can use
      the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
      Other languages and SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy
      is created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the policy version was created.
    """


_GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "PolicyVersionList": List[
            GetAccountAuthorizationDetailsPaginateResponsePoliciesPolicyVersionListTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponse` `Policies`

    Contains information about a managed policy, including the policy's ARN, versions, and the
    number of principal entities (users, groups, and roles) that the policy is attached to.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    For more information about managed policies, see `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default (operative)
      version.

      For more information about policy versions, see `Versioning for Managed Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in
      the *IAM User Guide* .

    - **AttachmentCount** *(integer) --*

      The number of principal entities (users, groups, and roles) that the policy is attached
      to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used as the permissions
      boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and
      time when the most recent policy version was created.

    - **PolicyVersionList** *(list) --*

      A list containing information about the versions of the policy.

      - *(dict) --*

        Contains information about a version of a managed policy.

        This data type is used as a response element in the  CreatePolicyVersion ,
        GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **Document** *(string) --*

          The policy document.

          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.

          The policy document returned in this structure is URL-encoded compliant with `RFC
          3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
          convert the policy back to plain JSON text. For example, if you use Java, you can use
          the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
          Other languages and SDKs provide similar functionality.

        - **VersionId** *(string) --*

          The identifier for the policy version.

          Policy version identifiers always begin with ``v`` (always lowercase). When a policy
          is created, the first policy version is ``v1`` .

        - **IsDefaultVersion** *(boolean) --*

          Specifies whether the policy version is set as the policy's default version.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the policy version was created.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries
    for IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes
    the date and time and the Region in which the role was last used. Activity is
    only reported for the trailing 400 days. This period can be shorter if your
    Region began supporting these features within the last year. The role might have
    been used more than 400 days ago. For more information, see `Regions Where Data
    Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking
      period. For more information about the tracking period, see `Regions Where Data
      Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with
    a resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
    User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value.
      For example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting``
      , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
      that consist of the number associated with the different cost centers in your
      company. Typically, many resources have tags with the same key name but with
      different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string.
        However, you must interpret the value in your code.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTagsTypeDef
        ],
        "RoleLastUsed": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileList` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about
      ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
      the *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses
      the AWS CLI, or API to assume the role can specify the duration using the
      optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries
      for IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information
      about tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
      User Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with
        a resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
        User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value.
          For example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting``
          , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
          that consist of the number associated with the different cost centers in your
          company. Typically, many resources have tags with the same key name but with
          different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string.
            However, you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes
      the date and time and the Region in which the role was last used. Activity is
      only reported for the trailing 400 days. This period can be shorter if your
      Region began supporting these features within the last year. The role might have
      been used more than 400 days ago. For more information, see `Regions Where Data
      Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking
        period. For more information about the tracking period, see `Regions Where Data
        Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListRolesTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `InstanceProfileList`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM
      Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information
      about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about
          ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
          the *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format
          <http://www.iso.org/iso/iso8601>`__ , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses
          the AWS CLI, or API to assume the role can specify the duration using the
          optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries
          for IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information
          about tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with
            a resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
            User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value.
              For example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting``
              , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
              that consist of the number associated with the different cost centers in your
              company. Typically, many resources have tags with the same key name but with
              different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string.
                However, you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes
          the date and time and the Region in which the role was last used. Activity is
          only reported for the trailing 400 days. This period can be shorter if your
          Region began supporting these features within the last year. The role might have
          been used more than 400 days ago. For more information, see `Regions Where Data
          Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking
            period. For more information about the tracking period, see `Regions Where Data
            Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `RolePolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseRoleDetailList` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "InstanceProfileList": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListInstanceProfileListTypeDef
        ],
        "RolePolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRolePolicyListTypeDef
        ],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListPermissionsBoundaryTypeDef,
        "Tags": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTagsTypeDef
        ],
        "RoleLastUsed": GetAccountAuthorizationDetailsPaginateResponseRoleDetailListRoleLastUsedTypeDef,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponse` `RoleDetailList`

    Contains information about an IAM role, including all of the role's policies.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The trust policy that grants permission to assume the role.

    - **InstanceProfileList** *(list) --*

      A list of instance profiles that contain this role.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM
          Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information
          about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about
              IDs, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about
              ARNs and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
              the *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format
              <http://www.iso.org/iso/iso8601>`__ , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses
              the AWS CLI, or API to assume the role can specify the duration using the
              optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries
              for IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information
              about tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
              User Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with
                a resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                User Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value.
                  For example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting``
                  , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
                  that consist of the number associated with the different cost centers in your
                  company. Typically, many resources have tags with the same key name but with
                  different values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string.
                    However, you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes
              the date and time and the Region in which the role was last used. Activity is
              only reported for the trailing 400 days. This period can be shorter if your
              Region began supporting these features within the last year. The role might have
              been used more than 400 days ago. For more information, see `Regions Where Data
              Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking
                period. For more information about the tracking period, see `Regions Where Data
                Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **RolePolicyList** *(list) --*

      A list of inline policies embedded in the role. These policies are the role's access
      (permissions) policies.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **AttachedManagedPolicies** *(list) --*

      A list of managed policies attached to the role. These policies are the role's access
      (permissions) policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseUserDetailList` `AttachedManagedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or
    role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
    GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline
    Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
    in the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
      the *AWS General Reference* .
    """


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseUserDetailList` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseUserDetailList` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef",
    {"PolicyName": str, "PolicyDocument": str},
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponseUserDetailList` `UserPolicyList`

    Contains information about an IAM policy, including the policy document.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyDocument** *(string) --*

      The policy document.
    """


_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "UserPolicyList": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListUserPolicyListTypeDef
        ],
        "GroupList": List[str],
        "AttachedManagedPolicies": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListAttachedManagedPoliciesTypeDef
        ],
        "PermissionsBoundary": GetAccountAuthorizationDetailsPaginateResponseUserDetailListPermissionsBoundaryTypeDef,
        "Tags": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListTagsTypeDef
        ],
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginateResponse` `UserDetailList`

    Contains information about an IAM user, including all the user's policies and all the IAM
    groups the user is in.

    This data type is used as a response element in the  GetAccountAuthorizationDetails
    operation.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **UserPolicyList** *(list) --*

      A list of the inline policies embedded in the user.

      - *(dict) --*

        Contains information about an IAM policy, including the policy document.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyDocument** *(string) --*

          The policy document.

    - **GroupList** *(list) --*

      A list of IAM groups that the user is in.

      - *(string) --*

    - **AttachedManagedPolicies** *(list) --*

      A list of the managed policies attached to the user.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or
        role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
        GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
        in the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
          the *AWS General Reference* .

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_GetAccountAuthorizationDetailsPaginateResponseTypeDef = TypedDict(
    "_GetAccountAuthorizationDetailsPaginateResponseTypeDef",
    {
        "UserDetailList": List[
            GetAccountAuthorizationDetailsPaginateResponseUserDetailListTypeDef
        ],
        "GroupDetailList": List[
            GetAccountAuthorizationDetailsPaginateResponseGroupDetailListTypeDef
        ],
        "RoleDetailList": List[
            GetAccountAuthorizationDetailsPaginateResponseRoleDetailListTypeDef
        ],
        "Policies": List[GetAccountAuthorizationDetailsPaginateResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class GetAccountAuthorizationDetailsPaginateResponseTypeDef(
    _GetAccountAuthorizationDetailsPaginateResponseTypeDef
):
    """
    Type definition for `GetAccountAuthorizationDetailsPaginate` `Response`

    Contains the response to a successful  GetAccountAuthorizationDetails request.

    - **UserDetailList** *(list) --*

      A list containing information about IAM users.

      - *(dict) --*

        Contains information about an IAM user, including all the user's policies and all the IAM
        groups the user is in.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **UserPolicyList** *(list) --*

          A list of the inline policies embedded in the user.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **GroupList** *(list) --*

          A list of IAM groups that the user is in.

          - *(string) --*

        - **AttachedManagedPolicies** *(list) --*

          A list of the managed policies attached to the user.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **GroupDetailList** *(list) --*

      A list containing information about IAM groups.

      - *(dict) --*

        Contains information about an IAM group, including all of the group's policies.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

        - **GroupPolicyList** *(list) --*

          A list of the inline policies embedded in the group.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **AttachedManagedPolicies** *(list) --*

          A list of the managed policies attached to the group.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

    - **RoleDetailList** *(list) --*

      A list containing information about IAM roles.

      - *(dict) --*

        Contains information about an IAM role, including all of the role's policies.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The trust policy that grants permission to assume the role.

        - **InstanceProfileList** *(list) --*

          A list of instance profiles that contain this role.

          - *(dict) --*

            Contains information about an instance profile.

            This data type is used as a response element in the following operations:

            *  CreateInstanceProfile

            *  GetInstanceProfile

            *  ListInstanceProfiles

            *  ListInstanceProfilesForRole

            - **Path** *(string) --*

              The path to the instance profile. For more information about paths, see `IAM
              Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **InstanceProfileName** *(string) --*

              The name identifying the instance profile.

            - **InstanceProfileId** *(string) --*

              The stable and unique string identifying the instance profile. For more information
              about IDs, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the instance profile. For more information
              about ARNs and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **CreateDate** *(datetime) --*

              The date when the instance profile was created.

            - **Roles** *(list) --*

              The role associated with the instance profile.

              - *(dict) --*

                Contains information about an IAM role. This structure is returned as a response
                element in several API operations that interact with roles.

                - **Path** *(string) --*

                  The path to the role. For more information about paths, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* .

                - **RoleName** *(string) --*

                  The friendly name that identifies the role.

                - **RoleId** *(string) --*

                  The stable and unique string identifying the role. For more information about
                  IDs, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) specifying the role. For more information about
                  ARNs and how to use them in policies, see `IAM Identifiers
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in
                  the *IAM User Guide* guide.

                - **CreateDate** *(datetime) --*

                  The date and time, in `ISO 8601 date-time format
                  <http://www.iso.org/iso/iso8601>`__ , when the role was created.

                - **AssumeRolePolicyDocument** *(string) --*

                  The policy that grants an entity permission to assume the role.

                - **Description** *(string) --*

                  A description of the role that you provide.

                - **MaxSessionDuration** *(integer) --*

                  The maximum session duration (in seconds) for the specified role. Anyone who uses
                  the AWS CLI, or API to assume the role can specify the duration using the
                  optional ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

                - **PermissionsBoundary** *(dict) --*

                  The ARN of the policy used to set the permissions boundary for the role.

                  For more information about permissions boundaries, see `Permissions Boundaries
                  for IAM Identities
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
                  in the *IAM User Guide* .

                  - **PermissionsBoundaryType** *(string) --*

                    The permissions boundary usage type that indicates what type of IAM resource is
                    used as the permissions boundary for an entity. This data type can only have a
                    value of ``Policy`` .

                  - **PermissionsBoundaryArn** *(string) --*

                    The ARN of the policy used to set the permissions boundary for the user or role.

                - **Tags** *(list) --*

                  A list of tags that are attached to the specified role. For more information
                  about tagging, see `Tagging IAM Identities
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                  User Guide* .

                  - *(dict) --*

                    A structure that represents user-provided metadata that can be associated with
                    a resource such as an IAM user or role. For more information about tagging, see
                    `Tagging IAM Identities
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
                    User Guide* .

                    - **Key** *(string) --*

                      The key name that can be used to look up or retrieve the associated value.
                      For example, ``Department`` or ``Cost Center`` are common choices.

                    - **Value** *(string) --*

                      The value associated with this tag. For example, tags with a key name of
                      ``Department`` could have values such as ``Human Resources`` , ``Accounting``
                      , and ``Support`` . Tags with a key name of ``Cost Center`` might have values
                      that consist of the number associated with the different cost centers in your
                      company. Typically, many resources have tags with the same key name but with
                      different values.

                      .. note::

                        AWS always interprets the tag ``Value`` as a single string. If you need to
                        store an array, you can store comma-separated values in the string.
                        However, you must interpret the value in your code.

                - **RoleLastUsed** *(dict) --*

                  Contains information about the last time that an IAM role was used. This includes
                  the date and time and the Region in which the role was last used. Activity is
                  only reported for the trailing 400 days. This period can be shorter if your
                  Region began supporting these features within the last year. The role might have
                  been used more than 400 days ago. For more information, see `Regions Where Data
                  Is Tracked
                  <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                  in the *IAM User Guide* .

                  - **LastUsedDate** *(datetime) --*

                    The date and time, in `ISO 8601 date-time format
                    <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                    This field is null if the role has not been used within the IAM tracking
                    period. For more information about the tracking period, see `Regions Where Data
                    Is Tracked
                    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                    in the *IAM User Guide* .

                  - **Region** *(string) --*

                    The name of the AWS Region in which the role was last used.

        - **RolePolicyList** *(list) --*

          A list of inline policies embedded in the role. These policies are the role's access
          (permissions) policies.

          - *(dict) --*

            Contains information about an IAM policy, including the policy document.

            This data type is used as a response element in the  GetAccountAuthorizationDetails
            operation.

            - **PolicyName** *(string) --*

              The name of the policy.

            - **PolicyDocument** *(string) --*

              The policy document.

        - **AttachedManagedPolicies** *(list) --*

          A list of managed policies attached to the role. These policies are the role's access
          (permissions) policies.

          - *(dict) --*

            Contains information about an attached policy.

            An attached policy is a managed policy that has been attached to a user, group, or
            role. This data type is used as a response element in the  ListAttachedGroupPolicies ,
            ListAttachedRolePolicies ,  ListAttachedUserPolicies , and
            GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **PolicyName** *(string) --*

              The friendly name of the attached policy.

            - **PolicyArn** *(string) --*

              The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

              For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
              Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
              the *AWS General Reference* .

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.

    - **Policies** *(list) --*

      A list containing information about managed policies.

      - *(dict) --*

        Contains information about a managed policy, including the policy's ARN, versions, and the
        number of principal entities (users, groups, and roles) that the policy is attached to.

        This data type is used as a response element in the  GetAccountAuthorizationDetails
        operation.

        For more information about managed policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.

        - **PolicyId** *(string) --*

          The stable and unique string identifying the policy.

          For more information about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **Path** *(string) --*

          The path to the policy.

          For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **DefaultVersionId** *(string) --*

          The identifier for the version of the policy that is set as the default (operative)
          version.

          For more information about policy versions, see `Versioning for Managed Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in
          the *IAM User Guide* .

        - **AttachmentCount** *(integer) --*

          The number of principal entities (users, groups, and roles) that the policy is attached
          to.

        - **PermissionsBoundaryUsageCount** *(integer) --*

          The number of entities (users and roles) for which the policy is used as the permissions
          boundary.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

        - **IsAttachable** *(boolean) --*

          Specifies whether the policy can be attached to an IAM user, group, or role.

        - **Description** *(string) --*

          A friendly description of the policy.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was created.

        - **UpdateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was last updated.

          When a policy has only one version, this field contains the date and time when the policy
          was created. When a policy has more than one version, this field contains the date and
          time when the most recent policy version was created.

        - **PolicyVersionList** *(list) --*

          A list containing information about the versions of the policy.

          - *(dict) --*

            Contains information about a version of a managed policy.

            This data type is used as a response element in the  CreatePolicyVersion ,
            GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

            For more information about managed policies, refer to `Managed Policies and Inline
            Policies
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__
            in the *IAM User Guide* .

            - **Document** *(string) --*

              The policy document.

              The policy document is returned in the response to the  GetPolicyVersion and
              GetAccountAuthorizationDetails operations. It is not returned in the response to the
              CreatePolicyVersion or  ListPolicyVersions operations.

              The policy document returned in this structure is URL-encoded compliant with `RFC
              3986 <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to
              convert the policy back to plain JSON text. For example, if you use Java, you can use
              the ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK.
              Other languages and SDKs provide similar functionality.

            - **VersionId** *(string) --*

              The identifier for the policy version.

              Policy version identifiers always begin with ``v`` (always lowercase). When a policy
              is created, the first policy version is ``v1`` .

            - **IsDefaultVersion** *(boolean) --*

              Specifies whether the policy version is set as the policy's default version.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetGroupPaginatePaginationConfigTypeDef(_GetGroupPaginatePaginationConfigTypeDef):
    """
    Type definition for `GetGroupPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_GetGroupPaginateResponseGroupTypeDef = TypedDict(
    "_GetGroupPaginateResponseGroupTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class GetGroupPaginateResponseGroupTypeDef(_GetGroupPaginateResponseGroupTypeDef):
    """
    Type definition for `GetGroupPaginateResponse` `Group`

    A structure that contains details about the group.

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
      the group was created.
    """


_GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef(
    _GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef
):
    """
    Type definition for `GetGroupPaginateResponseUsers` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_GetGroupPaginateResponseUsersTagsTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class GetGroupPaginateResponseUsersTagsTypeDef(
    _GetGroupPaginateResponseUsersTagsTypeDef
):
    """
    Type definition for `GetGroupPaginateResponseUsers` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_GetGroupPaginateResponseUsersTypeDef = TypedDict(
    "_GetGroupPaginateResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": GetGroupPaginateResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[GetGroupPaginateResponseUsersTagsTypeDef],
    },
    total=False,
)


class GetGroupPaginateResponseUsersTypeDef(_GetGroupPaginateResponseUsersTypeDef):
    """
    Type definition for `GetGroupPaginateResponse` `Users`

    Contains information about an IAM user entity.

    This data type is used as a response element in the following operations:

    *  CreateUser

    *  GetUser

    *  ListUsers

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the date
      and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_GetGroupPaginateResponseTypeDef = TypedDict(
    "_GetGroupPaginateResponseTypeDef",
    {
        "Group": GetGroupPaginateResponseGroupTypeDef,
        "Users": List[GetGroupPaginateResponseUsersTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class GetGroupPaginateResponseTypeDef(_GetGroupPaginateResponseTypeDef):
    """
    Type definition for `GetGroupPaginate` `Response`

    Contains the response to a successful  GetGroup request.

    - **Group** *(dict) --*

      A structure that contains details about the group.

      - **Path** *(string) --*

        The path to the group. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **GroupName** *(string) --*

        The friendly name that identifies the group.

      - **GroupId** *(string) --*

        The stable and unique string identifying the group. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
        how to use them in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
        User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ , when
        the group was created.

    - **Users** *(list) --*

      A list of users in the group.

      - *(dict) --*

        Contains information about an IAM user entity.

        This data type is used as a response element in the following operations:

        *  CreateUser

        *  GetUser

        *  ListUsers

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
          and how to use ARNs in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **PasswordLastUsed** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user's password was last used to sign in to an AWS website. For a list of AWS
          websites that capture a user's last sign-in time, see the `Credential Reports
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
          the *IAM User Guide* . If a password is used more than once in a five-minute span, only
          the first use is returned in this field. If the field is null (no value), then it
          indicates that they never signed in with a password. This can be because:

          * The user never had a password.

          * A password exists but has not been used since IAM started tracking this information on
          October 20, 2014.

          A null value does not mean that the user *never* had a password. Also, if the user does
          not currently have a password but had one in the past, then this field contains the date
          and time the most recent password was used.

          This value is returned only in the  GetUser and  ListUsers operations.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_InstanceProfileExistsWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceProfileExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceProfileExistsWaitWaiterConfigTypeDef(
    _InstanceProfileExistsWaitWaiterConfigTypeDef
):
    """
    Type definition for `InstanceProfileExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_ListAccessKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccessKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccessKeysPaginatePaginationConfigTypeDef(
    _ListAccessKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAccessKeysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef = TypedDict(
    "_ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef",
    {"UserName": str, "AccessKeyId": str, "Status": str, "CreateDate": datetime},
    total=False,
)


class ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef(
    _ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef
):
    """
    Type definition for `ListAccessKeysPaginateResponse` `AccessKeyMetadata`

    Contains information about an AWS access key, without its secret key.

    This data type is used as a response element in the  ListAccessKeys operation.

    - **UserName** *(string) --*

      The name of the IAM user that the key is associated with.

    - **AccessKeyId** *(string) --*

      The ID for this access key.

    - **Status** *(string) --*

      The status of the access key. ``Active`` means that the key is valid for API calls;
      ``Inactive`` means it is not.

    - **CreateDate** *(datetime) --*

      The date when the access key was created.
    """


_ListAccessKeysPaginateResponseTypeDef = TypedDict(
    "_ListAccessKeysPaginateResponseTypeDef",
    {
        "AccessKeyMetadata": List[
            ListAccessKeysPaginateResponseAccessKeyMetadataTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAccessKeysPaginateResponseTypeDef(_ListAccessKeysPaginateResponseTypeDef):
    """
    Type definition for `ListAccessKeysPaginate` `Response`

    Contains the response to a successful  ListAccessKeys request.

    - **AccessKeyMetadata** *(list) --*

      A list of objects containing metadata about the access keys.

      - *(dict) --*

        Contains information about an AWS access key, without its secret key.

        This data type is used as a response element in the  ListAccessKeys operation.

        - **UserName** *(string) --*

          The name of the IAM user that the key is associated with.

        - **AccessKeyId** *(string) --*

          The ID for this access key.

        - **Status** *(string) --*

          The status of the access key. ``Active`` means that the key is valid for API calls;
          ``Inactive`` means it is not.

        - **CreateDate** *(datetime) --*

          The date when the access key was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAccountAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAccountAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAccountAliasesPaginatePaginationConfigTypeDef(
    _ListAccountAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAccountAliasesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAccountAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAccountAliasesPaginateResponseTypeDef",
    {"AccountAliases": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListAccountAliasesPaginateResponseTypeDef(
    _ListAccountAliasesPaginateResponseTypeDef
):
    """
    Type definition for `ListAccountAliasesPaginate` `Response`

    Contains the response to a successful  ListAccountAliases request.

    - **AccountAliases** *(list) --*

      A list of aliases associated with the account. AWS supports only one alias per account.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedGroupPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttachedGroupPoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ListAttachedGroupPoliciesPaginateResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ListAttachedGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedGroupPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[
            ListAttachedGroupPoliciesPaginateResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedGroupPoliciesPaginateResponseTypeDef(
    _ListAttachedGroupPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListAttachedGroupPoliciesPaginate` `Response`

    Contains the response to a successful  ListAttachedGroupPolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAttachedRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedRolePoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedRolePoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttachedRolePoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ListAttachedRolePoliciesPaginateResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ListAttachedRolePoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedRolePoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[
            ListAttachedRolePoliciesPaginateResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedRolePoliciesPaginateResponseTypeDef(
    _ListAttachedRolePoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListAttachedRolePoliciesPaginate` `Response`

    Contains the response to a successful  ListAttachedRolePolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAttachedUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedUserPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedUserPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttachedUserPoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef",
    {"PolicyName": str, "PolicyArn": str},
    total=False,
)


class ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef(
    _ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef
):
    """
    Type definition for `ListAttachedUserPoliciesPaginateResponse` `AttachedPolicies`

    Contains information about an attached policy.

    An attached policy is a managed policy that has been attached to a user, group, or role.
    This data type is used as a response element in the  ListAttachedGroupPolicies ,
    ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
    operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name of the attached policy.

    - **PolicyArn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .
    """


_ListAttachedUserPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedUserPoliciesPaginateResponseTypeDef",
    {
        "AttachedPolicies": List[
            ListAttachedUserPoliciesPaginateResponseAttachedPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAttachedUserPoliciesPaginateResponseTypeDef(
    _ListAttachedUserPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListAttachedUserPoliciesPaginate` `Response`

    Contains the response to a successful  ListAttachedUserPolicies request.

    - **AttachedPolicies** *(list) --*

      A list of the attached policies.

      - *(dict) --*

        Contains information about an attached policy.

        An attached policy is a managed policy that has been attached to a user, group, or role.
        This data type is used as a response element in the  ListAttachedGroupPolicies ,
        ListAttachedRolePolicies ,  ListAttachedUserPolicies , and  GetAccountAuthorizationDetails
        operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name of the attached policy.

        - **PolicyArn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListEntitiesForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitiesForPolicyPaginatePaginationConfigTypeDef(
    _ListEntitiesForPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEntitiesForPolicyPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef",
    {"GroupName": str, "GroupId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef
):
    """
    Type definition for `ListEntitiesForPolicyPaginateResponse` `PolicyGroups`

    Contains information about a group that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **GroupName** *(string) --*

      The name (friendly name, not ARN) identifying the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef",
    {"RoleName": str, "RoleId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef
):
    """
    Type definition for `ListEntitiesForPolicyPaginateResponse` `PolicyRoles`

    Contains information about a role that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **RoleName** *(string) --*

      The name (friendly name, not ARN) identifying the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef",
    {"UserName": str, "UserId": str},
    total=False,
)


class ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef(
    _ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef
):
    """
    Type definition for `ListEntitiesForPolicyPaginateResponse` `PolicyUsers`

    Contains information about a user that a managed policy is attached to.

    This data type is used as a response element in the  ListEntitiesForPolicy operation.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **UserName** *(string) --*

      The name (friendly name, not ARN) identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
      *IAM User Guide* .
    """


_ListEntitiesForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListEntitiesForPolicyPaginateResponseTypeDef",
    {
        "PolicyGroups": List[ListEntitiesForPolicyPaginateResponsePolicyGroupsTypeDef],
        "PolicyUsers": List[ListEntitiesForPolicyPaginateResponsePolicyUsersTypeDef],
        "PolicyRoles": List[ListEntitiesForPolicyPaginateResponsePolicyRolesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListEntitiesForPolicyPaginateResponseTypeDef(
    _ListEntitiesForPolicyPaginateResponseTypeDef
):
    """
    Type definition for `ListEntitiesForPolicyPaginate` `Response`

    Contains the response to a successful  ListEntitiesForPolicy request.

    - **PolicyGroups** *(list) --*

      A list of IAM groups that the policy is attached to.

      - *(dict) --*

        Contains information about a group that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **GroupName** *(string) --*

          The name (friendly name, not ARN) identifying the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **PolicyUsers** *(list) --*

      A list of IAM users that the policy is attached to.

      - *(dict) --*

        Contains information about a user that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **UserName** *(string) --*

          The name (friendly name, not ARN) identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **PolicyRoles** *(list) --*

      A list of IAM roles that the policy is attached to.

      - *(dict) --*

        Contains information about a role that a managed policy is attached to.

        This data type is used as a response element in the  ListEntitiesForPolicy operation.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **RoleName** *(string) --*

          The name (friendly name, not ARN) identifying the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in the
          *IAM User Guide* .

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGroupPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupPoliciesPaginatePaginationConfigTypeDef(
    _ListGroupPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupPoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListGroupPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListGroupPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListGroupPoliciesPaginateResponseTypeDef(
    _ListGroupPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListGroupPoliciesPaginate` `Response`

    Contains the response to a successful  ListGroupPolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
      string of characters consisting of upper and lowercase alphanumeric characters with no
      spaces. You can also include any of the following characters: _+=,.@-

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGroupsForUserPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsForUserPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsForUserPaginatePaginationConfigTypeDef(
    _ListGroupsForUserPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupsForUserPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListGroupsForUserPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsForUserPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ListGroupsForUserPaginateResponseGroupsTypeDef(
    _ListGroupsForUserPaginateResponseGroupsTypeDef
):
    """
    Type definition for `ListGroupsForUserPaginateResponse` `Groups`

    Contains information about an IAM group entity.

    This data type is used as a response element in the following operations:

    *  CreateGroup

    *  GetGroup

    *  ListGroups

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.
    """


_ListGroupsForUserPaginateResponseTypeDef = TypedDict(
    "_ListGroupsForUserPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsForUserPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListGroupsForUserPaginateResponseTypeDef(
    _ListGroupsForUserPaginateResponseTypeDef
):
    """
    Type definition for `ListGroupsForUserPaginate` `Response`

    Contains the response to a successful  ListGroupsForUser request.

    - **Groups** *(list) --*

      A list of groups.

      - *(dict) --*

        Contains information about an IAM group entity.

        This data type is used as a response element in the following operations:

        *  CreateGroup

        *  GetGroup

        *  ListGroups

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(
    _ListGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGroupsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {"Path": str, "GroupName": str, "GroupId": str, "Arn": str, "CreateDate": datetime},
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `ListGroupsPaginateResponse` `Groups`

    Contains information about an IAM group entity.

    This data type is used as a response element in the following operations:

    *  CreateGroup

    *  GetGroup

    *  ListGroups

    - **Path** *(string) --*

      The path to the group. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **GroupName** *(string) --*

      The friendly name that identifies the group.

    - **GroupId** *(string) --*

      The stable and unique string identifying the group. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the group was created.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {
        "Groups": List[ListGroupsPaginateResponseGroupsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Response`

    Contains the response to a successful  ListGroups request.

    - **Groups** *(list) --*

      A list of groups.

      - *(dict) --*

        Contains information about an IAM group entity.

        This data type is used as a response element in the following operations:

        *  CreateGroup

        *  GetGroup

        *  ListGroups

        - **Path** *(string) --*

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **GroupName** *(string) --*

          The friendly name that identifies the group.

        - **GroupId** *(string) --*

          The stable and unique string identifying the group. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the group was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListInstanceProfilesForRolePaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstanceProfilesForRolePaginatePaginationConfigTypeDef(
    _ListInstanceProfilesForRolePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginateResponseInstanceProfilesRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for
    IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginateResponseInstanceProfilesRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only
    reported for the trailing 400 days. This period can be shorter if your Region began
    supporting these features within the last year. The role might have been used more
    than 400 days ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking period.
      For more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginateResponseInstanceProfilesRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
      and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string. However,
        you must interpret the value in your code.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTagsTypeDef
        ],
        "RoleLastUsed": ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginateResponseInstanceProfiles` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs,
      see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
      and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for
      IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
          and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string. However,
            you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only
      reported for the trailing 400 days. This period can be shorter if your Region began
      supporting these features within the last year. The role might have been used more
      than 400 days ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking period.
        For more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[
            ListInstanceProfilesForRolePaginateResponseInstanceProfilesRolesTypeDef
        ],
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef(
    _ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginateResponse` `InstanceProfiles`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs,
          see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
          and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for
          IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
              and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string. However,
                you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only
          reported for the trailing 400 days. This period can be shorter if your Region began
          supporting these features within the last year. The role might have been used more
          than 400 days ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking period.
            For more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesForRolePaginateResponseTypeDef = TypedDict(
    "_ListInstanceProfilesForRolePaginateResponseTypeDef",
    {
        "InstanceProfiles": List[
            ListInstanceProfilesForRolePaginateResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListInstanceProfilesForRolePaginateResponseTypeDef(
    _ListInstanceProfilesForRolePaginateResponseTypeDef
):
    """
    Type definition for `ListInstanceProfilesForRolePaginate` `Response`

    Contains the response to a successful  ListInstanceProfilesForRole request.

    - **InstanceProfiles** *(list) --*

      A list of instance profiles.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about IDs,
              see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
              and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses the
              AWS CLI, or API to assume the role can specify the duration using the optional
              ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries for
              IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information about
              tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with a
                resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
                Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value. For
                  example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
                  and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                  consist of the number associated with the different cost centers in your company.
                  Typically, many resources have tags with the same key name but with different
                  values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string. However,
                    you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes the
              date and time and the Region in which the role was last used. Activity is only
              reported for the trailing 400 days. This period can be shorter if your Region began
              supporting these features within the last year. The role might have been used more
              than 400 days ago. For more information, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking period.
                For more information about the tracking period, see `Regions Where Data Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListInstanceProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstanceProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstanceProfilesPaginatePaginationConfigTypeDef(
    _ListInstanceProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginateResponseInstanceProfilesRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for
    IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is
      used as the permissions boundary for an entity. This data type can only have a
      value of ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginateResponseInstanceProfilesRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only
    reported for the trailing 400 days. This period can be shorter if your Region began
    supporting these features within the last year. The role might have been used more
    than 400 days ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format
      <http://www.iso.org/iso/iso8601>`__ that the role was last used.

      This field is null if the role has not been used within the IAM tracking period.
      For more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginateResponseInstanceProfilesRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
      and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to
        store an array, you can store comma-separated values in the string. However,
        you must interpret the value in your code.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListInstanceProfilesPaginateResponseInstanceProfilesRolesPermissionsBoundaryTypeDef,
        "Tags": List[
            ListInstanceProfilesPaginateResponseInstanceProfilesRolesTagsTypeDef
        ],
        "RoleLastUsed": ListInstanceProfilesPaginateResponseInstanceProfilesRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginateResponseInstanceProfiles` `Roles`

    Contains information about an IAM role. This structure is returned as a response
    element in several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs,
      see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
      and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      , when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the
      AWS CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for
      IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is
        used as the permissions boundary for an entity. This data type can only have a
        value of ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
          and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to
            store an array, you can store comma-separated values in the string. However,
            you must interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only
      reported for the trailing 400 days. This period can be shorter if your Region began
      supporting these features within the last year. The role might have been used more
      than 400 days ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format
        <http://www.iso.org/iso/iso8601>`__ that the role was last used.

        This field is null if the role has not been used within the IAM tracking period.
        For more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[ListInstanceProfilesPaginateResponseInstanceProfilesRolesTypeDef],
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef(
    _ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginateResponse` `InstanceProfiles`

    Contains information about an instance profile.

    This data type is used as a response element in the following operations:

    *  CreateInstanceProfile

    *  GetInstanceProfile

    *  ListInstanceProfiles

    *  ListInstanceProfilesForRole

    - **Path** *(string) --*

      The path to the instance profile. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **InstanceProfileName** *(string) --*

      The name identifying the instance profile.

    - **InstanceProfileId** *(string) --*

      The stable and unique string identifying the instance profile. For more information about
      IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the instance profile. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date when the instance profile was created.

    - **Roles** *(list) --*

      The role associated with the instance profile.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response
        element in several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs,
          see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
          and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
          *IAM User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
          , when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the
          AWS CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for
          IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
          in the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is
            used as the permissions boundary for an entity. This data type can only have a
            value of ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see
            `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
              and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
              consist of the number associated with the different cost centers in your company.
              Typically, many resources have tags with the same key name but with different
              values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to
                store an array, you can store comma-separated values in the string. However,
                you must interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only
          reported for the trailing 400 days. This period can be shorter if your Region began
          supporting these features within the last year. The role might have been used more
          than 400 days ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format
            <http://www.iso.org/iso/iso8601>`__ that the role was last used.

            This field is null if the role has not been used within the IAM tracking period.
            For more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.
    """


_ListInstanceProfilesPaginateResponseTypeDef = TypedDict(
    "_ListInstanceProfilesPaginateResponseTypeDef",
    {
        "InstanceProfiles": List[
            ListInstanceProfilesPaginateResponseInstanceProfilesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListInstanceProfilesPaginateResponseTypeDef(
    _ListInstanceProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListInstanceProfilesPaginate` `Response`

    Contains the response to a successful  ListInstanceProfiles request.

    - **InstanceProfiles** *(list) --*

      A list of instance profiles.

      - *(dict) --*

        Contains information about an instance profile.

        This data type is used as a response element in the following operations:

        *  CreateInstanceProfile

        *  GetInstanceProfile

        *  ListInstanceProfiles

        *  ListInstanceProfilesForRole

        - **Path** *(string) --*

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **InstanceProfileName** *(string) --*

          The name identifying the instance profile.

        - **InstanceProfileId** *(string) --*

          The stable and unique string identifying the instance profile. For more information about
          IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the instance profile. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date when the instance profile was created.

        - **Roles** *(list) --*

          The role associated with the instance profile.

          - *(dict) --*

            Contains information about an IAM role. This structure is returned as a response
            element in several API operations that interact with roles.

            - **Path** *(string) --*

              The path to the role. For more information about paths, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **RoleName** *(string) --*

              The friendly name that identifies the role.

            - **RoleId** *(string) --*

              The stable and unique string identifying the role. For more information about IDs,
              see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* .

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) specifying the role. For more information about ARNs
              and how to use them in policies, see `IAM Identifiers
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
              *IAM User Guide* guide.

            - **CreateDate** *(datetime) --*

              The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
              , when the role was created.

            - **AssumeRolePolicyDocument** *(string) --*

              The policy that grants an entity permission to assume the role.

            - **Description** *(string) --*

              A description of the role that you provide.

            - **MaxSessionDuration** *(integer) --*

              The maximum session duration (in seconds) for the specified role. Anyone who uses the
              AWS CLI, or API to assume the role can specify the duration using the optional
              ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

            - **PermissionsBoundary** *(dict) --*

              The ARN of the policy used to set the permissions boundary for the role.

              For more information about permissions boundaries, see `Permissions Boundaries for
              IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
              in the *IAM User Guide* .

              - **PermissionsBoundaryType** *(string) --*

                The permissions boundary usage type that indicates what type of IAM resource is
                used as the permissions boundary for an entity. This data type can only have a
                value of ``Policy`` .

              - **PermissionsBoundaryArn** *(string) --*

                The ARN of the policy used to set the permissions boundary for the user or role.

            - **Tags** *(list) --*

              A list of tags that are attached to the specified role. For more information about
              tagging, see `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - *(dict) --*

                A structure that represents user-provided metadata that can be associated with a
                resource such as an IAM user or role. For more information about tagging, see
                `Tagging IAM Identities
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
                Guide* .

                - **Key** *(string) --*

                  The key name that can be used to look up or retrieve the associated value. For
                  example, ``Department`` or ``Cost Center`` are common choices.

                - **Value** *(string) --*

                  The value associated with this tag. For example, tags with a key name of
                  ``Department`` could have values such as ``Human Resources`` , ``Accounting`` ,
                  and ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                  consist of the number associated with the different cost centers in your company.
                  Typically, many resources have tags with the same key name but with different
                  values.

                  .. note::

                    AWS always interprets the tag ``Value`` as a single string. If you need to
                    store an array, you can store comma-separated values in the string. However,
                    you must interpret the value in your code.

            - **RoleLastUsed** *(dict) --*

              Contains information about the last time that an IAM role was used. This includes the
              date and time and the Region in which the role was last used. Activity is only
              reported for the trailing 400 days. This period can be shorter if your Region began
              supporting these features within the last year. The role might have been used more
              than 400 days ago. For more information, see `Regions Where Data Is Tracked
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
              in the *IAM User Guide* .

              - **LastUsedDate** *(datetime) --*

                The date and time, in `ISO 8601 date-time format
                <http://www.iso.org/iso/iso8601>`__ that the role was last used.

                This field is null if the role has not been used within the IAM tracking period.
                For more information about the tracking period, see `Regions Where Data Is Tracked
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
                in the *IAM User Guide* .

              - **Region** *(string) --*

                The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMFADevicesPaginatePaginationConfigTypeDef(
    _ListMFADevicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListMFADevicesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListMFADevicesPaginateResponseMFADevicesTypeDef = TypedDict(
    "_ListMFADevicesPaginateResponseMFADevicesTypeDef",
    {"UserName": str, "SerialNumber": str, "EnableDate": datetime},
    total=False,
)


class ListMFADevicesPaginateResponseMFADevicesTypeDef(
    _ListMFADevicesPaginateResponseMFADevicesTypeDef
):
    """
    Type definition for `ListMFADevicesPaginateResponse` `MFADevices`

    Contains information about an MFA device.

    This data type is used as a response element in the  ListMFADevices operation.

    - **UserName** *(string) --*

      The user with whom the MFA device is associated.

    - **SerialNumber** *(string) --*

      The serial number that uniquely identifies the MFA device. For virtual MFA devices, the
      serial number is the device ARN.

    - **EnableDate** *(datetime) --*

      The date when the MFA device was enabled for the user.
    """


_ListMFADevicesPaginateResponseTypeDef = TypedDict(
    "_ListMFADevicesPaginateResponseTypeDef",
    {
        "MFADevices": List[ListMFADevicesPaginateResponseMFADevicesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListMFADevicesPaginateResponseTypeDef(_ListMFADevicesPaginateResponseTypeDef):
    """
    Type definition for `ListMFADevicesPaginate` `Response`

    Contains the response to a successful  ListMFADevices request.

    - **MFADevices** *(list) --*

      A list of MFA devices.

      - *(dict) --*

        Contains information about an MFA device.

        This data type is used as a response element in the  ListMFADevices operation.

        - **UserName** *(string) --*

          The user with whom the MFA device is associated.

        - **SerialNumber** *(string) --*

          The serial number that uniquely identifies the MFA device. For virtual MFA devices, the
          serial number is the device ARN.

        - **EnableDate** *(datetime) --*

          The date when the MFA device was enabled for the user.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(
    _ListPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPoliciesPaginateResponsePoliciesTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsePoliciesTypeDef",
    {
        "PolicyName": str,
        "PolicyId": str,
        "Arn": str,
        "Path": str,
        "DefaultVersionId": str,
        "AttachmentCount": int,
        "PermissionsBoundaryUsageCount": int,
        "IsAttachable": bool,
        "Description": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
    },
    total=False,
)


class ListPoliciesPaginateResponsePoliciesTypeDef(
    _ListPoliciesPaginateResponsePoliciesTypeDef
):
    """
    Type definition for `ListPoliciesPaginateResponse` `Policies`

    Contains information about a managed policy.

    This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
    ListPolicies operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **PolicyName** *(string) --*

      The friendly name (not ARN) identifying the policy.

    - **PolicyId** *(string) --*

      The stable and unique string identifying the policy.

      For more information about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

      For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
      Namespaces
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
      *AWS General Reference* .

    - **Path** *(string) --*

      The path to the policy.

      For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **DefaultVersionId** *(string) --*

      The identifier for the version of the policy that is set as the default version.

    - **AttachmentCount** *(integer) --*

      The number of entities (users, groups, and roles) that the policy is attached to.

    - **PermissionsBoundaryUsageCount** *(integer) --*

      The number of entities (users and roles) for which the policy is used to set the
      permissions boundary.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

    - **IsAttachable** *(boolean) --*

      Specifies whether the policy can be attached to an IAM user, group, or role.

    - **Description** *(string) --*

      A friendly description of the policy.

      This element is included in the response to the  GetPolicy operation. It is not included
      in the response to the  ListPolicies operation.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was created.

    - **UpdateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy was last updated.

      When a policy has only one version, this field contains the date and time when the policy
      was created. When a policy has more than one version, this field contains the date and
      time when the most recent policy version was created.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {
        "Policies": List[ListPoliciesPaginateResponsePoliciesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListPoliciesPaginate` `Response`

    Contains the response to a successful  ListPolicies request.

    - **Policies** *(list) --*

      A list of policies.

      - *(dict) --*

        Contains information about a managed policy.

        This data type is used as a response element in the  CreatePolicy ,  GetPolicy , and
        ListPolicies operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **PolicyName** *(string) --*

          The friendly name (not ARN) identifying the policy.

        - **PolicyId** *(string) --*

          The stable and unique string identifying the policy.

          For more information about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.

          For more information about ARNs, go to `Amazon Resource Names (ARNs) and AWS Service
          Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .

        - **Path** *(string) --*

          The path to the policy.

          For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **DefaultVersionId** *(string) --*

          The identifier for the version of the policy that is set as the default version.

        - **AttachmentCount** *(integer) --*

          The number of entities (users, groups, and roles) that the policy is attached to.

        - **PermissionsBoundaryUsageCount** *(integer) --*

          The number of entities (users and roles) for which the policy is used to set the
          permissions boundary.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

        - **IsAttachable** *(boolean) --*

          Specifies whether the policy can be attached to an IAM user, group, or role.

        - **Description** *(string) --*

          A friendly description of the policy.

          This element is included in the response to the  GetPolicy operation. It is not included
          in the response to the  ListPolicies operation.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was created.

        - **UpdateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy was last updated.

          When a policy has only one version, this field contains the date and time when the policy
          was created. When a policy has more than one version, this field contains the date and
          time when the most recent policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPolicyVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyVersionsPaginatePaginationConfigTypeDef(
    _ListPolicyVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPolicyVersionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListPolicyVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListPolicyVersionsPaginateResponseVersionsTypeDef",
    {
        "Document": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "CreateDate": datetime,
    },
    total=False,
)


class ListPolicyVersionsPaginateResponseVersionsTypeDef(
    _ListPolicyVersionsPaginateResponseVersionsTypeDef
):
    """
    Type definition for `ListPolicyVersionsPaginateResponse` `Versions`

    Contains information about a version of a managed policy.

    This data type is used as a response element in the  CreatePolicyVersion ,
    GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

    For more information about managed policies, refer to `Managed Policies and Inline Policies
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
    the *IAM User Guide* .

    - **Document** *(string) --*

      The policy document.

      The policy document is returned in the response to the  GetPolicyVersion and
      GetAccountAuthorizationDetails operations. It is not returned in the response to the
      CreatePolicyVersion or  ListPolicyVersions operations.

      The policy document returned in this structure is URL-encoded compliant with `RFC 3986
      <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
      the policy back to plain JSON text. For example, if you use Java, you can use the
      ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
      languages and SDKs provide similar functionality.

    - **VersionId** *(string) --*

      The identifier for the policy version.

      Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
      created, the first policy version is ``v1`` .

    - **IsDefaultVersion** *(boolean) --*

      Specifies whether the policy version is set as the policy's default version.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the policy version was created.
    """


_ListPolicyVersionsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyVersionsPaginateResponseTypeDef",
    {
        "Versions": List[ListPolicyVersionsPaginateResponseVersionsTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListPolicyVersionsPaginateResponseTypeDef(
    _ListPolicyVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListPolicyVersionsPaginate` `Response`

    Contains the response to a successful  ListPolicyVersions request.

    - **Versions** *(list) --*

      A list of policy versions.

      For more information about managed policy versions, see `Versioning for Managed Policies
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
      *IAM User Guide* .

      - *(dict) --*

        Contains information about a version of a managed policy.

        This data type is used as a response element in the  CreatePolicyVersion ,
        GetPolicyVersion ,  ListPolicyVersions , and  GetAccountAuthorizationDetails operations.

        For more information about managed policies, refer to `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in
        the *IAM User Guide* .

        - **Document** *(string) --*

          The policy document.

          The policy document is returned in the response to the  GetPolicyVersion and
          GetAccountAuthorizationDetails operations. It is not returned in the response to the
          CreatePolicyVersion or  ListPolicyVersions operations.

          The policy document returned in this structure is URL-encoded compliant with `RFC 3986
          <https://tools.ietf.org/html/rfc3986>`__ . You can use a URL decoding method to convert
          the policy back to plain JSON text. For example, if you use Java, you can use the
          ``decode`` method of the ``java.net.URLDecoder`` utility class in the Java SDK. Other
          languages and SDKs provide similar functionality.

        - **VersionId** *(string) --*

          The identifier for the policy version.

          Policy version identifiers always begin with ``v`` (always lowercase). When a policy is
          created, the first policy version is ``v1`` .

        - **IsDefaultVersion** *(boolean) --*

          Specifies whether the policy version is set as the policy's default version.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the policy version was created.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRolePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRolePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRolePoliciesPaginatePaginationConfigTypeDef(
    _ListRolePoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRolePoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListRolePoliciesPaginateResponseTypeDef = TypedDict(
    "_ListRolePoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListRolePoliciesPaginateResponseTypeDef(_ListRolePoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListRolePoliciesPaginate` `Response`

    Contains the response to a successful  ListRolePolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRolesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRolesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRolesPaginatePaginationConfigTypeDef(
    _ListRolesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRolesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef(
    _ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef
):
    """
    Type definition for `ListRolesPaginateResponseRoles` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the role.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ListRolesPaginateResponseRolesRoleLastUsedTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesRoleLastUsedTypeDef",
    {"LastUsedDate": datetime, "Region": str},
    total=False,
)


class ListRolesPaginateResponseRolesRoleLastUsedTypeDef(
    _ListRolesPaginateResponseRolesRoleLastUsedTypeDef
):
    """
    Type definition for `ListRolesPaginateResponseRoles` `RoleLastUsed`

    Contains information about the last time that an IAM role was used. This includes the
    date and time and the Region in which the role was last used. Activity is only reported
    for the trailing 400 days. This period can be shorter if your Region began supporting
    these features within the last year. The role might have been used more than 400 days
    ago. For more information, see `Regions Where Data Is Tracked
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
    in the *IAM User Guide* .

    - **LastUsedDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
      that the role was last used.

      This field is null if the role has not been used within the IAM tracking period. For
      more information about the tracking period, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

    - **Region** *(string) --*

      The name of the AWS Region in which the role was last used.
    """


_ListRolesPaginateResponseRolesTagsTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListRolesPaginateResponseRolesTagsTypeDef(
    _ListRolesPaginateResponseRolesTagsTypeDef
):
    """
    Type definition for `ListRolesPaginateResponseRoles` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ListRolesPaginateResponseRolesTypeDef = TypedDict(
    "_ListRolesPaginateResponseRolesTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": str,
        "Description": str,
        "MaxSessionDuration": int,
        "PermissionsBoundary": ListRolesPaginateResponseRolesPermissionsBoundaryTypeDef,
        "Tags": List[ListRolesPaginateResponseRolesTagsTypeDef],
        "RoleLastUsed": ListRolesPaginateResponseRolesRoleLastUsedTypeDef,
    },
    total=False,
)


class ListRolesPaginateResponseRolesTypeDef(_ListRolesPaginateResponseRolesTypeDef):
    """
    Type definition for `ListRolesPaginateResponse` `Roles`

    Contains information about an IAM role. This structure is returned as a response element in
    several API operations that interact with roles.

    - **Path** *(string) --*

      The path to the role. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **RoleName** *(string) --*

      The friendly name that identifies the role.

    - **RoleId** *(string) --*

      The stable and unique string identifying the role. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
      how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* guide.

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the role was created.

    - **AssumeRolePolicyDocument** *(string) --*

      The policy that grants an entity permission to assume the role.

    - **Description** *(string) --*

      A description of the role that you provide.

    - **MaxSessionDuration** *(integer) --*

      The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
      CLI, or API to assume the role can specify the duration using the optional
      ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the role.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are attached to the specified role. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.

    - **RoleLastUsed** *(dict) --*

      Contains information about the last time that an IAM role was used. This includes the
      date and time and the Region in which the role was last used. Activity is only reported
      for the trailing 400 days. This period can be shorter if your Region began supporting
      these features within the last year. The role might have been used more than 400 days
      ago. For more information, see `Regions Where Data Is Tracked
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
      in the *IAM User Guide* .

      - **LastUsedDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
        that the role was last used.

        This field is null if the role has not been used within the IAM tracking period. For
        more information about the tracking period, see `Regions Where Data Is Tracked
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
        in the *IAM User Guide* .

      - **Region** *(string) --*

        The name of the AWS Region in which the role was last used.
    """


_ListRolesPaginateResponseTypeDef = TypedDict(
    "_ListRolesPaginateResponseTypeDef",
    {
        "Roles": List[ListRolesPaginateResponseRolesTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListRolesPaginateResponseTypeDef(_ListRolesPaginateResponseTypeDef):
    """
    Type definition for `ListRolesPaginate` `Response`

    Contains the response to a successful  ListRoles request.

    - **Roles** *(list) --*

      A list of roles.

      - *(dict) --*

        Contains information about an IAM role. This structure is returned as a response element in
        several API operations that interact with roles.

        - **Path** *(string) --*

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **RoleName** *(string) --*

          The friendly name that identifies the role.

        - **RoleId** *(string) --*

          The stable and unique string identifying the role. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and
          how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* guide.

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the role was created.

        - **AssumeRolePolicyDocument** *(string) --*

          The policy that grants an entity permission to assume the role.

        - **Description** *(string) --*

          A description of the role that you provide.

        - **MaxSessionDuration** *(integer) --*

          The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS
          CLI, or API to assume the role can specify the duration using the optional
          ``DurationSeconds`` API parameter or ``duration-seconds`` CLI parameter.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the role.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are attached to the specified role. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        - **RoleLastUsed** *(dict) --*

          Contains information about the last time that an IAM role was used. This includes the
          date and time and the Region in which the role was last used. Activity is only reported
          for the trailing 400 days. This period can be shorter if your Region began supporting
          these features within the last year. The role might have been used more than 400 days
          ago. For more information, see `Regions Where Data Is Tracked
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
          in the *IAM User Guide* .

          - **LastUsedDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__
            that the role was last used.

            This field is null if the role has not been used within the IAM tracking period. For
            more information about the tracking period, see `Regions Where Data Is Tracked
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period>`__
            in the *IAM User Guide* .

          - **Region** *(string) --*

            The name of the AWS Region in which the role was last used.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSSHPublicKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSSHPublicKeysPaginatePaginationConfigTypeDef(
    _ListSSHPublicKeysPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSSHPublicKeysPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef",
    {"UserName": str, "SSHPublicKeyId": str, "Status": str, "UploadDate": datetime},
    total=False,
)


class ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef(
    _ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef
):
    """
    Type definition for `ListSSHPublicKeysPaginateResponse` `SSHPublicKeys`

    Contains information about an SSH public key, without the key's body or fingerprint.

    This data type is used as a response element in the  ListSSHPublicKeys operation.

    - **UserName** *(string) --*

      The name of the IAM user associated with the SSH public key.

    - **SSHPublicKeyId** *(string) --*

      The unique identifier for the SSH public key.

    - **Status** *(string) --*

      The status of the SSH public key. ``Active`` means that the key can be used for
      authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot
      be used.

    - **UploadDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the SSH public key was uploaded.
    """


_ListSSHPublicKeysPaginateResponseTypeDef = TypedDict(
    "_ListSSHPublicKeysPaginateResponseTypeDef",
    {
        "SSHPublicKeys": List[ListSSHPublicKeysPaginateResponseSSHPublicKeysTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListSSHPublicKeysPaginateResponseTypeDef(
    _ListSSHPublicKeysPaginateResponseTypeDef
):
    """
    Type definition for `ListSSHPublicKeysPaginate` `Response`

    Contains the response to a successful  ListSSHPublicKeys request.

    - **SSHPublicKeys** *(list) --*

      A list of the SSH public keys assigned to IAM user.

      - *(dict) --*

        Contains information about an SSH public key, without the key's body or fingerprint.

        This data type is used as a response element in the  ListSSHPublicKeys operation.

        - **UserName** *(string) --*

          The name of the IAM user associated with the SSH public key.

        - **SSHPublicKeyId** *(string) --*

          The unique identifier for the SSH public key.

        - **Status** *(string) --*

          The status of the SSH public key. ``Active`` means that the key can be used for
          authentication with an AWS CodeCommit repository. ``Inactive`` means that the key cannot
          be used.

        - **UploadDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the SSH public key was uploaded.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListServerCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServerCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServerCertificatesPaginatePaginationConfigTypeDef(
    _ListServerCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServerCertificatesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef = TypedDict(
    "_ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
    },
    total=False,
)


class ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef(
    _ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef
):
    """
    Type definition for `ListServerCertificatesPaginateResponse` `ServerCertificateMetadataList`

    Contains information about a server certificate without its certificate body, certificate
    chain, and private key.

    This data type is used as a response element in the  UploadServerCertificate and
    ListServerCertificates operations.

    - **Path** *(string) --*

      The path to the server certificate. For more information about paths, see `IAM
      Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
      in the *IAM User Guide* .

    - **ServerCertificateName** *(string) --*

      The name that identifies the server certificate.

    - **ServerCertificateId** *(string) --*

      The stable and unique string identifying the server certificate. For more information
      about IDs, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) specifying the server certificate. For more information
      about ARNs and how to use them in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UploadDate** *(datetime) --*

      The date when the server certificate was uploaded.

    - **Expiration** *(datetime) --*

      The date on which the certificate is set to expire.
    """


_ListServerCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListServerCertificatesPaginateResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[
            ListServerCertificatesPaginateResponseServerCertificateMetadataListTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListServerCertificatesPaginateResponseTypeDef(
    _ListServerCertificatesPaginateResponseTypeDef
):
    """
    Type definition for `ListServerCertificatesPaginate` `Response`

    Contains the response to a successful  ListServerCertificates request.

    - **ServerCertificateMetadataList** *(list) --*

      A list of server certificates.

      - *(dict) --*

        Contains information about a server certificate without its certificate body, certificate
        chain, and private key.

        This data type is used as a response element in the  UploadServerCertificate and
        ListServerCertificates operations.

        - **Path** *(string) --*

          The path to the server certificate. For more information about paths, see `IAM
          Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
          in the *IAM User Guide* .

        - **ServerCertificateName** *(string) --*

          The name that identifies the server certificate.

        - **ServerCertificateId** *(string) --*

          The stable and unique string identifying the server certificate. For more information
          about IDs, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) specifying the server certificate. For more information
          about ARNs and how to use them in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UploadDate** *(datetime) --*

          The date when the server certificate was uploaded.

        - **Expiration** *(datetime) --*

          The date on which the certificate is set to expire.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSigningCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningCertificatesPaginatePaginationConfigTypeDef(
    _ListSigningCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSigningCertificatesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListSigningCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_ListSigningCertificatesPaginateResponseCertificatesTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": str,
        "UploadDate": datetime,
    },
    total=False,
)


class ListSigningCertificatesPaginateResponseCertificatesTypeDef(
    _ListSigningCertificatesPaginateResponseCertificatesTypeDef
):
    """
    Type definition for `ListSigningCertificatesPaginateResponse` `Certificates`

    Contains information about an X.509 signing certificate.

    This data type is used as a response element in the  UploadSigningCertificate and
    ListSigningCertificates operations.

    - **UserName** *(string) --*

      The name of the user the signing certificate is associated with.

    - **CertificateId** *(string) --*

      The ID for the signing certificate.

    - **CertificateBody** *(string) --*

      The contents of the signing certificate.

    - **Status** *(string) --*

      The status of the signing certificate. ``Active`` means that the key is valid for API
      calls, while ``Inactive`` means it is not.

    - **UploadDate** *(datetime) --*

      The date when the signing certificate was uploaded.
    """


_ListSigningCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListSigningCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[
            ListSigningCertificatesPaginateResponseCertificatesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListSigningCertificatesPaginateResponseTypeDef(
    _ListSigningCertificatesPaginateResponseTypeDef
):
    """
    Type definition for `ListSigningCertificatesPaginate` `Response`

    Contains the response to a successful  ListSigningCertificates request.

    - **Certificates** *(list) --*

      A list of the user's signing certificate information.

      - *(dict) --*

        Contains information about an X.509 signing certificate.

        This data type is used as a response element in the  UploadSigningCertificate and
        ListSigningCertificates operations.

        - **UserName** *(string) --*

          The name of the user the signing certificate is associated with.

        - **CertificateId** *(string) --*

          The ID for the signing certificate.

        - **CertificateBody** *(string) --*

          The contents of the signing certificate.

        - **Status** *(string) --*

          The status of the signing certificate. ``Active`` means that the key is valid for API
          calls, while ``Inactive`` means it is not.

        - **UploadDate** *(datetime) --*

          The date when the signing certificate was uploaded.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListUserPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoliciesPaginatePaginationConfigTypeDef(
    _ListUserPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUserPoliciesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListUserPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListUserPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListUserPoliciesPaginateResponseTypeDef(_ListUserPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListUserPoliciesPaginate` `Response`

    Contains the response to a successful  ListUserPolicies request.

    - **PolicyNames** *(list) --*

      A list of policy names.

      - *(string) --*

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(
    _ListUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsersPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef(
    _ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef
):
    """
    Type definition for `ListUsersPaginateResponseUsers` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
    the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used as
      the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ListUsersPaginateResponseUsersTagsTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListUsersPaginateResponseUsersTagsTypeDef(
    _ListUsersPaginateResponseUsersTagsTypeDef
):
    """
    Type definition for `ListUsersPaginateResponseUsers` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see `Tagging
    IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
    the *IAM User Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
      of the number associated with the different cost centers in your company. Typically,
      many resources have tags with the same key name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an
        array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ListUsersPaginateResponseUsersPermissionsBoundaryTypeDef,
        "Tags": List[ListUsersPaginateResponseUsersTagsTypeDef],
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    Type definition for `ListUsersPaginateResponse` `Users`

    Contains information about an IAM user entity.

    This data type is used as a response element in the following operations:

    *  CreateUser

    *  GetUser

    *  ListUsers

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
      and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
      User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information on
      October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the date
      and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
      the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used as
        the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see `Tagging
        IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
        the *IAM User Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
          of the number associated with the different cost centers in your company. Typically,
          many resources have tags with the same key name but with different values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store an
            array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {
        "Users": List[ListUsersPaginateResponseUsersTypeDef],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    Type definition for `ListUsersPaginate` `Response`

    Contains the response to a successful  ListUsers request.

    - **Users** *(list) --*

      A list of users.

      - *(dict) --*

        Contains information about an IAM user entity.

        This data type is used as a response element in the following operations:

        *  CreateUser

        *  GetUser

        *  ListUsers

        - **Path** *(string) --*

          The path to the user. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **UserName** *(string) --*

          The friendly name identifying the user.

        - **UserId** *(string) --*

          The stable and unique string identifying the user. For more information about IDs, see
          `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs
          and how to use ARNs in policies, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

        - **CreateDate** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user was created.

        - **PasswordLastUsed** *(datetime) --*

          The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
          when the user's password was last used to sign in to an AWS website. For a list of AWS
          websites that capture a user's last sign-in time, see the `Credential Reports
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
          the *IAM User Guide* . If a password is used more than once in a five-minute span, only
          the first use is returned in this field. If the field is null (no value), then it
          indicates that they never signed in with a password. This can be because:

          * The user never had a password.

          * A password exists but has not been used since IAM started tracking this information on
          October 20, 2014.

          A null value does not mean that the user *never* had a password. Also, if the user does
          not currently have a password but had one in the past, then this field contains the date
          and time the most recent password was used.

          This value is returned only in the  GetUser and  ListUsers operations.

        - **PermissionsBoundary** *(dict) --*

          The ARN of the policy used to set the permissions boundary for the user.

          For more information about permissions boundaries, see `Permissions Boundaries for IAM
          Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__ in
          the *IAM User Guide* .

          - **PermissionsBoundaryType** *(string) --*

            The permissions boundary usage type that indicates what type of IAM resource is used as
            the permissions boundary for an entity. This data type can only have a value of
            ``Policy`` .

          - **PermissionsBoundaryArn** *(string) --*

            The ARN of the policy used to set the permissions boundary for the user or role.

        - **Tags** *(list) --*

          A list of tags that are associated with the specified user. For more information about
          tagging, see `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in
            the *IAM User Guide* .

            - **Key** *(string) --*

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --*

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListVirtualMFADevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVirtualMFADevicesPaginatePaginationConfigTypeDef(
    _ListVirtualMFADevicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef",
    {"PermissionsBoundaryType": str, "PermissionsBoundaryArn": str},
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUser` `PermissionsBoundary`

    The ARN of the policy used to set the permissions boundary for the user.

    For more information about permissions boundaries, see `Permissions Boundaries for IAM
    Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
    in the *IAM User Guide* .

    - **PermissionsBoundaryType** *(string) --*

      The permissions boundary usage type that indicates what type of IAM resource is used
      as the permissions boundary for an entity. This data type can only have a value of
      ``Policy`` .

    - **PermissionsBoundaryArn** *(string) --*

      The ARN of the policy used to set the permissions boundary for the user or role.
    """


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a
    resource such as an IAM user or role. For more information about tagging, see
    `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
    Guide* .

    - **Key** *(string) --*

      The key name that can be used to look up or retrieve the associated value. For
      example, ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --*

      The value associated with this tag. For example, tags with a key name of
      ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
      ``Support`` . Tags with a key name of ``Cost Center`` might have values that
      consist of the number associated with the different cost centers in your company.
      Typically, many resources have tags with the same key name but with different
      values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store
        an array, you can store comma-separated values in the string. However, you must
        interpret the value in your code.
    """


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserPermissionsBoundaryTypeDef,
        "Tags": List[
            ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTagsTypeDef
        ],
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginateResponseVirtualMFADevices` `User`

    The IAM user associated with this virtual MFA device.

    - **Path** *(string) --*

      The path to the user. For more information about paths, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **UserName** *(string) --*

      The friendly name identifying the user.

    - **UserId** *(string) --*

      The stable and unique string identifying the user. For more information about IDs, see
      `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that identifies the user. For more information about
      ARNs and how to use ARNs in policies, see `IAM Identifiers
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
      *IAM User Guide* .

    - **CreateDate** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user was created.

    - **PasswordLastUsed** *(datetime) --*

      The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
      when the user's password was last used to sign in to an AWS website. For a list of AWS
      websites that capture a user's last sign-in time, see the `Credential Reports
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
      the *IAM User Guide* . If a password is used more than once in a five-minute span, only
      the first use is returned in this field. If the field is null (no value), then it
      indicates that they never signed in with a password. This can be because:

      * The user never had a password.

      * A password exists but has not been used since IAM started tracking this information
      on October 20, 2014.

      A null value does not mean that the user *never* had a password. Also, if the user does
      not currently have a password but had one in the past, then this field contains the
      date and time the most recent password was used.

      This value is returned only in the  GetUser and  ListUsers operations.

    - **PermissionsBoundary** *(dict) --*

      The ARN of the policy used to set the permissions boundary for the user.

      For more information about permissions boundaries, see `Permissions Boundaries for IAM
      Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
      in the *IAM User Guide* .

      - **PermissionsBoundaryType** *(string) --*

        The permissions boundary usage type that indicates what type of IAM resource is used
        as the permissions boundary for an entity. This data type can only have a value of
        ``Policy`` .

      - **PermissionsBoundaryArn** *(string) --*

        The ARN of the policy used to set the permissions boundary for the user or role.

    - **Tags** *(list) --*

      A list of tags that are associated with the specified user. For more information about
      tagging, see `Tagging IAM Identities
      <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
      Guide* .

      - *(dict) --*

        A structure that represents user-provided metadata that can be associated with a
        resource such as an IAM user or role. For more information about tagging, see
        `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - **Key** *(string) --*

          The key name that can be used to look up or retrieve the associated value. For
          example, ``Department`` or ``Cost Center`` are common choices.

        - **Value** *(string) --*

          The value associated with this tag. For example, tags with a key name of
          ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
          ``Support`` . Tags with a key name of ``Cost Center`` might have values that
          consist of the number associated with the different cost centers in your company.
          Typically, many resources have tags with the same key name but with different
          values.

          .. note::

            AWS always interprets the tag ``Value`` as a single string. If you need to store
            an array, you can store comma-separated values in the string. However, you must
            interpret the value in your code.
    """


_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": bytes,
        "QRCodePNG": bytes,
        "User": ListVirtualMFADevicesPaginateResponseVirtualMFADevicesUserTypeDef,
        "EnableDate": datetime,
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef(
    _ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginateResponse` `VirtualMFADevices`

    Contains information about a virtual MFA device.

    - **SerialNumber** *(string) --*

      The serial number associated with ``VirtualMFADevice`` .

    - **Base32StringSeed** *(bytes) --*

      The base32 seed defined as specified in `RFC3548
      <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

    - **QRCodePNG** *(bytes) --*

      A QR code PNG image that encodes
      ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
      ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the
      user name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed
      in base32 format. The ``Base32String`` value is base64-encoded.

    - **User** *(dict) --*

      The IAM user associated with this virtual MFA device.

      - **Path** *(string) --*

        The path to the user. For more information about paths, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **UserName** *(string) --*

        The friendly name identifying the user.

      - **UserId** *(string) --*

        The stable and unique string identifying the user. For more information about IDs, see
        `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the user. For more information about
        ARNs and how to use ARNs in policies, see `IAM Identifiers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
        *IAM User Guide* .

      - **CreateDate** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user was created.

      - **PasswordLastUsed** *(datetime) --*

        The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
        when the user's password was last used to sign in to an AWS website. For a list of AWS
        websites that capture a user's last sign-in time, see the `Credential Reports
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
        the *IAM User Guide* . If a password is used more than once in a five-minute span, only
        the first use is returned in this field. If the field is null (no value), then it
        indicates that they never signed in with a password. This can be because:

        * The user never had a password.

        * A password exists but has not been used since IAM started tracking this information
        on October 20, 2014.

        A null value does not mean that the user *never* had a password. Also, if the user does
        not currently have a password but had one in the past, then this field contains the
        date and time the most recent password was used.

        This value is returned only in the  GetUser and  ListUsers operations.

      - **PermissionsBoundary** *(dict) --*

        The ARN of the policy used to set the permissions boundary for the user.

        For more information about permissions boundaries, see `Permissions Boundaries for IAM
        Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
        in the *IAM User Guide* .

        - **PermissionsBoundaryType** *(string) --*

          The permissions boundary usage type that indicates what type of IAM resource is used
          as the permissions boundary for an entity. This data type can only have a value of
          ``Policy`` .

        - **PermissionsBoundaryArn** *(string) --*

          The ARN of the policy used to set the permissions boundary for the user or role.

      - **Tags** *(list) --*

        A list of tags that are associated with the specified user. For more information about
        tagging, see `Tagging IAM Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
        Guide* .

        - *(dict) --*

          A structure that represents user-provided metadata that can be associated with a
          resource such as an IAM user or role. For more information about tagging, see
          `Tagging IAM Identities
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
          Guide* .

          - **Key** *(string) --*

            The key name that can be used to look up or retrieve the associated value. For
            example, ``Department`` or ``Cost Center`` are common choices.

          - **Value** *(string) --*

            The value associated with this tag. For example, tags with a key name of
            ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
            ``Support`` . Tags with a key name of ``Cost Center`` might have values that
            consist of the number associated with the different cost centers in your company.
            Typically, many resources have tags with the same key name but with different
            values.

            .. note::

              AWS always interprets the tag ``Value`` as a single string. If you need to store
              an array, you can store comma-separated values in the string. However, you must
              interpret the value in your code.

    - **EnableDate** *(datetime) --*

      The date and time on which the virtual MFA device was enabled.
    """


_ListVirtualMFADevicesPaginateResponseTypeDef = TypedDict(
    "_ListVirtualMFADevicesPaginateResponseTypeDef",
    {
        "VirtualMFADevices": List[
            ListVirtualMFADevicesPaginateResponseVirtualMFADevicesTypeDef
        ],
        "IsTruncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListVirtualMFADevicesPaginateResponseTypeDef(
    _ListVirtualMFADevicesPaginateResponseTypeDef
):
    """
    Type definition for `ListVirtualMFADevicesPaginate` `Response`

    Contains the response to a successful  ListVirtualMFADevices request.

    - **VirtualMFADevices** *(list) --*

      The list of virtual MFA devices in the current account that match the ``AssignmentStatus``
      value that was passed in the request.

      - *(dict) --*

        Contains information about a virtual MFA device.

        - **SerialNumber** *(string) --*

          The serial number associated with ``VirtualMFADevice`` .

        - **Base32StringSeed** *(bytes) --*

          The base32 seed defined as specified in `RFC3548
          <https://tools.ietf.org/html/rfc3548.txt>`__ . The ``Base32StringSeed`` is base64-encoded.

        - **QRCodePNG** *(bytes) --*

          A QR code PNG image that encodes
          ``otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String`` where
          ``$virtualMFADeviceName`` is one of the create call arguments. ``AccountName`` is the
          user name if set (otherwise, the account ID otherwise), and ``Base32String`` is the seed
          in base32 format. The ``Base32String`` value is base64-encoded.

        - **User** *(dict) --*

          The IAM user associated with this virtual MFA device.

          - **Path** *(string) --*

            The path to the user. For more information about paths, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **UserName** *(string) --*

            The friendly name identifying the user.

          - **UserId** *(string) --*

            The stable and unique string identifying the user. For more information about IDs, see
            `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the user. For more information about
            ARNs and how to use ARNs in policies, see `IAM Identifiers
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the
            *IAM User Guide* .

          - **CreateDate** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the user was created.

          - **PasswordLastUsed** *(datetime) --*

            The date and time, in `ISO 8601 date-time format <http://www.iso.org/iso/iso8601>`__ ,
            when the user's password was last used to sign in to an AWS website. For a list of AWS
            websites that capture a user's last sign-in time, see the `Credential Reports
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html>`__ topic in
            the *IAM User Guide* . If a password is used more than once in a five-minute span, only
            the first use is returned in this field. If the field is null (no value), then it
            indicates that they never signed in with a password. This can be because:

            * The user never had a password.

            * A password exists but has not been used since IAM started tracking this information
            on October 20, 2014.

            A null value does not mean that the user *never* had a password. Also, if the user does
            not currently have a password but had one in the past, then this field contains the
            date and time the most recent password was used.

            This value is returned only in the  GetUser and  ListUsers operations.

          - **PermissionsBoundary** *(dict) --*

            The ARN of the policy used to set the permissions boundary for the user.

            For more information about permissions boundaries, see `Permissions Boundaries for IAM
            Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`__
            in the *IAM User Guide* .

            - **PermissionsBoundaryType** *(string) --*

              The permissions boundary usage type that indicates what type of IAM resource is used
              as the permissions boundary for an entity. This data type can only have a value of
              ``Policy`` .

            - **PermissionsBoundaryArn** *(string) --*

              The ARN of the policy used to set the permissions boundary for the user or role.

          - **Tags** *(list) --*

            A list of tags that are associated with the specified user. For more information about
            tagging, see `Tagging IAM Identities
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
            Guide* .

            - *(dict) --*

              A structure that represents user-provided metadata that can be associated with a
              resource such as an IAM user or role. For more information about tagging, see
              `Tagging IAM Identities
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User
              Guide* .

              - **Key** *(string) --*

                The key name that can be used to look up or retrieve the associated value. For
                example, ``Department`` or ``Cost Center`` are common choices.

              - **Value** *(string) --*

                The value associated with this tag. For example, tags with a key name of
                ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
                ``Support`` . Tags with a key name of ``Cost Center`` might have values that
                consist of the number associated with the different cost centers in your company.
                Typically, many resources have tags with the same key name but with different
                values.

                .. note::

                  AWS always interprets the tag ``Value`` as a single string. If you need to store
                  an array, you can store comma-separated values in the string. However, you must
                  interpret the value in your code.

        - **EnableDate** *(datetime) --*

          The date and time on which the virtual MFA device was enabled.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more items to return. If your results were truncated,
      you can make a subsequent pagination request using the ``Marker`` request parameter to
      retrieve more items. Note that IAM might return fewer than the ``MaxItems`` number of results
      even when there are more results available. We recommend that you check ``IsTruncated`` after
      every call to ensure that you receive all your results.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_PolicyExistsWaitWaiterConfigTypeDef = TypedDict(
    "_PolicyExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class PolicyExistsWaitWaiterConfigTypeDef(_PolicyExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `PolicyExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """


_RoleExistsWaitWaiterConfigTypeDef = TypedDict(
    "_RoleExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class RoleExistsWaitWaiterConfigTypeDef(_RoleExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `RoleExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """


_SamlProviderUpdateResponseTypeDef = TypedDict(
    "_SamlProviderUpdateResponseTypeDef", {"SAMLProviderArn": str}, total=False
)


class SamlProviderUpdateResponseTypeDef(_SamlProviderUpdateResponseTypeDef):
    """
    Type definition for `SamlProviderUpdate` `Response`

    Contains the response to a successful  UpdateSAMLProvider request.

    - **SAMLProviderArn** *(string) --*

      The Amazon Resource Name (ARN) of the SAML provider that was updated.
    """


_ServiceResourceCreateRoleTagsTypeDef = TypedDict(
    "_ServiceResourceCreateRoleTagsTypeDef", {"Key": str, "Value": str}
)


class ServiceResourceCreateRoleTagsTypeDef(_ServiceResourceCreateRoleTagsTypeDef):
    """
    Type definition for `ServiceResourceCreateRole` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_ServiceResourceCreateUserTagsTypeDef = TypedDict(
    "_ServiceResourceCreateUserTagsTypeDef", {"Key": str, "Value": str}
)


class ServiceResourceCreateUserTagsTypeDef(_ServiceResourceCreateUserTagsTypeDef):
    """
    Type definition for `ServiceResourceCreateUser` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_SimulateCustomPolicyPaginateContextEntriesTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginateContextEntriesTypeDef",
    {"ContextKeyName": str, "ContextKeyValues": List[str], "ContextKeyType": str},
    total=False,
)


class SimulateCustomPolicyPaginateContextEntriesTypeDef(
    _SimulateCustomPolicyPaginateContextEntriesTypeDef
):
    """
    Type definition for `SimulateCustomPolicyPaginate` `ContextEntries`

    Contains information about a condition context key. It includes the name of the key and
    specifies the value (or values, if the context key supports multiple values) to use in the
    simulation. This information is used when evaluating the ``Condition`` elements of the input
    policies.

    This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
    SimulatePrincipalPolicy `` .

    - **ContextKeyName** *(string) --*

      The full name of a condition context key, including the service prefix. For example,
      ``aws:SourceIp`` or ``s3:VersionId`` .

    - **ContextKeyValues** *(list) --*

      The value (or values, if the condition context key supports multiple values) to provide to
      the simulation when the key is referenced by a ``Condition`` element in an input policy.

      - *(string) --*

    - **ContextKeyType** *(string) --*

      The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
    """


_SimulateCustomPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_SimulateCustomPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SimulateCustomPolicyPaginatePaginationConfigTypeDef(
    _SimulateCustomPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SimulateCustomPolicyPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_SimulatePrincipalPolicyPaginateContextEntriesTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginateContextEntriesTypeDef",
    {"ContextKeyName": str, "ContextKeyValues": List[str], "ContextKeyType": str},
    total=False,
)


class SimulatePrincipalPolicyPaginateContextEntriesTypeDef(
    _SimulatePrincipalPolicyPaginateContextEntriesTypeDef
):
    """
    Type definition for `SimulatePrincipalPolicyPaginate` `ContextEntries`

    Contains information about a condition context key. It includes the name of the key and
    specifies the value (or values, if the context key supports multiple values) to use in the
    simulation. This information is used when evaluating the ``Condition`` elements of the input
    policies.

    This data type is used as an input parameter to ``  SimulateCustomPolicy `` and ``
    SimulatePrincipalPolicy `` .

    - **ContextKeyName** *(string) --*

      The full name of a condition context key, including the service prefix. For example,
      ``aws:SourceIp`` or ``s3:VersionId`` .

    - **ContextKeyValues** *(list) --*

      The value (or values, if the condition context key supports multiple values) to provide to
      the simulation when the key is referenced by a ``Condition`` element in an input policy.

      - *(string) --*

    - **ContextKeyType** *(string) --*

      The data type of the value (or values) specified in the ``ContextKeyValues`` parameter.
    """


_SimulatePrincipalPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_SimulatePrincipalPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SimulatePrincipalPolicyPaginatePaginationConfigTypeDef(
    _SimulatePrincipalPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SimulatePrincipalPolicyPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_UserCreateTagsTypeDef = TypedDict("_UserCreateTagsTypeDef", {"Key": str, "Value": str})


class UserCreateTagsTypeDef(_UserCreateTagsTypeDef):
    """
    Type definition for `UserCreate` `Tags`

    A structure that represents user-provided metadata that can be associated with a resource such
    as an IAM user or role. For more information about tagging, see `Tagging IAM Identities
    <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM User Guide* .

    - **Key** *(string) --* **[REQUIRED]**

      The key name that can be used to look up or retrieve the associated value. For example,
      ``Department`` or ``Cost Center`` are common choices.

    - **Value** *(string) --* **[REQUIRED]**

      The value associated with this tag. For example, tags with a key name of ``Department`` could
      have values such as ``Human Resources`` , ``Accounting`` , and ``Support`` . Tags with a key
      name of ``Cost Center`` might have values that consist of the number associated with the
      different cost centers in your company. Typically, many resources have tags with the same key
      name but with different values.

      .. note::

        AWS always interprets the tag ``Value`` as a single string. If you need to store an array,
        you can store comma-separated values in the string. However, you must interpret the value
        in your code.
    """


_UserExistsWaitWaiterConfigTypeDef = TypedDict(
    "_UserExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class UserExistsWaitWaiterConfigTypeDef(_UserExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `UserExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 20
    """
