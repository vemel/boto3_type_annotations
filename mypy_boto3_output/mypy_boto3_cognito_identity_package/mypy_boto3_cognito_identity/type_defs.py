"Main interface for cognito-identity type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientCreateIdentityPoolResponseTypeDef",
    "ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    "ClientDeleteIdentitiesResponseTypeDef",
    "ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientDescribeIdentityPoolResponseTypeDef",
    "ClientDescribeIdentityResponseTypeDef",
    "ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    "ClientGetCredentialsForIdentityResponseTypeDef",
    "ClientGetIdResponseTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    "ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    "ClientGetIdentityPoolRolesResponseTypeDef",
    "ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "ClientGetOpenIdTokenResponseTypeDef",
    "ClientListIdentitiesResponseIdentitiesTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    "ClientListIdentityPoolsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientLookupDeveloperIdentityResponseTypeDef",
    "ClientMergeDeveloperIdentitiesResponseTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    "ClientSetIdentityPoolRolesRoleMappingsTypeDef",
    "ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    "ClientUpdateIdentityPoolResponseTypeDef",
    "ListIdentityPoolsPaginatePaginationConfigTypeDef",
    "ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef",
    "ListIdentityPoolsPaginateResponseTypeDef",
)


_ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef(
    _ClientCreateIdentityPoolCognitoIdentityProvidersTypeDef
):
    """
    Type definition for `ClientCreateIdentityPool` `CognitoIdentityProviders`

    A provider representing an Amazon Cognito user pool and its client ID.

    - **ProviderName** *(string) --*

      The provider name for an Amazon Cognito user pool. For example,
      ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

    - **ClientId** *(string) --*

      The client ID for the Amazon Cognito user pool.

    - **ServerSideTokenCheck** *(boolean) --*

      TRUE if server-side token validation is enabled for the identity provider’s token.

      Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool will
      check with the integrated user pools to make sure that the user has not been globally signed
      out or deleted before the identity pool provides an OIDC token or AWS credentials for the
      user.

      If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
      error.
    """


_ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    """
    Type definition for `ClientCreateIdentityPoolResponse` `CognitoIdentityProviders`

    A provider representing an Amazon Cognito user pool and its client ID.

    - **ProviderName** *(string) --*

      The provider name for an Amazon Cognito user pool. For example,
      ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

    - **ClientId** *(string) --*

      The client ID for the Amazon Cognito user pool.

    - **ServerSideTokenCheck** *(boolean) --*

      TRUE if server-side token validation is enabled for the identity provider’s token.

      Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
      will check with the integrated user pools to make sure that the user has not been
      globally signed out or deleted before the identity pool provides an OIDC token or AWS
      credentials for the user.

      If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
      error.
    """


_ClientCreateIdentityPoolResponseTypeDef = TypedDict(
    "_ClientCreateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientCreateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientCreateIdentityPoolResponseTypeDef(_ClientCreateIdentityPoolResponseTypeDef):
    """
    Type definition for `ClientCreateIdentityPool` `Response`

    An object representing an Amazon Cognito identity pool.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **IdentityPoolName** *(string) --*

      A string that you provide.

    - **AllowUnauthenticatedIdentities** *(boolean) --*

      TRUE if the identity pool supports unauthenticated logins.

    - **AllowClassicFlow** *(boolean) --*

      Enables or disables the Basic (Classic) authentication flow. For more information, see
      `Identity Pools (Federated Identities) Authentication Flow
      <https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html>`__ in
      the *Amazon Cognito Developer Guide* .

    - **SupportedLoginProviders** *(dict) --*

      Optional key:value pairs mapping provider names to provider app IDs.

      - *(string) --*

        - *(string) --*

    - **DeveloperProviderName** *(string) --*

      The "domain" by which Cognito will refer to your users.

    - **OpenIdConnectProviderARNs** *(list) --*

      A list of OpendID Connect provider ARNs.

      - *(string) --*

    - **CognitoIdentityProviders** *(list) --*

      A list representing an Amazon Cognito user pool and its client ID.

      - *(dict) --*

        A provider representing an Amazon Cognito user pool and its client ID.

        - **ProviderName** *(string) --*

          The provider name for an Amazon Cognito user pool. For example,
          ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

        - **ClientId** *(string) --*

          The client ID for the Amazon Cognito user pool.

        - **ServerSideTokenCheck** *(boolean) --*

          TRUE if server-side token validation is enabled for the identity provider’s token.

          Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
          will check with the integrated user pools to make sure that the user has not been
          globally signed out or deleted before the identity pool provides an OIDC token or AWS
          credentials for the user.

          If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
          error.

    - **SamlProviderARNs** *(list) --*

      An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

      - *(string) --*

    - **IdentityPoolTags** *(dict) --*

      The tags that are assigned to the identity pool. A tag is a label that you can apply to
      identity pools to categorize and manage them in different ways, such as by purpose, owner,
      environment, or other criteria.

      - *(string) --*

        - *(string) --*
    """


_ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef = TypedDict(
    "_ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef",
    {"IdentityId": str, "ErrorCode": str},
    total=False,
)


class ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef(
    _ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef
):
    """
    Type definition for `ClientDeleteIdentitiesResponse` `UnprocessedIdentityIds`

    An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and
    IdentityId.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **ErrorCode** *(string) --*

      The error code indicating the type of error that occurred.
    """


_ClientDeleteIdentitiesResponseTypeDef = TypedDict(
    "_ClientDeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List[
            ClientDeleteIdentitiesResponseUnprocessedIdentityIdsTypeDef
        ]
    },
    total=False,
)


class ClientDeleteIdentitiesResponseTypeDef(_ClientDeleteIdentitiesResponseTypeDef):
    """
    Type definition for `ClientDeleteIdentities` `Response`

    Returned in response to a successful ``DeleteIdentities`` operation.

    - **UnprocessedIdentityIds** *(list) --*

      An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.

      - *(dict) --*

        An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and
        IdentityId.

        - **IdentityId** *(string) --*

          A unique identifier in the format REGION:GUID.

        - **ErrorCode** *(string) --*

          The error code indicating the type of error that occurred.
    """


_ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    """
    Type definition for `ClientDescribeIdentityPoolResponse` `CognitoIdentityProviders`

    A provider representing an Amazon Cognito user pool and its client ID.

    - **ProviderName** *(string) --*

      The provider name for an Amazon Cognito user pool. For example,
      ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

    - **ClientId** *(string) --*

      The client ID for the Amazon Cognito user pool.

    - **ServerSideTokenCheck** *(boolean) --*

      TRUE if server-side token validation is enabled for the identity provider’s token.

      Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
      will check with the integrated user pools to make sure that the user has not been
      globally signed out or deleted before the identity pool provides an OIDC token or AWS
      credentials for the user.

      If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
      error.
    """


_ClientDescribeIdentityPoolResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientDescribeIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeIdentityPoolResponseTypeDef(
    _ClientDescribeIdentityPoolResponseTypeDef
):
    """
    Type definition for `ClientDescribeIdentityPool` `Response`

    An object representing an Amazon Cognito identity pool.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **IdentityPoolName** *(string) --*

      A string that you provide.

    - **AllowUnauthenticatedIdentities** *(boolean) --*

      TRUE if the identity pool supports unauthenticated logins.

    - **AllowClassicFlow** *(boolean) --*

      Enables or disables the Basic (Classic) authentication flow. For more information, see
      `Identity Pools (Federated Identities) Authentication Flow
      <https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html>`__ in
      the *Amazon Cognito Developer Guide* .

    - **SupportedLoginProviders** *(dict) --*

      Optional key:value pairs mapping provider names to provider app IDs.

      - *(string) --*

        - *(string) --*

    - **DeveloperProviderName** *(string) --*

      The "domain" by which Cognito will refer to your users.

    - **OpenIdConnectProviderARNs** *(list) --*

      A list of OpendID Connect provider ARNs.

      - *(string) --*

    - **CognitoIdentityProviders** *(list) --*

      A list representing an Amazon Cognito user pool and its client ID.

      - *(dict) --*

        A provider representing an Amazon Cognito user pool and its client ID.

        - **ProviderName** *(string) --*

          The provider name for an Amazon Cognito user pool. For example,
          ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

        - **ClientId** *(string) --*

          The client ID for the Amazon Cognito user pool.

        - **ServerSideTokenCheck** *(boolean) --*

          TRUE if server-side token validation is enabled for the identity provider’s token.

          Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
          will check with the integrated user pools to make sure that the user has not been
          globally signed out or deleted before the identity pool provides an OIDC token or AWS
          credentials for the user.

          If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
          error.

    - **SamlProviderARNs** *(list) --*

      An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

      - *(string) --*

    - **IdentityPoolTags** *(dict) --*

      The tags that are assigned to the identity pool. A tag is a label that you can apply to
      identity pools to categorize and manage them in different ways, such as by purpose, owner,
      environment, or other criteria.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeIdentityResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeIdentityResponseTypeDef(_ClientDescribeIdentityResponseTypeDef):
    """
    Type definition for `ClientDescribeIdentity` `Response`

    A description of the identity.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **Logins** *(list) --*

      The provider names.

      - *(string) --*

    - **CreationDate** *(datetime) --*

      Date on which the identity was created.

    - **LastModifiedDate** *(datetime) --*

      Date on which the identity was last modified.
    """


_ClientGetCredentialsForIdentityResponseCredentialsTypeDef = TypedDict(
    "_ClientGetCredentialsForIdentityResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientGetCredentialsForIdentityResponseCredentialsTypeDef(
    _ClientGetCredentialsForIdentityResponseCredentialsTypeDef
):
    """
    Type definition for `ClientGetCredentialsForIdentityResponse` `Credentials`

    Credentials for the provided identity ID.

    - **AccessKeyId** *(string) --*

      The Access Key portion of the credentials.

    - **SecretKey** *(string) --*

      The Secret Access Key portion of the credentials

    - **SessionToken** *(string) --*

      The Session Token portion of the credentials

    - **Expiration** *(datetime) --*

      The date at which these credentials will expire.
    """


_ClientGetCredentialsForIdentityResponseTypeDef = TypedDict(
    "_ClientGetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": ClientGetCredentialsForIdentityResponseCredentialsTypeDef,
    },
    total=False,
)


class ClientGetCredentialsForIdentityResponseTypeDef(
    _ClientGetCredentialsForIdentityResponseTypeDef
):
    """
    Type definition for `ClientGetCredentialsForIdentity` `Response`

    Returned in response to a successful ``GetCredentialsForIdentity`` operation.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **Credentials** *(dict) --*

      Credentials for the provided identity ID.

      - **AccessKeyId** *(string) --*

        The Access Key portion of the credentials.

      - **SecretKey** *(string) --*

        The Secret Access Key portion of the credentials

      - **SessionToken** *(string) --*

        The Session Token portion of the credentials

      - **Expiration** *(datetime) --*

        The date at which these credentials will expire.
    """


_ClientGetIdResponseTypeDef = TypedDict(
    "_ClientGetIdResponseTypeDef", {"IdentityId": str}, total=False
)


class ClientGetIdResponseTypeDef(_ClientGetIdResponseTypeDef):
    """
    Type definition for `ClientGetId` `Response`

    Returned in response to a GetId request.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.
    """


_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef",
    {"Claim": str, "MatchType": str, "Value": str, "RoleARN": str},
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfiguration` `Rules`

    A rule that maps a claim name, a claim value, and a match type to a role ARN.

    - **Claim** *(string) --*

      The claim name that must be present in the token, for example, "isAdmin" or
      "paid".

    - **MatchType** *(string) --*

      The match condition that specifies how closely the claim value in the IdP token
      must match ``Value`` .

    - **Value** *(string) --*

      A brief string that the claim must match, for example, "paid" or "yes".

    - **RoleARN** *(string) --*

      The role ARN.
    """


_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef",
    {
        "Rules": List[
            ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationRulesTypeDef
        ]
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolRolesResponseRoleMappings` `RulesConfiguration`

    The rules to be used for mapping users to roles.

    If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.

    - **Rules** *(list) --*

      An array of rules. You can specify up to 25 rules per identity provider.

      Rules are evaluated in order. The first one to match specifies the role.

      - *(dict) --*

        A rule that maps a claim name, a claim value, and a match type to a role ARN.

        - **Claim** *(string) --*

          The claim name that must be present in the token, for example, "isAdmin" or
          "paid".

        - **MatchType** *(string) --*

          The match condition that specifies how closely the claim value in the IdP token
          must match ``Value`` .

        - **Value** *(string) --*

          A brief string that the claim must match, for example, "paid" or "yes".

        - **RoleARN** *(string) --*

          The role ARN.
    """


_ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef",
    {
        "Type": str,
        "AmbiguousRoleResolution": str,
        "RulesConfiguration": ClientGetIdentityPoolRolesResponseRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef(
    _ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolRolesResponse` `RoleMappings`

    A role mapping.

    - **Type** *(string) --*

      The role mapping type. Token will use ``cognito:roles`` and ``cognito:preferred_role``
      claims from the Cognito identity provider token to map groups to roles. Rules will
      attempt to match claims from the token to map to a role.

    - **AmbiguousRoleResolution** *(string) --*

      If you specify Token or Rules as the ``Type`` , ``AmbiguousRoleResolution`` is required.

      Specifies the action to be taken if either no rules match the claim value for the
      ``Rules`` type, or there is no ``cognito:preferred_role`` claim and there are multiple
      ``cognito:roles`` matches for the ``Token`` type.

    - **RulesConfiguration** *(dict) --*

      The rules to be used for mapping users to roles.

      If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.

      - **Rules** *(list) --*

        An array of rules. You can specify up to 25 rules per identity provider.

        Rules are evaluated in order. The first one to match specifies the role.

        - *(dict) --*

          A rule that maps a claim name, a claim value, and a match type to a role ARN.

          - **Claim** *(string) --*

            The claim name that must be present in the token, for example, "isAdmin" or
            "paid".

          - **MatchType** *(string) --*

            The match condition that specifies how closely the claim value in the IdP token
            must match ``Value`` .

          - **Value** *(string) --*

            A brief string that the claim must match, for example, "paid" or "yes".

          - **RoleARN** *(string) --*

            The role ARN.
    """


_ClientGetIdentityPoolRolesResponseTypeDef = TypedDict(
    "_ClientGetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[
            str, ClientGetIdentityPoolRolesResponseRoleMappingsTypeDef
        ],
    },
    total=False,
)


class ClientGetIdentityPoolRolesResponseTypeDef(
    _ClientGetIdentityPoolRolesResponseTypeDef
):
    """
    Type definition for `ClientGetIdentityPoolRoles` `Response`

    Returned in response to a successful ``GetIdentityPoolRoles`` operation.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **Roles** *(dict) --*

      The map of roles associated with this pool. Currently only authenticated and unauthenticated
      roles are supported.

      - *(string) --*

        - *(string) --*

    - **RoleMappings** *(dict) --*

      How users for a specific identity provider are to mapped to roles. This is a String-to-
      RoleMapping object map. The string identifies the identity provider, for example,
      "graph.facebook.com" or
      "cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".

      - *(string) --*

        - *(dict) --*

          A role mapping.

          - **Type** *(string) --*

            The role mapping type. Token will use ``cognito:roles`` and ``cognito:preferred_role``
            claims from the Cognito identity provider token to map groups to roles. Rules will
            attempt to match claims from the token to map to a role.

          - **AmbiguousRoleResolution** *(string) --*

            If you specify Token or Rules as the ``Type`` , ``AmbiguousRoleResolution`` is required.

            Specifies the action to be taken if either no rules match the claim value for the
            ``Rules`` type, or there is no ``cognito:preferred_role`` claim and there are multiple
            ``cognito:roles`` matches for the ``Token`` type.

          - **RulesConfiguration** *(dict) --*

            The rules to be used for mapping users to roles.

            If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.

            - **Rules** *(list) --*

              An array of rules. You can specify up to 25 rules per identity provider.

              Rules are evaluated in order. The first one to match specifies the role.

              - *(dict) --*

                A rule that maps a claim name, a claim value, and a match type to a role ARN.

                - **Claim** *(string) --*

                  The claim name that must be present in the token, for example, "isAdmin" or
                  "paid".

                - **MatchType** *(string) --*

                  The match condition that specifies how closely the claim value in the IdP token
                  must match ``Value`` .

                - **Value** *(string) --*

                  A brief string that the claim must match, for example, "paid" or "yes".

                - **RoleARN** *(string) --*

                  The role ARN.
    """


_ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "_ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "Token": str},
    total=False,
)


class ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef(
    _ClientGetOpenIdTokenForDeveloperIdentityResponseTypeDef
):
    """
    Type definition for `ClientGetOpenIdTokenForDeveloperIdentity` `Response`

    Returned in response to a successful ``GetOpenIdTokenForDeveloperIdentity`` request.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **Token** *(string) --*

      An OpenID token.
    """


_ClientGetOpenIdTokenResponseTypeDef = TypedDict(
    "_ClientGetOpenIdTokenResponseTypeDef",
    {"IdentityId": str, "Token": str},
    total=False,
)


class ClientGetOpenIdTokenResponseTypeDef(_ClientGetOpenIdTokenResponseTypeDef):
    """
    Type definition for `ClientGetOpenIdToken` `Response`

    Returned in response to a successful GetOpenIdToken request.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not
      match the one passed on input.

    - **Token** *(string) --*

      An OpenID token, valid for 10 minutes.
    """


_ClientListIdentitiesResponseIdentitiesTypeDef = TypedDict(
    "_ClientListIdentitiesResponseIdentitiesTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)


class ClientListIdentitiesResponseIdentitiesTypeDef(
    _ClientListIdentitiesResponseIdentitiesTypeDef
):
    """
    Type definition for `ClientListIdentitiesResponse` `Identities`

    A description of the identity.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **Logins** *(list) --*

      The provider names.

      - *(string) --*

    - **CreationDate** *(datetime) --*

      Date on which the identity was created.

    - **LastModifiedDate** *(datetime) --*

      Date on which the identity was last modified.
    """


_ClientListIdentitiesResponseTypeDef = TypedDict(
    "_ClientListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List[ClientListIdentitiesResponseIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIdentitiesResponseTypeDef(_ClientListIdentitiesResponseTypeDef):
    """
    Type definition for `ClientListIdentities` `Response`

    The response to a ListIdentities request.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **Identities** *(list) --*

      An object containing a set of identities and associated mappings.

      - *(dict) --*

        A description of the identity.

        - **IdentityId** *(string) --*

          A unique identifier in the format REGION:GUID.

        - **Logins** *(list) --*

          The provider names.

          - *(string) --*

        - **CreationDate** *(datetime) --*

          Date on which the identity was created.

        - **LastModifiedDate** *(datetime) --*

          Date on which the identity was last modified.

    - **NextToken** *(string) --*

      A pagination token.
    """


_ClientListIdentityPoolsResponseIdentityPoolsTypeDef = TypedDict(
    "_ClientListIdentityPoolsResponseIdentityPoolsTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)


class ClientListIdentityPoolsResponseIdentityPoolsTypeDef(
    _ClientListIdentityPoolsResponseIdentityPoolsTypeDef
):
    """
    Type definition for `ClientListIdentityPoolsResponse` `IdentityPools`

    A description of the identity pool.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **IdentityPoolName** *(string) --*

      A string that you provide.
    """


_ClientListIdentityPoolsResponseTypeDef = TypedDict(
    "_ClientListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List[ClientListIdentityPoolsResponseIdentityPoolsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIdentityPoolsResponseTypeDef(_ClientListIdentityPoolsResponseTypeDef):
    """
    Type definition for `ClientListIdentityPools` `Response`

    The result of a successful ListIdentityPools action.

    - **IdentityPools** *(list) --*

      The identity pools returned by the ListIdentityPools action.

      - *(dict) --*

        A description of the identity pool.

        - **IdentityPoolId** *(string) --*

          An identity pool ID in the format REGION:GUID.

        - **IdentityPoolName** *(string) --*

          A string that you provide.

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

      The tags that are assigned to the identity pool.

      - *(string) --*

        - *(string) --*
    """


_ClientLookupDeveloperIdentityResponseTypeDef = TypedDict(
    "_ClientLookupDeveloperIdentityResponseTypeDef",
    {"IdentityId": str, "DeveloperUserIdentifierList": List[str], "NextToken": str},
    total=False,
)


class ClientLookupDeveloperIdentityResponseTypeDef(
    _ClientLookupDeveloperIdentityResponseTypeDef
):
    """
    Type definition for `ClientLookupDeveloperIdentity` `Response`

    Returned in response to a successful ``LookupDeveloperIdentity`` action.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.

    - **DeveloperUserIdentifierList** *(list) --*

      This is the list of developer user identifiers associated with an identity ID. Cognito
      supports the association of multiple developer user identifiers with an identity ID.

      - *(string) --*

    - **NextToken** *(string) --*

      A pagination token. The first call you make will have ``NextToken`` set to null. After that
      the service will return ``NextToken`` values as needed. For example, let's say you make a
      request with ``MaxResults`` set to 10, and there are 20 matches in the database. The service
      will return a pagination token as a part of the response. This token can be used to call the
      API again and get results starting from the 11th match.
    """


_ClientMergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "_ClientMergeDeveloperIdentitiesResponseTypeDef", {"IdentityId": str}, total=False
)


class ClientMergeDeveloperIdentitiesResponseTypeDef(
    _ClientMergeDeveloperIdentitiesResponseTypeDef
):
    """
    Type definition for `ClientMergeDeveloperIdentities` `Response`

    Returned in response to a successful ``MergeDeveloperIdentities`` action.

    - **IdentityId** *(string) --*

      A unique identifier in the format REGION:GUID.
    """


_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef = TypedDict(
    "_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef",
    {"Claim": str, "MatchType": str, "Value": str, "RoleARN": str},
)


class ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef(
    _ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolRolesRoleMappingsRulesConfiguration` `Rules`

    A rule that maps a claim name, a claim value, and a match type to a role ARN.

    - **Claim** *(string) --* **[REQUIRED]**

      The claim name that must be present in the token, for example, "isAdmin" or "paid".

    - **MatchType** *(string) --* **[REQUIRED]**

      The match condition that specifies how closely the claim value in the IdP token must
      match ``Value`` .

    - **Value** *(string) --* **[REQUIRED]**

      A brief string that the claim must match, for example, "paid" or "yes".

    - **RoleARN** *(string) --* **[REQUIRED]**

      The role ARN.
    """


_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef = TypedDict(
    "_ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef",
    {
        "Rules": List[
            ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationRulesTypeDef
        ]
    },
)


class ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef(
    _ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef
):
    """
    Type definition for `ClientSetIdentityPoolRolesRoleMappings` `RulesConfiguration`

    The rules to be used for mapping users to roles.

    If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.

    - **Rules** *(list) --* **[REQUIRED]**

      An array of rules. You can specify up to 25 rules per identity provider.

      Rules are evaluated in order. The first one to match specifies the role.

      - *(dict) --*

        A rule that maps a claim name, a claim value, and a match type to a role ARN.

        - **Claim** *(string) --* **[REQUIRED]**

          The claim name that must be present in the token, for example, "isAdmin" or "paid".

        - **MatchType** *(string) --* **[REQUIRED]**

          The match condition that specifies how closely the claim value in the IdP token must
          match ``Value`` .

        - **Value** *(string) --* **[REQUIRED]**

          A brief string that the claim must match, for example, "paid" or "yes".

        - **RoleARN** *(string) --* **[REQUIRED]**

          The role ARN.
    """


_RequiredClientSetIdentityPoolRolesRoleMappingsTypeDef = TypedDict(
    "_RequiredClientSetIdentityPoolRolesRoleMappingsTypeDef", {"Type": str}
)
_OptionalClientSetIdentityPoolRolesRoleMappingsTypeDef = TypedDict(
    "_OptionalClientSetIdentityPoolRolesRoleMappingsTypeDef",
    {
        "AmbiguousRoleResolution": str,
        "RulesConfiguration": ClientSetIdentityPoolRolesRoleMappingsRulesConfigurationTypeDef,
    },
    total=False,
)


class ClientSetIdentityPoolRolesRoleMappingsTypeDef(
    _RequiredClientSetIdentityPoolRolesRoleMappingsTypeDef,
    _OptionalClientSetIdentityPoolRolesRoleMappingsTypeDef,
):
    """
    Type definition for `ClientSetIdentityPoolRoles` `RoleMappings`

    A role mapping.

    - **Type** *(string) --* **[REQUIRED]**

      The role mapping type. Token will use ``cognito:roles`` and ``cognito:preferred_role``
      claims from the Cognito identity provider token to map groups to roles. Rules will attempt
      to match claims from the token to map to a role.

    - **AmbiguousRoleResolution** *(string) --*

      If you specify Token or Rules as the ``Type`` , ``AmbiguousRoleResolution`` is required.

      Specifies the action to be taken if either no rules match the claim value for the ``Rules``
      type, or there is no ``cognito:preferred_role`` claim and there are multiple
      ``cognito:roles`` matches for the ``Token`` type.

    - **RulesConfiguration** *(dict) --*

      The rules to be used for mapping users to roles.

      If you specify Rules as the role mapping type, ``RulesConfiguration`` is required.

      - **Rules** *(list) --* **[REQUIRED]**

        An array of rules. You can specify up to 25 rules per identity provider.

        Rules are evaluated in order. The first one to match specifies the role.

        - *(dict) --*

          A rule that maps a claim name, a claim value, and a match type to a role ARN.

          - **Claim** *(string) --* **[REQUIRED]**

            The claim name that must be present in the token, for example, "isAdmin" or "paid".

          - **MatchType** *(string) --* **[REQUIRED]**

            The match condition that specifies how closely the claim value in the IdP token must
            match ``Value`` .

          - **Value** *(string) --* **[REQUIRED]**

            A brief string that the claim must match, for example, "paid" or "yes".

          - **RoleARN** *(string) --* **[REQUIRED]**

            The role ARN.
    """


_ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef(
    _ClientUpdateIdentityPoolCognitoIdentityProvidersTypeDef
):
    """
    Type definition for `ClientUpdateIdentityPool` `CognitoIdentityProviders`

    A provider representing an Amazon Cognito user pool and its client ID.

    - **ProviderName** *(string) --*

      The provider name for an Amazon Cognito user pool. For example,
      ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

    - **ClientId** *(string) --*

      The client ID for the Amazon Cognito user pool.

    - **ServerSideTokenCheck** *(boolean) --*

      TRUE if server-side token validation is enabled for the identity provider’s token.

      Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool will
      check with the integrated user pools to make sure that the user has not been globally signed
      out or deleted before the identity pool provides an OIDC token or AWS credentials for the
      user.

      If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
      error.
    """


_ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef",
    {"ProviderName": str, "ClientId": str, "ServerSideTokenCheck": bool},
    total=False,
)


class ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef(
    _ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef
):
    """
    Type definition for `ClientUpdateIdentityPoolResponse` `CognitoIdentityProviders`

    A provider representing an Amazon Cognito user pool and its client ID.

    - **ProviderName** *(string) --*

      The provider name for an Amazon Cognito user pool. For example,
      ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

    - **ClientId** *(string) --*

      The client ID for the Amazon Cognito user pool.

    - **ServerSideTokenCheck** *(boolean) --*

      TRUE if server-side token validation is enabled for the identity provider’s token.

      Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
      will check with the integrated user pools to make sure that the user has not been
      globally signed out or deleted before the identity pool provides an OIDC token or AWS
      credentials for the user.

      If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
      error.
    """


_ClientUpdateIdentityPoolResponseTypeDef = TypedDict(
    "_ClientUpdateIdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List[
            ClientUpdateIdentityPoolResponseCognitoIdentityProvidersTypeDef
        ],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateIdentityPoolResponseTypeDef(_ClientUpdateIdentityPoolResponseTypeDef):
    """
    Type definition for `ClientUpdateIdentityPool` `Response`

    An object representing an Amazon Cognito identity pool.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **IdentityPoolName** *(string) --*

      A string that you provide.

    - **AllowUnauthenticatedIdentities** *(boolean) --*

      TRUE if the identity pool supports unauthenticated logins.

    - **AllowClassicFlow** *(boolean) --*

      Enables or disables the Basic (Classic) authentication flow. For more information, see
      `Identity Pools (Federated Identities) Authentication Flow
      <https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html>`__ in
      the *Amazon Cognito Developer Guide* .

    - **SupportedLoginProviders** *(dict) --*

      Optional key:value pairs mapping provider names to provider app IDs.

      - *(string) --*

        - *(string) --*

    - **DeveloperProviderName** *(string) --*

      The "domain" by which Cognito will refer to your users.

    - **OpenIdConnectProviderARNs** *(list) --*

      A list of OpendID Connect provider ARNs.

      - *(string) --*

    - **CognitoIdentityProviders** *(list) --*

      A list representing an Amazon Cognito user pool and its client ID.

      - *(dict) --*

        A provider representing an Amazon Cognito user pool and its client ID.

        - **ProviderName** *(string) --*

          The provider name for an Amazon Cognito user pool. For example,
          ``cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`` .

        - **ClientId** *(string) --*

          The client ID for the Amazon Cognito user pool.

        - **ServerSideTokenCheck** *(boolean) --*

          TRUE if server-side token validation is enabled for the identity provider’s token.

          Once you set ``ServerSideTokenCheck`` to TRUE for an identity pool, that identity pool
          will check with the integrated user pools to make sure that the user has not been
          globally signed out or deleted before the identity pool provides an OIDC token or AWS
          credentials for the user.

          If the user is signed out or deleted, the identity pool will return a 400 Not Authorized
          error.

    - **SamlProviderARNs** *(list) --*

      An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.

      - *(string) --*

    - **IdentityPoolTags** *(dict) --*

      The tags that are assigned to the identity pool. A tag is a label that you can apply to
      identity pools to categorize and manage them in different ways, such as by purpose, owner,
      environment, or other criteria.

      - *(string) --*

        - *(string) --*
    """


_ListIdentityPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentityPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentityPoolsPaginatePaginationConfigTypeDef(
    _ListIdentityPoolsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIdentityPoolsPaginate` `PaginationConfig`

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


_ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef = TypedDict(
    "_ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef",
    {"IdentityPoolId": str, "IdentityPoolName": str},
    total=False,
)


class ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef(
    _ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef
):
    """
    Type definition for `ListIdentityPoolsPaginateResponse` `IdentityPools`

    A description of the identity pool.

    - **IdentityPoolId** *(string) --*

      An identity pool ID in the format REGION:GUID.

    - **IdentityPoolName** *(string) --*

      A string that you provide.
    """


_ListIdentityPoolsPaginateResponseTypeDef = TypedDict(
    "_ListIdentityPoolsPaginateResponseTypeDef",
    {"IdentityPools": List[ListIdentityPoolsPaginateResponseIdentityPoolsTypeDef]},
    total=False,
)


class ListIdentityPoolsPaginateResponseTypeDef(
    _ListIdentityPoolsPaginateResponseTypeDef
):
    """
    Type definition for `ListIdentityPoolsPaginate` `Response`

    The result of a successful ListIdentityPools action.

    - **IdentityPools** *(list) --*

      The identity pools returned by the ListIdentityPools action.

      - *(dict) --*

        A description of the identity pool.

        - **IdentityPoolId** *(string) --*

          An identity pool ID in the format REGION:GUID.

        - **IdentityPoolName** *(string) --*

          A string that you provide.
    """
