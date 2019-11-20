"Main interface for elbv2 type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddListenerCertificatesCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseCertificatesTypeDef",
    "ClientAddListenerCertificatesResponseTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientCreateListenerCertificatesTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersCertificatesTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    "ClientCreateListenerResponseListenersTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    "ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerSubnetMappingsTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleActionsForwardConfigTypeDef",
    "ClientCreateRuleActionsRedirectConfigTypeDef",
    "ClientCreateRuleActionsTypeDef",
    "ClientCreateRuleConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleConditionsTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientCreateRuleResponseRulesActionsTypeDef",
    "ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientCreateRuleResponseRulesConditionsTypeDef",
    "ClientCreateRuleResponseRulesTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateTargetGroupMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    "ClientCreateTargetGroupResponseTypeDef",
    "ClientDeregisterTargetsTargetsTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    "ClientDescribeListenerCertificatesResponseTypeDef",
    "ClientDescribeListenersResponseListenersCertificatesTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    "ClientDescribeListenersResponseListenersTypeDef",
    "ClientDescribeListenersResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    "ClientDescribeRulesResponseRulesActionsTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientDescribeRulesResponseRulesConditionsTypeDef",
    "ClientDescribeRulesResponseRulesTypeDef",
    "ClientDescribeRulesResponseTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    "ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    "ClientDescribeSslPoliciesResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    "ClientDescribeTargetGroupAttributesResponseTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef",
    "ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    "ClientDescribeTargetGroupsResponseTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    "ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    "ClientDescribeTargetHealthResponseTypeDef",
    "ClientDescribeTargetHealthTargetsTypeDef",
    "ClientModifyListenerCertificatesTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersCertificatesTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    "ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    "ClientModifyListenerResponseListenersTypeDef",
    "ClientModifyListenerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleActionsForwardConfigTypeDef",
    "ClientModifyRuleActionsRedirectConfigTypeDef",
    "ClientModifyRuleActionsTypeDef",
    "ClientModifyRuleConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleConditionsTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    "ClientModifyRuleResponseRulesActionsTypeDef",
    "ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientModifyRuleResponseRulesConditionsTypeDef",
    "ClientModifyRuleResponseRulesTypeDef",
    "ClientModifyRuleResponseTypeDef",
    "ClientModifyTargetGroupAttributesAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    "ClientModifyTargetGroupAttributesResponseTypeDef",
    "ClientModifyTargetGroupMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef",
    "ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    "ClientModifyTargetGroupResponseTypeDef",
    "ClientRegisterTargetsTargetsTypeDef",
    "ClientRemoveListenerCertificatesCertificatesTypeDef",
    "ClientSetIpAddressTypeResponseTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    "ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    "ClientSetRulePrioritiesResponseRulesTypeDef",
    "ClientSetRulePrioritiesResponseTypeDef",
    "ClientSetRulePrioritiesRulePrioritiesTypeDef",
    "ClientSetSecurityGroupsResponseTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    "ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    "ClientSetSubnetsResponseTypeDef",
    "ClientSetSubnetsSubnetMappingsTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeListenerCertificatesPaginatePaginationConfigTypeDef",
    "DescribeListenerCertificatesPaginateResponseCertificatesTypeDef",
    "DescribeListenerCertificatesPaginateResponseTypeDef",
    "DescribeListenersPaginatePaginationConfigTypeDef",
    "DescribeListenersPaginateResponseListenersCertificatesTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef",
    "DescribeListenersPaginateResponseListenersDefaultActionsTypeDef",
    "DescribeListenersPaginateResponseListenersTypeDef",
    "DescribeListenersPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "DescribeRulesPaginatePaginationConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    "DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef",
    "DescribeRulesPaginateResponseRulesActionsTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef",
    "DescribeRulesPaginateResponseRulesConditionsTypeDef",
    "DescribeRulesPaginateResponseRulesTypeDef",
    "DescribeRulesPaginateResponseTypeDef",
    "DescribeSSLPoliciesPaginatePaginationConfigTypeDef",
    "DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef",
    "DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef",
    "DescribeSSLPoliciesPaginateResponseTypeDef",
    "DescribeTargetGroupsPaginatePaginationConfigTypeDef",
    "DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef",
    "DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef",
    "DescribeTargetGroupsPaginateResponseTypeDef",
    "LoadBalancerAvailableWaitWaiterConfigTypeDef",
    "LoadBalancerExistsWaitWaiterConfigTypeDef",
    "LoadBalancersDeletedWaitWaiterConfigTypeDef",
    "TargetDeregisteredWaitTargetsTypeDef",
    "TargetDeregisteredWaitWaiterConfigTypeDef",
    "TargetInServiceWaitTargetsTypeDef",
    "TargetInServiceWaitWaiterConfigTypeDef",
)


_ClientAddListenerCertificatesCertificatesTypeDef = TypedDict(
    "_ClientAddListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientAddListenerCertificatesCertificatesTypeDef(
    _ClientAddListenerCertificatesCertificatesTypeDef
):
    """
    Type definition for `ClientAddListenerCertificates` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_ClientAddListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientAddListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientAddListenerCertificatesResponseCertificatesTypeDef(
    _ClientAddListenerCertificatesResponseCertificatesTypeDef
):
    """
    Type definition for `ClientAddListenerCertificatesResponse` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_ClientAddListenerCertificatesResponseTypeDef = TypedDict(
    "_ClientAddListenerCertificatesResponseTypeDef",
    {"Certificates": List[ClientAddListenerCertificatesResponseCertificatesTypeDef]},
    total=False,
)


class ClientAddListenerCertificatesResponseTypeDef(
    _ClientAddListenerCertificatesResponseTypeDef
):
    """
    Type definition for `ClientAddListenerCertificates` `Response`

    - **Certificates** *(list) --*

      Information about the certificates in the certificate list.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value when
          specifying a certificate as an input. This value is not included in the output when
          describing a listener, but is included when describing listener certificates.
    """


_RequiredClientAddTagsTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagsTypeDef(
    _RequiredClientAddTagsTagsTypeDef, _OptionalClientAddTagsTagsTypeDef
):
    """
    Type definition for `ClientAddTags` `Tags`

    Information about a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateListenerCertificatesTypeDef = TypedDict(
    "_ClientCreateListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientCreateListenerCertificatesTypeDef(_ClientCreateListenerCertificatesTypeDef):
    """
    Type definition for `ClientCreateListener` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_RequiredClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef(
    _RequiredClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
    _OptionalClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
):
    """
    Type definition for `ClientCreateListenerDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
    when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --* **[REQUIRED]**

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --* **[REQUIRED]**

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.
    """


_RequiredClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef(
    _RequiredClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef,
    _OptionalClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef,
):
    """
    Type definition for `ClientCreateListenerDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with OpenID
    Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --* **[REQUIRED]**

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --* **[REQUIRED]**

      The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
      domain, and the path.

    - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
      the domain, and the path.

    - **ClientId** *(string) --* **[REQUIRED]**

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
      are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
      true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you are
      creating a rule, you can omit this parameter or set it to false.
    """


_RequiredClientCreateListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    {"StatusCode": str},
)
_OptionalClientCreateListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
    total=False,
)


class ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef(
    _RequiredClientCreateListenerDefaultActionsFixedResponseConfigTypeDef,
    _OptionalClientCreateListenerDefaultActionsFixedResponseConfigTypeDef,
):
    """
    Type definition for `ClientCreateListenerDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom HTTP
    response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript | application/json
    """


_ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed to the
      same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateListenerDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups in a
    forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientCreateListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientCreateListenerDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientCreateListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsForwardConfigTypeDef(
    _ClientCreateListenerDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target groups.
    For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
    is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
    specify only one target group using ``ForwardConfig`` and it must be the same target group
    specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single target
      group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups in a
        forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed to the
        same target group. The range is 1-604800 seconds (7 days).
    """


_RequiredClientCreateListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    {"StatusCode": str},
)
_OptionalClientCreateListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsRedirectConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class ClientCreateListenerDefaultActionsRedirectConfigTypeDef(
    _RequiredClientCreateListenerDefaultActionsRedirectConfigTypeDef,
    _OptionalClientCreateListenerDefaultActionsRedirectConfigTypeDef,
):
    """
    Type definition for `ClientCreateListenerDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only when
    ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
      HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not percent-encoded.
      The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
      the leading "?", as it is automatically added. You can specify any of the reserved keywords.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
    """


_RequiredClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientCreateListenerDefaultActionsTypeDef", {"Type": str}
)
_OptionalClientCreateListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientCreateListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerDefaultActionsTypeDef(
    _RequiredClientCreateListenerDefaultActionsTypeDef,
    _OptionalClientCreateListenerDefaultActionsTypeDef,
):
    """
    Type definition for `ClientCreateListener` `DefaultActions`

    Information about an action.

    - **Type** *(string) --* **[REQUIRED]**

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward``
      and you want to route to a single target group. To route to one or more target groups, use
      ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with OpenID
      Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --* **[REQUIRED]**

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --* **[REQUIRED]**

        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
        domain, and the path.

      - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
        the domain, and the path.

      - **ClientId** *(string) --* **[REQUIRED]**

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
        are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
        true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you are
        creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
      when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --* **[REQUIRED]**

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --* **[REQUIRED]**

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The action
      with the lowest value for order is performed first. The last action to be performed must be
      one of the following types of actions: a ``forward`` , ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only when
      ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
        HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not percent-encoded.
        The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
        the leading "?", as it is automatically added. You can specify any of the reserved keywords.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom HTTP
      response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript | application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target groups.
      For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
      is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
      specify only one target group using ``ForwardConfig`` and it must be the same target group
      specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single target
        group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups in a
          forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed to the
          same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientCreateListenerResponseListenersCertificatesTypeDef(
    _ClientCreateListenerResponseListenersCertificatesTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListeners` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value
      when specifying a certificate as an input. This value is not included in the output
      when describing a listener, but is included when describing listener certificates.
    """


_ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListenersDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientCreateListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateListenerResponseListenersDefaultActionsTypeDef(
    _ClientCreateListenerResponseListenersDefaultActionsTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListeners` `DefaultActions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerResponseListenersTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": str,
        "Certificates": List[ClientCreateListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[
            ClientCreateListenerResponseListenersDefaultActionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateListenerResponseListenersTypeDef(
    _ClientCreateListenerResponseListenersTypeDef
):
    """
    Type definition for `ClientCreateListenerResponse` `Listeners`

    Information about a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **Port** *(integer) --*

      The port on which the load balancer is listening.

    - **Protocol** *(string) --*

      The protocol for connections from clients to the load balancer.

    - **Certificates** *(list) --*

      [HTTPS or TLS listener] The default certificate for the listener.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value
          when specifying a certificate as an input. This value is not included in the output
          when describing a listener, but is included when describing listener certificates.

    - **SslPolicy** *(string) --*

      [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
      supported. The default is the current predefined security policy.

    - **DefaultActions** *(list) --*

      The default actions for the listener.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateListenerResponseTypeDef = TypedDict(
    "_ClientCreateListenerResponseTypeDef",
    {"Listeners": List[ClientCreateListenerResponseListenersTypeDef]},
    total=False,
)


class ClientCreateListenerResponseTypeDef(_ClientCreateListenerResponseTypeDef):
    """
    Type definition for `ClientCreateListener` `Response`

    - **Listeners** *(list) --*

      Information about the listener.

      - *(dict) --*

        Information about a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **Port** *(integer) --*

          The port on which the load balancer is listening.

        - **Protocol** *(string) --*

          The protocol for connections from clients to the load balancer.

        - **Certificates** *(list) --*

          [HTTPS or TLS listener] The default certificate for the listener.

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value
              when specifying a certificate as an input. This value is not included in the output
              when describing a listener, but is included when describing listener certificates.

        - **SslPolicy** *(string) --*

          [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
          supported. The default is the current predefined security policy.

        - **DefaultActions** *(list) --*

          The default actions for the listener.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str},
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZones` `LoadBalancerAddresses`

    Information about a static IP address for a load balancer.

    - **IpAddress** *(string) --*

      The static IP address.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancerResponseLoadBalancers` `AvailabilityZones`

    Information about an Availability Zone.

    - **ZoneName** *(string) --*

      The name of the Availability Zone.

    - **SubnetId** *(string) --*

      The ID of the subnet. You can specify one subnet per Availability Zone.

    - **LoadBalancerAddresses** *(list) --*

      [Network Load Balancers] If you need static IP addresses for your load balancer, you
      can specify one Elastic IP address per Availability Zone when you create the load
      balancer.

      - *(dict) --*

        Information about a static IP address for a load balancer.

        - **IpAddress** *(string) --*

          The static IP address.

        - **AllocationId** *(string) --*

          [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef",
    {"Code": str, "Reason": str},
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancerResponseLoadBalancers` `State`

    The state of the load balancer.

    - **Code** *(string) --*

      The state code. The initial state of the load balancer is ``provisioning`` . After the
      load balancer is fully set up and ready to route traffic, its state is ``active`` . If
      the load balancer could not be set up, its state is ``failed`` .

    - **Reason** *(string) --*

      A description of the state.
    """


_ClientCreateLoadBalancerResponseLoadBalancersTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": str,
        "VpcId": str,
        "State": ClientCreateLoadBalancerResponseLoadBalancersStateTypeDef,
        "Type": str,
        "AvailabilityZones": List[
            ClientCreateLoadBalancerResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": str,
    },
    total=False,
)


class ClientCreateLoadBalancerResponseLoadBalancersTypeDef(
    _ClientCreateLoadBalancerResponseLoadBalancersTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancerResponse` `LoadBalancers`

    Information about a load balancer.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **DNSName** *(string) --*

      The public DNS name of the load balancer.

    - **CanonicalHostedZoneId** *(string) --*

      The ID of the Amazon Route 53 hosted zone associated with the load balancer.

    - **CreatedTime** *(datetime) --*

      The date and time the load balancer was created.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **Scheme** *(string) --*

      The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
      an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
      nodes. Therefore, Internet-facing load balancers can route requests from clients over the
      internet.

      The nodes of an internal load balancer have only private IP addresses. The DNS name of an
      internal load balancer is publicly resolvable to the private IP addresses of the nodes.
      Therefore, internal load balancers can route requests only from clients with access to
      the VPC for the load balancer.

    - **VpcId** *(string) --*

      The ID of the VPC for the load balancer.

    - **State** *(dict) --*

      The state of the load balancer.

      - **Code** *(string) --*

        The state code. The initial state of the load balancer is ``provisioning`` . After the
        load balancer is fully set up and ready to route traffic, its state is ``active`` . If
        the load balancer could not be set up, its state is ``failed`` .

      - **Reason** *(string) --*

        A description of the state.

    - **Type** *(string) --*

      The type of load balancer.

    - **AvailabilityZones** *(list) --*

      The Availability Zones for the load balancer.

      - *(dict) --*

        Information about an Availability Zone.

        - **ZoneName** *(string) --*

          The name of the Availability Zone.

        - **SubnetId** *(string) --*

          The ID of the subnet. You can specify one subnet per Availability Zone.

        - **LoadBalancerAddresses** *(list) --*

          [Network Load Balancers] If you need static IP addresses for your load balancer, you
          can specify one Elastic IP address per Availability Zone when you create the load
          balancer.

          - *(dict) --*

            Information about a static IP address for a load balancer.

            - **IpAddress** *(string) --*

              The static IP address.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.

    - **SecurityGroups** *(list) --*

      The IDs of the security groups for the load balancer.

      - *(string) --*

    - **IpAddressType** *(string) --*

      The type of IP addresses used by the subnets for your load balancer. The possible values
      are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
    """


_ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseTypeDef",
    {"LoadBalancers": List[ClientCreateLoadBalancerResponseLoadBalancersTypeDef]},
    total=False,
)


class ClientCreateLoadBalancerResponseTypeDef(_ClientCreateLoadBalancerResponseTypeDef):
    """
    Type definition for `ClientCreateLoadBalancer` `Response`

    - **LoadBalancers** *(list) --*

      Information about the load balancer.

      - *(dict) --*

        Information about a load balancer.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **DNSName** *(string) --*

          The public DNS name of the load balancer.

        - **CanonicalHostedZoneId** *(string) --*

          The ID of the Amazon Route 53 hosted zone associated with the load balancer.

        - **CreatedTime** *(datetime) --*

          The date and time the load balancer was created.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **Scheme** *(string) --*

          The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
          an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
          nodes. Therefore, Internet-facing load balancers can route requests from clients over the
          internet.

          The nodes of an internal load balancer have only private IP addresses. The DNS name of an
          internal load balancer is publicly resolvable to the private IP addresses of the nodes.
          Therefore, internal load balancers can route requests only from clients with access to
          the VPC for the load balancer.

        - **VpcId** *(string) --*

          The ID of the VPC for the load balancer.

        - **State** *(dict) --*

          The state of the load balancer.

          - **Code** *(string) --*

            The state code. The initial state of the load balancer is ``provisioning`` . After the
            load balancer is fully set up and ready to route traffic, its state is ``active`` . If
            the load balancer could not be set up, its state is ``failed`` .

          - **Reason** *(string) --*

            A description of the state.

        - **Type** *(string) --*

          The type of load balancer.

        - **AvailabilityZones** *(list) --*

          The Availability Zones for the load balancer.

          - *(dict) --*

            Information about an Availability Zone.

            - **ZoneName** *(string) --*

              The name of the Availability Zone.

            - **SubnetId** *(string) --*

              The ID of the subnet. You can specify one subnet per Availability Zone.

            - **LoadBalancerAddresses** *(list) --*

              [Network Load Balancers] If you need static IP addresses for your load balancer, you
              can specify one Elastic IP address per Availability Zone when you create the load
              balancer.

              - *(dict) --*

                Information about a static IP address for a load balancer.

                - **IpAddress** *(string) --*

                  The static IP address.

                - **AllocationId** *(string) --*

                  [Network Load Balancers] The allocation ID of the Elastic IP address.

        - **SecurityGroups** *(list) --*

          The IDs of the security groups for the load balancer.

          - *(string) --*

        - **IpAddressType** *(string) --*

          The type of IP addresses used by the subnets for your load balancer. The possible values
          are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
    """


_ClientCreateLoadBalancerSubnetMappingsTypeDef = TypedDict(
    "_ClientCreateLoadBalancerSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str},
    total=False,
)


class ClientCreateLoadBalancerSubnetMappingsTypeDef(
    _ClientCreateLoadBalancerSubnetMappingsTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancer` `SubnetMappings`

    Information about a subnet mapping.

    - **SubnetId** *(string) --*

      The ID of the subnet.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_RequiredClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateLoadBalancerTagsTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateLoadBalancerTagsTypeDef(
    _RequiredClientCreateLoadBalancerTagsTypeDef,
    _OptionalClientCreateLoadBalancerTagsTypeDef,
):
    """
    Type definition for `ClientCreateLoadBalancer` `Tags`

    Information about a tag.

    - **Key** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_RequiredClientCreateRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalClientCreateRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef(
    _RequiredClientCreateRuleActionsAuthenticateCognitoConfigTypeDef,
    _OptionalClientCreateRuleActionsAuthenticateCognitoConfigTypeDef,
):
    """
    Type definition for `ClientCreateRuleActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
    when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --* **[REQUIRED]**

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --* **[REQUIRED]**

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.
    """


_RequiredClientCreateRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalClientCreateRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateRuleActionsAuthenticateOidcConfigTypeDef(
    _RequiredClientCreateRuleActionsAuthenticateOidcConfigTypeDef,
    _OptionalClientCreateRuleActionsAuthenticateOidcConfigTypeDef,
):
    """
    Type definition for `ClientCreateRuleActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with OpenID
    Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --* **[REQUIRED]**

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --* **[REQUIRED]**

      The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
      domain, and the path.

    - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
      the domain, and the path.

    - **ClientId** *(string) --* **[REQUIRED]**

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
      are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
      true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you are
      creating a rule, you can omit this parameter or set it to false.
    """


_RequiredClientCreateRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsFixedResponseConfigTypeDef", {"StatusCode": str}
)
_OptionalClientCreateRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
    total=False,
)


class ClientCreateRuleActionsFixedResponseConfigTypeDef(
    _RequiredClientCreateRuleActionsFixedResponseConfigTypeDef,
    _OptionalClientCreateRuleActionsFixedResponseConfigTypeDef,
):
    """
    Type definition for `ClientCreateRuleActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom HTTP
    response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript | application/json
    """


_ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed to the
      same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateRuleActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups in a
    forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientCreateRuleActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientCreateRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientCreateRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleActionsForwardConfigTypeDef(
    _ClientCreateRuleActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target groups.
    For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
    is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
    specify only one target group using ``ForwardConfig`` and it must be the same target group
    specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single target
      group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups in a
        forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed to the
        same target group. The range is 1-604800 seconds (7 days).
    """


_RequiredClientCreateRuleActionsRedirectConfigTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsRedirectConfigTypeDef", {"StatusCode": str}
)
_OptionalClientCreateRuleActionsRedirectConfigTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsRedirectConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class ClientCreateRuleActionsRedirectConfigTypeDef(
    _RequiredClientCreateRuleActionsRedirectConfigTypeDef,
    _OptionalClientCreateRuleActionsRedirectConfigTypeDef,
):
    """
    Type definition for `ClientCreateRuleActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only when
    ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
      HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not percent-encoded.
      The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
      the leading "?", as it is automatically added. You can specify any of the reserved keywords.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
    """


_RequiredClientCreateRuleActionsTypeDef = TypedDict(
    "_RequiredClientCreateRuleActionsTypeDef", {"Type": str}
)
_OptionalClientCreateRuleActionsTypeDef = TypedDict(
    "_OptionalClientCreateRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleActionsTypeDef(
    _RequiredClientCreateRuleActionsTypeDef, _OptionalClientCreateRuleActionsTypeDef
):
    """
    Type definition for `ClientCreateRule` `Actions`

    Information about an action.

    - **Type** *(string) --* **[REQUIRED]**

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward``
      and you want to route to a single target group. To route to one or more target groups, use
      ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with OpenID
      Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --* **[REQUIRED]**

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --* **[REQUIRED]**

        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
        domain, and the path.

      - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
        the domain, and the path.

      - **ClientId** *(string) --* **[REQUIRED]**

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
        are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
        true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you are
        creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
      when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --* **[REQUIRED]**

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --* **[REQUIRED]**

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The action
      with the lowest value for order is performed first. The last action to be performed must be
      one of the following types of actions: a ``forward`` , ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only when
      ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
        HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not percent-encoded.
        The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
        the leading "?", as it is automatically added. You can specify any of the reserved keywords.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom HTTP
      response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript | application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target groups.
      For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
      is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
      specify only one target group using ``ForwardConfig`` and it must be the same target group
      specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single target
        group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups in a
          forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed to the
          same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsHostHeaderConfigTypeDef(
    _ClientCreateRuleConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The comparison is
      case insensitive. The following wildcard characters are supported: * (matches 0 or more
      characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the host name.

      - *(string) --*
    """


_ClientCreateRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsHttpHeaderConfigTypeDef(
    _ClientCreateRuleConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header name is
      case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not
      supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum size of
      each string is 128 characters. The comparison strings are case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly
      1 character).

      If the same header appears multiple times in the request, we search them in order until a
      match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the value of the HTTP header. To require that all of the strings are a match, create one
      condition per string.

      - *(string) --*
    """


_ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef(
    _ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed characters
      are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are
      not supported; therefore, the method name must be an exact match.

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the HTTP request method. We recommend that you route GET and HEAD requests in the same way,
      because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientCreateRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsPathPatternConfigTypeDef(
    _ClientCreateRuleConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of each
      string is 128 characters. The comparison is case sensitive. The following wildcard
      characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
      character).

      If you specify multiple strings, the condition is satisfied if one of them matches the
      request URL. The path pattern is compared only to the path of the URL, not to its query
      string. To compare against the query string, use  QueryStringConditionConfig .

      - *(string) --*
    """


_ClientCreateRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientCreateRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateRuleConditionsQueryStringConfigValuesTypeDef(
    _ClientCreateRuleConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientCreateRuleConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientCreateRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientCreateRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientCreateRuleConditionsQueryStringConfigTypeDef(
    _ClientCreateRuleConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size of each
      string is 128 characters. The comparison is case insensitive. The following wildcard
      characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
      character). To search for a literal '*' or '?' character in a query string, you must escape
      these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if one of
      them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientCreateRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientCreateRuleConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleConditionsSourceIpConfigTypeDef(
    _ClientCreateRuleConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses.
      Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP address of
      the request matches one of the CIDR blocks. This condition is not satisfied by the
      addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For
      header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientCreateRuleConditionsTypeDef = TypedDict(
    "_ClientCreateRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleConditionsTypeDef(_ClientCreateRuleConditionsTypeDef):
    """
    Type definition for `ClientCreateRule` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header`` and
      ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for ``host-header``
      conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in length, and
      can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for example,
      /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can
      contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The comparison is
        case insensitive. The following wildcard characters are supported: * (matches 0 or more
        characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of each
        string is 128 characters. The comparison is case sensitive. The following wildcard
        characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
        character).

        If you specify multiple strings, the condition is satisfied if one of them matches the
        request URL. The path pattern is compared only to the path of the URL, not to its query
        string. To compare against the query string, use  QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header name is
        case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not
        supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum size of
        each string is 128 characters. The comparison strings are case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly
        1 character).

        If the same header appears multiple times in the request, we search them in order until a
        match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the value of the HTTP header. To require that all of the strings are a match, create one
        condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size of each
        string is 128 characters. The comparison is case insensitive. The following wildcard
        characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
        character). To search for a literal '*' or '?' character in a query string, you must escape
        these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if one of
        them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed characters
        are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are
        not supported; therefore, the method name must be an exact match.

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the HTTP request method. We recommend that you route GET and HEAD requests in the same way,
        because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses.
        Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP address of
        the request matches one of the CIDR blocks. This condition is not satisfied by the
        addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For
        header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientCreateRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientCreateRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsForwardConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef(
    _ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientCreateRuleResponseRulesActionsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientCreateRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientCreateRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientCreateRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientCreateRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientCreateRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesActionsTypeDef(
    _ClientCreateRuleResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRules` `Actions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is
    ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The
      comparison is case insensitive. The following wildcard characters are supported: *
      (matches 0 or more characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the host name.

      - *(string) --*
    """


_ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is
    ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header
      name is case insensitive. The allowed characters are specified by RFC 7230.
      Wildcards are not supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum
      size of each string is 128 characters. The comparison strings are case insensitive.
      The following wildcard characters are supported: * (matches 0 or more characters)
      and ? (matches exactly 1 character).

      If the same header appears multiple times in the request, we search them in order
      until a match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the value of the HTTP header. To require that all of the strings are a
      match, create one condition per string.

      - *(string) --*
    """


_ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed
      characters are A-Z, hyphen (-), and underscore (_). The comparison is case
      sensitive. Wildcards are not supported; therefore, the method name must be an exact
      match.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the HTTP request method. We recommend that you route GET and HEAD requests
      in the same way, because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is
    ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of
      each string is 128 characters. The comparison is case sensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of them matches
      the request URL. The path pattern is compared only to the path of the URL, not to
      its query string. To compare against the query string, use
      QueryStringConditionConfig .

      - *(string) --*
    """


_ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {
        "Values": List[
            ClientCreateRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
        ]
    },
    total=False,
)


class ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is
    ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size
      of each string is 128 characters. The comparison is case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character). To search for a literal '*' or '?' character in a query
      string, you must escape these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if
      one of them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRulesConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
      addresses. Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP
      address of the request matches one of the CIDR blocks. This condition is not
      satisfied by the addresses in the X-Forwarded-For header. To search for addresses
      in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientCreateRuleResponseRulesConditionsTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientCreateRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientCreateRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientCreateRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientCreateRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientCreateRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientCreateRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientCreateRuleResponseRulesConditionsTypeDef(
    _ClientCreateRuleResponseRulesConditionsTypeDef
):
    """
    Type definition for `ClientCreateRuleResponseRules` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header``
      and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
      ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
      example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is
      ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The
        comparison is case insensitive. The following wildcard characters are supported: *
        (matches 0 or more characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is
      ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of
        each string is 128 characters. The comparison is case sensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of them matches
        the request URL. The path pattern is compared only to the path of the URL, not to
        its query string. To compare against the query string, use
        QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is
      ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header
        name is case insensitive. The allowed characters are specified by RFC 7230.
        Wildcards are not supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum
        size of each string is 128 characters. The comparison strings are case insensitive.
        The following wildcard characters are supported: * (matches 0 or more characters)
        and ? (matches exactly 1 character).

        If the same header appears multiple times in the request, we search them in order
        until a match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the value of the HTTP header. To require that all of the strings are a
        match, create one condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is
      ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size
        of each string is 128 characters. The comparison is case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character). To search for a literal '*' or '?' character in a query
        string, you must escape these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if
        one of them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed
        characters are A-Z, hyphen (-), and underscore (_). The comparison is case
        sensitive. Wildcards are not supported; therefore, the method name must be an exact
        match.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the HTTP request method. We recommend that you route GET and HEAD requests
        in the same way, because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
        addresses. Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP
        address of the request matches one of the CIDR blocks. This condition is not
        satisfied by the addresses in the X-Forwarded-For header. To search for addresses
        in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientCreateRuleResponseRulesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientCreateRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientCreateRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientCreateRuleResponseRulesTypeDef(_ClientCreateRuleResponseRulesTypeDef):
    """
    Type definition for `ClientCreateRuleResponse` `Rules`

    Information about a rule.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(string) --*

      The priority.

    - **Conditions** *(list) --*

      The conditions. Each rule can include zero or one of the following conditions:
      ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
      zero or more of the following conditions: ``http-header`` and ``query-string`` .

      - *(dict) --*

        Information about a condition for a rule.

        - **Field** *(string) --*

          The field in the HTTP request. The following are the possible values:

          * ``http-header``

          * ``http-request-method``

          * ``host-header``

          * ``path-pattern``

          * ``query-string``

          * ``source-ip``

        - **Values** *(list) --*

          The condition value. You can use ``Values`` if the rule contains only ``host-header``
          and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
          ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

          If ``Field`` is ``host-header`` , you can specify a single host name (for example,
          my.example.com). A host name is case insensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * - .

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
          example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * _ - . $ / ~ " ' @ : +

          * & (using &amp;)

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          - *(string) --*

        - **HostHeaderConfig** *(dict) --*

          Information for a host header condition. Specify only when ``Field`` is
          ``host-header`` .

          - **Values** *(list) --*

            One or more host names. The maximum size of each name is 128 characters. The
            comparison is case insensitive. The following wildcard characters are supported: *
            (matches 0 or more characters) and ? (matches exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the host name.

            - *(string) --*

        - **PathPatternConfig** *(dict) --*

          Information for a path pattern condition. Specify only when ``Field`` is
          ``path-pattern`` .

          - **Values** *(list) --*

            One or more path patterns to compare against the request URL. The maximum size of
            each string is 128 characters. The comparison is case sensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of them matches
            the request URL. The path pattern is compared only to the path of the URL, not to
            its query string. To compare against the query string, use
            QueryStringConditionConfig .

            - *(string) --*

        - **HttpHeaderConfig** *(dict) --*

          Information for an HTTP header condition. Specify only when ``Field`` is
          ``http-header`` .

          - **HttpHeaderName** *(string) --*

            The name of the HTTP header field. The maximum size is 40 characters. The header
            name is case insensitive. The allowed characters are specified by RFC 7230.
            Wildcards are not supported.

            You can't use an HTTP header condition to specify the host header. Use
            HostHeaderConditionConfig to specify a host header condition.

          - **Values** *(list) --*

            One or more strings to compare against the value of the HTTP header. The maximum
            size of each string is 128 characters. The comparison strings are case insensitive.
            The following wildcard characters are supported: * (matches 0 or more characters)
            and ? (matches exactly 1 character).

            If the same header appears multiple times in the request, we search them in order
            until a match is found.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the value of the HTTP header. To require that all of the strings are a
            match, create one condition per string.

            - *(string) --*

        - **QueryStringConfig** *(dict) --*

          Information for a query string condition. Specify only when ``Field`` is
          ``query-string`` .

          - **Values** *(list) --*

            One or more key/value pairs or values to find in the query string. The maximum size
            of each string is 128 characters. The comparison is case insensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character). To search for a literal '*' or '?' character in a query
            string, you must escape these characters in ``Values`` using a '\\' character.

            If you specify multiple key/value pairs or values, the condition is satisfied if
            one of them is found in the query string.

            - *(dict) --*

              Information about a key/value pair.

              - **Key** *(string) --*

                The key. You can omit the key.

              - **Value** *(string) --*

                The value.

        - **HttpRequestMethodConfig** *(dict) --*

          Information for an HTTP method condition. Specify only when ``Field`` is
          ``http-request-method`` .

          - **Values** *(list) --*

            The name of the request method. The maximum size is 40 characters. The allowed
            characters are A-Z, hyphen (-), and underscore (_). The comparison is case
            sensitive. Wildcards are not supported; therefore, the method name must be an exact
            match.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the HTTP request method. We recommend that you route GET and HEAD requests
            in the same way, because the response to a HEAD request may be cached.

            - *(string) --*

        - **SourceIpConfig** *(dict) --*

          Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

          - **Values** *(list) --*

            One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
            addresses. Wildcards are not supported.

            If you specify multiple addresses, the condition is satisfied if the source IP
            address of the request matches one of the CIDR blocks. This condition is not
            satisfied by the addresses in the X-Forwarded-For header. To search for addresses
            in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

            - *(string) --*

    - **Actions** *(list) --*

      The actions. Each rule must include exactly one of the following types of actions:
      ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
      performed.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).

    - **IsDefault** *(boolean) --*

      Indicates whether this is the default rule.
    """


_ClientCreateRuleResponseTypeDef = TypedDict(
    "_ClientCreateRuleResponseTypeDef",
    {"Rules": List[ClientCreateRuleResponseRulesTypeDef]},
    total=False,
)


class ClientCreateRuleResponseTypeDef(_ClientCreateRuleResponseTypeDef):
    """
    Type definition for `ClientCreateRule` `Response`

    - **Rules** *(list) --*

      Information about the rule.

      - *(dict) --*

        Information about a rule.

        - **RuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **Priority** *(string) --*

          The priority.

        - **Conditions** *(list) --*

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
          zero or more of the following conditions: ``http-header`` and ``query-string`` .

          - *(dict) --*

            Information about a condition for a rule.

            - **Field** *(string) --*

              The field in the HTTP request. The following are the possible values:

              * ``http-header``

              * ``http-request-method``

              * ``host-header``

              * ``path-pattern``

              * ``query-string``

              * ``source-ip``

            - **Values** *(list) --*

              The condition value. You can use ``Values`` if the rule contains only ``host-header``
              and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
              ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

              If ``Field`` is ``host-header`` , you can specify a single host name (for example,
              my.example.com). A host name is case insensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * - .

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
              example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * _ - . $ / ~ " ' @ : +

              * & (using &amp;)

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              - *(string) --*

            - **HostHeaderConfig** *(dict) --*

              Information for a host header condition. Specify only when ``Field`` is
              ``host-header`` .

              - **Values** *(list) --*

                One or more host names. The maximum size of each name is 128 characters. The
                comparison is case insensitive. The following wildcard characters are supported: *
                (matches 0 or more characters) and ? (matches exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the host name.

                - *(string) --*

            - **PathPatternConfig** *(dict) --*

              Information for a path pattern condition. Specify only when ``Field`` is
              ``path-pattern`` .

              - **Values** *(list) --*

                One or more path patterns to compare against the request URL. The maximum size of
                each string is 128 characters. The comparison is case sensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of them matches
                the request URL. The path pattern is compared only to the path of the URL, not to
                its query string. To compare against the query string, use
                QueryStringConditionConfig .

                - *(string) --*

            - **HttpHeaderConfig** *(dict) --*

              Information for an HTTP header condition. Specify only when ``Field`` is
              ``http-header`` .

              - **HttpHeaderName** *(string) --*

                The name of the HTTP header field. The maximum size is 40 characters. The header
                name is case insensitive. The allowed characters are specified by RFC 7230.
                Wildcards are not supported.

                You can't use an HTTP header condition to specify the host header. Use
                HostHeaderConditionConfig to specify a host header condition.

              - **Values** *(list) --*

                One or more strings to compare against the value of the HTTP header. The maximum
                size of each string is 128 characters. The comparison strings are case insensitive.
                The following wildcard characters are supported: * (matches 0 or more characters)
                and ? (matches exactly 1 character).

                If the same header appears multiple times in the request, we search them in order
                until a match is found.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the value of the HTTP header. To require that all of the strings are a
                match, create one condition per string.

                - *(string) --*

            - **QueryStringConfig** *(dict) --*

              Information for a query string condition. Specify only when ``Field`` is
              ``query-string`` .

              - **Values** *(list) --*

                One or more key/value pairs or values to find in the query string. The maximum size
                of each string is 128 characters. The comparison is case insensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character). To search for a literal '*' or '?' character in a query
                string, you must escape these characters in ``Values`` using a '\\' character.

                If you specify multiple key/value pairs or values, the condition is satisfied if
                one of them is found in the query string.

                - *(dict) --*

                  Information about a key/value pair.

                  - **Key** *(string) --*

                    The key. You can omit the key.

                  - **Value** *(string) --*

                    The value.

            - **HttpRequestMethodConfig** *(dict) --*

              Information for an HTTP method condition. Specify only when ``Field`` is
              ``http-request-method`` .

              - **Values** *(list) --*

                The name of the request method. The maximum size is 40 characters. The allowed
                characters are A-Z, hyphen (-), and underscore (_). The comparison is case
                sensitive. Wildcards are not supported; therefore, the method name must be an exact
                match.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the HTTP request method. We recommend that you route GET and HEAD requests
                in the same way, because the response to a HEAD request may be cached.

                - *(string) --*

            - **SourceIpConfig** *(dict) --*

              Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

              - **Values** *(list) --*

                One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
                addresses. Wildcards are not supported.

                If you specify multiple addresses, the condition is satisfied if the source IP
                address of the request matches one of the CIDR blocks. This condition is not
                satisfied by the addresses in the X-Forwarded-For header. To search for addresses
                in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

                - *(string) --*

        - **Actions** *(list) --*

          The actions. Each rule must include exactly one of the following types of actions:
          ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
          performed.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

        - **IsDefault** *(boolean) --*

          Indicates whether this is the default rule.
    """


_ClientCreateTargetGroupMatcherTypeDef = TypedDict(
    "_ClientCreateTargetGroupMatcherTypeDef", {"HttpCode": str}
)


class ClientCreateTargetGroupMatcherTypeDef(_ClientCreateTargetGroupMatcherTypeDef):
    """
    Type definition for `ClientCreateTargetGroup` `Matcher`

    [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
    target.

    - **HttpCode** *(string) --* **[REQUIRED]**

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the default
      value is 200. You can specify multiple values (for example, "200,202") or a range of values
      (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef",
    {"HttpCode": str},
    total=False,
)


class ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef(
    _ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef
):
    """
    Type definition for `ClientCreateTargetGroupResponseTargetGroups` `Matcher`

    The HTTP codes to use when checking for a successful response from a target.

    - **HttpCode** *(string) --*

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the
      default value is 200. You can specify multiple values (for example, "200,202") or a
      range of values (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_ClientCreateTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": str,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientCreateTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": str,
    },
    total=False,
)


class ClientCreateTargetGroupResponseTargetGroupsTypeDef(
    _ClientCreateTargetGroupResponseTargetGroupsTypeDef
):
    """
    Type definition for `ClientCreateTargetGroupResponse` `TargetGroups`

    Information about a target group.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **TargetGroupName** *(string) --*

      The name of the target group.

    - **Protocol** *(string) --*

      The protocol to use for routing traffic to the targets.

    - **Port** *(integer) --*

      The port on which the targets are listening. Not used if the target is a Lambda function.

    - **VpcId** *(string) --*

      The ID of the VPC for the targets.

    - **HealthCheckProtocol** *(string) --*

      The protocol to use to connect with the target.

    - **HealthCheckPort** *(string) --*

      The port to use to connect with the target.

    - **HealthCheckEnabled** *(boolean) --*

      Indicates whether health checks are enabled.

    - **HealthCheckIntervalSeconds** *(integer) --*

      The approximate amount of time, in seconds, between health checks of an individual target.

    - **HealthCheckTimeoutSeconds** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

    - **HealthyThresholdCount** *(integer) --*

      The number of consecutive health checks successes required before considering an
      unhealthy target healthy.

    - **UnhealthyThresholdCount** *(integer) --*

      The number of consecutive health check failures required before considering the target
      unhealthy.

    - **HealthCheckPath** *(string) --*

      The destination for the health check request.

    - **Matcher** *(dict) --*

      The HTTP codes to use when checking for a successful response from a target.

      - **HttpCode** *(string) --*

        The HTTP codes.

        For Application Load Balancers, you can specify values between 200 and 499, and the
        default value is 200. You can specify multiple values (for example, "200,202") or a
        range of values (for example, "200-299").

        For Network Load Balancers, this is 200–399.

    - **LoadBalancerArns** *(list) --*

      The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
      group.

      - *(string) --*

    - **TargetType** *(string) --*

      The type of target that you must specify when registering targets with this target group.
      The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
      (targets are specified by IP address).
    """


_ClientCreateTargetGroupResponseTypeDef = TypedDict(
    "_ClientCreateTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientCreateTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)


class ClientCreateTargetGroupResponseTypeDef(_ClientCreateTargetGroupResponseTypeDef):
    """
    Type definition for `ClientCreateTargetGroup` `Response`

    - **TargetGroups** *(list) --*

      Information about the target group.

      - *(dict) --*

        Information about a target group.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **TargetGroupName** *(string) --*

          The name of the target group.

        - **Protocol** *(string) --*

          The protocol to use for routing traffic to the targets.

        - **Port** *(integer) --*

          The port on which the targets are listening. Not used if the target is a Lambda function.

        - **VpcId** *(string) --*

          The ID of the VPC for the targets.

        - **HealthCheckProtocol** *(string) --*

          The protocol to use to connect with the target.

        - **HealthCheckPort** *(string) --*

          The port to use to connect with the target.

        - **HealthCheckEnabled** *(boolean) --*

          Indicates whether health checks are enabled.

        - **HealthCheckIntervalSeconds** *(integer) --*

          The approximate amount of time, in seconds, between health checks of an individual target.

        - **HealthCheckTimeoutSeconds** *(integer) --*

          The amount of time, in seconds, during which no response means a failed health check.

        - **HealthyThresholdCount** *(integer) --*

          The number of consecutive health checks successes required before considering an
          unhealthy target healthy.

        - **UnhealthyThresholdCount** *(integer) --*

          The number of consecutive health check failures required before considering the target
          unhealthy.

        - **HealthCheckPath** *(string) --*

          The destination for the health check request.

        - **Matcher** *(dict) --*

          The HTTP codes to use when checking for a successful response from a target.

          - **HttpCode** *(string) --*

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the
            default value is 200. You can specify multiple values (for example, "200,202") or a
            range of values (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        - **LoadBalancerArns** *(list) --*

          The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
          group.

          - *(string) --*

        - **TargetType** *(string) --*

          The type of target that you must specify when registering targets with this target group.
          The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
          (targets are specified by IP address).
    """


_RequiredClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientDeregisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientDeregisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientDeregisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDeregisterTargetsTargetsTypeDef(
    _RequiredClientDeregisterTargetsTargetsTypeDef,
    _OptionalClientDeregisterTargetsTargetsTypeDef,
):
    """
    Type definition for `ClientDeregisterTargets` `Targets`

    Information about a target.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the target. If the target type of the target group is ``instance`` , specify an
      instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
      ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic from
      the load balancer nodes in the specified Availability Zone or from all enabled Availability
      Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the target
      group, the Availability Zone is automatically detected and this parameter is optional. If the
      IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is outside
      the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported value is
      ``all`` .
    """


_ClientDescribeAccountLimitsResponseLimitsTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseLimitsTypeDef",
    {"Name": str, "Max": str},
    total=False,
)


class ClientDescribeAccountLimitsResponseLimitsTypeDef(
    _ClientDescribeAccountLimitsResponseLimitsTypeDef
):
    """
    Type definition for `ClientDescribeAccountLimitsResponse` `Limits`

    Information about an Elastic Load Balancing resource limit for your AWS account.

    - **Name** *(string) --*

      The name of the limit. The possible values are:

      * application-load-balancers

      * listeners-per-application-load-balancer

      * listeners-per-network-load-balancer

      * network-load-balancers

      * rules-per-application-load-balancer

      * target-groups

      * target-groups-per-action-on-application-load-balancer

      * target-groups-per-action-on-network-load-balancer

      * target-groups-per-application-load-balancer

      * targets-per-application-load-balancer

      * targets-per-availability-zone-per-network-load-balancer

      * targets-per-network-load-balancer

    - **Max** *(string) --*

      The maximum value of the limit.
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {
        "Limits": List[ClientDescribeAccountLimitsResponseLimitsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(
    _ClientDescribeAccountLimitsResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountLimits` `Response`

    - **Limits** *(list) --*

      Information about the limits.

      - *(dict) --*

        Information about an Elastic Load Balancing resource limit for your AWS account.

        - **Name** *(string) --*

          The name of the limit. The possible values are:

          * application-load-balancers

          * listeners-per-application-load-balancer

          * listeners-per-network-load-balancer

          * network-load-balancers

          * rules-per-application-load-balancer

          * target-groups

          * target-groups-per-action-on-application-load-balancer

          * target-groups-per-action-on-network-load-balancer

          * target-groups-per-application-load-balancer

          * targets-per-application-load-balancer

          * targets-per-availability-zone-per-network-load-balancer

          * targets-per-network-load-balancer

        - **Max** *(string) --*

          The maximum value of the limit.

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeListenerCertificatesResponseCertificatesTypeDef = TypedDict(
    "_ClientDescribeListenerCertificatesResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientDescribeListenerCertificatesResponseCertificatesTypeDef(
    _ClientDescribeListenerCertificatesResponseCertificatesTypeDef
):
    """
    Type definition for `ClientDescribeListenerCertificatesResponse` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_ClientDescribeListenerCertificatesResponseTypeDef = TypedDict(
    "_ClientDescribeListenerCertificatesResponseTypeDef",
    {
        "Certificates": List[
            ClientDescribeListenerCertificatesResponseCertificatesTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeListenerCertificatesResponseTypeDef(
    _ClientDescribeListenerCertificatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeListenerCertificates` `Response`

    - **Certificates** *(list) --*

      Information about the certificates.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value when
          specifying a certificate as an input. This value is not included in the output when
          describing a listener, but is included when describing listener certificates.

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeListenersResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientDescribeListenersResponseListenersCertificatesTypeDef(
    _ClientDescribeListenersResponseListenersCertificatesTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListeners` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value
      when specifying a certificate as an input. This value is not included in the output
      when describing a listener, but is included when describing listener certificates.
    """


_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListenersDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientDescribeListenersResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersDefaultActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeListenersResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeListenersResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeListenersResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeListenersResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientDescribeListenersResponseListenersDefaultActionsTypeDef(
    _ClientDescribeListenersResponseListenersDefaultActionsTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponseListeners` `DefaultActions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeListenersResponseListenersTypeDef = TypedDict(
    "_ClientDescribeListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": str,
        "Certificates": List[
            ClientDescribeListenersResponseListenersCertificatesTypeDef
        ],
        "SslPolicy": str,
        "DefaultActions": List[
            ClientDescribeListenersResponseListenersDefaultActionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeListenersResponseListenersTypeDef(
    _ClientDescribeListenersResponseListenersTypeDef
):
    """
    Type definition for `ClientDescribeListenersResponse` `Listeners`

    Information about a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **Port** *(integer) --*

      The port on which the load balancer is listening.

    - **Protocol** *(string) --*

      The protocol for connections from clients to the load balancer.

    - **Certificates** *(list) --*

      [HTTPS or TLS listener] The default certificate for the listener.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value
          when specifying a certificate as an input. This value is not included in the output
          when describing a listener, but is included when describing listener certificates.

    - **SslPolicy** *(string) --*

      [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
      supported. The default is the current predefined security policy.

    - **DefaultActions** *(list) --*

      The default actions for the listener.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeListenersResponseTypeDef = TypedDict(
    "_ClientDescribeListenersResponseTypeDef",
    {
        "Listeners": List[ClientDescribeListenersResponseListenersTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeListenersResponseTypeDef(_ClientDescribeListenersResponseTypeDef):
    """
    Type definition for `ClientDescribeListeners` `Response`

    - **Listeners** *(list) --*

      Information about the listeners.

      - *(dict) --*

        Information about a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **Port** *(integer) --*

          The port on which the load balancer is listening.

        - **Protocol** *(string) --*

          The protocol for connections from clients to the load balancer.

        - **Certificates** *(list) --*

          [HTTPS or TLS listener] The default certificate for the listener.

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value
              when specifying a certificate as an input. This value is not included in the output
              when describing a listener, but is included when describing listener certificates.

        - **SslPolicy** *(string) --*

          [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
          supported. The default is the current predefined security policy.

        - **DefaultActions** *(list) --*

          The default actions for the listener.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponse` `Attributes`

    Information about a load balancer attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attributes are supported by both Application Load Balancers and Network
      Load Balancers:

      * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
      attribute is required if access logs are enabled. The bucket must exist in the same
      region as the load balancer and have a bucket policy that grants Elastic Load Balancing
      permissions to write to the bucket.

      * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
      logs.

      * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
      value is ``true`` or ``false`` . The default is ``false`` .

      The following attributes are supported by only Application Load Balancers:

      * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
      is 1-4000 seconds. The default is 60 seconds.

      * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
      with invalid header fields are removed by the load balancer (``true`` ) or routed to
      targets (``false`` ). The default is ``false`` .

      * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
      or ``false`` . The default is ``true`` .

      The following attributes are supported by only Network Load Balancers:

      * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
      enabled. The value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributes` `Response`

    - **Attributes** *(list) --*

      Information about the load balancer attributes.

      - *(dict) --*

        Information about a load balancer attribute.

        - **Key** *(string) --*

          The name of the attribute.

          The following attributes are supported by both Application Load Balancers and Network
          Load Balancers:

          * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
          ``true`` or ``false`` . The default is ``false`` .

          * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
          attribute is required if access logs are enabled. The bucket must exist in the same
          region as the load balancer and have a bucket policy that grants Elastic Load Balancing
          permissions to write to the bucket.

          * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
          logs.

          * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
          value is ``true`` or ``false`` . The default is ``false`` .

          The following attributes are supported by only Application Load Balancers:

          * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
          is 1-4000 seconds. The default is 60 seconds.

          * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
          with invalid header fields are removed by the load balancer (``true`` ) or routed to
          targets (``false`` ). The default is ``false`` .

          * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
          or ``false`` . The default is ``true`` .

          The following attributes are supported by only Network Load Balancers:

          * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
          enabled. The value is ``true`` or ``false`` . The default is ``false`` .

        - **Value** *(string) --*

          The value of the attribute.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZones` `LoadBalancerAddresses`

    Information about a static IP address for a load balancer.

    - **IpAddress** *(string) --*

      The static IP address.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancers` `AvailabilityZones`

    Information about an Availability Zone.

    - **ZoneName** *(string) --*

      The name of the Availability Zone.

    - **SubnetId** *(string) --*

      The ID of the subnet. You can specify one subnet per Availability Zone.

    - **LoadBalancerAddresses** *(list) --*

      [Network Load Balancers] If you need static IP addresses for your load balancer, you
      can specify one Elastic IP address per Availability Zone when you create the load
      balancer.

      - *(dict) --*

        Information about a static IP address for a load balancer.

        - **IpAddress** *(string) --*

          The static IP address.

        - **AllocationId** *(string) --*

          [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef",
    {"Code": str, "Reason": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancers` `State`

    The state of the load balancer.

    - **Code** *(string) --*

      The state code. The initial state of the load balancer is ``provisioning`` . After the
      load balancer is fully set up and ready to route traffic, its state is ``active`` . If
      the load balancer could not be set up, its state is ``failed`` .

    - **Reason** *(string) --*

      A description of the state.
    """


_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": str,
        "VpcId": str,
        "State": ClientDescribeLoadBalancersResponseLoadBalancersStateTypeDef,
        "Type": str,
        "AvailabilityZones": List[
            ClientDescribeLoadBalancersResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancersTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancersTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponse` `LoadBalancers`

    Information about a load balancer.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **DNSName** *(string) --*

      The public DNS name of the load balancer.

    - **CanonicalHostedZoneId** *(string) --*

      The ID of the Amazon Route 53 hosted zone associated with the load balancer.

    - **CreatedTime** *(datetime) --*

      The date and time the load balancer was created.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **Scheme** *(string) --*

      The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
      an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
      nodes. Therefore, Internet-facing load balancers can route requests from clients over the
      internet.

      The nodes of an internal load balancer have only private IP addresses. The DNS name of an
      internal load balancer is publicly resolvable to the private IP addresses of the nodes.
      Therefore, internal load balancers can route requests only from clients with access to
      the VPC for the load balancer.

    - **VpcId** *(string) --*

      The ID of the VPC for the load balancer.

    - **State** *(dict) --*

      The state of the load balancer.

      - **Code** *(string) --*

        The state code. The initial state of the load balancer is ``provisioning`` . After the
        load balancer is fully set up and ready to route traffic, its state is ``active`` . If
        the load balancer could not be set up, its state is ``failed`` .

      - **Reason** *(string) --*

        A description of the state.

    - **Type** *(string) --*

      The type of load balancer.

    - **AvailabilityZones** *(list) --*

      The Availability Zones for the load balancer.

      - *(dict) --*

        Information about an Availability Zone.

        - **ZoneName** *(string) --*

          The name of the Availability Zone.

        - **SubnetId** *(string) --*

          The ID of the subnet. You can specify one subnet per Availability Zone.

        - **LoadBalancerAddresses** *(list) --*

          [Network Load Balancers] If you need static IP addresses for your load balancer, you
          can specify one Elastic IP address per Availability Zone when you create the load
          balancer.

          - *(dict) --*

            Information about a static IP address for a load balancer.

            - **IpAddress** *(string) --*

              The static IP address.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.

    - **SecurityGroups** *(list) --*

      The IDs of the security groups for the load balancer.

      - *(string) --*

    - **IpAddressType** *(string) --*

      The type of IP addresses used by the subnets for your load balancer. The possible values
      are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[ClientDescribeLoadBalancersResponseLoadBalancersTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(
    _ClientDescribeLoadBalancersResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancers` `Response`

    - **LoadBalancers** *(list) --*

      Information about the load balancers.

      - *(dict) --*

        Information about a load balancer.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **DNSName** *(string) --*

          The public DNS name of the load balancer.

        - **CanonicalHostedZoneId** *(string) --*

          The ID of the Amazon Route 53 hosted zone associated with the load balancer.

        - **CreatedTime** *(datetime) --*

          The date and time the load balancer was created.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **Scheme** *(string) --*

          The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
          an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
          nodes. Therefore, Internet-facing load balancers can route requests from clients over the
          internet.

          The nodes of an internal load balancer have only private IP addresses. The DNS name of an
          internal load balancer is publicly resolvable to the private IP addresses of the nodes.
          Therefore, internal load balancers can route requests only from clients with access to
          the VPC for the load balancer.

        - **VpcId** *(string) --*

          The ID of the VPC for the load balancer.

        - **State** *(dict) --*

          The state of the load balancer.

          - **Code** *(string) --*

            The state code. The initial state of the load balancer is ``provisioning`` . After the
            load balancer is fully set up and ready to route traffic, its state is ``active`` . If
            the load balancer could not be set up, its state is ``failed`` .

          - **Reason** *(string) --*

            A description of the state.

        - **Type** *(string) --*

          The type of load balancer.

        - **AvailabilityZones** *(list) --*

          The Availability Zones for the load balancer.

          - *(dict) --*

            Information about an Availability Zone.

            - **ZoneName** *(string) --*

              The name of the Availability Zone.

            - **SubnetId** *(string) --*

              The ID of the subnet. You can specify one subnet per Availability Zone.

            - **LoadBalancerAddresses** *(list) --*

              [Network Load Balancers] If you need static IP addresses for your load balancer, you
              can specify one Elastic IP address per Availability Zone when you create the load
              balancer.

              - *(dict) --*

                Information about a static IP address for a load balancer.

                - **IpAddress** *(string) --*

                  The static IP address.

                - **AllocationId** *(string) --*

                  [Network Load Balancers] The allocation ID of the Elastic IP address.

        - **SecurityGroups** *(list) --*

          The IDs of the security groups for the load balancer.

          - *(string) --*

        - **IpAddressType** *(string) --*

          The type of IP addresses used by the subnets for your load balancer. The possible values
          are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef(
    _ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientDescribeRulesResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientDescribeRulesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientDescribeRulesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientDescribeRulesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientDescribeRulesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientDescribeRulesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesActionsTypeDef(
    _ClientDescribeRulesResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRules` `Actions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is
    ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The
      comparison is case insensitive. The following wildcard characters are supported: *
      (matches 0 or more characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the host name.

      - *(string) --*
    """


_ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is
    ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header
      name is case insensitive. The allowed characters are specified by RFC 7230.
      Wildcards are not supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum
      size of each string is 128 characters. The comparison strings are case insensitive.
      The following wildcard characters are supported: * (matches 0 or more characters)
      and ? (matches exactly 1 character).

      If the same header appears multiple times in the request, we search them in order
      until a match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the value of the HTTP header. To require that all of the strings are a
      match, create one condition per string.

      - *(string) --*
    """


_ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed
      characters are A-Z, hyphen (-), and underscore (_). The comparison is case
      sensitive. Wildcards are not supported; therefore, the method name must be an exact
      match.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the HTTP request method. We recommend that you route GET and HEAD requests
      in the same way, because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is
    ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of
      each string is 128 characters. The comparison is case sensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of them matches
      the request URL. The path pattern is compared only to the path of the URL, not to
      its query string. To compare against the query string, use
      QueryStringConditionConfig .

      - *(string) --*
    """


_ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef",
    {
        "Values": List[
            ClientDescribeRulesResponseRulesConditionsQueryStringConfigValuesTypeDef
        ]
    },
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is
    ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size
      of each string is 128 characters. The comparison is case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character). To search for a literal '*' or '?' character in a query
      string, you must escape these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if
      one of them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRulesConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
      addresses. Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP
      address of the request matches one of the CIDR blocks. This condition is not
      satisfied by the addresses in the X-Forwarded-For header. To search for addresses
      in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientDescribeRulesResponseRulesConditionsTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientDescribeRulesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientDescribeRulesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientDescribeRulesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientDescribeRulesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientDescribeRulesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientDescribeRulesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesConditionsTypeDef(
    _ClientDescribeRulesResponseRulesConditionsTypeDef
):
    """
    Type definition for `ClientDescribeRulesResponseRules` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header``
      and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
      ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
      example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is
      ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The
        comparison is case insensitive. The following wildcard characters are supported: *
        (matches 0 or more characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is
      ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of
        each string is 128 characters. The comparison is case sensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of them matches
        the request URL. The path pattern is compared only to the path of the URL, not to
        its query string. To compare against the query string, use
        QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is
      ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header
        name is case insensitive. The allowed characters are specified by RFC 7230.
        Wildcards are not supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum
        size of each string is 128 characters. The comparison strings are case insensitive.
        The following wildcard characters are supported: * (matches 0 or more characters)
        and ? (matches exactly 1 character).

        If the same header appears multiple times in the request, we search them in order
        until a match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the value of the HTTP header. To require that all of the strings are a
        match, create one condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is
      ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size
        of each string is 128 characters. The comparison is case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character). To search for a literal '*' or '?' character in a query
        string, you must escape these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if
        one of them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed
        characters are A-Z, hyphen (-), and underscore (_). The comparison is case
        sensitive. Wildcards are not supported; therefore, the method name must be an exact
        match.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the HTTP request method. We recommend that you route GET and HEAD requests
        in the same way, because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
        addresses. Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP
        address of the request matches one of the CIDR blocks. This condition is not
        satisfied by the addresses in the X-Forwarded-For header. To search for addresses
        in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientDescribeRulesResponseRulesTypeDef = TypedDict(
    "_ClientDescribeRulesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientDescribeRulesResponseRulesConditionsTypeDef],
        "Actions": List[ClientDescribeRulesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientDescribeRulesResponseRulesTypeDef(_ClientDescribeRulesResponseRulesTypeDef):
    """
    Type definition for `ClientDescribeRulesResponse` `Rules`

    Information about a rule.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(string) --*

      The priority.

    - **Conditions** *(list) --*

      The conditions. Each rule can include zero or one of the following conditions:
      ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
      zero or more of the following conditions: ``http-header`` and ``query-string`` .

      - *(dict) --*

        Information about a condition for a rule.

        - **Field** *(string) --*

          The field in the HTTP request. The following are the possible values:

          * ``http-header``

          * ``http-request-method``

          * ``host-header``

          * ``path-pattern``

          * ``query-string``

          * ``source-ip``

        - **Values** *(list) --*

          The condition value. You can use ``Values`` if the rule contains only ``host-header``
          and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
          ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

          If ``Field`` is ``host-header`` , you can specify a single host name (for example,
          my.example.com). A host name is case insensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * - .

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
          example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * _ - . $ / ~ " ' @ : +

          * & (using &amp;)

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          - *(string) --*

        - **HostHeaderConfig** *(dict) --*

          Information for a host header condition. Specify only when ``Field`` is
          ``host-header`` .

          - **Values** *(list) --*

            One or more host names. The maximum size of each name is 128 characters. The
            comparison is case insensitive. The following wildcard characters are supported: *
            (matches 0 or more characters) and ? (matches exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the host name.

            - *(string) --*

        - **PathPatternConfig** *(dict) --*

          Information for a path pattern condition. Specify only when ``Field`` is
          ``path-pattern`` .

          - **Values** *(list) --*

            One or more path patterns to compare against the request URL. The maximum size of
            each string is 128 characters. The comparison is case sensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of them matches
            the request URL. The path pattern is compared only to the path of the URL, not to
            its query string. To compare against the query string, use
            QueryStringConditionConfig .

            - *(string) --*

        - **HttpHeaderConfig** *(dict) --*

          Information for an HTTP header condition. Specify only when ``Field`` is
          ``http-header`` .

          - **HttpHeaderName** *(string) --*

            The name of the HTTP header field. The maximum size is 40 characters. The header
            name is case insensitive. The allowed characters are specified by RFC 7230.
            Wildcards are not supported.

            You can't use an HTTP header condition to specify the host header. Use
            HostHeaderConditionConfig to specify a host header condition.

          - **Values** *(list) --*

            One or more strings to compare against the value of the HTTP header. The maximum
            size of each string is 128 characters. The comparison strings are case insensitive.
            The following wildcard characters are supported: * (matches 0 or more characters)
            and ? (matches exactly 1 character).

            If the same header appears multiple times in the request, we search them in order
            until a match is found.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the value of the HTTP header. To require that all of the strings are a
            match, create one condition per string.

            - *(string) --*

        - **QueryStringConfig** *(dict) --*

          Information for a query string condition. Specify only when ``Field`` is
          ``query-string`` .

          - **Values** *(list) --*

            One or more key/value pairs or values to find in the query string. The maximum size
            of each string is 128 characters. The comparison is case insensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character). To search for a literal '*' or '?' character in a query
            string, you must escape these characters in ``Values`` using a '\\' character.

            If you specify multiple key/value pairs or values, the condition is satisfied if
            one of them is found in the query string.

            - *(dict) --*

              Information about a key/value pair.

              - **Key** *(string) --*

                The key. You can omit the key.

              - **Value** *(string) --*

                The value.

        - **HttpRequestMethodConfig** *(dict) --*

          Information for an HTTP method condition. Specify only when ``Field`` is
          ``http-request-method`` .

          - **Values** *(list) --*

            The name of the request method. The maximum size is 40 characters. The allowed
            characters are A-Z, hyphen (-), and underscore (_). The comparison is case
            sensitive. Wildcards are not supported; therefore, the method name must be an exact
            match.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the HTTP request method. We recommend that you route GET and HEAD requests
            in the same way, because the response to a HEAD request may be cached.

            - *(string) --*

        - **SourceIpConfig** *(dict) --*

          Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

          - **Values** *(list) --*

            One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
            addresses. Wildcards are not supported.

            If you specify multiple addresses, the condition is satisfied if the source IP
            address of the request matches one of the CIDR blocks. This condition is not
            satisfied by the addresses in the X-Forwarded-For header. To search for addresses
            in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

            - *(string) --*

    - **Actions** *(list) --*

      The actions. Each rule must include exactly one of the following types of actions:
      ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
      performed.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).

    - **IsDefault** *(boolean) --*

      Indicates whether this is the default rule.
    """


_ClientDescribeRulesResponseTypeDef = TypedDict(
    "_ClientDescribeRulesResponseTypeDef",
    {"Rules": List[ClientDescribeRulesResponseRulesTypeDef], "NextMarker": str},
    total=False,
)


class ClientDescribeRulesResponseTypeDef(_ClientDescribeRulesResponseTypeDef):
    """
    Type definition for `ClientDescribeRules` `Response`

    - **Rules** *(list) --*

      Information about the rules.

      - *(dict) --*

        Information about a rule.

        - **RuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **Priority** *(string) --*

          The priority.

        - **Conditions** *(list) --*

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
          zero or more of the following conditions: ``http-header`` and ``query-string`` .

          - *(dict) --*

            Information about a condition for a rule.

            - **Field** *(string) --*

              The field in the HTTP request. The following are the possible values:

              * ``http-header``

              * ``http-request-method``

              * ``host-header``

              * ``path-pattern``

              * ``query-string``

              * ``source-ip``

            - **Values** *(list) --*

              The condition value. You can use ``Values`` if the rule contains only ``host-header``
              and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
              ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

              If ``Field`` is ``host-header`` , you can specify a single host name (for example,
              my.example.com). A host name is case insensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * - .

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
              example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * _ - . $ / ~ " ' @ : +

              * & (using &amp;)

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              - *(string) --*

            - **HostHeaderConfig** *(dict) --*

              Information for a host header condition. Specify only when ``Field`` is
              ``host-header`` .

              - **Values** *(list) --*

                One or more host names. The maximum size of each name is 128 characters. The
                comparison is case insensitive. The following wildcard characters are supported: *
                (matches 0 or more characters) and ? (matches exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the host name.

                - *(string) --*

            - **PathPatternConfig** *(dict) --*

              Information for a path pattern condition. Specify only when ``Field`` is
              ``path-pattern`` .

              - **Values** *(list) --*

                One or more path patterns to compare against the request URL. The maximum size of
                each string is 128 characters. The comparison is case sensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of them matches
                the request URL. The path pattern is compared only to the path of the URL, not to
                its query string. To compare against the query string, use
                QueryStringConditionConfig .

                - *(string) --*

            - **HttpHeaderConfig** *(dict) --*

              Information for an HTTP header condition. Specify only when ``Field`` is
              ``http-header`` .

              - **HttpHeaderName** *(string) --*

                The name of the HTTP header field. The maximum size is 40 characters. The header
                name is case insensitive. The allowed characters are specified by RFC 7230.
                Wildcards are not supported.

                You can't use an HTTP header condition to specify the host header. Use
                HostHeaderConditionConfig to specify a host header condition.

              - **Values** *(list) --*

                One or more strings to compare against the value of the HTTP header. The maximum
                size of each string is 128 characters. The comparison strings are case insensitive.
                The following wildcard characters are supported: * (matches 0 or more characters)
                and ? (matches exactly 1 character).

                If the same header appears multiple times in the request, we search them in order
                until a match is found.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the value of the HTTP header. To require that all of the strings are a
                match, create one condition per string.

                - *(string) --*

            - **QueryStringConfig** *(dict) --*

              Information for a query string condition. Specify only when ``Field`` is
              ``query-string`` .

              - **Values** *(list) --*

                One or more key/value pairs or values to find in the query string. The maximum size
                of each string is 128 characters. The comparison is case insensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character). To search for a literal '*' or '?' character in a query
                string, you must escape these characters in ``Values`` using a '\\' character.

                If you specify multiple key/value pairs or values, the condition is satisfied if
                one of them is found in the query string.

                - *(dict) --*

                  Information about a key/value pair.

                  - **Key** *(string) --*

                    The key. You can omit the key.

                  - **Value** *(string) --*

                    The value.

            - **HttpRequestMethodConfig** *(dict) --*

              Information for an HTTP method condition. Specify only when ``Field`` is
              ``http-request-method`` .

              - **Values** *(list) --*

                The name of the request method. The maximum size is 40 characters. The allowed
                characters are A-Z, hyphen (-), and underscore (_). The comparison is case
                sensitive. Wildcards are not supported; therefore, the method name must be an exact
                match.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the HTTP request method. We recommend that you route GET and HEAD requests
                in the same way, because the response to a HEAD request may be cached.

                - *(string) --*

            - **SourceIpConfig** *(dict) --*

              Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

              - **Values** *(list) --*

                One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
                addresses. Wildcards are not supported.

                If you specify multiple addresses, the condition is satisfied if the source IP
                address of the request matches one of the CIDR blocks. This condition is not
                satisfied by the addresses in the X-Forwarded-For header. To search for addresses
                in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

                - *(string) --*

        - **Actions** *(list) --*

          The actions. Each rule must include exactly one of the following types of actions:
          ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
          performed.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

        - **IsDefault** *(boolean) --*

          Indicates whether this is the default rule.

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef",
    {"Name": str, "Priority": int},
    total=False,
)


class ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef(
    _ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef
):
    """
    Type definition for `ClientDescribeSslPoliciesResponseSslPolicies` `Ciphers`

    Information about a cipher used in a policy.

    - **Name** *(string) --*

      The name of the cipher.

    - **Priority** *(integer) --*

      The priority of the cipher.
    """


_ClientDescribeSslPoliciesResponseSslPoliciesTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseSslPoliciesTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[ClientDescribeSslPoliciesResponseSslPoliciesCiphersTypeDef],
        "Name": str,
    },
    total=False,
)


class ClientDescribeSslPoliciesResponseSslPoliciesTypeDef(
    _ClientDescribeSslPoliciesResponseSslPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeSslPoliciesResponse` `SslPolicies`

    Information about a policy used for SSL negotiation.

    - **SslProtocols** *(list) --*

      The protocols.

      - *(string) --*

    - **Ciphers** *(list) --*

      The ciphers.

      - *(dict) --*

        Information about a cipher used in a policy.

        - **Name** *(string) --*

          The name of the cipher.

        - **Priority** *(integer) --*

          The priority of the cipher.

    - **Name** *(string) --*

      The name of the policy.
    """


_ClientDescribeSslPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeSslPoliciesResponseTypeDef",
    {
        "SslPolicies": List[ClientDescribeSslPoliciesResponseSslPoliciesTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeSslPoliciesResponseTypeDef(
    _ClientDescribeSslPoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeSslPolicies` `Response`

    - **SslPolicies** *(list) --*

      Information about the policies.

      - *(dict) --*

        Information about a policy used for SSL negotiation.

        - **SslProtocols** *(list) --*

          The protocols.

          - *(string) --*

        - **Ciphers** *(list) --*

          The ciphers.

          - *(dict) --*

            Information about a cipher used in a policy.

            - **Name** *(string) --*

              The name of the cipher.

            - **Priority** *(integer) --*

              The priority of the cipher.

        - **Name** *(string) --*

          The name of the policy.

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeTagsResponseTagDescriptionsTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeTagsResponseTagDescriptionsTagsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTagsTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponseTagDescriptions` `Tags`

    Information about a tag.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientDescribeTagsResponseTagDescriptionsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTagDescriptionsTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeTagsResponseTagDescriptionsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponse` `TagDescriptions`

    The tags associated with a resource.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **Tags** *(list) --*

      Information about the tags.

      - *(dict) --*

        Information about a tag.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"TagDescriptions": List[ClientDescribeTagsResponseTagDescriptionsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    Type definition for `ClientDescribeTags` `Response`

    - **TagDescriptions** *(list) --*

      Information about the tags.

      - *(dict) --*

        The tags associated with a resource.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **Tags** *(list) --*

          Information about the tags.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.
    """


_ClientDescribeTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientDescribeTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeTargetGroupAttributesResponseAttributesTypeDef(
    _ClientDescribeTargetGroupAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientDescribeTargetGroupAttributesResponse` `Attributes`

    Information about a target group attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attribute is supported by both Application Load Balancers and Network Load
      Balancers:

      * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
      Load Balancing to wait before changing the state of a deregistering target from
      ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
      seconds. If the target is a Lambda function, this attribute is not supported.

      The following attributes are supported by Application Load Balancers if the target is not
      a Lambda function:

      * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
      registered target receives a linearly increasing share of the traffic to the target
      group. After this time period ends, the target receives its full share of traffic. The
      range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.

      * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .

      * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
      requests from a client should be routed to the same target. After this time period
      expires, the load balancer-generated cookie is considered stale. The range is 1 second to
      1 week (604800 seconds). The default value is 1 day (86400 seconds).

      The following attribute is supported only if the target is a Lambda function.

      * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
      headers exchanged between the load balancer and the Lambda function include arrays of
      values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the
      value is ``false`` and the request contains a duplicate header field name or query
      parameter key, the load balancer uses the last value sent by the client.

      The following attribute is supported only by Network Load Balancers:

      * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
      The value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientDescribeTargetGroupAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientDescribeTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientDescribeTargetGroupAttributesResponseTypeDef(
    _ClientDescribeTargetGroupAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeTargetGroupAttributes` `Response`

    - **Attributes** *(list) --*

      Information about the target group attributes

      - *(dict) --*

        Information about a target group attribute.

        - **Key** *(string) --*

          The name of the attribute.

          The following attribute is supported by both Application Load Balancers and Network Load
          Balancers:

          * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
          Load Balancing to wait before changing the state of a deregistering target from
          ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
          seconds. If the target is a Lambda function, this attribute is not supported.

          The following attributes are supported by Application Load Balancers if the target is not
          a Lambda function:

          * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
          registered target receives a linearly increasing share of the traffic to the target
          group. After this time period ends, the target receives its full share of traffic. The
          range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.

          * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
          ``true`` or ``false`` . The default is ``false`` .

          * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .

          * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
          requests from a client should be routed to the same target. After this time period
          expires, the load balancer-generated cookie is considered stale. The range is 1 second to
          1 week (604800 seconds). The default value is 1 day (86400 seconds).

          The following attribute is supported only if the target is a Lambda function.

          * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
          headers exchanged between the load balancer and the Lambda function include arrays of
          values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the
          value is ``false`` and the request contains a duplicate header field name or query
          parameter key, the load balancer uses the last value sent by the client.

          The following attribute is supported only by Network Load Balancers:

          * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
          The value is ``true`` or ``false`` . The default is ``false`` .

        - **Value** *(string) --*

          The value of the attribute.
    """


_ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef",
    {"HttpCode": str},
    total=False,
)


class ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef(
    _ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef
):
    """
    Type definition for `ClientDescribeTargetGroupsResponseTargetGroups` `Matcher`

    The HTTP codes to use when checking for a successful response from a target.

    - **HttpCode** *(string) --*

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the
      default value is 200. You can specify multiple values (for example, "200,202") or a
      range of values (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_ClientDescribeTargetGroupsResponseTargetGroupsTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": str,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientDescribeTargetGroupsResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": str,
    },
    total=False,
)


class ClientDescribeTargetGroupsResponseTargetGroupsTypeDef(
    _ClientDescribeTargetGroupsResponseTargetGroupsTypeDef
):
    """
    Type definition for `ClientDescribeTargetGroupsResponse` `TargetGroups`

    Information about a target group.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **TargetGroupName** *(string) --*

      The name of the target group.

    - **Protocol** *(string) --*

      The protocol to use for routing traffic to the targets.

    - **Port** *(integer) --*

      The port on which the targets are listening. Not used if the target is a Lambda function.

    - **VpcId** *(string) --*

      The ID of the VPC for the targets.

    - **HealthCheckProtocol** *(string) --*

      The protocol to use to connect with the target.

    - **HealthCheckPort** *(string) --*

      The port to use to connect with the target.

    - **HealthCheckEnabled** *(boolean) --*

      Indicates whether health checks are enabled.

    - **HealthCheckIntervalSeconds** *(integer) --*

      The approximate amount of time, in seconds, between health checks of an individual target.

    - **HealthCheckTimeoutSeconds** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

    - **HealthyThresholdCount** *(integer) --*

      The number of consecutive health checks successes required before considering an
      unhealthy target healthy.

    - **UnhealthyThresholdCount** *(integer) --*

      The number of consecutive health check failures required before considering the target
      unhealthy.

    - **HealthCheckPath** *(string) --*

      The destination for the health check request.

    - **Matcher** *(dict) --*

      The HTTP codes to use when checking for a successful response from a target.

      - **HttpCode** *(string) --*

        The HTTP codes.

        For Application Load Balancers, you can specify values between 200 and 499, and the
        default value is 200. You can specify multiple values (for example, "200,202") or a
        range of values (for example, "200-299").

        For Network Load Balancers, this is 200–399.

    - **LoadBalancerArns** *(list) --*

      The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
      group.

      - *(string) --*

    - **TargetType** *(string) --*

      The type of target that you must specify when registering targets with this target group.
      The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
      (targets are specified by IP address).
    """


_ClientDescribeTargetGroupsResponseTypeDef = TypedDict(
    "_ClientDescribeTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List[ClientDescribeTargetGroupsResponseTargetGroupsTypeDef],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeTargetGroupsResponseTypeDef(
    _ClientDescribeTargetGroupsResponseTypeDef
):
    """
    Type definition for `ClientDescribeTargetGroups` `Response`

    - **TargetGroups** *(list) --*

      Information about the target groups.

      - *(dict) --*

        Information about a target group.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **TargetGroupName** *(string) --*

          The name of the target group.

        - **Protocol** *(string) --*

          The protocol to use for routing traffic to the targets.

        - **Port** *(integer) --*

          The port on which the targets are listening. Not used if the target is a Lambda function.

        - **VpcId** *(string) --*

          The ID of the VPC for the targets.

        - **HealthCheckProtocol** *(string) --*

          The protocol to use to connect with the target.

        - **HealthCheckPort** *(string) --*

          The port to use to connect with the target.

        - **HealthCheckEnabled** *(boolean) --*

          Indicates whether health checks are enabled.

        - **HealthCheckIntervalSeconds** *(integer) --*

          The approximate amount of time, in seconds, between health checks of an individual target.

        - **HealthCheckTimeoutSeconds** *(integer) --*

          The amount of time, in seconds, during which no response means a failed health check.

        - **HealthyThresholdCount** *(integer) --*

          The number of consecutive health checks successes required before considering an
          unhealthy target healthy.

        - **UnhealthyThresholdCount** *(integer) --*

          The number of consecutive health check failures required before considering the target
          unhealthy.

        - **HealthCheckPath** *(string) --*

          The destination for the health check request.

        - **Matcher** *(dict) --*

          The HTTP codes to use when checking for a successful response from a target.

          - **HttpCode** *(string) --*

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the
            default value is 200. You can specify multiple values (for example, "200,202") or a
            range of values (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        - **LoadBalancerArns** *(list) --*

          The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
          group.

          - *(string) --*

        - **TargetType** *(string) --*

          The type of target that you must specify when registering targets with this target group.
          The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
          (targets are specified by IP address).

    - **NextMarker** *(string) --*

      If there are additional results, this is the marker for the next set of results. Otherwise,
      this is null.
    """


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef",
    {"State": str, "Reason": str, "Description": str},
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef
):
    """
    Type definition for `ClientDescribeTargetHealthResponseTargetHealthDescriptions` `TargetHealth`

    The health information for the target.

    - **State** *(string) --*

      The state of the target.

    - **Reason** *(string) --*

      The reason code.

      If the target state is ``healthy`` , a reason code is not provided.

      If the target state is ``initial`` , the reason code can be one of the following values:

      * ``Elb.RegistrationInProgress`` - The target is in the process of being registered
      with the load balancer.

      * ``Elb.InitialHealthChecking`` - The load balancer is still sending the target the
      minimum number of health checks required to determine its health status.

      If the target state is ``unhealthy`` , the reason code can be one of the following
      values:

      * ``Target.ResponseCodeMismatch`` - The health checks did not return an expected HTTP
      code. Applies only to Application Load Balancers.

      * ``Target.Timeout`` - The health check requests timed out. Applies only to Application
      Load Balancers.

      * ``Target.FailedHealthChecks`` - The load balancer received an error while
      establishing a connection to the target or the target response was malformed.

      * ``Elb.InternalError`` - The health checks failed due to an internal error. Applies
      only to Application Load Balancers.

      If the target state is ``unused`` , the reason code can be one of the following values:

      * ``Target.NotRegistered`` - The target is not registered with the target group.

      * ``Target.NotInUse`` - The target group is not used by any load balancer or the target
      is in an Availability Zone that is not enabled for its load balancer.

      * ``Target.InvalidState`` - The target is in the stopped or terminated state.

      * ``Target.IpUnusable`` - The target IP address is reserved for use by a load balancer.

      If the target state is ``draining`` , the reason code can be the following value:

      * ``Target.DeregistrationInProgress`` - The target is in the process of being
      deregistered and the deregistration delay period has not expired.

      If the target state is ``unavailable`` , the reason code can be the following value:

      * ``Target.HealthCheckDisabled`` - Health checks are disabled for the target group.
      Applies only to Application Load Balancers.

      * ``Elb.InternalError`` - Target health is unavailable due to an internal error.
      Applies only to Network Load Balancers.

    - **Description** *(string) --*

      A description of the target health that provides additional details. If the state is
      ``healthy`` , a description is not provided.
    """


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef",
    {"Id": str, "Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef
):
    """
    Type definition for `ClientDescribeTargetHealthResponseTargetHealthDescriptions` `Target`

    The description of the target.

    - **Id** *(string) --*

      The ID of the target. If the target type of the target group is ``instance`` , specify
      an instance ID. If the target type is ``ip`` , specify an IP address. If the target
      type is ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic
      from the load balancer nodes in the specified Availability Zone or from all enabled
      Availability Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the
      target group, the Availability Zone is automatically detected and this parameter is
      optional. If the IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is
      outside the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported
      value is ``all`` .
    """


_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef",
    {
        "Target": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetTypeDef,
        "HealthCheckPort": str,
        "TargetHealth": ClientDescribeTargetHealthResponseTargetHealthDescriptionsTargetHealthTypeDef,
    },
    total=False,
)


class ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef(
    _ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeTargetHealthResponse` `TargetHealthDescriptions`

    Information about the health of a target.

    - **Target** *(dict) --*

      The description of the target.

      - **Id** *(string) --*

        The ID of the target. If the target type of the target group is ``instance`` , specify
        an instance ID. If the target type is ``ip`` , specify an IP address. If the target
        type is ``lambda`` , specify the ARN of the Lambda function.

      - **Port** *(integer) --*

        The port on which the target is listening. Not used if the target is a Lambda function.

      - **AvailabilityZone** *(string) --*

        An Availability Zone or ``all`` . This determines whether the target receives traffic
        from the load balancer nodes in the specified Availability Zone or from all enabled
        Availability Zones for the load balancer.

        This parameter is not supported if the target type of the target group is ``instance`` .

        If the target type is ``ip`` and the IP address is in a subnet of the VPC for the
        target group, the Availability Zone is automatically detected and this parameter is
        optional. If the IP address is outside the VPC, this parameter is required.

        With an Application Load Balancer, if the target type is ``ip`` and the IP address is
        outside the VPC for the target group, the only supported value is ``all`` .

        If the target type is ``lambda`` , this parameter is optional and the only supported
        value is ``all`` .

    - **HealthCheckPort** *(string) --*

      The port to use to connect with the target.

    - **TargetHealth** *(dict) --*

      The health information for the target.

      - **State** *(string) --*

        The state of the target.

      - **Reason** *(string) --*

        The reason code.

        If the target state is ``healthy`` , a reason code is not provided.

        If the target state is ``initial`` , the reason code can be one of the following values:

        * ``Elb.RegistrationInProgress`` - The target is in the process of being registered
        with the load balancer.

        * ``Elb.InitialHealthChecking`` - The load balancer is still sending the target the
        minimum number of health checks required to determine its health status.

        If the target state is ``unhealthy`` , the reason code can be one of the following
        values:

        * ``Target.ResponseCodeMismatch`` - The health checks did not return an expected HTTP
        code. Applies only to Application Load Balancers.

        * ``Target.Timeout`` - The health check requests timed out. Applies only to Application
        Load Balancers.

        * ``Target.FailedHealthChecks`` - The load balancer received an error while
        establishing a connection to the target or the target response was malformed.

        * ``Elb.InternalError`` - The health checks failed due to an internal error. Applies
        only to Application Load Balancers.

        If the target state is ``unused`` , the reason code can be one of the following values:

        * ``Target.NotRegistered`` - The target is not registered with the target group.

        * ``Target.NotInUse`` - The target group is not used by any load balancer or the target
        is in an Availability Zone that is not enabled for its load balancer.

        * ``Target.InvalidState`` - The target is in the stopped or terminated state.

        * ``Target.IpUnusable`` - The target IP address is reserved for use by a load balancer.

        If the target state is ``draining`` , the reason code can be the following value:

        * ``Target.DeregistrationInProgress`` - The target is in the process of being
        deregistered and the deregistration delay period has not expired.

        If the target state is ``unavailable`` , the reason code can be the following value:

        * ``Target.HealthCheckDisabled`` - Health checks are disabled for the target group.
        Applies only to Application Load Balancers.

        * ``Elb.InternalError`` - Target health is unavailable due to an internal error.
        Applies only to Network Load Balancers.

      - **Description** *(string) --*

        A description of the target health that provides additional details. If the state is
        ``healthy`` , a description is not provided.
    """


_ClientDescribeTargetHealthResponseTypeDef = TypedDict(
    "_ClientDescribeTargetHealthResponseTypeDef",
    {
        "TargetHealthDescriptions": List[
            ClientDescribeTargetHealthResponseTargetHealthDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeTargetHealthResponseTypeDef(
    _ClientDescribeTargetHealthResponseTypeDef
):
    """
    Type definition for `ClientDescribeTargetHealth` `Response`

    - **TargetHealthDescriptions** *(list) --*

      Information about the health of the targets.

      - *(dict) --*

        Information about the health of a target.

        - **Target** *(dict) --*

          The description of the target.

          - **Id** *(string) --*

            The ID of the target. If the target type of the target group is ``instance`` , specify
            an instance ID. If the target type is ``ip`` , specify an IP address. If the target
            type is ``lambda`` , specify the ARN of the Lambda function.

          - **Port** *(integer) --*

            The port on which the target is listening. Not used if the target is a Lambda function.

          - **AvailabilityZone** *(string) --*

            An Availability Zone or ``all`` . This determines whether the target receives traffic
            from the load balancer nodes in the specified Availability Zone or from all enabled
            Availability Zones for the load balancer.

            This parameter is not supported if the target type of the target group is ``instance`` .

            If the target type is ``ip`` and the IP address is in a subnet of the VPC for the
            target group, the Availability Zone is automatically detected and this parameter is
            optional. If the IP address is outside the VPC, this parameter is required.

            With an Application Load Balancer, if the target type is ``ip`` and the IP address is
            outside the VPC for the target group, the only supported value is ``all`` .

            If the target type is ``lambda`` , this parameter is optional and the only supported
            value is ``all`` .

        - **HealthCheckPort** *(string) --*

          The port to use to connect with the target.

        - **TargetHealth** *(dict) --*

          The health information for the target.

          - **State** *(string) --*

            The state of the target.

          - **Reason** *(string) --*

            The reason code.

            If the target state is ``healthy`` , a reason code is not provided.

            If the target state is ``initial`` , the reason code can be one of the following values:

            * ``Elb.RegistrationInProgress`` - The target is in the process of being registered
            with the load balancer.

            * ``Elb.InitialHealthChecking`` - The load balancer is still sending the target the
            minimum number of health checks required to determine its health status.

            If the target state is ``unhealthy`` , the reason code can be one of the following
            values:

            * ``Target.ResponseCodeMismatch`` - The health checks did not return an expected HTTP
            code. Applies only to Application Load Balancers.

            * ``Target.Timeout`` - The health check requests timed out. Applies only to Application
            Load Balancers.

            * ``Target.FailedHealthChecks`` - The load balancer received an error while
            establishing a connection to the target or the target response was malformed.

            * ``Elb.InternalError`` - The health checks failed due to an internal error. Applies
            only to Application Load Balancers.

            If the target state is ``unused`` , the reason code can be one of the following values:

            * ``Target.NotRegistered`` - The target is not registered with the target group.

            * ``Target.NotInUse`` - The target group is not used by any load balancer or the target
            is in an Availability Zone that is not enabled for its load balancer.

            * ``Target.InvalidState`` - The target is in the stopped or terminated state.

            * ``Target.IpUnusable`` - The target IP address is reserved for use by a load balancer.

            If the target state is ``draining`` , the reason code can be the following value:

            * ``Target.DeregistrationInProgress`` - The target is in the process of being
            deregistered and the deregistration delay period has not expired.

            If the target state is ``unavailable`` , the reason code can be the following value:

            * ``Target.HealthCheckDisabled`` - Health checks are disabled for the target group.
            Applies only to Application Load Balancers.

            * ``Elb.InternalError`` - Target health is unavailable due to an internal error.
            Applies only to Network Load Balancers.

          - **Description** *(string) --*

            A description of the target health that provides additional details. If the state is
            ``healthy`` , a description is not provided.
    """


_RequiredClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_RequiredClientDescribeTargetHealthTargetsTypeDef", {"Id": str}
)
_OptionalClientDescribeTargetHealthTargetsTypeDef = TypedDict(
    "_OptionalClientDescribeTargetHealthTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientDescribeTargetHealthTargetsTypeDef(
    _RequiredClientDescribeTargetHealthTargetsTypeDef,
    _OptionalClientDescribeTargetHealthTargetsTypeDef,
):
    """
    Type definition for `ClientDescribeTargetHealth` `Targets`

    Information about a target.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the target. If the target type of the target group is ``instance`` , specify an
      instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
      ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic from
      the load balancer nodes in the specified Availability Zone or from all enabled Availability
      Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the target
      group, the Availability Zone is automatically detected and this parameter is optional. If the
      IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is outside
      the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported value is
      ``all`` .
    """


_ClientModifyListenerCertificatesTypeDef = TypedDict(
    "_ClientModifyListenerCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientModifyListenerCertificatesTypeDef(_ClientModifyListenerCertificatesTypeDef):
    """
    Type definition for `ClientModifyListener` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_RequiredClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef(
    _RequiredClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
    _OptionalClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
):
    """
    Type definition for `ClientModifyListenerDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
    when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --* **[REQUIRED]**

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --* **[REQUIRED]**

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.
    """


_RequiredClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef(
    _RequiredClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef,
    _OptionalClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef,
):
    """
    Type definition for `ClientModifyListenerDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with OpenID
    Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --* **[REQUIRED]**

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --* **[REQUIRED]**

      The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
      domain, and the path.

    - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
      the domain, and the path.

    - **ClientId** *(string) --* **[REQUIRED]**

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
      are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
      true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you are
      creating a rule, you can omit this parameter or set it to false.
    """


_RequiredClientModifyListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    {"StatusCode": str},
)
_OptionalClientModifyListenerDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
    total=False,
)


class ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef(
    _RequiredClientModifyListenerDefaultActionsFixedResponseConfigTypeDef,
    _OptionalClientModifyListenerDefaultActionsFixedResponseConfigTypeDef,
):
    """
    Type definition for `ClientModifyListenerDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom HTTP
    response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript | application/json
    """


_ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed to the
      same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientModifyListenerDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups in a
    forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientModifyListenerDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyListenerDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientModifyListenerDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientModifyListenerDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsForwardConfigTypeDef(
    _ClientModifyListenerDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target groups.
    For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
    is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
    specify only one target group using ``ForwardConfig`` and it must be the same target group
    specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single target
      group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups in a
        forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed to the
        same target group. The range is 1-604800 seconds (7 days).
    """


_RequiredClientModifyListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    {"StatusCode": str},
)
_OptionalClientModifyListenerDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsRedirectConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class ClientModifyListenerDefaultActionsRedirectConfigTypeDef(
    _RequiredClientModifyListenerDefaultActionsRedirectConfigTypeDef,
    _OptionalClientModifyListenerDefaultActionsRedirectConfigTypeDef,
):
    """
    Type definition for `ClientModifyListenerDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only when
    ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
      HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not percent-encoded.
      The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
      the leading "?", as it is automatically added. You can specify any of the reserved keywords.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
    """


_RequiredClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_RequiredClientModifyListenerDefaultActionsTypeDef", {"Type": str}
)
_OptionalClientModifyListenerDefaultActionsTypeDef = TypedDict(
    "_OptionalClientModifyListenerDefaultActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerDefaultActionsTypeDef(
    _RequiredClientModifyListenerDefaultActionsTypeDef,
    _OptionalClientModifyListenerDefaultActionsTypeDef,
):
    """
    Type definition for `ClientModifyListener` `DefaultActions`

    Information about an action.

    - **Type** *(string) --* **[REQUIRED]**

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward``
      and you want to route to a single target group. To route to one or more target groups, use
      ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with OpenID
      Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --* **[REQUIRED]**

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --* **[REQUIRED]**

        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
        domain, and the path.

      - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
        the domain, and the path.

      - **ClientId** *(string) --* **[REQUIRED]**

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
        are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
        true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you are
        creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
      when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --* **[REQUIRED]**

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --* **[REQUIRED]**

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The action
      with the lowest value for order is performed first. The last action to be performed must be
      one of the following types of actions: a ``forward`` , ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only when
      ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
        HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not percent-encoded.
        The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
        the leading "?", as it is automatically added. You can specify any of the reserved keywords.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom HTTP
      response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript | application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target groups.
      For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
      is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
      specify only one target group using ``ForwardConfig`` and it must be the same target group
      specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single target
        group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups in a
          forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed to the
          same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerResponseListenersCertificatesTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientModifyListenerResponseListenersCertificatesTypeDef(
    _ClientModifyListenerResponseListenersCertificatesTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListeners` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value
      when specifying a certificate as an input. This value is not included in the output
      when describing a listener, but is included when describing listener certificates.
    """


_ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListenersDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientModifyListenerResponseListenersDefaultActionsTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersDefaultActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyListenerResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyListenerResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyListenerResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyListenerResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyListenerResponseListenersDefaultActionsTypeDef(
    _ClientModifyListenerResponseListenersDefaultActionsTypeDef
):
    """
    Type definition for `ClientModifyListenerResponseListeners` `DefaultActions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerResponseListenersTypeDef = TypedDict(
    "_ClientModifyListenerResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": str,
        "Certificates": List[ClientModifyListenerResponseListenersCertificatesTypeDef],
        "SslPolicy": str,
        "DefaultActions": List[
            ClientModifyListenerResponseListenersDefaultActionsTypeDef
        ],
    },
    total=False,
)


class ClientModifyListenerResponseListenersTypeDef(
    _ClientModifyListenerResponseListenersTypeDef
):
    """
    Type definition for `ClientModifyListenerResponse` `Listeners`

    Information about a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **Port** *(integer) --*

      The port on which the load balancer is listening.

    - **Protocol** *(string) --*

      The protocol for connections from clients to the load balancer.

    - **Certificates** *(list) --*

      [HTTPS or TLS listener] The default certificate for the listener.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value
          when specifying a certificate as an input. This value is not included in the output
          when describing a listener, but is included when describing listener certificates.

    - **SslPolicy** *(string) --*

      [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
      supported. The default is the current predefined security policy.

    - **DefaultActions** *(list) --*

      The default actions for the listener.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyListenerResponseTypeDef = TypedDict(
    "_ClientModifyListenerResponseTypeDef",
    {"Listeners": List[ClientModifyListenerResponseListenersTypeDef]},
    total=False,
)


class ClientModifyListenerResponseTypeDef(_ClientModifyListenerResponseTypeDef):
    """
    Type definition for `ClientModifyListener` `Response`

    - **Listeners** *(list) --*

      Information about the modified listener.

      - *(dict) --*

        Information about a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **Port** *(integer) --*

          The port on which the load balancer is listening.

        - **Protocol** *(string) --*

          The protocol for connections from clients to the load balancer.

        - **Certificates** *(list) --*

          [HTTPS or TLS listener] The default certificate for the listener.

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value
              when specifying a certificate as an input. This value is not included in the output
              when describing a listener, but is included when describing listener certificates.

        - **SslPolicy** *(string) --*

          [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
          supported. The default is the current predefined security policy.

        - **DefaultActions** *(list) --*

          The default actions for the listener.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyLoadBalancerAttributesAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributes` `Attributes`

    Information about a load balancer attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attributes are supported by both Application Load Balancers and Network Load
      Balancers:

      * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute
      is required if access logs are enabled. The bucket must exist in the same region as the load
      balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to
      the bucket.

      * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
      logs.

      * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
      value is ``true`` or ``false`` . The default is ``false`` .

      The following attributes are supported by only Application Load Balancers:

      * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is
      1-4000 seconds. The default is 60 seconds.

      * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers with
      invalid header fields are removed by the load balancer (``true`` ) or routed to targets
      (``false`` ). The default is ``false`` .

      * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or
      ``false`` . The default is ``true`` .

      The following attributes are supported by only Network Load Balancers:

      * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
      enabled. The value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientModifyLoadBalancerAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponse` `Attributes`

    Information about a load balancer attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attributes are supported by both Application Load Balancers and Network
      Load Balancers:

      * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
      attribute is required if access logs are enabled. The bucket must exist in the same
      region as the load balancer and have a bucket policy that grants Elastic Load Balancing
      permissions to write to the bucket.

      * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
      logs.

      * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
      value is ``true`` or ``false`` . The default is ``false`` .

      The following attributes are supported by only Application Load Balancers:

      * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
      is 1-4000 seconds. The default is 60 seconds.

      * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
      with invalid header fields are removed by the load balancer (``true`` ) or routed to
      targets (``false`` ). The default is ``false`` .

      * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
      or ``false`` . The default is ``true`` .

      The following attributes are supported by only Network Load Balancers:

      * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
      enabled. The value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyLoadBalancerAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseTypeDef(
    _ClientModifyLoadBalancerAttributesResponseTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributes` `Response`

    - **Attributes** *(list) --*

      Information about the load balancer attributes.

      - *(dict) --*

        Information about a load balancer attribute.

        - **Key** *(string) --*

          The name of the attribute.

          The following attributes are supported by both Application Load Balancers and Network
          Load Balancers:

          * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is
          ``true`` or ``false`` . The default is ``false`` .

          * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This
          attribute is required if access logs are enabled. The bucket must exist in the same
          region as the load balancer and have a bucket policy that grants Elastic Load Balancing
          permissions to write to the bucket.

          * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access
          logs.

          * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The
          value is ``true`` or ``false`` . The default is ``false`` .

          The following attributes are supported by only Application Load Balancers:

          * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range
          is 1-4000 seconds. The default is 60 seconds.

          * ``routing.http.drop_invalid_header_fields.enabled`` - Indicates whether HTTP headers
          with invalid header fields are removed by the load balancer (``true`` ) or routed to
          targets (``false`` ). The default is ``false`` .

          * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true``
          or ``false`` . The default is ``true`` .

          The following attributes are supported by only Network Load Balancers:

          * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is
          enabled. The value is ``true`` or ``false`` . The default is ``false`` .

        - **Value** *(string) --*

          The value of the attribute.
    """


_RequiredClientModifyRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalClientModifyRuleActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsAuthenticateCognitoConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef(
    _RequiredClientModifyRuleActionsAuthenticateCognitoConfigTypeDef,
    _OptionalClientModifyRuleActionsAuthenticateCognitoConfigTypeDef,
):
    """
    Type definition for `ClientModifyRuleActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
    when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --* **[REQUIRED]**

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --* **[REQUIRED]**

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.
    """


_RequiredClientModifyRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalClientModifyRuleActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsAuthenticateOidcConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyRuleActionsAuthenticateOidcConfigTypeDef(
    _RequiredClientModifyRuleActionsAuthenticateOidcConfigTypeDef,
    _OptionalClientModifyRuleActionsAuthenticateOidcConfigTypeDef,
):
    """
    Type definition for `ClientModifyRuleActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with OpenID
    Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --* **[REQUIRED]**

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --* **[REQUIRED]**

      The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
      domain, and the path.

    - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
      the domain, and the path.

    - **ClientId** *(string) --* **[REQUIRED]**

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
      are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
      true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values, see the
      documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is 604800
      seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the authorization
      endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
      value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you are
      creating a rule, you can omit this parameter or set it to false.
    """


_RequiredClientModifyRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsFixedResponseConfigTypeDef", {"StatusCode": str}
)
_OptionalClientModifyRuleActionsFixedResponseConfigTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
    total=False,
)


class ClientModifyRuleActionsFixedResponseConfigTypeDef(
    _RequiredClientModifyRuleActionsFixedResponseConfigTypeDef,
    _OptionalClientModifyRuleActionsFixedResponseConfigTypeDef,
):
    """
    Type definition for `ClientModifyRuleActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom HTTP
    response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript | application/json
    """


_ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed to the
      same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientModifyRuleActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups in a
    forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientModifyRuleActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyRuleActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[ClientModifyRuleActionsForwardConfigTargetGroupsTypeDef],
        "TargetGroupStickinessConfig": ClientModifyRuleActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleActionsForwardConfigTypeDef(
    _ClientModifyRuleActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target groups.
    For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
    is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
    specify only one target group using ``ForwardConfig`` and it must be the same target group
    specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single target
      group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups in a
        forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed to the
        same target group. The range is 1-604800 seconds (7 days).
    """


_RequiredClientModifyRuleActionsRedirectConfigTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsRedirectConfigTypeDef", {"StatusCode": str}
)
_OptionalClientModifyRuleActionsRedirectConfigTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsRedirectConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class ClientModifyRuleActionsRedirectConfigTypeDef(
    _RequiredClientModifyRuleActionsRedirectConfigTypeDef,
    _OptionalClientModifyRuleActionsRedirectConfigTypeDef,
):
    """
    Type definition for `ClientModifyRuleActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only when
    ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
      HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not percent-encoded.
      The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
      the leading "?", as it is automatically added. You can specify any of the reserved keywords.

    - **StatusCode** *(string) --* **[REQUIRED]**

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
    """


_RequiredClientModifyRuleActionsTypeDef = TypedDict(
    "_RequiredClientModifyRuleActionsTypeDef", {"Type": str}
)
_OptionalClientModifyRuleActionsTypeDef = TypedDict(
    "_OptionalClientModifyRuleActionsTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleActionsTypeDef(
    _RequiredClientModifyRuleActionsTypeDef, _OptionalClientModifyRuleActionsTypeDef
):
    """
    Type definition for `ClientModifyRule` `Actions`

    Information about an action.

    - **Type** *(string) --* **[REQUIRED]**

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward``
      and you want to route to a single target group. To route to one or more target groups, use
      ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with OpenID
      Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --* **[REQUIRED]**

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --* **[REQUIRED]**

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --* **[REQUIRED]**

        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the
        domain, and the path.

      - **UserInfoEndpoint** *(string) --* **[REQUIRED]**

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol,
        the domain, and the path.

      - **ClientId** *(string) --* **[REQUIRED]**

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you
        are modifying a rule, you can omit this parameter if you set ``UseExistingClientSecret`` to
        true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you are
        creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only
      when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --* **[REQUIRED]**

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --* **[REQUIRED]**

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values, see the
        documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is 604800
        seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the authorization
        endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default
        value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The action
      with the lowest value for order is performed first. The last action to be performed must be
      one of the following types of actions: a ``forward`` , ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only when
      ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP,
        HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not percent-encoded.
        The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include
        the leading "?", as it is automatically added. You can specify any of the reserved keywords.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom HTTP
      response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --* **[REQUIRED]**

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript | application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target groups.
      For Network Load Balancers, you can specify a single target group. Specify only when ``Type``
      is ``forward`` . If you specify both ``ForwardConfig`` and ``TargetGroupArn`` , you can
      specify only one target group using ``ForwardConfig`` and it must be the same target group
      specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single target
        group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups in a
          forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed to the
          same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyRuleConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsHostHeaderConfigTypeDef(
    _ClientModifyRuleConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The comparison is
      case insensitive. The following wildcard characters are supported: * (matches 0 or more
      characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the host name.

      - *(string) --*
    """


_ClientModifyRuleConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsHttpHeaderConfigTypeDef(
    _ClientModifyRuleConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header name is
      case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not
      supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum size of
      each string is 128 characters. The comparison strings are case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly
      1 character).

      If the same header appears multiple times in the request, we search them in order until a
      match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the value of the HTTP header. To require that all of the strings are a match, create one
      condition per string.

      - *(string) --*
    """


_ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef(
    _ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed characters
      are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are
      not supported; therefore, the method name must be an exact match.

      If you specify multiple strings, the condition is satisfied if one of the strings matches
      the HTTP request method. We recommend that you route GET and HEAD requests in the same way,
      because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientModifyRuleConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsPathPatternConfigTypeDef(
    _ClientModifyRuleConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of each
      string is 128 characters. The comparison is case sensitive. The following wildcard
      characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
      character).

      If you specify multiple strings, the condition is satisfied if one of them matches the
      request URL. The path pattern is compared only to the path of the URL, not to its query
      string. To compare against the query string, use  QueryStringConditionConfig .

      - *(string) --*
    """


_ClientModifyRuleConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientModifyRuleConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyRuleConditionsQueryStringConfigValuesTypeDef(
    _ClientModifyRuleConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientModifyRuleConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientModifyRuleConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsQueryStringConfigTypeDef",
    {"Values": List[ClientModifyRuleConditionsQueryStringConfigValuesTypeDef]},
    total=False,
)


class ClientModifyRuleConditionsQueryStringConfigTypeDef(
    _ClientModifyRuleConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size of each
      string is 128 characters. The comparison is case insensitive. The following wildcard
      characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
      character). To search for a literal '*' or '?' character in a query string, you must escape
      these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if one of
      them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientModifyRuleConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientModifyRuleConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleConditionsSourceIpConfigTypeDef(
    _ClientModifyRuleConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses.
      Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP address of
      the request matches one of the CIDR blocks. This condition is not satisfied by the
      addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For
      header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientModifyRuleConditionsTypeDef = TypedDict(
    "_ClientModifyRuleConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleConditionsTypeDef(_ClientModifyRuleConditionsTypeDef):
    """
    Type definition for `ClientModifyRule` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header`` and
      ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for ``host-header``
      conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in length, and
      can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for example,
      /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can
      contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The comparison is
        case insensitive. The following wildcard characters are supported: * (matches 0 or more
        characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of each
        string is 128 characters. The comparison is case sensitive. The following wildcard
        characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
        character).

        If you specify multiple strings, the condition is satisfied if one of them matches the
        request URL. The path pattern is compared only to the path of the URL, not to its query
        string. To compare against the query string, use  QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header name is
        case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not
        supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum size of
        each string is 128 characters. The comparison strings are case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly
        1 character).

        If the same header appears multiple times in the request, we search them in order until a
        match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the value of the HTTP header. To require that all of the strings are a match, create one
        condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size of each
        string is 128 characters. The comparison is case insensitive. The following wildcard
        characters are supported: * (matches 0 or more characters) and ? (matches exactly 1
        character). To search for a literal '*' or '?' character in a query string, you must escape
        these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if one of
        them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed characters
        are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are
        not supported; therefore, the method name must be an exact match.

        If you specify multiple strings, the condition is satisfied if one of the strings matches
        the HTTP request method. We recommend that you route GET and HEAD requests in the same way,
        because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses.
        Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP address of
        the request matches one of the CIDR blocks. This condition is not satisfied by the
        addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For
        header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientModifyRuleResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientModifyRuleResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsForwardConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef(
    _ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientModifyRuleResponseRulesActionsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientModifyRuleResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientModifyRuleResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientModifyRuleResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientModifyRuleResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientModifyRuleResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesActionsTypeDef(
    _ClientModifyRuleResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRules` `Actions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is
    ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The
      comparison is case insensitive. The following wildcard characters are supported: *
      (matches 0 or more characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the host name.

      - *(string) --*
    """


_ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is
    ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header
      name is case insensitive. The allowed characters are specified by RFC 7230.
      Wildcards are not supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum
      size of each string is 128 characters. The comparison strings are case insensitive.
      The following wildcard characters are supported: * (matches 0 or more characters)
      and ? (matches exactly 1 character).

      If the same header appears multiple times in the request, we search them in order
      until a match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the value of the HTTP header. To require that all of the strings are a
      match, create one condition per string.

      - *(string) --*
    """


_ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed
      characters are A-Z, hyphen (-), and underscore (_). The comparison is case
      sensitive. Wildcards are not supported; therefore, the method name must be an exact
      match.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the HTTP request method. We recommend that you route GET and HEAD requests
      in the same way, because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is
    ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of
      each string is 128 characters. The comparison is case sensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of them matches
      the request URL. The path pattern is compared only to the path of the URL, not to
      its query string. To compare against the query string, use
      QueryStringConditionConfig .

      - *(string) --*
    """


_ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef",
    {
        "Values": List[
            ClientModifyRuleResponseRulesConditionsQueryStringConfigValuesTypeDef
        ]
    },
    total=False,
)


class ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is
    ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size
      of each string is 128 characters. The comparison is case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character). To search for a literal '*' or '?' character in a query
      string, you must escape these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if
      one of them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRulesConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
      addresses. Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP
      address of the request matches one of the CIDR blocks. This condition is not
      satisfied by the addresses in the X-Forwarded-For header. To search for addresses
      in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientModifyRuleResponseRulesConditionsTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientModifyRuleResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientModifyRuleResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientModifyRuleResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientModifyRuleResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientModifyRuleResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientModifyRuleResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientModifyRuleResponseRulesConditionsTypeDef(
    _ClientModifyRuleResponseRulesConditionsTypeDef
):
    """
    Type definition for `ClientModifyRuleResponseRules` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header``
      and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
      ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
      example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is
      ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The
        comparison is case insensitive. The following wildcard characters are supported: *
        (matches 0 or more characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is
      ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of
        each string is 128 characters. The comparison is case sensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of them matches
        the request URL. The path pattern is compared only to the path of the URL, not to
        its query string. To compare against the query string, use
        QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is
      ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header
        name is case insensitive. The allowed characters are specified by RFC 7230.
        Wildcards are not supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum
        size of each string is 128 characters. The comparison strings are case insensitive.
        The following wildcard characters are supported: * (matches 0 or more characters)
        and ? (matches exactly 1 character).

        If the same header appears multiple times in the request, we search them in order
        until a match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the value of the HTTP header. To require that all of the strings are a
        match, create one condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is
      ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size
        of each string is 128 characters. The comparison is case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character). To search for a literal '*' or '?' character in a query
        string, you must escape these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if
        one of them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed
        characters are A-Z, hyphen (-), and underscore (_). The comparison is case
        sensitive. Wildcards are not supported; therefore, the method name must be an exact
        match.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the HTTP request method. We recommend that you route GET and HEAD requests
        in the same way, because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
        addresses. Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP
        address of the request matches one of the CIDR blocks. This condition is not
        satisfied by the addresses in the X-Forwarded-For header. To search for addresses
        in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientModifyRuleResponseRulesTypeDef = TypedDict(
    "_ClientModifyRuleResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientModifyRuleResponseRulesConditionsTypeDef],
        "Actions": List[ClientModifyRuleResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientModifyRuleResponseRulesTypeDef(_ClientModifyRuleResponseRulesTypeDef):
    """
    Type definition for `ClientModifyRuleResponse` `Rules`

    Information about a rule.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(string) --*

      The priority.

    - **Conditions** *(list) --*

      The conditions. Each rule can include zero or one of the following conditions:
      ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
      zero or more of the following conditions: ``http-header`` and ``query-string`` .

      - *(dict) --*

        Information about a condition for a rule.

        - **Field** *(string) --*

          The field in the HTTP request. The following are the possible values:

          * ``http-header``

          * ``http-request-method``

          * ``host-header``

          * ``path-pattern``

          * ``query-string``

          * ``source-ip``

        - **Values** *(list) --*

          The condition value. You can use ``Values`` if the rule contains only ``host-header``
          and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
          ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

          If ``Field`` is ``host-header`` , you can specify a single host name (for example,
          my.example.com). A host name is case insensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * - .

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
          example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * _ - . $ / ~ " ' @ : +

          * & (using &amp;)

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          - *(string) --*

        - **HostHeaderConfig** *(dict) --*

          Information for a host header condition. Specify only when ``Field`` is
          ``host-header`` .

          - **Values** *(list) --*

            One or more host names. The maximum size of each name is 128 characters. The
            comparison is case insensitive. The following wildcard characters are supported: *
            (matches 0 or more characters) and ? (matches exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the host name.

            - *(string) --*

        - **PathPatternConfig** *(dict) --*

          Information for a path pattern condition. Specify only when ``Field`` is
          ``path-pattern`` .

          - **Values** *(list) --*

            One or more path patterns to compare against the request URL. The maximum size of
            each string is 128 characters. The comparison is case sensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of them matches
            the request URL. The path pattern is compared only to the path of the URL, not to
            its query string. To compare against the query string, use
            QueryStringConditionConfig .

            - *(string) --*

        - **HttpHeaderConfig** *(dict) --*

          Information for an HTTP header condition. Specify only when ``Field`` is
          ``http-header`` .

          - **HttpHeaderName** *(string) --*

            The name of the HTTP header field. The maximum size is 40 characters. The header
            name is case insensitive. The allowed characters are specified by RFC 7230.
            Wildcards are not supported.

            You can't use an HTTP header condition to specify the host header. Use
            HostHeaderConditionConfig to specify a host header condition.

          - **Values** *(list) --*

            One or more strings to compare against the value of the HTTP header. The maximum
            size of each string is 128 characters. The comparison strings are case insensitive.
            The following wildcard characters are supported: * (matches 0 or more characters)
            and ? (matches exactly 1 character).

            If the same header appears multiple times in the request, we search them in order
            until a match is found.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the value of the HTTP header. To require that all of the strings are a
            match, create one condition per string.

            - *(string) --*

        - **QueryStringConfig** *(dict) --*

          Information for a query string condition. Specify only when ``Field`` is
          ``query-string`` .

          - **Values** *(list) --*

            One or more key/value pairs or values to find in the query string. The maximum size
            of each string is 128 characters. The comparison is case insensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character). To search for a literal '*' or '?' character in a query
            string, you must escape these characters in ``Values`` using a '\\' character.

            If you specify multiple key/value pairs or values, the condition is satisfied if
            one of them is found in the query string.

            - *(dict) --*

              Information about a key/value pair.

              - **Key** *(string) --*

                The key. You can omit the key.

              - **Value** *(string) --*

                The value.

        - **HttpRequestMethodConfig** *(dict) --*

          Information for an HTTP method condition. Specify only when ``Field`` is
          ``http-request-method`` .

          - **Values** *(list) --*

            The name of the request method. The maximum size is 40 characters. The allowed
            characters are A-Z, hyphen (-), and underscore (_). The comparison is case
            sensitive. Wildcards are not supported; therefore, the method name must be an exact
            match.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the HTTP request method. We recommend that you route GET and HEAD requests
            in the same way, because the response to a HEAD request may be cached.

            - *(string) --*

        - **SourceIpConfig** *(dict) --*

          Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

          - **Values** *(list) --*

            One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
            addresses. Wildcards are not supported.

            If you specify multiple addresses, the condition is satisfied if the source IP
            address of the request matches one of the CIDR blocks. This condition is not
            satisfied by the addresses in the X-Forwarded-For header. To search for addresses
            in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

            - *(string) --*

    - **Actions** *(list) --*

      The actions. Each rule must include exactly one of the following types of actions:
      ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
      performed.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).

    - **IsDefault** *(boolean) --*

      Indicates whether this is the default rule.
    """


_ClientModifyRuleResponseTypeDef = TypedDict(
    "_ClientModifyRuleResponseTypeDef",
    {"Rules": List[ClientModifyRuleResponseRulesTypeDef]},
    total=False,
)


class ClientModifyRuleResponseTypeDef(_ClientModifyRuleResponseTypeDef):
    """
    Type definition for `ClientModifyRule` `Response`

    - **Rules** *(list) --*

      Information about the modified rule.

      - *(dict) --*

        Information about a rule.

        - **RuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **Priority** *(string) --*

          The priority.

        - **Conditions** *(list) --*

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
          zero or more of the following conditions: ``http-header`` and ``query-string`` .

          - *(dict) --*

            Information about a condition for a rule.

            - **Field** *(string) --*

              The field in the HTTP request. The following are the possible values:

              * ``http-header``

              * ``http-request-method``

              * ``host-header``

              * ``path-pattern``

              * ``query-string``

              * ``source-ip``

            - **Values** *(list) --*

              The condition value. You can use ``Values`` if the rule contains only ``host-header``
              and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
              ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

              If ``Field`` is ``host-header`` , you can specify a single host name (for example,
              my.example.com). A host name is case insensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * - .

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
              example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * _ - . $ / ~ " ' @ : +

              * & (using &amp;)

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              - *(string) --*

            - **HostHeaderConfig** *(dict) --*

              Information for a host header condition. Specify only when ``Field`` is
              ``host-header`` .

              - **Values** *(list) --*

                One or more host names. The maximum size of each name is 128 characters. The
                comparison is case insensitive. The following wildcard characters are supported: *
                (matches 0 or more characters) and ? (matches exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the host name.

                - *(string) --*

            - **PathPatternConfig** *(dict) --*

              Information for a path pattern condition. Specify only when ``Field`` is
              ``path-pattern`` .

              - **Values** *(list) --*

                One or more path patterns to compare against the request URL. The maximum size of
                each string is 128 characters. The comparison is case sensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of them matches
                the request URL. The path pattern is compared only to the path of the URL, not to
                its query string. To compare against the query string, use
                QueryStringConditionConfig .

                - *(string) --*

            - **HttpHeaderConfig** *(dict) --*

              Information for an HTTP header condition. Specify only when ``Field`` is
              ``http-header`` .

              - **HttpHeaderName** *(string) --*

                The name of the HTTP header field. The maximum size is 40 characters. The header
                name is case insensitive. The allowed characters are specified by RFC 7230.
                Wildcards are not supported.

                You can't use an HTTP header condition to specify the host header. Use
                HostHeaderConditionConfig to specify a host header condition.

              - **Values** *(list) --*

                One or more strings to compare against the value of the HTTP header. The maximum
                size of each string is 128 characters. The comparison strings are case insensitive.
                The following wildcard characters are supported: * (matches 0 or more characters)
                and ? (matches exactly 1 character).

                If the same header appears multiple times in the request, we search them in order
                until a match is found.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the value of the HTTP header. To require that all of the strings are a
                match, create one condition per string.

                - *(string) --*

            - **QueryStringConfig** *(dict) --*

              Information for a query string condition. Specify only when ``Field`` is
              ``query-string`` .

              - **Values** *(list) --*

                One or more key/value pairs or values to find in the query string. The maximum size
                of each string is 128 characters. The comparison is case insensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character). To search for a literal '*' or '?' character in a query
                string, you must escape these characters in ``Values`` using a '\\' character.

                If you specify multiple key/value pairs or values, the condition is satisfied if
                one of them is found in the query string.

                - *(dict) --*

                  Information about a key/value pair.

                  - **Key** *(string) --*

                    The key. You can omit the key.

                  - **Value** *(string) --*

                    The value.

            - **HttpRequestMethodConfig** *(dict) --*

              Information for an HTTP method condition. Specify only when ``Field`` is
              ``http-request-method`` .

              - **Values** *(list) --*

                The name of the request method. The maximum size is 40 characters. The allowed
                characters are A-Z, hyphen (-), and underscore (_). The comparison is case
                sensitive. Wildcards are not supported; therefore, the method name must be an exact
                match.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the HTTP request method. We recommend that you route GET and HEAD requests
                in the same way, because the response to a HEAD request may be cached.

                - *(string) --*

            - **SourceIpConfig** *(dict) --*

              Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

              - **Values** *(list) --*

                One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
                addresses. Wildcards are not supported.

                If you specify multiple addresses, the condition is satisfied if the source IP
                address of the request matches one of the CIDR blocks. This condition is not
                satisfied by the addresses in the X-Forwarded-For header. To search for addresses
                in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

                - *(string) --*

        - **Actions** *(list) --*

          The actions. Each rule must include exactly one of the following types of actions:
          ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
          performed.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

        - **IsDefault** *(boolean) --*

          Indicates whether this is the default rule.
    """


_ClientModifyTargetGroupAttributesAttributesTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyTargetGroupAttributesAttributesTypeDef(
    _ClientModifyTargetGroupAttributesAttributesTypeDef
):
    """
    Type definition for `ClientModifyTargetGroupAttributes` `Attributes`

    Information about a target group attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attribute is supported by both Application Load Balancers and Network Load
      Balancers:

      * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic Load
      Balancing to wait before changing the state of a deregistering target from ``draining`` to
      ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. If the target is
      a Lambda function, this attribute is not supported.

      The following attributes are supported by Application Load Balancers if the target is not a
      Lambda function:

      * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
      registered target receives a linearly increasing share of the traffic to the target group.
      After this time period ends, the target receives its full share of traffic. The range is
      30-900 seconds (15 minutes). Slow start mode is disabled by default.

      * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .

      * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
      requests from a client should be routed to the same target. After this time period expires,
      the load balancer-generated cookie is considered stale. The range is 1 second to 1 week
      (604800 seconds). The default value is 1 day (86400 seconds).

      The following attribute is supported only if the target is a Lambda function.

      * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response headers
      exchanged between the load balancer and the Lambda function include arrays of values or
      strings. The value is ``true`` or ``false`` . The default is ``false`` . If the value is
      ``false`` and the request contains a duplicate header field name or query parameter key, the
      load balancer uses the last value sent by the client.

      The following attribute is supported only by Network Load Balancers:

      * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The
      value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientModifyTargetGroupAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesResponseAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyTargetGroupAttributesResponseAttributesTypeDef(
    _ClientModifyTargetGroupAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientModifyTargetGroupAttributesResponse` `Attributes`

    Information about a target group attribute.

    - **Key** *(string) --*

      The name of the attribute.

      The following attribute is supported by both Application Load Balancers and Network Load
      Balancers:

      * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
      Load Balancing to wait before changing the state of a deregistering target from
      ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
      seconds. If the target is a Lambda function, this attribute is not supported.

      The following attributes are supported by Application Load Balancers if the target is not
      a Lambda function:

      * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
      registered target receives a linearly increasing share of the traffic to the target
      group. After this time period ends, the target receives its full share of traffic. The
      range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.

      * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
      ``true`` or ``false`` . The default is ``false`` .

      * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .

      * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
      requests from a client should be routed to the same target. After this time period
      expires, the load balancer-generated cookie is considered stale. The range is 1 second to
      1 week (604800 seconds). The default value is 1 day (86400 seconds).

      The following attribute is supported only if the target is a Lambda function.

      * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
      headers exchanged between the load balancer and the Lambda function include arrays of
      values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the
      value is ``false`` and the request contains a duplicate header field name or query
      parameter key, the load balancer uses the last value sent by the client.

      The following attribute is supported only by Network Load Balancers:

      * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
      The value is ``true`` or ``false`` . The default is ``false`` .

    - **Value** *(string) --*

      The value of the attribute.
    """


_ClientModifyTargetGroupAttributesResponseTypeDef = TypedDict(
    "_ClientModifyTargetGroupAttributesResponseTypeDef",
    {"Attributes": List[ClientModifyTargetGroupAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientModifyTargetGroupAttributesResponseTypeDef(
    _ClientModifyTargetGroupAttributesResponseTypeDef
):
    """
    Type definition for `ClientModifyTargetGroupAttributes` `Response`

    - **Attributes** *(list) --*

      Information about the attributes.

      - *(dict) --*

        Information about a target group attribute.

        - **Key** *(string) --*

          The name of the attribute.

          The following attribute is supported by both Application Load Balancers and Network Load
          Balancers:

          * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic
          Load Balancing to wait before changing the state of a deregistering target from
          ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300
          seconds. If the target is a Lambda function, this attribute is not supported.

          The following attributes are supported by Application Load Balancers if the target is not
          a Lambda function:

          * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly
          registered target receives a linearly increasing share of the traffic to the target
          group. After this time period ends, the target receives its full share of traffic. The
          range is 30-900 seconds (15 minutes). Slow start mode is disabled by default.

          * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is
          ``true`` or ``false`` . The default is ``false`` .

          * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` .

          * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which
          requests from a client should be routed to the same target. After this time period
          expires, the load balancer-generated cookie is considered stale. The range is 1 second to
          1 week (604800 seconds). The default value is 1 day (86400 seconds).

          The following attribute is supported only if the target is a Lambda function.

          * ``lambda.multi_value_headers.enabled`` - Indicates whether the request and response
          headers exchanged between the load balancer and the Lambda function include arrays of
          values or strings. The value is ``true`` or ``false`` . The default is ``false`` . If the
          value is ``false`` and the request contains a duplicate header field name or query
          parameter key, the load balancer uses the last value sent by the client.

          The following attribute is supported only by Network Load Balancers:

          * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled.
          The value is ``true`` or ``false`` . The default is ``false`` .

        - **Value** *(string) --*

          The value of the attribute.
    """


_ClientModifyTargetGroupMatcherTypeDef = TypedDict(
    "_ClientModifyTargetGroupMatcherTypeDef", {"HttpCode": str}
)


class ClientModifyTargetGroupMatcherTypeDef(_ClientModifyTargetGroupMatcherTypeDef):
    """
    Type definition for `ClientModifyTargetGroup` `Matcher`

    [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
    target.

    With Network Load Balancers, you can't modify this setting.

    - **HttpCode** *(string) --* **[REQUIRED]**

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the default
      value is 200. You can specify multiple values (for example, "200,202") or a range of values
      (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef",
    {"HttpCode": str},
    total=False,
)


class ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef(
    _ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef
):
    """
    Type definition for `ClientModifyTargetGroupResponseTargetGroups` `Matcher`

    The HTTP codes to use when checking for a successful response from a target.

    - **HttpCode** *(string) --*

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the
      default value is 200. You can specify multiple values (for example, "200,202") or a
      range of values (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_ClientModifyTargetGroupResponseTargetGroupsTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": str,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": ClientModifyTargetGroupResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": str,
    },
    total=False,
)


class ClientModifyTargetGroupResponseTargetGroupsTypeDef(
    _ClientModifyTargetGroupResponseTargetGroupsTypeDef
):
    """
    Type definition for `ClientModifyTargetGroupResponse` `TargetGroups`

    Information about a target group.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **TargetGroupName** *(string) --*

      The name of the target group.

    - **Protocol** *(string) --*

      The protocol to use for routing traffic to the targets.

    - **Port** *(integer) --*

      The port on which the targets are listening. Not used if the target is a Lambda function.

    - **VpcId** *(string) --*

      The ID of the VPC for the targets.

    - **HealthCheckProtocol** *(string) --*

      The protocol to use to connect with the target.

    - **HealthCheckPort** *(string) --*

      The port to use to connect with the target.

    - **HealthCheckEnabled** *(boolean) --*

      Indicates whether health checks are enabled.

    - **HealthCheckIntervalSeconds** *(integer) --*

      The approximate amount of time, in seconds, between health checks of an individual target.

    - **HealthCheckTimeoutSeconds** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

    - **HealthyThresholdCount** *(integer) --*

      The number of consecutive health checks successes required before considering an
      unhealthy target healthy.

    - **UnhealthyThresholdCount** *(integer) --*

      The number of consecutive health check failures required before considering the target
      unhealthy.

    - **HealthCheckPath** *(string) --*

      The destination for the health check request.

    - **Matcher** *(dict) --*

      The HTTP codes to use when checking for a successful response from a target.

      - **HttpCode** *(string) --*

        The HTTP codes.

        For Application Load Balancers, you can specify values between 200 and 499, and the
        default value is 200. You can specify multiple values (for example, "200,202") or a
        range of values (for example, "200-299").

        For Network Load Balancers, this is 200–399.

    - **LoadBalancerArns** *(list) --*

      The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
      group.

      - *(string) --*

    - **TargetType** *(string) --*

      The type of target that you must specify when registering targets with this target group.
      The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
      (targets are specified by IP address).
    """


_ClientModifyTargetGroupResponseTypeDef = TypedDict(
    "_ClientModifyTargetGroupResponseTypeDef",
    {"TargetGroups": List[ClientModifyTargetGroupResponseTargetGroupsTypeDef]},
    total=False,
)


class ClientModifyTargetGroupResponseTypeDef(_ClientModifyTargetGroupResponseTypeDef):
    """
    Type definition for `ClientModifyTargetGroup` `Response`

    - **TargetGroups** *(list) --*

      Information about the modified target group.

      - *(dict) --*

        Information about a target group.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **TargetGroupName** *(string) --*

          The name of the target group.

        - **Protocol** *(string) --*

          The protocol to use for routing traffic to the targets.

        - **Port** *(integer) --*

          The port on which the targets are listening. Not used if the target is a Lambda function.

        - **VpcId** *(string) --*

          The ID of the VPC for the targets.

        - **HealthCheckProtocol** *(string) --*

          The protocol to use to connect with the target.

        - **HealthCheckPort** *(string) --*

          The port to use to connect with the target.

        - **HealthCheckEnabled** *(boolean) --*

          Indicates whether health checks are enabled.

        - **HealthCheckIntervalSeconds** *(integer) --*

          The approximate amount of time, in seconds, between health checks of an individual target.

        - **HealthCheckTimeoutSeconds** *(integer) --*

          The amount of time, in seconds, during which no response means a failed health check.

        - **HealthyThresholdCount** *(integer) --*

          The number of consecutive health checks successes required before considering an
          unhealthy target healthy.

        - **UnhealthyThresholdCount** *(integer) --*

          The number of consecutive health check failures required before considering the target
          unhealthy.

        - **HealthCheckPath** *(string) --*

          The destination for the health check request.

        - **Matcher** *(dict) --*

          The HTTP codes to use when checking for a successful response from a target.

          - **HttpCode** *(string) --*

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the
            default value is 200. You can specify multiple values (for example, "200,202") or a
            range of values (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        - **LoadBalancerArns** *(list) --*

          The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
          group.

          - *(string) --*

        - **TargetType** *(string) --*

          The type of target that you must specify when registering targets with this target group.
          The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
          (targets are specified by IP address).
    """


_RequiredClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_RequiredClientRegisterTargetsTargetsTypeDef", {"Id": str}
)
_OptionalClientRegisterTargetsTargetsTypeDef = TypedDict(
    "_OptionalClientRegisterTargetsTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class ClientRegisterTargetsTargetsTypeDef(
    _RequiredClientRegisterTargetsTargetsTypeDef,
    _OptionalClientRegisterTargetsTargetsTypeDef,
):
    """
    Type definition for `ClientRegisterTargets` `Targets`

    Information about a target.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the target. If the target type of the target group is ``instance`` , specify an
      instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
      ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic from
      the load balancer nodes in the specified Availability Zone or from all enabled Availability
      Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the target
      group, the Availability Zone is automatically detected and this parameter is optional. If the
      IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is outside
      the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported value is
      ``all`` .
    """


_ClientRemoveListenerCertificatesCertificatesTypeDef = TypedDict(
    "_ClientRemoveListenerCertificatesCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class ClientRemoveListenerCertificatesCertificatesTypeDef(
    _ClientRemoveListenerCertificatesCertificatesTypeDef
):
    """
    Type definition for `ClientRemoveListenerCertificates` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_ClientSetIpAddressTypeResponseTypeDef = TypedDict(
    "_ClientSetIpAddressTypeResponseTypeDef", {"IpAddressType": str}, total=False
)


class ClientSetIpAddressTypeResponseTypeDef(_ClientSetIpAddressTypeResponseTypeDef):
    """
    Type definition for `ClientSetIpAddressType` `Response`

    - **IpAddressType** *(string) --*

      The IP address type.
    """


_ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_ClientSetRulePrioritiesResponseRulesActionsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": ClientSetRulePrioritiesResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": ClientSetRulePrioritiesResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": ClientSetRulePrioritiesResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": ClientSetRulePrioritiesResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesActionsTypeDef(
    _ClientSetRulePrioritiesResponseRulesActionsTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRules` `Actions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is
    ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The
      comparison is case insensitive. The following wildcard characters are supported: *
      (matches 0 or more characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the host name.

      - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is
    ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header
      name is case insensitive. The allowed characters are specified by RFC 7230.
      Wildcards are not supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum
      size of each string is 128 characters. The comparison strings are case insensitive.
      The following wildcard characters are supported: * (matches 0 or more characters)
      and ? (matches exactly 1 character).

      If the same header appears multiple times in the request, we search them in order
      until a match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the value of the HTTP header. To require that all of the strings are a
      match, create one condition per string.

      - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed
      characters are A-Z, hyphen (-), and underscore (_). The comparison is case
      sensitive. Wildcards are not supported; therefore, the method name must be an exact
      match.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the HTTP request method. We recommend that you route GET and HEAD requests
      in the same way, because the response to a HEAD request may be cached.

      - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is
    ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of
      each string is 128 characters. The comparison is case sensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of them matches
      the request URL. The path pattern is compared only to the path of the URL, not to
      its query string. To compare against the query string, use
      QueryStringConditionConfig .

      - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef",
    {
        "Values": List[
            ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigValuesTypeDef
        ]
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is
    ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size
      of each string is 128 characters. The comparison is case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character). To search for a literal '*' or '?' character in a query
      string, you must escape these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if
      one of them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRulesConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
      addresses. Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP
      address of the request matches one of the CIDR blocks. This condition is not
      satisfied by the addresses in the X-Forwarded-For header. To search for addresses
      in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesConditionsTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": ClientSetRulePrioritiesResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": ClientSetRulePrioritiesResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": ClientSetRulePrioritiesResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": ClientSetRulePrioritiesResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesConditionsTypeDef(
    _ClientSetRulePrioritiesResponseRulesConditionsTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponseRules` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header``
      and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
      ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
      example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is
      ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The
        comparison is case insensitive. The following wildcard characters are supported: *
        (matches 0 or more characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is
      ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of
        each string is 128 characters. The comparison is case sensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of them matches
        the request URL. The path pattern is compared only to the path of the URL, not to
        its query string. To compare against the query string, use
        QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is
      ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header
        name is case insensitive. The allowed characters are specified by RFC 7230.
        Wildcards are not supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum
        size of each string is 128 characters. The comparison strings are case insensitive.
        The following wildcard characters are supported: * (matches 0 or more characters)
        and ? (matches exactly 1 character).

        If the same header appears multiple times in the request, we search them in order
        until a match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the value of the HTTP header. To require that all of the strings are a
        match, create one condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is
      ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size
        of each string is 128 characters. The comparison is case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character). To search for a literal '*' or '?' character in a query
        string, you must escape these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if
        one of them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed
        characters are A-Z, hyphen (-), and underscore (_). The comparison is case
        sensitive. Wildcards are not supported; therefore, the method name must be an exact
        match.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the HTTP request method. We recommend that you route GET and HEAD requests
        in the same way, because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
        addresses. Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP
        address of the request matches one of the CIDR blocks. This condition is not
        satisfied by the addresses in the X-Forwarded-For header. To search for addresses
        in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_ClientSetRulePrioritiesResponseRulesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[ClientSetRulePrioritiesResponseRulesConditionsTypeDef],
        "Actions": List[ClientSetRulePrioritiesResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class ClientSetRulePrioritiesResponseRulesTypeDef(
    _ClientSetRulePrioritiesResponseRulesTypeDef
):
    """
    Type definition for `ClientSetRulePrioritiesResponse` `Rules`

    Information about a rule.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(string) --*

      The priority.

    - **Conditions** *(list) --*

      The conditions. Each rule can include zero or one of the following conditions:
      ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
      zero or more of the following conditions: ``http-header`` and ``query-string`` .

      - *(dict) --*

        Information about a condition for a rule.

        - **Field** *(string) --*

          The field in the HTTP request. The following are the possible values:

          * ``http-header``

          * ``http-request-method``

          * ``host-header``

          * ``path-pattern``

          * ``query-string``

          * ``source-ip``

        - **Values** *(list) --*

          The condition value. You can use ``Values`` if the rule contains only ``host-header``
          and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
          ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

          If ``Field`` is ``host-header`` , you can specify a single host name (for example,
          my.example.com). A host name is case insensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * - .

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
          example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * _ - . $ / ~ " ' @ : +

          * & (using &amp;)

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          - *(string) --*

        - **HostHeaderConfig** *(dict) --*

          Information for a host header condition. Specify only when ``Field`` is
          ``host-header`` .

          - **Values** *(list) --*

            One or more host names. The maximum size of each name is 128 characters. The
            comparison is case insensitive. The following wildcard characters are supported: *
            (matches 0 or more characters) and ? (matches exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the host name.

            - *(string) --*

        - **PathPatternConfig** *(dict) --*

          Information for a path pattern condition. Specify only when ``Field`` is
          ``path-pattern`` .

          - **Values** *(list) --*

            One or more path patterns to compare against the request URL. The maximum size of
            each string is 128 characters. The comparison is case sensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of them matches
            the request URL. The path pattern is compared only to the path of the URL, not to
            its query string. To compare against the query string, use
            QueryStringConditionConfig .

            - *(string) --*

        - **HttpHeaderConfig** *(dict) --*

          Information for an HTTP header condition. Specify only when ``Field`` is
          ``http-header`` .

          - **HttpHeaderName** *(string) --*

            The name of the HTTP header field. The maximum size is 40 characters. The header
            name is case insensitive. The allowed characters are specified by RFC 7230.
            Wildcards are not supported.

            You can't use an HTTP header condition to specify the host header. Use
            HostHeaderConditionConfig to specify a host header condition.

          - **Values** *(list) --*

            One or more strings to compare against the value of the HTTP header. The maximum
            size of each string is 128 characters. The comparison strings are case insensitive.
            The following wildcard characters are supported: * (matches 0 or more characters)
            and ? (matches exactly 1 character).

            If the same header appears multiple times in the request, we search them in order
            until a match is found.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the value of the HTTP header. To require that all of the strings are a
            match, create one condition per string.

            - *(string) --*

        - **QueryStringConfig** *(dict) --*

          Information for a query string condition. Specify only when ``Field`` is
          ``query-string`` .

          - **Values** *(list) --*

            One or more key/value pairs or values to find in the query string. The maximum size
            of each string is 128 characters. The comparison is case insensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character). To search for a literal '*' or '?' character in a query
            string, you must escape these characters in ``Values`` using a '\\' character.

            If you specify multiple key/value pairs or values, the condition is satisfied if
            one of them is found in the query string.

            - *(dict) --*

              Information about a key/value pair.

              - **Key** *(string) --*

                The key. You can omit the key.

              - **Value** *(string) --*

                The value.

        - **HttpRequestMethodConfig** *(dict) --*

          Information for an HTTP method condition. Specify only when ``Field`` is
          ``http-request-method`` .

          - **Values** *(list) --*

            The name of the request method. The maximum size is 40 characters. The allowed
            characters are A-Z, hyphen (-), and underscore (_). The comparison is case
            sensitive. Wildcards are not supported; therefore, the method name must be an exact
            match.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the HTTP request method. We recommend that you route GET and HEAD requests
            in the same way, because the response to a HEAD request may be cached.

            - *(string) --*

        - **SourceIpConfig** *(dict) --*

          Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

          - **Values** *(list) --*

            One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
            addresses. Wildcards are not supported.

            If you specify multiple addresses, the condition is satisfied if the source IP
            address of the request matches one of the CIDR blocks. This condition is not
            satisfied by the addresses in the X-Forwarded-For header. To search for addresses
            in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

            - *(string) --*

    - **Actions** *(list) --*

      The actions. Each rule must include exactly one of the following types of actions:
      ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
      performed.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).

    - **IsDefault** *(boolean) --*

      Indicates whether this is the default rule.
    """


_ClientSetRulePrioritiesResponseTypeDef = TypedDict(
    "_ClientSetRulePrioritiesResponseTypeDef",
    {"Rules": List[ClientSetRulePrioritiesResponseRulesTypeDef]},
    total=False,
)


class ClientSetRulePrioritiesResponseTypeDef(_ClientSetRulePrioritiesResponseTypeDef):
    """
    Type definition for `ClientSetRulePriorities` `Response`

    - **Rules** *(list) --*

      Information about the rules.

      - *(dict) --*

        Information about a rule.

        - **RuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **Priority** *(string) --*

          The priority.

        - **Conditions** *(list) --*

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
          zero or more of the following conditions: ``http-header`` and ``query-string`` .

          - *(dict) --*

            Information about a condition for a rule.

            - **Field** *(string) --*

              The field in the HTTP request. The following are the possible values:

              * ``http-header``

              * ``http-request-method``

              * ``host-header``

              * ``path-pattern``

              * ``query-string``

              * ``source-ip``

            - **Values** *(list) --*

              The condition value. You can use ``Values`` if the rule contains only ``host-header``
              and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
              ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

              If ``Field`` is ``host-header`` , you can specify a single host name (for example,
              my.example.com). A host name is case insensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * - .

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
              example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * _ - . $ / ~ " ' @ : +

              * & (using &amp;)

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              - *(string) --*

            - **HostHeaderConfig** *(dict) --*

              Information for a host header condition. Specify only when ``Field`` is
              ``host-header`` .

              - **Values** *(list) --*

                One or more host names. The maximum size of each name is 128 characters. The
                comparison is case insensitive. The following wildcard characters are supported: *
                (matches 0 or more characters) and ? (matches exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the host name.

                - *(string) --*

            - **PathPatternConfig** *(dict) --*

              Information for a path pattern condition. Specify only when ``Field`` is
              ``path-pattern`` .

              - **Values** *(list) --*

                One or more path patterns to compare against the request URL. The maximum size of
                each string is 128 characters. The comparison is case sensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of them matches
                the request URL. The path pattern is compared only to the path of the URL, not to
                its query string. To compare against the query string, use
                QueryStringConditionConfig .

                - *(string) --*

            - **HttpHeaderConfig** *(dict) --*

              Information for an HTTP header condition. Specify only when ``Field`` is
              ``http-header`` .

              - **HttpHeaderName** *(string) --*

                The name of the HTTP header field. The maximum size is 40 characters. The header
                name is case insensitive. The allowed characters are specified by RFC 7230.
                Wildcards are not supported.

                You can't use an HTTP header condition to specify the host header. Use
                HostHeaderConditionConfig to specify a host header condition.

              - **Values** *(list) --*

                One or more strings to compare against the value of the HTTP header. The maximum
                size of each string is 128 characters. The comparison strings are case insensitive.
                The following wildcard characters are supported: * (matches 0 or more characters)
                and ? (matches exactly 1 character).

                If the same header appears multiple times in the request, we search them in order
                until a match is found.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the value of the HTTP header. To require that all of the strings are a
                match, create one condition per string.

                - *(string) --*

            - **QueryStringConfig** *(dict) --*

              Information for a query string condition. Specify only when ``Field`` is
              ``query-string`` .

              - **Values** *(list) --*

                One or more key/value pairs or values to find in the query string. The maximum size
                of each string is 128 characters. The comparison is case insensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character). To search for a literal '*' or '?' character in a query
                string, you must escape these characters in ``Values`` using a '\\' character.

                If you specify multiple key/value pairs or values, the condition is satisfied if
                one of them is found in the query string.

                - *(dict) --*

                  Information about a key/value pair.

                  - **Key** *(string) --*

                    The key. You can omit the key.

                  - **Value** *(string) --*

                    The value.

            - **HttpRequestMethodConfig** *(dict) --*

              Information for an HTTP method condition. Specify only when ``Field`` is
              ``http-request-method`` .

              - **Values** *(list) --*

                The name of the request method. The maximum size is 40 characters. The allowed
                characters are A-Z, hyphen (-), and underscore (_). The comparison is case
                sensitive. Wildcards are not supported; therefore, the method name must be an exact
                match.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the HTTP request method. We recommend that you route GET and HEAD requests
                in the same way, because the response to a HEAD request may be cached.

                - *(string) --*

            - **SourceIpConfig** *(dict) --*

              Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

              - **Values** *(list) --*

                One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
                addresses. Wildcards are not supported.

                If you specify multiple addresses, the condition is satisfied if the source IP
                address of the request matches one of the CIDR blocks. This condition is not
                satisfied by the addresses in the X-Forwarded-For header. To search for addresses
                in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

                - *(string) --*

        - **Actions** *(list) --*

          The actions. Each rule must include exactly one of the following types of actions:
          ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
          performed.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

        - **IsDefault** *(boolean) --*

          Indicates whether this is the default rule.
    """


_ClientSetRulePrioritiesRulePrioritiesTypeDef = TypedDict(
    "_ClientSetRulePrioritiesRulePrioritiesTypeDef",
    {"RuleArn": str, "Priority": int},
    total=False,
)


class ClientSetRulePrioritiesRulePrioritiesTypeDef(
    _ClientSetRulePrioritiesRulePrioritiesTypeDef
):
    """
    Type definition for `ClientSetRulePriorities` `RulePriorities`

    Information about the priorities for the rules for a listener.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(integer) --*

      The rule priority.
    """


_ClientSetSecurityGroupsResponseTypeDef = TypedDict(
    "_ClientSetSecurityGroupsResponseTypeDef",
    {"SecurityGroupIds": List[str]},
    total=False,
)


class ClientSetSecurityGroupsResponseTypeDef(_ClientSetSecurityGroupsResponseTypeDef):
    """
    Type definition for `ClientSetSecurityGroups` `Response`

    - **SecurityGroupIds** *(list) --*

      The IDs of the security groups associated with the load balancer.

      - *(string) --*
    """


_ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str},
    total=False,
)


class ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef(
    _ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef
):
    """
    Type definition for `ClientSetSubnetsResponseAvailabilityZones` `LoadBalancerAddresses`

    Information about a static IP address for a load balancer.

    - **IpAddress** *(string) --*

      The static IP address.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientSetSubnetsResponseAvailabilityZonesTypeDef = TypedDict(
    "_ClientSetSubnetsResponseAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            ClientSetSubnetsResponseAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class ClientSetSubnetsResponseAvailabilityZonesTypeDef(
    _ClientSetSubnetsResponseAvailabilityZonesTypeDef
):
    """
    Type definition for `ClientSetSubnetsResponse` `AvailabilityZones`

    Information about an Availability Zone.

    - **ZoneName** *(string) --*

      The name of the Availability Zone.

    - **SubnetId** *(string) --*

      The ID of the subnet. You can specify one subnet per Availability Zone.

    - **LoadBalancerAddresses** *(list) --*

      [Network Load Balancers] If you need static IP addresses for your load balancer, you can
      specify one Elastic IP address per Availability Zone when you create the load balancer.

      - *(dict) --*

        Information about a static IP address for a load balancer.

        - **IpAddress** *(string) --*

          The static IP address.

        - **AllocationId** *(string) --*

          [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientSetSubnetsResponseTypeDef = TypedDict(
    "_ClientSetSubnetsResponseTypeDef",
    {"AvailabilityZones": List[ClientSetSubnetsResponseAvailabilityZonesTypeDef]},
    total=False,
)


class ClientSetSubnetsResponseTypeDef(_ClientSetSubnetsResponseTypeDef):
    """
    Type definition for `ClientSetSubnets` `Response`

    - **AvailabilityZones** *(list) --*

      Information about the subnet and Availability Zone.

      - *(dict) --*

        Information about an Availability Zone.

        - **ZoneName** *(string) --*

          The name of the Availability Zone.

        - **SubnetId** *(string) --*

          The ID of the subnet. You can specify one subnet per Availability Zone.

        - **LoadBalancerAddresses** *(list) --*

          [Network Load Balancers] If you need static IP addresses for your load balancer, you can
          specify one Elastic IP address per Availability Zone when you create the load balancer.

          - *(dict) --*

            Information about a static IP address for a load balancer.

            - **IpAddress** *(string) --*

              The static IP address.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_ClientSetSubnetsSubnetMappingsTypeDef = TypedDict(
    "_ClientSetSubnetsSubnetMappingsTypeDef",
    {"SubnetId": str, "AllocationId": str},
    total=False,
)


class ClientSetSubnetsSubnetMappingsTypeDef(_ClientSetSubnetsSubnetMappingsTypeDef):
    """
    Type definition for `ClientSetSubnets` `SubnetMappings`

    Information about a subnet mapping.

    - **SubnetId** *(string) --*

      The ID of the subnet.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAccountLimitsPaginatePaginationConfigTypeDef(
    _DescribeAccountLimitsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginate` `PaginationConfig`

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


_DescribeAccountLimitsPaginateResponseLimitsTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseLimitsTypeDef",
    {"Name": str, "Max": str},
    total=False,
)


class DescribeAccountLimitsPaginateResponseLimitsTypeDef(
    _DescribeAccountLimitsPaginateResponseLimitsTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginateResponse` `Limits`

    Information about an Elastic Load Balancing resource limit for your AWS account.

    - **Name** *(string) --*

      The name of the limit. The possible values are:

      * application-load-balancers

      * listeners-per-application-load-balancer

      * listeners-per-network-load-balancer

      * network-load-balancers

      * rules-per-application-load-balancer

      * target-groups

      * target-groups-per-action-on-application-load-balancer

      * target-groups-per-action-on-network-load-balancer

      * target-groups-per-application-load-balancer

      * targets-per-application-load-balancer

      * targets-per-availability-zone-per-network-load-balancer

      * targets-per-network-load-balancer

    - **Max** *(string) --*

      The maximum value of the limit.
    """


_DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseTypeDef",
    {
        "Limits": List[DescribeAccountLimitsPaginateResponseLimitsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeAccountLimitsPaginateResponseTypeDef(
    _DescribeAccountLimitsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeAccountLimitsPaginate` `Response`

    - **Limits** *(list) --*

      Information about the limits.

      - *(dict) --*

        Information about an Elastic Load Balancing resource limit for your AWS account.

        - **Name** *(string) --*

          The name of the limit. The possible values are:

          * application-load-balancers

          * listeners-per-application-load-balancer

          * listeners-per-network-load-balancer

          * network-load-balancers

          * rules-per-application-load-balancer

          * target-groups

          * target-groups-per-action-on-application-load-balancer

          * target-groups-per-action-on-network-load-balancer

          * target-groups-per-application-load-balancer

          * targets-per-application-load-balancer

          * targets-per-availability-zone-per-network-load-balancer

          * targets-per-network-load-balancer

        - **Max** *(string) --*

          The maximum value of the limit.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeListenerCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeListenerCertificatesPaginatePaginationConfigTypeDef(
    _DescribeListenerCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeListenerCertificatesPaginate` `PaginationConfig`

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


_DescribeListenerCertificatesPaginateResponseCertificatesTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginateResponseCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class DescribeListenerCertificatesPaginateResponseCertificatesTypeDef(
    _DescribeListenerCertificatesPaginateResponseCertificatesTypeDef
):
    """
    Type definition for `DescribeListenerCertificatesPaginateResponse` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value when
      specifying a certificate as an input. This value is not included in the output when
      describing a listener, but is included when describing listener certificates.
    """


_DescribeListenerCertificatesPaginateResponseTypeDef = TypedDict(
    "_DescribeListenerCertificatesPaginateResponseTypeDef",
    {
        "Certificates": List[
            DescribeListenerCertificatesPaginateResponseCertificatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeListenerCertificatesPaginateResponseTypeDef(
    _DescribeListenerCertificatesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeListenerCertificatesPaginate` `Response`

    - **Certificates** *(list) --*

      Information about the certificates.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value when
          specifying a certificate as an input. This value is not included in the output when
          describing a listener, but is included when describing listener certificates.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeListenersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeListenersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeListenersPaginatePaginationConfigTypeDef(
    _DescribeListenersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginate` `PaginationConfig`

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


_DescribeListenersPaginateResponseListenersCertificatesTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersCertificatesTypeDef",
    {"CertificateArn": str, "IsDefault": bool},
    total=False,
)


class DescribeListenersPaginateResponseListenersCertificatesTypeDef(
    _DescribeListenersPaginateResponseListenersCertificatesTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListeners` `Certificates`

    Information about an SSL server certificate.

    - **CertificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate.

    - **IsDefault** *(boolean) --*

      Indicates whether the certificate is the default certificate. Do not set this value
      when specifying a certificate as an input. This value is not included in the output
      when describing a listener, but is included when describing listener certificates.
    """


_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListenersDefaultActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_DescribeListenersPaginateResponseListenersDefaultActionsTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersDefaultActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": DescribeListenersPaginateResponseListenersDefaultActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": DescribeListenersPaginateResponseListenersDefaultActionsRedirectConfigTypeDef,
        "FixedResponseConfig": DescribeListenersPaginateResponseListenersDefaultActionsFixedResponseConfigTypeDef,
        "ForwardConfig": DescribeListenersPaginateResponseListenersDefaultActionsForwardConfigTypeDef,
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersDefaultActionsTypeDef(
    _DescribeListenersPaginateResponseListenersDefaultActionsTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponseListeners` `DefaultActions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeListenersPaginateResponseListenersTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": str,
        "Certificates": List[
            DescribeListenersPaginateResponseListenersCertificatesTypeDef
        ],
        "SslPolicy": str,
        "DefaultActions": List[
            DescribeListenersPaginateResponseListenersDefaultActionsTypeDef
        ],
    },
    total=False,
)


class DescribeListenersPaginateResponseListenersTypeDef(
    _DescribeListenersPaginateResponseListenersTypeDef
):
    """
    Type definition for `DescribeListenersPaginateResponse` `Listeners`

    Information about a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **Port** *(integer) --*

      The port on which the load balancer is listening.

    - **Protocol** *(string) --*

      The protocol for connections from clients to the load balancer.

    - **Certificates** *(list) --*

      [HTTPS or TLS listener] The default certificate for the listener.

      - *(dict) --*

        Information about an SSL server certificate.

        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate.

        - **IsDefault** *(boolean) --*

          Indicates whether the certificate is the default certificate. Do not set this value
          when specifying a certificate as an input. This value is not included in the output
          when describing a listener, but is included when describing listener certificates.

    - **SslPolicy** *(string) --*

      [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
      supported. The default is the current predefined security policy.

    - **DefaultActions** *(list) --*

      The default actions for the listener.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeListenersPaginateResponseTypeDef = TypedDict(
    "_DescribeListenersPaginateResponseTypeDef",
    {
        "Listeners": List[DescribeListenersPaginateResponseListenersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeListenersPaginateResponseTypeDef(
    _DescribeListenersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeListenersPaginate` `Response`

    - **Listeners** *(list) --*

      Information about the listeners.

      - *(dict) --*

        Information about a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **Port** *(integer) --*

          The port on which the load balancer is listening.

        - **Protocol** *(string) --*

          The protocol for connections from clients to the load balancer.

        - **Certificates** *(list) --*

          [HTTPS or TLS listener] The default certificate for the listener.

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value
              when specifying a certificate as an input. This value is not included in the output
              when describing a listener, but is included when describing listener certificates.

        - **SslPolicy** *(string) --*

          [HTTPS or TLS listener] The security policy that defines which ciphers and protocols are
          supported. The default is the current predefined security policy.

        - **DefaultActions** *(list) --*

          The default actions for the listener.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeLoadBalancersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeLoadBalancersPaginatePaginationConfigTypeDef(
    _DescribeLoadBalancersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginate` `PaginationConfig`

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


_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef",
    {"IpAddress": str, "AllocationId": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZones` `LoadBalancerAddresses`

    Information about a static IP address for a load balancer.

    - **IpAddress** *(string) --*

      The static IP address.

    - **AllocationId** *(string) --*

      [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "LoadBalancerAddresses": List[
            DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesLoadBalancerAddressesTypeDef
        ],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancers` `AvailabilityZones`

    Information about an Availability Zone.

    - **ZoneName** *(string) --*

      The name of the Availability Zone.

    - **SubnetId** *(string) --*

      The ID of the subnet. You can specify one subnet per Availability Zone.

    - **LoadBalancerAddresses** *(list) --*

      [Network Load Balancers] If you need static IP addresses for your load balancer, you
      can specify one Elastic IP address per Availability Zone when you create the load
      balancer.

      - *(dict) --*

        Information about a static IP address for a load balancer.

        - **IpAddress** *(string) --*

          The static IP address.

        - **AllocationId** *(string) --*

          [Network Load Balancers] The allocation ID of the Elastic IP address.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef",
    {"Code": str, "Reason": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancers` `State`

    The state of the load balancer.

    - **Code** *(string) --*

      The state code. The initial state of the load balancer is ``provisioning`` . After the
      load balancer is fully set up and ready to route traffic, its state is ``active`` . If
      the load balancer could not be set up, its state is ``failed`` .

    - **Reason** *(string) --*

      A description of the state.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": str,
        "VpcId": str,
        "State": DescribeLoadBalancersPaginateResponseLoadBalancersStateTypeDef,
        "Type": str,
        "AvailabilityZones": List[
            DescribeLoadBalancersPaginateResponseLoadBalancersAvailabilityZonesTypeDef
        ],
        "SecurityGroups": List[str],
        "IpAddressType": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponse` `LoadBalancers`

    Information about a load balancer.

    - **LoadBalancerArn** *(string) --*

      The Amazon Resource Name (ARN) of the load balancer.

    - **DNSName** *(string) --*

      The public DNS name of the load balancer.

    - **CanonicalHostedZoneId** *(string) --*

      The ID of the Amazon Route 53 hosted zone associated with the load balancer.

    - **CreatedTime** *(datetime) --*

      The date and time the load balancer was created.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **Scheme** *(string) --*

      The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
      an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
      nodes. Therefore, Internet-facing load balancers can route requests from clients over the
      internet.

      The nodes of an internal load balancer have only private IP addresses. The DNS name of an
      internal load balancer is publicly resolvable to the private IP addresses of the nodes.
      Therefore, internal load balancers can route requests only from clients with access to
      the VPC for the load balancer.

    - **VpcId** *(string) --*

      The ID of the VPC for the load balancer.

    - **State** *(dict) --*

      The state of the load balancer.

      - **Code** *(string) --*

        The state code. The initial state of the load balancer is ``provisioning`` . After the
        load balancer is fully set up and ready to route traffic, its state is ``active`` . If
        the load balancer could not be set up, its state is ``failed`` .

      - **Reason** *(string) --*

        A description of the state.

    - **Type** *(string) --*

      The type of load balancer.

    - **AvailabilityZones** *(list) --*

      The Availability Zones for the load balancer.

      - *(dict) --*

        Information about an Availability Zone.

        - **ZoneName** *(string) --*

          The name of the Availability Zone.

        - **SubnetId** *(string) --*

          The ID of the subnet. You can specify one subnet per Availability Zone.

        - **LoadBalancerAddresses** *(list) --*

          [Network Load Balancers] If you need static IP addresses for your load balancer, you
          can specify one Elastic IP address per Availability Zone when you create the load
          balancer.

          - *(dict) --*

            Information about a static IP address for a load balancer.

            - **IpAddress** *(string) --*

              The static IP address.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.

    - **SecurityGroups** *(list) --*

      The IDs of the security groups for the load balancer.

      - *(string) --*

    - **IpAddressType** *(string) --*

      The type of IP addresses used by the subnets for your load balancer. The possible values
      are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {
        "LoadBalancers": List[
            DescribeLoadBalancersPaginateResponseLoadBalancersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseTypeDef(
    _DescribeLoadBalancersPaginateResponseTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginate` `Response`

    - **LoadBalancers** *(list) --*

      Information about the load balancers.

      - *(dict) --*

        Information about a load balancer.

        - **LoadBalancerArn** *(string) --*

          The Amazon Resource Name (ARN) of the load balancer.

        - **DNSName** *(string) --*

          The public DNS name of the load balancer.

        - **CanonicalHostedZoneId** *(string) --*

          The ID of the Amazon Route 53 hosted zone associated with the load balancer.

        - **CreatedTime** *(datetime) --*

          The date and time the load balancer was created.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **Scheme** *(string) --*

          The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of
          an Internet-facing load balancer is publicly resolvable to the public IP addresses of the
          nodes. Therefore, Internet-facing load balancers can route requests from clients over the
          internet.

          The nodes of an internal load balancer have only private IP addresses. The DNS name of an
          internal load balancer is publicly resolvable to the private IP addresses of the nodes.
          Therefore, internal load balancers can route requests only from clients with access to
          the VPC for the load balancer.

        - **VpcId** *(string) --*

          The ID of the VPC for the load balancer.

        - **State** *(dict) --*

          The state of the load balancer.

          - **Code** *(string) --*

            The state code. The initial state of the load balancer is ``provisioning`` . After the
            load balancer is fully set up and ready to route traffic, its state is ``active`` . If
            the load balancer could not be set up, its state is ``failed`` .

          - **Reason** *(string) --*

            A description of the state.

        - **Type** *(string) --*

          The type of load balancer.

        - **AvailabilityZones** *(list) --*

          The Availability Zones for the load balancer.

          - *(dict) --*

            Information about an Availability Zone.

            - **ZoneName** *(string) --*

              The name of the Availability Zone.

            - **SubnetId** *(string) --*

              The ID of the subnet. You can specify one subnet per Availability Zone.

            - **LoadBalancerAddresses** *(list) --*

              [Network Load Balancers] If you need static IP addresses for your load balancer, you
              can specify one Elastic IP address per Availability Zone when you create the load
              balancer.

              - *(dict) --*

                Information about a static IP address for a load balancer.

                - **IpAddress** *(string) --*

                  The static IP address.

                - **AllocationId** *(string) --*

                  [Network Load Balancers] The allocation ID of the Elastic IP address.

        - **SecurityGroups** *(list) --*

          The IDs of the security groups for the load balancer.

          - *(string) --*

        - **IpAddressType** *(string) --*

          The type of IP addresses used by the subnets for your load balancer. The possible values
          are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRulesPaginatePaginationConfigTypeDef(
    _DescribeRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginate` `PaginationConfig`

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


_DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActions` `AuthenticateCognitoConfig`

    [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
    only when ``Type`` is ``authenticate-cognito`` .

    - **UserPoolArn** *(string) --*

      The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

    - **UserPoolClientId** *(string) --*

      The ID of the Amazon Cognito user pool client.

    - **UserPoolDomain** *(string) --*

      The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.
    """


_DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": str,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActions` `AuthenticateOidcConfig`

    [HTTPS listeners] Information about an identity provider that is compliant with
    OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

    - **Issuer** *(string) --*

      The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **AuthorizationEndpoint** *(string) --*

      The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **TokenEndpoint** *(string) --*

      The token endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **UserInfoEndpoint** *(string) --*

      The user info endpoint of the IdP. This must be a full URL, including the HTTPS
      protocol, the domain, and the path.

    - **ClientId** *(string) --*

      The OAuth 2.0 client identifier.

    - **ClientSecret** *(string) --*

      The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
      If you are modifying a rule, you can omit this parameter if you set
      ``UseExistingClientSecret`` to true.

    - **SessionCookieName** *(string) --*

      The name of the cookie used to maintain session information. The default is
      AWSELBAuthSessionCookie.

    - **Scope** *(string) --*

      The set of user claims to be requested from the IdP. The default is ``openid`` .

      To verify which scope values your IdP supports and how to separate multiple values,
      see the documentation for your IdP.

    - **SessionTimeout** *(integer) --*

      The maximum duration of the authentication session, in seconds. The default is
      604800 seconds (7 days).

    - **AuthenticationRequestExtraParams** *(dict) --*

      The query parameters (up to 10) to include in the redirect request to the
      authorization endpoint.

      - *(string) --*

        - *(string) --*

    - **OnUnauthenticatedRequest** *(string) --*

      The behavior if the user is not authenticated. The following are possible values:

      * deny- Return an HTTP 401 Unauthorized error.

      * allow- Allow the request to be forwarded to the target.

      * authenticate- Redirect the request to the IdP authorization endpoint. This is the
      default value.

    - **UseExistingClientSecret** *(boolean) --*

      Indicates whether to use the existing client secret when modifying a rule. If you
      are creating a rule, you can omit this parameter or set it to false.
    """


_DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef",
    {"MessageBody": str, "StatusCode": str, "ContentType": str},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActions` `FixedResponseConfig`

    [Application Load Balancer] Information for creating an action that returns a custom
    HTTP response. Specify only when ``Type`` is ``fixed-response`` .

    - **MessageBody** *(string) --*

      The message.

    - **StatusCode** *(string) --*

      The HTTP response code (2XX, 4XX, or 5XX).

    - **ContentType** *(string) --*

      The content type.

      Valid Values: text/plain | text/css | text/html | application/javascript |
      application/json
    """


_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef",
    {"Enabled": bool, "DurationSeconds": int},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActionsForwardConfig` `TargetGroupStickinessConfig`

    The target group stickiness for the rule.

    - **Enabled** *(boolean) --*

      Indicates whether target group stickiness is enabled.

    - **DurationSeconds** *(integer) --*

      The time period, in seconds, during which requests from a client should be routed
      to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef",
    {"TargetGroupArn": str, "Weight": int},
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActionsForwardConfig` `TargetGroups`

    Information about how traffic will be distributed between multiple target groups
    in a forward rule.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **Weight** *(integer) --*

      The weight. The range is 0 to 999.
    """


_DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef",
    {
        "TargetGroups": List[
            DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupsTypeDef
        ],
        "TargetGroupStickinessConfig": DescribeRulesPaginateResponseRulesActionsForwardConfigTargetGroupStickinessConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActions` `ForwardConfig`

    Information for creating an action that distributes requests among one or more target
    groups. For Network Load Balancers, you can specify a single target group. Specify
    only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
    ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
    and it must be the same target group specified in ``TargetGroupArn`` .

    - **TargetGroups** *(list) --*

      One or more target groups. For Network Load Balancers, you can specify a single
      target group.

      - *(dict) --*

        Information about how traffic will be distributed between multiple target groups
        in a forward rule.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **Weight** *(integer) --*

          The weight. The range is 0 to 999.

    - **TargetGroupStickinessConfig** *(dict) --*

      The target group stickiness for the rule.

      - **Enabled** *(boolean) --*

        Indicates whether target group stickiness is enabled.

      - **DurationSeconds** *(integer) --*

        The time period, in seconds, during which requests from a client should be routed
        to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
        "StatusCode": str,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef(
    _DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesActions` `RedirectConfig`

    [Application Load Balancer] Information for creating a redirect action. Specify only
    when ``Type`` is ``redirect`` .

    - **Protocol** *(string) --*

      The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
      HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

    - **Port** *(string) --*

      The port. You can specify a value from 1 to 65535 or #{port}.

    - **Host** *(string) --*

      The hostname. This component is not percent-encoded. The hostname can contain
      #{host}.

    - **Path** *(string) --*

      The absolute path, starting with the leading "/". This component is not
      percent-encoded. The path can contain #{host}, #{path}, and #{port}.

    - **Query** *(string) --*

      The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
      include the leading "?", as it is automatically added. You can specify any of the
      reserved keywords.

    - **StatusCode** *(string) --*

      The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
      (HTTP 302).
    """


_DescribeRulesPaginateResponseRulesActionsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesActionsTypeDef",
    {
        "Type": str,
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": DescribeRulesPaginateResponseRulesActionsAuthenticateOidcConfigTypeDef,
        "AuthenticateCognitoConfig": DescribeRulesPaginateResponseRulesActionsAuthenticateCognitoConfigTypeDef,
        "Order": int,
        "RedirectConfig": DescribeRulesPaginateResponseRulesActionsRedirectConfigTypeDef,
        "FixedResponseConfig": DescribeRulesPaginateResponseRulesActionsFixedResponseConfigTypeDef,
        "ForwardConfig": DescribeRulesPaginateResponseRulesActionsForwardConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesActionsTypeDef(
    _DescribeRulesPaginateResponseRulesActionsTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRules` `Actions`

    Information about an action.

    - **Type** *(string) --*

      The type of action.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
      ``forward`` and you want to route to a single target group. To route to one or more
      target groups, use ``ForwardConfig`` instead.

    - **AuthenticateOidcConfig** *(dict) --*

      [HTTPS listeners] Information about an identity provider that is compliant with
      OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

      - **Issuer** *(string) --*

        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **AuthorizationEndpoint** *(string) --*

        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **TokenEndpoint** *(string) --*

        The token endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **UserInfoEndpoint** *(string) --*

        The user info endpoint of the IdP. This must be a full URL, including the HTTPS
        protocol, the domain, and the path.

      - **ClientId** *(string) --*

        The OAuth 2.0 client identifier.

      - **ClientSecret** *(string) --*

        The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
        If you are modifying a rule, you can omit this parameter if you set
        ``UseExistingClientSecret`` to true.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

      - **UseExistingClientSecret** *(boolean) --*

        Indicates whether to use the existing client secret when modifying a rule. If you
        are creating a rule, you can omit this parameter or set it to false.

    - **AuthenticateCognitoConfig** *(dict) --*

      [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
      only when ``Type`` is ``authenticate-cognito`` .

      - **UserPoolArn** *(string) --*

        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

      - **UserPoolClientId** *(string) --*

        The ID of the Amazon Cognito user pool client.

      - **UserPoolDomain** *(string) --*

        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

      - **SessionCookieName** *(string) --*

        The name of the cookie used to maintain session information. The default is
        AWSELBAuthSessionCookie.

      - **Scope** *(string) --*

        The set of user claims to be requested from the IdP. The default is ``openid`` .

        To verify which scope values your IdP supports and how to separate multiple values,
        see the documentation for your IdP.

      - **SessionTimeout** *(integer) --*

        The maximum duration of the authentication session, in seconds. The default is
        604800 seconds (7 days).

      - **AuthenticationRequestExtraParams** *(dict) --*

        The query parameters (up to 10) to include in the redirect request to the
        authorization endpoint.

        - *(string) --*

          - *(string) --*

      - **OnUnauthenticatedRequest** *(string) --*

        The behavior if the user is not authenticated. The following are possible values:

        * deny- Return an HTTP 401 Unauthorized error.

        * allow- Allow the request to be forwarded to the target.

        * authenticate- Redirect the request to the IdP authorization endpoint. This is the
        default value.

    - **Order** *(integer) --*

      The order for the action. This value is required for rules with multiple actions. The
      action with the lowest value for order is performed first. The last action to be
      performed must be one of the following types of actions: a ``forward`` ,
      ``fixed-response`` , or ``redirect`` .

    - **RedirectConfig** *(dict) --*

      [Application Load Balancer] Information for creating a redirect action. Specify only
      when ``Type`` is ``redirect`` .

      - **Protocol** *(string) --*

        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
        HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

      - **Port** *(string) --*

        The port. You can specify a value from 1 to 65535 or #{port}.

      - **Host** *(string) --*

        The hostname. This component is not percent-encoded. The hostname can contain
        #{host}.

      - **Path** *(string) --*

        The absolute path, starting with the leading "/". This component is not
        percent-encoded. The path can contain #{host}, #{path}, and #{port}.

      - **Query** *(string) --*

        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
        include the leading "?", as it is automatically added. You can specify any of the
        reserved keywords.

      - **StatusCode** *(string) --*

        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
        (HTTP 302).

    - **FixedResponseConfig** *(dict) --*

      [Application Load Balancer] Information for creating an action that returns a custom
      HTTP response. Specify only when ``Type`` is ``fixed-response`` .

      - **MessageBody** *(string) --*

        The message.

      - **StatusCode** *(string) --*

        The HTTP response code (2XX, 4XX, or 5XX).

      - **ContentType** *(string) --*

        The content type.

        Valid Values: text/plain | text/css | text/html | application/javascript |
        application/json

    - **ForwardConfig** *(dict) --*

      Information for creating an action that distributes requests among one or more target
      groups. For Network Load Balancers, you can specify a single target group. Specify
      only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
      ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
      and it must be the same target group specified in ``TargetGroupArn`` .

      - **TargetGroups** *(list) --*

        One or more target groups. For Network Load Balancers, you can specify a single
        target group.

        - *(dict) --*

          Information about how traffic will be distributed between multiple target groups
          in a forward rule.

          - **TargetGroupArn** *(string) --*

            The Amazon Resource Name (ARN) of the target group.

          - **Weight** *(integer) --*

            The weight. The range is 0 to 999.

      - **TargetGroupStickinessConfig** *(dict) --*

        The target group stickiness for the rule.

        - **Enabled** *(boolean) --*

          Indicates whether target group stickiness is enabled.

        - **DurationSeconds** *(integer) --*

          The time period, in seconds, during which requests from a client should be routed
          to the same target group. The range is 1-604800 seconds (7 days).
    """


_DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `HostHeaderConfig`

    Information for a host header condition. Specify only when ``Field`` is
    ``host-header`` .

    - **Values** *(list) --*

      One or more host names. The maximum size of each name is 128 characters. The
      comparison is case insensitive. The following wildcard characters are supported: *
      (matches 0 or more characters) and ? (matches exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the host name.

      - *(string) --*
    """


_DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef",
    {"HttpHeaderName": str, "Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `HttpHeaderConfig`

    Information for an HTTP header condition. Specify only when ``Field`` is
    ``http-header`` .

    - **HttpHeaderName** *(string) --*

      The name of the HTTP header field. The maximum size is 40 characters. The header
      name is case insensitive. The allowed characters are specified by RFC 7230.
      Wildcards are not supported.

      You can't use an HTTP header condition to specify the host header. Use
      HostHeaderConditionConfig to specify a host header condition.

    - **Values** *(list) --*

      One or more strings to compare against the value of the HTTP header. The maximum
      size of each string is 128 characters. The comparison strings are case insensitive.
      The following wildcard characters are supported: * (matches 0 or more characters)
      and ? (matches exactly 1 character).

      If the same header appears multiple times in the request, we search them in order
      until a match is found.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the value of the HTTP header. To require that all of the strings are a
      match, create one condition per string.

      - *(string) --*
    """


_DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `HttpRequestMethodConfig`

    Information for an HTTP method condition. Specify only when ``Field`` is
    ``http-request-method`` .

    - **Values** *(list) --*

      The name of the request method. The maximum size is 40 characters. The allowed
      characters are A-Z, hyphen (-), and underscore (_). The comparison is case
      sensitive. Wildcards are not supported; therefore, the method name must be an exact
      match.

      If you specify multiple strings, the condition is satisfied if one of the strings
      matches the HTTP request method. We recommend that you route GET and HEAD requests
      in the same way, because the response to a HEAD request may be cached.

      - *(string) --*
    """


_DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `PathPatternConfig`

    Information for a path pattern condition. Specify only when ``Field`` is
    ``path-pattern`` .

    - **Values** *(list) --*

      One or more path patterns to compare against the request URL. The maximum size of
      each string is 128 characters. The comparison is case sensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character).

      If you specify multiple strings, the condition is satisfied if one of them matches
      the request URL. The path pattern is compared only to the path of the URL, not to
      its query string. To compare against the query string, use
      QueryStringConditionConfig .

      - *(string) --*
    """


_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditionsQueryStringConfig` `Values`

    Information about a key/value pair.

    - **Key** *(string) --*

      The key. You can omit the key.

    - **Value** *(string) --*

      The value.
    """


_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef",
    {
        "Values": List[
            DescribeRulesPaginateResponseRulesConditionsQueryStringConfigValuesTypeDef
        ]
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `QueryStringConfig`

    Information for a query string condition. Specify only when ``Field`` is
    ``query-string`` .

    - **Values** *(list) --*

      One or more key/value pairs or values to find in the query string. The maximum size
      of each string is 128 characters. The comparison is case insensitive. The following
      wildcard characters are supported: * (matches 0 or more characters) and ? (matches
      exactly 1 character). To search for a literal '*' or '?' character in a query
      string, you must escape these characters in ``Values`` using a '\\' character.

      If you specify multiple key/value pairs or values, the condition is satisfied if
      one of them is found in the query string.

      - *(dict) --*

        Information about a key/value pair.

        - **Key** *(string) --*

          The key. You can omit the key.

        - **Value** *(string) --*

          The value.
    """


_DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef",
    {"Values": List[str]},
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRulesConditions` `SourceIpConfig`

    Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

    - **Values** *(list) --*

      One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
      addresses. Wildcards are not supported.

      If you specify multiple addresses, the condition is satisfied if the source IP
      address of the request matches one of the CIDR blocks. This condition is not
      satisfied by the addresses in the X-Forwarded-For header. To search for addresses
      in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

      - *(string) --*
    """


_DescribeRulesPaginateResponseRulesConditionsTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesConditionsTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": DescribeRulesPaginateResponseRulesConditionsHostHeaderConfigTypeDef,
        "PathPatternConfig": DescribeRulesPaginateResponseRulesConditionsPathPatternConfigTypeDef,
        "HttpHeaderConfig": DescribeRulesPaginateResponseRulesConditionsHttpHeaderConfigTypeDef,
        "QueryStringConfig": DescribeRulesPaginateResponseRulesConditionsQueryStringConfigTypeDef,
        "HttpRequestMethodConfig": DescribeRulesPaginateResponseRulesConditionsHttpRequestMethodConfigTypeDef,
        "SourceIpConfig": DescribeRulesPaginateResponseRulesConditionsSourceIpConfigTypeDef,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesConditionsTypeDef(
    _DescribeRulesPaginateResponseRulesConditionsTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponseRules` `Conditions`

    Information about a condition for a rule.

    - **Field** *(string) --*

      The field in the HTTP request. The following are the possible values:

      * ``http-header``

      * ``http-request-method``

      * ``host-header``

      * ``path-pattern``

      * ``query-string``

      * ``source-ip``

    - **Values** *(list) --*

      The condition value. You can use ``Values`` if the rule contains only ``host-header``
      and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
      ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

      If ``Field`` is ``host-header`` , you can specify a single host name (for example,
      my.example.com). A host name is case insensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * - .

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
      example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
      length, and can contain any of the following characters.

      * A-Z, a-z, 0-9

      * _ - . $ / ~ " ' @ : +

      * & (using &amp;)

      * * (matches 0 or more characters)

      * ? (matches exactly 1 character)

      - *(string) --*

    - **HostHeaderConfig** *(dict) --*

      Information for a host header condition. Specify only when ``Field`` is
      ``host-header`` .

      - **Values** *(list) --*

        One or more host names. The maximum size of each name is 128 characters. The
        comparison is case insensitive. The following wildcard characters are supported: *
        (matches 0 or more characters) and ? (matches exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the host name.

        - *(string) --*

    - **PathPatternConfig** *(dict) --*

      Information for a path pattern condition. Specify only when ``Field`` is
      ``path-pattern`` .

      - **Values** *(list) --*

        One or more path patterns to compare against the request URL. The maximum size of
        each string is 128 characters. The comparison is case sensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character).

        If you specify multiple strings, the condition is satisfied if one of them matches
        the request URL. The path pattern is compared only to the path of the URL, not to
        its query string. To compare against the query string, use
        QueryStringConditionConfig .

        - *(string) --*

    - **HttpHeaderConfig** *(dict) --*

      Information for an HTTP header condition. Specify only when ``Field`` is
      ``http-header`` .

      - **HttpHeaderName** *(string) --*

        The name of the HTTP header field. The maximum size is 40 characters. The header
        name is case insensitive. The allowed characters are specified by RFC 7230.
        Wildcards are not supported.

        You can't use an HTTP header condition to specify the host header. Use
        HostHeaderConditionConfig to specify a host header condition.

      - **Values** *(list) --*

        One or more strings to compare against the value of the HTTP header. The maximum
        size of each string is 128 characters. The comparison strings are case insensitive.
        The following wildcard characters are supported: * (matches 0 or more characters)
        and ? (matches exactly 1 character).

        If the same header appears multiple times in the request, we search them in order
        until a match is found.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the value of the HTTP header. To require that all of the strings are a
        match, create one condition per string.

        - *(string) --*

    - **QueryStringConfig** *(dict) --*

      Information for a query string condition. Specify only when ``Field`` is
      ``query-string`` .

      - **Values** *(list) --*

        One or more key/value pairs or values to find in the query string. The maximum size
        of each string is 128 characters. The comparison is case insensitive. The following
        wildcard characters are supported: * (matches 0 or more characters) and ? (matches
        exactly 1 character). To search for a literal '*' or '?' character in a query
        string, you must escape these characters in ``Values`` using a '\\' character.

        If you specify multiple key/value pairs or values, the condition is satisfied if
        one of them is found in the query string.

        - *(dict) --*

          Information about a key/value pair.

          - **Key** *(string) --*

            The key. You can omit the key.

          - **Value** *(string) --*

            The value.

    - **HttpRequestMethodConfig** *(dict) --*

      Information for an HTTP method condition. Specify only when ``Field`` is
      ``http-request-method`` .

      - **Values** *(list) --*

        The name of the request method. The maximum size is 40 characters. The allowed
        characters are A-Z, hyphen (-), and underscore (_). The comparison is case
        sensitive. Wildcards are not supported; therefore, the method name must be an exact
        match.

        If you specify multiple strings, the condition is satisfied if one of the strings
        matches the HTTP request method. We recommend that you route GET and HEAD requests
        in the same way, because the response to a HEAD request may be cached.

        - *(string) --*

    - **SourceIpConfig** *(dict) --*

      Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

      - **Values** *(list) --*

        One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
        addresses. Wildcards are not supported.

        If you specify multiple addresses, the condition is satisfied if the source IP
        address of the request matches one of the CIDR blocks. This condition is not
        satisfied by the addresses in the X-Forwarded-For header. To search for addresses
        in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

        - *(string) --*
    """


_DescribeRulesPaginateResponseRulesTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseRulesTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List[DescribeRulesPaginateResponseRulesConditionsTypeDef],
        "Actions": List[DescribeRulesPaginateResponseRulesActionsTypeDef],
        "IsDefault": bool,
    },
    total=False,
)


class DescribeRulesPaginateResponseRulesTypeDef(
    _DescribeRulesPaginateResponseRulesTypeDef
):
    """
    Type definition for `DescribeRulesPaginateResponse` `Rules`

    Information about a rule.

    - **RuleArn** *(string) --*

      The Amazon Resource Name (ARN) of the rule.

    - **Priority** *(string) --*

      The priority.

    - **Conditions** *(list) --*

      The conditions. Each rule can include zero or one of the following conditions:
      ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
      zero or more of the following conditions: ``http-header`` and ``query-string`` .

      - *(dict) --*

        Information about a condition for a rule.

        - **Field** *(string) --*

          The field in the HTTP request. The following are the possible values:

          * ``http-header``

          * ``http-request-method``

          * ``host-header``

          * ``path-pattern``

          * ``query-string``

          * ``source-ip``

        - **Values** *(list) --*

          The condition value. You can use ``Values`` if the rule contains only ``host-header``
          and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
          ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

          If ``Field`` is ``host-header`` , you can specify a single host name (for example,
          my.example.com). A host name is case insensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * - .

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
          example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
          length, and can contain any of the following characters.

          * A-Z, a-z, 0-9

          * _ - . $ / ~ " ' @ : +

          * & (using &amp;)

          * * (matches 0 or more characters)

          * ? (matches exactly 1 character)

          - *(string) --*

        - **HostHeaderConfig** *(dict) --*

          Information for a host header condition. Specify only when ``Field`` is
          ``host-header`` .

          - **Values** *(list) --*

            One or more host names. The maximum size of each name is 128 characters. The
            comparison is case insensitive. The following wildcard characters are supported: *
            (matches 0 or more characters) and ? (matches exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the host name.

            - *(string) --*

        - **PathPatternConfig** *(dict) --*

          Information for a path pattern condition. Specify only when ``Field`` is
          ``path-pattern`` .

          - **Values** *(list) --*

            One or more path patterns to compare against the request URL. The maximum size of
            each string is 128 characters. The comparison is case sensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character).

            If you specify multiple strings, the condition is satisfied if one of them matches
            the request URL. The path pattern is compared only to the path of the URL, not to
            its query string. To compare against the query string, use
            QueryStringConditionConfig .

            - *(string) --*

        - **HttpHeaderConfig** *(dict) --*

          Information for an HTTP header condition. Specify only when ``Field`` is
          ``http-header`` .

          - **HttpHeaderName** *(string) --*

            The name of the HTTP header field. The maximum size is 40 characters. The header
            name is case insensitive. The allowed characters are specified by RFC 7230.
            Wildcards are not supported.

            You can't use an HTTP header condition to specify the host header. Use
            HostHeaderConditionConfig to specify a host header condition.

          - **Values** *(list) --*

            One or more strings to compare against the value of the HTTP header. The maximum
            size of each string is 128 characters. The comparison strings are case insensitive.
            The following wildcard characters are supported: * (matches 0 or more characters)
            and ? (matches exactly 1 character).

            If the same header appears multiple times in the request, we search them in order
            until a match is found.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the value of the HTTP header. To require that all of the strings are a
            match, create one condition per string.

            - *(string) --*

        - **QueryStringConfig** *(dict) --*

          Information for a query string condition. Specify only when ``Field`` is
          ``query-string`` .

          - **Values** *(list) --*

            One or more key/value pairs or values to find in the query string. The maximum size
            of each string is 128 characters. The comparison is case insensitive. The following
            wildcard characters are supported: * (matches 0 or more characters) and ? (matches
            exactly 1 character). To search for a literal '*' or '?' character in a query
            string, you must escape these characters in ``Values`` using a '\\' character.

            If you specify multiple key/value pairs or values, the condition is satisfied if
            one of them is found in the query string.

            - *(dict) --*

              Information about a key/value pair.

              - **Key** *(string) --*

                The key. You can omit the key.

              - **Value** *(string) --*

                The value.

        - **HttpRequestMethodConfig** *(dict) --*

          Information for an HTTP method condition. Specify only when ``Field`` is
          ``http-request-method`` .

          - **Values** *(list) --*

            The name of the request method. The maximum size is 40 characters. The allowed
            characters are A-Z, hyphen (-), and underscore (_). The comparison is case
            sensitive. Wildcards are not supported; therefore, the method name must be an exact
            match.

            If you specify multiple strings, the condition is satisfied if one of the strings
            matches the HTTP request method. We recommend that you route GET and HEAD requests
            in the same way, because the response to a HEAD request may be cached.

            - *(string) --*

        - **SourceIpConfig** *(dict) --*

          Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

          - **Values** *(list) --*

            One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
            addresses. Wildcards are not supported.

            If you specify multiple addresses, the condition is satisfied if the source IP
            address of the request matches one of the CIDR blocks. This condition is not
            satisfied by the addresses in the X-Forwarded-For header. To search for addresses
            in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

            - *(string) --*

    - **Actions** *(list) --*

      The actions. Each rule must include exactly one of the following types of actions:
      ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
      performed.

      - *(dict) --*

        Information about an action.

        - **Type** *(string) --*

          The type of action.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
          ``forward`` and you want to route to a single target group. To route to one or more
          target groups, use ``ForwardConfig`` instead.

        - **AuthenticateOidcConfig** *(dict) --*

          [HTTPS listeners] Information about an identity provider that is compliant with
          OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

          - **Issuer** *(string) --*

            The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **AuthorizationEndpoint** *(string) --*

            The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **TokenEndpoint** *(string) --*

            The token endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **UserInfoEndpoint** *(string) --*

            The user info endpoint of the IdP. This must be a full URL, including the HTTPS
            protocol, the domain, and the path.

          - **ClientId** *(string) --*

            The OAuth 2.0 client identifier.

          - **ClientSecret** *(string) --*

            The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
            If you are modifying a rule, you can omit this parameter if you set
            ``UseExistingClientSecret`` to true.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

          - **UseExistingClientSecret** *(boolean) --*

            Indicates whether to use the existing client secret when modifying a rule. If you
            are creating a rule, you can omit this parameter or set it to false.

        - **AuthenticateCognitoConfig** *(dict) --*

          [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
          only when ``Type`` is ``authenticate-cognito`` .

          - **UserPoolArn** *(string) --*

            The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

          - **UserPoolClientId** *(string) --*

            The ID of the Amazon Cognito user pool client.

          - **UserPoolDomain** *(string) --*

            The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

          - **SessionCookieName** *(string) --*

            The name of the cookie used to maintain session information. The default is
            AWSELBAuthSessionCookie.

          - **Scope** *(string) --*

            The set of user claims to be requested from the IdP. The default is ``openid`` .

            To verify which scope values your IdP supports and how to separate multiple values,
            see the documentation for your IdP.

          - **SessionTimeout** *(integer) --*

            The maximum duration of the authentication session, in seconds. The default is
            604800 seconds (7 days).

          - **AuthenticationRequestExtraParams** *(dict) --*

            The query parameters (up to 10) to include in the redirect request to the
            authorization endpoint.

            - *(string) --*

              - *(string) --*

          - **OnUnauthenticatedRequest** *(string) --*

            The behavior if the user is not authenticated. The following are possible values:

            * deny- Return an HTTP 401 Unauthorized error.

            * allow- Allow the request to be forwarded to the target.

            * authenticate- Redirect the request to the IdP authorization endpoint. This is the
            default value.

        - **Order** *(integer) --*

          The order for the action. This value is required for rules with multiple actions. The
          action with the lowest value for order is performed first. The last action to be
          performed must be one of the following types of actions: a ``forward`` ,
          ``fixed-response`` , or ``redirect`` .

        - **RedirectConfig** *(dict) --*

          [Application Load Balancer] Information for creating a redirect action. Specify only
          when ``Type`` is ``redirect`` .

          - **Protocol** *(string) --*

            The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
            HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

          - **Port** *(string) --*

            The port. You can specify a value from 1 to 65535 or #{port}.

          - **Host** *(string) --*

            The hostname. This component is not percent-encoded. The hostname can contain
            #{host}.

          - **Path** *(string) --*

            The absolute path, starting with the leading "/". This component is not
            percent-encoded. The path can contain #{host}, #{path}, and #{port}.

          - **Query** *(string) --*

            The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
            include the leading "?", as it is automatically added. You can specify any of the
            reserved keywords.

          - **StatusCode** *(string) --*

            The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
            (HTTP 302).

        - **FixedResponseConfig** *(dict) --*

          [Application Load Balancer] Information for creating an action that returns a custom
          HTTP response. Specify only when ``Type`` is ``fixed-response`` .

          - **MessageBody** *(string) --*

            The message.

          - **StatusCode** *(string) --*

            The HTTP response code (2XX, 4XX, or 5XX).

          - **ContentType** *(string) --*

            The content type.

            Valid Values: text/plain | text/css | text/html | application/javascript |
            application/json

        - **ForwardConfig** *(dict) --*

          Information for creating an action that distributes requests among one or more target
          groups. For Network Load Balancers, you can specify a single target group. Specify
          only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
          ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
          and it must be the same target group specified in ``TargetGroupArn`` .

          - **TargetGroups** *(list) --*

            One or more target groups. For Network Load Balancers, you can specify a single
            target group.

            - *(dict) --*

              Information about how traffic will be distributed between multiple target groups
              in a forward rule.

              - **TargetGroupArn** *(string) --*

                The Amazon Resource Name (ARN) of the target group.

              - **Weight** *(integer) --*

                The weight. The range is 0 to 999.

          - **TargetGroupStickinessConfig** *(dict) --*

            The target group stickiness for the rule.

            - **Enabled** *(boolean) --*

              Indicates whether target group stickiness is enabled.

            - **DurationSeconds** *(integer) --*

              The time period, in seconds, during which requests from a client should be routed
              to the same target group. The range is 1-604800 seconds (7 days).

    - **IsDefault** *(boolean) --*

      Indicates whether this is the default rule.
    """


_DescribeRulesPaginateResponseTypeDef = TypedDict(
    "_DescribeRulesPaginateResponseTypeDef",
    {"Rules": List[DescribeRulesPaginateResponseRulesTypeDef], "NextToken": str},
    total=False,
)


class DescribeRulesPaginateResponseTypeDef(_DescribeRulesPaginateResponseTypeDef):
    """
    Type definition for `DescribeRulesPaginate` `Response`

    - **Rules** *(list) --*

      Information about the rules.

      - *(dict) --*

        Information about a rule.

        - **RuleArn** *(string) --*

          The Amazon Resource Name (ARN) of the rule.

        - **Priority** *(string) --*

          The priority.

        - **Conditions** *(list) --*

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and
          zero or more of the following conditions: ``http-header`` and ``query-string`` .

          - *(dict) --*

            Information about a condition for a rule.

            - **Field** *(string) --*

              The field in the HTTP request. The following are the possible values:

              * ``http-header``

              * ``http-request-method``

              * ``host-header``

              * ``path-pattern``

              * ``query-string``

              * ``source-ip``

            - **Values** *(list) --*

              The condition value. You can use ``Values`` if the rule contains only ``host-header``
              and ``path-pattern`` conditions. Otherwise, you can use ``HostHeaderConfig`` for
              ``host-header`` conditions and ``PathPatternConfig`` for ``path-pattern`` conditions.

              If ``Field`` is ``host-header`` , you can specify a single host name (for example,
              my.example.com). A host name is case insensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * - .

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              If ``Field`` is ``path-pattern`` , you can specify a single path pattern (for
              example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in
              length, and can contain any of the following characters.

              * A-Z, a-z, 0-9

              * _ - . $ / ~ " ' @ : +

              * & (using &amp;)

              * * (matches 0 or more characters)

              * ? (matches exactly 1 character)

              - *(string) --*

            - **HostHeaderConfig** *(dict) --*

              Information for a host header condition. Specify only when ``Field`` is
              ``host-header`` .

              - **Values** *(list) --*

                One or more host names. The maximum size of each name is 128 characters. The
                comparison is case insensitive. The following wildcard characters are supported: *
                (matches 0 or more characters) and ? (matches exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the host name.

                - *(string) --*

            - **PathPatternConfig** *(dict) --*

              Information for a path pattern condition. Specify only when ``Field`` is
              ``path-pattern`` .

              - **Values** *(list) --*

                One or more path patterns to compare against the request URL. The maximum size of
                each string is 128 characters. The comparison is case sensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character).

                If you specify multiple strings, the condition is satisfied if one of them matches
                the request URL. The path pattern is compared only to the path of the URL, not to
                its query string. To compare against the query string, use
                QueryStringConditionConfig .

                - *(string) --*

            - **HttpHeaderConfig** *(dict) --*

              Information for an HTTP header condition. Specify only when ``Field`` is
              ``http-header`` .

              - **HttpHeaderName** *(string) --*

                The name of the HTTP header field. The maximum size is 40 characters. The header
                name is case insensitive. The allowed characters are specified by RFC 7230.
                Wildcards are not supported.

                You can't use an HTTP header condition to specify the host header. Use
                HostHeaderConditionConfig to specify a host header condition.

              - **Values** *(list) --*

                One or more strings to compare against the value of the HTTP header. The maximum
                size of each string is 128 characters. The comparison strings are case insensitive.
                The following wildcard characters are supported: * (matches 0 or more characters)
                and ? (matches exactly 1 character).

                If the same header appears multiple times in the request, we search them in order
                until a match is found.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the value of the HTTP header. To require that all of the strings are a
                match, create one condition per string.

                - *(string) --*

            - **QueryStringConfig** *(dict) --*

              Information for a query string condition. Specify only when ``Field`` is
              ``query-string`` .

              - **Values** *(list) --*

                One or more key/value pairs or values to find in the query string. The maximum size
                of each string is 128 characters. The comparison is case insensitive. The following
                wildcard characters are supported: * (matches 0 or more characters) and ? (matches
                exactly 1 character). To search for a literal '*' or '?' character in a query
                string, you must escape these characters in ``Values`` using a '\\' character.

                If you specify multiple key/value pairs or values, the condition is satisfied if
                one of them is found in the query string.

                - *(dict) --*

                  Information about a key/value pair.

                  - **Key** *(string) --*

                    The key. You can omit the key.

                  - **Value** *(string) --*

                    The value.

            - **HttpRequestMethodConfig** *(dict) --*

              Information for an HTTP method condition. Specify only when ``Field`` is
              ``http-request-method`` .

              - **Values** *(list) --*

                The name of the request method. The maximum size is 40 characters. The allowed
                characters are A-Z, hyphen (-), and underscore (_). The comparison is case
                sensitive. Wildcards are not supported; therefore, the method name must be an exact
                match.

                If you specify multiple strings, the condition is satisfied if one of the strings
                matches the HTTP request method. We recommend that you route GET and HEAD requests
                in the same way, because the response to a HEAD request may be cached.

                - *(string) --*

            - **SourceIpConfig** *(dict) --*

              Information for a source IP condition. Specify only when ``Field`` is ``source-ip`` .

              - **Values** *(list) --*

                One or more source IP addresses, in CIDR format. You can use both IPv4 and IPv6
                addresses. Wildcards are not supported.

                If you specify multiple addresses, the condition is satisfied if the source IP
                address of the request matches one of the CIDR blocks. This condition is not
                satisfied by the addresses in the X-Forwarded-For header. To search for addresses
                in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

                - *(string) --*

        - **Actions** *(list) --*

          The actions. Each rule must include exactly one of the following types of actions:
          ``forward`` , ``redirect`` , or ``fixed-response`` , and it must be the last action to be
          performed.

          - *(dict) --*

            Information about an action.

            - **Type** *(string) --*

              The type of action.

            - **TargetGroupArn** *(string) --*

              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is
              ``forward`` and you want to route to a single target group. To route to one or more
              target groups, use ``ForwardConfig`` instead.

            - **AuthenticateOidcConfig** *(dict) --*

              [HTTPS listeners] Information about an identity provider that is compliant with
              OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .

              - **Issuer** *(string) --*

                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **AuthorizationEndpoint** *(string) --*

                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **TokenEndpoint** *(string) --*

                The token endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **UserInfoEndpoint** *(string) --*

                The user info endpoint of the IdP. This must be a full URL, including the HTTPS
                protocol, the domain, and the path.

              - **ClientId** *(string) --*

                The OAuth 2.0 client identifier.

              - **ClientSecret** *(string) --*

                The OAuth 2.0 client secret. This parameter is required if you are creating a rule.
                If you are modifying a rule, you can omit this parameter if you set
                ``UseExistingClientSecret`` to true.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

              - **UseExistingClientSecret** *(boolean) --*

                Indicates whether to use the existing client secret when modifying a rule. If you
                are creating a rule, you can omit this parameter or set it to false.

            - **AuthenticateCognitoConfig** *(dict) --*

              [HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify
              only when ``Type`` is ``authenticate-cognito`` .

              - **UserPoolArn** *(string) --*

                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

              - **UserPoolClientId** *(string) --*

                The ID of the Amazon Cognito user pool client.

              - **UserPoolDomain** *(string) --*

                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

              - **SessionCookieName** *(string) --*

                The name of the cookie used to maintain session information. The default is
                AWSELBAuthSessionCookie.

              - **Scope** *(string) --*

                The set of user claims to be requested from the IdP. The default is ``openid`` .

                To verify which scope values your IdP supports and how to separate multiple values,
                see the documentation for your IdP.

              - **SessionTimeout** *(integer) --*

                The maximum duration of the authentication session, in seconds. The default is
                604800 seconds (7 days).

              - **AuthenticationRequestExtraParams** *(dict) --*

                The query parameters (up to 10) to include in the redirect request to the
                authorization endpoint.

                - *(string) --*

                  - *(string) --*

              - **OnUnauthenticatedRequest** *(string) --*

                The behavior if the user is not authenticated. The following are possible values:

                * deny- Return an HTTP 401 Unauthorized error.

                * allow- Allow the request to be forwarded to the target.

                * authenticate- Redirect the request to the IdP authorization endpoint. This is the
                default value.

            - **Order** *(integer) --*

              The order for the action. This value is required for rules with multiple actions. The
              action with the lowest value for order is performed first. The last action to be
              performed must be one of the following types of actions: a ``forward`` ,
              ``fixed-response`` , or ``redirect`` .

            - **RedirectConfig** *(dict) --*

              [Application Load Balancer] Information for creating a redirect action. Specify only
              when ``Type`` is ``redirect`` .

              - **Protocol** *(string) --*

                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to
                HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.

              - **Port** *(string) --*

                The port. You can specify a value from 1 to 65535 or #{port}.

              - **Host** *(string) --*

                The hostname. This component is not percent-encoded. The hostname can contain
                #{host}.

              - **Path** *(string) --*

                The absolute path, starting with the leading "/". This component is not
                percent-encoded. The path can contain #{host}, #{path}, and #{port}.

              - **Query** *(string) --*

                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not
                include the leading "?", as it is automatically added. You can specify any of the
                reserved keywords.

              - **StatusCode** *(string) --*

                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary
                (HTTP 302).

            - **FixedResponseConfig** *(dict) --*

              [Application Load Balancer] Information for creating an action that returns a custom
              HTTP response. Specify only when ``Type`` is ``fixed-response`` .

              - **MessageBody** *(string) --*

                The message.

              - **StatusCode** *(string) --*

                The HTTP response code (2XX, 4XX, or 5XX).

              - **ContentType** *(string) --*

                The content type.

                Valid Values: text/plain | text/css | text/html | application/javascript |
                application/json

            - **ForwardConfig** *(dict) --*

              Information for creating an action that distributes requests among one or more target
              groups. For Network Load Balancers, you can specify a single target group. Specify
              only when ``Type`` is ``forward`` . If you specify both ``ForwardConfig`` and
              ``TargetGroupArn`` , you can specify only one target group using ``ForwardConfig``
              and it must be the same target group specified in ``TargetGroupArn`` .

              - **TargetGroups** *(list) --*

                One or more target groups. For Network Load Balancers, you can specify a single
                target group.

                - *(dict) --*

                  Information about how traffic will be distributed between multiple target groups
                  in a forward rule.

                  - **TargetGroupArn** *(string) --*

                    The Amazon Resource Name (ARN) of the target group.

                  - **Weight** *(integer) --*

                    The weight. The range is 0 to 999.

              - **TargetGroupStickinessConfig** *(dict) --*

                The target group stickiness for the rule.

                - **Enabled** *(boolean) --*

                  Indicates whether target group stickiness is enabled.

                - **DurationSeconds** *(integer) --*

                  The time period, in seconds, during which requests from a client should be routed
                  to the same target group. The range is 1-604800 seconds (7 days).

        - **IsDefault** *(boolean) --*

          Indicates whether this is the default rule.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeSSLPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSSLPoliciesPaginatePaginationConfigTypeDef(
    _DescribeSSLPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeSSLPoliciesPaginate` `PaginationConfig`

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


_DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef",
    {"Name": str, "Priority": int},
    total=False,
)


class DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef(
    _DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef
):
    """
    Type definition for `DescribeSSLPoliciesPaginateResponseSslPolicies` `Ciphers`

    Information about a cipher used in a policy.

    - **Name** *(string) --*

      The name of the cipher.

    - **Priority** *(integer) --*

      The priority of the cipher.
    """


_DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List[DescribeSSLPoliciesPaginateResponseSslPoliciesCiphersTypeDef],
        "Name": str,
    },
    total=False,
)


class DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef(
    _DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef
):
    """
    Type definition for `DescribeSSLPoliciesPaginateResponse` `SslPolicies`

    Information about a policy used for SSL negotiation.

    - **SslProtocols** *(list) --*

      The protocols.

      - *(string) --*

    - **Ciphers** *(list) --*

      The ciphers.

      - *(dict) --*

        Information about a cipher used in a policy.

        - **Name** *(string) --*

          The name of the cipher.

        - **Priority** *(integer) --*

          The priority of the cipher.

    - **Name** *(string) --*

      The name of the policy.
    """


_DescribeSSLPoliciesPaginateResponseTypeDef = TypedDict(
    "_DescribeSSLPoliciesPaginateResponseTypeDef",
    {
        "SslPolicies": List[DescribeSSLPoliciesPaginateResponseSslPoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeSSLPoliciesPaginateResponseTypeDef(
    _DescribeSSLPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeSSLPoliciesPaginate` `Response`

    - **SslPolicies** *(list) --*

      Information about the policies.

      - *(dict) --*

        Information about a policy used for SSL negotiation.

        - **SslProtocols** *(list) --*

          The protocols.

          - *(string) --*

        - **Ciphers** *(list) --*

          The ciphers.

          - *(dict) --*

            Information about a cipher used in a policy.

            - **Name** *(string) --*

              The name of the cipher.

            - **Priority** *(integer) --*

              The priority of the cipher.

        - **Name** *(string) --*

          The name of the policy.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeTargetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTargetGroupsPaginatePaginationConfigTypeDef(
    _DescribeTargetGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeTargetGroupsPaginate` `PaginationConfig`

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


_DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef",
    {"HttpCode": str},
    total=False,
)


class DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef(
    _DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef
):
    """
    Type definition for `DescribeTargetGroupsPaginateResponseTargetGroups` `Matcher`

    The HTTP codes to use when checking for a successful response from a target.

    - **HttpCode** *(string) --*

      The HTTP codes.

      For Application Load Balancers, you can specify values between 200 and 499, and the
      default value is 200. You can specify multiple values (for example, "200,202") or a
      range of values (for example, "200-299").

      For Network Load Balancers, this is 200–399.
    """


_DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": str,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": DescribeTargetGroupsPaginateResponseTargetGroupsMatcherTypeDef,
        "LoadBalancerArns": List[str],
        "TargetType": str,
    },
    total=False,
)


class DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef(
    _DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef
):
    """
    Type definition for `DescribeTargetGroupsPaginateResponse` `TargetGroups`

    Information about a target group.

    - **TargetGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the target group.

    - **TargetGroupName** *(string) --*

      The name of the target group.

    - **Protocol** *(string) --*

      The protocol to use for routing traffic to the targets.

    - **Port** *(integer) --*

      The port on which the targets are listening. Not used if the target is a Lambda function.

    - **VpcId** *(string) --*

      The ID of the VPC for the targets.

    - **HealthCheckProtocol** *(string) --*

      The protocol to use to connect with the target.

    - **HealthCheckPort** *(string) --*

      The port to use to connect with the target.

    - **HealthCheckEnabled** *(boolean) --*

      Indicates whether health checks are enabled.

    - **HealthCheckIntervalSeconds** *(integer) --*

      The approximate amount of time, in seconds, between health checks of an individual target.

    - **HealthCheckTimeoutSeconds** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

    - **HealthyThresholdCount** *(integer) --*

      The number of consecutive health checks successes required before considering an
      unhealthy target healthy.

    - **UnhealthyThresholdCount** *(integer) --*

      The number of consecutive health check failures required before considering the target
      unhealthy.

    - **HealthCheckPath** *(string) --*

      The destination for the health check request.

    - **Matcher** *(dict) --*

      The HTTP codes to use when checking for a successful response from a target.

      - **HttpCode** *(string) --*

        The HTTP codes.

        For Application Load Balancers, you can specify values between 200 and 499, and the
        default value is 200. You can specify multiple values (for example, "200,202") or a
        range of values (for example, "200-299").

        For Network Load Balancers, this is 200–399.

    - **LoadBalancerArns** *(list) --*

      The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
      group.

      - *(string) --*

    - **TargetType** *(string) --*

      The type of target that you must specify when registering targets with this target group.
      The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
      (targets are specified by IP address).
    """


_DescribeTargetGroupsPaginateResponseTypeDef = TypedDict(
    "_DescribeTargetGroupsPaginateResponseTypeDef",
    {
        "TargetGroups": List[DescribeTargetGroupsPaginateResponseTargetGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTargetGroupsPaginateResponseTypeDef(
    _DescribeTargetGroupsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeTargetGroupsPaginate` `Response`

    - **TargetGroups** *(list) --*

      Information about the target groups.

      - *(dict) --*

        Information about a target group.

        - **TargetGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the target group.

        - **TargetGroupName** *(string) --*

          The name of the target group.

        - **Protocol** *(string) --*

          The protocol to use for routing traffic to the targets.

        - **Port** *(integer) --*

          The port on which the targets are listening. Not used if the target is a Lambda function.

        - **VpcId** *(string) --*

          The ID of the VPC for the targets.

        - **HealthCheckProtocol** *(string) --*

          The protocol to use to connect with the target.

        - **HealthCheckPort** *(string) --*

          The port to use to connect with the target.

        - **HealthCheckEnabled** *(boolean) --*

          Indicates whether health checks are enabled.

        - **HealthCheckIntervalSeconds** *(integer) --*

          The approximate amount of time, in seconds, between health checks of an individual target.

        - **HealthCheckTimeoutSeconds** *(integer) --*

          The amount of time, in seconds, during which no response means a failed health check.

        - **HealthyThresholdCount** *(integer) --*

          The number of consecutive health checks successes required before considering an
          unhealthy target healthy.

        - **UnhealthyThresholdCount** *(integer) --*

          The number of consecutive health check failures required before considering the target
          unhealthy.

        - **HealthCheckPath** *(string) --*

          The destination for the health check request.

        - **Matcher** *(dict) --*

          The HTTP codes to use when checking for a successful response from a target.

          - **HttpCode** *(string) --*

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the
            default value is 200. You can specify multiple values (for example, "200,202") or a
            range of values (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        - **LoadBalancerArns** *(list) --*

          The Amazon Resource Names (ARN) of the load balancers that route traffic to this target
          group.

          - *(string) --*

        - **TargetType** *(string) --*

          The type of target that you must specify when registering targets with this target group.
          The possible values are ``instance`` (targets are specified by instance ID) or ``ip``
          (targets are specified by IP address).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_LoadBalancerAvailableWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancerAvailableWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class LoadBalancerAvailableWaitWaiterConfigTypeDef(
    _LoadBalancerAvailableWaitWaiterConfigTypeDef
):
    """
    Type definition for `LoadBalancerAvailableWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_LoadBalancerExistsWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancerExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class LoadBalancerExistsWaitWaiterConfigTypeDef(
    _LoadBalancerExistsWaitWaiterConfigTypeDef
):
    """
    Type definition for `LoadBalancerExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_LoadBalancersDeletedWaitWaiterConfigTypeDef = TypedDict(
    "_LoadBalancersDeletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class LoadBalancersDeletedWaitWaiterConfigTypeDef(
    _LoadBalancersDeletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `LoadBalancersDeletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_RequiredTargetDeregisteredWaitTargetsTypeDef = TypedDict(
    "_RequiredTargetDeregisteredWaitTargetsTypeDef", {"Id": str}
)
_OptionalTargetDeregisteredWaitTargetsTypeDef = TypedDict(
    "_OptionalTargetDeregisteredWaitTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class TargetDeregisteredWaitTargetsTypeDef(
    _RequiredTargetDeregisteredWaitTargetsTypeDef,
    _OptionalTargetDeregisteredWaitTargetsTypeDef,
):
    """
    Type definition for `TargetDeregisteredWait` `Targets`

    Information about a target.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the target. If the target type of the target group is ``instance`` , specify an
      instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
      ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic from
      the load balancer nodes in the specified Availability Zone or from all enabled Availability
      Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the target
      group, the Availability Zone is automatically detected and this parameter is optional. If the
      IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is outside
      the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported value is
      ``all`` .
    """


_TargetDeregisteredWaitWaiterConfigTypeDef = TypedDict(
    "_TargetDeregisteredWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TargetDeregisteredWaitWaiterConfigTypeDef(
    _TargetDeregisteredWaitWaiterConfigTypeDef
):
    """
    Type definition for `TargetDeregisteredWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_RequiredTargetInServiceWaitTargetsTypeDef = TypedDict(
    "_RequiredTargetInServiceWaitTargetsTypeDef", {"Id": str}
)
_OptionalTargetInServiceWaitTargetsTypeDef = TypedDict(
    "_OptionalTargetInServiceWaitTargetsTypeDef",
    {"Port": int, "AvailabilityZone": str},
    total=False,
)


class TargetInServiceWaitTargetsTypeDef(
    _RequiredTargetInServiceWaitTargetsTypeDef,
    _OptionalTargetInServiceWaitTargetsTypeDef,
):
    """
    Type definition for `TargetInServiceWait` `Targets`

    Information about a target.

    - **Id** *(string) --* **[REQUIRED]**

      The ID of the target. If the target type of the target group is ``instance`` , specify an
      instance ID. If the target type is ``ip`` , specify an IP address. If the target type is
      ``lambda`` , specify the ARN of the Lambda function.

    - **Port** *(integer) --*

      The port on which the target is listening. Not used if the target is a Lambda function.

    - **AvailabilityZone** *(string) --*

      An Availability Zone or ``all`` . This determines whether the target receives traffic from
      the load balancer nodes in the specified Availability Zone or from all enabled Availability
      Zones for the load balancer.

      This parameter is not supported if the target type of the target group is ``instance`` .

      If the target type is ``ip`` and the IP address is in a subnet of the VPC for the target
      group, the Availability Zone is automatically detected and this parameter is optional. If the
      IP address is outside the VPC, this parameter is required.

      With an Application Load Balancer, if the target type is ``ip`` and the IP address is outside
      the VPC for the target group, the only supported value is ``all`` .

      If the target type is ``lambda`` , this parameter is optional and the only supported value is
      ``all`` .
    """


_TargetInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_TargetInServiceWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TargetInServiceWaitWaiterConfigTypeDef(_TargetInServiceWaitWaiterConfigTypeDef):
    """
    Type definition for `TargetInServiceWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """
