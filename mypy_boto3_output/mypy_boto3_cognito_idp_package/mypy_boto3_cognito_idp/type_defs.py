"Main interface for cognito-idp type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "AdminListGroupsForUserPaginatePaginationConfigTypeDef",
    "AdminListGroupsForUserPaginateResponseGroupsTypeDef",
    "AdminListGroupsForUserPaginateResponseTypeDef",
    "AdminListUserAuthEventsPaginatePaginationConfigTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef",
    "AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef",
    "AdminListUserAuthEventsPaginateResponseTypeDef",
    "ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    "ClientAddCustomAttributesCustomAttributesTypeDef",
    "ClientAdminCreateUserResponseUserAttributesTypeDef",
    "ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    "ClientAdminCreateUserResponseUserTypeDef",
    "ClientAdminCreateUserResponseTypeDef",
    "ClientAdminCreateUserUserAttributesTypeDef",
    "ClientAdminCreateUserValidationDataTypeDef",
    "ClientAdminDisableProviderForUserUserTypeDef",
    "ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientAdminGetDeviceResponseDeviceTypeDef",
    "ClientAdminGetDeviceResponseTypeDef",
    "ClientAdminGetUserResponseMFAOptionsTypeDef",
    "ClientAdminGetUserResponseUserAttributesTypeDef",
    "ClientAdminGetUserResponseTypeDef",
    "ClientAdminInitiateAuthAnalyticsMetadataTypeDef",
    "ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    "ClientAdminInitiateAuthContextDataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientAdminInitiateAuthResponseTypeDef",
    "ClientAdminLinkProviderForUserDestinationUserTypeDef",
    "ClientAdminLinkProviderForUserSourceUserTypeDef",
    "ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientAdminListDevicesResponseDevicesTypeDef",
    "ClientAdminListDevicesResponseTypeDef",
    "ClientAdminListGroupsForUserResponseGroupsTypeDef",
    "ClientAdminListGroupsForUserResponseTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    "ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    "ClientAdminListUserAuthEventsResponseTypeDef",
    "ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    "ClientAdminRespondToAuthChallengeContextDataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientAdminRespondToAuthChallengeResponseTypeDef",
    "ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientAdminSetUserSettingsMFAOptionsTypeDef",
    "ClientAdminUpdateUserAttributesUserAttributesTypeDef",
    "ClientAssociateSoftwareTokenResponseTypeDef",
    "ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    "ClientConfirmDeviceResponseTypeDef",
    "ClientConfirmForgotPasswordAnalyticsMetadataTypeDef",
    "ClientConfirmForgotPasswordUserContextDataTypeDef",
    "ClientConfirmSignUpAnalyticsMetadataTypeDef",
    "ClientConfirmSignUpUserContextDataTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientCreateIdentityProviderResponseTypeDef",
    "ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    "ClientCreateResourceServerResponseResourceServerTypeDef",
    "ClientCreateResourceServerResponseTypeDef",
    "ClientCreateResourceServerScopesTypeDef",
    "ClientCreateUserImportJobResponseUserImportJobTypeDef",
    "ClientCreateUserImportJobResponseTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientCreateUserPoolClientResponseTypeDef",
    "ClientCreateUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientCreateUserPoolDomainResponseTypeDef",
    "ClientCreateUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientCreateUserPoolResponseUserPoolTypeDef",
    "ClientCreateUserPoolResponseTypeDef",
    "ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    "ClientCreateUserPoolSchemaTypeDef",
    "ClientCreateUserPoolSmsConfigurationTypeDef",
    "ClientCreateUserPoolUserPoolAddOnsTypeDef",
    "ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    "ClientDescribeIdentityProviderResponseTypeDef",
    "ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    "ClientDescribeResourceServerResponseResourceServerTypeDef",
    "ClientDescribeResourceServerResponseTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientDescribeRiskConfigurationResponseTypeDef",
    "ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    "ClientDescribeUserImportJobResponseTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    "ClientDescribeUserPoolClientResponseTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    "ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    "ClientDescribeUserPoolDomainResponseTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    "ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    "ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    "ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    "ClientDescribeUserPoolResponseUserPoolTypeDef",
    "ClientDescribeUserPoolResponseTypeDef",
    "ClientForgotPasswordAnalyticsMetadataTypeDef",
    "ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    "ClientForgotPasswordResponseTypeDef",
    "ClientForgotPasswordUserContextDataTypeDef",
    "ClientGetCsvHeaderResponseTypeDef",
    "ClientGetDeviceResponseDeviceDeviceAttributesTypeDef",
    "ClientGetDeviceResponseDeviceTypeDef",
    "ClientGetDeviceResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    "ClientGetIdentityProviderByIdentifierResponseTypeDef",
    "ClientGetSigningCertificateResponseTypeDef",
    "ClientGetUiCustomizationResponseUICustomizationTypeDef",
    "ClientGetUiCustomizationResponseTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientGetUserAttributeVerificationCodeResponseTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientGetUserPoolMfaConfigResponseTypeDef",
    "ClientGetUserResponseMFAOptionsTypeDef",
    "ClientGetUserResponseUserAttributesTypeDef",
    "ClientGetUserResponseTypeDef",
    "ClientInitiateAuthAnalyticsMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientInitiateAuthResponseAuthenticationResultTypeDef",
    "ClientInitiateAuthResponseTypeDef",
    "ClientInitiateAuthUserContextDataTypeDef",
    "ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListIdentityProvidersResponseProvidersTypeDef",
    "ClientListIdentityProvidersResponseTypeDef",
    "ClientListResourceServersResponseResourceServersScopesTypeDef",
    "ClientListResourceServersResponseResourceServersTypeDef",
    "ClientListResourceServersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUserImportJobsResponseUserImportJobsTypeDef",
    "ClientListUserImportJobsResponseTypeDef",
    "ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    "ClientListUserPoolClientsResponseTypeDef",
    "ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    "ClientListUserPoolsResponseUserPoolsTypeDef",
    "ClientListUserPoolsResponseTypeDef",
    "ClientListUsersInGroupResponseUsersAttributesTypeDef",
    "ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    "ClientListUsersInGroupResponseUsersTypeDef",
    "ClientListUsersInGroupResponseTypeDef",
    "ClientListUsersResponseUsersAttributesTypeDef",
    "ClientListUsersResponseUsersMFAOptionsTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    "ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    "ClientResendConfirmationCodeResponseTypeDef",
    "ClientResendConfirmationCodeUserContextDataTypeDef",
    "ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    "ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    "ClientRespondToAuthChallengeResponseTypeDef",
    "ClientRespondToAuthChallengeUserContextDataTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    "ClientSetRiskConfigurationResponseTypeDef",
    "ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    "ClientSetUiCustomizationResponseUICustomizationTypeDef",
    "ClientSetUiCustomizationResponseTypeDef",
    "ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    "ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigResponseTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    "ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef",
    "ClientSetUserSettingsMFAOptionsTypeDef",
    "ClientSignUpAnalyticsMetadataTypeDef",
    "ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    "ClientSignUpResponseTypeDef",
    "ClientSignUpUserAttributesTypeDef",
    "ClientSignUpUserContextDataTypeDef",
    "ClientSignUpValidationDataTypeDef",
    "ClientStartUserImportJobResponseUserImportJobTypeDef",
    "ClientStartUserImportJobResponseTypeDef",
    "ClientStopUserImportJobResponseUserImportJobTypeDef",
    "ClientStopUserImportJobResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    "ClientUpdateIdentityProviderResponseTypeDef",
    "ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    "ClientUpdateResourceServerResponseResourceServerTypeDef",
    "ClientUpdateResourceServerResponseTypeDef",
    "ClientUpdateResourceServerScopesTypeDef",
    "ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    "ClientUpdateUserAttributesResponseTypeDef",
    "ClientUpdateUserAttributesUserAttributesTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    "ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    "ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    "ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    "ClientUpdateUserPoolClientResponseTypeDef",
    "ClientUpdateUserPoolDeviceConfigurationTypeDef",
    "ClientUpdateUserPoolDomainCustomDomainConfigTypeDef",
    "ClientUpdateUserPoolDomainResponseTypeDef",
    "ClientUpdateUserPoolEmailConfigurationTypeDef",
    "ClientUpdateUserPoolLambdaConfigTypeDef",
    "ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    "ClientUpdateUserPoolPoliciesTypeDef",
    "ClientUpdateUserPoolSmsConfigurationTypeDef",
    "ClientUpdateUserPoolUserPoolAddOnsTypeDef",
    "ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    "ClientVerifySoftwareTokenResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListIdentityProvidersPaginatePaginationConfigTypeDef",
    "ListIdentityProvidersPaginateResponseProvidersTypeDef",
    "ListIdentityProvidersPaginateResponseTypeDef",
    "ListResourceServersPaginatePaginationConfigTypeDef",
    "ListResourceServersPaginateResponseResourceServersScopesTypeDef",
    "ListResourceServersPaginateResponseResourceServersTypeDef",
    "ListResourceServersPaginateResponseTypeDef",
    "ListUserPoolClientsPaginatePaginationConfigTypeDef",
    "ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef",
    "ListUserPoolClientsPaginateResponseTypeDef",
    "ListUserPoolsPaginatePaginationConfigTypeDef",
    "ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef",
    "ListUserPoolsPaginateResponseUserPoolsTypeDef",
    "ListUserPoolsPaginateResponseTypeDef",
    "ListUsersInGroupPaginatePaginationConfigTypeDef",
    "ListUsersInGroupPaginateResponseUsersAttributesTypeDef",
    "ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef",
    "ListUsersInGroupPaginateResponseUsersTypeDef",
    "ListUsersInGroupPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUsersAttributesTypeDef",
    "ListUsersPaginateResponseUsersMFAOptionsTypeDef",
    "ListUsersPaginateResponseUsersTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_AdminListGroupsForUserPaginatePaginationConfigTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class AdminListGroupsForUserPaginatePaginationConfigTypeDef(
    _AdminListGroupsForUserPaginatePaginationConfigTypeDef
):
    """
    Type definition for `AdminListGroupsForUserPaginate` `PaginationConfig`

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


_AdminListGroupsForUserPaginateResponseGroupsTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginateResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class AdminListGroupsForUserPaginateResponseGroupsTypeDef(
    _AdminListGroupsForUserPaginateResponseGroupsTypeDef
):
    """
    Type definition for `AdminListGroupsForUserPaginateResponse` `Groups`

    The group type.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
      each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
      claim is not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_AdminListGroupsForUserPaginateResponseTypeDef = TypedDict(
    "_AdminListGroupsForUserPaginateResponseTypeDef",
    {"Groups": List[AdminListGroupsForUserPaginateResponseGroupsTypeDef]},
    total=False,
)


class AdminListGroupsForUserPaginateResponseTypeDef(
    _AdminListGroupsForUserPaginateResponseTypeDef
):
    """
    Type definition for `AdminListGroupsForUserPaginate` `Response`

    - **Groups** *(list) --*

      The groups that the user belongs to.

      - *(dict) --*

        The group type.

        - **GroupName** *(string) --*

          The name of the group.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.

        - **Description** *(string) --*

          A string containing the description of the group.

        - **RoleArn** *(string) --*

          The role ARN for the group.

        - **Precedence** *(integer) --*

          A nonnegative integer value that specifies the precedence of this group relative to the
          other groups that a user can belong to in the user pool. If a user belongs to two or more
          groups, it is the group with the highest precedence whose role ARN will be used in the
          ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
          higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
          or with null ``Precedence`` values.

          Two groups can have the same ``Precedence`` value. If this happens, neither group takes
          precedence over the other. If two groups with the same ``Precedence`` have the same role
          ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
          each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
          claim is not set in users' tokens.

          The default ``Precedence`` value is null.

        - **LastModifiedDate** *(datetime) --*

          The date the group was last modified.

        - **CreationDate** *(datetime) --*

          The date the group was created.
    """


_AdminListUserAuthEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class AdminListUserAuthEventsPaginatePaginationConfigTypeDef(
    _AdminListUserAuthEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginate` `PaginationConfig`

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


_AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef",
    {"ChallengeName": str, "ChallengeResponse": str},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginateResponseAuthEvents` `ChallengeResponses`

    The challenge response type.

    - **ChallengeName** *(string) --*

      The challenge name

    - **ChallengeResponse** *(string) --*

      The challenge response.
    """


_AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginateResponseAuthEvents` `EventContextData`

    The user context data captured at the time of an event request. It provides additional
    information about the client from which event the request is received.

    - **IpAddress** *(string) --*

      The user's IP address.

    - **DeviceName** *(string) --*

      The user's device name.

    - **Timezone** *(string) --*

      The user's time zone.

    - **City** *(string) --*

      The user's city.

    - **Country** *(string) --*

      The user's country.
    """


_AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef",
    {"FeedbackValue": str, "Provider": str, "FeedbackDate": datetime},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginateResponseAuthEvents` `EventFeedback`

    A flag specifying the user feedback captured at the time of an event request is good or
    bad.

    - **FeedbackValue** *(string) --*

      The event feedback value.

    - **Provider** *(string) --*

      The provider.

    - **FeedbackDate** *(datetime) --*

      The event feedback date.
    """


_AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef",
    {"RiskDecision": str, "RiskLevel": str},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginateResponseAuthEvents` `EventRisk`

    The event risk.

    - **RiskDecision** *(string) --*

      The risk decision.

    - **RiskLevel** *(string) --*

      The risk level.
    """


_AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef",
    {
        "EventId": str,
        "EventType": str,
        "CreationDate": datetime,
        "EventResponse": str,
        "EventRisk": AdminListUserAuthEventsPaginateResponseAuthEventsEventRiskTypeDef,
        "ChallengeResponses": List[
            AdminListUserAuthEventsPaginateResponseAuthEventsChallengeResponsesTypeDef
        ],
        "EventContextData": AdminListUserAuthEventsPaginateResponseAuthEventsEventContextDataTypeDef,
        "EventFeedback": AdminListUserAuthEventsPaginateResponseAuthEventsEventFeedbackTypeDef,
    },
    total=False,
)


class AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef(
    _AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginateResponse` `AuthEvents`

    The authentication event type.

    - **EventId** *(string) --*

      The event ID.

    - **EventType** *(string) --*

      The event type.

    - **CreationDate** *(datetime) --*

      The creation date

    - **EventResponse** *(string) --*

      The event response.

    - **EventRisk** *(dict) --*

      The event risk.

      - **RiskDecision** *(string) --*

        The risk decision.

      - **RiskLevel** *(string) --*

        The risk level.

    - **ChallengeResponses** *(list) --*

      The challenge responses.

      - *(dict) --*

        The challenge response type.

        - **ChallengeName** *(string) --*

          The challenge name

        - **ChallengeResponse** *(string) --*

          The challenge response.

    - **EventContextData** *(dict) --*

      The user context data captured at the time of an event request. It provides additional
      information about the client from which event the request is received.

      - **IpAddress** *(string) --*

        The user's IP address.

      - **DeviceName** *(string) --*

        The user's device name.

      - **Timezone** *(string) --*

        The user's time zone.

      - **City** *(string) --*

        The user's city.

      - **Country** *(string) --*

        The user's country.

    - **EventFeedback** *(dict) --*

      A flag specifying the user feedback captured at the time of an event request is good or
      bad.

      - **FeedbackValue** *(string) --*

        The event feedback value.

      - **Provider** *(string) --*

        The provider.

      - **FeedbackDate** *(datetime) --*

        The event feedback date.
    """


_AdminListUserAuthEventsPaginateResponseTypeDef = TypedDict(
    "_AdminListUserAuthEventsPaginateResponseTypeDef",
    {"AuthEvents": List[AdminListUserAuthEventsPaginateResponseAuthEventsTypeDef]},
    total=False,
)


class AdminListUserAuthEventsPaginateResponseTypeDef(
    _AdminListUserAuthEventsPaginateResponseTypeDef
):
    """
    Type definition for `AdminListUserAuthEventsPaginate` `Response`

    - **AuthEvents** *(list) --*

      The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` ,
      ``EventRisk`` , and ``EventResponse`` .

      - *(dict) --*

        The authentication event type.

        - **EventId** *(string) --*

          The event ID.

        - **EventType** *(string) --*

          The event type.

        - **CreationDate** *(datetime) --*

          The creation date

        - **EventResponse** *(string) --*

          The event response.

        - **EventRisk** *(dict) --*

          The event risk.

          - **RiskDecision** *(string) --*

            The risk decision.

          - **RiskLevel** *(string) --*

            The risk level.

        - **ChallengeResponses** *(list) --*

          The challenge responses.

          - *(dict) --*

            The challenge response type.

            - **ChallengeName** *(string) --*

              The challenge name

            - **ChallengeResponse** *(string) --*

              The challenge response.

        - **EventContextData** *(dict) --*

          The user context data captured at the time of an event request. It provides additional
          information about the client from which event the request is received.

          - **IpAddress** *(string) --*

            The user's IP address.

          - **DeviceName** *(string) --*

            The user's device name.

          - **Timezone** *(string) --*

            The user's time zone.

          - **City** *(string) --*

            The user's city.

          - **Country** *(string) --*

            The user's country.

        - **EventFeedback** *(dict) --*

          A flag specifying the user feedback captured at the time of an event request is good or
          bad.

          - **FeedbackValue** *(string) --*

            The event feedback value.

          - **Provider** *(string) --*

            The provider.

          - **FeedbackDate** *(datetime) --*

            The event feedback date.
    """


_ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef(
    _ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientAddCustomAttributesCustomAttributes` `NumberAttributeConstraints`

    Specifies the constraints for an attribute of the number type.

    - **MinValue** *(string) --*

      The minimum value of an attribute that is of the number data type.

    - **MaxValue** *(string) --*

      The maximum value of an attribute that is of the number data type.
    """


_ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef(
    _ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientAddCustomAttributesCustomAttributes` `StringAttributeConstraints`

    Specifies the constraints for an attribute of the string type.

    - **MinLength** *(string) --*

      The minimum length.

    - **MaxLength** *(string) --*

      The maximum length.
    """


_ClientAddCustomAttributesCustomAttributesTypeDef = TypedDict(
    "_ClientAddCustomAttributesCustomAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": str,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientAddCustomAttributesCustomAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientAddCustomAttributesCustomAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientAddCustomAttributesCustomAttributesTypeDef(
    _ClientAddCustomAttributesCustomAttributesTypeDef
):
    """
    Type definition for `ClientAddCustomAttributes` `CustomAttributes`

    Contains information about the schema attribute.

    - **Name** *(string) --*

      A schema attribute of the name type.

    - **AttributeDataType** *(string) --*

      The attribute data type.

    - **DeveloperOnlyAttribute** *(boolean) --*

      Specifies whether the attribute type is developer only.

    - **Mutable** *(boolean) --*

      Specifies whether the value of the attribute can be changed.

      For any user pool attribute that's mapped to an identity provider attribute, you must set
      this parameter to ``true`` . Amazon Cognito updates mapped attributes when users sign in to
      your application through an identity provider. If an attribute is immutable, Amazon Cognito
      throws an error when it attempts to update the attribute. For more information, see
      `Specifying Identity Provider Attribute Mappings for Your User Pool
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
      .

    - **Required** *(boolean) --*

      Specifies whether a user pool attribute is required. If the attribute is required and the
      user does not provide a value, registration or sign-in will fail.

    - **NumberAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the number type.

      - **MinValue** *(string) --*

        The minimum value of an attribute that is of the number data type.

      - **MaxValue** *(string) --*

        The maximum value of an attribute that is of the number data type.

    - **StringAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the string type.

      - **MinLength** *(string) --*

        The minimum length.

      - **MaxLength** *(string) --*

        The maximum length.
    """


_ClientAdminCreateUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminCreateUserResponseUserAttributesTypeDef(
    _ClientAdminCreateUserResponseUserAttributesTypeDef
):
    """
    Type definition for `ClientAdminCreateUserResponseUser` `Attributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAdminCreateUserResponseUserMFAOptionsTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientAdminCreateUserResponseUserMFAOptionsTypeDef(
    _ClientAdminCreateUserResponseUserMFAOptionsTypeDef
):
    """
    Type definition for `ClientAdminCreateUserResponseUser` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA configurations.
     You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientAdminCreateUserResponseUserTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseUserTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientAdminCreateUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ClientAdminCreateUserResponseUserMFAOptionsTypeDef],
    },
    total=False,
)


class ClientAdminCreateUserResponseUserTypeDef(
    _ClientAdminCreateUserResponseUserTypeDef
):
    """
    Type definition for `ClientAdminCreateUserResponse` `User`

    The newly created user.

    - **Username** *(string) --*

      The user name of the user you wish to describe.

    - **Attributes** *(list) --*

      A container with information about the user type attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The creation date of the user.

    - **UserLastModifiedDate** *(datetime) --*

      The last modified date of the user.

    - **Enabled** *(boolean) --*

      Specifies whether the user is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her
      password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary
      password, but on first sign-in, the user must change his or her password to a new value
      before doing anything else.

    - **MFAOptions** *(list) --*

      The MFA options for the user.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA configurations.
         You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientAdminCreateUserResponseTypeDef = TypedDict(
    "_ClientAdminCreateUserResponseTypeDef",
    {"User": ClientAdminCreateUserResponseUserTypeDef},
    total=False,
)


class ClientAdminCreateUserResponseTypeDef(_ClientAdminCreateUserResponseTypeDef):
    """
    Type definition for `ClientAdminCreateUser` `Response`

    Represents the response from the server to the request to create the user.

    - **User** *(dict) --*

      The newly created user.

      - **Username** *(string) --*

        The user name of the user you wish to describe.

      - **Attributes** *(list) --*

        A container with information about the user type attributes.

        - *(dict) --*

          Specifies whether the attribute is standard or custom.

          - **Name** *(string) --*

            The name of the attribute.

          - **Value** *(string) --*

            The value of the attribute.

      - **UserCreateDate** *(datetime) --*

        The creation date of the user.

      - **UserLastModifiedDate** *(datetime) --*

        The last modified date of the user.

      - **Enabled** *(boolean) --*

        Specifies whether the user is enabled.

      - **UserStatus** *(string) --*

        The user status. Can be one of the following:

        * UNCONFIRMED - User has been created but not confirmed.

        * CONFIRMED - User has been confirmed.

        * ARCHIVED - User is no longer active.

        * COMPROMISED - User is disabled due to a potential security threat.

        * UNKNOWN - User status is not known.

        * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her
        password before he or she can sign in.

        * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary
        password, but on first sign-in, the user must change his or her password to a new value
        before doing anything else.

      - **MFAOptions** *(list) --*

        The MFA options for the user.

        - *(dict) --*

           *This data type is no longer supported.* You can use it only for SMS MFA configurations.
           You can't use it for TOTP software token MFA configurations.

          To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
          SetUserMFAPreference actions.

          To look up information about either type of MFA configuration, use the
          AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

          - **DeliveryMedium** *(string) --*

            The delivery medium to send the MFA code. You can use this parameter to set only the
            ``SMS`` delivery medium value.

          - **AttributeName** *(string) --*

            The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_RequiredClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserUserAttributesTypeDef(
    _RequiredClientAdminCreateUserUserAttributesTypeDef,
    _OptionalClientAdminCreateUserUserAttributesTypeDef,
):
    """
    Type definition for `ClientAdminCreateUser` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_RequiredClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_RequiredClientAdminCreateUserValidationDataTypeDef", {"Name": str}
)
_OptionalClientAdminCreateUserValidationDataTypeDef = TypedDict(
    "_OptionalClientAdminCreateUserValidationDataTypeDef", {"Value": str}, total=False
)


class ClientAdminCreateUserValidationDataTypeDef(
    _RequiredClientAdminCreateUserValidationDataTypeDef,
    _OptionalClientAdminCreateUserValidationDataTypeDef,
):
    """
    Type definition for `ClientAdminCreateUser` `ValidationData`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAdminDisableProviderForUserUserTypeDef = TypedDict(
    "_ClientAdminDisableProviderForUserUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminDisableProviderForUserUserTypeDef(
    _ClientAdminDisableProviderForUserUserTypeDef
):
    """
    Type definition for `ClientAdminDisableProviderForUser` `User`

    The user to be disabled.

    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.

    - **ProviderAttributeName** *(string) --*

      The name of the provider attribute to link to, for example, ``NameID`` .

    - **ProviderAttributeValue** *(string) --*

      The value of the provider attribute to link to, for example, ``xxxxx_account`` .
    """


_ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef(
    _ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef
):
    """
    Type definition for `ClientAdminGetDeviceResponseDevice` `DeviceAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAdminGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[
            ClientAdminGetDeviceResponseDeviceDeviceAttributesTypeDef
        ],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientAdminGetDeviceResponseDeviceTypeDef(
    _ClientAdminGetDeviceResponseDeviceTypeDef
):
    """
    Type definition for `ClientAdminGetDeviceResponse` `Device`

    The device.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceAttributes** *(list) --*

      The device attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **DeviceCreateDate** *(datetime) --*

      The creation date of the device.

    - **DeviceLastModifiedDate** *(datetime) --*

      The last modified date of the device.

    - **DeviceLastAuthenticatedDate** *(datetime) --*

      The date in which the device was last authenticated.
    """


_ClientAdminGetDeviceResponseTypeDef = TypedDict(
    "_ClientAdminGetDeviceResponseTypeDef",
    {"Device": ClientAdminGetDeviceResponseDeviceTypeDef},
    total=False,
)


class ClientAdminGetDeviceResponseTypeDef(_ClientAdminGetDeviceResponseTypeDef):
    """
    Type definition for `ClientAdminGetDevice` `Response`

    Gets the device response, as an administrator.

    - **Device** *(dict) --*

      The device.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceAttributes** *(list) --*

        The device attributes.

        - *(dict) --*

          Specifies whether the attribute is standard or custom.

          - **Name** *(string) --*

            The name of the attribute.

          - **Value** *(string) --*

            The value of the attribute.

      - **DeviceCreateDate** *(datetime) --*

        The creation date of the device.

      - **DeviceLastModifiedDate** *(datetime) --*

        The last modified date of the device.

      - **DeviceLastAuthenticatedDate** *(datetime) --*

        The date in which the device was last authenticated.
    """


_ClientAdminGetUserResponseMFAOptionsTypeDef = TypedDict(
    "_ClientAdminGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientAdminGetUserResponseMFAOptionsTypeDef(
    _ClientAdminGetUserResponseMFAOptionsTypeDef
):
    """
    Type definition for `ClientAdminGetUserResponse` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA configurations.
     You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientAdminGetUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientAdminGetUserResponseUserAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminGetUserResponseUserAttributesTypeDef(
    _ClientAdminGetUserResponseUserAttributesTypeDef
):
    """
    Type definition for `ClientAdminGetUserResponse` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAdminGetUserResponseTypeDef = TypedDict(
    "_ClientAdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientAdminGetUserResponseUserAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ClientAdminGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class ClientAdminGetUserResponseTypeDef(_ClientAdminGetUserResponseTypeDef):
    """
    Type definition for `ClientAdminGetUser` `Response`

    Represents the response from the server from the request to get the specified user as an
    administrator.

    - **Username** *(string) --*

      The user name of the user about whom you are receiving information.

    - **UserAttributes** *(list) --*

      An array of name-value pairs representing user attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The date the user was created.

    - **UserLastModifiedDate** *(datetime) --*

      The date the user was last modified.

    - **Enabled** *(boolean) --*

      Indicates that the status is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her
      password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary
      password, but on first sign-in, the user must change his or her password to a new value
      before doing anything else.

    - **MFAOptions** *(list) --*

       *This response parameter is no longer supported.* It provides information only about SMS MFA
       configurations. It doesn't provide information about TOTP software token MFA configurations.
       To look up information about either type of MFA configuration, use the
       AdminGetUserResponse$UserMFASettingList response instead.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA configurations.
         You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .

    - **PreferredMfaSetting** *(string) --*

      The user's preferred MFA setting.

    - **UserMFASettingList** *(list) --*

      The MFA options that are enabled for the user. The possible values in this list are
      ``SMS_MFA`` and ``SOFTWARE_TOKEN_MFA`` .

      - *(string) --*
    """


_ClientAdminInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "_ClientAdminInitiateAuthAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientAdminInitiateAuthAnalyticsMetadataTypeDef(
    _ClientAdminInitiateAuthAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientAdminInitiateAuth` `AnalyticsMetadata`

    The analytics metadata for collecting Amazon Pinpoint metrics for ``AdminInitiateAuth`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientAdminInitiateAuthContextDataHttpHeadersTypeDef = TypedDict(
    "_ClientAdminInitiateAuthContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)


class ClientAdminInitiateAuthContextDataHttpHeadersTypeDef(
    _ClientAdminInitiateAuthContextDataHttpHeadersTypeDef
):
    """
    Type definition for `ClientAdminInitiateAuthContextData` `HttpHeaders`

    The HTTP header.

    - **headerName** *(string) --*

      The header name

    - **headerValue** *(string) --*

      The header value.
    """


_RequiredClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_RequiredClientAdminInitiateAuthContextDataTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[ClientAdminInitiateAuthContextDataHttpHeadersTypeDef],
    },
)
_OptionalClientAdminInitiateAuthContextDataTypeDef = TypedDict(
    "_OptionalClientAdminInitiateAuthContextDataTypeDef",
    {"EncodedData": str},
    total=False,
)


class ClientAdminInitiateAuthContextDataTypeDef(
    _RequiredClientAdminInitiateAuthContextDataTypeDef,
    _OptionalClientAdminInitiateAuthContextDataTypeDef,
):
    """
    Type definition for `ClientAdminInitiateAuth` `ContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **IpAddress** *(string) --* **[REQUIRED]**

      Source IP address of your user.

    - **ServerName** *(string) --* **[REQUIRED]**

      Your server endpoint where this API is invoked.

    - **ServerPath** *(string) --* **[REQUIRED]**

      Your server path where this API is invoked.

    - **HttpHeaders** *(list) --* **[REQUIRED]**

      HttpHeaders received on your server in same order.

      - *(dict) --*

        The HTTP header.

        - **headerName** *(string) --*

          The header name

        - **headerValue** *(string) --*

          The header value.

    - **EncodedData** *(string) --*

      Encoded data containing device fingerprinting details, collected using the Amazon Cognito
      context data collection library.
    """


_ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    """
    Type definition for `ClientAdminInitiateAuthResponseAuthenticationResult` `NewDeviceMetadata`

    The new device metadata from an authentication result.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceGroupKey** *(string) --*

      The device group key.
    """


_ClientAdminInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientAdminInitiateAuthResponseAuthenticationResultTypeDef(
    _ClientAdminInitiateAuthResponseAuthenticationResultTypeDef
):
    """
    Type definition for `ClientAdminInitiateAuthResponse` `AuthenticationResult`

    The result of the authentication response. This is only returned if the caller does not need
    to pass another challenge. If the caller does need to pass another challenge before it gets
    tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

    - **AccessToken** *(string) --*

      The access token.

    - **ExpiresIn** *(integer) --*

      The expiration period of the authentication result in seconds.

    - **TokenType** *(string) --*

      The token type.

    - **RefreshToken** *(string) --*

      The refresh token.

    - **IdToken** *(string) --*

      The ID token.

    - **NewDeviceMetadata** *(dict) --*

      The new device metadata from an authentication result.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceGroupKey** *(string) --*

        The device group key.
    """


_ClientAdminInitiateAuthResponseTypeDef = TypedDict(
    "_ClientAdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": str,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientAdminInitiateAuthResponseTypeDef(_ClientAdminInitiateAuthResponseTypeDef):
    """
    Type definition for `ClientAdminInitiateAuth` `Response`

    Initiates the authentication response, as an administrator.

    - **ChallengeName** *(string) --*

      The name of the challenge which you are responding to with this call. This is returned to you
      in the ``AdminInitiateAuth`` response if you need to pass another challenge.

      * ``MFA_SETUP`` : If MFA is required, users who do not have at least one of the MFA methods
      set up are presented with an ``MFA_SETUP`` challenge. The user must set up at least one MFA
      type to continue to authenticate.

      * ``SELECT_MFA_TYPE`` : Selects the MFA type. Valid MFA options are ``SMS_MFA`` for text SMS
      MFA, and ``SOFTWARE_TOKEN_MFA`` for TOTP software token MFA.

      * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS.

      * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` ,
      ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations.

      * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that
      the user should pass another challenge before tokens are issued.

      * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous
      challenges were passed, this challenge is returned so that Amazon Cognito can start tracking
      this device.

      * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only.

      * ``ADMIN_NO_SRP_AUTH`` : This is returned if you need to authenticate with ``USERNAME`` and
      ``PASSWORD`` directly. An app client must be enabled to use this flow.

      * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after
      successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other
      required attributes.

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service. If
      ``AdminInitiateAuth`` or ``AdminRespondToAuthChallenge`` API call determines that the caller
      needs to go through another challenge, they return a session with other challenge parameters.
      This session should be passed as it is to the next ``AdminRespondToAuthChallenge`` API call.

    - **ChallengeParameters** *(dict) --*

      The challenge parameters. These are returned to you in the ``AdminInitiateAuth`` response if
      you need to pass another challenge. The responses in this parameter should be used to compute
      inputs to the next call (``AdminRespondToAuthChallenge`` ).

      All challenges require ``USERNAME`` and ``SECRET_HASH`` (if applicable).

      The value of the ``USER_ID_FOR_SRP`` attribute will be the user's actual username, not an
      alias (such as email address or phone number), even if you specified an alias in your call to
      ``AdminInitiateAuth`` . This is because, in the ``AdminRespondToAuthChallenge`` API
      ``ChallengeResponses`` , the ``USERNAME`` attribute cannot be an alias.

      - *(string) --*

        - *(string) --*

    - **AuthenticationResult** *(dict) --*

      The result of the authentication response. This is only returned if the caller does not need
      to pass another challenge. If the caller does need to pass another challenge before it gets
      tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

      - **AccessToken** *(string) --*

        The access token.

      - **ExpiresIn** *(integer) --*

        The expiration period of the authentication result in seconds.

      - **TokenType** *(string) --*

        The token type.

      - **RefreshToken** *(string) --*

        The refresh token.

      - **IdToken** *(string) --*

        The ID token.

      - **NewDeviceMetadata** *(dict) --*

        The new device metadata from an authentication result.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceGroupKey** *(string) --*

          The device group key.
    """


_ClientAdminLinkProviderForUserDestinationUserTypeDef = TypedDict(
    "_ClientAdminLinkProviderForUserDestinationUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminLinkProviderForUserDestinationUserTypeDef(
    _ClientAdminLinkProviderForUserDestinationUserTypeDef
):
    """
    Type definition for `ClientAdminLinkProviderForUser` `DestinationUser`

    The existing user in the user pool to be linked to the external identity provider user account.
    Can be a native (Username + Password) Cognito User Pools user or a federated user (for example, a
    SAML or Facebook user). If the user doesn't exist, an exception is thrown. This is the user that
    is returned when the new user (with the linked identity provider attribute) signs in.

    For a native username + password user, the ``ProviderAttributeValue`` for the ``DestinationUser``
    should be the username in the user pool. For a federated user, it should be the provider-specific
    ``user_id`` .

    The ``ProviderAttributeName`` of the ``DestinationUser`` is ignored.

    The ``ProviderName`` should be set to ``Cognito`` for users in Cognito user pools.

    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.

    - **ProviderAttributeName** *(string) --*

      The name of the provider attribute to link to, for example, ``NameID`` .

    - **ProviderAttributeValue** *(string) --*

      The value of the provider attribute to link to, for example, ``xxxxx_account`` .
    """


_ClientAdminLinkProviderForUserSourceUserTypeDef = TypedDict(
    "_ClientAdminLinkProviderForUserSourceUserTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)


class ClientAdminLinkProviderForUserSourceUserTypeDef(
    _ClientAdminLinkProviderForUserSourceUserTypeDef
):
    """
    Type definition for `ClientAdminLinkProviderForUser` `SourceUser`

    An external identity provider account for a user who does not currently exist yet in the user
    pool. This user must be a federated user (for example, a SAML or Facebook user), not another
    native user.

    If the ``SourceUser`` is a federated social identity provider user (Facebook, Google, or Login
    with Amazon), you must set the ``ProviderAttributeName`` to ``Cognito_Subject`` . For social
    identity providers, the ``ProviderName`` will be ``Facebook`` , ``Google`` , or
    ``LoginWithAmazon`` , and Cognito will automatically parse the Facebook, Google, and Login with
    Amazon tokens for ``id`` , ``sub`` , and ``user_id`` , respectively. The
    ``ProviderAttributeValue`` for the user must be the same value as the ``id`` , ``sub`` , or
    ``user_id`` value found in the social identity provider token.

    For SAML, the ``ProviderAttributeName`` can be any value that matches a claim in the SAML
    assertion. If you wish to link SAML users based on the subject of the SAML assertion, you should
    map the subject to a claim through the SAML identity provider and submit that claim name as the
    ``ProviderAttributeName`` . If you set ``ProviderAttributeName`` to ``Cognito_Subject`` , Cognito
    will automatically parse the default unique identifier found in the subject from the SAML token.

    - **ProviderName** *(string) --*

      The name of the provider, for example, Facebook, Google, or Login with Amazon.

    - **ProviderAttributeName** *(string) --*

      The name of the provider attribute to link to, for example, ``NameID`` .

    - **ProviderAttributeValue** *(string) --*

      The value of the provider attribute to link to, for example, ``xxxxx_account`` .
    """


_ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef(
    _ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef
):
    """
    Type definition for `ClientAdminListDevicesResponseDevices` `DeviceAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAdminListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[
            ClientAdminListDevicesResponseDevicesDeviceAttributesTypeDef
        ],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientAdminListDevicesResponseDevicesTypeDef(
    _ClientAdminListDevicesResponseDevicesTypeDef
):
    """
    Type definition for `ClientAdminListDevicesResponse` `Devices`

    The device type.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceAttributes** *(list) --*

      The device attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **DeviceCreateDate** *(datetime) --*

      The creation date of the device.

    - **DeviceLastModifiedDate** *(datetime) --*

      The last modified date of the device.

    - **DeviceLastAuthenticatedDate** *(datetime) --*

      The date in which the device was last authenticated.
    """


_ClientAdminListDevicesResponseTypeDef = TypedDict(
    "_ClientAdminListDevicesResponseTypeDef",
    {
        "Devices": List[ClientAdminListDevicesResponseDevicesTypeDef],
        "PaginationToken": str,
    },
    total=False,
)


class ClientAdminListDevicesResponseTypeDef(_ClientAdminListDevicesResponseTypeDef):
    """
    Type definition for `ClientAdminListDevices` `Response`

    Lists the device's response, as an administrator.

    - **Devices** *(list) --*

      The devices in the list of devices response.

      - *(dict) --*

        The device type.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceAttributes** *(list) --*

          The device attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **DeviceCreateDate** *(datetime) --*

          The creation date of the device.

        - **DeviceLastModifiedDate** *(datetime) --*

          The last modified date of the device.

        - **DeviceLastAuthenticatedDate** *(datetime) --*

          The date in which the device was last authenticated.

    - **PaginationToken** *(string) --*

      The pagination token.
    """


_ClientAdminListGroupsForUserResponseGroupsTypeDef = TypedDict(
    "_ClientAdminListGroupsForUserResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientAdminListGroupsForUserResponseGroupsTypeDef(
    _ClientAdminListGroupsForUserResponseGroupsTypeDef
):
    """
    Type definition for `ClientAdminListGroupsForUserResponse` `Groups`

    The group type.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
      each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
      claim is not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ClientAdminListGroupsForUserResponseTypeDef = TypedDict(
    "_ClientAdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List[ClientAdminListGroupsForUserResponseGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientAdminListGroupsForUserResponseTypeDef(
    _ClientAdminListGroupsForUserResponseTypeDef
):
    """
    Type definition for `ClientAdminListGroupsForUser` `Response`

    - **Groups** *(list) --*

      The groups that the user belongs to.

      - *(dict) --*

        The group type.

        - **GroupName** *(string) --*

          The name of the group.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.

        - **Description** *(string) --*

          A string containing the description of the group.

        - **RoleArn** *(string) --*

          The role ARN for the group.

        - **Precedence** *(integer) --*

          A nonnegative integer value that specifies the precedence of this group relative to the
          other groups that a user can belong to in the user pool. If a user belongs to two or more
          groups, it is the group with the highest precedence whose role ARN will be used in the
          ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
          higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
          or with null ``Precedence`` values.

          Two groups can have the same ``Precedence`` value. If this happens, neither group takes
          precedence over the other. If two groups with the same ``Precedence`` have the same role
          ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
          each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
          claim is not set in users' tokens.

          The default ``Precedence`` value is null.

        - **LastModifiedDate** *(datetime) --*

          The date the group was last modified.

        - **CreationDate** *(datetime) --*

          The date the group was created.

    - **NextToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef",
    {"ChallengeName": str, "ChallengeResponse": str},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEventsResponseAuthEvents` `ChallengeResponses`

    The challenge response type.

    - **ChallengeName** *(string) --*

      The challenge name

    - **ChallengeResponse** *(string) --*

      The challenge response.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEventsResponseAuthEvents` `EventContextData`

    The user context data captured at the time of an event request. It provides additional
    information about the client from which event the request is received.

    - **IpAddress** *(string) --*

      The user's IP address.

    - **DeviceName** *(string) --*

      The user's device name.

    - **Timezone** *(string) --*

      The user's time zone.

    - **City** *(string) --*

      The user's city.

    - **Country** *(string) --*

      The user's country.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef",
    {"FeedbackValue": str, "Provider": str, "FeedbackDate": datetime},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEventsResponseAuthEvents` `EventFeedback`

    A flag specifying the user feedback captured at the time of an event request is good or
    bad.

    - **FeedbackValue** *(string) --*

      The event feedback value.

    - **Provider** *(string) --*

      The provider.

    - **FeedbackDate** *(datetime) --*

      The event feedback date.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef",
    {"RiskDecision": str, "RiskLevel": str},
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEventsResponseAuthEvents` `EventRisk`

    The event risk.

    - **RiskDecision** *(string) --*

      The risk decision.

    - **RiskLevel** *(string) --*

      The risk level.
    """


_ClientAdminListUserAuthEventsResponseAuthEventsTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseAuthEventsTypeDef",
    {
        "EventId": str,
        "EventType": str,
        "CreationDate": datetime,
        "EventResponse": str,
        "EventRisk": ClientAdminListUserAuthEventsResponseAuthEventsEventRiskTypeDef,
        "ChallengeResponses": List[
            ClientAdminListUserAuthEventsResponseAuthEventsChallengeResponsesTypeDef
        ],
        "EventContextData": ClientAdminListUserAuthEventsResponseAuthEventsEventContextDataTypeDef,
        "EventFeedback": ClientAdminListUserAuthEventsResponseAuthEventsEventFeedbackTypeDef,
    },
    total=False,
)


class ClientAdminListUserAuthEventsResponseAuthEventsTypeDef(
    _ClientAdminListUserAuthEventsResponseAuthEventsTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEventsResponse` `AuthEvents`

    The authentication event type.

    - **EventId** *(string) --*

      The event ID.

    - **EventType** *(string) --*

      The event type.

    - **CreationDate** *(datetime) --*

      The creation date

    - **EventResponse** *(string) --*

      The event response.

    - **EventRisk** *(dict) --*

      The event risk.

      - **RiskDecision** *(string) --*

        The risk decision.

      - **RiskLevel** *(string) --*

        The risk level.

    - **ChallengeResponses** *(list) --*

      The challenge responses.

      - *(dict) --*

        The challenge response type.

        - **ChallengeName** *(string) --*

          The challenge name

        - **ChallengeResponse** *(string) --*

          The challenge response.

    - **EventContextData** *(dict) --*

      The user context data captured at the time of an event request. It provides additional
      information about the client from which event the request is received.

      - **IpAddress** *(string) --*

        The user's IP address.

      - **DeviceName** *(string) --*

        The user's device name.

      - **Timezone** *(string) --*

        The user's time zone.

      - **City** *(string) --*

        The user's city.

      - **Country** *(string) --*

        The user's country.

    - **EventFeedback** *(dict) --*

      A flag specifying the user feedback captured at the time of an event request is good or
      bad.

      - **FeedbackValue** *(string) --*

        The event feedback value.

      - **Provider** *(string) --*

        The provider.

      - **FeedbackDate** *(datetime) --*

        The event feedback date.
    """


_ClientAdminListUserAuthEventsResponseTypeDef = TypedDict(
    "_ClientAdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List[ClientAdminListUserAuthEventsResponseAuthEventsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientAdminListUserAuthEventsResponseTypeDef(
    _ClientAdminListUserAuthEventsResponseTypeDef
):
    """
    Type definition for `ClientAdminListUserAuthEvents` `Response`

    - **AuthEvents** *(list) --*

      The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` ,
      ``EventRisk`` , and ``EventResponse`` .

      - *(dict) --*

        The authentication event type.

        - **EventId** *(string) --*

          The event ID.

        - **EventType** *(string) --*

          The event type.

        - **CreationDate** *(datetime) --*

          The creation date

        - **EventResponse** *(string) --*

          The event response.

        - **EventRisk** *(dict) --*

          The event risk.

          - **RiskDecision** *(string) --*

            The risk decision.

          - **RiskLevel** *(string) --*

            The risk level.

        - **ChallengeResponses** *(list) --*

          The challenge responses.

          - *(dict) --*

            The challenge response type.

            - **ChallengeName** *(string) --*

              The challenge name

            - **ChallengeResponse** *(string) --*

              The challenge response.

        - **EventContextData** *(dict) --*

          The user context data captured at the time of an event request. It provides additional
          information about the client from which event the request is received.

          - **IpAddress** *(string) --*

            The user's IP address.

          - **DeviceName** *(string) --*

            The user's device name.

          - **Timezone** *(string) --*

            The user's time zone.

          - **City** *(string) --*

            The user's city.

          - **Country** *(string) --*

            The user's country.

        - **EventFeedback** *(dict) --*

          A flag specifying the user feedback captured at the time of an event request is good or
          bad.

          - **FeedbackValue** *(string) --*

            The event feedback value.

          - **Provider** *(string) --*

            The provider.

          - **FeedbackDate** *(datetime) --*

            The event feedback date.

    - **NextToken** *(string) --*

      A pagination token.
    """


_ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef(
    _ClientAdminRespondToAuthChallengeAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientAdminRespondToAuthChallenge` `AnalyticsMetadata`

    The analytics metadata for collecting Amazon Pinpoint metrics for ``AdminRespondToAuthChallenge``
    calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef",
    {"headerName": str, "headerValue": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef(
    _ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef
):
    """
    Type definition for `ClientAdminRespondToAuthChallengeContextData` `HttpHeaders`

    The HTTP header.

    - **headerName** *(string) --*

      The header name

    - **headerValue** *(string) --*

      The header value.
    """


_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_RequiredClientAdminRespondToAuthChallengeContextDataTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List[
            ClientAdminRespondToAuthChallengeContextDataHttpHeadersTypeDef
        ],
    },
)
_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef = TypedDict(
    "_OptionalClientAdminRespondToAuthChallengeContextDataTypeDef",
    {"EncodedData": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeContextDataTypeDef(
    _RequiredClientAdminRespondToAuthChallengeContextDataTypeDef,
    _OptionalClientAdminRespondToAuthChallengeContextDataTypeDef,
):
    """
    Type definition for `ClientAdminRespondToAuthChallenge` `ContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **IpAddress** *(string) --* **[REQUIRED]**

      Source IP address of your user.

    - **ServerName** *(string) --* **[REQUIRED]**

      Your server endpoint where this API is invoked.

    - **ServerPath** *(string) --* **[REQUIRED]**

      Your server path where this API is invoked.

    - **HttpHeaders** *(list) --* **[REQUIRED]**

      HttpHeaders received on your server in same order.

      - *(dict) --*

        The HTTP header.

        - **headerName** *(string) --*

          The header name

        - **headerValue** *(string) --*

          The header value.

    - **EncodedData** *(string) --*

      Encoded data containing device fingerprinting details, collected using the Amazon Cognito
      context data collection library.
    """


_ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    """
    Type definition for `ClientAdminRespondToAuthChallengeResponseAuthenticationResult` `NewDeviceMetadata`

    The new device metadata from an authentication result.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceGroupKey** *(string) --*

      The device group key.
    """


_ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientAdminRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef(
    _ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef
):
    """
    Type definition for `ClientAdminRespondToAuthChallengeResponse` `AuthenticationResult`

    The result returned by the server in response to the authentication request.

    - **AccessToken** *(string) --*

      The access token.

    - **ExpiresIn** *(integer) --*

      The expiration period of the authentication result in seconds.

    - **TokenType** *(string) --*

      The token type.

    - **RefreshToken** *(string) --*

      The refresh token.

    - **IdToken** *(string) --*

      The ID token.

    - **NewDeviceMetadata** *(dict) --*

      The new device metadata from an authentication result.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceGroupKey** *(string) --*

        The device group key.
    """


_ClientAdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "_ClientAdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": str,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientAdminRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientAdminRespondToAuthChallengeResponseTypeDef(
    _ClientAdminRespondToAuthChallengeResponseTypeDef
):
    """
    Type definition for `ClientAdminRespondToAuthChallenge` `Response`

    Responds to the authentication challenge, as an administrator.

    - **ChallengeName** *(string) --*

      The name of the challenge. For more information, see .

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service. If
      the or API call determines that the caller needs to go through another challenge, they return
      a session with other challenge parameters. This session should be passed as it is to the next
      ``RespondToAuthChallenge`` API call.

    - **ChallengeParameters** *(dict) --*

      The challenge parameters. For more information, see .

      - *(string) --*

        - *(string) --*

    - **AuthenticationResult** *(dict) --*

      The result returned by the server in response to the authentication request.

      - **AccessToken** *(string) --*

        The access token.

      - **ExpiresIn** *(integer) --*

        The expiration period of the authentication result in seconds.

      - **TokenType** *(string) --*

        The token type.

      - **RefreshToken** *(string) --*

        The refresh token.

      - **IdToken** *(string) --*

        The ID token.

      - **NewDeviceMetadata** *(dict) --*

        The new device metadata from an authentication result.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceGroupKey** *(string) --*

          The device group key.
    """


_ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "_ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef(
    _ClientAdminSetUserMfaPreferenceSMSMfaSettingsTypeDef
):
    """
    Type definition for `ClientAdminSetUserMfaPreference` `SMSMfaSettings`

    The SMS text message MFA settings.

    - **Enabled** *(boolean) --*

      Specifies whether SMS text message MFA is enabled.

    - **PreferredMfa** *(boolean) --*

      Specifies whether SMS is the preferred MFA method.
    """


_ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "_ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef(
    _ClientAdminSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef
):
    """
    Type definition for `ClientAdminSetUserMfaPreference` `SoftwareTokenMfaSettings`

    The time-based one-time password software token MFA settings.

    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.

    - **PreferredMfa** *(boolean) --*

      Specifies whether software token MFA is the preferred MFA method.
    """


_ClientAdminSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "_ClientAdminSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientAdminSetUserSettingsMFAOptionsTypeDef(
    _ClientAdminSetUserSettingsMFAOptionsTypeDef
):
    """
    Type definition for `ClientAdminSetUserSettings` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA configurations. You
     can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the ``SMS``
      delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef",
    {"Value": str},
    total=False,
)


class ClientAdminUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientAdminUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientAdminUpdateUserAttributesUserAttributesTypeDef,
):
    """
    Type definition for `ClientAdminUpdateUserAttributes` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientAssociateSoftwareTokenResponseTypeDef = TypedDict(
    "_ClientAssociateSoftwareTokenResponseTypeDef",
    {"SecretCode": str, "Session": str},
    total=False,
)


class ClientAssociateSoftwareTokenResponseTypeDef(
    _ClientAssociateSoftwareTokenResponseTypeDef
):
    """
    Type definition for `ClientAssociateSoftwareToken` `Response`

    - **SecretCode** *(string) --*

      A unique generated shared secret code that is used in the TOTP algorithm to generate a one
      time code.

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service. This
      allows authentication of the user as part of the MFA setup process.
    """


_ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef = TypedDict(
    "_ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef",
    {"PasswordVerifier": str, "Salt": str},
    total=False,
)


class ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef(
    _ClientConfirmDeviceDeviceSecretVerifierConfigTypeDef
):
    """
    Type definition for `ClientConfirmDevice` `DeviceSecretVerifierConfig`

    The configuration of the device secret verifier.

    - **PasswordVerifier** *(string) --*

      The password verifier.

    - **Salt** *(string) --*

      The salt.
    """


_ClientConfirmDeviceResponseTypeDef = TypedDict(
    "_ClientConfirmDeviceResponseTypeDef",
    {"UserConfirmationNecessary": bool},
    total=False,
)


class ClientConfirmDeviceResponseTypeDef(_ClientConfirmDeviceResponseTypeDef):
    """
    Type definition for `ClientConfirmDevice` `Response`

    Confirms the device response.

    - **UserConfirmationNecessary** *(boolean) --*

      Indicates whether the user confirmation is necessary to confirm the device response.
    """


_ClientConfirmForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "_ClientConfirmForgotPasswordAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientConfirmForgotPasswordAnalyticsMetadataTypeDef(
    _ClientConfirmForgotPasswordAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientConfirmForgotPassword` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmForgotPassword`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientConfirmForgotPasswordUserContextDataTypeDef = TypedDict(
    "_ClientConfirmForgotPasswordUserContextDataTypeDef",
    {"EncodedData": str},
    total=False,
)


class ClientConfirmForgotPasswordUserContextDataTypeDef(
    _ClientConfirmForgotPasswordUserContextDataTypeDef
):
    """
    Type definition for `ClientConfirmForgotPassword` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientConfirmSignUpAnalyticsMetadataTypeDef = TypedDict(
    "_ClientConfirmSignUpAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientConfirmSignUpAnalyticsMetadataTypeDef(
    _ClientConfirmSignUpAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientConfirmSignUp` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``ConfirmSignUp`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientConfirmSignUpUserContextDataTypeDef = TypedDict(
    "_ClientConfirmSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientConfirmSignUpUserContextDataTypeDef(
    _ClientConfirmSignUpUserContextDataTypeDef
):
    """
    Type definition for `ClientConfirmSignUp` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientCreateGroupResponse` `Group`

    The group object for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
      group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
      not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    Type definition for `ClientCreateGroup` `Response`

    - **Group** *(dict) --*

      The group object for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.

      - **Description** *(string) --*

        A string containing the description of the group.

      - **RoleArn** *(string) --*

        The role ARN for the group.

      - **Precedence** *(integer) --*

        A nonnegative integer value that specifies the precedence of this group relative to the
        other groups that a user can belong to in the user pool. If a user belongs to two or more
        groups, it is the group with the highest precedence whose role ARN will be used in the
        ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
        higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
        or with null ``Precedence`` values.

        Two groups can have the same ``Precedence`` value. If this happens, neither group takes
        precedence over the other. If two groups with the same ``Precedence`` have the same role
        ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
        group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
        not set in users' tokens.

        The default ``Precedence`` value is null.

      - **LastModifiedDate** *(datetime) --*

        The date the group was last modified.

      - **CreationDate** *(datetime) --*

        The date the group was created.
    """


_ClientCreateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientCreateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": str,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientCreateIdentityProviderResponseIdentityProviderTypeDef(
    _ClientCreateIdentityProviderResponseIdentityProviderTypeDef
):
    """
    Type definition for `ClientCreateIdentityProviderResponse` `IdentityProvider`

    The newly created identity provider object.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **ProviderDetails** *(dict) --*

      The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

      - *(string) --*

        - *(string) --*

    - **AttributeMapping** *(dict) --*

      A mapping of identity provider attributes to standard and custom user pool attributes.

      - *(string) --*

        - *(string) --*

    - **IdpIdentifiers** *(list) --*

      A list of identity provider identifiers.

      - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The date the identity provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the identity provider was created.
    """


_ClientCreateIdentityProviderResponseTypeDef = TypedDict(
    "_ClientCreateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientCreateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientCreateIdentityProviderResponseTypeDef(
    _ClientCreateIdentityProviderResponseTypeDef
):
    """
    Type definition for `ClientCreateIdentityProvider` `Response`

    - **IdentityProvider** *(dict) --*

      The newly created identity provider object.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ProviderName** *(string) --*

        The identity provider name.

      - **ProviderType** *(string) --*

        The identity provider type.

      - **ProviderDetails** *(dict) --*

        The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

        - *(string) --*

          - *(string) --*

      - **AttributeMapping** *(dict) --*

        A mapping of identity provider attributes to standard and custom user pool attributes.

        - *(string) --*

          - *(string) --*

      - **IdpIdentifiers** *(list) --*

        A list of identity provider identifiers.

        - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The date the identity provider was last modified.

      - **CreationDate** *(datetime) --*

        The date the identity provider was created.
    """


_ClientCreateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientCreateResourceServerResponseResourceServerScopesTypeDef(
    _ClientCreateResourceServerResponseResourceServerScopesTypeDef
):
    """
    Type definition for `ClientCreateResourceServerResponseResourceServer` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --*

      The name of the scope.

    - **ScopeDescription** *(string) --*

      A description of the scope.
    """


_ClientCreateResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientCreateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientCreateResourceServerResponseResourceServerTypeDef(
    _ClientCreateResourceServerResponseResourceServerTypeDef
):
    """
    Type definition for `ClientCreateResourceServerResponse` `ResourceServer`

    The newly created resource server.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that hosts the resource server.

    - **Identifier** *(string) --*

      The identifier for the resource server.

    - **Name** *(string) --*

      The name of the resource server.

    - **Scopes** *(list) --*

      A list of scopes that are defined for the resource server.

      - *(dict) --*

        A resource server scope.

        - **ScopeName** *(string) --*

          The name of the scope.

        - **ScopeDescription** *(string) --*

          A description of the scope.
    """


_ClientCreateResourceServerResponseTypeDef = TypedDict(
    "_ClientCreateResourceServerResponseTypeDef",
    {"ResourceServer": ClientCreateResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientCreateResourceServerResponseTypeDef(
    _ClientCreateResourceServerResponseTypeDef
):
    """
    Type definition for `ClientCreateResourceServer` `Response`

    - **ResourceServer** *(dict) --*

      The newly created resource server.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.

      - **Identifier** *(string) --*

        The identifier for the resource server.

      - **Name** *(string) --*

        The name of the resource server.

      - **Scopes** *(list) --*

        A list of scopes that are defined for the resource server.

        - *(dict) --*

          A resource server scope.

          - **ScopeName** *(string) --*

            The name of the scope.

          - **ScopeDescription** *(string) --*

            A description of the scope.
    """


_ClientCreateResourceServerScopesTypeDef = TypedDict(
    "_ClientCreateResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
)


class ClientCreateResourceServerScopesTypeDef(_ClientCreateResourceServerScopesTypeDef):
    """
    Type definition for `ClientCreateResourceServer` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --* **[REQUIRED]**

      The name of the scope.

    - **ScopeDescription** *(string) --* **[REQUIRED]**

      A description of the scope.
    """


_ClientCreateUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientCreateUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientCreateUserImportJobResponseUserImportJobTypeDef(
    _ClientCreateUserImportJobResponseUserImportJobTypeDef
):
    """
    Type definition for `ClientCreateUserImportJobResponse` `UserImportJob`

    The job object that represents the user import job.

    - **JobName** *(string) --*

      The job name for the user import job.

    - **JobId** *(string) --*

      The job ID for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are being imported into.

    - **PreSignedUrl** *(string) --*

      The pre-signed URL to be used to upload the ``.csv`` file.

    - **CreationDate** *(datetime) --*

      The date the user import job was created.

    - **StartDate** *(datetime) --*

      The date when the user import job was started.

    - **CompletionDate** *(datetime) --*

      The date when the user import job was completed.

    - **Status** *(string) --*

      The status of the user import job. One of the following:

      * ``Created`` - The job was created but not started.

      * ``Pending`` - A transition state. You have started the job, but it has not begun
      importing users yet.

      * ``InProgress`` - The job has started, and users are being imported.

      * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

      * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

      * ``Succeeded`` - The job has completed successfully.

      * ``Failed`` - The job has stopped due to an error.

      * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
      associated with the job was deleted, and the job cannot be started.

    - **CloudWatchLogsRoleArn** *(string) --*

      The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
      information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
      Guide.

    - **ImportedUsers** *(integer) --*

      The number of users that were successfully imported.

    - **SkippedUsers** *(integer) --*

      The number of users that were skipped.

    - **FailedUsers** *(integer) --*

      The number of users that could not be imported.

    - **CompletionMessage** *(string) --*

      The message returned when the user import job is completed.
    """


_ClientCreateUserImportJobResponseTypeDef = TypedDict(
    "_ClientCreateUserImportJobResponseTypeDef",
    {"UserImportJob": ClientCreateUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientCreateUserImportJobResponseTypeDef(
    _ClientCreateUserImportJobResponseTypeDef
):
    """
    Type definition for `ClientCreateUserImportJob` `Response`

    Represents the response from the server to the request to create the user import job.

    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.

      - **JobName** *(string) --*

        The job name for the user import job.

      - **JobId** *(string) --*

        The job ID for the user import job.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that the users are being imported into.

      - **PreSignedUrl** *(string) --*

        The pre-signed URL to be used to upload the ``.csv`` file.

      - **CreationDate** *(datetime) --*

        The date the user import job was created.

      - **StartDate** *(datetime) --*

        The date when the user import job was started.

      - **CompletionDate** *(datetime) --*

        The date when the user import job was completed.

      - **Status** *(string) --*

        The status of the user import job. One of the following:

        * ``Created`` - The job was created but not started.

        * ``Pending`` - A transition state. You have started the job, but it has not begun
        importing users yet.

        * ``InProgress`` - The job has started, and users are being imported.

        * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

        * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

        * ``Succeeded`` - The job has completed successfully.

        * ``Failed`` - The job has stopped due to an error.

        * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
        associated with the job was deleted, and the job cannot be started.

      - **CloudWatchLogsRoleArn** *(string) --*

        The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
        information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
        Guide.

      - **ImportedUsers** *(integer) --*

        The number of users that were successfully imported.

      - **SkippedUsers** *(integer) --*

        The number of users that were skipped.

      - **FailedUsers** *(integer) --*

        The number of users that could not be imported.

      - **CompletionMessage** *(string) --*

        The message returned when the user import job is completed.
    """


_ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    """
    Type definition for `ClientCreateUserPoolAdminCreateUserConfig` `InviteMessageTemplate`

    The message template to be used for the welcome message to new users.

    See also `Customizing User Invitation Messages
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
    .

    - **SMSMessage** *(string) --*

      The message template for SMS messages.

    - **EmailMessage** *(string) --*

      The message template for email messages.

    - **EmailSubject** *(string) --*

      The subject line for email messages.
    """


_ClientCreateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolAdminCreateUserConfigTypeDef(
    _ClientCreateUserPoolAdminCreateUserConfigTypeDef
):
    """
    Type definition for `ClientCreateUserPool` `AdminCreateUserConfig`

    The configuration for ``AdminCreateUser`` requests.

    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False``
      if users can sign themselves up via an app.

    - **UnusedAccountValidityDays** *(integer) --*

      The user account expiration limit, in days, after which the account is no longer usable. To
      reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying
      ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

      .. note::

        If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that value
        will be used and ``UnusedAccountValidityDays`` will be deprecated for that user pool.

    - **InviteMessageTemplate** *(dict) --*

      The message template to be used for the welcome message to new users.

      See also `Customizing User Invitation Messages
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
      .

      - **SMSMessage** *(string) --*

        The message template for SMS messages.

      - **EmailMessage** *(string) --*

        The message template for email messages.

      - **EmailSubject** *(string) --*

        The subject line for email messages.
    """


_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str},
)
_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef",
    {"UserDataShared": bool},
    total=False,
)


class ClientCreateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientCreateUserPoolClientAnalyticsConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateUserPoolClient` `AnalyticsConfiguration`

    The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.

    - **ApplicationId** *(string) --* **[REQUIRED]**

      The application ID for an Amazon Pinpoint application.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint
      analytics.

    - **ExternalId** *(string) --* **[REQUIRED]**

      The external ID.

    - **UserDataShared** *(boolean) --*

      If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it
      publishes to Amazon Pinpoint analytics.
    """


_ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPoolClientResponseUserPoolClient` `AnalyticsConfiguration`

    The Amazon Pinpoint analytics configuration for the user pool client.

    - **ApplicationId** *(string) --*

      The application ID for an Amazon Pinpoint application.

    - **RoleArn** *(string) --*

      The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
      Pinpoint analytics.

    - **ExternalId** *(string) --*

      The external ID.

    - **UserDataShared** *(boolean) --*

      If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
      it publishes to Amazon Pinpoint analytics.
    """


_ClientCreateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[str],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[str],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientCreateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": str,
    },
    total=False,
)


class ClientCreateUserPoolClientResponseUserPoolClientTypeDef(
    _ClientCreateUserPoolClientResponseUserPoolClientTypeDef
):
    """
    Type definition for `ClientCreateUserPoolClientResponse` `UserPoolClient`

    The user pool client that was just created.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool client.

    - **ClientName** *(string) --*

      The client name from the user pool request of the client type.

    - **ClientId** *(string) --*

      The ID of the client associated with the user pool.

    - **ClientSecret** *(string) --*

      The client secret from the user pool request of the client type.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool client was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool client was created.

    - **RefreshTokenValidity** *(integer) --*

      The time limit, in days, after which the refresh token is no longer valid and cannot be
      used.

    - **ReadAttributes** *(list) --*

      The Read-only attributes.

      - *(string) --*

    - **WriteAttributes** *(list) --*

      The writeable attributes.

      - *(string) --*

    - **ExplicitAuthFlows** *(list) --*

      The authentication flows that are supported by the user pool clients. Flow names without
      the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
      that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
      prefix.

      Valid values include:

      * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
      ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
      With this authentication flow, Cognito receives the password in the request instead of
      using the SRP (Secure Remote Password protocol) protocol to verify passwords.

      * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

      * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
      Cognito receives the password in the request instead of using the SRP protocol to verify
      passwords.

      * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

      * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

      - *(string) --*

    - **SupportedIdentityProviders** *(list) --*

      A list of provider names for the identity providers that are supported on this client.

      - *(string) --*

    - **CallbackURLs** *(list) --*

      A list of allowed redirect (callback) URLs for the identity providers.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

      - *(string) --*

    - **LogoutURLs** *(list) --*

      A list of allowed logout URLs for the identity providers.

      - *(string) --*

    - **DefaultRedirectURI** *(string) --*

      The default redirect URI. Must be in the ``CallbackURLs`` list.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

    - **AllowedOAuthFlows** *(list) --*

      Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
      response. This code can be exchanged for access tokens with the token endpoint.

      Set to ``token`` to specify that the client should get the access token (and, optionally,
      ID token, based on scopes) directly.

      - *(string) --*

    - **AllowedOAuthScopes** *(list) --*

      A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
      ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
      created in Resource Servers are also supported.

      - *(string) --*

    - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

      Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
      Cognito user pools.

    - **AnalyticsConfiguration** *(dict) --*

      The Amazon Pinpoint analytics configuration for the user pool client.

      - **ApplicationId** *(string) --*

        The application ID for an Amazon Pinpoint application.

      - **RoleArn** *(string) --*

        The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
        Pinpoint analytics.

      - **ExternalId** *(string) --*

        The external ID.

      - **UserDataShared** *(boolean) --*

        If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
        it publishes to Amazon Pinpoint analytics.

    - **PreventUserExistenceErrors** *(string) --*

      Use this setting to choose which errors and responses are returned by Cognito APIs during
      authentication, account confirmation, and password recovery when the user does not exist in
      the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
      an error indicating either the username or password was incorrect, and account confirmation
      and password recovery return a response indicating a code was sent to a simulated
      destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
      exception if the user does not exist in the user pool.

      Valid values include:

      * ``ENABLED`` - This prevents user existence-related errors.

      * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
      errors are not prevented.

      This setting affects the behavior of following APIs:

      *  AdminInitiateAuth

      *  AdminRespondToAuthChallenge

      *  InitiateAuth

      *  RespondToAuthChallenge

      *  ForgotPassword

      *  ConfirmForgotPassword

      *  ConfirmSignUp

      *  ResendConfirmationCode

      .. note::

        After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
        ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientCreateUserPoolClientResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientCreateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientCreateUserPoolClientResponseTypeDef(
    _ClientCreateUserPoolClientResponseTypeDef
):
    """
    Type definition for `ClientCreateUserPoolClient` `Response`

    Represents the response from the server to create a user pool client.

    - **UserPoolClient** *(dict) --*

      The user pool client that was just created.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.

      - **ClientName** *(string) --*

        The client name from the user pool request of the client type.

      - **ClientId** *(string) --*

        The ID of the client associated with the user pool.

      - **ClientSecret** *(string) --*

        The client secret from the user pool request of the client type.

      - **LastModifiedDate** *(datetime) --*

        The date the user pool client was last modified.

      - **CreationDate** *(datetime) --*

        The date the user pool client was created.

      - **RefreshTokenValidity** *(integer) --*

        The time limit, in days, after which the refresh token is no longer valid and cannot be
        used.

      - **ReadAttributes** *(list) --*

        The Read-only attributes.

        - *(string) --*

      - **WriteAttributes** *(list) --*

        The writeable attributes.

        - *(string) --*

      - **ExplicitAuthFlows** *(list) --*

        The authentication flows that are supported by the user pool clients. Flow names without
        the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
        that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
        prefix.

        Valid values include:

        * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
        ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
        With this authentication flow, Cognito receives the password in the request instead of
        using the SRP (Secure Remote Password protocol) protocol to verify passwords.

        * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

        * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
        Cognito receives the password in the request instead of using the SRP protocol to verify
        passwords.

        * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

        * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

        - *(string) --*

      - **SupportedIdentityProviders** *(list) --*

        A list of provider names for the identity providers that are supported on this client.

        - *(string) --*

      - **CallbackURLs** *(list) --*

        A list of allowed redirect (callback) URLs for the identity providers.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

        - *(string) --*

      - **LogoutURLs** *(list) --*

        A list of allowed logout URLs for the identity providers.

        - *(string) --*

      - **DefaultRedirectURI** *(string) --*

        The default redirect URI. Must be in the ``CallbackURLs`` list.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

      - **AllowedOAuthFlows** *(list) --*

        Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
        response. This code can be exchanged for access tokens with the token endpoint.

        Set to ``token`` to specify that the client should get the access token (and, optionally,
        ID token, based on scopes) directly.

        - *(string) --*

      - **AllowedOAuthScopes** *(list) --*

        A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
        ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
        created in Resource Servers are also supported.

        - *(string) --*

      - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

        Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
        Cognito user pools.

      - **AnalyticsConfiguration** *(dict) --*

        The Amazon Pinpoint analytics configuration for the user pool client.

        - **ApplicationId** *(string) --*

          The application ID for an Amazon Pinpoint application.

        - **RoleArn** *(string) --*

          The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
          Pinpoint analytics.

        - **ExternalId** *(string) --*

          The external ID.

        - **UserDataShared** *(boolean) --*

          If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
          it publishes to Amazon Pinpoint analytics.

      - **PreventUserExistenceErrors** *(string) --*

        Use this setting to choose which errors and responses are returned by Cognito APIs during
        authentication, account confirmation, and password recovery when the user does not exist in
        the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
        an error indicating either the username or password was incorrect, and account confirmation
        and password recovery return a response indicating a code was sent to a simulated
        destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
        exception if the user does not exist in the user pool.

        Valid values include:

        * ``ENABLED`` - This prevents user existence-related errors.

        * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
        errors are not prevented.

        This setting affects the behavior of following APIs:

        *  AdminInitiateAuth

        *  AdminRespondToAuthChallenge

        *  InitiateAuth

        *  RespondToAuthChallenge

        *  ForgotPassword

        *  ConfirmForgotPassword

        *  ConfirmSignUp

        *  ResendConfirmationCode

        .. note::

          After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
          ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientCreateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientCreateUserPoolDeviceConfigurationTypeDef(
    _ClientCreateUserPoolDeviceConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPool` `DeviceConfiguration`

    The device configuration.

    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new device.

    - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

      If true, a device is only remembered on user prompt.
    """


_ClientCreateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)


class ClientCreateUserPoolDomainCustomDomainConfigTypeDef(
    _ClientCreateUserPoolDomainCustomDomainConfigTypeDef
):
    """
    Type definition for `ClientCreateUserPoolDomain` `CustomDomainConfig`

    The configuration for a custom domain that hosts the sign-up and sign-in webpages for your
    application.

    Provide this parameter only if you want to use a custom domain for your user pool. Otherwise, you
    can exclude this parameter and use the Amazon Cognito hosted domain instead.

    For more information about the hosted domain and custom domains, see `Configuring a User Pool
    Domain
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html>`__
    .

    - **CertificateArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this
      certificate for the subdomain of your custom domain.
    """


_ClientCreateUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)


class ClientCreateUserPoolDomainResponseTypeDef(
    _ClientCreateUserPoolDomainResponseTypeDef
):
    """
    Type definition for `ClientCreateUserPoolDomain` `Response`

    - **CloudFrontDomain** *(string) --*

      The Amazon CloudFront endpoint that you use as the target of the alias that you set up with
      your Domain Name Service (DNS) provider.
    """


_ClientCreateUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": str,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientCreateUserPoolEmailConfigurationTypeDef(
    _ClientCreateUserPoolEmailConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPool` `EmailConfiguration`

    The email configuration.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is
      used in one of the following ways, depending on the value that you specify for the
      ``EmailSendingAccount`` parameter:

      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom FROM
      address when it emails your users by using its built-in email account.

      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by calling
      Amazon SES on your behalf.

    - **ReplyToEmailAddress** *(string) --*

      The destination to which the receiver of the email should reply to.

    - **EmailSendingAccount** *(string) --*

      Specifies whether Amazon Cognito emails your users by using its built-in email functionality or
      your Amazon SES email configuration. Specify one of the following values:

        COGNITO_DEFAULT

      When Amazon Cognito emails your users, it uses its built-in email functionality. When you use
      the default option, Amazon Cognito allows only a limited number of emails each day for your
      user pool. For typical production environments, the default email limit is below the required
      delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES
      email configuration.

      To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
      Cognito Developer Guide* .

      The default FROM address is no-reply@verificationemail.com. To customize the FROM address,
      provide the ARN of an Amazon SES verified email address for the ``SourceArn`` parameter.

        DEVELOPER

      When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito
      calls Amazon SES on your behalf to send email from your verified email address. When you use
      this option, the email delivery limits are the same limits that apply to your Amazon SES
      verified email address in your AWS account.

      If you use this option, you must provide the ARN of an Amazon SES verified email address for
      the ``SourceArn`` parameter.

      Before Amazon Cognito can email your users, it requires additional permissions to call Amazon
      SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a
      *service-linked role* , which is a type of IAM role, in your AWS account. This role contains
      the permissions that allow Amazon Cognito to access Amazon SES and send email messages with
      your address. For more information about the service-linked role that Amazon Cognito creates,
      see `Using Service-Linked Roles for Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
      in the *Amazon Cognito Developer Guide* .

    - **From** *(string) --*

      Identifies either the sender’s email address or the sender’s name with their email address. For
      example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` . This address will
      appear before the body of the email.

    - **ConfigurationSet** *(string) --*

      The set of configuration rules that can be applied to emails sent using Amazon SES. A
      configuration set is applied to an email by including a reference to the configuration set in
      the headers of the email. Once applied, all of the rules in that configuration set are applied
      to the email. Configuration sets can be used to apply the following types of rules to emails:

      * Event publishing – Amazon SES can track the number of send, delivery, open, click, bounce,
      and complaint events for each email sent. Use event publishing to send information about these
      events to other AWS services such as SNS and CloudWatch.

      * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can create
      groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP
      pools with configuration sets.
    """


_ClientCreateUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientCreateUserPoolLambdaConfigTypeDef(_ClientCreateUserPoolLambdaConfigTypeDef):
    """
    Type definition for `ClientCreateUserPool` `LambdaConfig`

    The Lambda trigger configuration information for the new user pool.

    .. note::

      In a push model, event sources (such as Amazon S3 and custom applications) need permission to
      invoke a function. So you will need to make an extra call to add permission for these event
      sources to invoke your Lambda function.

      For more information on using the Lambda API to add permission, see `AddPermission
      <https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html>`__ .

      For adding permission using the AWS CLI, see `add-permission
      <https://docs.aws.amazon.com/cli/latest/reference/lambda/add-permission.html>`__ .

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ClientCreateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientCreateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientCreateUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientCreateUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    Type definition for `ClientCreateUserPoolPolicies` `PasswordPolicy`

    The password policy.

    - **MinimumLength** *(integer) --*

      The minimum length of the password policy that you have set. Cannot be less than 6.

    - **RequireUppercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one uppercase letter in their password.

    - **RequireLowercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one lowercase letter in their password.

    - **RequireNumbers** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one number in their password.

    - **RequireSymbols** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one symbol in their password.

    - **TemporaryPasswordValidityDays** *(integer) --*

      In the password policy you have set, refers to the number of days a temporary password is
      valid. If the user does not sign-in during this time, their password will need to be reset by
      an administrator.

      .. note::

        When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be able
        to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientCreateUserPoolPoliciesTypeDef = TypedDict(
    "_ClientCreateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientCreateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientCreateUserPoolPoliciesTypeDef(_ClientCreateUserPoolPoliciesTypeDef):
    """
    Type definition for `ClientCreateUserPool` `Policies`

    The policies associated with the new user pool.

    - **PasswordPolicy** *(dict) --*

      The password policy.

      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.

      - **RequireUppercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one uppercase letter in their password.

      - **RequireLowercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one lowercase letter in their password.

      - **RequireNumbers** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one number in their password.

      - **RequireSymbols** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one symbol in their password.

      - **TemporaryPasswordValidityDays** *(integer) --*

        In the password policy you have set, refers to the number of days a temporary password is
        valid. If the user does not sign-in during this time, their password will need to be reset by
        an administrator.

        .. note::

          When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be able
          to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPoolAdminCreateUserConfig` `InviteMessageTemplate`

    The message template to be used for the welcome message to new users.

    See also `Customizing User Invitation Messages
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
    .

    - **SMSMessage** *(string) --*

      The message template for SMS messages.

    - **EmailMessage** *(string) --*

      The message template for email messages.

    - **EmailSubject** *(string) --*

      The subject line for email messages.
    """


_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef(
    _ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `AdminCreateUserConfig`

    The configuration for ``AdminCreateUser`` requests.

    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to
      ``False`` if users can sign themselves up via an app.

    - **UnusedAccountValidityDays** *(integer) --*

      The user account expiration limit, in days, after which the account is no longer usable.
      To reset the account after that time limit, you must call ``AdminCreateUser`` again,
      specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
      parameter is 7.

      .. note::

        If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
        value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
        pool.

    - **InviteMessageTemplate** *(dict) --*

      The message template to be used for the welcome message to new users.

      See also `Customizing User Invitation Messages
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
      .

      - **SMSMessage** *(string) --*

        The message template for SMS messages.

      - **EmailMessage** *(string) --*

        The message template for email messages.

      - **EmailSubject** *(string) --*

        The subject line for email messages.
    """


_ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `DeviceConfiguration`

    The device configuration.

    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new
      device.

    - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

      If true, a device is only remembered on user prompt.
    """


_ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": str,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `EmailConfiguration`

    The email configuration.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
      address is used in one of the following ways, depending on the value that you specify for
      the ``EmailSendingAccount`` parameter:

      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
      FROM address when it emails your users by using its built-in email account.

      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
      calling Amazon SES on your behalf.

    - **ReplyToEmailAddress** *(string) --*

      The destination to which the receiver of the email should reply to.

    - **EmailSendingAccount** *(string) --*

      Specifies whether Amazon Cognito emails your users by using its built-in email
      functionality or your Amazon SES email configuration. Specify one of the following values:

        COGNITO_DEFAULT

      When Amazon Cognito emails your users, it uses its built-in email functionality. When you
      use the default option, Amazon Cognito allows only a limited number of emails each day
      for your user pool. For typical production environments, the default email limit is below
      the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
      use your Amazon SES email configuration.

      To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
      Cognito Developer Guide* .

      The default FROM address is no-reply@verificationemail.com. To customize the FROM
      address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
      parameter.

        DEVELOPER

      When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
      Cognito calls Amazon SES on your behalf to send email from your verified email address.
      When you use this option, the email delivery limits are the same limits that apply to
      your Amazon SES verified email address in your AWS account.

      If you use this option, you must provide the ARN of an Amazon SES verified email address
      for the ``SourceArn`` parameter.

      Before Amazon Cognito can email your users, it requires additional permissions to call
      Amazon SES on your behalf. When you update your user pool with this option, Amazon
      Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
      account. This role contains the permissions that allow Amazon Cognito to access Amazon
      SES and send email messages with your address. For more information about the
      service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
      Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
      in the *Amazon Cognito Developer Guide* .

    - **From** *(string) --*

      Identifies either the sender’s email address or the sender’s name with their email
      address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
      This address will appear before the body of the email.

    - **ConfigurationSet** *(string) --*

      The set of configuration rules that can be applied to emails sent using Amazon SES. A
      configuration set is applied to an email by including a reference to the configuration
      set in the headers of the email. Once applied, all of the rules in that configuration set
      are applied to the email. Configuration sets can be used to apply the following types of
      rules to emails:

      * Event publishing – Amazon SES can track the number of send, delivery, open, click,
      bounce, and complaint events for each email sent. Use event publishing to send
      information about these events to other AWS services such as SNS and CloudWatch.

      * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
      create groups of IP addresses, called dedicated IP pools. You can then associate the
      dedicated IP pools with configuration sets.
    """


_ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef(
    _ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `LambdaConfig`

    The AWS Lambda triggers associated with the user pool.

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPoolPolicies` `PasswordPolicy`

    The password policy.

    - **MinimumLength** *(integer) --*

      The minimum length of the password policy that you have set. Cannot be less than 6.

    - **RequireUppercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one uppercase letter in their password.

    - **RequireLowercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one lowercase letter in their password.

    - **RequireNumbers** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one number in their password.

    - **RequireSymbols** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one symbol in their password.

    - **TemporaryPasswordValidityDays** *(integer) --*

      In the password policy you have set, refers to the number of days a temporary password
      is valid. If the user does not sign-in during this time, their password will need to be
      reset by an administrator.

      .. note::

        When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
        able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientCreateUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolPoliciesTypeDef",
    {
        "PasswordPolicy": ClientCreateUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolPoliciesTypeDef(
    _ClientCreateUserPoolResponseUserPoolPoliciesTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `Policies`

    The policies associated with the user pool.

    - **PasswordPolicy** *(dict) --*

      The password policy.

      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.

      - **RequireUppercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one uppercase letter in their password.

      - **RequireLowercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one lowercase letter in their password.

      - **RequireNumbers** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one number in their password.

      - **RequireSymbols** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one symbol in their password.

      - **TemporaryPasswordValidityDays** *(integer) --*

        In the password policy you have set, refers to the number of days a temporary password
        is valid. If the user does not sign-in during this time, their password will need to be
        reset by an administrator.

        .. note::

          When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
          able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPoolSchemaAttributes` `NumberAttributeConstraints`

    Specifies the constraints for an attribute of the number type.

    - **MinValue** *(string) --*

      The minimum value of an attribute that is of the number data type.

    - **MaxValue** *(string) --*

      The maximum value of an attribute that is of the number data type.
    """


_ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPoolSchemaAttributes` `StringAttributeConstraints`

    Specifies the constraints for an attribute of the string type.

    - **MinLength** *(string) --*

      The minimum length.

    - **MaxLength** *(string) --*

      The maximum length.
    """


_ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": str,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef(
    _ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `SchemaAttributes`

    Contains information about the schema attribute.

    - **Name** *(string) --*

      A schema attribute of the name type.

    - **AttributeDataType** *(string) --*

      The attribute data type.

    - **DeveloperOnlyAttribute** *(boolean) --*

      Specifies whether the attribute type is developer only.

    - **Mutable** *(boolean) --*

      Specifies whether the value of the attribute can be changed.

      For any user pool attribute that's mapped to an identity provider attribute, you must
      set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
      sign in to your application through an identity provider. If an attribute is immutable,
      Amazon Cognito throws an error when it attempts to update the attribute. For more
      information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
      .

    - **Required** *(boolean) --*

      Specifies whether a user pool attribute is required. If the attribute is required and
      the user does not provide a value, registration or sign-in will fail.

    - **NumberAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the number type.

      - **MinValue** *(string) --*

        The minimum value of an attribute that is of the number data type.

      - **MaxValue** *(string) --*

        The maximum value of an attribute that is of the number data type.

    - **StringAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the string type.

      - **MinLength** *(string) --*

        The minimum length.

      - **MaxLength** *(string) --*

        The maximum length.
    """


_ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef(
    _ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
      This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
      messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role
      which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
      an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
      IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
      you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
      a role with the required permissions and a trust policy that demonstrates use of the
      ``ExternalId`` .
    """


_ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": str},
    total=False,
)


class ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef(
    _ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `UserPoolAddOns`

    The user pool add-ons.

    - **AdvancedSecurityMode** *(string) --*

      The advanced security mode.
    """


_ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef(
    _ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponseUserPool` `VerificationMessageTemplate`

    The template for verification messages.

    - **SmsMessage** *(string) --*

      The SMS message template.

    - **EmailMessage** *(string) --*

      The email message template.

    - **EmailSubject** *(string) --*

      The subject line for the email message template.

    - **EmailMessageByLink** *(string) --*

      The email message template for sending a confirmation link to the user.

    - **EmailSubjectByLink** *(string) --*

      The subject line for the email message template for sending a confirmation link to the
      user.

    - **DefaultEmailOption** *(string) --*

      The default email option.
    """


_ClientCreateUserPoolResponseUserPoolTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientCreateUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientCreateUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[
            ClientCreateUserPoolResponseUserPoolSchemaAttributesTypeDef
        ],
        "AutoVerifiedAttributes": List[str],
        "AliasAttributes": List[str],
        "UsernameAttributes": List[str],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientCreateUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": str,
        "DeviceConfiguration": ClientCreateUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientCreateUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientCreateUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientCreateUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientCreateUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "Arn": str,
    },
    total=False,
)


class ClientCreateUserPoolResponseUserPoolTypeDef(
    _ClientCreateUserPoolResponseUserPoolTypeDef
):
    """
    Type definition for `ClientCreateUserPoolResponse` `UserPool`

    A container for the user pool details.

    - **Id** *(string) --*

      The ID of the user pool.

    - **Name** *(string) --*

      The name of the user pool.

    - **Policies** *(dict) --*

      The policies associated with the user pool.

      - **PasswordPolicy** *(dict) --*

        The password policy.

        - **MinimumLength** *(integer) --*

          The minimum length of the password policy that you have set. Cannot be less than 6.

        - **RequireUppercase** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one uppercase letter in their password.

        - **RequireLowercase** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one lowercase letter in their password.

        - **RequireNumbers** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one number in their password.

        - **RequireSymbols** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one symbol in their password.

        - **TemporaryPasswordValidityDays** *(integer) --*

          In the password policy you have set, refers to the number of days a temporary password
          is valid. If the user does not sign-in during this time, their password will need to be
          reset by an administrator.

          .. note::

            When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
            able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.

    - **LambdaConfig** *(dict) --*

      The AWS Lambda triggers associated with the user pool.

      - **PreSignUp** *(string) --*

        A pre-registration AWS Lambda trigger.

      - **CustomMessage** *(string) --*

        A custom Message AWS Lambda trigger.

      - **PostConfirmation** *(string) --*

        A post-confirmation AWS Lambda trigger.

      - **PreAuthentication** *(string) --*

        A pre-authentication AWS Lambda trigger.

      - **PostAuthentication** *(string) --*

        A post-authentication AWS Lambda trigger.

      - **DefineAuthChallenge** *(string) --*

        Defines the authentication challenge.

      - **CreateAuthChallenge** *(string) --*

        Creates an authentication challenge.

      - **VerifyAuthChallengeResponse** *(string) --*

        Verifies the authentication challenge response.

      - **PreTokenGeneration** *(string) --*

        A Lambda trigger that is invoked before token generation.

      - **UserMigration** *(string) --*

        The user migration Lambda config type.

    - **Status** *(string) --*

      The status of a user pool.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool was created.

    - **SchemaAttributes** *(list) --*

      A container with the schema attributes of a user pool.

      - *(dict) --*

        Contains information about the schema attribute.

        - **Name** *(string) --*

          A schema attribute of the name type.

        - **AttributeDataType** *(string) --*

          The attribute data type.

        - **DeveloperOnlyAttribute** *(boolean) --*

          Specifies whether the attribute type is developer only.

        - **Mutable** *(boolean) --*

          Specifies whether the value of the attribute can be changed.

          For any user pool attribute that's mapped to an identity provider attribute, you must
          set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
          sign in to your application through an identity provider. If an attribute is immutable,
          Amazon Cognito throws an error when it attempts to update the attribute. For more
          information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
          <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
          .

        - **Required** *(boolean) --*

          Specifies whether a user pool attribute is required. If the attribute is required and
          the user does not provide a value, registration or sign-in will fail.

        - **NumberAttributeConstraints** *(dict) --*

          Specifies the constraints for an attribute of the number type.

          - **MinValue** *(string) --*

            The minimum value of an attribute that is of the number data type.

          - **MaxValue** *(string) --*

            The maximum value of an attribute that is of the number data type.

        - **StringAttributeConstraints** *(dict) --*

          Specifies the constraints for an attribute of the string type.

          - **MinLength** *(string) --*

            The minimum length.

          - **MaxLength** *(string) --*

            The maximum length.

    - **AutoVerifiedAttributes** *(list) --*

      Specifies the attributes that are auto-verified in a user pool.

      - *(string) --*

    - **AliasAttributes** *(list) --*

      Specifies the attributes that are aliased in a user pool.

      - *(string) --*

    - **UsernameAttributes** *(list) --*

      Specifies whether email addresses or phone numbers can be specified as usernames when a
      user signs up.

      - *(string) --*

    - **SmsVerificationMessage** *(string) --*

      The contents of the SMS verification message.

    - **EmailVerificationMessage** *(string) --*

      The contents of the email verification message.

    - **EmailVerificationSubject** *(string) --*

      The subject of the email verification message.

    - **VerificationMessageTemplate** *(dict) --*

      The template for verification messages.

      - **SmsMessage** *(string) --*

        The SMS message template.

      - **EmailMessage** *(string) --*

        The email message template.

      - **EmailSubject** *(string) --*

        The subject line for the email message template.

      - **EmailMessageByLink** *(string) --*

        The email message template for sending a confirmation link to the user.

      - **EmailSubjectByLink** *(string) --*

        The subject line for the email message template for sending a confirmation link to the
        user.

      - **DefaultEmailOption** *(string) --*

        The default email option.

    - **SmsAuthenticationMessage** *(string) --*

      The contents of the SMS authentication message.

    - **MfaConfiguration** *(string) --*

      Can be one of the following values:

      * ``OFF`` - MFA tokens are not required and cannot be specified during user registration.

      * ``ON`` - MFA tokens are required for all user registrations. You can only specify
      required when you are initially creating a user pool.

      * ``OPTIONAL`` - Users have the option when registering to create an MFA token.

    - **DeviceConfiguration** *(dict) --*

      The device configuration.

      - **ChallengeRequiredOnNewDevice** *(boolean) --*

        Indicates whether a challenge is required on a new device. Only applicable to a new
        device.

      - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

        If true, a device is only remembered on user prompt.

    - **EstimatedNumberOfUsers** *(integer) --*

      A number estimating the size of the user pool.

    - **EmailConfiguration** *(dict) --*

      The email configuration.

      - **SourceArn** *(string) --*

        The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
        address is used in one of the following ways, depending on the value that you specify for
        the ``EmailSendingAccount`` parameter:

        * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
        FROM address when it emails your users by using its built-in email account.

        * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
        calling Amazon SES on your behalf.

      - **ReplyToEmailAddress** *(string) --*

        The destination to which the receiver of the email should reply to.

      - **EmailSendingAccount** *(string) --*

        Specifies whether Amazon Cognito emails your users by using its built-in email
        functionality or your Amazon SES email configuration. Specify one of the following values:

          COGNITO_DEFAULT

        When Amazon Cognito emails your users, it uses its built-in email functionality. When you
        use the default option, Amazon Cognito allows only a limited number of emails each day
        for your user pool. For typical production environments, the default email limit is below
        the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
        use your Amazon SES email configuration.

        To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
        <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
        Cognito Developer Guide* .

        The default FROM address is no-reply@verificationemail.com. To customize the FROM
        address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
        parameter.

          DEVELOPER

        When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
        Cognito calls Amazon SES on your behalf to send email from your verified email address.
        When you use this option, the email delivery limits are the same limits that apply to
        your Amazon SES verified email address in your AWS account.

        If you use this option, you must provide the ARN of an Amazon SES verified email address
        for the ``SourceArn`` parameter.

        Before Amazon Cognito can email your users, it requires additional permissions to call
        Amazon SES on your behalf. When you update your user pool with this option, Amazon
        Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
        account. This role contains the permissions that allow Amazon Cognito to access Amazon
        SES and send email messages with your address. For more information about the
        service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
        Amazon Cognito
        <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
        in the *Amazon Cognito Developer Guide* .

      - **From** *(string) --*

        Identifies either the sender’s email address or the sender’s name with their email
        address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
        This address will appear before the body of the email.

      - **ConfigurationSet** *(string) --*

        The set of configuration rules that can be applied to emails sent using Amazon SES. A
        configuration set is applied to an email by including a reference to the configuration
        set in the headers of the email. Once applied, all of the rules in that configuration set
        are applied to the email. Configuration sets can be used to apply the following types of
        rules to emails:

        * Event publishing – Amazon SES can track the number of send, delivery, open, click,
        bounce, and complaint events for each email sent. Use event publishing to send
        information about these events to other AWS services such as SNS and CloudWatch.

        * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
        create groups of IP addresses, called dedicated IP pools. You can then associate the
        dedicated IP pools with configuration sets.

    - **SmsConfiguration** *(dict) --*

      The SMS configuration.

      - **SnsCallerArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
        This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
        messages.

      - **ExternalId** *(string) --*

        The external ID is a value that we recommend you use to add security to your IAM role
        which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
        an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
        IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
        you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
        a role with the required permissions and a trust policy that demonstrates use of the
        ``ExternalId`` .

    - **UserPoolTags** *(dict) --*

      The tags that are assigned to the user pool. A tag is a label that you can apply to user
      pools to categorize and manage them in different ways, such as by purpose, owner,
      environment, or other criteria.

      - *(string) --*

        - *(string) --*

    - **SmsConfigurationFailure** *(string) --*

      The reason why the SMS configuration cannot send the messages to your users.

    - **EmailConfigurationFailure** *(string) --*

      The reason why the email configuration cannot send the messages to your users.

    - **Domain** *(string) --*

      Holds the domain prefix if the user pool has a domain associated with it.

    - **CustomDomain** *(string) --*

      A custom domain name that you provide to Amazon Cognito. This parameter applies only if you
      use a custom domain to host the sign-up and sign-in pages for your application. For
      example: ``auth.example.com`` .

      For more information about adding a custom domain to your user pool, see `Using Your Own
      Domain for the Hosted UI
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__
      .

    - **AdminCreateUserConfig** *(dict) --*

      The configuration for ``AdminCreateUser`` requests.

      - **AllowAdminCreateUserOnly** *(boolean) --*

        Set to ``True`` if only the administrator is allowed to create user profiles. Set to
        ``False`` if users can sign themselves up via an app.

      - **UnusedAccountValidityDays** *(integer) --*

        The user account expiration limit, in days, after which the account is no longer usable.
        To reset the account after that time limit, you must call ``AdminCreateUser`` again,
        specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
        parameter is 7.

        .. note::

          If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
          value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
          pool.

      - **InviteMessageTemplate** *(dict) --*

        The message template to be used for the welcome message to new users.

        See also `Customizing User Invitation Messages
        <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
        .

        - **SMSMessage** *(string) --*

          The message template for SMS messages.

        - **EmailMessage** *(string) --*

          The message template for email messages.

        - **EmailSubject** *(string) --*

          The subject line for email messages.

    - **UserPoolAddOns** *(dict) --*

      The user pool add-ons.

      - **AdvancedSecurityMode** *(string) --*

        The advanced security mode.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user pool.
    """


_ClientCreateUserPoolResponseTypeDef = TypedDict(
    "_ClientCreateUserPoolResponseTypeDef",
    {"UserPool": ClientCreateUserPoolResponseUserPoolTypeDef},
    total=False,
)


class ClientCreateUserPoolResponseTypeDef(_ClientCreateUserPoolResponseTypeDef):
    """
    Type definition for `ClientCreateUserPool` `Response`

    Represents the response from the server for the request to create a user pool.

    - **UserPool** *(dict) --*

      A container for the user pool details.

      - **Id** *(string) --*

        The ID of the user pool.

      - **Name** *(string) --*

        The name of the user pool.

      - **Policies** *(dict) --*

        The policies associated with the user pool.

        - **PasswordPolicy** *(dict) --*

          The password policy.

          - **MinimumLength** *(integer) --*

            The minimum length of the password policy that you have set. Cannot be less than 6.

          - **RequireUppercase** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one uppercase letter in their password.

          - **RequireLowercase** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one lowercase letter in their password.

          - **RequireNumbers** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one number in their password.

          - **RequireSymbols** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one symbol in their password.

          - **TemporaryPasswordValidityDays** *(integer) --*

            In the password policy you have set, refers to the number of days a temporary password
            is valid. If the user does not sign-in during this time, their password will need to be
            reset by an administrator.

            .. note::

              When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
              able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.

      - **LambdaConfig** *(dict) --*

        The AWS Lambda triggers associated with the user pool.

        - **PreSignUp** *(string) --*

          A pre-registration AWS Lambda trigger.

        - **CustomMessage** *(string) --*

          A custom Message AWS Lambda trigger.

        - **PostConfirmation** *(string) --*

          A post-confirmation AWS Lambda trigger.

        - **PreAuthentication** *(string) --*

          A pre-authentication AWS Lambda trigger.

        - **PostAuthentication** *(string) --*

          A post-authentication AWS Lambda trigger.

        - **DefineAuthChallenge** *(string) --*

          Defines the authentication challenge.

        - **CreateAuthChallenge** *(string) --*

          Creates an authentication challenge.

        - **VerifyAuthChallengeResponse** *(string) --*

          Verifies the authentication challenge response.

        - **PreTokenGeneration** *(string) --*

          A Lambda trigger that is invoked before token generation.

        - **UserMigration** *(string) --*

          The user migration Lambda config type.

      - **Status** *(string) --*

        The status of a user pool.

      - **LastModifiedDate** *(datetime) --*

        The date the user pool was last modified.

      - **CreationDate** *(datetime) --*

        The date the user pool was created.

      - **SchemaAttributes** *(list) --*

        A container with the schema attributes of a user pool.

        - *(dict) --*

          Contains information about the schema attribute.

          - **Name** *(string) --*

            A schema attribute of the name type.

          - **AttributeDataType** *(string) --*

            The attribute data type.

          - **DeveloperOnlyAttribute** *(boolean) --*

            Specifies whether the attribute type is developer only.

          - **Mutable** *(boolean) --*

            Specifies whether the value of the attribute can be changed.

            For any user pool attribute that's mapped to an identity provider attribute, you must
            set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
            sign in to your application through an identity provider. If an attribute is immutable,
            Amazon Cognito throws an error when it attempts to update the attribute. For more
            information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
            <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
            .

          - **Required** *(boolean) --*

            Specifies whether a user pool attribute is required. If the attribute is required and
            the user does not provide a value, registration or sign-in will fail.

          - **NumberAttributeConstraints** *(dict) --*

            Specifies the constraints for an attribute of the number type.

            - **MinValue** *(string) --*

              The minimum value of an attribute that is of the number data type.

            - **MaxValue** *(string) --*

              The maximum value of an attribute that is of the number data type.

          - **StringAttributeConstraints** *(dict) --*

            Specifies the constraints for an attribute of the string type.

            - **MinLength** *(string) --*

              The minimum length.

            - **MaxLength** *(string) --*

              The maximum length.

      - **AutoVerifiedAttributes** *(list) --*

        Specifies the attributes that are auto-verified in a user pool.

        - *(string) --*

      - **AliasAttributes** *(list) --*

        Specifies the attributes that are aliased in a user pool.

        - *(string) --*

      - **UsernameAttributes** *(list) --*

        Specifies whether email addresses or phone numbers can be specified as usernames when a
        user signs up.

        - *(string) --*

      - **SmsVerificationMessage** *(string) --*

        The contents of the SMS verification message.

      - **EmailVerificationMessage** *(string) --*

        The contents of the email verification message.

      - **EmailVerificationSubject** *(string) --*

        The subject of the email verification message.

      - **VerificationMessageTemplate** *(dict) --*

        The template for verification messages.

        - **SmsMessage** *(string) --*

          The SMS message template.

        - **EmailMessage** *(string) --*

          The email message template.

        - **EmailSubject** *(string) --*

          The subject line for the email message template.

        - **EmailMessageByLink** *(string) --*

          The email message template for sending a confirmation link to the user.

        - **EmailSubjectByLink** *(string) --*

          The subject line for the email message template for sending a confirmation link to the
          user.

        - **DefaultEmailOption** *(string) --*

          The default email option.

      - **SmsAuthenticationMessage** *(string) --*

        The contents of the SMS authentication message.

      - **MfaConfiguration** *(string) --*

        Can be one of the following values:

        * ``OFF`` - MFA tokens are not required and cannot be specified during user registration.

        * ``ON`` - MFA tokens are required for all user registrations. You can only specify
        required when you are initially creating a user pool.

        * ``OPTIONAL`` - Users have the option when registering to create an MFA token.

      - **DeviceConfiguration** *(dict) --*

        The device configuration.

        - **ChallengeRequiredOnNewDevice** *(boolean) --*

          Indicates whether a challenge is required on a new device. Only applicable to a new
          device.

        - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

          If true, a device is only remembered on user prompt.

      - **EstimatedNumberOfUsers** *(integer) --*

        A number estimating the size of the user pool.

      - **EmailConfiguration** *(dict) --*

        The email configuration.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
          address is used in one of the following ways, depending on the value that you specify for
          the ``EmailSendingAccount`` parameter:

          * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
          FROM address when it emails your users by using its built-in email account.

          * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
          calling Amazon SES on your behalf.

        - **ReplyToEmailAddress** *(string) --*

          The destination to which the receiver of the email should reply to.

        - **EmailSendingAccount** *(string) --*

          Specifies whether Amazon Cognito emails your users by using its built-in email
          functionality or your Amazon SES email configuration. Specify one of the following values:

            COGNITO_DEFAULT

          When Amazon Cognito emails your users, it uses its built-in email functionality. When you
          use the default option, Amazon Cognito allows only a limited number of emails each day
          for your user pool. For typical production environments, the default email limit is below
          the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
          use your Amazon SES email configuration.

          To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
          <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
          Cognito Developer Guide* .

          The default FROM address is no-reply@verificationemail.com. To customize the FROM
          address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
          parameter.

            DEVELOPER

          When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
          Cognito calls Amazon SES on your behalf to send email from your verified email address.
          When you use this option, the email delivery limits are the same limits that apply to
          your Amazon SES verified email address in your AWS account.

          If you use this option, you must provide the ARN of an Amazon SES verified email address
          for the ``SourceArn`` parameter.

          Before Amazon Cognito can email your users, it requires additional permissions to call
          Amazon SES on your behalf. When you update your user pool with this option, Amazon
          Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
          account. This role contains the permissions that allow Amazon Cognito to access Amazon
          SES and send email messages with your address. For more information about the
          service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
          Amazon Cognito
          <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
          in the *Amazon Cognito Developer Guide* .

        - **From** *(string) --*

          Identifies either the sender’s email address or the sender’s name with their email
          address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
          This address will appear before the body of the email.

        - **ConfigurationSet** *(string) --*

          The set of configuration rules that can be applied to emails sent using Amazon SES. A
          configuration set is applied to an email by including a reference to the configuration
          set in the headers of the email. Once applied, all of the rules in that configuration set
          are applied to the email. Configuration sets can be used to apply the following types of
          rules to emails:

          * Event publishing – Amazon SES can track the number of send, delivery, open, click,
          bounce, and complaint events for each email sent. Use event publishing to send
          information about these events to other AWS services such as SNS and CloudWatch.

          * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
          create groups of IP addresses, called dedicated IP pools. You can then associate the
          dedicated IP pools with configuration sets.

      - **SmsConfiguration** *(dict) --*

        The SMS configuration.

        - **SnsCallerArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
          This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
          messages.

        - **ExternalId** *(string) --*

          The external ID is a value that we recommend you use to add security to your IAM role
          which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
          an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
          IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
          you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
          a role with the required permissions and a trust policy that demonstrates use of the
          ``ExternalId`` .

      - **UserPoolTags** *(dict) --*

        The tags that are assigned to the user pool. A tag is a label that you can apply to user
        pools to categorize and manage them in different ways, such as by purpose, owner,
        environment, or other criteria.

        - *(string) --*

          - *(string) --*

      - **SmsConfigurationFailure** *(string) --*

        The reason why the SMS configuration cannot send the messages to your users.

      - **EmailConfigurationFailure** *(string) --*

        The reason why the email configuration cannot send the messages to your users.

      - **Domain** *(string) --*

        Holds the domain prefix if the user pool has a domain associated with it.

      - **CustomDomain** *(string) --*

        A custom domain name that you provide to Amazon Cognito. This parameter applies only if you
        use a custom domain to host the sign-up and sign-in pages for your application. For
        example: ``auth.example.com`` .

        For more information about adding a custom domain to your user pool, see `Using Your Own
        Domain for the Hosted UI
        <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__
        .

      - **AdminCreateUserConfig** *(dict) --*

        The configuration for ``AdminCreateUser`` requests.

        - **AllowAdminCreateUserOnly** *(boolean) --*

          Set to ``True`` if only the administrator is allowed to create user profiles. Set to
          ``False`` if users can sign themselves up via an app.

        - **UnusedAccountValidityDays** *(integer) --*

          The user account expiration limit, in days, after which the account is no longer usable.
          To reset the account after that time limit, you must call ``AdminCreateUser`` again,
          specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
          parameter is 7.

          .. note::

            If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
            value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
            pool.

        - **InviteMessageTemplate** *(dict) --*

          The message template to be used for the welcome message to new users.

          See also `Customizing User Invitation Messages
          <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
          .

          - **SMSMessage** *(string) --*

            The message template for SMS messages.

          - **EmailMessage** *(string) --*

            The message template for email messages.

          - **EmailSubject** *(string) --*

            The subject line for email messages.

      - **UserPoolAddOns** *(dict) --*

        The user pool add-ons.

        - **AdvancedSecurityMode** *(string) --*

          The advanced security mode.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the user pool.
    """


_ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef(
    _ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientCreateUserPoolSchema` `NumberAttributeConstraints`

    Specifies the constraints for an attribute of the number type.

    - **MinValue** *(string) --*

      The minimum value of an attribute that is of the number data type.

    - **MaxValue** *(string) --*

      The maximum value of an attribute that is of the number data type.
    """


_ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef(
    _ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientCreateUserPoolSchema` `StringAttributeConstraints`

    Specifies the constraints for an attribute of the string type.

    - **MinLength** *(string) --*

      The minimum length.

    - **MaxLength** *(string) --*

      The maximum length.
    """


_ClientCreateUserPoolSchemaTypeDef = TypedDict(
    "_ClientCreateUserPoolSchemaTypeDef",
    {
        "Name": str,
        "AttributeDataType": str,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientCreateUserPoolSchemaNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientCreateUserPoolSchemaStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientCreateUserPoolSchemaTypeDef(_ClientCreateUserPoolSchemaTypeDef):
    """
    Type definition for `ClientCreateUserPool` `Schema`

    Contains information about the schema attribute.

    - **Name** *(string) --*

      A schema attribute of the name type.

    - **AttributeDataType** *(string) --*

      The attribute data type.

    - **DeveloperOnlyAttribute** *(boolean) --*

      Specifies whether the attribute type is developer only.

    - **Mutable** *(boolean) --*

      Specifies whether the value of the attribute can be changed.

      For any user pool attribute that's mapped to an identity provider attribute, you must set
      this parameter to ``true`` . Amazon Cognito updates mapped attributes when users sign in to
      your application through an identity provider. If an attribute is immutable, Amazon Cognito
      throws an error when it attempts to update the attribute. For more information, see
      `Specifying Identity Provider Attribute Mappings for Your User Pool
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
      .

    - **Required** *(boolean) --*

      Specifies whether a user pool attribute is required. If the attribute is required and the
      user does not provide a value, registration or sign-in will fail.

    - **NumberAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the number type.

      - **MinValue** *(string) --*

        The minimum value of an attribute that is of the number data type.

      - **MaxValue** *(string) --*

        The maximum value of an attribute that is of the number data type.

    - **StringAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the string type.

      - **MinLength** *(string) --*

        The minimum length.

      - **MaxLength** *(string) --*

        The maximum length.
    """


_RequiredClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientCreateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateUserPoolSmsConfigurationTypeDef",
    {"ExternalId": str},
    total=False,
)


class ClientCreateUserPoolSmsConfigurationTypeDef(
    _RequiredClientCreateUserPoolSmsConfigurationTypeDef,
    _OptionalClientCreateUserPoolSmsConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateUserPool` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is
      the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role which is
      used to call Amazon SNS to send SMS messages for your user pool. If you provide an
      ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your IAM role,
      so that you can set your roles trust policy to require the ``ExternalID`` . If you use the
      Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the
      required permissions and a trust policy that demonstrates use of the ``ExternalId`` .
    """


_ClientCreateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientCreateUserPoolUserPoolAddOnsTypeDef", {"AdvancedSecurityMode": str}
)


class ClientCreateUserPoolUserPoolAddOnsTypeDef(
    _ClientCreateUserPoolUserPoolAddOnsTypeDef
):
    """
    Type definition for `ClientCreateUserPool` `UserPoolAddOns`

    Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the
    value "AUDIT".

    - **AdvancedSecurityMode** *(string) --* **[REQUIRED]**

      The advanced security mode.
    """


_ClientCreateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientCreateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": str,
    },
    total=False,
)


class ClientCreateUserPoolVerificationMessageTemplateTypeDef(
    _ClientCreateUserPoolVerificationMessageTemplateTypeDef
):
    """
    Type definition for `ClientCreateUserPool` `VerificationMessageTemplate`

    The template for the verification message that the user sees when the app requests permission to
    access the user's information.

    - **SmsMessage** *(string) --*

      The SMS message template.

    - **EmailMessage** *(string) --*

      The email message template.

    - **EmailSubject** *(string) --*

      The subject line for the email message template.

    - **EmailMessageByLink** *(string) --*

      The email message template for sending a confirmation link to the user.

    - **EmailSubjectByLink** *(string) --*

      The subject line for the email message template for sending a confirmation link to the user.

    - **DefaultEmailOption** *(string) --*

      The default email option.
    """


_ClientDescribeIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": str,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientDescribeIdentityProviderResponseIdentityProviderTypeDef(
    _ClientDescribeIdentityProviderResponseIdentityProviderTypeDef
):
    """
    Type definition for `ClientDescribeIdentityProviderResponse` `IdentityProvider`

    The identity provider that was deleted.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **ProviderDetails** *(dict) --*

      The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

      - *(string) --*

        - *(string) --*

    - **AttributeMapping** *(dict) --*

      A mapping of identity provider attributes to standard and custom user pool attributes.

      - *(string) --*

        - *(string) --*

    - **IdpIdentifiers** *(list) --*

      A list of identity provider identifiers.

      - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The date the identity provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the identity provider was created.
    """


_ClientDescribeIdentityProviderResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientDescribeIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientDescribeIdentityProviderResponseTypeDef(
    _ClientDescribeIdentityProviderResponseTypeDef
):
    """
    Type definition for `ClientDescribeIdentityProvider` `Response`

    - **IdentityProvider** *(dict) --*

      The identity provider that was deleted.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ProviderName** *(string) --*

        The identity provider name.

      - **ProviderType** *(string) --*

        The identity provider type.

      - **ProviderDetails** *(dict) --*

        The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

        - *(string) --*

          - *(string) --*

      - **AttributeMapping** *(dict) --*

        A mapping of identity provider attributes to standard and custom user pool attributes.

        - *(string) --*

          - *(string) --*

      - **IdpIdentifiers** *(list) --*

        A list of identity provider identifiers.

        - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The date the identity provider was last modified.

      - **CreationDate** *(datetime) --*

        The date the identity provider was created.
    """


_ClientDescribeResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientDescribeResourceServerResponseResourceServerScopesTypeDef(
    _ClientDescribeResourceServerResponseResourceServerScopesTypeDef
):
    """
    Type definition for `ClientDescribeResourceServerResponseResourceServer` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --*

      The name of the scope.

    - **ScopeDescription** *(string) --*

      A description of the scope.
    """


_ClientDescribeResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientDescribeResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientDescribeResourceServerResponseResourceServerTypeDef(
    _ClientDescribeResourceServerResponseResourceServerTypeDef
):
    """
    Type definition for `ClientDescribeResourceServerResponse` `ResourceServer`

    The resource server.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that hosts the resource server.

    - **Identifier** *(string) --*

      The identifier for the resource server.

    - **Name** *(string) --*

      The name of the resource server.

    - **Scopes** *(list) --*

      A list of scopes that are defined for the resource server.

      - *(dict) --*

        A resource server scope.

        - **ScopeName** *(string) --*

          The name of the scope.

        - **ScopeDescription** *(string) --*

          A description of the scope.
    """


_ClientDescribeResourceServerResponseTypeDef = TypedDict(
    "_ClientDescribeResourceServerResponseTypeDef",
    {"ResourceServer": ClientDescribeResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientDescribeResourceServerResponseTypeDef(
    _ClientDescribeResourceServerResponseTypeDef
):
    """
    Type definition for `ClientDescribeResourceServer` `Response`

    - **ResourceServer** *(dict) --*

      The resource server.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.

      - **Identifier** *(string) --*

        The identifier for the resource server.

      - **Name** *(string) --*

        The name of the resource server.

      - **Scopes** *(list) --*

        A list of scopes that are defined for the resource server.

        - *(dict) --*

          A resource server scope.

          - **ScopeName** *(string) --*

            The name of the scope.

          - **ScopeDescription** *(string) --*

            A description of the scope.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `HighAction`

    Action to take for a high risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `LowAction`

    Action to take for a low risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `MediumAction`

    Action to take for a medium risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfiguration` `Actions`

    Account takeover risk configuration actions

    - **LowAction** *(dict) --*

      Action to take for a low risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **MediumAction** *(dict) --*

      Action to take for a medium risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **HighAction** *(dict) --*

      Action to take for a high risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `BlockEmail`

    Email template used when a detected risk event is blocked.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `MfaEmail`

    The MFA email template used when MFA is challenged as part of a detected risk.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `NoActionEmail`

    The email template used when a detected risk event is allowed.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfiguration` `NotifyConfiguration`

    The notify configuration used to construct email notifications.

    - **From** *(string) --*

      The email address that is sending the email. It must be either individually verified
      with Amazon SES, or from a domain that has been verified with Amazon SES.

    - **ReplyTo** *(string) --*

      The destination to which the receiver of an email should reply to.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the identity that is associated with the sending
      authorization policy. It permits Amazon Cognito to send for the email address specified
      in the ``From`` parameter.

    - **BlockEmail** *(dict) --*

      Email template used when a detected risk event is blocked.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **NoActionEmail** *(dict) --*

      The email template used when a detected risk event is allowed.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **MfaEmail** *(dict) --*

      The MFA email template used when MFA is challenged as part of a detected risk.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfiguration` `AccountTakeoverRiskConfiguration`

    The account takeover risk configuration object including the ``NotifyConfiguration`` object
    and ``Actions`` to take in the case of an account takeover.

    - **NotifyConfiguration** *(dict) --*

      The notify configuration used to construct email notifications.

      - **From** *(string) --*

        The email address that is sending the email. It must be either individually verified
        with Amazon SES, or from a domain that has been verified with Amazon SES.

      - **ReplyTo** *(string) --*

        The destination to which the receiver of an email should reply to.

      - **SourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the identity that is associated with the sending
        authorization policy. It permits Amazon Cognito to send for the email address specified
        in the ``From`` parameter.

      - **BlockEmail** *(dict) --*

        Email template used when a detected risk event is blocked.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **NoActionEmail** *(dict) --*

        The email template used when a detected risk event is allowed.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **MfaEmail** *(dict) --*

        The MFA email template used when MFA is challenged as part of a detected risk.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

    - **Actions** *(dict) --*

      Account takeover risk configuration actions

      - **LowAction** *(dict) --*

        Action to take for a low risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **MediumAction** *(dict) --*

        Action to take for a medium risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **HighAction** *(dict) --*

        Action to take for a high risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": str},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfiguration` `Actions`

    The compromised credentials risk configuration actions.

    - **EventAction** *(string) --*

      The event action.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[str],
        "Actions": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfiguration` `CompromisedCredentialsRiskConfiguration`

    The compromised credentials risk configuration object including the ``EventFilter`` and the
    ``EventAction``

    - **EventFilter** *(list) --*

      Perform the action for these events. The default is to perform all events if no event
      filter is specified.

      - *(string) --*

    - **Actions** *(dict) --*

      The compromised credentials risk configuration actions.

      - **EventAction** *(string) --*

        The event action.
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponseRiskConfiguration` `RiskExceptionConfiguration`

    The configuration to override the risk decision.

    - **BlockedIPRangeList** *(list) --*

      Overrides the risk decision to always block the pre-authentication requests. The IP range
      is in CIDR notation: a compact representation of an IP address and its associated routing
      prefix.

      - *(string) --*

    - **SkippedIPRangeList** *(list) --*

      Risk detection is not performed on the IP addresses in the range list. The IP range is in
      CIDR notation.

      - *(string) --*
    """


_ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef(
    _ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfigurationResponse` `RiskConfiguration`

    The risk configuration.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ClientId** *(string) --*

      The app client ID.

    - **CompromisedCredentialsRiskConfiguration** *(dict) --*

      The compromised credentials risk configuration object including the ``EventFilter`` and the
      ``EventAction``

      - **EventFilter** *(list) --*

        Perform the action for these events. The default is to perform all events if no event
        filter is specified.

        - *(string) --*

      - **Actions** *(dict) --*

        The compromised credentials risk configuration actions.

        - **EventAction** *(string) --*

          The event action.

    - **AccountTakeoverRiskConfiguration** *(dict) --*

      The account takeover risk configuration object including the ``NotifyConfiguration`` object
      and ``Actions`` to take in the case of an account takeover.

      - **NotifyConfiguration** *(dict) --*

        The notify configuration used to construct email notifications.

        - **From** *(string) --*

          The email address that is sending the email. It must be either individually verified
          with Amazon SES, or from a domain that has been verified with Amazon SES.

        - **ReplyTo** *(string) --*

          The destination to which the receiver of an email should reply to.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the identity that is associated with the sending
          authorization policy. It permits Amazon Cognito to send for the email address specified
          in the ``From`` parameter.

        - **BlockEmail** *(dict) --*

          Email template used when a detected risk event is blocked.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

        - **NoActionEmail** *(dict) --*

          The email template used when a detected risk event is allowed.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

        - **MfaEmail** *(dict) --*

          The MFA email template used when MFA is challenged as part of a detected risk.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

      - **Actions** *(dict) --*

        Account takeover risk configuration actions

        - **LowAction** *(dict) --*

          Action to take for a low risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

        - **MediumAction** *(dict) --*

          Action to take for a medium risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

        - **HighAction** *(dict) --*

          Action to take for a high risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

    - **RiskExceptionConfiguration** *(dict) --*

      The configuration to override the risk decision.

      - **BlockedIPRangeList** *(list) --*

        Overrides the risk decision to always block the pre-authentication requests. The IP range
        is in CIDR notation: a compact representation of an IP address and its associated routing
        prefix.

        - *(string) --*

      - **SkippedIPRangeList** *(list) --*

        Risk detection is not performed on the IP addresses in the range list. The IP range is in
        CIDR notation.

        - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The last modified date.
    """


_ClientDescribeRiskConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": ClientDescribeRiskConfigurationResponseRiskConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeRiskConfigurationResponseTypeDef(
    _ClientDescribeRiskConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeRiskConfiguration` `Response`

    - **RiskConfiguration** *(dict) --*

      The risk configuration.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ClientId** *(string) --*

        The app client ID.

      - **CompromisedCredentialsRiskConfiguration** *(dict) --*

        The compromised credentials risk configuration object including the ``EventFilter`` and the
        ``EventAction``

        - **EventFilter** *(list) --*

          Perform the action for these events. The default is to perform all events if no event
          filter is specified.

          - *(string) --*

        - **Actions** *(dict) --*

          The compromised credentials risk configuration actions.

          - **EventAction** *(string) --*

            The event action.

      - **AccountTakeoverRiskConfiguration** *(dict) --*

        The account takeover risk configuration object including the ``NotifyConfiguration`` object
        and ``Actions`` to take in the case of an account takeover.

        - **NotifyConfiguration** *(dict) --*

          The notify configuration used to construct email notifications.

          - **From** *(string) --*

            The email address that is sending the email. It must be either individually verified
            with Amazon SES, or from a domain that has been verified with Amazon SES.

          - **ReplyTo** *(string) --*

            The destination to which the receiver of an email should reply to.

          - **SourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the identity that is associated with the sending
            authorization policy. It permits Amazon Cognito to send for the email address specified
            in the ``From`` parameter.

          - **BlockEmail** *(dict) --*

            Email template used when a detected risk event is blocked.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

          - **NoActionEmail** *(dict) --*

            The email template used when a detected risk event is allowed.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

          - **MfaEmail** *(dict) --*

            The MFA email template used when MFA is challenged as part of a detected risk.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

        - **Actions** *(dict) --*

          Account takeover risk configuration actions

          - **LowAction** *(dict) --*

            Action to take for a low risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

          - **MediumAction** *(dict) --*

            Action to take for a medium risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

          - **HighAction** *(dict) --*

            Action to take for a high risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

      - **RiskExceptionConfiguration** *(dict) --*

        The configuration to override the risk decision.

        - **BlockedIPRangeList** *(list) --*

          Overrides the risk decision to always block the pre-authentication requests. The IP range
          is in CIDR notation: a compact representation of an IP address and its associated routing
          prefix.

          - *(string) --*

        - **SkippedIPRangeList** *(list) --*

          Risk detection is not performed on the IP addresses in the range list. The IP range is in
          CIDR notation.

          - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The last modified date.
    """


_ClientDescribeUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientDescribeUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientDescribeUserImportJobResponseUserImportJobTypeDef(
    _ClientDescribeUserImportJobResponseUserImportJobTypeDef
):
    """
    Type definition for `ClientDescribeUserImportJobResponse` `UserImportJob`

    The job object that represents the user import job.

    - **JobName** *(string) --*

      The job name for the user import job.

    - **JobId** *(string) --*

      The job ID for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are being imported into.

    - **PreSignedUrl** *(string) --*

      The pre-signed URL to be used to upload the ``.csv`` file.

    - **CreationDate** *(datetime) --*

      The date the user import job was created.

    - **StartDate** *(datetime) --*

      The date when the user import job was started.

    - **CompletionDate** *(datetime) --*

      The date when the user import job was completed.

    - **Status** *(string) --*

      The status of the user import job. One of the following:

      * ``Created`` - The job was created but not started.

      * ``Pending`` - A transition state. You have started the job, but it has not begun
      importing users yet.

      * ``InProgress`` - The job has started, and users are being imported.

      * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

      * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

      * ``Succeeded`` - The job has completed successfully.

      * ``Failed`` - The job has stopped due to an error.

      * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
      associated with the job was deleted, and the job cannot be started.

    - **CloudWatchLogsRoleArn** *(string) --*

      The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
      information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
      Guide.

    - **ImportedUsers** *(integer) --*

      The number of users that were successfully imported.

    - **SkippedUsers** *(integer) --*

      The number of users that were skipped.

    - **FailedUsers** *(integer) --*

      The number of users that could not be imported.

    - **CompletionMessage** *(string) --*

      The message returned when the user import job is completed.
    """


_ClientDescribeUserImportJobResponseTypeDef = TypedDict(
    "_ClientDescribeUserImportJobResponseTypeDef",
    {"UserImportJob": ClientDescribeUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientDescribeUserImportJobResponseTypeDef(
    _ClientDescribeUserImportJobResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserImportJob` `Response`

    Represents the response from the server to the request to describe the user import job.

    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.

      - **JobName** *(string) --*

        The job name for the user import job.

      - **JobId** *(string) --*

        The job ID for the user import job.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that the users are being imported into.

      - **PreSignedUrl** *(string) --*

        The pre-signed URL to be used to upload the ``.csv`` file.

      - **CreationDate** *(datetime) --*

        The date the user import job was created.

      - **StartDate** *(datetime) --*

        The date when the user import job was started.

      - **CompletionDate** *(datetime) --*

        The date when the user import job was completed.

      - **Status** *(string) --*

        The status of the user import job. One of the following:

        * ``Created`` - The job was created but not started.

        * ``Pending`` - A transition state. You have started the job, but it has not begun
        importing users yet.

        * ``InProgress`` - The job has started, and users are being imported.

        * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

        * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

        * ``Succeeded`` - The job has completed successfully.

        * ``Failed`` - The job has stopped due to an error.

        * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
        associated with the job was deleted, and the job cannot be started.

      - **CloudWatchLogsRoleArn** *(string) --*

        The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
        information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
        Guide.

      - **ImportedUsers** *(integer) --*

        The number of users that were successfully imported.

      - **SkippedUsers** *(integer) --*

        The number of users that were skipped.

      - **FailedUsers** *(integer) --*

        The number of users that could not be imported.

      - **CompletionMessage** *(string) --*

        The message returned when the user import job is completed.
    """


_ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolClientResponseUserPoolClient` `AnalyticsConfiguration`

    The Amazon Pinpoint analytics configuration for the user pool client.

    - **ApplicationId** *(string) --*

      The application ID for an Amazon Pinpoint application.

    - **RoleArn** *(string) --*

      The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
      Pinpoint analytics.

    - **ExternalId** *(string) --*

      The external ID.

    - **UserDataShared** *(boolean) --*

      If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
      it publishes to Amazon Pinpoint analytics.
    """


_ClientDescribeUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[str],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[str],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientDescribeUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": str,
    },
    total=False,
)


class ClientDescribeUserPoolClientResponseUserPoolClientTypeDef(
    _ClientDescribeUserPoolClientResponseUserPoolClientTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolClientResponse` `UserPoolClient`

    The user pool client from a server response to describe the user pool client.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool client.

    - **ClientName** *(string) --*

      The client name from the user pool request of the client type.

    - **ClientId** *(string) --*

      The ID of the client associated with the user pool.

    - **ClientSecret** *(string) --*

      The client secret from the user pool request of the client type.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool client was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool client was created.

    - **RefreshTokenValidity** *(integer) --*

      The time limit, in days, after which the refresh token is no longer valid and cannot be
      used.

    - **ReadAttributes** *(list) --*

      The Read-only attributes.

      - *(string) --*

    - **WriteAttributes** *(list) --*

      The writeable attributes.

      - *(string) --*

    - **ExplicitAuthFlows** *(list) --*

      The authentication flows that are supported by the user pool clients. Flow names without
      the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
      that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
      prefix.

      Valid values include:

      * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
      ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
      With this authentication flow, Cognito receives the password in the request instead of
      using the SRP (Secure Remote Password protocol) protocol to verify passwords.

      * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

      * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
      Cognito receives the password in the request instead of using the SRP protocol to verify
      passwords.

      * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

      * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

      - *(string) --*

    - **SupportedIdentityProviders** *(list) --*

      A list of provider names for the identity providers that are supported on this client.

      - *(string) --*

    - **CallbackURLs** *(list) --*

      A list of allowed redirect (callback) URLs for the identity providers.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

      - *(string) --*

    - **LogoutURLs** *(list) --*

      A list of allowed logout URLs for the identity providers.

      - *(string) --*

    - **DefaultRedirectURI** *(string) --*

      The default redirect URI. Must be in the ``CallbackURLs`` list.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

    - **AllowedOAuthFlows** *(list) --*

      Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
      response. This code can be exchanged for access tokens with the token endpoint.

      Set to ``token`` to specify that the client should get the access token (and, optionally,
      ID token, based on scopes) directly.

      - *(string) --*

    - **AllowedOAuthScopes** *(list) --*

      A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
      ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
      created in Resource Servers are also supported.

      - *(string) --*

    - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

      Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
      Cognito user pools.

    - **AnalyticsConfiguration** *(dict) --*

      The Amazon Pinpoint analytics configuration for the user pool client.

      - **ApplicationId** *(string) --*

        The application ID for an Amazon Pinpoint application.

      - **RoleArn** *(string) --*

        The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
        Pinpoint analytics.

      - **ExternalId** *(string) --*

        The external ID.

      - **UserDataShared** *(boolean) --*

        If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
        it publishes to Amazon Pinpoint analytics.

    - **PreventUserExistenceErrors** *(string) --*

      Use this setting to choose which errors and responses are returned by Cognito APIs during
      authentication, account confirmation, and password recovery when the user does not exist in
      the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
      an error indicating either the username or password was incorrect, and account confirmation
      and password recovery return a response indicating a code was sent to a simulated
      destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
      exception if the user does not exist in the user pool.

      Valid values include:

      * ``ENABLED`` - This prevents user existence-related errors.

      * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
      errors are not prevented.

      This setting affects the behavior of following APIs:

      *  AdminInitiateAuth

      *  AdminRespondToAuthChallenge

      *  InitiateAuth

      *  RespondToAuthChallenge

      *  ForgotPassword

      *  ConfirmForgotPassword

      *  ConfirmSignUp

      *  ResendConfirmationCode

      .. note::

        After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
        ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientDescribeUserPoolClientResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientDescribeUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientDescribeUserPoolClientResponseTypeDef(
    _ClientDescribeUserPoolClientResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolClient` `Response`

    Represents the response from the server from a request to describe the user pool client.

    - **UserPoolClient** *(dict) --*

      The user pool client from a server response to describe the user pool client.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.

      - **ClientName** *(string) --*

        The client name from the user pool request of the client type.

      - **ClientId** *(string) --*

        The ID of the client associated with the user pool.

      - **ClientSecret** *(string) --*

        The client secret from the user pool request of the client type.

      - **LastModifiedDate** *(datetime) --*

        The date the user pool client was last modified.

      - **CreationDate** *(datetime) --*

        The date the user pool client was created.

      - **RefreshTokenValidity** *(integer) --*

        The time limit, in days, after which the refresh token is no longer valid and cannot be
        used.

      - **ReadAttributes** *(list) --*

        The Read-only attributes.

        - *(string) --*

      - **WriteAttributes** *(list) --*

        The writeable attributes.

        - *(string) --*

      - **ExplicitAuthFlows** *(list) --*

        The authentication flows that are supported by the user pool clients. Flow names without
        the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
        that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
        prefix.

        Valid values include:

        * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
        ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
        With this authentication flow, Cognito receives the password in the request instead of
        using the SRP (Secure Remote Password protocol) protocol to verify passwords.

        * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

        * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
        Cognito receives the password in the request instead of using the SRP protocol to verify
        passwords.

        * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

        * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

        - *(string) --*

      - **SupportedIdentityProviders** *(list) --*

        A list of provider names for the identity providers that are supported on this client.

        - *(string) --*

      - **CallbackURLs** *(list) --*

        A list of allowed redirect (callback) URLs for the identity providers.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

        - *(string) --*

      - **LogoutURLs** *(list) --*

        A list of allowed logout URLs for the identity providers.

        - *(string) --*

      - **DefaultRedirectURI** *(string) --*

        The default redirect URI. Must be in the ``CallbackURLs`` list.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

      - **AllowedOAuthFlows** *(list) --*

        Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
        response. This code can be exchanged for access tokens with the token endpoint.

        Set to ``token`` to specify that the client should get the access token (and, optionally,
        ID token, based on scopes) directly.

        - *(string) --*

      - **AllowedOAuthScopes** *(list) --*

        A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
        ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
        created in Resource Servers are also supported.

        - *(string) --*

      - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

        Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
        Cognito user pools.

      - **AnalyticsConfiguration** *(dict) --*

        The Amazon Pinpoint analytics configuration for the user pool client.

        - **ApplicationId** *(string) --*

          The application ID for an Amazon Pinpoint application.

        - **RoleArn** *(string) --*

          The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
          Pinpoint analytics.

        - **ExternalId** *(string) --*

          The external ID.

        - **UserDataShared** *(boolean) --*

          If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
          it publishes to Amazon Pinpoint analytics.

      - **PreventUserExistenceErrors** *(string) --*

        Use this setting to choose which errors and responses are returned by Cognito APIs during
        authentication, account confirmation, and password recovery when the user does not exist in
        the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
        an error indicating either the username or password was incorrect, and account confirmation
        and password recovery return a response indicating a code was sent to a simulated
        destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
        exception if the user does not exist in the user pool.

        Valid values include:

        * ``ENABLED`` - This prevents user existence-related errors.

        * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
        errors are not prevented.

        This setting affects the behavior of following APIs:

        *  AdminInitiateAuth

        *  AdminRespondToAuthChallenge

        *  InitiateAuth

        *  RespondToAuthChallenge

        *  ForgotPassword

        *  ConfirmForgotPassword

        *  ConfirmSignUp

        *  ResendConfirmationCode

        .. note::

          After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
          ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef",
    {"CertificateArn": str},
    total=False,
)


class ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef(
    _ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolDomainResponseDomainDescription` `CustomDomainConfig`

    The configuration for a custom domain that hosts the sign-up and sign-in webpages for your
    application.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use
      this certificate for the subdomain of your custom domain.
    """


_ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": str,
        "CustomDomainConfig": ClientDescribeUserPoolDomainResponseDomainDescriptionCustomDomainConfigTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef(
    _ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolDomainResponse` `DomainDescription`

    A domain description object containing information about the domain.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **AWSAccountId** *(string) --*

      The AWS account ID for the user pool owner.

    - **Domain** *(string) --*

      The domain string.

    - **S3Bucket** *(string) --*

      The S3 bucket where the static files for this domain are stored.

    - **CloudFrontDistribution** *(string) --*

      The ARN of the CloudFront distribution.

    - **Version** *(string) --*

      The app version.

    - **Status** *(string) --*

      The domain status.

    - **CustomDomainConfig** *(dict) --*

      The configuration for a custom domain that hosts the sign-up and sign-in webpages for your
      application.

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use
        this certificate for the subdomain of your custom domain.
    """


_ClientDescribeUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolDomainResponseTypeDef",
    {"DomainDescription": ClientDescribeUserPoolDomainResponseDomainDescriptionTypeDef},
    total=False,
)


class ClientDescribeUserPoolDomainResponseTypeDef(
    _ClientDescribeUserPoolDomainResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolDomain` `Response`

    - **DomainDescription** *(dict) --*

      A domain description object containing information about the domain.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **AWSAccountId** *(string) --*

        The AWS account ID for the user pool owner.

      - **Domain** *(string) --*

        The domain string.

      - **S3Bucket** *(string) --*

        The S3 bucket where the static files for this domain are stored.

      - **CloudFrontDistribution** *(string) --*

        The ARN of the CloudFront distribution.

      - **Version** *(string) --*

        The app version.

      - **Status** *(string) --*

        The domain status.

      - **CustomDomainConfig** *(dict) --*

        The configuration for a custom domain that hosts the sign-up and sign-in webpages for your
        application.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use
          this certificate for the subdomain of your custom domain.
    """


_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfig` `InviteMessageTemplate`

    The message template to be used for the welcome message to new users.

    See also `Customizing User Invitation Messages
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
    .

    - **SMSMessage** *(string) --*

      The message template for SMS messages.

    - **EmailMessage** *(string) --*

      The message template for email messages.

    - **EmailSubject** *(string) --*

      The subject line for email messages.
    """


_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef(
    _ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `AdminCreateUserConfig`

    The configuration for ``AdminCreateUser`` requests.

    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to
      ``False`` if users can sign themselves up via an app.

    - **UnusedAccountValidityDays** *(integer) --*

      The user account expiration limit, in days, after which the account is no longer usable.
      To reset the account after that time limit, you must call ``AdminCreateUser`` again,
      specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
      parameter is 7.

      .. note::

        If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
        value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
        pool.

    - **InviteMessageTemplate** *(dict) --*

      The message template to be used for the welcome message to new users.

      See also `Customizing User Invitation Messages
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
      .

      - **SMSMessage** *(string) --*

        The message template for SMS messages.

      - **EmailMessage** *(string) --*

        The message template for email messages.

      - **EmailSubject** *(string) --*

        The subject line for email messages.
    """


_ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `DeviceConfiguration`

    The device configuration.

    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new
      device.

    - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

      If true, a device is only remembered on user prompt.
    """


_ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": str,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `EmailConfiguration`

    The email configuration.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
      address is used in one of the following ways, depending on the value that you specify for
      the ``EmailSendingAccount`` parameter:

      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
      FROM address when it emails your users by using its built-in email account.

      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
      calling Amazon SES on your behalf.

    - **ReplyToEmailAddress** *(string) --*

      The destination to which the receiver of the email should reply to.

    - **EmailSendingAccount** *(string) --*

      Specifies whether Amazon Cognito emails your users by using its built-in email
      functionality or your Amazon SES email configuration. Specify one of the following values:

        COGNITO_DEFAULT

      When Amazon Cognito emails your users, it uses its built-in email functionality. When you
      use the default option, Amazon Cognito allows only a limited number of emails each day
      for your user pool. For typical production environments, the default email limit is below
      the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
      use your Amazon SES email configuration.

      To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
      Cognito Developer Guide* .

      The default FROM address is no-reply@verificationemail.com. To customize the FROM
      address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
      parameter.

        DEVELOPER

      When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
      Cognito calls Amazon SES on your behalf to send email from your verified email address.
      When you use this option, the email delivery limits are the same limits that apply to
      your Amazon SES verified email address in your AWS account.

      If you use this option, you must provide the ARN of an Amazon SES verified email address
      for the ``SourceArn`` parameter.

      Before Amazon Cognito can email your users, it requires additional permissions to call
      Amazon SES on your behalf. When you update your user pool with this option, Amazon
      Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
      account. This role contains the permissions that allow Amazon Cognito to access Amazon
      SES and send email messages with your address. For more information about the
      service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
      Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
      in the *Amazon Cognito Developer Guide* .

    - **From** *(string) --*

      Identifies either the sender’s email address or the sender’s name with their email
      address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
      This address will appear before the body of the email.

    - **ConfigurationSet** *(string) --*

      The set of configuration rules that can be applied to emails sent using Amazon SES. A
      configuration set is applied to an email by including a reference to the configuration
      set in the headers of the email. Once applied, all of the rules in that configuration set
      are applied to the email. Configuration sets can be used to apply the following types of
      rules to emails:

      * Event publishing – Amazon SES can track the number of send, delivery, open, click,
      bounce, and complaint events for each email sent. Use event publishing to send
      information about these events to other AWS services such as SNS and CloudWatch.

      * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
      create groups of IP addresses, called dedicated IP pools. You can then associate the
      dedicated IP pools with configuration sets.
    """


_ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef(
    _ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `LambdaConfig`

    The AWS Lambda triggers associated with the user pool.

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPoolPolicies` `PasswordPolicy`

    The password policy.

    - **MinimumLength** *(integer) --*

      The minimum length of the password policy that you have set. Cannot be less than 6.

    - **RequireUppercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one uppercase letter in their password.

    - **RequireLowercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one lowercase letter in their password.

    - **RequireNumbers** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one number in their password.

    - **RequireSymbols** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to
      use at least one symbol in their password.

    - **TemporaryPasswordValidityDays** *(integer) --*

      In the password policy you have set, refers to the number of days a temporary password
      is valid. If the user does not sign-in during this time, their password will need to be
      reset by an administrator.

      .. note::

        When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
        able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef",
    {
        "PasswordPolicy": ClientDescribeUserPoolResponseUserPoolPoliciesPasswordPolicyTypeDef
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef(
    _ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `Policies`

    The policies associated with the user pool.

    - **PasswordPolicy** *(dict) --*

      The password policy.

      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.

      - **RequireUppercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one uppercase letter in their password.

      - **RequireLowercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one lowercase letter in their password.

      - **RequireNumbers** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one number in their password.

      - **RequireSymbols** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to
        use at least one symbol in their password.

      - **TemporaryPasswordValidityDays** *(integer) --*

        In the password policy you have set, refers to the number of days a temporary password
        is valid. If the user does not sign-in during this time, their password will need to be
        reset by an administrator.

        .. note::

          When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
          able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef",
    {"MinValue": str, "MaxValue": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPoolSchemaAttributes` `NumberAttributeConstraints`

    Specifies the constraints for an attribute of the number type.

    - **MinValue** *(string) --*

      The minimum value of an attribute that is of the number data type.

    - **MaxValue** *(string) --*

      The maximum value of an attribute that is of the number data type.
    """


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef",
    {"MinLength": str, "MaxLength": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPoolSchemaAttributes` `StringAttributeConstraints`

    Specifies the constraints for an attribute of the string type.

    - **MinLength** *(string) --*

      The minimum length.

    - **MaxLength** *(string) --*

      The maximum length.
    """


_ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef",
    {
        "Name": str,
        "AttributeDataType": str,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesNumberAttributeConstraintsTypeDef,
        "StringAttributeConstraints": ClientDescribeUserPoolResponseUserPoolSchemaAttributesStringAttributeConstraintsTypeDef,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `SchemaAttributes`

    Contains information about the schema attribute.

    - **Name** *(string) --*

      A schema attribute of the name type.

    - **AttributeDataType** *(string) --*

      The attribute data type.

    - **DeveloperOnlyAttribute** *(boolean) --*

      Specifies whether the attribute type is developer only.

    - **Mutable** *(boolean) --*

      Specifies whether the value of the attribute can be changed.

      For any user pool attribute that's mapped to an identity provider attribute, you must
      set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
      sign in to your application through an identity provider. If an attribute is immutable,
      Amazon Cognito throws an error when it attempts to update the attribute. For more
      information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
      .

    - **Required** *(boolean) --*

      Specifies whether a user pool attribute is required. If the attribute is required and
      the user does not provide a value, registration or sign-in will fail.

    - **NumberAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the number type.

      - **MinValue** *(string) --*

        The minimum value of an attribute that is of the number data type.

      - **MaxValue** *(string) --*

        The maximum value of an attribute that is of the number data type.

    - **StringAttributeConstraints** *(dict) --*

      Specifies the constraints for an attribute of the string type.

      - **MinLength** *(string) --*

        The minimum length.

      - **MaxLength** *(string) --*

        The maximum length.
    """


_ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef(
    _ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
      This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
      messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role
      which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
      an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
      IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
      you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
      a role with the required permissions and a trust policy that demonstrates use of the
      ``ExternalId`` .
    """


_ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef",
    {"AdvancedSecurityMode": str},
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef(
    _ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `UserPoolAddOns`

    The user pool add-ons.

    - **AdvancedSecurityMode** *(string) --*

      The advanced security mode.
    """


_ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef(
    _ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponseUserPool` `VerificationMessageTemplate`

    The template for verification messages.

    - **SmsMessage** *(string) --*

      The SMS message template.

    - **EmailMessage** *(string) --*

      The email message template.

    - **EmailSubject** *(string) --*

      The subject line for the email message template.

    - **EmailMessageByLink** *(string) --*

      The email message template for sending a confirmation link to the user.

    - **EmailSubjectByLink** *(string) --*

      The subject line for the email message template for sending a confirmation link to the
      user.

    - **DefaultEmailOption** *(string) --*

      The default email option.
    """


_ClientDescribeUserPoolResponseUserPoolTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseUserPoolTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": ClientDescribeUserPoolResponseUserPoolPoliciesTypeDef,
        "LambdaConfig": ClientDescribeUserPoolResponseUserPoolLambdaConfigTypeDef,
        "Status": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List[
            ClientDescribeUserPoolResponseUserPoolSchemaAttributesTypeDef
        ],
        "AutoVerifiedAttributes": List[str],
        "AliasAttributes": List[str],
        "UsernameAttributes": List[str],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": ClientDescribeUserPoolResponseUserPoolVerificationMessageTemplateTypeDef,
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": str,
        "DeviceConfiguration": ClientDescribeUserPoolResponseUserPoolDeviceConfigurationTypeDef,
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": ClientDescribeUserPoolResponseUserPoolEmailConfigurationTypeDef,
        "SmsConfiguration": ClientDescribeUserPoolResponseUserPoolSmsConfigurationTypeDef,
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": ClientDescribeUserPoolResponseUserPoolAdminCreateUserConfigTypeDef,
        "UserPoolAddOns": ClientDescribeUserPoolResponseUserPoolUserPoolAddOnsTypeDef,
        "Arn": str,
    },
    total=False,
)


class ClientDescribeUserPoolResponseUserPoolTypeDef(
    _ClientDescribeUserPoolResponseUserPoolTypeDef
):
    """
    Type definition for `ClientDescribeUserPoolResponse` `UserPool`

    The container of metadata returned by the server to describe the pool.

    - **Id** *(string) --*

      The ID of the user pool.

    - **Name** *(string) --*

      The name of the user pool.

    - **Policies** *(dict) --*

      The policies associated with the user pool.

      - **PasswordPolicy** *(dict) --*

        The password policy.

        - **MinimumLength** *(integer) --*

          The minimum length of the password policy that you have set. Cannot be less than 6.

        - **RequireUppercase** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one uppercase letter in their password.

        - **RequireLowercase** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one lowercase letter in their password.

        - **RequireNumbers** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one number in their password.

        - **RequireSymbols** *(boolean) --*

          In the password policy that you have set, refers to whether you have required users to
          use at least one symbol in their password.

        - **TemporaryPasswordValidityDays** *(integer) --*

          In the password policy you have set, refers to the number of days a temporary password
          is valid. If the user does not sign-in during this time, their password will need to be
          reset by an administrator.

          .. note::

            When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
            able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.

    - **LambdaConfig** *(dict) --*

      The AWS Lambda triggers associated with the user pool.

      - **PreSignUp** *(string) --*

        A pre-registration AWS Lambda trigger.

      - **CustomMessage** *(string) --*

        A custom Message AWS Lambda trigger.

      - **PostConfirmation** *(string) --*

        A post-confirmation AWS Lambda trigger.

      - **PreAuthentication** *(string) --*

        A pre-authentication AWS Lambda trigger.

      - **PostAuthentication** *(string) --*

        A post-authentication AWS Lambda trigger.

      - **DefineAuthChallenge** *(string) --*

        Defines the authentication challenge.

      - **CreateAuthChallenge** *(string) --*

        Creates an authentication challenge.

      - **VerifyAuthChallengeResponse** *(string) --*

        Verifies the authentication challenge response.

      - **PreTokenGeneration** *(string) --*

        A Lambda trigger that is invoked before token generation.

      - **UserMigration** *(string) --*

        The user migration Lambda config type.

    - **Status** *(string) --*

      The status of a user pool.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool was created.

    - **SchemaAttributes** *(list) --*

      A container with the schema attributes of a user pool.

      - *(dict) --*

        Contains information about the schema attribute.

        - **Name** *(string) --*

          A schema attribute of the name type.

        - **AttributeDataType** *(string) --*

          The attribute data type.

        - **DeveloperOnlyAttribute** *(boolean) --*

          Specifies whether the attribute type is developer only.

        - **Mutable** *(boolean) --*

          Specifies whether the value of the attribute can be changed.

          For any user pool attribute that's mapped to an identity provider attribute, you must
          set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
          sign in to your application through an identity provider. If an attribute is immutable,
          Amazon Cognito throws an error when it attempts to update the attribute. For more
          information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
          <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
          .

        - **Required** *(boolean) --*

          Specifies whether a user pool attribute is required. If the attribute is required and
          the user does not provide a value, registration or sign-in will fail.

        - **NumberAttributeConstraints** *(dict) --*

          Specifies the constraints for an attribute of the number type.

          - **MinValue** *(string) --*

            The minimum value of an attribute that is of the number data type.

          - **MaxValue** *(string) --*

            The maximum value of an attribute that is of the number data type.

        - **StringAttributeConstraints** *(dict) --*

          Specifies the constraints for an attribute of the string type.

          - **MinLength** *(string) --*

            The minimum length.

          - **MaxLength** *(string) --*

            The maximum length.

    - **AutoVerifiedAttributes** *(list) --*

      Specifies the attributes that are auto-verified in a user pool.

      - *(string) --*

    - **AliasAttributes** *(list) --*

      Specifies the attributes that are aliased in a user pool.

      - *(string) --*

    - **UsernameAttributes** *(list) --*

      Specifies whether email addresses or phone numbers can be specified as usernames when a
      user signs up.

      - *(string) --*

    - **SmsVerificationMessage** *(string) --*

      The contents of the SMS verification message.

    - **EmailVerificationMessage** *(string) --*

      The contents of the email verification message.

    - **EmailVerificationSubject** *(string) --*

      The subject of the email verification message.

    - **VerificationMessageTemplate** *(dict) --*

      The template for verification messages.

      - **SmsMessage** *(string) --*

        The SMS message template.

      - **EmailMessage** *(string) --*

        The email message template.

      - **EmailSubject** *(string) --*

        The subject line for the email message template.

      - **EmailMessageByLink** *(string) --*

        The email message template for sending a confirmation link to the user.

      - **EmailSubjectByLink** *(string) --*

        The subject line for the email message template for sending a confirmation link to the
        user.

      - **DefaultEmailOption** *(string) --*

        The default email option.

    - **SmsAuthenticationMessage** *(string) --*

      The contents of the SMS authentication message.

    - **MfaConfiguration** *(string) --*

      Can be one of the following values:

      * ``OFF`` - MFA tokens are not required and cannot be specified during user registration.

      * ``ON`` - MFA tokens are required for all user registrations. You can only specify
      required when you are initially creating a user pool.

      * ``OPTIONAL`` - Users have the option when registering to create an MFA token.

    - **DeviceConfiguration** *(dict) --*

      The device configuration.

      - **ChallengeRequiredOnNewDevice** *(boolean) --*

        Indicates whether a challenge is required on a new device. Only applicable to a new
        device.

      - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

        If true, a device is only remembered on user prompt.

    - **EstimatedNumberOfUsers** *(integer) --*

      A number estimating the size of the user pool.

    - **EmailConfiguration** *(dict) --*

      The email configuration.

      - **SourceArn** *(string) --*

        The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
        address is used in one of the following ways, depending on the value that you specify for
        the ``EmailSendingAccount`` parameter:

        * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
        FROM address when it emails your users by using its built-in email account.

        * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
        calling Amazon SES on your behalf.

      - **ReplyToEmailAddress** *(string) --*

        The destination to which the receiver of the email should reply to.

      - **EmailSendingAccount** *(string) --*

        Specifies whether Amazon Cognito emails your users by using its built-in email
        functionality or your Amazon SES email configuration. Specify one of the following values:

          COGNITO_DEFAULT

        When Amazon Cognito emails your users, it uses its built-in email functionality. When you
        use the default option, Amazon Cognito allows only a limited number of emails each day
        for your user pool. For typical production environments, the default email limit is below
        the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
        use your Amazon SES email configuration.

        To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
        <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
        Cognito Developer Guide* .

        The default FROM address is no-reply@verificationemail.com. To customize the FROM
        address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
        parameter.

          DEVELOPER

        When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
        Cognito calls Amazon SES on your behalf to send email from your verified email address.
        When you use this option, the email delivery limits are the same limits that apply to
        your Amazon SES verified email address in your AWS account.

        If you use this option, you must provide the ARN of an Amazon SES verified email address
        for the ``SourceArn`` parameter.

        Before Amazon Cognito can email your users, it requires additional permissions to call
        Amazon SES on your behalf. When you update your user pool with this option, Amazon
        Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
        account. This role contains the permissions that allow Amazon Cognito to access Amazon
        SES and send email messages with your address. For more information about the
        service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
        Amazon Cognito
        <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
        in the *Amazon Cognito Developer Guide* .

      - **From** *(string) --*

        Identifies either the sender’s email address or the sender’s name with their email
        address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
        This address will appear before the body of the email.

      - **ConfigurationSet** *(string) --*

        The set of configuration rules that can be applied to emails sent using Amazon SES. A
        configuration set is applied to an email by including a reference to the configuration
        set in the headers of the email. Once applied, all of the rules in that configuration set
        are applied to the email. Configuration sets can be used to apply the following types of
        rules to emails:

        * Event publishing – Amazon SES can track the number of send, delivery, open, click,
        bounce, and complaint events for each email sent. Use event publishing to send
        information about these events to other AWS services such as SNS and CloudWatch.

        * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
        create groups of IP addresses, called dedicated IP pools. You can then associate the
        dedicated IP pools with configuration sets.

    - **SmsConfiguration** *(dict) --*

      The SMS configuration.

      - **SnsCallerArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
        This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
        messages.

      - **ExternalId** *(string) --*

        The external ID is a value that we recommend you use to add security to your IAM role
        which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
        an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
        IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
        you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
        a role with the required permissions and a trust policy that demonstrates use of the
        ``ExternalId`` .

    - **UserPoolTags** *(dict) --*

      The tags that are assigned to the user pool. A tag is a label that you can apply to user
      pools to categorize and manage them in different ways, such as by purpose, owner,
      environment, or other criteria.

      - *(string) --*

        - *(string) --*

    - **SmsConfigurationFailure** *(string) --*

      The reason why the SMS configuration cannot send the messages to your users.

    - **EmailConfigurationFailure** *(string) --*

      The reason why the email configuration cannot send the messages to your users.

    - **Domain** *(string) --*

      Holds the domain prefix if the user pool has a domain associated with it.

    - **CustomDomain** *(string) --*

      A custom domain name that you provide to Amazon Cognito. This parameter applies only if you
      use a custom domain to host the sign-up and sign-in pages for your application. For
      example: ``auth.example.com`` .

      For more information about adding a custom domain to your user pool, see `Using Your Own
      Domain for the Hosted UI
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__
      .

    - **AdminCreateUserConfig** *(dict) --*

      The configuration for ``AdminCreateUser`` requests.

      - **AllowAdminCreateUserOnly** *(boolean) --*

        Set to ``True`` if only the administrator is allowed to create user profiles. Set to
        ``False`` if users can sign themselves up via an app.

      - **UnusedAccountValidityDays** *(integer) --*

        The user account expiration limit, in days, after which the account is no longer usable.
        To reset the account after that time limit, you must call ``AdminCreateUser`` again,
        specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
        parameter is 7.

        .. note::

          If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
          value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
          pool.

      - **InviteMessageTemplate** *(dict) --*

        The message template to be used for the welcome message to new users.

        See also `Customizing User Invitation Messages
        <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
        .

        - **SMSMessage** *(string) --*

          The message template for SMS messages.

        - **EmailMessage** *(string) --*

          The message template for email messages.

        - **EmailSubject** *(string) --*

          The subject line for email messages.

    - **UserPoolAddOns** *(dict) --*

      The user pool add-ons.

      - **AdvancedSecurityMode** *(string) --*

        The advanced security mode.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the user pool.
    """


_ClientDescribeUserPoolResponseTypeDef = TypedDict(
    "_ClientDescribeUserPoolResponseTypeDef",
    {"UserPool": ClientDescribeUserPoolResponseUserPoolTypeDef},
    total=False,
)


class ClientDescribeUserPoolResponseTypeDef(_ClientDescribeUserPoolResponseTypeDef):
    """
    Type definition for `ClientDescribeUserPool` `Response`

    Represents the response to describe the user pool.

    - **UserPool** *(dict) --*

      The container of metadata returned by the server to describe the pool.

      - **Id** *(string) --*

        The ID of the user pool.

      - **Name** *(string) --*

        The name of the user pool.

      - **Policies** *(dict) --*

        The policies associated with the user pool.

        - **PasswordPolicy** *(dict) --*

          The password policy.

          - **MinimumLength** *(integer) --*

            The minimum length of the password policy that you have set. Cannot be less than 6.

          - **RequireUppercase** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one uppercase letter in their password.

          - **RequireLowercase** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one lowercase letter in their password.

          - **RequireNumbers** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one number in their password.

          - **RequireSymbols** *(boolean) --*

            In the password policy that you have set, refers to whether you have required users to
            use at least one symbol in their password.

          - **TemporaryPasswordValidityDays** *(integer) --*

            In the password policy you have set, refers to the number of days a temporary password
            is valid. If the user does not sign-in during this time, their password will need to be
            reset by an administrator.

            .. note::

              When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be
              able to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.

      - **LambdaConfig** *(dict) --*

        The AWS Lambda triggers associated with the user pool.

        - **PreSignUp** *(string) --*

          A pre-registration AWS Lambda trigger.

        - **CustomMessage** *(string) --*

          A custom Message AWS Lambda trigger.

        - **PostConfirmation** *(string) --*

          A post-confirmation AWS Lambda trigger.

        - **PreAuthentication** *(string) --*

          A pre-authentication AWS Lambda trigger.

        - **PostAuthentication** *(string) --*

          A post-authentication AWS Lambda trigger.

        - **DefineAuthChallenge** *(string) --*

          Defines the authentication challenge.

        - **CreateAuthChallenge** *(string) --*

          Creates an authentication challenge.

        - **VerifyAuthChallengeResponse** *(string) --*

          Verifies the authentication challenge response.

        - **PreTokenGeneration** *(string) --*

          A Lambda trigger that is invoked before token generation.

        - **UserMigration** *(string) --*

          The user migration Lambda config type.

      - **Status** *(string) --*

        The status of a user pool.

      - **LastModifiedDate** *(datetime) --*

        The date the user pool was last modified.

      - **CreationDate** *(datetime) --*

        The date the user pool was created.

      - **SchemaAttributes** *(list) --*

        A container with the schema attributes of a user pool.

        - *(dict) --*

          Contains information about the schema attribute.

          - **Name** *(string) --*

            A schema attribute of the name type.

          - **AttributeDataType** *(string) --*

            The attribute data type.

          - **DeveloperOnlyAttribute** *(boolean) --*

            Specifies whether the attribute type is developer only.

          - **Mutable** *(boolean) --*

            Specifies whether the value of the attribute can be changed.

            For any user pool attribute that's mapped to an identity provider attribute, you must
            set this parameter to ``true`` . Amazon Cognito updates mapped attributes when users
            sign in to your application through an identity provider. If an attribute is immutable,
            Amazon Cognito throws an error when it attempts to update the attribute. For more
            information, see `Specifying Identity Provider Attribute Mappings for Your User Pool
            <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html>`__
            .

          - **Required** *(boolean) --*

            Specifies whether a user pool attribute is required. If the attribute is required and
            the user does not provide a value, registration or sign-in will fail.

          - **NumberAttributeConstraints** *(dict) --*

            Specifies the constraints for an attribute of the number type.

            - **MinValue** *(string) --*

              The minimum value of an attribute that is of the number data type.

            - **MaxValue** *(string) --*

              The maximum value of an attribute that is of the number data type.

          - **StringAttributeConstraints** *(dict) --*

            Specifies the constraints for an attribute of the string type.

            - **MinLength** *(string) --*

              The minimum length.

            - **MaxLength** *(string) --*

              The maximum length.

      - **AutoVerifiedAttributes** *(list) --*

        Specifies the attributes that are auto-verified in a user pool.

        - *(string) --*

      - **AliasAttributes** *(list) --*

        Specifies the attributes that are aliased in a user pool.

        - *(string) --*

      - **UsernameAttributes** *(list) --*

        Specifies whether email addresses or phone numbers can be specified as usernames when a
        user signs up.

        - *(string) --*

      - **SmsVerificationMessage** *(string) --*

        The contents of the SMS verification message.

      - **EmailVerificationMessage** *(string) --*

        The contents of the email verification message.

      - **EmailVerificationSubject** *(string) --*

        The subject of the email verification message.

      - **VerificationMessageTemplate** *(dict) --*

        The template for verification messages.

        - **SmsMessage** *(string) --*

          The SMS message template.

        - **EmailMessage** *(string) --*

          The email message template.

        - **EmailSubject** *(string) --*

          The subject line for the email message template.

        - **EmailMessageByLink** *(string) --*

          The email message template for sending a confirmation link to the user.

        - **EmailSubjectByLink** *(string) --*

          The subject line for the email message template for sending a confirmation link to the
          user.

        - **DefaultEmailOption** *(string) --*

          The default email option.

      - **SmsAuthenticationMessage** *(string) --*

        The contents of the SMS authentication message.

      - **MfaConfiguration** *(string) --*

        Can be one of the following values:

        * ``OFF`` - MFA tokens are not required and cannot be specified during user registration.

        * ``ON`` - MFA tokens are required for all user registrations. You can only specify
        required when you are initially creating a user pool.

        * ``OPTIONAL`` - Users have the option when registering to create an MFA token.

      - **DeviceConfiguration** *(dict) --*

        The device configuration.

        - **ChallengeRequiredOnNewDevice** *(boolean) --*

          Indicates whether a challenge is required on a new device. Only applicable to a new
          device.

        - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

          If true, a device is only remembered on user prompt.

      - **EstimatedNumberOfUsers** *(integer) --*

        A number estimating the size of the user pool.

      - **EmailConfiguration** *(dict) --*

        The email configuration.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email
          address is used in one of the following ways, depending on the value that you specify for
          the ``EmailSendingAccount`` parameter:

          * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom
          FROM address when it emails your users by using its built-in email account.

          * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by
          calling Amazon SES on your behalf.

        - **ReplyToEmailAddress** *(string) --*

          The destination to which the receiver of the email should reply to.

        - **EmailSendingAccount** *(string) --*

          Specifies whether Amazon Cognito emails your users by using its built-in email
          functionality or your Amazon SES email configuration. Specify one of the following values:

            COGNITO_DEFAULT

          When Amazon Cognito emails your users, it uses its built-in email functionality. When you
          use the default option, Amazon Cognito allows only a limited number of emails each day
          for your user pool. For typical production environments, the default email limit is below
          the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to
          use your Amazon SES email configuration.

          To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
          <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
          Cognito Developer Guide* .

          The default FROM address is no-reply@verificationemail.com. To customize the FROM
          address, provide the ARN of an Amazon SES verified email address for the ``SourceArn``
          parameter.

            DEVELOPER

          When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon
          Cognito calls Amazon SES on your behalf to send email from your verified email address.
          When you use this option, the email delivery limits are the same limits that apply to
          your Amazon SES verified email address in your AWS account.

          If you use this option, you must provide the ARN of an Amazon SES verified email address
          for the ``SourceArn`` parameter.

          Before Amazon Cognito can email your users, it requires additional permissions to call
          Amazon SES on your behalf. When you update your user pool with this option, Amazon
          Cognito creates a *service-linked role* , which is a type of IAM role, in your AWS
          account. This role contains the permissions that allow Amazon Cognito to access Amazon
          SES and send email messages with your address. For more information about the
          service-linked role that Amazon Cognito creates, see `Using Service-Linked Roles for
          Amazon Cognito
          <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
          in the *Amazon Cognito Developer Guide* .

        - **From** *(string) --*

          Identifies either the sender’s email address or the sender’s name with their email
          address. For example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` .
          This address will appear before the body of the email.

        - **ConfigurationSet** *(string) --*

          The set of configuration rules that can be applied to emails sent using Amazon SES. A
          configuration set is applied to an email by including a reference to the configuration
          set in the headers of the email. Once applied, all of the rules in that configuration set
          are applied to the email. Configuration sets can be used to apply the following types of
          rules to emails:

          * Event publishing – Amazon SES can track the number of send, delivery, open, click,
          bounce, and complaint events for each email sent. Use event publishing to send
          information about these events to other AWS services such as SNS and CloudWatch.

          * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can
          create groups of IP addresses, called dedicated IP pools. You can then associate the
          dedicated IP pools with configuration sets.

      - **SmsConfiguration** *(dict) --*

        The SMS configuration.

        - **SnsCallerArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
          This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
          messages.

        - **ExternalId** *(string) --*

          The external ID is a value that we recommend you use to add security to your IAM role
          which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
          an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
          IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
          you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
          a role with the required permissions and a trust policy that demonstrates use of the
          ``ExternalId`` .

      - **UserPoolTags** *(dict) --*

        The tags that are assigned to the user pool. A tag is a label that you can apply to user
        pools to categorize and manage them in different ways, such as by purpose, owner,
        environment, or other criteria.

        - *(string) --*

          - *(string) --*

      - **SmsConfigurationFailure** *(string) --*

        The reason why the SMS configuration cannot send the messages to your users.

      - **EmailConfigurationFailure** *(string) --*

        The reason why the email configuration cannot send the messages to your users.

      - **Domain** *(string) --*

        Holds the domain prefix if the user pool has a domain associated with it.

      - **CustomDomain** *(string) --*

        A custom domain name that you provide to Amazon Cognito. This parameter applies only if you
        use a custom domain to host the sign-up and sign-in pages for your application. For
        example: ``auth.example.com`` .

        For more information about adding a custom domain to your user pool, see `Using Your Own
        Domain for the Hosted UI
        <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html>`__
        .

      - **AdminCreateUserConfig** *(dict) --*

        The configuration for ``AdminCreateUser`` requests.

        - **AllowAdminCreateUserOnly** *(boolean) --*

          Set to ``True`` if only the administrator is allowed to create user profiles. Set to
          ``False`` if users can sign themselves up via an app.

        - **UnusedAccountValidityDays** *(integer) --*

          The user account expiration limit, in days, after which the account is no longer usable.
          To reset the account after that time limit, you must call ``AdminCreateUser`` again,
          specifying ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this
          parameter is 7.

          .. note::

            If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that
            value will be used and ``UnusedAccountValidityDays`` will be deprecated for that user
            pool.

        - **InviteMessageTemplate** *(dict) --*

          The message template to be used for the welcome message to new users.

          See also `Customizing User Invitation Messages
          <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
          .

          - **SMSMessage** *(string) --*

            The message template for SMS messages.

          - **EmailMessage** *(string) --*

            The message template for email messages.

          - **EmailSubject** *(string) --*

            The subject line for email messages.

      - **UserPoolAddOns** *(dict) --*

        The user pool add-ons.

        - **AdvancedSecurityMode** *(string) --*

          The advanced security mode.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) for the user pool.
    """


_ClientForgotPasswordAnalyticsMetadataTypeDef = TypedDict(
    "_ClientForgotPasswordAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientForgotPasswordAnalyticsMetadataTypeDef(
    _ClientForgotPasswordAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientForgotPassword` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``ForgotPassword`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef(
    _ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef
):
    """
    Type definition for `ClientForgotPasswordResponse` `CodeDeliveryDetails`

    The code delivery details returned by the server in response to the request to reset a
    password.

    - **Destination** *(string) --*

      The destination for the code delivery details.

    - **DeliveryMedium** *(string) --*

      The delivery medium (email message or phone number).

    - **AttributeName** *(string) --*

      The attribute name.
    """


_ClientForgotPasswordResponseTypeDef = TypedDict(
    "_ClientForgotPasswordResponseTypeDef",
    {"CodeDeliveryDetails": ClientForgotPasswordResponseCodeDeliveryDetailsTypeDef},
    total=False,
)


class ClientForgotPasswordResponseTypeDef(_ClientForgotPasswordResponseTypeDef):
    """
    Type definition for `ClientForgotPassword` `Response`

    Respresents the response from the server regarding the request to reset a password.

    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to reset a
      password.

      - **Destination** *(string) --*

        The destination for the code delivery details.

      - **DeliveryMedium** *(string) --*

        The delivery medium (email message or phone number).

      - **AttributeName** *(string) --*

        The attribute name.
    """


_ClientForgotPasswordUserContextDataTypeDef = TypedDict(
    "_ClientForgotPasswordUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientForgotPasswordUserContextDataTypeDef(
    _ClientForgotPasswordUserContextDataTypeDef
):
    """
    Type definition for `ClientForgotPassword` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientGetCsvHeaderResponseTypeDef = TypedDict(
    "_ClientGetCsvHeaderResponseTypeDef",
    {"UserPoolId": str, "CSVHeader": List[str]},
    total=False,
)


class ClientGetCsvHeaderResponseTypeDef(_ClientGetCsvHeaderResponseTypeDef):
    """
    Type definition for `ClientGetCsvHeader` `Response`

    Represents the response from the server to the request to get the header information for the
    .csv file for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are to be imported into.

    - **CSVHeader** *(list) --*

      The header information for the .csv file for the user import job.

      - *(string) --*
    """


_ClientGetDeviceResponseDeviceDeviceAttributesTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetDeviceResponseDeviceDeviceAttributesTypeDef(
    _ClientGetDeviceResponseDeviceDeviceAttributesTypeDef
):
    """
    Type definition for `ClientGetDeviceResponseDevice` `DeviceAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientGetDeviceResponseDeviceTypeDef = TypedDict(
    "_ClientGetDeviceResponseDeviceTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[ClientGetDeviceResponseDeviceDeviceAttributesTypeDef],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientGetDeviceResponseDeviceTypeDef(_ClientGetDeviceResponseDeviceTypeDef):
    """
    Type definition for `ClientGetDeviceResponse` `Device`

    The device.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceAttributes** *(list) --*

      The device attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **DeviceCreateDate** *(datetime) --*

      The creation date of the device.

    - **DeviceLastModifiedDate** *(datetime) --*

      The last modified date of the device.

    - **DeviceLastAuthenticatedDate** *(datetime) --*

      The date in which the device was last authenticated.
    """


_ClientGetDeviceResponseTypeDef = TypedDict(
    "_ClientGetDeviceResponseTypeDef",
    {"Device": ClientGetDeviceResponseDeviceTypeDef},
    total=False,
)


class ClientGetDeviceResponseTypeDef(_ClientGetDeviceResponseTypeDef):
    """
    Type definition for `ClientGetDevice` `Response`

    Gets the device response.

    - **Device** *(dict) --*

      The device.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceAttributes** *(list) --*

        The device attributes.

        - *(dict) --*

          Specifies whether the attribute is standard or custom.

          - **Name** *(string) --*

            The name of the attribute.

          - **Value** *(string) --*

            The value of the attribute.

      - **DeviceCreateDate** *(datetime) --*

        The creation date of the device.

      - **DeviceLastModifiedDate** *(datetime) --*

        The last modified date of the device.

      - **DeviceLastAuthenticatedDate** *(datetime) --*

        The date in which the device was last authenticated.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    Type definition for `ClientGetGroupResponse` `Group`

    The group object for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
      group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
      not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {"Group": ClientGetGroupResponseGroupTypeDef},
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    Type definition for `ClientGetGroup` `Response`

    - **Group** *(dict) --*

      The group object for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.

      - **Description** *(string) --*

        A string containing the description of the group.

      - **RoleArn** *(string) --*

        The role ARN for the group.

      - **Precedence** *(integer) --*

        A nonnegative integer value that specifies the precedence of this group relative to the
        other groups that a user can belong to in the user pool. If a user belongs to two or more
        groups, it is the group with the highest precedence whose role ARN will be used in the
        ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
        higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
        or with null ``Precedence`` values.

        Two groups can have the same ``Precedence`` value. If this happens, neither group takes
        precedence over the other. If two groups with the same ``Precedence`` have the same role
        ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
        group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
        not set in users' tokens.

        The default ``Precedence`` value is null.

      - **LastModifiedDate** *(datetime) --*

        The date the group was last modified.

      - **CreationDate** *(datetime) --*

        The date the group was created.
    """


_ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef = TypedDict(
    "_ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": str,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef(
    _ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef
):
    """
    Type definition for `ClientGetIdentityProviderByIdentifierResponse` `IdentityProvider`

    The identity provider object.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **ProviderDetails** *(dict) --*

      The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

      - *(string) --*

        - *(string) --*

    - **AttributeMapping** *(dict) --*

      A mapping of identity provider attributes to standard and custom user pool attributes.

      - *(string) --*

        - *(string) --*

    - **IdpIdentifiers** *(list) --*

      A list of identity provider identifiers.

      - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The date the identity provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the identity provider was created.
    """


_ClientGetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "_ClientGetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": ClientGetIdentityProviderByIdentifierResponseIdentityProviderTypeDef
    },
    total=False,
)


class ClientGetIdentityProviderByIdentifierResponseTypeDef(
    _ClientGetIdentityProviderByIdentifierResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityProviderByIdentifier` `Response`

    - **IdentityProvider** *(dict) --*

      The identity provider object.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ProviderName** *(string) --*

        The identity provider name.

      - **ProviderType** *(string) --*

        The identity provider type.

      - **ProviderDetails** *(dict) --*

        The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

        - *(string) --*

          - *(string) --*

      - **AttributeMapping** *(dict) --*

        A mapping of identity provider attributes to standard and custom user pool attributes.

        - *(string) --*

          - *(string) --*

      - **IdpIdentifiers** *(list) --*

        A list of identity provider identifiers.

        - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The date the identity provider was last modified.

      - **CreationDate** *(datetime) --*

        The date the identity provider was created.
    """


_ClientGetSigningCertificateResponseTypeDef = TypedDict(
    "_ClientGetSigningCertificateResponseTypeDef", {"Certificate": str}, total=False
)


class ClientGetSigningCertificateResponseTypeDef(
    _ClientGetSigningCertificateResponseTypeDef
):
    """
    Type definition for `ClientGetSigningCertificate` `Response`

    Response from Cognito for a signing certificate request.

    - **Certificate** *(string) --*

      The signing certificate.
    """


_ClientGetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "_ClientGetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetUiCustomizationResponseUICustomizationTypeDef(
    _ClientGetUiCustomizationResponseUICustomizationTypeDef
):
    """
    Type definition for `ClientGetUiCustomizationResponse` `UICustomization`

    The UI customization information.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **ClientId** *(string) --*

      The client ID for the client app.

    - **ImageUrl** *(string) --*

      The logo image for the UI customization.

    - **CSS** *(string) --*

      The CSS values in the UI customization.

    - **CSSVersion** *(string) --*

      The CSS version number.

    - **LastModifiedDate** *(datetime) --*

      The last-modified date for the UI customization.

    - **CreationDate** *(datetime) --*

      The creation date for the UI customization.
    """


_ClientGetUiCustomizationResponseTypeDef = TypedDict(
    "_ClientGetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientGetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)


class ClientGetUiCustomizationResponseTypeDef(_ClientGetUiCustomizationResponseTypeDef):
    """
    Type definition for `ClientGetUiCustomization` `Response`

    - **UICustomization** *(dict) --*

      The UI customization information.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.

      - **ClientId** *(string) --*

        The client ID for the client app.

      - **ImageUrl** *(string) --*

        The logo image for the UI customization.

      - **CSS** *(string) --*

        The CSS values in the UI customization.

      - **CSSVersion** *(string) --*

        The CSS version number.

      - **LastModifiedDate** *(datetime) --*

        The last-modified date for the UI customization.

      - **CreationDate** *(datetime) --*

        The creation date for the UI customization.
    """


_ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef(
    _ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef
):
    """
    Type definition for `ClientGetUserAttributeVerificationCodeResponse` `CodeDeliveryDetails`

    The code delivery details returned by the server in response to the request to get the user
    attribute verification code.

    - **Destination** *(string) --*

      The destination for the code delivery details.

    - **DeliveryMedium** *(string) --*

      The delivery medium (email message or phone number).

    - **AttributeName** *(string) --*

      The attribute name.
    """


_ClientGetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "_ClientGetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": ClientGetUserAttributeVerificationCodeResponseCodeDeliveryDetailsTypeDef
    },
    total=False,
)


class ClientGetUserAttributeVerificationCodeResponseTypeDef(
    _ClientGetUserAttributeVerificationCodeResponseTypeDef
):
    """
    Type definition for `ClientGetUserAttributeVerificationCode` `Response`

    The verification code response returned by the server response to get the user attribute
    verification code.

    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to get the user
      attribute verification code.

      - **Destination** *(string) --*

        The destination for the code delivery details.

      - **DeliveryMedium** *(string) --*

        The delivery medium (email message or phone number).

      - **AttributeName** *(string) --*

        The attribute name.
    """


_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef
):
    """
    Type definition for `ClientGetUserPoolMfaConfigResponseSmsMfaConfiguration` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
      This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
      messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role
      which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
      an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
      IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
      you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
      a role with the required permissions and a trust policy that demonstrates use of the
      ``ExternalId`` .
    """


_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef
):
    """
    Type definition for `ClientGetUserPoolMfaConfigResponse` `SmsMfaConfiguration`

    The SMS text message multi-factor (MFA) configuration.

    - **SmsAuthenticationMessage** *(string) --*

      The SMS authentication message that will be sent to users with the code they need to sign
      in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
      code. If the message is not included, and default message will be used.

    - **SmsConfiguration** *(dict) --*

      The SMS configuration.

      - **SnsCallerArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
        This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
        messages.

      - **ExternalId** *(string) --*

        The external ID is a value that we recommend you use to add security to your IAM role
        which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
        an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
        IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
        you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
        a role with the required permissions and a trust policy that demonstrates use of the
        ``ExternalId`` .
    """


_ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef(
    _ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef
):
    """
    Type definition for `ClientGetUserPoolMfaConfigResponse` `SoftwareTokenMfaConfiguration`

    The software token multi-factor (MFA) configuration.

    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientGetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "_ClientGetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientGetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientGetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": str,
    },
    total=False,
)


class ClientGetUserPoolMfaConfigResponseTypeDef(
    _ClientGetUserPoolMfaConfigResponseTypeDef
):
    """
    Type definition for `ClientGetUserPoolMfaConfig` `Response`

    - **SmsMfaConfiguration** *(dict) --*

      The SMS text message multi-factor (MFA) configuration.

      - **SmsAuthenticationMessage** *(string) --*

        The SMS authentication message that will be sent to users with the code they need to sign
        in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
        code. If the message is not included, and default message will be used.

      - **SmsConfiguration** *(dict) --*

        The SMS configuration.

        - **SnsCallerArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
          This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
          messages.

        - **ExternalId** *(string) --*

          The external ID is a value that we recommend you use to add security to your IAM role
          which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
          an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
          IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
          you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
          a role with the required permissions and a trust policy that demonstrates use of the
          ``ExternalId`` .

    - **SoftwareTokenMfaConfiguration** *(dict) --*

      The software token multi-factor (MFA) configuration.

      - **Enabled** *(boolean) --*

        Specifies whether software token MFA is enabled.

    - **MfaConfiguration** *(string) --*

      The multi-factor (MFA) configuration. Valid values include:

      * ``OFF`` MFA will not be used for any users.

      * ``ON`` MFA is required for all users to sign in.

      * ``OPTIONAL`` MFA will be required only for individual users who have an MFA factor enabled.
    """


_ClientGetUserResponseMFAOptionsTypeDef = TypedDict(
    "_ClientGetUserResponseMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientGetUserResponseMFAOptionsTypeDef(_ClientGetUserResponseMFAOptionsTypeDef):
    """
    Type definition for `ClientGetUserResponse` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA configurations.
     You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientGetUserResponseUserAttributesTypeDef = TypedDict(
    "_ClientGetUserResponseUserAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetUserResponseUserAttributesTypeDef(
    _ClientGetUserResponseUserAttributesTypeDef
):
    """
    Type definition for `ClientGetUserResponse` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientGetUserResponseTypeDef = TypedDict(
    "_ClientGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List[ClientGetUserResponseUserAttributesTypeDef],
        "MFAOptions": List[ClientGetUserResponseMFAOptionsTypeDef],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)


class ClientGetUserResponseTypeDef(_ClientGetUserResponseTypeDef):
    """
    Type definition for `ClientGetUser` `Response`

    Represents the response from the server from the request to get information about the user.

    - **Username** *(string) --*

      The user name of the user you wish to retrieve from the get user request.

    - **UserAttributes** *(list) --*

      An array of name-value pairs representing user attributes.

      For custom attributes, you must prepend the ``custom:`` prefix to the attribute name.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **MFAOptions** *(list) --*

       *This response parameter is no longer supported.* It provides information only about SMS MFA
       configurations. It doesn't provide information about TOTP software token MFA configurations.
       To look up information about either type of MFA configuration, use the use the
       GetUserResponse$UserMFASettingList response instead.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA configurations.
         You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .

    - **PreferredMfaSetting** *(string) --*

      The user's preferred MFA setting.

    - **UserMFASettingList** *(list) --*

      The MFA options that are enabled for the user. The possible values in this list are
      ``SMS_MFA`` and ``SOFTWARE_TOKEN_MFA`` .

      - *(string) --*
    """


_ClientInitiateAuthAnalyticsMetadataTypeDef = TypedDict(
    "_ClientInitiateAuthAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientInitiateAuthAnalyticsMetadataTypeDef(
    _ClientInitiateAuthAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientInitiateAuth` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``InitiateAuth`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    """
    Type definition for `ClientInitiateAuthResponseAuthenticationResult` `NewDeviceMetadata`

    The new device metadata from an authentication result.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceGroupKey** *(string) --*

      The device group key.
    """


_ClientInitiateAuthResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientInitiateAuthResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientInitiateAuthResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientInitiateAuthResponseAuthenticationResultTypeDef(
    _ClientInitiateAuthResponseAuthenticationResultTypeDef
):
    """
    Type definition for `ClientInitiateAuthResponse` `AuthenticationResult`

    The result of the authentication response. This is only returned if the caller does not need
    to pass another challenge. If the caller does need to pass another challenge before it gets
    tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

    - **AccessToken** *(string) --*

      The access token.

    - **ExpiresIn** *(integer) --*

      The expiration period of the authentication result in seconds.

    - **TokenType** *(string) --*

      The token type.

    - **RefreshToken** *(string) --*

      The refresh token.

    - **IdToken** *(string) --*

      The ID token.

    - **NewDeviceMetadata** *(dict) --*

      The new device metadata from an authentication result.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceGroupKey** *(string) --*

        The device group key.
    """


_ClientInitiateAuthResponseTypeDef = TypedDict(
    "_ClientInitiateAuthResponseTypeDef",
    {
        "ChallengeName": str,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientInitiateAuthResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientInitiateAuthResponseTypeDef(_ClientInitiateAuthResponseTypeDef):
    """
    Type definition for `ClientInitiateAuth` `Response`

    Initiates the authentication response.

    - **ChallengeName** *(string) --*

      The name of the challenge which you are responding to with this call. This is returned to you
      in the ``AdminInitiateAuth`` response if you need to pass another challenge.

      Valid values include the following. Note that all of these challenges require ``USERNAME``
      and ``SECRET_HASH`` (if applicable) in the parameters.

      * ``SMS_MFA`` : Next challenge is to supply an ``SMS_MFA_CODE`` , delivered via SMS.

      * ``PASSWORD_VERIFIER`` : Next challenge is to supply ``PASSWORD_CLAIM_SIGNATURE`` ,
      ``PASSWORD_CLAIM_SECRET_BLOCK`` , and ``TIMESTAMP`` after the client-side SRP calculations.

      * ``CUSTOM_CHALLENGE`` : This is returned if your custom authentication flow determines that
      the user should pass another challenge before tokens are issued.

      * ``DEVICE_SRP_AUTH`` : If device tracking was enabled on your user pool and the previous
      challenges were passed, this challenge is returned so that Amazon Cognito can start tracking
      this device.

      * ``DEVICE_PASSWORD_VERIFIER`` : Similar to ``PASSWORD_VERIFIER`` , but for devices only.

      * ``NEW_PASSWORD_REQUIRED`` : For users which are required to change their passwords after
      successful first login. This challenge should be passed with ``NEW_PASSWORD`` and any other
      required attributes.

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service. If
      the or API call determines that the caller needs to go through another challenge, they return
      a session with other challenge parameters. This session should be passed as it is to the next
      ``RespondToAuthChallenge`` API call.

    - **ChallengeParameters** *(dict) --*

      The challenge parameters. These are returned to you in the ``InitiateAuth`` response if you
      need to pass another challenge. The responses in this parameter should be used to compute
      inputs to the next call (``RespondToAuthChallenge`` ).

      All challenges require ``USERNAME`` and ``SECRET_HASH`` (if applicable).

      - *(string) --*

        - *(string) --*

    - **AuthenticationResult** *(dict) --*

      The result of the authentication response. This is only returned if the caller does not need
      to pass another challenge. If the caller does need to pass another challenge before it gets
      tokens, ``ChallengeName`` , ``ChallengeParameters`` , and ``Session`` are returned.

      - **AccessToken** *(string) --*

        The access token.

      - **ExpiresIn** *(integer) --*

        The expiration period of the authentication result in seconds.

      - **TokenType** *(string) --*

        The token type.

      - **RefreshToken** *(string) --*

        The refresh token.

      - **IdToken** *(string) --*

        The ID token.

      - **NewDeviceMetadata** *(dict) --*

        The new device metadata from an authentication result.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceGroupKey** *(string) --*

          The device group key.
    """


_ClientInitiateAuthUserContextDataTypeDef = TypedDict(
    "_ClientInitiateAuthUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientInitiateAuthUserContextDataTypeDef(
    _ClientInitiateAuthUserContextDataTypeDef
):
    """
    Type definition for `ClientInitiateAuth` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientListDevicesResponseDevicesDeviceAttributesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesDeviceAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListDevicesResponseDevicesDeviceAttributesTypeDef(
    _ClientListDevicesResponseDevicesDeviceAttributesTypeDef
):
    """
    Type definition for `ClientListDevicesResponseDevices` `DeviceAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List[
            ClientListDevicesResponseDevicesDeviceAttributesTypeDef
        ],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    Type definition for `ClientListDevicesResponse` `Devices`

    The device type.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceAttributes** *(list) --*

      The device attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **DeviceCreateDate** *(datetime) --*

      The creation date of the device.

    - **DeviceLastModifiedDate** *(datetime) --*

      The last modified date of the device.

    - **DeviceLastAuthenticatedDate** *(datetime) --*

      The date in which the device was last authenticated.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "PaginationToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    Type definition for `ClientListDevices` `Response`

    Represents the response to list devices.

    - **Devices** *(list) --*

      The devices returned in the list devices response.

      - *(dict) --*

        The device type.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceAttributes** *(list) --*

          The device attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **DeviceCreateDate** *(datetime) --*

          The creation date of the device.

        - **DeviceLastModifiedDate** *(datetime) --*

          The last modified date of the device.

        - **DeviceLastAuthenticatedDate** *(datetime) --*

          The date in which the device was last authenticated.

    - **PaginationToken** *(string) --*

      The pagination token for the list device response.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    Type definition for `ClientListGroupsResponse` `Groups`

    The group type.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
      each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
      claim is not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    Type definition for `ClientListGroups` `Response`

    - **Groups** *(list) --*

      The group objects for the groups.

      - *(dict) --*

        The group type.

        - **GroupName** *(string) --*

          The name of the group.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.

        - **Description** *(string) --*

          A string containing the description of the group.

        - **RoleArn** *(string) --*

          The role ARN for the group.

        - **Precedence** *(integer) --*

          A nonnegative integer value that specifies the precedence of this group relative to the
          other groups that a user can belong to in the user pool. If a user belongs to two or more
          groups, it is the group with the highest precedence whose role ARN will be used in the
          ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
          higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
          or with null ``Precedence`` values.

          Two groups can have the same ``Precedence`` value. If this happens, neither group takes
          precedence over the other. If two groups with the same ``Precedence`` have the same role
          ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
          each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
          claim is not set in users' tokens.

          The default ``Precedence`` value is null.

        - **LastModifiedDate** *(datetime) --*

          The date the group was last modified.

        - **CreationDate** *(datetime) --*

          The date the group was created.

    - **NextToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientListIdentityProvidersResponseProvidersTypeDef = TypedDict(
    "_ClientListIdentityProvidersResponseProvidersTypeDef",
    {
        "ProviderName": str,
        "ProviderType": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListIdentityProvidersResponseProvidersTypeDef(
    _ClientListIdentityProvidersResponseProvidersTypeDef
):
    """
    Type definition for `ClientListIdentityProvidersResponse` `Providers`

    A container for identity provider details.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **LastModifiedDate** *(datetime) --*

      The date the provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the provider was added to the user pool.
    """


_ClientListIdentityProvidersResponseTypeDef = TypedDict(
    "_ClientListIdentityProvidersResponseTypeDef",
    {
        "Providers": List[ClientListIdentityProvidersResponseProvidersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIdentityProvidersResponseTypeDef(
    _ClientListIdentityProvidersResponseTypeDef
):
    """
    Type definition for `ClientListIdentityProviders` `Response`

    - **Providers** *(list) --*

      A list of identity provider objects.

      - *(dict) --*

        A container for identity provider details.

        - **ProviderName** *(string) --*

          The identity provider name.

        - **ProviderType** *(string) --*

          The identity provider type.

        - **LastModifiedDate** *(datetime) --*

          The date the provider was last modified.

        - **CreationDate** *(datetime) --*

          The date the provider was added to the user pool.

    - **NextToken** *(string) --*

      A pagination token.
    """


_ClientListResourceServersResponseResourceServersScopesTypeDef = TypedDict(
    "_ClientListResourceServersResponseResourceServersScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientListResourceServersResponseResourceServersScopesTypeDef(
    _ClientListResourceServersResponseResourceServersScopesTypeDef
):
    """
    Type definition for `ClientListResourceServersResponseResourceServers` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --*

      The name of the scope.

    - **ScopeDescription** *(string) --*

      A description of the scope.
    """


_ClientListResourceServersResponseResourceServersTypeDef = TypedDict(
    "_ClientListResourceServersResponseResourceServersTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientListResourceServersResponseResourceServersScopesTypeDef],
    },
    total=False,
)


class ClientListResourceServersResponseResourceServersTypeDef(
    _ClientListResourceServersResponseResourceServersTypeDef
):
    """
    Type definition for `ClientListResourceServersResponse` `ResourceServers`

    A container for information about a resource server for a user pool.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that hosts the resource server.

    - **Identifier** *(string) --*

      The identifier for the resource server.

    - **Name** *(string) --*

      The name of the resource server.

    - **Scopes** *(list) --*

      A list of scopes that are defined for the resource server.

      - *(dict) --*

        A resource server scope.

        - **ScopeName** *(string) --*

          The name of the scope.

        - **ScopeDescription** *(string) --*

          A description of the scope.
    """


_ClientListResourceServersResponseTypeDef = TypedDict(
    "_ClientListResourceServersResponseTypeDef",
    {
        "ResourceServers": List[
            ClientListResourceServersResponseResourceServersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceServersResponseTypeDef(
    _ClientListResourceServersResponseTypeDef
):
    """
    Type definition for `ClientListResourceServers` `Response`

    - **ResourceServers** *(list) --*

      The resource servers.

      - *(dict) --*

        A container for information about a resource server for a user pool.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that hosts the resource server.

        - **Identifier** *(string) --*

          The identifier for the resource server.

        - **Name** *(string) --*

          The name of the resource server.

        - **Scopes** *(list) --*

          A list of scopes that are defined for the resource server.

          - *(dict) --*

            A resource server scope.

            - **ScopeName** *(string) --*

              The name of the scope.

            - **ScopeDescription** *(string) --*

              A description of the scope.

    - **NextToken** *(string) --*

      A pagination token.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      The tags that are assigned to the user pool.

      - *(string) --*

        - *(string) --*
    """


_ClientListUserImportJobsResponseUserImportJobsTypeDef = TypedDict(
    "_ClientListUserImportJobsResponseUserImportJobsTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientListUserImportJobsResponseUserImportJobsTypeDef(
    _ClientListUserImportJobsResponseUserImportJobsTypeDef
):
    """
    Type definition for `ClientListUserImportJobsResponse` `UserImportJobs`

    The user import job type.

    - **JobName** *(string) --*

      The job name for the user import job.

    - **JobId** *(string) --*

      The job ID for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are being imported into.

    - **PreSignedUrl** *(string) --*

      The pre-signed URL to be used to upload the ``.csv`` file.

    - **CreationDate** *(datetime) --*

      The date the user import job was created.

    - **StartDate** *(datetime) --*

      The date when the user import job was started.

    - **CompletionDate** *(datetime) --*

      The date when the user import job was completed.

    - **Status** *(string) --*

      The status of the user import job. One of the following:

      * ``Created`` - The job was created but not started.

      * ``Pending`` - A transition state. You have started the job, but it has not begun
      importing users yet.

      * ``InProgress`` - The job has started, and users are being imported.

      * ``Stopping`` - You have stopped the job, but the job has not stopped importing users
      yet.

      * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

      * ``Succeeded`` - The job has completed successfully.

      * ``Failed`` - The job has stopped due to an error.

      * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
      associated with the job was deleted, and the job cannot be started.

    - **CloudWatchLogsRoleArn** *(string) --*

      The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
      information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
      Guide.

    - **ImportedUsers** *(integer) --*

      The number of users that were successfully imported.

    - **SkippedUsers** *(integer) --*

      The number of users that were skipped.

    - **FailedUsers** *(integer) --*

      The number of users that could not be imported.

    - **CompletionMessage** *(string) --*

      The message returned when the user import job is completed.
    """


_ClientListUserImportJobsResponseTypeDef = TypedDict(
    "_ClientListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List[ClientListUserImportJobsResponseUserImportJobsTypeDef],
        "PaginationToken": str,
    },
    total=False,
)


class ClientListUserImportJobsResponseTypeDef(_ClientListUserImportJobsResponseTypeDef):
    """
    Type definition for `ClientListUserImportJobs` `Response`

    Represents the response from the server to the request to list the user import jobs.

    - **UserImportJobs** *(list) --*

      The user import jobs.

      - *(dict) --*

        The user import job type.

        - **JobName** *(string) --*

          The job name for the user import job.

        - **JobId** *(string) --*

          The job ID for the user import job.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that the users are being imported into.

        - **PreSignedUrl** *(string) --*

          The pre-signed URL to be used to upload the ``.csv`` file.

        - **CreationDate** *(datetime) --*

          The date the user import job was created.

        - **StartDate** *(datetime) --*

          The date when the user import job was started.

        - **CompletionDate** *(datetime) --*

          The date when the user import job was completed.

        - **Status** *(string) --*

          The status of the user import job. One of the following:

          * ``Created`` - The job was created but not started.

          * ``Pending`` - A transition state. You have started the job, but it has not begun
          importing users yet.

          * ``InProgress`` - The job has started, and users are being imported.

          * ``Stopping`` - You have stopped the job, but the job has not stopped importing users
          yet.

          * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

          * ``Succeeded`` - The job has completed successfully.

          * ``Failed`` - The job has stopped due to an error.

          * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
          associated with the job was deleted, and the job cannot be started.

        - **CloudWatchLogsRoleArn** *(string) --*

          The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
          information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
          Guide.

        - **ImportedUsers** *(integer) --*

          The number of users that were successfully imported.

        - **SkippedUsers** *(integer) --*

          The number of users that were skipped.

        - **FailedUsers** *(integer) --*

          The number of users that could not be imported.

        - **CompletionMessage** *(string) --*

          The message returned when the user import job is completed.

    - **PaginationToken** *(string) --*

      An identifier that can be used to return the next set of user import jobs in the list.
    """


_ClientListUserPoolClientsResponseUserPoolClientsTypeDef = TypedDict(
    "_ClientListUserPoolClientsResponseUserPoolClientsTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)


class ClientListUserPoolClientsResponseUserPoolClientsTypeDef(
    _ClientListUserPoolClientsResponseUserPoolClientsTypeDef
):
    """
    Type definition for `ClientListUserPoolClientsResponse` `UserPoolClients`

    The description of the user pool client.

    - **ClientId** *(string) --*

      The ID of the client associated with the user pool.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool where you want to describe the user pool client.

    - **ClientName** *(string) --*

      The client name from the user pool client description.
    """


_ClientListUserPoolClientsResponseTypeDef = TypedDict(
    "_ClientListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List[
            ClientListUserPoolClientsResponseUserPoolClientsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListUserPoolClientsResponseTypeDef(
    _ClientListUserPoolClientsResponseTypeDef
):
    """
    Type definition for `ClientListUserPoolClients` `Response`

    Represents the response from the server that lists user pool clients.

    - **UserPoolClients** *(list) --*

      The user pool clients in the response that lists user pool clients.

      - *(dict) --*

        The description of the user pool client.

        - **ClientId** *(string) --*

          The ID of the client associated with the user pool.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool where you want to describe the user pool client.

        - **ClientName** *(string) --*

          The client name from the user pool client description.

    - **NextToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef = TypedDict(
    "_ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef(
    _ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef
):
    """
    Type definition for `ClientListUserPoolsResponseUserPools` `LambdaConfig`

    The AWS Lambda configuration information in a user pool description.

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ClientListUserPoolsResponseUserPoolsTypeDef = TypedDict(
    "_ClientListUserPoolsResponseUserPoolsTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": ClientListUserPoolsResponseUserPoolsLambdaConfigTypeDef,
        "Status": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListUserPoolsResponseUserPoolsTypeDef(
    _ClientListUserPoolsResponseUserPoolsTypeDef
):
    """
    Type definition for `ClientListUserPoolsResponse` `UserPools`

    A user pool description.

    - **Id** *(string) --*

      The ID in a user pool description.

    - **Name** *(string) --*

      The name in a user pool description.

    - **LambdaConfig** *(dict) --*

      The AWS Lambda configuration information in a user pool description.

      - **PreSignUp** *(string) --*

        A pre-registration AWS Lambda trigger.

      - **CustomMessage** *(string) --*

        A custom Message AWS Lambda trigger.

      - **PostConfirmation** *(string) --*

        A post-confirmation AWS Lambda trigger.

      - **PreAuthentication** *(string) --*

        A pre-authentication AWS Lambda trigger.

      - **PostAuthentication** *(string) --*

        A post-authentication AWS Lambda trigger.

      - **DefineAuthChallenge** *(string) --*

        Defines the authentication challenge.

      - **CreateAuthChallenge** *(string) --*

        Creates an authentication challenge.

      - **VerifyAuthChallengeResponse** *(string) --*

        Verifies the authentication challenge response.

      - **PreTokenGeneration** *(string) --*

        A Lambda trigger that is invoked before token generation.

      - **UserMigration** *(string) --*

        The user migration Lambda config type.

    - **Status** *(string) --*

      The user pool status in a user pool description.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool description was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool description was created.
    """


_ClientListUserPoolsResponseTypeDef = TypedDict(
    "_ClientListUserPoolsResponseTypeDef",
    {"UserPools": List[ClientListUserPoolsResponseUserPoolsTypeDef], "NextToken": str},
    total=False,
)


class ClientListUserPoolsResponseTypeDef(_ClientListUserPoolsResponseTypeDef):
    """
    Type definition for `ClientListUserPools` `Response`

    Represents the response to list user pools.

    - **UserPools** *(list) --*

      The user pools from the response to list users.

      - *(dict) --*

        A user pool description.

        - **Id** *(string) --*

          The ID in a user pool description.

        - **Name** *(string) --*

          The name in a user pool description.

        - **LambdaConfig** *(dict) --*

          The AWS Lambda configuration information in a user pool description.

          - **PreSignUp** *(string) --*

            A pre-registration AWS Lambda trigger.

          - **CustomMessage** *(string) --*

            A custom Message AWS Lambda trigger.

          - **PostConfirmation** *(string) --*

            A post-confirmation AWS Lambda trigger.

          - **PreAuthentication** *(string) --*

            A pre-authentication AWS Lambda trigger.

          - **PostAuthentication** *(string) --*

            A post-authentication AWS Lambda trigger.

          - **DefineAuthChallenge** *(string) --*

            Defines the authentication challenge.

          - **CreateAuthChallenge** *(string) --*

            Creates an authentication challenge.

          - **VerifyAuthChallengeResponse** *(string) --*

            Verifies the authentication challenge response.

          - **PreTokenGeneration** *(string) --*

            A Lambda trigger that is invoked before token generation.

          - **UserMigration** *(string) --*

            The user migration Lambda config type.

        - **Status** *(string) --*

          The user pool status in a user pool description.

        - **LastModifiedDate** *(datetime) --*

          The date the user pool description was last modified.

        - **CreationDate** *(datetime) --*

          The date the user pool description was created.

    - **NextToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientListUsersInGroupResponseUsersAttributesTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListUsersInGroupResponseUsersAttributesTypeDef(
    _ClientListUsersInGroupResponseUsersAttributesTypeDef
):
    """
    Type definition for `ClientListUsersInGroupResponseUsers` `Attributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientListUsersInGroupResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientListUsersInGroupResponseUsersMFAOptionsTypeDef(
    _ClientListUsersInGroupResponseUsersMFAOptionsTypeDef
):
    """
    Type definition for `ClientListUsersInGroupResponseUsers` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA
     configurations. You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
    responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientListUsersInGroupResponseUsersTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersInGroupResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ClientListUsersInGroupResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ClientListUsersInGroupResponseUsersTypeDef(
    _ClientListUsersInGroupResponseUsersTypeDef
):
    """
    Type definition for `ClientListUsersInGroupResponse` `Users`

    The user type.

    - **Username** *(string) --*

      The user name of the user you wish to describe.

    - **Attributes** *(list) --*

      A container with information about the user type attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The creation date of the user.

    - **UserLastModifiedDate** *(datetime) --*

      The last modified date of the user.

    - **Enabled** *(boolean) --*

      Specifies whether the user is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
      her password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
      temporary password, but on first sign-in, the user must change his or her password to a
      new value before doing anything else.

    - **MFAOptions** *(list) --*

      The MFA options for the user.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA
         configurations. You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
        responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientListUsersInGroupResponseTypeDef = TypedDict(
    "_ClientListUsersInGroupResponseTypeDef",
    {"Users": List[ClientListUsersInGroupResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ClientListUsersInGroupResponseTypeDef(_ClientListUsersInGroupResponseTypeDef):
    """
    Type definition for `ClientListUsersInGroup` `Response`

    - **Users** *(list) --*

      The users returned in the request to list users.

      - *(dict) --*

        The user type.

        - **Username** *(string) --*

          The user name of the user you wish to describe.

        - **Attributes** *(list) --*

          A container with information about the user type attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **UserCreateDate** *(datetime) --*

          The creation date of the user.

        - **UserLastModifiedDate** *(datetime) --*

          The last modified date of the user.

        - **Enabled** *(boolean) --*

          Specifies whether the user is enabled.

        - **UserStatus** *(string) --*

          The user status. Can be one of the following:

          * UNCONFIRMED - User has been created but not confirmed.

          * CONFIRMED - User has been confirmed.

          * ARCHIVED - User is no longer active.

          * COMPROMISED - User is disabled due to a potential security threat.

          * UNKNOWN - User status is not known.

          * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
          her password before he or she can sign in.

          * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
          temporary password, but on first sign-in, the user must change his or her password to a
          new value before doing anything else.

        - **MFAOptions** *(list) --*

          The MFA options for the user.

          - *(dict) --*

             *This data type is no longer supported.* You can use it only for SMS MFA
             configurations. You can't use it for TOTP software token MFA configurations.

            To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
            SetUserMFAPreference actions.

            To look up information about either type of MFA configuration, use the
            AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
            responses.

            - **DeliveryMedium** *(string) --*

              The delivery medium to send the MFA code. You can use this parameter to set only the
              ``SMS`` delivery medium value.

            - **AttributeName** *(string) --*

              The attribute name of the MFA option type. The only valid value is ``phone_number`` .

    - **NextToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientListUsersResponseUsersAttributesTypeDef = TypedDict(
    "_ClientListUsersResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListUsersResponseUsersAttributesTypeDef(
    _ClientListUsersResponseUsersAttributesTypeDef
):
    """
    Type definition for `ClientListUsersResponseUsers` `Attributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientListUsersResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ClientListUsersResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientListUsersResponseUsersMFAOptionsTypeDef(
    _ClientListUsersResponseUsersMFAOptionsTypeDef
):
    """
    Type definition for `ClientListUsersResponseUsers` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA
     configurations. You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
    responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ClientListUsersResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ClientListUsersResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    """
    Type definition for `ClientListUsersResponse` `Users`

    The user type.

    - **Username** *(string) --*

      The user name of the user you wish to describe.

    - **Attributes** *(list) --*

      A container with information about the user type attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The creation date of the user.

    - **UserLastModifiedDate** *(datetime) --*

      The last modified date of the user.

    - **Enabled** *(boolean) --*

      Specifies whether the user is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
      her password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
      temporary password, but on first sign-in, the user must change his or her password to a
      new value before doing anything else.

    - **MFAOptions** *(list) --*

      The MFA options for the user.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA
         configurations. You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
        responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"Users": List[ClientListUsersResponseUsersTypeDef], "PaginationToken": str},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    The response from the request to list users.

    - **Users** *(list) --*

      The users returned in the request to list users.

      - *(dict) --*

        The user type.

        - **Username** *(string) --*

          The user name of the user you wish to describe.

        - **Attributes** *(list) --*

          A container with information about the user type attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **UserCreateDate** *(datetime) --*

          The creation date of the user.

        - **UserLastModifiedDate** *(datetime) --*

          The last modified date of the user.

        - **Enabled** *(boolean) --*

          Specifies whether the user is enabled.

        - **UserStatus** *(string) --*

          The user status. Can be one of the following:

          * UNCONFIRMED - User has been created but not confirmed.

          * CONFIRMED - User has been confirmed.

          * ARCHIVED - User is no longer active.

          * COMPROMISED - User is disabled due to a potential security threat.

          * UNKNOWN - User status is not known.

          * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
          her password before he or she can sign in.

          * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
          temporary password, but on first sign-in, the user must change his or her password to a
          new value before doing anything else.

        - **MFAOptions** *(list) --*

          The MFA options for the user.

          - *(dict) --*

             *This data type is no longer supported.* You can use it only for SMS MFA
             configurations. You can't use it for TOTP software token MFA configurations.

            To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
            SetUserMFAPreference actions.

            To look up information about either type of MFA configuration, use the
            AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
            responses.

            - **DeliveryMedium** *(string) --*

              The delivery medium to send the MFA code. You can use this parameter to set only the
              ``SMS`` delivery medium value.

            - **AttributeName** *(string) --*

              The attribute name of the MFA option type. The only valid value is ``phone_number`` .

    - **PaginationToken** *(string) --*

      An identifier that was returned from the previous call to this operation, which can be used
      to return the next set of items in the list.
    """


_ClientResendConfirmationCodeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientResendConfirmationCodeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientResendConfirmationCodeAnalyticsMetadataTypeDef(
    _ClientResendConfirmationCodeAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientResendConfirmationCode` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``ResendConfirmationCode``
    calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef(
    _ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef
):
    """
    Type definition for `ClientResendConfirmationCodeResponse` `CodeDeliveryDetails`

    The code delivery details returned by the server in response to the request to resend the
    confirmation code.

    - **Destination** *(string) --*

      The destination for the code delivery details.

    - **DeliveryMedium** *(string) --*

      The delivery medium (email message or phone number).

    - **AttributeName** *(string) --*

      The attribute name.
    """


_ClientResendConfirmationCodeResponseTypeDef = TypedDict(
    "_ClientResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": ClientResendConfirmationCodeResponseCodeDeliveryDetailsTypeDef
    },
    total=False,
)


class ClientResendConfirmationCodeResponseTypeDef(
    _ClientResendConfirmationCodeResponseTypeDef
):
    """
    Type definition for `ClientResendConfirmationCode` `Response`

    The response from the server when the Amazon Cognito Your User Pools service makes the request
    to resend a confirmation code.

    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server in response to the request to resend the
      confirmation code.

      - **Destination** *(string) --*

        The destination for the code delivery details.

      - **DeliveryMedium** *(string) --*

        The delivery medium (email message or phone number).

      - **AttributeName** *(string) --*

        The attribute name.
    """


_ClientResendConfirmationCodeUserContextDataTypeDef = TypedDict(
    "_ClientResendConfirmationCodeUserContextDataTypeDef",
    {"EncodedData": str},
    total=False,
)


class ClientResendConfirmationCodeUserContextDataTypeDef(
    _ClientResendConfirmationCodeUserContextDataTypeDef
):
    """
    Type definition for `ClientResendConfirmationCode` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientRespondToAuthChallengeAnalyticsMetadataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeAnalyticsMetadataTypeDef",
    {"AnalyticsEndpointId": str},
    total=False,
)


class ClientRespondToAuthChallengeAnalyticsMetadataTypeDef(
    _ClientRespondToAuthChallengeAnalyticsMetadataTypeDef
):
    """
    Type definition for `ClientRespondToAuthChallenge` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``RespondToAuthChallenge``
    calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef",
    {"DeviceKey": str, "DeviceGroupKey": str},
    total=False,
)


class ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef(
    _ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef
):
    """
    Type definition for `ClientRespondToAuthChallengeResponseAuthenticationResult` `NewDeviceMetadata`

    The new device metadata from an authentication result.

    - **DeviceKey** *(string) --*

      The device key.

    - **DeviceGroupKey** *(string) --*

      The device group key.
    """


_ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": ClientRespondToAuthChallengeResponseAuthenticationResultNewDeviceMetadataTypeDef,
    },
    total=False,
)


class ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef(
    _ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef
):
    """
    Type definition for `ClientRespondToAuthChallengeResponse` `AuthenticationResult`

    The result returned by the server in response to the request to respond to the authentication
    challenge.

    - **AccessToken** *(string) --*

      The access token.

    - **ExpiresIn** *(integer) --*

      The expiration period of the authentication result in seconds.

    - **TokenType** *(string) --*

      The token type.

    - **RefreshToken** *(string) --*

      The refresh token.

    - **IdToken** *(string) --*

      The ID token.

    - **NewDeviceMetadata** *(dict) --*

      The new device metadata from an authentication result.

      - **DeviceKey** *(string) --*

        The device key.

      - **DeviceGroupKey** *(string) --*

        The device group key.
    """


_ClientRespondToAuthChallengeResponseTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": str,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": ClientRespondToAuthChallengeResponseAuthenticationResultTypeDef,
    },
    total=False,
)


class ClientRespondToAuthChallengeResponseTypeDef(
    _ClientRespondToAuthChallengeResponseTypeDef
):
    """
    Type definition for `ClientRespondToAuthChallenge` `Response`

    The response to respond to the authentication challenge.

    - **ChallengeName** *(string) --*

      The challenge name. For more information, see .

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service. If
      the or API call determines that the caller needs to go through another challenge, they return
      a session with other challenge parameters. This session should be passed as it is to the next
      ``RespondToAuthChallenge`` API call.

    - **ChallengeParameters** *(dict) --*

      The challenge parameters. For more information, see .

      - *(string) --*

        - *(string) --*

    - **AuthenticationResult** *(dict) --*

      The result returned by the server in response to the request to respond to the authentication
      challenge.

      - **AccessToken** *(string) --*

        The access token.

      - **ExpiresIn** *(integer) --*

        The expiration period of the authentication result in seconds.

      - **TokenType** *(string) --*

        The token type.

      - **RefreshToken** *(string) --*

        The refresh token.

      - **IdToken** *(string) --*

        The ID token.

      - **NewDeviceMetadata** *(dict) --*

        The new device metadata from an authentication result.

        - **DeviceKey** *(string) --*

          The device key.

        - **DeviceGroupKey** *(string) --*

          The device group key.
    """


_ClientRespondToAuthChallengeUserContextDataTypeDef = TypedDict(
    "_ClientRespondToAuthChallengeUserContextDataTypeDef",
    {"EncodedData": str},
    total=False,
)


class ClientRespondToAuthChallengeUserContextDataTypeDef(
    _ClientRespondToAuthChallengeUserContextDataTypeDef
):
    """
    Type definition for `ClientRespondToAuthChallenge` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {"Notify": bool, "EventAction": str},
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActions` `HighAction`

    Action to take for a high risk.

    - **Notify** *(boolean) --* **[REQUIRED]**

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --* **[REQUIRED]**

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {"Notify": bool, "EventAction": str},
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActions` `LowAction`

    Action to take for a low risk.

    - **Notify** *(boolean) --* **[REQUIRED]**

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --* **[REQUIRED]**

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {"Notify": bool, "EventAction": str},
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActions` `MediumAction`

    Action to take for a medium risk.

    - **Notify** *(boolean) --* **[REQUIRED]**

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --* **[REQUIRED]**

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfiguration` `Actions`

    Account takeover risk configuration actions

    - **LowAction** *(dict) --*

      Action to take for a low risk.

      - **Notify** *(boolean) --* **[REQUIRED]**

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --* **[REQUIRED]**

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **MediumAction** *(dict) --*

      Action to take for a medium risk.

      - **Notify** *(boolean) --* **[REQUIRED]**

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --* **[REQUIRED]**

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **HighAction** *(dict) --*

      Action to take for a high risk.

      - **Notify** *(boolean) --* **[REQUIRED]**

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --* **[REQUIRED]**

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

        * ``NO_ACTION`` Allow the user sign-in.
    """


_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str},
)
_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
    _OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `BlockEmail`

    Email template used when a detected risk event is blocked.

    - **Subject** *(string) --* **[REQUIRED]**

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str},
)
_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    _OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `MfaEmail`

    The MFA email template used when MFA is challenged as part of a detected risk.

    - **Subject** *(string) --* **[REQUIRED]**

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str},
)
_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
    _OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `NoActionEmail`

    The email template used when a detected risk event is allowed.

    - **Subject** *(string) --* **[REQUIRED]**

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {"SourceArn": str},
)
_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
    _OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
):
    """
    Type definition for `ClientSetRiskConfigurationAccountTakeoverRiskConfiguration` `NotifyConfiguration`

    The notify configuration used to construct email notifications.

    - **From** *(string) --*

      The email address that is sending the email. It must be either individually verified with
      Amazon SES, or from a domain that has been verified with Amazon SES.

    - **ReplyTo** *(string) --*

      The destination to which the receiver of an email should reply to.

    - **SourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the identity that is associated with the sending
      authorization policy. It permits Amazon Cognito to send for the email address specified in
      the ``From`` parameter.

    - **BlockEmail** *(dict) --*

      Email template used when a detected risk event is blocked.

      - **Subject** *(string) --* **[REQUIRED]**

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **NoActionEmail** *(dict) --*

      The email template used when a detected risk event is allowed.

      - **Subject** *(string) --* **[REQUIRED]**

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **MfaEmail** *(dict) --*

      The MFA email template used when MFA is challenged as part of a detected risk.

      - **Subject** *(string) --* **[REQUIRED]**

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.
    """


_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "Actions": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
    },
)
_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
    },
    total=False,
)


class ClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _RequiredClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
    _OptionalClientSetRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
):
    """
    Type definition for `ClientSetRiskConfiguration` `AccountTakeoverRiskConfiguration`

    The account takeover risk configuration.

    - **NotifyConfiguration** *(dict) --*

      The notify configuration used to construct email notifications.

      - **From** *(string) --*

        The email address that is sending the email. It must be either individually verified with
        Amazon SES, or from a domain that has been verified with Amazon SES.

      - **ReplyTo** *(string) --*

        The destination to which the receiver of an email should reply to.

      - **SourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the identity that is associated with the sending
        authorization policy. It permits Amazon Cognito to send for the email address specified in
        the ``From`` parameter.

      - **BlockEmail** *(dict) --*

        Email template used when a detected risk event is blocked.

        - **Subject** *(string) --* **[REQUIRED]**

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **NoActionEmail** *(dict) --*

        The email template used when a detected risk event is allowed.

        - **Subject** *(string) --* **[REQUIRED]**

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **MfaEmail** *(dict) --*

        The MFA email template used when MFA is challenged as part of a detected risk.

        - **Subject** *(string) --* **[REQUIRED]**

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

    - **Actions** *(dict) --* **[REQUIRED]**

      Account takeover risk configuration actions

      - **LowAction** *(dict) --*

        Action to take for a low risk.

        - **Notify** *(boolean) --* **[REQUIRED]**

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --* **[REQUIRED]**

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **MediumAction** *(dict) --*

        Action to take for a medium risk.

        - **Notify** *(boolean) --* **[REQUIRED]**

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --* **[REQUIRED]**

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **HighAction** *(dict) --*

        Action to take for a high risk.

        - **Notify** *(boolean) --* **[REQUIRED]**

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --* **[REQUIRED]**

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the request.

          * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": str},
)


class ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationCompromisedCredentialsRiskConfiguration` `Actions`

    The compromised credentials risk configuration actions.

    - **EventAction** *(string) --* **[REQUIRED]**

      The event action.
    """


_RequiredClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_RequiredClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "Actions": ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
    },
)
_OptionalClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_OptionalClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {"EventFilter": List[str]},
    total=False,
)


class ClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _RequiredClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
    _OptionalClientSetRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
):
    """
    Type definition for `ClientSetRiskConfiguration` `CompromisedCredentialsRiskConfiguration`

    The compromised credentials risk configuration.

    - **EventFilter** *(list) --*

      Perform the action for these events. The default is to perform all events if no event filter is
      specified.

      - *(string) --*

    - **Actions** *(dict) --* **[REQUIRED]**

      The compromised credentials risk configuration actions.

      - **EventAction** *(string) --* **[REQUIRED]**

        The event action.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `HighAction`

    Action to take for a high risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `LowAction`

    Action to take for a low risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef",
    {"Notify": bool, "EventAction": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActions` `MediumAction`

    Action to take for a medium risk.

    - **Notify** *(boolean) --*

      Flag specifying whether to send a notification.

    - **EventAction** *(string) --*

      The event action.

      * ``BLOCK`` Choosing this action will block the request.

      * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
      request.

      * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
      request.

      * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef",
    {
        "LowAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionTypeDef,
        "MediumAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionTypeDef,
        "HighAction": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfiguration` `Actions`

    Account takeover risk configuration actions

    - **LowAction** *(dict) --*

      Action to take for a low risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **MediumAction** *(dict) --*

      Action to take for a medium risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.

    - **HighAction** *(dict) --*

      Action to take for a high risk.

      - **Notify** *(boolean) --*

        Flag specifying whether to send a notification.

      - **EventAction** *(string) --*

        The event action.

        * ``BLOCK`` Choosing this action will block the request.

        * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
        request.

        * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
        request.

        * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `BlockEmail`

    Email template used when a detected risk event is blocked.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `MfaEmail`

    The MFA email template used when MFA is challenged as part of a detected risk.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef",
    {"Subject": str, "HtmlBody": str, "TextBody": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration` `NoActionEmail`

    The email template used when a detected risk event is allowed.

    - **Subject** *(string) --*

      The subject.

    - **HtmlBody** *(string) --*

      The HTML body.

    - **TextBody** *(string) --*

      The text body.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "SourceArn": str,
        "BlockEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailTypeDef,
        "NoActionEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailTypeDef,
        "MfaEmail": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfiguration` `NotifyConfiguration`

    The notify configuration used to construct email notifications.

    - **From** *(string) --*

      The email address that is sending the email. It must be either individually verified
      with Amazon SES, or from a domain that has been verified with Amazon SES.

    - **ReplyTo** *(string) --*

      The destination to which the receiver of an email should reply to.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the identity that is associated with the sending
      authorization policy. It permits Amazon Cognito to send for the email address specified
      in the ``From`` parameter.

    - **BlockEmail** *(dict) --*

      Email template used when a detected risk event is blocked.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **NoActionEmail** *(dict) --*

      The email template used when a detected risk event is allowed.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.

    - **MfaEmail** *(dict) --*

      The MFA email template used when MFA is challenged as part of a detected risk.

      - **Subject** *(string) --*

        The subject.

      - **HtmlBody** *(string) --*

        The HTML body.

      - **TextBody** *(string) --*

        The text body.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef",
    {
        "NotifyConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationTypeDef,
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfiguration` `AccountTakeoverRiskConfiguration`

    The account takeover risk configuration object including the ``NotifyConfiguration`` object
    and ``Actions`` to take in the case of an account takeover.

    - **NotifyConfiguration** *(dict) --*

      The notify configuration used to construct email notifications.

      - **From** *(string) --*

        The email address that is sending the email. It must be either individually verified
        with Amazon SES, or from a domain that has been verified with Amazon SES.

      - **ReplyTo** *(string) --*

        The destination to which the receiver of an email should reply to.

      - **SourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the identity that is associated with the sending
        authorization policy. It permits Amazon Cognito to send for the email address specified
        in the ``From`` parameter.

      - **BlockEmail** *(dict) --*

        Email template used when a detected risk event is blocked.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **NoActionEmail** *(dict) --*

        The email template used when a detected risk event is allowed.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

      - **MfaEmail** *(dict) --*

        The MFA email template used when MFA is challenged as part of a detected risk.

        - **Subject** *(string) --*

          The subject.

        - **HtmlBody** *(string) --*

          The HTML body.

        - **TextBody** *(string) --*

          The text body.

    - **Actions** *(dict) --*

      Account takeover risk configuration actions

      - **LowAction** *(dict) --*

        Action to take for a low risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **MediumAction** *(dict) --*

        Action to take for a medium risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.

      - **HighAction** *(dict) --*

        Action to take for a high risk.

        - **Notify** *(boolean) --*

          Flag specifying whether to send a notification.

        - **EventAction** *(string) --*

          The event action.

          * ``BLOCK`` Choosing this action will block the request.

          * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
          request.

          * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
          request.

          * ``NO_ACTION`` Allow the user sign-in.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef",
    {"EventAction": str},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfiguration` `Actions`

    The compromised credentials risk configuration actions.

    - **EventAction** *(string) --*

      The event action.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef",
    {
        "EventFilter": List[str],
        "Actions": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationActionsTypeDef,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfiguration` `CompromisedCredentialsRiskConfiguration`

    The compromised credentials risk configuration object including the ``EventFilter`` and the
    ``EventAction``

    - **EventFilter** *(list) --*

      Perform the action for these events. The default is to perform all events if no event
      filter is specified.

      - *(string) --*

    - **Actions** *(dict) --*

      The compromised credentials risk configuration actions.

      - **EventAction** *(string) --*

        The event action.
    """


_ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponseRiskConfiguration` `RiskExceptionConfiguration`

    The configuration to override the risk decision.

    - **BlockedIPRangeList** *(list) --*

      Overrides the risk decision to always block the pre-authentication requests. The IP range
      is in CIDR notation: a compact representation of an IP address and its associated routing
      prefix.

      - *(string) --*

    - **SkippedIPRangeList** *(list) --*

      Risk detection is not performed on the IP addresses in the range list. The IP range is in
      CIDR notation.

      - *(string) --*
    """


_ClientSetRiskConfigurationResponseRiskConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseRiskConfigurationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationCompromisedCredentialsRiskConfigurationTypeDef,
        "AccountTakeoverRiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationAccountTakeoverRiskConfigurationTypeDef,
        "RiskExceptionConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationRiskExceptionConfigurationTypeDef,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientSetRiskConfigurationResponseRiskConfigurationTypeDef(
    _ClientSetRiskConfigurationResponseRiskConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfigurationResponse` `RiskConfiguration`

    The risk configuration.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ClientId** *(string) --*

      The app client ID.

    - **CompromisedCredentialsRiskConfiguration** *(dict) --*

      The compromised credentials risk configuration object including the ``EventFilter`` and the
      ``EventAction``

      - **EventFilter** *(list) --*

        Perform the action for these events. The default is to perform all events if no event
        filter is specified.

        - *(string) --*

      - **Actions** *(dict) --*

        The compromised credentials risk configuration actions.

        - **EventAction** *(string) --*

          The event action.

    - **AccountTakeoverRiskConfiguration** *(dict) --*

      The account takeover risk configuration object including the ``NotifyConfiguration`` object
      and ``Actions`` to take in the case of an account takeover.

      - **NotifyConfiguration** *(dict) --*

        The notify configuration used to construct email notifications.

        - **From** *(string) --*

          The email address that is sending the email. It must be either individually verified
          with Amazon SES, or from a domain that has been verified with Amazon SES.

        - **ReplyTo** *(string) --*

          The destination to which the receiver of an email should reply to.

        - **SourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the identity that is associated with the sending
          authorization policy. It permits Amazon Cognito to send for the email address specified
          in the ``From`` parameter.

        - **BlockEmail** *(dict) --*

          Email template used when a detected risk event is blocked.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

        - **NoActionEmail** *(dict) --*

          The email template used when a detected risk event is allowed.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

        - **MfaEmail** *(dict) --*

          The MFA email template used when MFA is challenged as part of a detected risk.

          - **Subject** *(string) --*

            The subject.

          - **HtmlBody** *(string) --*

            The HTML body.

          - **TextBody** *(string) --*

            The text body.

      - **Actions** *(dict) --*

        Account takeover risk configuration actions

        - **LowAction** *(dict) --*

          Action to take for a low risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

        - **MediumAction** *(dict) --*

          Action to take for a medium risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

        - **HighAction** *(dict) --*

          Action to take for a high risk.

          - **Notify** *(boolean) --*

            Flag specifying whether to send a notification.

          - **EventAction** *(string) --*

            The event action.

            * ``BLOCK`` Choosing this action will block the request.

            * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
            request.

            * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
            request.

            * ``NO_ACTION`` Allow the user sign-in.

    - **RiskExceptionConfiguration** *(dict) --*

      The configuration to override the risk decision.

      - **BlockedIPRangeList** *(list) --*

        Overrides the risk decision to always block the pre-authentication requests. The IP range
        is in CIDR notation: a compact representation of an IP address and its associated routing
        prefix.

        - *(string) --*

      - **SkippedIPRangeList** *(list) --*

        Risk detection is not performed on the IP addresses in the range list. The IP range is in
        CIDR notation.

        - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The last modified date.
    """


_ClientSetRiskConfigurationResponseTypeDef = TypedDict(
    "_ClientSetRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": ClientSetRiskConfigurationResponseRiskConfigurationTypeDef},
    total=False,
)


class ClientSetRiskConfigurationResponseTypeDef(
    _ClientSetRiskConfigurationResponseTypeDef
):
    """
    Type definition for `ClientSetRiskConfiguration` `Response`

    - **RiskConfiguration** *(dict) --*

      The risk configuration.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ClientId** *(string) --*

        The app client ID.

      - **CompromisedCredentialsRiskConfiguration** *(dict) --*

        The compromised credentials risk configuration object including the ``EventFilter`` and the
        ``EventAction``

        - **EventFilter** *(list) --*

          Perform the action for these events. The default is to perform all events if no event
          filter is specified.

          - *(string) --*

        - **Actions** *(dict) --*

          The compromised credentials risk configuration actions.

          - **EventAction** *(string) --*

            The event action.

      - **AccountTakeoverRiskConfiguration** *(dict) --*

        The account takeover risk configuration object including the ``NotifyConfiguration`` object
        and ``Actions`` to take in the case of an account takeover.

        - **NotifyConfiguration** *(dict) --*

          The notify configuration used to construct email notifications.

          - **From** *(string) --*

            The email address that is sending the email. It must be either individually verified
            with Amazon SES, or from a domain that has been verified with Amazon SES.

          - **ReplyTo** *(string) --*

            The destination to which the receiver of an email should reply to.

          - **SourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the identity that is associated with the sending
            authorization policy. It permits Amazon Cognito to send for the email address specified
            in the ``From`` parameter.

          - **BlockEmail** *(dict) --*

            Email template used when a detected risk event is blocked.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

          - **NoActionEmail** *(dict) --*

            The email template used when a detected risk event is allowed.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

          - **MfaEmail** *(dict) --*

            The MFA email template used when MFA is challenged as part of a detected risk.

            - **Subject** *(string) --*

              The subject.

            - **HtmlBody** *(string) --*

              The HTML body.

            - **TextBody** *(string) --*

              The text body.

        - **Actions** *(dict) --*

          Account takeover risk configuration actions

          - **LowAction** *(dict) --*

            Action to take for a low risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

          - **MediumAction** *(dict) --*

            Action to take for a medium risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

          - **HighAction** *(dict) --*

            Action to take for a high risk.

            - **Notify** *(boolean) --*

              Flag specifying whether to send a notification.

            - **EventAction** *(string) --*

              The event action.

              * ``BLOCK`` Choosing this action will block the request.

              * ``MFA_IF_CONFIGURED`` Throw MFA challenge if user has configured it, else allow the
              request.

              * ``MFA_REQUIRED`` Throw MFA challenge if user has configured it, else block the
              request.

              * ``NO_ACTION`` Allow the user sign-in.

      - **RiskExceptionConfiguration** *(dict) --*

        The configuration to override the risk decision.

        - **BlockedIPRangeList** *(list) --*

          Overrides the risk decision to always block the pre-authentication requests. The IP range
          is in CIDR notation: a compact representation of an IP address and its associated routing
          prefix.

          - *(string) --*

        - **SkippedIPRangeList** *(list) --*

          Risk detection is not performed on the IP addresses in the range list. The IP range is in
          CIDR notation.

          - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The last modified date.
    """


_ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef = TypedDict(
    "_ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)


class ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef(
    _ClientSetRiskConfigurationRiskExceptionConfigurationTypeDef
):
    """
    Type definition for `ClientSetRiskConfiguration` `RiskExceptionConfiguration`

    The configuration to override the risk decision.

    - **BlockedIPRangeList** *(list) --*

      Overrides the risk decision to always block the pre-authentication requests. The IP range is in
      CIDR notation: a compact representation of an IP address and its associated routing prefix.

      - *(string) --*

    - **SkippedIPRangeList** *(list) --*

      Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR
      notation.

      - *(string) --*
    """


_ClientSetUiCustomizationResponseUICustomizationTypeDef = TypedDict(
    "_ClientSetUiCustomizationResponseUICustomizationTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientSetUiCustomizationResponseUICustomizationTypeDef(
    _ClientSetUiCustomizationResponseUICustomizationTypeDef
):
    """
    Type definition for `ClientSetUiCustomizationResponse` `UICustomization`

    The UI customization information.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **ClientId** *(string) --*

      The client ID for the client app.

    - **ImageUrl** *(string) --*

      The logo image for the UI customization.

    - **CSS** *(string) --*

      The CSS values in the UI customization.

    - **CSSVersion** *(string) --*

      The CSS version number.

    - **LastModifiedDate** *(datetime) --*

      The last-modified date for the UI customization.

    - **CreationDate** *(datetime) --*

      The creation date for the UI customization.
    """


_ClientSetUiCustomizationResponseTypeDef = TypedDict(
    "_ClientSetUiCustomizationResponseTypeDef",
    {"UICustomization": ClientSetUiCustomizationResponseUICustomizationTypeDef},
    total=False,
)


class ClientSetUiCustomizationResponseTypeDef(_ClientSetUiCustomizationResponseTypeDef):
    """
    Type definition for `ClientSetUiCustomization` `Response`

    - **UICustomization** *(dict) --*

      The UI customization information.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.

      - **ClientId** *(string) --*

        The client ID for the client app.

      - **ImageUrl** *(string) --*

        The logo image for the UI customization.

      - **CSS** *(string) --*

        The CSS values in the UI customization.

      - **CSSVersion** *(string) --*

        The CSS version number.

      - **LastModifiedDate** *(datetime) --*

        The last-modified date for the UI customization.

      - **CreationDate** *(datetime) --*

        The creation date for the UI customization.
    """


_ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef = TypedDict(
    "_ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef(
    _ClientSetUserMfaPreferenceSMSMfaSettingsTypeDef
):
    """
    Type definition for `ClientSetUserMfaPreference` `SMSMfaSettings`

    The SMS text message multi-factor authentication (MFA) settings.

    - **Enabled** *(boolean) --*

      Specifies whether SMS text message MFA is enabled.

    - **PreferredMfa** *(boolean) --*

      Specifies whether SMS is the preferred MFA method.
    """


_ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef = TypedDict(
    "_ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef",
    {"Enabled": bool, "PreferredMfa": bool},
    total=False,
)


class ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef(
    _ClientSetUserMfaPreferenceSoftwareTokenMfaSettingsTypeDef
):
    """
    Type definition for `ClientSetUserMfaPreference` `SoftwareTokenMfaSettings`

    The time-based one-time password software token MFA settings.

    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.

    - **PreferredMfa** *(boolean) --*

      Specifies whether software token MFA is the preferred MFA method.
    """


_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str, "ExternalId": str},
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfigResponseSmsMfaConfiguration` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
      This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
      messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role
      which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
      an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
      IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
      you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
      a role with the required permissions and a trust policy that demonstrates use of the
      ``ExternalId`` .
    """


_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfigResponse` `SmsMfaConfiguration`

    The SMS text message MFA configuration.

    - **SmsAuthenticationMessage** *(string) --*

      The SMS authentication message that will be sent to users with the code they need to sign
      in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
      code. If the message is not included, and default message will be used.

    - **SmsConfiguration** *(dict) --*

      The SMS configuration.

      - **SnsCallerArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
        This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
        messages.

      - **ExternalId** *(string) --*

        The external ID is a value that we recommend you use to add security to your IAM role
        which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
        an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
        IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
        you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
        a role with the required permissions and a trust policy that demonstrates use of the
        ``ExternalId`` .
    """


_ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfigResponse` `SoftwareTokenMfaConfiguration`

    The software token MFA configuration.

    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientSetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": ClientSetUserPoolMfaConfigResponseSmsMfaConfigurationTypeDef,
        "SoftwareTokenMfaConfiguration": ClientSetUserPoolMfaConfigResponseSoftwareTokenMfaConfigurationTypeDef,
        "MfaConfiguration": str,
    },
    total=False,
)


class ClientSetUserPoolMfaConfigResponseTypeDef(
    _ClientSetUserPoolMfaConfigResponseTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfig` `Response`

    - **SmsMfaConfiguration** *(dict) --*

      The SMS text message MFA configuration.

      - **SmsAuthenticationMessage** *(string) --*

        The SMS authentication message that will be sent to users with the code they need to sign
        in. The message must contain the ‘{####}’ placeholder, which will be replaced with the
        code. If the message is not included, and default message will be used.

      - **SmsConfiguration** *(dict) --*

        The SMS configuration.

        - **SnsCallerArn** *(string) --*

          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller.
          This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS
          messages.

        - **ExternalId** *(string) --*

          The external ID is a value that we recommend you use to add security to your IAM role
          which is used to call Amazon SNS to send SMS messages for your user pool. If you provide
          an ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your
          IAM role, so that you can set your roles trust policy to require the ``ExternalID`` . If
          you use the Cognito Management Console to create a role for SMS MFA, Cognito will create
          a role with the required permissions and a trust policy that demonstrates use of the
          ``ExternalId`` .

    - **SoftwareTokenMfaConfiguration** *(dict) --*

      The software token MFA configuration.

      - **Enabled** *(boolean) --*

        Specifies whether software token MFA is enabled.

    - **MfaConfiguration** *(string) --*

      The MFA configuration. Valid values include:

      * ``OFF`` MFA will not be used for any users.

      * ``ON`` MFA is required for all users to sign in.

      * ``OPTIONAL`` MFA will be required only for individual users who have an MFA factor enabled.
    """


_RequiredClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    {"SnsCallerArn": str},
)
_OptionalClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef",
    {"ExternalId": str},
    total=False,
)


class ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef(
    _RequiredClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef,
    _OptionalClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef,
):
    """
    Type definition for `ClientSetUserPoolMfaConfigSmsMfaConfiguration` `SmsConfiguration`

    The SMS configuration.

    - **SnsCallerArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This
      is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role which
      is used to call Amazon SNS to send SMS messages for your user pool. If you provide an
      ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your IAM
      role, so that you can set your roles trust policy to require the ``ExternalID`` . If you use
      the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with
      the required permissions and a trust policy that demonstrates use of the ``ExternalId`` .
    """


_ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": ClientSetUserPoolMfaConfigSmsMfaConfigurationSmsConfigurationTypeDef,
    },
    total=False,
)


class ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigSmsMfaConfigurationTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfig` `SmsMfaConfiguration`

    The SMS text message MFA configuration.

    - **SmsAuthenticationMessage** *(string) --*

      The SMS authentication message that will be sent to users with the code they need to sign in.
      The message must contain the ‘{####}’ placeholder, which will be replaced with the code. If the
      message is not included, and default message will be used.

    - **SmsConfiguration** *(dict) --*

      The SMS configuration.

      - **SnsCallerArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This
        is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

      - **ExternalId** *(string) --*

        The external ID is a value that we recommend you use to add security to your IAM role which
        is used to call Amazon SNS to send SMS messages for your user pool. If you provide an
        ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your IAM
        role, so that you can set your roles trust policy to require the ``ExternalID`` . If you use
        the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with
        the required permissions and a trust policy that demonstrates use of the ``ExternalId`` .
    """


_ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef = TypedDict(
    "_ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef(
    _ClientSetUserPoolMfaConfigSoftwareTokenMfaConfigurationTypeDef
):
    """
    Type definition for `ClientSetUserPoolMfaConfig` `SoftwareTokenMfaConfiguration`

    The software token MFA configuration.

    - **Enabled** *(boolean) --*

      Specifies whether software token MFA is enabled.
    """


_ClientSetUserSettingsMFAOptionsTypeDef = TypedDict(
    "_ClientSetUserSettingsMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientSetUserSettingsMFAOptionsTypeDef(_ClientSetUserSettingsMFAOptionsTypeDef):
    """
    Type definition for `ClientSetUserSettings` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA configurations. You
     can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the ``SMS``
      delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ClientSignUpAnalyticsMetadataTypeDef = TypedDict(
    "_ClientSignUpAnalyticsMetadataTypeDef", {"AnalyticsEndpointId": str}, total=False
)


class ClientSignUpAnalyticsMetadataTypeDef(_ClientSignUpAnalyticsMetadataTypeDef):
    """
    Type definition for `ClientSignUp` `AnalyticsMetadata`

    The Amazon Pinpoint analytics metadata for collecting metrics for ``SignUp`` calls.

    - **AnalyticsEndpointId** *(string) --*

      The endpoint ID.
    """


_ClientSignUpResponseCodeDeliveryDetailsTypeDef = TypedDict(
    "_ClientSignUpResponseCodeDeliveryDetailsTypeDef",
    {"Destination": str, "DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientSignUpResponseCodeDeliveryDetailsTypeDef(
    _ClientSignUpResponseCodeDeliveryDetailsTypeDef
):
    """
    Type definition for `ClientSignUpResponse` `CodeDeliveryDetails`

    The code delivery details returned by the server response to the user registration request.

    - **Destination** *(string) --*

      The destination for the code delivery details.

    - **DeliveryMedium** *(string) --*

      The delivery medium (email message or phone number).

    - **AttributeName** *(string) --*

      The attribute name.
    """


_ClientSignUpResponseTypeDef = TypedDict(
    "_ClientSignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": ClientSignUpResponseCodeDeliveryDetailsTypeDef,
        "UserSub": str,
    },
    total=False,
)


class ClientSignUpResponseTypeDef(_ClientSignUpResponseTypeDef):
    """
    Type definition for `ClientSignUp` `Response`

    The response from the server for a registration request.

    - **UserConfirmed** *(boolean) --*

      A response from the server indicating that a user registration has been confirmed.

    - **CodeDeliveryDetails** *(dict) --*

      The code delivery details returned by the server response to the user registration request.

      - **Destination** *(string) --*

        The destination for the code delivery details.

      - **DeliveryMedium** *(string) --*

        The delivery medium (email message or phone number).

      - **AttributeName** *(string) --*

        The attribute name.

    - **UserSub** *(string) --*

      The UUID of the authenticated user. This is not the same as ``username`` .
    """


_RequiredClientSignUpUserAttributesTypeDef = TypedDict(
    "_RequiredClientSignUpUserAttributesTypeDef", {"Name": str}
)
_OptionalClientSignUpUserAttributesTypeDef = TypedDict(
    "_OptionalClientSignUpUserAttributesTypeDef", {"Value": str}, total=False
)


class ClientSignUpUserAttributesTypeDef(
    _RequiredClientSignUpUserAttributesTypeDef,
    _OptionalClientSignUpUserAttributesTypeDef,
):
    """
    Type definition for `ClientSignUp` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientSignUpUserContextDataTypeDef = TypedDict(
    "_ClientSignUpUserContextDataTypeDef", {"EncodedData": str}, total=False
)


class ClientSignUpUserContextDataTypeDef(_ClientSignUpUserContextDataTypeDef):
    """
    Type definition for `ClientSignUp` `UserContextData`

    Contextual data such as the user's device fingerprint, IP address, or location used for
    evaluating the risk of an unexpected event by Amazon Cognito advanced security.

    - **EncodedData** *(string) --*

      Contextual data such as the user's device fingerprint, IP address, or location used for
      evaluating the risk of an unexpected event by Amazon Cognito advanced security.
    """


_RequiredClientSignUpValidationDataTypeDef = TypedDict(
    "_RequiredClientSignUpValidationDataTypeDef", {"Name": str}
)
_OptionalClientSignUpValidationDataTypeDef = TypedDict(
    "_OptionalClientSignUpValidationDataTypeDef", {"Value": str}, total=False
)


class ClientSignUpValidationDataTypeDef(
    _RequiredClientSignUpValidationDataTypeDef,
    _OptionalClientSignUpValidationDataTypeDef,
):
    """
    Type definition for `ClientSignUp` `ValidationData`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientStartUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientStartUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientStartUserImportJobResponseUserImportJobTypeDef(
    _ClientStartUserImportJobResponseUserImportJobTypeDef
):
    """
    Type definition for `ClientStartUserImportJobResponse` `UserImportJob`

    The job object that represents the user import job.

    - **JobName** *(string) --*

      The job name for the user import job.

    - **JobId** *(string) --*

      The job ID for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are being imported into.

    - **PreSignedUrl** *(string) --*

      The pre-signed URL to be used to upload the ``.csv`` file.

    - **CreationDate** *(datetime) --*

      The date the user import job was created.

    - **StartDate** *(datetime) --*

      The date when the user import job was started.

    - **CompletionDate** *(datetime) --*

      The date when the user import job was completed.

    - **Status** *(string) --*

      The status of the user import job. One of the following:

      * ``Created`` - The job was created but not started.

      * ``Pending`` - A transition state. You have started the job, but it has not begun
      importing users yet.

      * ``InProgress`` - The job has started, and users are being imported.

      * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

      * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

      * ``Succeeded`` - The job has completed successfully.

      * ``Failed`` - The job has stopped due to an error.

      * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
      associated with the job was deleted, and the job cannot be started.

    - **CloudWatchLogsRoleArn** *(string) --*

      The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
      information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
      Guide.

    - **ImportedUsers** *(integer) --*

      The number of users that were successfully imported.

    - **SkippedUsers** *(integer) --*

      The number of users that were skipped.

    - **FailedUsers** *(integer) --*

      The number of users that could not be imported.

    - **CompletionMessage** *(string) --*

      The message returned when the user import job is completed.
    """


_ClientStartUserImportJobResponseTypeDef = TypedDict(
    "_ClientStartUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStartUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientStartUserImportJobResponseTypeDef(_ClientStartUserImportJobResponseTypeDef):
    """
    Type definition for `ClientStartUserImportJob` `Response`

    Represents the response from the server to the request to start the user import job.

    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.

      - **JobName** *(string) --*

        The job name for the user import job.

      - **JobId** *(string) --*

        The job ID for the user import job.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that the users are being imported into.

      - **PreSignedUrl** *(string) --*

        The pre-signed URL to be used to upload the ``.csv`` file.

      - **CreationDate** *(datetime) --*

        The date the user import job was created.

      - **StartDate** *(datetime) --*

        The date when the user import job was started.

      - **CompletionDate** *(datetime) --*

        The date when the user import job was completed.

      - **Status** *(string) --*

        The status of the user import job. One of the following:

        * ``Created`` - The job was created but not started.

        * ``Pending`` - A transition state. You have started the job, but it has not begun
        importing users yet.

        * ``InProgress`` - The job has started, and users are being imported.

        * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

        * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

        * ``Succeeded`` - The job has completed successfully.

        * ``Failed`` - The job has stopped due to an error.

        * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
        associated with the job was deleted, and the job cannot be started.

      - **CloudWatchLogsRoleArn** *(string) --*

        The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
        information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
        Guide.

      - **ImportedUsers** *(integer) --*

        The number of users that were successfully imported.

      - **SkippedUsers** *(integer) --*

        The number of users that were skipped.

      - **FailedUsers** *(integer) --*

        The number of users that could not be imported.

      - **CompletionMessage** *(string) --*

        The message returned when the user import job is completed.
    """


_ClientStopUserImportJobResponseUserImportJobTypeDef = TypedDict(
    "_ClientStopUserImportJobResponseUserImportJobTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": str,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)


class ClientStopUserImportJobResponseUserImportJobTypeDef(
    _ClientStopUserImportJobResponseUserImportJobTypeDef
):
    """
    Type definition for `ClientStopUserImportJobResponse` `UserImportJob`

    The job object that represents the user import job.

    - **JobName** *(string) --*

      The job name for the user import job.

    - **JobId** *(string) --*

      The job ID for the user import job.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that the users are being imported into.

    - **PreSignedUrl** *(string) --*

      The pre-signed URL to be used to upload the ``.csv`` file.

    - **CreationDate** *(datetime) --*

      The date the user import job was created.

    - **StartDate** *(datetime) --*

      The date when the user import job was started.

    - **CompletionDate** *(datetime) --*

      The date when the user import job was completed.

    - **Status** *(string) --*

      The status of the user import job. One of the following:

      * ``Created`` - The job was created but not started.

      * ``Pending`` - A transition state. You have started the job, but it has not begun
      importing users yet.

      * ``InProgress`` - The job has started, and users are being imported.

      * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

      * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

      * ``Succeeded`` - The job has completed successfully.

      * ``Failed`` - The job has stopped due to an error.

      * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
      associated with the job was deleted, and the job cannot be started.

    - **CloudWatchLogsRoleArn** *(string) --*

      The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
      information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
      Guide.

    - **ImportedUsers** *(integer) --*

      The number of users that were successfully imported.

    - **SkippedUsers** *(integer) --*

      The number of users that were skipped.

    - **FailedUsers** *(integer) --*

      The number of users that could not be imported.

    - **CompletionMessage** *(string) --*

      The message returned when the user import job is completed.
    """


_ClientStopUserImportJobResponseTypeDef = TypedDict(
    "_ClientStopUserImportJobResponseTypeDef",
    {"UserImportJob": ClientStopUserImportJobResponseUserImportJobTypeDef},
    total=False,
)


class ClientStopUserImportJobResponseTypeDef(_ClientStopUserImportJobResponseTypeDef):
    """
    Type definition for `ClientStopUserImportJob` `Response`

    Represents the response from the server to the request to stop the user import job.

    - **UserImportJob** *(dict) --*

      The job object that represents the user import job.

      - **JobName** *(string) --*

        The job name for the user import job.

      - **JobId** *(string) --*

        The job ID for the user import job.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that the users are being imported into.

      - **PreSignedUrl** *(string) --*

        The pre-signed URL to be used to upload the ``.csv`` file.

      - **CreationDate** *(datetime) --*

        The date the user import job was created.

      - **StartDate** *(datetime) --*

        The date when the user import job was started.

      - **CompletionDate** *(datetime) --*

        The date when the user import job was completed.

      - **Status** *(string) --*

        The status of the user import job. One of the following:

        * ``Created`` - The job was created but not started.

        * ``Pending`` - A transition state. You have started the job, but it has not begun
        importing users yet.

        * ``InProgress`` - The job has started, and users are being imported.

        * ``Stopping`` - You have stopped the job, but the job has not stopped importing users yet.

        * ``Stopped`` - You have stopped the job, and the job has stopped importing users.

        * ``Succeeded`` - The job has completed successfully.

        * ``Failed`` - The job has stopped due to an error.

        * ``Expired`` - You created a job, but did not start the job within 24-48 hours. All data
        associated with the job was deleted, and the job cannot be started.

      - **CloudWatchLogsRoleArn** *(string) --*

        The role ARN for the Amazon CloudWatch Logging role for the user import job. For more
        information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer
        Guide.

      - **ImportedUsers** *(integer) --*

        The number of users that were successfully imported.

      - **SkippedUsers** *(integer) --*

        The number of users that were skipped.

      - **FailedUsers** *(integer) --*

        The number of users that could not be imported.

      - **CompletionMessage** *(string) --*

        The message returned when the user import job is completed.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    Type definition for `ClientUpdateGroupResponse` `Group`

    The group object for the group.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
      group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
      not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateGroup` `Response`

    - **Group** *(dict) --*

      The group object for the group.

      - **GroupName** *(string) --*

        The name of the group.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool.

      - **Description** *(string) --*

        A string containing the description of the group.

      - **RoleArn** *(string) --*

        The role ARN for the group.

      - **Precedence** *(integer) --*

        A nonnegative integer value that specifies the precedence of this group relative to the
        other groups that a user can belong to in the user pool. If a user belongs to two or more
        groups, it is the group with the highest precedence whose role ARN will be used in the
        ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
        higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
        or with null ``Precedence`` values.

        Two groups can have the same ``Precedence`` value. If this happens, neither group takes
        precedence over the other. If two groups with the same ``Precedence`` have the same role
        ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in each
        group. If the two groups have different role ARNs, the ``cognito:preferred_role`` claim is
        not set in users' tokens.

        The default ``Precedence`` value is null.

      - **LastModifiedDate** *(datetime) --*

        The date the group was last modified.

      - **CreationDate** *(datetime) --*

        The date the group was created.
    """


_ClientUpdateIdentityProviderResponseIdentityProviderTypeDef = TypedDict(
    "_ClientUpdateIdentityProviderResponseIdentityProviderTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": str,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientUpdateIdentityProviderResponseIdentityProviderTypeDef(
    _ClientUpdateIdentityProviderResponseIdentityProviderTypeDef
):
    """
    Type definition for `ClientUpdateIdentityProviderResponse` `IdentityProvider`

    The identity provider object.

    - **UserPoolId** *(string) --*

      The user pool ID.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **ProviderDetails** *(dict) --*

      The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

      - *(string) --*

        - *(string) --*

    - **AttributeMapping** *(dict) --*

      A mapping of identity provider attributes to standard and custom user pool attributes.

      - *(string) --*

        - *(string) --*

    - **IdpIdentifiers** *(list) --*

      A list of identity provider identifiers.

      - *(string) --*

    - **LastModifiedDate** *(datetime) --*

      The date the identity provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the identity provider was created.
    """


_ClientUpdateIdentityProviderResponseTypeDef = TypedDict(
    "_ClientUpdateIdentityProviderResponseTypeDef",
    {"IdentityProvider": ClientUpdateIdentityProviderResponseIdentityProviderTypeDef},
    total=False,
)


class ClientUpdateIdentityProviderResponseTypeDef(
    _ClientUpdateIdentityProviderResponseTypeDef
):
    """
    Type definition for `ClientUpdateIdentityProvider` `Response`

    - **IdentityProvider** *(dict) --*

      The identity provider object.

      - **UserPoolId** *(string) --*

        The user pool ID.

      - **ProviderName** *(string) --*

        The identity provider name.

      - **ProviderType** *(string) --*

        The identity provider type.

      - **ProviderDetails** *(dict) --*

        The identity provider details, such as ``MetadataURL`` and ``MetadataFile`` .

        - *(string) --*

          - *(string) --*

      - **AttributeMapping** *(dict) --*

        A mapping of identity provider attributes to standard and custom user pool attributes.

        - *(string) --*

          - *(string) --*

      - **IdpIdentifiers** *(list) --*

        A list of identity provider identifiers.

        - *(string) --*

      - **LastModifiedDate** *(datetime) --*

        The date the identity provider was last modified.

      - **CreationDate** *(datetime) --*

        The date the identity provider was created.
    """


_ClientUpdateResourceServerResponseResourceServerScopesTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ClientUpdateResourceServerResponseResourceServerScopesTypeDef(
    _ClientUpdateResourceServerResponseResourceServerScopesTypeDef
):
    """
    Type definition for `ClientUpdateResourceServerResponseResourceServer` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --*

      The name of the scope.

    - **ScopeDescription** *(string) --*

      A description of the scope.
    """


_ClientUpdateResourceServerResponseResourceServerTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseResourceServerTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ClientUpdateResourceServerResponseResourceServerScopesTypeDef],
    },
    total=False,
)


class ClientUpdateResourceServerResponseResourceServerTypeDef(
    _ClientUpdateResourceServerResponseResourceServerTypeDef
):
    """
    Type definition for `ClientUpdateResourceServerResponse` `ResourceServer`

    The resource server.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that hosts the resource server.

    - **Identifier** *(string) --*

      The identifier for the resource server.

    - **Name** *(string) --*

      The name of the resource server.

    - **Scopes** *(list) --*

      A list of scopes that are defined for the resource server.

      - *(dict) --*

        A resource server scope.

        - **ScopeName** *(string) --*

          The name of the scope.

        - **ScopeDescription** *(string) --*

          A description of the scope.
    """


_ClientUpdateResourceServerResponseTypeDef = TypedDict(
    "_ClientUpdateResourceServerResponseTypeDef",
    {"ResourceServer": ClientUpdateResourceServerResponseResourceServerTypeDef},
    total=False,
)


class ClientUpdateResourceServerResponseTypeDef(
    _ClientUpdateResourceServerResponseTypeDef
):
    """
    Type definition for `ClientUpdateResourceServer` `Response`

    - **ResourceServer** *(dict) --*

      The resource server.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool that hosts the resource server.

      - **Identifier** *(string) --*

        The identifier for the resource server.

      - **Name** *(string) --*

        The name of the resource server.

      - **Scopes** *(list) --*

        A list of scopes that are defined for the resource server.

        - *(dict) --*

          A resource server scope.

          - **ScopeName** *(string) --*

            The name of the scope.

          - **ScopeDescription** *(string) --*

            A description of the scope.
    """


_ClientUpdateResourceServerScopesTypeDef = TypedDict(
    "_ClientUpdateResourceServerScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
)


class ClientUpdateResourceServerScopesTypeDef(_ClientUpdateResourceServerScopesTypeDef):
    """
    Type definition for `ClientUpdateResourceServer` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --* **[REQUIRED]**

      The name of the scope.

    - **ScopeDescription** *(string) --* **[REQUIRED]**

      A description of the scope.
    """


_ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef = TypedDict(
    "_ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef",
    {"Destination": str, "DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef(
    _ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef
):
    """
    Type definition for `ClientUpdateUserAttributesResponse` `CodeDeliveryDetailsList`

    The code delivery details being returned from the server.

    - **Destination** *(string) --*

      The destination for the code delivery details.

    - **DeliveryMedium** *(string) --*

      The delivery medium (email message or phone number).

    - **AttributeName** *(string) --*

      The attribute name.
    """


_ClientUpdateUserAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List[
            ClientUpdateUserAttributesResponseCodeDeliveryDetailsListTypeDef
        ]
    },
    total=False,
)


class ClientUpdateUserAttributesResponseTypeDef(
    _ClientUpdateUserAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateUserAttributes` `Response`

    Represents the response from the server for the request to update user attributes.

    - **CodeDeliveryDetailsList** *(list) --*

      The code delivery details list from the server for the request to update user attributes.

      - *(dict) --*

        The code delivery details being returned from the server.

        - **Destination** *(string) --*

          The destination for the code delivery details.

        - **DeliveryMedium** *(string) --*

          The delivery medium (email message or phone number).

        - **AttributeName** *(string) --*

          The attribute name.
    """


_RequiredClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_RequiredClientUpdateUserAttributesUserAttributesTypeDef", {"Name": str}
)
_OptionalClientUpdateUserAttributesUserAttributesTypeDef = TypedDict(
    "_OptionalClientUpdateUserAttributesUserAttributesTypeDef",
    {"Value": str},
    total=False,
)


class ClientUpdateUserAttributesUserAttributesTypeDef(
    _RequiredClientUpdateUserAttributesUserAttributesTypeDef,
    _OptionalClientUpdateUserAttributesUserAttributesTypeDef,
):
    """
    Type definition for `ClientUpdateUserAttributes` `UserAttributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef = TypedDict(
    "_ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)


class ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef(
    _ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolAdminCreateUserConfig` `InviteMessageTemplate`

    The message template to be used for the welcome message to new users.

    See also `Customizing User Invitation Messages
    <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
    .

    - **SMSMessage** *(string) --*

      The message template for SMS messages.

    - **EmailMessage** *(string) --*

      The message template for email messages.

    - **EmailSubject** *(string) --*

      The subject line for email messages.
    """


_ClientUpdateUserPoolAdminCreateUserConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolAdminCreateUserConfigTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": ClientUpdateUserPoolAdminCreateUserConfigInviteMessageTemplateTypeDef,
    },
    total=False,
)


class ClientUpdateUserPoolAdminCreateUserConfigTypeDef(
    _ClientUpdateUserPoolAdminCreateUserConfigTypeDef
):
    """
    Type definition for `ClientUpdateUserPool` `AdminCreateUserConfig`

    The configuration for ``AdminCreateUser`` requests.

    - **AllowAdminCreateUserOnly** *(boolean) --*

      Set to ``True`` if only the administrator is allowed to create user profiles. Set to ``False``
      if users can sign themselves up via an app.

    - **UnusedAccountValidityDays** *(integer) --*

      The user account expiration limit, in days, after which the account is no longer usable. To
      reset the account after that time limit, you must call ``AdminCreateUser`` again, specifying
      ``"RESEND"`` for the ``MessageAction`` parameter. The default value for this parameter is 7.

      .. note::

        If you set a value for ``TemporaryPasswordValidityDays`` in ``PasswordPolicy`` , that value
        will be used and ``UnusedAccountValidityDays`` will be deprecated for that user pool.

    - **InviteMessageTemplate** *(dict) --*

      The message template to be used for the welcome message to new users.

      See also `Customizing User Invitation Messages
      <https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization>`__
      .

      - **SMSMessage** *(string) --*

        The message template for SMS messages.

      - **EmailMessage** *(string) --*

        The message template for email messages.

      - **EmailSubject** *(string) --*

        The subject line for email messages.
    """


_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str},
)
_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef",
    {"UserDataShared": bool},
    total=False,
)


class ClientUpdateUserPoolClientAnalyticsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolClientAnalyticsConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateUserPoolClient` `AnalyticsConfiguration`

    The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.

    - **ApplicationId** *(string) --* **[REQUIRED]**

      The application ID for an Amazon Pinpoint application.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint
      analytics.

    - **ExternalId** *(string) --* **[REQUIRED]**

      The external ID.

    - **UserDataShared** *(boolean) --*

      If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events it
      publishes to Amazon Pinpoint analytics.
    """


_ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef",
    {"ApplicationId": str, "RoleArn": str, "ExternalId": str, "UserDataShared": bool},
    total=False,
)


class ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef(
    _ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolClientResponseUserPoolClient` `AnalyticsConfiguration`

    The Amazon Pinpoint analytics configuration for the user pool client.

    - **ApplicationId** *(string) --*

      The application ID for an Amazon Pinpoint application.

    - **RoleArn** *(string) --*

      The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
      Pinpoint analytics.

    - **ExternalId** *(string) --*

      The external ID.

    - **UserDataShared** *(boolean) --*

      If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
      it publishes to Amazon Pinpoint analytics.
    """


_ClientUpdateUserPoolClientResponseUserPoolClientTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseUserPoolClientTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[str],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[str],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": ClientUpdateUserPoolClientResponseUserPoolClientAnalyticsConfigurationTypeDef,
        "PreventUserExistenceErrors": str,
    },
    total=False,
)


class ClientUpdateUserPoolClientResponseUserPoolClientTypeDef(
    _ClientUpdateUserPoolClientResponseUserPoolClientTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolClientResponse` `UserPoolClient`

    The user pool client value from the response from the server when an update user pool client
    request is made.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool client.

    - **ClientName** *(string) --*

      The client name from the user pool request of the client type.

    - **ClientId** *(string) --*

      The ID of the client associated with the user pool.

    - **ClientSecret** *(string) --*

      The client secret from the user pool request of the client type.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool client was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool client was created.

    - **RefreshTokenValidity** *(integer) --*

      The time limit, in days, after which the refresh token is no longer valid and cannot be
      used.

    - **ReadAttributes** *(list) --*

      The Read-only attributes.

      - *(string) --*

    - **WriteAttributes** *(list) --*

      The writeable attributes.

      - *(string) --*

    - **ExplicitAuthFlows** *(list) --*

      The authentication flows that are supported by the user pool clients. Flow names without
      the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
      that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
      prefix.

      Valid values include:

      * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
      ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
      With this authentication flow, Cognito receives the password in the request instead of
      using the SRP (Secure Remote Password protocol) protocol to verify passwords.

      * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

      * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
      Cognito receives the password in the request instead of using the SRP protocol to verify
      passwords.

      * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

      * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

      - *(string) --*

    - **SupportedIdentityProviders** *(list) --*

      A list of provider names for the identity providers that are supported on this client.

      - *(string) --*

    - **CallbackURLs** *(list) --*

      A list of allowed redirect (callback) URLs for the identity providers.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

      - *(string) --*

    - **LogoutURLs** *(list) --*

      A list of allowed logout URLs for the identity providers.

      - *(string) --*

    - **DefaultRedirectURI** *(string) --*

      The default redirect URI. Must be in the ``CallbackURLs`` list.

      A redirect URI must:

      * Be an absolute URI.

      * Be registered with the authorization server.

      * Not include a fragment component.

      See `OAuth 2.0 - Redirection Endpoint
      <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

      Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
      only.

      App callback URLs such as myapp://example are also supported.

    - **AllowedOAuthFlows** *(list) --*

      Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
      response. This code can be exchanged for access tokens with the token endpoint.

      Set to ``token`` to specify that the client should get the access token (and, optionally,
      ID token, based on scopes) directly.

      - *(string) --*

    - **AllowedOAuthScopes** *(list) --*

      A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
      ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
      created in Resource Servers are also supported.

      - *(string) --*

    - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

      Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
      Cognito user pools.

    - **AnalyticsConfiguration** *(dict) --*

      The Amazon Pinpoint analytics configuration for the user pool client.

      - **ApplicationId** *(string) --*

        The application ID for an Amazon Pinpoint application.

      - **RoleArn** *(string) --*

        The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
        Pinpoint analytics.

      - **ExternalId** *(string) --*

        The external ID.

      - **UserDataShared** *(boolean) --*

        If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
        it publishes to Amazon Pinpoint analytics.

    - **PreventUserExistenceErrors** *(string) --*

      Use this setting to choose which errors and responses are returned by Cognito APIs during
      authentication, account confirmation, and password recovery when the user does not exist in
      the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
      an error indicating either the username or password was incorrect, and account confirmation
      and password recovery return a response indicating a code was sent to a simulated
      destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
      exception if the user does not exist in the user pool.

      Valid values include:

      * ``ENABLED`` - This prevents user existence-related errors.

      * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
      errors are not prevented.

      This setting affects the behavior of following APIs:

      *  AdminInitiateAuth

      *  AdminRespondToAuthChallenge

      *  InitiateAuth

      *  RespondToAuthChallenge

      *  ForgotPassword

      *  ConfirmForgotPassword

      *  ConfirmSignUp

      *  ResendConfirmationCode

      .. note::

        After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
        ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientUpdateUserPoolClientResponseTypeDef = TypedDict(
    "_ClientUpdateUserPoolClientResponseTypeDef",
    {"UserPoolClient": ClientUpdateUserPoolClientResponseUserPoolClientTypeDef},
    total=False,
)


class ClientUpdateUserPoolClientResponseTypeDef(
    _ClientUpdateUserPoolClientResponseTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolClient` `Response`

    Represents the response from the server to the request to update the user pool client.

    - **UserPoolClient** *(dict) --*

      The user pool client value from the response from the server when an update user pool client
      request is made.

      - **UserPoolId** *(string) --*

        The user pool ID for the user pool client.

      - **ClientName** *(string) --*

        The client name from the user pool request of the client type.

      - **ClientId** *(string) --*

        The ID of the client associated with the user pool.

      - **ClientSecret** *(string) --*

        The client secret from the user pool request of the client type.

      - **LastModifiedDate** *(datetime) --*

        The date the user pool client was last modified.

      - **CreationDate** *(datetime) --*

        The date the user pool client was created.

      - **RefreshTokenValidity** *(integer) --*

        The time limit, in days, after which the refresh token is no longer valid and cannot be
        used.

      - **ReadAttributes** *(list) --*

        The Read-only attributes.

        - *(string) --*

      - **WriteAttributes** *(list) --*

        The writeable attributes.

        - *(string) --*

      - **ExplicitAuthFlows** *(list) --*

        The authentication flows that are supported by the user pool clients. Flow names without
        the ``ALLOW_`` prefix are deprecated in favor of new names with the ``ALLOW_`` prefix. Note
        that values with ``ALLOW_`` prefix cannot be used along with values without ``ALLOW_``
        prefix.

        Valid values include:

        * ``ALLOW_ADMIN_USER_PASSWORD_AUTH`` : Enable admin based user password authentication flow
        ``ADMIN_USER_PASSWORD_AUTH`` . This setting replaces the ``ADMIN_NO_SRP_AUTH`` setting.
        With this authentication flow, Cognito receives the password in the request instead of
        using the SRP (Secure Remote Password protocol) protocol to verify passwords.

        * ``ALLOW_CUSTOM_AUTH`` : Enable Lambda trigger based authentication.

        * ``ALLOW_USER_PASSWORD_AUTH`` : Enable user password-based authentication. In this flow,
        Cognito receives the password in the request instead of using the SRP protocol to verify
        passwords.

        * ``ALLOW_USER_SRP_AUTH`` : Enable SRP based authentication.

        * ``ALLOW_REFRESH_TOKEN_AUTH`` : Enable authflow to refresh tokens.

        - *(string) --*

      - **SupportedIdentityProviders** *(list) --*

        A list of provider names for the identity providers that are supported on this client.

        - *(string) --*

      - **CallbackURLs** *(list) --*

        A list of allowed redirect (callback) URLs for the identity providers.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

        - *(string) --*

      - **LogoutURLs** *(list) --*

        A list of allowed logout URLs for the identity providers.

        - *(string) --*

      - **DefaultRedirectURI** *(string) --*

        The default redirect URI. Must be in the ``CallbackURLs`` list.

        A redirect URI must:

        * Be an absolute URI.

        * Be registered with the authorization server.

        * Not include a fragment component.

        See `OAuth 2.0 - Redirection Endpoint
        <https://tools.ietf.org/html/rfc6749#section-3.1.2>`__ .

        Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes
        only.

        App callback URLs such as myapp://example are also supported.

      - **AllowedOAuthFlows** *(list) --*

        Set to ``code`` to initiate a code grant flow, which provides an authorization code as the
        response. This code can be exchanged for access tokens with the token endpoint.

        Set to ``token`` to specify that the client should get the access token (and, optionally,
        ID token, based on scopes) directly.

        - *(string) --*

      - **AllowedOAuthScopes** *(list) --*

        A list of allowed ``OAuth`` scopes. Currently supported values are ``"phone"`` ,
        ``"email"`` , ``"openid"`` , and ``"Cognito"`` . In addition to these values, custom scopes
        created in Resource Servers are also supported.

        - *(string) --*

      - **AllowedOAuthFlowsUserPoolClient** *(boolean) --*

        Set to TRUE if the client is allowed to follow the OAuth protocol when interacting with
        Cognito user pools.

      - **AnalyticsConfiguration** *(dict) --*

        The Amazon Pinpoint analytics configuration for the user pool client.

        - **ApplicationId** *(string) --*

          The application ID for an Amazon Pinpoint application.

        - **RoleArn** *(string) --*

          The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon
          Pinpoint analytics.

        - **ExternalId** *(string) --*

          The external ID.

        - **UserDataShared** *(boolean) --*

          If ``UserDataShared`` is ``true`` , Amazon Cognito will include user data in the events
          it publishes to Amazon Pinpoint analytics.

      - **PreventUserExistenceErrors** *(string) --*

        Use this setting to choose which errors and responses are returned by Cognito APIs during
        authentication, account confirmation, and password recovery when the user does not exist in
        the user pool. When set to ``ENABLED`` and the user does not exist, authentication returns
        an error indicating either the username or password was incorrect, and account confirmation
        and password recovery return a response indicating a code was sent to a simulated
        destination. When set to ``LEGACY`` , those APIs will return a ``UserNotFoundException``
        exception if the user does not exist in the user pool.

        Valid values include:

        * ``ENABLED`` - This prevents user existence-related errors.

        * ``LEGACY`` - This represents the old behavior of Cognito where user existence related
        errors are not prevented.

        This setting affects the behavior of following APIs:

        *  AdminInitiateAuth

        *  AdminRespondToAuthChallenge

        *  InitiateAuth

        *  RespondToAuthChallenge

        *  ForgotPassword

        *  ConfirmForgotPassword

        *  ConfirmSignUp

        *  ResendConfirmationCode

        .. note::

          After January 1st 2020, the value of ``PreventUserExistenceErrors`` will default to
          ``ENABLED`` for newly created user pool clients if no value is provided.
    """


_ClientUpdateUserPoolDeviceConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolDeviceConfigurationTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)


class ClientUpdateUserPoolDeviceConfigurationTypeDef(
    _ClientUpdateUserPoolDeviceConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateUserPool` `DeviceConfiguration`

    Device configuration.

    - **ChallengeRequiredOnNewDevice** *(boolean) --*

      Indicates whether a challenge is required on a new device. Only applicable to a new device.

    - **DeviceOnlyRememberedOnUserPrompt** *(boolean) --*

      If true, a device is only remembered on user prompt.
    """


_ClientUpdateUserPoolDomainCustomDomainConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolDomainCustomDomainConfigTypeDef", {"CertificateArn": str}
)


class ClientUpdateUserPoolDomainCustomDomainConfigTypeDef(
    _ClientUpdateUserPoolDomainCustomDomainConfigTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolDomain` `CustomDomainConfig`

    The configuration for a custom domain that hosts the sign-up and sign-in pages for your
    application. Use this object to specify an SSL certificate that is managed by ACM.

    - **CertificateArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this
      certificate for the subdomain of your custom domain.
    """


_ClientUpdateUserPoolDomainResponseTypeDef = TypedDict(
    "_ClientUpdateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)


class ClientUpdateUserPoolDomainResponseTypeDef(
    _ClientUpdateUserPoolDomainResponseTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolDomain` `Response`

    The UpdateUserPoolDomain response output.

    - **CloudFrontDomain** *(string) --*

      The Amazon CloudFront endpoint that Amazon Cognito set up when you added the custom domain to
      your user pool.
    """


_ClientUpdateUserPoolEmailConfigurationTypeDef = TypedDict(
    "_ClientUpdateUserPoolEmailConfigurationTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": str,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)


class ClientUpdateUserPoolEmailConfigurationTypeDef(
    _ClientUpdateUserPoolEmailConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateUserPool` `EmailConfiguration`

    Email configuration.

    - **SourceArn** *(string) --*

      The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is
      used in one of the following ways, depending on the value that you specify for the
      ``EmailSendingAccount`` parameter:

      * If you specify ``COGNITO_DEFAULT`` , Amazon Cognito uses this address as the custom FROM
      address when it emails your users by using its built-in email account.

      * If you specify ``DEVELOPER`` , Amazon Cognito emails your users with this address by calling
      Amazon SES on your behalf.

    - **ReplyToEmailAddress** *(string) --*

      The destination to which the receiver of the email should reply to.

    - **EmailSendingAccount** *(string) --*

      Specifies whether Amazon Cognito emails your users by using its built-in email functionality or
      your Amazon SES email configuration. Specify one of the following values:

        COGNITO_DEFAULT

      When Amazon Cognito emails your users, it uses its built-in email functionality. When you use
      the default option, Amazon Cognito allows only a limited number of emails each day for your
      user pool. For typical production environments, the default email limit is below the required
      delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES
      email configuration.

      To look up the email delivery limit for the default option, see `Limits in Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html>`__ in the *Amazon
      Cognito Developer Guide* .

      The default FROM address is no-reply@verificationemail.com. To customize the FROM address,
      provide the ARN of an Amazon SES verified email address for the ``SourceArn`` parameter.

        DEVELOPER

      When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito
      calls Amazon SES on your behalf to send email from your verified email address. When you use
      this option, the email delivery limits are the same limits that apply to your Amazon SES
      verified email address in your AWS account.

      If you use this option, you must provide the ARN of an Amazon SES verified email address for
      the ``SourceArn`` parameter.

      Before Amazon Cognito can email your users, it requires additional permissions to call Amazon
      SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a
      *service-linked role* , which is a type of IAM role, in your AWS account. This role contains
      the permissions that allow Amazon Cognito to access Amazon SES and send email messages with
      your address. For more information about the service-linked role that Amazon Cognito creates,
      see `Using Service-Linked Roles for Amazon Cognito
      <https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html>`__
      in the *Amazon Cognito Developer Guide* .

    - **From** *(string) --*

      Identifies either the sender’s email address or the sender’s name with their email address. For
      example, ``testuser@example.com`` or ``Test User <testuser@example.com>`` . This address will
      appear before the body of the email.

    - **ConfigurationSet** *(string) --*

      The set of configuration rules that can be applied to emails sent using Amazon SES. A
      configuration set is applied to an email by including a reference to the configuration set in
      the headers of the email. Once applied, all of the rules in that configuration set are applied
      to the email. Configuration sets can be used to apply the following types of rules to emails:

      * Event publishing – Amazon SES can track the number of send, delivery, open, click, bounce,
      and complaint events for each email sent. Use event publishing to send information about these
      events to other AWS services such as SNS and CloudWatch.

      * IP pool management – When leasing dedicated IP addresses with Amazon SES, you can create
      groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP
      pools with configuration sets.
    """


_ClientUpdateUserPoolLambdaConfigTypeDef = TypedDict(
    "_ClientUpdateUserPoolLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ClientUpdateUserPoolLambdaConfigTypeDef(_ClientUpdateUserPoolLambdaConfigTypeDef):
    """
    Type definition for `ClientUpdateUserPool` `LambdaConfig`

    The AWS Lambda configuration information from the request to update the user pool.

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef = TypedDict(
    "_ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)


class ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef(
    _ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef
):
    """
    Type definition for `ClientUpdateUserPoolPolicies` `PasswordPolicy`

    The password policy.

    - **MinimumLength** *(integer) --*

      The minimum length of the password policy that you have set. Cannot be less than 6.

    - **RequireUppercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one uppercase letter in their password.

    - **RequireLowercase** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one lowercase letter in their password.

    - **RequireNumbers** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one number in their password.

    - **RequireSymbols** *(boolean) --*

      In the password policy that you have set, refers to whether you have required users to use at
      least one symbol in their password.

    - **TemporaryPasswordValidityDays** *(integer) --*

      In the password policy you have set, refers to the number of days a temporary password is
      valid. If the user does not sign-in during this time, their password will need to be reset by
      an administrator.

      .. note::

        When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be able
        to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_ClientUpdateUserPoolPoliciesTypeDef = TypedDict(
    "_ClientUpdateUserPoolPoliciesTypeDef",
    {"PasswordPolicy": ClientUpdateUserPoolPoliciesPasswordPolicyTypeDef},
    total=False,
)


class ClientUpdateUserPoolPoliciesTypeDef(_ClientUpdateUserPoolPoliciesTypeDef):
    """
    Type definition for `ClientUpdateUserPool` `Policies`

    A container with the policies you wish to update in a user pool.

    - **PasswordPolicy** *(dict) --*

      The password policy.

      - **MinimumLength** *(integer) --*

        The minimum length of the password policy that you have set. Cannot be less than 6.

      - **RequireUppercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one uppercase letter in their password.

      - **RequireLowercase** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one lowercase letter in their password.

      - **RequireNumbers** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one number in their password.

      - **RequireSymbols** *(boolean) --*

        In the password policy that you have set, refers to whether you have required users to use at
        least one symbol in their password.

      - **TemporaryPasswordValidityDays** *(integer) --*

        In the password policy you have set, refers to the number of days a temporary password is
        valid. If the user does not sign-in during this time, their password will need to be reset by
        an administrator.

        .. note::

          When you set ``TemporaryPasswordValidityDays`` for a user pool, you will no longer be able
          to set the deprecated ``UnusedAccountValidityDays`` value for that user pool.
    """


_RequiredClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateUserPoolSmsConfigurationTypeDef", {"SnsCallerArn": str}
)
_OptionalClientUpdateUserPoolSmsConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateUserPoolSmsConfigurationTypeDef",
    {"ExternalId": str},
    total=False,
)


class ClientUpdateUserPoolSmsConfigurationTypeDef(
    _RequiredClientUpdateUserPoolSmsConfigurationTypeDef,
    _OptionalClientUpdateUserPoolSmsConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateUserPool` `SmsConfiguration`

    SMS configuration.

    - **SnsCallerArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is
      the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

    - **ExternalId** *(string) --*

      The external ID is a value that we recommend you use to add security to your IAM role which is
      used to call Amazon SNS to send SMS messages for your user pool. If you provide an
      ``ExternalId`` , the Cognito User Pool will include it when attempting to assume your IAM role,
      so that you can set your roles trust policy to require the ``ExternalID`` . If you use the
      Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the
      required permissions and a trust policy that demonstrates use of the ``ExternalId`` .
    """


_ClientUpdateUserPoolUserPoolAddOnsTypeDef = TypedDict(
    "_ClientUpdateUserPoolUserPoolAddOnsTypeDef", {"AdvancedSecurityMode": str}
)


class ClientUpdateUserPoolUserPoolAddOnsTypeDef(
    _ClientUpdateUserPoolUserPoolAddOnsTypeDef
):
    """
    Type definition for `ClientUpdateUserPool` `UserPoolAddOns`

    Used to enable advanced security risk detection. Set the key ``AdvancedSecurityMode`` to the
    value "AUDIT".

    - **AdvancedSecurityMode** *(string) --* **[REQUIRED]**

      The advanced security mode.
    """


_ClientUpdateUserPoolVerificationMessageTemplateTypeDef = TypedDict(
    "_ClientUpdateUserPoolVerificationMessageTemplateTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": str,
    },
    total=False,
)


class ClientUpdateUserPoolVerificationMessageTemplateTypeDef(
    _ClientUpdateUserPoolVerificationMessageTemplateTypeDef
):
    """
    Type definition for `ClientUpdateUserPool` `VerificationMessageTemplate`

    The template for verification messages.

    - **SmsMessage** *(string) --*

      The SMS message template.

    - **EmailMessage** *(string) --*

      The email message template.

    - **EmailSubject** *(string) --*

      The subject line for the email message template.

    - **EmailMessageByLink** *(string) --*

      The email message template for sending a confirmation link to the user.

    - **EmailSubjectByLink** *(string) --*

      The subject line for the email message template for sending a confirmation link to the user.

    - **DefaultEmailOption** *(string) --*

      The default email option.
    """


_ClientVerifySoftwareTokenResponseTypeDef = TypedDict(
    "_ClientVerifySoftwareTokenResponseTypeDef",
    {"Status": str, "Session": str},
    total=False,
)


class ClientVerifySoftwareTokenResponseTypeDef(
    _ClientVerifySoftwareTokenResponseTypeDef
):
    """
    Type definition for `ClientVerifySoftwareToken` `Response`

    - **Status** *(string) --*

      The status of the verify software token.

    - **Session** *(string) --*

      The session which should be passed both ways in challenge-response calls to the service.
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
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    Type definition for `ListGroupsPaginateResponse` `Groups`

    The group type.

    - **GroupName** *(string) --*

      The name of the group.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool.

    - **Description** *(string) --*

      A string containing the description of the group.

    - **RoleArn** *(string) --*

      The role ARN for the group.

    - **Precedence** *(integer) --*

      A nonnegative integer value that specifies the precedence of this group relative to the
      other groups that a user can belong to in the user pool. If a user belongs to two or more
      groups, it is the group with the highest precedence whose role ARN will be used in the
      ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
      higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
      or with null ``Precedence`` values.

      Two groups can have the same ``Precedence`` value. If this happens, neither group takes
      precedence over the other. If two groups with the same ``Precedence`` have the same role
      ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
      each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
      claim is not set in users' tokens.

      The default ``Precedence`` value is null.

    - **LastModifiedDate** *(datetime) --*

      The date the group was last modified.

    - **CreationDate** *(datetime) --*

      The date the group was created.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListGroupsPaginate` `Response`

    - **Groups** *(list) --*

      The group objects for the groups.

      - *(dict) --*

        The group type.

        - **GroupName** *(string) --*

          The name of the group.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool.

        - **Description** *(string) --*

          A string containing the description of the group.

        - **RoleArn** *(string) --*

          The role ARN for the group.

        - **Precedence** *(integer) --*

          A nonnegative integer value that specifies the precedence of this group relative to the
          other groups that a user can belong to in the user pool. If a user belongs to two or more
          groups, it is the group with the highest precedence whose role ARN will be used in the
          ``cognito:roles`` and ``cognito:preferred_role`` claims in the user's tokens. Groups with
          higher ``Precedence`` values take precedence over groups with lower ``Precedence`` values
          or with null ``Precedence`` values.

          Two groups can have the same ``Precedence`` value. If this happens, neither group takes
          precedence over the other. If two groups with the same ``Precedence`` have the same role
          ARN, that role is used in the ``cognito:preferred_role`` claim in tokens for users in
          each group. If the two groups have different role ARNs, the ``cognito:preferred_role``
          claim is not set in users' tokens.

          The default ``Precedence`` value is null.

        - **LastModifiedDate** *(datetime) --*

          The date the group was last modified.

        - **CreationDate** *(datetime) --*

          The date the group was created.
    """


_ListIdentityProvidersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentityProvidersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentityProvidersPaginatePaginationConfigTypeDef(
    _ListIdentityProvidersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIdentityProvidersPaginate` `PaginationConfig`

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


_ListIdentityProvidersPaginateResponseProvidersTypeDef = TypedDict(
    "_ListIdentityProvidersPaginateResponseProvidersTypeDef",
    {
        "ProviderName": str,
        "ProviderType": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListIdentityProvidersPaginateResponseProvidersTypeDef(
    _ListIdentityProvidersPaginateResponseProvidersTypeDef
):
    """
    Type definition for `ListIdentityProvidersPaginateResponse` `Providers`

    A container for identity provider details.

    - **ProviderName** *(string) --*

      The identity provider name.

    - **ProviderType** *(string) --*

      The identity provider type.

    - **LastModifiedDate** *(datetime) --*

      The date the provider was last modified.

    - **CreationDate** *(datetime) --*

      The date the provider was added to the user pool.
    """


_ListIdentityProvidersPaginateResponseTypeDef = TypedDict(
    "_ListIdentityProvidersPaginateResponseTypeDef",
    {"Providers": List[ListIdentityProvidersPaginateResponseProvidersTypeDef]},
    total=False,
)


class ListIdentityProvidersPaginateResponseTypeDef(
    _ListIdentityProvidersPaginateResponseTypeDef
):
    """
    Type definition for `ListIdentityProvidersPaginate` `Response`

    - **Providers** *(list) --*

      A list of identity provider objects.

      - *(dict) --*

        A container for identity provider details.

        - **ProviderName** *(string) --*

          The identity provider name.

        - **ProviderType** *(string) --*

          The identity provider type.

        - **LastModifiedDate** *(datetime) --*

          The date the provider was last modified.

        - **CreationDate** *(datetime) --*

          The date the provider was added to the user pool.
    """


_ListResourceServersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceServersPaginatePaginationConfigTypeDef(
    _ListResourceServersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceServersPaginate` `PaginationConfig`

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


_ListResourceServersPaginateResponseResourceServersScopesTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseResourceServersScopesTypeDef",
    {"ScopeName": str, "ScopeDescription": str},
    total=False,
)


class ListResourceServersPaginateResponseResourceServersScopesTypeDef(
    _ListResourceServersPaginateResponseResourceServersScopesTypeDef
):
    """
    Type definition for `ListResourceServersPaginateResponseResourceServers` `Scopes`

    A resource server scope.

    - **ScopeName** *(string) --*

      The name of the scope.

    - **ScopeDescription** *(string) --*

      A description of the scope.
    """


_ListResourceServersPaginateResponseResourceServersTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseResourceServersTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List[ListResourceServersPaginateResponseResourceServersScopesTypeDef],
    },
    total=False,
)


class ListResourceServersPaginateResponseResourceServersTypeDef(
    _ListResourceServersPaginateResponseResourceServersTypeDef
):
    """
    Type definition for `ListResourceServersPaginateResponse` `ResourceServers`

    A container for information about a resource server for a user pool.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool that hosts the resource server.

    - **Identifier** *(string) --*

      The identifier for the resource server.

    - **Name** *(string) --*

      The name of the resource server.

    - **Scopes** *(list) --*

      A list of scopes that are defined for the resource server.

      - *(dict) --*

        A resource server scope.

        - **ScopeName** *(string) --*

          The name of the scope.

        - **ScopeDescription** *(string) --*

          A description of the scope.
    """


_ListResourceServersPaginateResponseTypeDef = TypedDict(
    "_ListResourceServersPaginateResponseTypeDef",
    {
        "ResourceServers": List[
            ListResourceServersPaginateResponseResourceServersTypeDef
        ]
    },
    total=False,
)


class ListResourceServersPaginateResponseTypeDef(
    _ListResourceServersPaginateResponseTypeDef
):
    """
    Type definition for `ListResourceServersPaginate` `Response`

    - **ResourceServers** *(list) --*

      The resource servers.

      - *(dict) --*

        A container for information about a resource server for a user pool.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool that hosts the resource server.

        - **Identifier** *(string) --*

          The identifier for the resource server.

        - **Name** *(string) --*

          The name of the resource server.

        - **Scopes** *(list) --*

          A list of scopes that are defined for the resource server.

          - *(dict) --*

            A resource server scope.

            - **ScopeName** *(string) --*

              The name of the scope.

            - **ScopeDescription** *(string) --*

              A description of the scope.
    """


_ListUserPoolClientsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoolClientsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoolClientsPaginatePaginationConfigTypeDef(
    _ListUserPoolClientsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUserPoolClientsPaginate` `PaginationConfig`

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


_ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef = TypedDict(
    "_ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)


class ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef(
    _ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef
):
    """
    Type definition for `ListUserPoolClientsPaginateResponse` `UserPoolClients`

    The description of the user pool client.

    - **ClientId** *(string) --*

      The ID of the client associated with the user pool.

    - **UserPoolId** *(string) --*

      The user pool ID for the user pool where you want to describe the user pool client.

    - **ClientName** *(string) --*

      The client name from the user pool client description.
    """


_ListUserPoolClientsPaginateResponseTypeDef = TypedDict(
    "_ListUserPoolClientsPaginateResponseTypeDef",
    {
        "UserPoolClients": List[
            ListUserPoolClientsPaginateResponseUserPoolClientsTypeDef
        ]
    },
    total=False,
)


class ListUserPoolClientsPaginateResponseTypeDef(
    _ListUserPoolClientsPaginateResponseTypeDef
):
    """
    Type definition for `ListUserPoolClientsPaginate` `Response`

    Represents the response from the server that lists user pool clients.

    - **UserPoolClients** *(list) --*

      The user pool clients in the response that lists user pool clients.

      - *(dict) --*

        The description of the user pool client.

        - **ClientId** *(string) --*

          The ID of the client associated with the user pool.

        - **UserPoolId** *(string) --*

          The user pool ID for the user pool where you want to describe the user pool client.

        - **ClientName** *(string) --*

          The client name from the user pool client description.
    """


_ListUserPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserPoolsPaginatePaginationConfigTypeDef(
    _ListUserPoolsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUserPoolsPaginate` `PaginationConfig`

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


_ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
    },
    total=False,
)


class ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef(
    _ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef
):
    """
    Type definition for `ListUserPoolsPaginateResponseUserPools` `LambdaConfig`

    The AWS Lambda configuration information in a user pool description.

    - **PreSignUp** *(string) --*

      A pre-registration AWS Lambda trigger.

    - **CustomMessage** *(string) --*

      A custom Message AWS Lambda trigger.

    - **PostConfirmation** *(string) --*

      A post-confirmation AWS Lambda trigger.

    - **PreAuthentication** *(string) --*

      A pre-authentication AWS Lambda trigger.

    - **PostAuthentication** *(string) --*

      A post-authentication AWS Lambda trigger.

    - **DefineAuthChallenge** *(string) --*

      Defines the authentication challenge.

    - **CreateAuthChallenge** *(string) --*

      Creates an authentication challenge.

    - **VerifyAuthChallengeResponse** *(string) --*

      Verifies the authentication challenge response.

    - **PreTokenGeneration** *(string) --*

      A Lambda trigger that is invoked before token generation.

    - **UserMigration** *(string) --*

      The user migration Lambda config type.
    """


_ListUserPoolsPaginateResponseUserPoolsTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseUserPoolsTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": ListUserPoolsPaginateResponseUserPoolsLambdaConfigTypeDef,
        "Status": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)


class ListUserPoolsPaginateResponseUserPoolsTypeDef(
    _ListUserPoolsPaginateResponseUserPoolsTypeDef
):
    """
    Type definition for `ListUserPoolsPaginateResponse` `UserPools`

    A user pool description.

    - **Id** *(string) --*

      The ID in a user pool description.

    - **Name** *(string) --*

      The name in a user pool description.

    - **LambdaConfig** *(dict) --*

      The AWS Lambda configuration information in a user pool description.

      - **PreSignUp** *(string) --*

        A pre-registration AWS Lambda trigger.

      - **CustomMessage** *(string) --*

        A custom Message AWS Lambda trigger.

      - **PostConfirmation** *(string) --*

        A post-confirmation AWS Lambda trigger.

      - **PreAuthentication** *(string) --*

        A pre-authentication AWS Lambda trigger.

      - **PostAuthentication** *(string) --*

        A post-authentication AWS Lambda trigger.

      - **DefineAuthChallenge** *(string) --*

        Defines the authentication challenge.

      - **CreateAuthChallenge** *(string) --*

        Creates an authentication challenge.

      - **VerifyAuthChallengeResponse** *(string) --*

        Verifies the authentication challenge response.

      - **PreTokenGeneration** *(string) --*

        A Lambda trigger that is invoked before token generation.

      - **UserMigration** *(string) --*

        The user migration Lambda config type.

    - **Status** *(string) --*

      The user pool status in a user pool description.

    - **LastModifiedDate** *(datetime) --*

      The date the user pool description was last modified.

    - **CreationDate** *(datetime) --*

      The date the user pool description was created.
    """


_ListUserPoolsPaginateResponseTypeDef = TypedDict(
    "_ListUserPoolsPaginateResponseTypeDef",
    {"UserPools": List[ListUserPoolsPaginateResponseUserPoolsTypeDef]},
    total=False,
)


class ListUserPoolsPaginateResponseTypeDef(_ListUserPoolsPaginateResponseTypeDef):
    """
    Type definition for `ListUserPoolsPaginate` `Response`

    Represents the response to list user pools.

    - **UserPools** *(list) --*

      The user pools from the response to list users.

      - *(dict) --*

        A user pool description.

        - **Id** *(string) --*

          The ID in a user pool description.

        - **Name** *(string) --*

          The name in a user pool description.

        - **LambdaConfig** *(dict) --*

          The AWS Lambda configuration information in a user pool description.

          - **PreSignUp** *(string) --*

            A pre-registration AWS Lambda trigger.

          - **CustomMessage** *(string) --*

            A custom Message AWS Lambda trigger.

          - **PostConfirmation** *(string) --*

            A post-confirmation AWS Lambda trigger.

          - **PreAuthentication** *(string) --*

            A pre-authentication AWS Lambda trigger.

          - **PostAuthentication** *(string) --*

            A post-authentication AWS Lambda trigger.

          - **DefineAuthChallenge** *(string) --*

            Defines the authentication challenge.

          - **CreateAuthChallenge** *(string) --*

            Creates an authentication challenge.

          - **VerifyAuthChallengeResponse** *(string) --*

            Verifies the authentication challenge response.

          - **PreTokenGeneration** *(string) --*

            A Lambda trigger that is invoked before token generation.

          - **UserMigration** *(string) --*

            The user migration Lambda config type.

        - **Status** *(string) --*

          The user pool status in a user pool description.

        - **LastModifiedDate** *(datetime) --*

          The date the user pool description was last modified.

        - **CreationDate** *(datetime) --*

          The date the user pool description was created.
    """


_ListUsersInGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersInGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersInGroupPaginatePaginationConfigTypeDef(
    _ListUsersInGroupPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsersInGroupPaginate` `PaginationConfig`

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


_ListUsersInGroupPaginateResponseUsersAttributesTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListUsersInGroupPaginateResponseUsersAttributesTypeDef(
    _ListUsersInGroupPaginateResponseUsersAttributesTypeDef
):
    """
    Type definition for `ListUsersInGroupPaginateResponseUsers` `Attributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef(
    _ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef
):
    """
    Type definition for `ListUsersInGroupPaginateResponseUsers` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA
     configurations. You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
    responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ListUsersInGroupPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ListUsersInGroupPaginateResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ListUsersInGroupPaginateResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ListUsersInGroupPaginateResponseUsersTypeDef(
    _ListUsersInGroupPaginateResponseUsersTypeDef
):
    """
    Type definition for `ListUsersInGroupPaginateResponse` `Users`

    The user type.

    - **Username** *(string) --*

      The user name of the user you wish to describe.

    - **Attributes** *(list) --*

      A container with information about the user type attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The creation date of the user.

    - **UserLastModifiedDate** *(datetime) --*

      The last modified date of the user.

    - **Enabled** *(boolean) --*

      Specifies whether the user is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
      her password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
      temporary password, but on first sign-in, the user must change his or her password to a
      new value before doing anything else.

    - **MFAOptions** *(list) --*

      The MFA options for the user.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA
         configurations. You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
        responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ListUsersInGroupPaginateResponseTypeDef = TypedDict(
    "_ListUsersInGroupPaginateResponseTypeDef",
    {"Users": List[ListUsersInGroupPaginateResponseUsersTypeDef]},
    total=False,
)


class ListUsersInGroupPaginateResponseTypeDef(_ListUsersInGroupPaginateResponseTypeDef):
    """
    Type definition for `ListUsersInGroupPaginate` `Response`

    - **Users** *(list) --*

      The users returned in the request to list users.

      - *(dict) --*

        The user type.

        - **Username** *(string) --*

          The user name of the user you wish to describe.

        - **Attributes** *(list) --*

          A container with information about the user type attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **UserCreateDate** *(datetime) --*

          The creation date of the user.

        - **UserLastModifiedDate** *(datetime) --*

          The last modified date of the user.

        - **Enabled** *(boolean) --*

          Specifies whether the user is enabled.

        - **UserStatus** *(string) --*

          The user status. Can be one of the following:

          * UNCONFIRMED - User has been created but not confirmed.

          * CONFIRMED - User has been confirmed.

          * ARCHIVED - User is no longer active.

          * COMPROMISED - User is disabled due to a potential security threat.

          * UNKNOWN - User status is not known.

          * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
          her password before he or she can sign in.

          * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
          temporary password, but on first sign-in, the user must change his or her password to a
          new value before doing anything else.

        - **MFAOptions** *(list) --*

          The MFA options for the user.

          - *(dict) --*

             *This data type is no longer supported.* You can use it only for SMS MFA
             configurations. You can't use it for TOTP software token MFA configurations.

            To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
            SetUserMFAPreference actions.

            To look up information about either type of MFA configuration, use the
            AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
            responses.

            - **DeliveryMedium** *(string) --*

              The delivery medium to send the MFA code. You can use this parameter to set only the
              ``SMS`` delivery medium value.

            - **AttributeName** *(string) --*

              The attribute name of the MFA option type. The only valid value is ``phone_number`` .
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


_ListUsersPaginateResponseUsersAttributesTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListUsersPaginateResponseUsersAttributesTypeDef(
    _ListUsersPaginateResponseUsersAttributesTypeDef
):
    """
    Type definition for `ListUsersPaginateResponseUsers` `Attributes`

    Specifies whether the attribute is standard or custom.

    - **Name** *(string) --*

      The name of the attribute.

    - **Value** *(string) --*

      The value of the attribute.
    """


_ListUsersPaginateResponseUsersMFAOptionsTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersMFAOptionsTypeDef",
    {"DeliveryMedium": str, "AttributeName": str},
    total=False,
)


class ListUsersPaginateResponseUsersMFAOptionsTypeDef(
    _ListUsersPaginateResponseUsersMFAOptionsTypeDef
):
    """
    Type definition for `ListUsersPaginateResponseUsers` `MFAOptions`

     *This data type is no longer supported.* You can use it only for SMS MFA
     configurations. You can't use it for TOTP software token MFA configurations.

    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
    SetUserMFAPreference actions.

    To look up information about either type of MFA configuration, use the
    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
    responses.

    - **DeliveryMedium** *(string) --*

      The delivery medium to send the MFA code. You can use this parameter to set only the
      ``SMS`` delivery medium value.

    - **AttributeName** *(string) --*

      The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ListUsersPaginateResponseUsersTypeDef = TypedDict(
    "_ListUsersPaginateResponseUsersTypeDef",
    {
        "Username": str,
        "Attributes": List[ListUsersPaginateResponseUsersAttributesTypeDef],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": str,
        "MFAOptions": List[ListUsersPaginateResponseUsersMFAOptionsTypeDef],
    },
    total=False,
)


class ListUsersPaginateResponseUsersTypeDef(_ListUsersPaginateResponseUsersTypeDef):
    """
    Type definition for `ListUsersPaginateResponse` `Users`

    The user type.

    - **Username** *(string) --*

      The user name of the user you wish to describe.

    - **Attributes** *(list) --*

      A container with information about the user type attributes.

      - *(dict) --*

        Specifies whether the attribute is standard or custom.

        - **Name** *(string) --*

          The name of the attribute.

        - **Value** *(string) --*

          The value of the attribute.

    - **UserCreateDate** *(datetime) --*

      The creation date of the user.

    - **UserLastModifiedDate** *(datetime) --*

      The last modified date of the user.

    - **Enabled** *(boolean) --*

      Specifies whether the user is enabled.

    - **UserStatus** *(string) --*

      The user status. Can be one of the following:

      * UNCONFIRMED - User has been created but not confirmed.

      * CONFIRMED - User has been confirmed.

      * ARCHIVED - User is no longer active.

      * COMPROMISED - User is disabled due to a potential security threat.

      * UNKNOWN - User status is not known.

      * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
      her password before he or she can sign in.

      * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
      temporary password, but on first sign-in, the user must change his or her password to a
      new value before doing anything else.

    - **MFAOptions** *(list) --*

      The MFA options for the user.

      - *(dict) --*

         *This data type is no longer supported.* You can use it only for SMS MFA
         configurations. You can't use it for TOTP software token MFA configurations.

        To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
        SetUserMFAPreference actions.

        To look up information about either type of MFA configuration, use the
        AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
        responses.

        - **DeliveryMedium** *(string) --*

          The delivery medium to send the MFA code. You can use this parameter to set only the
          ``SMS`` delivery medium value.

        - **AttributeName** *(string) --*

          The attribute name of the MFA option type. The only valid value is ``phone_number`` .
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"Users": List[ListUsersPaginateResponseUsersTypeDef], "NextToken": str},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    Type definition for `ListUsersPaginate` `Response`

    The response from the request to list users.

    - **Users** *(list) --*

      The users returned in the request to list users.

      - *(dict) --*

        The user type.

        - **Username** *(string) --*

          The user name of the user you wish to describe.

        - **Attributes** *(list) --*

          A container with information about the user type attributes.

          - *(dict) --*

            Specifies whether the attribute is standard or custom.

            - **Name** *(string) --*

              The name of the attribute.

            - **Value** *(string) --*

              The value of the attribute.

        - **UserCreateDate** *(datetime) --*

          The creation date of the user.

        - **UserLastModifiedDate** *(datetime) --*

          The last modified date of the user.

        - **Enabled** *(boolean) --*

          Specifies whether the user is enabled.

        - **UserStatus** *(string) --*

          The user status. Can be one of the following:

          * UNCONFIRMED - User has been created but not confirmed.

          * CONFIRMED - User has been confirmed.

          * ARCHIVED - User is no longer active.

          * COMPROMISED - User is disabled due to a potential security threat.

          * UNKNOWN - User status is not known.

          * RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or
          her password before he or she can sign in.

          * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
          temporary password, but on first sign-in, the user must change his or her password to a
          new value before doing anything else.

        - **MFAOptions** *(list) --*

          The MFA options for the user.

          - *(dict) --*

             *This data type is no longer supported.* You can use it only for SMS MFA
             configurations. You can't use it for TOTP software token MFA configurations.

            To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
            SetUserMFAPreference actions.

            To look up information about either type of MFA configuration, use the
            AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
            responses.

            - **DeliveryMedium** *(string) --*

              The delivery medium to send the MFA code. You can use this parameter to set only the
              ``SMS`` delivery medium value.

            - **AttributeName** *(string) --*

              The attribute name of the MFA option type. The only valid value is ``phone_number`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
