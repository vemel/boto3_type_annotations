"Main interface for elbv2 Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

# pylint: disable=import-self
import mypy_boto3_elbv2.client as client_scope

# pylint: disable=import-self
import mypy_boto3_elbv2.paginator as paginator_scope
from mypy_boto3_elbv2.type_defs import (
    ClientAddListenerCertificatesCertificatesTypeDef,
    ClientAddListenerCertificatesResponseTypeDef,
    ClientAddTagsTagsTypeDef,
    ClientCreateListenerCertificatesTypeDef,
    ClientCreateListenerDefaultActionsTypeDef,
    ClientCreateListenerResponseTypeDef,
    ClientCreateLoadBalancerResponseTypeDef,
    ClientCreateLoadBalancerSubnetMappingsTypeDef,
    ClientCreateLoadBalancerTagsTypeDef,
    ClientCreateRuleActionsTypeDef,
    ClientCreateRuleConditionsTypeDef,
    ClientCreateRuleResponseTypeDef,
    ClientCreateTargetGroupMatcherTypeDef,
    ClientCreateTargetGroupResponseTypeDef,
    ClientDeregisterTargetsTargetsTypeDef,
    ClientDescribeAccountLimitsResponseTypeDef,
    ClientDescribeListenerCertificatesResponseTypeDef,
    ClientDescribeListenersResponseTypeDef,
    ClientDescribeLoadBalancerAttributesResponseTypeDef,
    ClientDescribeLoadBalancersResponseTypeDef,
    ClientDescribeRulesResponseTypeDef,
    ClientDescribeSslPoliciesResponseTypeDef,
    ClientDescribeTagsResponseTypeDef,
    ClientDescribeTargetGroupAttributesResponseTypeDef,
    ClientDescribeTargetGroupsResponseTypeDef,
    ClientDescribeTargetHealthResponseTypeDef,
    ClientDescribeTargetHealthTargetsTypeDef,
    ClientModifyListenerCertificatesTypeDef,
    ClientModifyListenerDefaultActionsTypeDef,
    ClientModifyListenerResponseTypeDef,
    ClientModifyLoadBalancerAttributesAttributesTypeDef,
    ClientModifyLoadBalancerAttributesResponseTypeDef,
    ClientModifyRuleActionsTypeDef,
    ClientModifyRuleConditionsTypeDef,
    ClientModifyRuleResponseTypeDef,
    ClientModifyTargetGroupAttributesAttributesTypeDef,
    ClientModifyTargetGroupAttributesResponseTypeDef,
    ClientModifyTargetGroupMatcherTypeDef,
    ClientModifyTargetGroupResponseTypeDef,
    ClientRegisterTargetsTargetsTypeDef,
    ClientRemoveListenerCertificatesCertificatesTypeDef,
    ClientSetIpAddressTypeResponseTypeDef,
    ClientSetRulePrioritiesResponseTypeDef,
    ClientSetRulePrioritiesRulePrioritiesTypeDef,
    ClientSetSecurityGroupsResponseTypeDef,
    ClientSetSubnetsResponseTypeDef,
    ClientSetSubnetsSubnetMappingsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_elbv2.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_listener_certificates(
        self,
        ListenerArn: str,
        Certificates: List[ClientAddListenerCertificatesCertificatesTypeDef],
    ) -> ClientAddListenerCertificatesResponseTypeDef:
        """
        Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS
        listener.

        If the certificate in already in the certificate list, the call is successful but the certificate
        is not added again.

        To get the certificate list for a listener, use  DescribeListenerCertificates . To remove
        certificates from the certificate list for a listener, use  RemoveListenerCertificates . To replace
        the default certificate for a listener, use  ModifyListener .

        For more information, see `SSL Certificates
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates>`__
        in the *Application Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddListenerCertificates>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddListenerCertificates>`_

        **Request Syntax**
        ::

          response = client.add_listener_certificates(
              ListenerArn='string',
              Certificates=[
                  {
                      'CertificateArn': 'string',
                      'IsDefault': True|False
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the listener.

        :type Certificates: list
        :param Certificates: **[REQUIRED]**

          The certificate to add. You can specify one certificate per call. Set ``CertificateArn`` to the
          certificate ARN but do not set ``IsDefault`` .

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value when
              specifying a certificate as an input. This value is not included in the output when
              describing a listener, but is included when describing listener certificates.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags(
        self, ResourceArns: List[str], Tags: List[ClientAddTagsTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your
        Application Load Balancers, Network Load Balancers, and your target groups.

        Each tag consists of a key and an optional value. If a resource already has a tag with the same
        key, ``AddTags`` updates its value.

        To list the current tags for your resources, use  DescribeTags . To remove tags from your
        resources, use  RemoveTags .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddTags>`_

        **Request Syntax**
        ::

          response = client.add_tags(
              ResourceArns=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

          - *(string) --*

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The tags. Each resource can have a maximum of 10 tags.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_listener(
        self,
        LoadBalancerArn: str,
        Protocol: str,
        Port: int,
        DefaultActions: List[ClientCreateListenerDefaultActionsTypeDef],
        SslPolicy: str = None,
        Certificates: List[ClientCreateListenerCertificatesTypeDef] = None,
    ) -> ClientCreateListenerResponseTypeDef:
        """
        Creates a listener for the specified Application Load Balancer or Network Load Balancer.

        To update a listener, use  ModifyListener . When you are finished with a listener, you can delete
        it using  DeleteListener . If you are finished with both the listener and the load balancer, you
        can delete them both using  DeleteLoadBalancer .

        This operation is idempotent, which means that it completes at most one time. If you attempt to
        create multiple listeners with the same settings, each call succeeds.

        For more information, see `Listeners for Your Application Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html>`__
        in the *Application Load Balancers Guide* and `Listeners for Your Network Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html>`__
        in the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateListener>`_

        **Request Syntax**
        ::

          response = client.create_listener(
              LoadBalancerArn='string',
              Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
              Port=123,
              SslPolicy='string',
              Certificates=[
                  {
                      'CertificateArn': 'string',
                      'IsDefault': True|False
                  },
              ],
              DefaultActions=[
                  {
                      'Type':
                      'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                      'TargetGroupArn': 'string',
                      'AuthenticateOidcConfig': {
                          'Issuer': 'string',
                          'AuthorizationEndpoint': 'string',
                          'TokenEndpoint': 'string',
                          'UserInfoEndpoint': 'string',
                          'ClientId': 'string',
                          'ClientSecret': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                          'UseExistingClientSecret': True|False
                      },
                      'AuthenticateCognitoConfig': {
                          'UserPoolArn': 'string',
                          'UserPoolClientId': 'string',
                          'UserPoolDomain': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                      },
                      'Order': 123,
                      'RedirectConfig': {
                          'Protocol': 'string',
                          'Port': 'string',
                          'Host': 'string',
                          'Path': 'string',
                          'Query': 'string',
                          'StatusCode': 'HTTP_301'|'HTTP_302'
                      },
                      'FixedResponseConfig': {
                          'MessageBody': 'string',
                          'StatusCode': 'string',
                          'ContentType': 'string'
                      },
                      'ForwardConfig': {
                          'TargetGroups': [
                              {
                                  'TargetGroupArn': 'string',
                                  'Weight': 123
                              },
                          ],
                          'TargetGroupStickinessConfig': {
                              'Enabled': True|False,
                              'DurationSeconds': 123
                          }
                      }
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :type Protocol: string
        :param Protocol: **[REQUIRED]**

          The protocol for connections from clients to the load balancer. For Application Load Balancers,
          the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols
          are TCP, TLS, UDP, and TCP_UDP.

        :type Port: integer
        :param Port: **[REQUIRED]**

          The port on which the load balancer is listening.

        :type SslPolicy: string
        :param SslPolicy:

          [HTTPS and TLS listeners] The security policy that defines which ciphers and protocols are
          supported. The default is the current predefined security policy.

        :type Certificates: list
        :param Certificates:

          [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one
          certificate. Set ``CertificateArn`` to the certificate ARN but do not set ``IsDefault`` .

          To create a certificate list for the listener, use  AddListenerCertificates .

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value when
              specifying a certificate as an input. This value is not included in the output when
              describing a listener, but is included when describing listener certificates.

        :type DefaultActions: list
        :param DefaultActions: **[REQUIRED]**

          The actions for the default rule. The rule must include one forward action or one or more
          fixed-response actions.

          If the action type is ``forward`` , you specify one or more target groups. The protocol of the
          target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target
          group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.

          [HTTPS listeners] If the action type is ``authenticate-oidc`` , you authenticate users through an
          identity provider that is OpenID Connect (OIDC) compliant.

          [HTTPS listeners] If the action type is ``authenticate-cognito`` , you authenticate users through
          the user pools supported by Amazon Cognito.

          [Application Load Balancer] If the action type is ``redirect`` , you redirect specified client
          requests from one URL to another.

          [Application Load Balancer] If the action type is ``fixed-response`` , you drop specified client
          requests and return a custom HTTP response.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Listeners': [
                    {
                        'ListenerArn': 'string',
                        'LoadBalancerArn': 'string',
                        'Port': 123,
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Certificates': [
                            {
                                'CertificateArn': 'string',
                                'IsDefault': True|False
                            },
                        ],
                        'SslPolicy': 'string',
                        'DefaultActions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_load_balancer(
        self,
        Name: str,
        Subnets: List[str] = None,
        SubnetMappings: List[ClientCreateLoadBalancerSubnetMappingsTypeDef] = None,
        SecurityGroups: List[str] = None,
        Scheme: str = None,
        Tags: List[ClientCreateLoadBalancerTagsTypeDef] = None,
        Type: str = None,
        IpAddressType: str = None,
    ) -> ClientCreateLoadBalancerResponseTypeDef:
        """
        Creates an Application Load Balancer or a Network Load Balancer.

        When you create a load balancer, you can specify security groups, public subnets, IP address type,
        and tags. Otherwise, you could do so later using  SetSecurityGroups ,  SetSubnets ,
        SetIpAddressType , and  AddTags .

        To create listeners for your load balancer, use  CreateListener . To describe your current load
        balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete
        it using  DeleteLoadBalancer .

        For limit information, see `Limits for Your Application Load Balancer
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__
        in the *Application Load Balancers Guide* and `Limits for Your Network Load Balancer
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in
        the *Network Load Balancers Guide* .

        This operation is idempotent, which means that it completes at most one time. If you attempt to
        create multiple load balancers with the same settings, each call succeeds.

        For more information, see `Application Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html>`__
        in the *Application Load Balancers Guide* and `Network Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html>`__ in
        the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer>`_

        **Request Syntax**
        ::

          response = client.create_load_balancer(
              Name='string',
              Subnets=[
                  'string',
              ],
              SubnetMappings=[
                  {
                      'SubnetId': 'string',
                      'AllocationId': 'string'
                  },
              ],
              SecurityGroups=[
                  'string',
              ],
              Scheme='internet-facing'|'internal',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              Type='application'|'network',
              IpAddressType='ipv4'|'dualstack'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the load balancer.

          This name must be unique per region per account, can have a maximum of 32 characters, must
          contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must
          not begin with "internal-".

        :type Subnets: list
        :param Subnets:

          The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must
          specify either subnets or subnet mappings.

          [Application Load Balancers] You must specify subnets from at least two Availability Zones.

          [Network Load Balancers] You can specify subnets from one or more Availability Zones.

          - *(string) --*

        :type SubnetMappings: list
        :param SubnetMappings:

          The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must
          specify either subnets or subnet mappings.

          [Application Load Balancers] You must specify subnets from at least two Availability Zones. You
          cannot specify Elastic IP addresses for your subnets.

          [Network Load Balancers] You can specify subnets from one or more Availability Zones. You can
          specify one Elastic IP address per subnet if you need static IP addresses for your load balancer.

          - *(dict) --*

            Information about a subnet mapping.

            - **SubnetId** *(string) --*

              The ID of the subnet.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.

        :type SecurityGroups: list
        :param SecurityGroups:

          [Application Load Balancers] The IDs of the security groups for the load balancer.

          - *(string) --*

        :type Scheme: string
        :param Scheme:

          The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an
          Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes.
          Therefore, Internet-facing load balancers can route requests from clients over the internet.

          The nodes of an internal load balancer have only private IP addresses. The DNS name of an
          internal load balancer is publicly resolvable to the private IP addresses of the nodes.
          Therefore, internal load balancers can route requests only from clients with access to the VPC
          for the load balancer.

          The default is an Internet-facing load balancer.

        :type Tags: list
        :param Tags:

          One or more tags to assign to the load balancer.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :type Type: string
        :param Type:

          The type of load balancer. The default is ``application`` .

        :type IpAddressType: string
        :param IpAddressType:

          [Application Load Balancers] The type of IP addresses used by the subnets for your load balancer.
          The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6
          addresses). Internal load balancers must use ``ipv4`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LoadBalancers': [
                    {
                        'LoadBalancerArn': 'string',
                        'DNSName': 'string',
                        'CanonicalHostedZoneId': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LoadBalancerName': 'string',
                        'Scheme': 'internet-facing'|'internal',
                        'VpcId': 'string',
                        'State': {
                            'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                            'Reason': 'string'
                        },
                        'Type': 'application'|'network',
                        'AvailabilityZones': [
                            {
                                'ZoneName': 'string',
                                'SubnetId': 'string',
                                'LoadBalancerAddresses': [
                                    {
                                        'IpAddress': 'string',
                                        'AllocationId': 'string'
                                    },
                                ]
                            },
                        ],
                        'SecurityGroups': [
                            'string',
                        ],
                        'IpAddressType': 'ipv4'|'dualstack'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_rule(
        self,
        ListenerArn: str,
        Conditions: List[ClientCreateRuleConditionsTypeDef],
        Priority: int,
        Actions: List[ClientCreateRuleActionsTypeDef],
    ) -> ClientCreateRuleResponseTypeDef:
        """
        Creates a rule for the specified listener. The listener must be associated with an Application Load
        Balancer.

        Rules are evaluated in priority order, from the lowest value to the highest value. When the
        conditions for a rule are met, its actions are performed. If the conditions for no rules are met,
        the actions for the default rule are performed. For more information, see `Listener Rules
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules>`__
        in the *Application Load Balancers Guide* .

        To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the
        priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateRule>`_

        **Request Syntax**
        ::

          response = client.create_rule(
              ListenerArn='string',
              Conditions=[
                  {
                      'Field': 'string',
                      'Values': [
                          'string',
                      ],
                      'HostHeaderConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'PathPatternConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'HttpHeaderConfig': {
                          'HttpHeaderName': 'string',
                          'Values': [
                              'string',
                          ]
                      },
                      'QueryStringConfig': {
                          'Values': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      },
                      'HttpRequestMethodConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'SourceIpConfig': {
                          'Values': [
                              'string',
                          ]
                      }
                  },
              ],
              Priority=123,
              Actions=[
                  {
                      'Type':
                      'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                      'TargetGroupArn': 'string',
                      'AuthenticateOidcConfig': {
                          'Issuer': 'string',
                          'AuthorizationEndpoint': 'string',
                          'TokenEndpoint': 'string',
                          'UserInfoEndpoint': 'string',
                          'ClientId': 'string',
                          'ClientSecret': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                          'UseExistingClientSecret': True|False
                      },
                      'AuthenticateCognitoConfig': {
                          'UserPoolArn': 'string',
                          'UserPoolClientId': 'string',
                          'UserPoolDomain': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                      },
                      'Order': 123,
                      'RedirectConfig': {
                          'Protocol': 'string',
                          'Port': 'string',
                          'Host': 'string',
                          'Path': 'string',
                          'Query': 'string',
                          'StatusCode': 'HTTP_301'|'HTTP_302'
                      },
                      'FixedResponseConfig': {
                          'MessageBody': 'string',
                          'StatusCode': 'string',
                          'ContentType': 'string'
                      },
                      'ForwardConfig': {
                          'TargetGroups': [
                              {
                                  'TargetGroupArn': 'string',
                                  'Weight': 123
                              },
                          ],
                          'TargetGroupStickinessConfig': {
                              'Enabled': True|False,
                              'DurationSeconds': 123
                          }
                      }
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the listener.

        :type Conditions: list
        :param Conditions: **[REQUIRED]**

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and zero or
          more of the following conditions: ``http-header`` and ``query-string`` .

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

        :type Priority: integer
        :param Priority: **[REQUIRED]**

          The rule priority. A listener can't have multiple rules with the same priority.

        :type Actions: list
        :param Actions: **[REQUIRED]**

          The actions. Each rule must include exactly one of the following types of actions: ``forward`` ,
          ``fixed-response`` , or ``redirect`` , and it must be the last action to be performed.

          If the action type is ``forward`` , you specify one or more target groups. The protocol of the
          target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target
          group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.

          [HTTPS listeners] If the action type is ``authenticate-oidc`` , you authenticate users through an
          identity provider that is OpenID Connect (OIDC) compliant.

          [HTTPS listeners] If the action type is ``authenticate-cognito`` , you authenticate users through
          the user pools supported by Amazon Cognito.

          [Application Load Balancer] If the action type is ``redirect`` , you redirect specified client
          requests from one URL to another.

          [Application Load Balancer] If the action type is ``fixed-response`` , you drop specified client
          requests and return a custom HTTP response.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'RuleArn': 'string',
                        'Priority': 'string',
                        'Conditions': [
                            {
                                'Field': 'string',
                                'Values': [
                                    'string',
                                ],
                                'HostHeaderConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'PathPatternConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'HttpHeaderConfig': {
                                    'HttpHeaderName': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'QueryStringConfig': {
                                    'Values': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                                'HttpRequestMethodConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'SourceIpConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            },
                        ],
                        'Actions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ],
                        'IsDefault': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_target_group(
        self,
        Name: str,
        Protocol: str = None,
        Port: int = None,
        VpcId: str = None,
        HealthCheckProtocol: str = None,
        HealthCheckPort: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: ClientCreateTargetGroupMatcherTypeDef = None,
        TargetType: str = None,
    ) -> ClientCreateTargetGroupResponseTypeDef:
        """
        Creates a target group.

        To register targets with the target group, use  RegisterTargets . To update the health check
        settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the
        target group, use  DescribeTargetHealth .

        To route traffic to the targets in a target group, specify the target group in an action using
        CreateListener or  CreateRule .

        To delete a target group, use  DeleteTargetGroup .

        This operation is idempotent, which means that it completes at most one time. If you attempt to
        create multiple target groups with the same settings, each call succeeds.

        For more information, see `Target Groups for Your Application Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html>`__
        in the *Application Load Balancers Guide* or `Target Groups for Your Network Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>`__
        in the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateTargetGroup>`_

        **Request Syntax**
        ::

          response = client.create_target_group(
              Name='string',
              Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
              Port=123,
              VpcId='string',
              HealthCheckProtocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
              HealthCheckPort='string',
              HealthCheckEnabled=True|False,
              HealthCheckPath='string',
              HealthCheckIntervalSeconds=123,
              HealthCheckTimeoutSeconds=123,
              HealthyThresholdCount=123,
              UnhealthyThresholdCount=123,
              Matcher={
                  'HttpCode': 'string'
              },
              TargetType='instance'|'ip'|'lambda'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the target group.

          This name must be unique per region per account, can have a maximum of 32 characters, must
          contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

        :type Protocol: string
        :param Protocol:

          The protocol to use for routing traffic to the targets. For Application Load Balancers, the
          supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are
          TCP, TLS, UDP, or TCP_UDP. A TCP_UDP listener must be associated with a TCP_UDP target group. If
          the target is a Lambda function, this parameter does not apply.

        :type Port: integer
        :param Port:

          The port on which the targets receive traffic. This port is used unless you specify a port
          override when registering the target. If the target is a Lambda function, this parameter does not
          apply.

        :type VpcId: string
        :param VpcId:

          The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this
          parameter does not apply. Otherwise, this parameter is required.

        :type HealthCheckProtocol: string
        :param HealthCheckProtocol:

          The protocol the load balancer uses when performing health checks on targets. For Application
          Load Balancers, the default is HTTP. For Network Load Balancers, the default is TCP. The TCP
          protocol is supported for health checks only if the protocol of the target group is TCP, TLS,
          UDP, or TCP_UDP. The TLS, UDP, and TCP_UDP protocols are not supported for health checks.

        :type HealthCheckPort: string
        :param HealthCheckPort:

          The port the load balancer uses when performing health checks on targets. The default is
          ``traffic-port`` , which is the port on which each target receives traffic from the load balancer.

        :type HealthCheckEnabled: boolean
        :param HealthCheckEnabled:

          Indicates whether health checks are enabled. If the target type is ``lambda`` , health checks are
          disabled by default but can be enabled. If the target type is ``instance`` or ``ip`` , health
          checks are always enabled and cannot be disabled.

        :type HealthCheckPath: string
        :param HealthCheckPath:

          [HTTP/HTTPS health checks] The ping path that is the destination on the targets for health
          checks. The default is /.

        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds:

          The approximate amount of time, in seconds, between health checks of an individual target. For
          HTTP and HTTPS health checks, the range is 5–300 seconds. For TCP health checks, the supported
          values are 10 and 30 seconds. If the target type is ``instance`` or ``ip`` , the default is 30
          seconds. If the target type is ``lambda`` , the default is 35 seconds.

        :type HealthCheckTimeoutSeconds: integer
        :param HealthCheckTimeoutSeconds:

          The amount of time, in seconds, during which no response from a target means a failed health
          check. For target groups with a protocol of HTTP or HTTPS, the default is 5 seconds. For target
          groups with a protocol of TCP or TLS, this value must be 6 seconds for HTTP health checks and 10
          seconds for TCP and HTTPS health checks. If the target type is ``lambda`` , the default is 30
          seconds.

        :type HealthyThresholdCount: integer
        :param HealthyThresholdCount:

          The number of consecutive health checks successes required before considering an unhealthy target
          healthy. For target groups with a protocol of HTTP or HTTPS, the default is 5. For target groups
          with a protocol of TCP or TLS, the default is 3. If the target type is ``lambda`` , the default
          is 5.

        :type UnhealthyThresholdCount: integer
        :param UnhealthyThresholdCount:

          The number of consecutive health check failures required before considering a target unhealthy.
          For target groups with a protocol of HTTP or HTTPS, the default is 2. For target groups with a
          protocol of TCP or TLS, this value must be the same as the healthy threshold count. If the target
          type is ``lambda`` , the default is 2.

        :type Matcher: dict
        :param Matcher:

          [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
          target.

          - **HttpCode** *(string) --* **[REQUIRED]**

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the default
            value is 200. You can specify multiple values (for example, "200,202") or a range of values
            (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        :type TargetType: string
        :param TargetType:

          The type of target that you must specify when registering targets with this target group. You
          can't specify targets for a target group using more than one target type.

          * ``instance`` - Targets are specified by instance ID. This is the default value. If the target
          group protocol is UDP or TCP_UDP, the target type must be ``instance`` .

          * ``ip`` - Targets are specified by IP address. You can specify IP addresses from the subnets of
          the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8,
          172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify
          publicly routable IP addresses.

          * ``lambda`` - The target groups contains a single Lambda function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetGroups': [
                    {
                        'TargetGroupArn': 'string',
                        'TargetGroupName': 'string',
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Port': 123,
                        'VpcId': 'string',
                        'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'HealthCheckPort': 'string',
                        'HealthCheckEnabled': True|False,
                        'HealthCheckIntervalSeconds': 123,
                        'HealthCheckTimeoutSeconds': 123,
                        'HealthyThresholdCount': 123,
                        'UnhealthyThresholdCount': 123,
                        'HealthCheckPath': 'string',
                        'Matcher': {
                            'HttpCode': 'string'
                        },
                        'LoadBalancerArns': [
                            'string',
                        ],
                        'TargetType': 'instance'|'ip'|'lambda'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_listener(self, ListenerArn: str) -> Dict[str, Any]:
        """
        Deletes the specified listener.

        Alternatively, your listener is deleted when you delete the load balancer to which it is attached,
        using  DeleteLoadBalancer .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteListener>`_

        **Request Syntax**
        ::

          response = client.delete_listener(
              ListenerArn='string'
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the listener.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict[str, Any]:
        """
        Deletes the specified Application Load Balancer or Network Load Balancer and its attached listeners.

        You can't delete a load balancer if deletion protection is enabled. If the load balancer does not
        exist or has already been deleted, the call succeeds.

        Deleting a load balancer does not affect its registered targets. For example, your EC2 instances
        continue to run and are still registered to their target groups. If you no longer need these EC2
        instances, you can stop or terminate them.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteLoadBalancer>`_

        **Request Syntax**
        ::

          response = client.delete_load_balancer(
              LoadBalancerArn='string'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_rule(self, RuleArn: str) -> Dict[str, Any]:
        """
        Deletes the specified rule.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteRule>`_

        **Request Syntax**
        ::

          response = client.delete_rule(
              RuleArn='string'
          )
        :type RuleArn: string
        :param RuleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rule.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_target_group(self, TargetGroupArn: str) -> Dict[str, Any]:
        """
        Deletes the specified target group.

        You can delete a target group if it is not referenced by any actions. Deleting a target group also
        deletes any associated health checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteTargetGroup>`_

        **Request Syntax**
        ::

          response = client.delete_target_group(
              TargetGroupArn='string'
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_targets(
        self, TargetGroupArn: str, Targets: List[ClientDeregisterTargetsTargetsTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters the specified targets from the specified target group. After the targets are
        deregistered, they no longer receive traffic from the load balancer.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeregisterTargets>`_

        **Request Syntax**
        ::

          response = client.deregister_targets(
              TargetGroupArn='string',
              Targets=[
                  {
                      'Id': 'string',
                      'Port': 123,
                      'AvailabilityZone': 'string'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :type Targets: list
        :param Targets: **[REQUIRED]**

          The targets. If you specified a port override when you registered a target, you must specify both
          the target ID and the port when you deregister it.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_limits(
        self, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeAccountLimitsResponseTypeDef:
        """
        Describes the current Elastic Load Balancing resource limits for your AWS account.

        For more information, see `Limits for Your Application Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__
        in the *Application Load Balancer Guide* or `Limits for Your Network Load Balancers
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in
        the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits>`_

        **Request Syntax**
        ::

          response = client.describe_account_limits(
              Marker='string',
              PageSize=123
          )
        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Limits': [
                    {
                        'Name': 'string',
                        'Max': 'string'
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listener_certificates(
        self, ListenerArn: str, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeListenerCertificatesResponseTypeDef:
        """
        Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.

        If the default certificate is also in the certificate list, it appears twice in the results (once
        with ``IsDefault`` set to true and once with ``IsDefault`` set to false).

        For more information, see `SSL Certificates
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates>`__
        in the *Application Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_

        **Request Syntax**
        ::

          response = client.describe_listener_certificates(
              ListenerArn='string',
              Marker='string',
              PageSize=123
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Names (ARN) of the listener.

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificates': [
                    {
                        'CertificateArn': 'string',
                        'IsDefault': True|False
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listeners(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeListenersResponseTypeDef:
        """
        Describes the specified listeners or the listeners for the specified Application Load Balancer or
        Network Load Balancer. You must specify either a load balancer or one or more listeners.

        For an HTTPS or TLS listener, the output includes the default certificate for the listener. To
        describe the certificate list for the listener, use  DescribeListenerCertificates .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_

        **Request Syntax**
        ::

          response = client.describe_listeners(
              LoadBalancerArn='string',
              ListenerArns=[
                  'string',
              ],
              Marker='string',
              PageSize=123
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn:

          The Amazon Resource Name (ARN) of the load balancer.

        :type ListenerArns: list
        :param ListenerArns:

          The Amazon Resource Names (ARN) of the listeners.

          - *(string) --*

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Listeners': [
                    {
                        'ListenerArn': 'string',
                        'LoadBalancerArn': 'string',
                        'Port': 123,
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Certificates': [
                            {
                                'CertificateArn': 'string',
                                'IsDefault': True|False
                            },
                        ],
                        'SslPolicy': 'string',
                        'DefaultActions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ]
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancer_attributes(
        self, LoadBalancerArn: str
    ) -> ClientDescribeLoadBalancerAttributesResponseTypeDef:
        """
        Describes the attributes for the specified Application Load Balancer or Network Load Balancer.

        For more information, see `Load Balancer Attributes
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes>`__
        in the *Application Load Balancers Guide* or `Load Balancer Attributes
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes>`__
        in the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes>`_

        **Request Syntax**
        ::

          response = client.describe_load_balancer_attributes(
              LoadBalancerArn='string'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_load_balancers(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeLoadBalancersResponseTypeDef:
        """
        Describes the specified load balancers or all of your load balancers.

        To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes
        for a load balancer, use  DescribeLoadBalancerAttributes .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_

        **Request Syntax**
        ::

          response = client.describe_load_balancers(
              LoadBalancerArns=[
                  'string',
              ],
              Names=[
                  'string',
              ],
              Marker='string',
              PageSize=123
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns:

          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in
          a single call.

          - *(string) --*

        :type Names: list
        :param Names:

          The names of the load balancers.

          - *(string) --*

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LoadBalancers': [
                    {
                        'LoadBalancerArn': 'string',
                        'DNSName': 'string',
                        'CanonicalHostedZoneId': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LoadBalancerName': 'string',
                        'Scheme': 'internet-facing'|'internal',
                        'VpcId': 'string',
                        'State': {
                            'Code': 'active'|'provisioning'|'active_impaired'|'failed',
                            'Reason': 'string'
                        },
                        'Type': 'application'|'network',
                        'AvailabilityZones': [
                            {
                                'ZoneName': 'string',
                                'SubnetId': 'string',
                                'LoadBalancerAddresses': [
                                    {
                                        'IpAddress': 'string',
                                        'AllocationId': 'string'
                                    },
                                ]
                            },
                        ],
                        'SecurityGroups': [
                            'string',
                        ],
                        'IpAddressType': 'ipv4'|'dualstack'
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_rules(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeRulesResponseTypeDef:
        """
        Describes the specified rules or the rules for the specified listener. You must specify either a
        listener or one or more rules.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeRules>`_

        **Request Syntax**
        ::

          response = client.describe_rules(
              ListenerArn='string',
              RuleArns=[
                  'string',
              ],
              Marker='string',
              PageSize=123
          )
        :type ListenerArn: string
        :param ListenerArn:

          The Amazon Resource Name (ARN) of the listener.

        :type RuleArns: list
        :param RuleArns:

          The Amazon Resource Names (ARN) of the rules.

          - *(string) --*

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'RuleArn': 'string',
                        'Priority': 'string',
                        'Conditions': [
                            {
                                'Field': 'string',
                                'Values': [
                                    'string',
                                ],
                                'HostHeaderConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'PathPatternConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'HttpHeaderConfig': {
                                    'HttpHeaderName': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'QueryStringConfig': {
                                    'Values': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                                'HttpRequestMethodConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'SourceIpConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            },
                        ],
                        'Actions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ],
                        'IsDefault': True|False
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ssl_policies(
        self, Names: List[str] = None, Marker: str = None, PageSize: int = None
    ) -> ClientDescribeSslPoliciesResponseTypeDef:
        """
        Describes the specified policies or all policies used for SSL negotiation.

        For more information, see `Security Policies
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__
        in the *Application Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies>`_

        **Request Syntax**
        ::

          response = client.describe_ssl_policies(
              Names=[
                  'string',
              ],
              Marker='string',
              PageSize=123
          )
        :type Names: list
        :param Names:

          The names of the policies.

          - *(string) --*

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SslPolicies': [
                    {
                        'SslProtocols': [
                            'string',
                        ],
                        'Ciphers': [
                            {
                                'Name': 'string',
                                'Priority': 123
                            },
                        ],
                        'Name': 'string'
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_tags(
        self, ResourceArns: List[str]
    ) -> ClientDescribeTagsResponseTypeDef:
        """
        Describes the tags for the specified resources. You can describe the tags for one or more
        Application Load Balancers, Network Load Balancers, and target groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTags>`_

        **Request Syntax**
        ::

          response = client.describe_tags(
              ResourceArns=[
                  'string',
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]**

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagDescriptions': [
                    {
                        'ResourceArn': 'string',
                        'Tags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_group_attributes(
        self, TargetGroupArn: str
    ) -> ClientDescribeTargetGroupAttributesResponseTypeDef:
        """
        Describes the attributes for the specified target group.

        For more information, see `Target Group Attributes
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-attributes>`__
        in the *Application Load Balancers Guide* or `Target Group Attributes
        <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-group-attributes>`__
        in the *Network Load Balancers Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroupAttributes>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroupAttributes>`_

        **Request Syntax**
        ::

          response = client.describe_target_group_attributes(
              TargetGroupArn='string'
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_groups(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        Marker: str = None,
        PageSize: int = None,
    ) -> ClientDescribeTargetGroupsResponseTypeDef:
        """
        Describes the specified target groups or all of your target groups. By default, all target groups
        are described. Alternatively, you can specify one of the following to filter the results: the ARN
        of the load balancer, the names of one or more target groups, or the ARNs of one or more target
        groups.

        To describe the targets for a target group, use  DescribeTargetHealth . To describe the attributes
        of a target group, use  DescribeTargetGroupAttributes .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_

        **Request Syntax**
        ::

          response = client.describe_target_groups(
              LoadBalancerArn='string',
              TargetGroupArns=[
                  'string',
              ],
              Names=[
                  'string',
              ],
              Marker='string',
              PageSize=123
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn:

          The Amazon Resource Name (ARN) of the load balancer.

        :type TargetGroupArns: list
        :param TargetGroupArns:

          The Amazon Resource Names (ARN) of the target groups.

          - *(string) --*

        :type Names: list
        :param Names:

          The names of the target groups.

          - *(string) --*

        :type Marker: string
        :param Marker:

          The marker for the next set of results. (You received this marker from a previous call.)

        :type PageSize: integer
        :param PageSize:

          The maximum number of results to return with this call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetGroups': [
                    {
                        'TargetGroupArn': 'string',
                        'TargetGroupName': 'string',
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Port': 123,
                        'VpcId': 'string',
                        'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'HealthCheckPort': 'string',
                        'HealthCheckEnabled': True|False,
                        'HealthCheckIntervalSeconds': 123,
                        'HealthCheckTimeoutSeconds': 123,
                        'HealthyThresholdCount': 123,
                        'UnhealthyThresholdCount': 123,
                        'HealthCheckPath': 'string',
                        'Matcher': {
                            'HttpCode': 'string'
                        },
                        'LoadBalancerArns': [
                            'string',
                        ],
                        'TargetType': 'instance'|'ip'|'lambda'
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_target_health(
        self,
        TargetGroupArn: str,
        Targets: List[ClientDescribeTargetHealthTargetsTypeDef] = None,
    ) -> ClientDescribeTargetHealthResponseTypeDef:
        """
        Describes the health of the specified targets or all of your targets.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth>`_

        **Request Syntax**
        ::

          response = client.describe_target_health(
              TargetGroupArn='string',
              Targets=[
                  {
                      'Id': 'string',
                      'Port': 123,
                      'AvailabilityZone': 'string'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :type Targets: list
        :param Targets:

          The targets.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetHealthDescriptions': [
                    {
                        'Target': {
                            'Id': 'string',
                            'Port': 123,
                            'AvailabilityZone': 'string'
                        },
                        'HealthCheckPort': 'string',
                        'TargetHealth': {
                            'State': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                            'Reason':
                            'Elb.RegistrationInProgress'|'Elb.InitialHealthChecking'
                            |'Target.ResponseCodeMismatch'|'Target.Timeout'|'Target.FailedHealthChecks'
                            |'Target.NotRegistered'|'Target.NotInUse'|'Target.DeregistrationInProgress'
                            |'Target.InvalidState'|'Target.IpUnusable'|'Target.HealthCheckDisabled'
                            |'Elb.InternalError',
                            'Description': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_listener(
        self,
        ListenerArn: str,
        Port: int = None,
        Protocol: str = None,
        SslPolicy: str = None,
        Certificates: List[ClientModifyListenerCertificatesTypeDef] = None,
        DefaultActions: List[ClientModifyListenerDefaultActionsTypeDef] = None,
    ) -> ClientModifyListenerResponseTypeDef:
        """
        Replaces the specified properties of the specified listener. Any properties that you do not specify
        remain unchanged.

        Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and
        default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS,
        you must add the security policy and default certificate properties.

        To add an item to a list, remove an item from a list, or update an item in a list, you must provide
        the entire list. For example, to add an action, specify a list with the current actions plus the
        new action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyListener>`_

        **Request Syntax**
        ::

          response = client.modify_listener(
              ListenerArn='string',
              Port=123,
              Protocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
              SslPolicy='string',
              Certificates=[
                  {
                      'CertificateArn': 'string',
                      'IsDefault': True|False
                  },
              ],
              DefaultActions=[
                  {
                      'Type':
                      'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                      'TargetGroupArn': 'string',
                      'AuthenticateOidcConfig': {
                          'Issuer': 'string',
                          'AuthorizationEndpoint': 'string',
                          'TokenEndpoint': 'string',
                          'UserInfoEndpoint': 'string',
                          'ClientId': 'string',
                          'ClientSecret': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                          'UseExistingClientSecret': True|False
                      },
                      'AuthenticateCognitoConfig': {
                          'UserPoolArn': 'string',
                          'UserPoolClientId': 'string',
                          'UserPoolDomain': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                      },
                      'Order': 123,
                      'RedirectConfig': {
                          'Protocol': 'string',
                          'Port': 'string',
                          'Host': 'string',
                          'Path': 'string',
                          'Query': 'string',
                          'StatusCode': 'HTTP_301'|'HTTP_302'
                      },
                      'FixedResponseConfig': {
                          'MessageBody': 'string',
                          'StatusCode': 'string',
                          'ContentType': 'string'
                      },
                      'ForwardConfig': {
                          'TargetGroups': [
                              {
                                  'TargetGroupArn': 'string',
                                  'Weight': 123
                              },
                          ],
                          'TargetGroupStickinessConfig': {
                              'Enabled': True|False,
                              'DurationSeconds': 123
                          }
                      }
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the listener.

        :type Port: integer
        :param Port:

          The port for connections from clients to the load balancer.

        :type Protocol: string
        :param Protocol:

          The protocol for connections from clients to the load balancer. Application Load Balancers
          support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, and
          TCP_UDP protocols.

        :type SslPolicy: string
        :param SslPolicy:

          [HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are
          supported. For more information, see `Security Policies
          <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__
          in the *Application Load Balancers Guide* .

        :type Certificates: list
        :param Certificates:

          [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one
          certificate. Set ``CertificateArn`` to the certificate ARN but do not set ``IsDefault`` .

          To create a certificate list, use  AddListenerCertificates .

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value when
              specifying a certificate as an input. This value is not included in the output when
              describing a listener, but is included when describing listener certificates.

        :type DefaultActions: list
        :param DefaultActions:

          The actions for the default rule. The rule must include one forward action or one or more
          fixed-response actions.

          If the action type is ``forward`` , you specify one or more target groups. The protocol of the
          target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target
          group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.

          [HTTPS listeners] If the action type is ``authenticate-oidc`` , you authenticate users through an
          identity provider that is OpenID Connect (OIDC) compliant.

          [HTTPS listeners] If the action type is ``authenticate-cognito`` , you authenticate users through
          the user pools supported by Amazon Cognito.

          [Application Load Balancer] If the action type is ``redirect`` , you redirect specified client
          requests from one URL to another.

          [Application Load Balancer] If the action type is ``fixed-response`` , you drop specified client
          requests and return a custom HTTP response.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Listeners': [
                    {
                        'ListenerArn': 'string',
                        'LoadBalancerArn': 'string',
                        'Port': 123,
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Certificates': [
                            {
                                'CertificateArn': 'string',
                                'IsDefault': True|False
                            },
                        ],
                        'SslPolicy': 'string',
                        'DefaultActions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_load_balancer_attributes(
        self,
        LoadBalancerArn: str,
        Attributes: List[ClientModifyLoadBalancerAttributesAttributesTypeDef],
    ) -> ClientModifyLoadBalancerAttributesResponseTypeDef:
        """
        Modifies the specified attributes of the specified Application Load Balancer or Network Load
        Balancer.

        If any of the specified attributes can't be modified as requested, the call fails. Any existing
        attributes that you do not modify retain their current values.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes>`_

        **Request Syntax**
        ::

          response = client.modify_load_balancer_attributes(
              LoadBalancerArn='string',
              Attributes=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :type Attributes: list
        :param Attributes: **[REQUIRED]**

          The load balancer attributes.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_rule(
        self,
        RuleArn: str,
        Conditions: List[ClientModifyRuleConditionsTypeDef] = None,
        Actions: List[ClientModifyRuleActionsTypeDef] = None,
    ) -> ClientModifyRuleResponseTypeDef:
        """
        Replaces the specified properties of the specified rule. Any properties that you do not specify are
        unchanged.

        To add an item to a list, remove an item from a list, or update an item in a list, you must provide
        the entire list. For example, to add an action, specify a list with the current actions plus the
        new action.

        To modify the actions for the default rule, use  ModifyListener .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyRule>`_

        **Request Syntax**
        ::

          response = client.modify_rule(
              RuleArn='string',
              Conditions=[
                  {
                      'Field': 'string',
                      'Values': [
                          'string',
                      ],
                      'HostHeaderConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'PathPatternConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'HttpHeaderConfig': {
                          'HttpHeaderName': 'string',
                          'Values': [
                              'string',
                          ]
                      },
                      'QueryStringConfig': {
                          'Values': [
                              {
                                  'Key': 'string',
                                  'Value': 'string'
                              },
                          ]
                      },
                      'HttpRequestMethodConfig': {
                          'Values': [
                              'string',
                          ]
                      },
                      'SourceIpConfig': {
                          'Values': [
                              'string',
                          ]
                      }
                  },
              ],
              Actions=[
                  {
                      'Type':
                      'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'|'fixed-response',
                      'TargetGroupArn': 'string',
                      'AuthenticateOidcConfig': {
                          'Issuer': 'string',
                          'AuthorizationEndpoint': 'string',
                          'TokenEndpoint': 'string',
                          'UserInfoEndpoint': 'string',
                          'ClientId': 'string',
                          'ClientSecret': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                          'UseExistingClientSecret': True|False
                      },
                      'AuthenticateCognitoConfig': {
                          'UserPoolArn': 'string',
                          'UserPoolClientId': 'string',
                          'UserPoolDomain': 'string',
                          'SessionCookieName': 'string',
                          'Scope': 'string',
                          'SessionTimeout': 123,
                          'AuthenticationRequestExtraParams': {
                              'string': 'string'
                          },
                          'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                      },
                      'Order': 123,
                      'RedirectConfig': {
                          'Protocol': 'string',
                          'Port': 'string',
                          'Host': 'string',
                          'Path': 'string',
                          'Query': 'string',
                          'StatusCode': 'HTTP_301'|'HTTP_302'
                      },
                      'FixedResponseConfig': {
                          'MessageBody': 'string',
                          'StatusCode': 'string',
                          'ContentType': 'string'
                      },
                      'ForwardConfig': {
                          'TargetGroups': [
                              {
                                  'TargetGroupArn': 'string',
                                  'Weight': 123
                              },
                          ],
                          'TargetGroupStickinessConfig': {
                              'Enabled': True|False,
                              'DurationSeconds': 123
                          }
                      }
                  },
              ]
          )
        :type RuleArn: string
        :param RuleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the rule.

        :type Conditions: list
        :param Conditions:

          The conditions. Each rule can include zero or one of the following conditions:
          ``http-request-method`` , ``host-header`` , ``path-pattern`` , and ``source-ip`` , and zero or
          more of the following conditions: ``http-header`` and ``query-string`` .

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

        :type Actions: list
        :param Actions:

          The actions. Each rule must include exactly one of the following types of actions: ``forward`` ,
          ``fixed-response`` , or ``redirect`` , and it must be the last action to be performed.

          If the action type is ``forward`` , you specify one or more target groups. The protocol of the
          target group must be HTTP or HTTPS for an Application Load Balancer. The protocol of the target
          group must be TCP, TLS, UDP, or TCP_UDP for a Network Load Balancer.

          [HTTPS listeners] If the action type is ``authenticate-oidc`` , you authenticate users through an
          identity provider that is OpenID Connect (OIDC) compliant.

          [HTTPS listeners] If the action type is ``authenticate-cognito`` , you authenticate users through
          the user pools supported by Amazon Cognito.

          [Application Load Balancer] If the action type is ``redirect`` , you redirect specified client
          requests from one URL to another.

          [Application Load Balancer] If the action type is ``fixed-response`` , you drop specified client
          requests and return a custom HTTP response.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'RuleArn': 'string',
                        'Priority': 'string',
                        'Conditions': [
                            {
                                'Field': 'string',
                                'Values': [
                                    'string',
                                ],
                                'HostHeaderConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'PathPatternConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'HttpHeaderConfig': {
                                    'HttpHeaderName': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'QueryStringConfig': {
                                    'Values': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                                'HttpRequestMethodConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'SourceIpConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            },
                        ],
                        'Actions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ],
                        'IsDefault': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_target_group(
        self,
        TargetGroupArn: str,
        HealthCheckProtocol: str = None,
        HealthCheckPort: str = None,
        HealthCheckPath: str = None,
        HealthCheckEnabled: bool = None,
        HealthCheckIntervalSeconds: int = None,
        HealthCheckTimeoutSeconds: int = None,
        HealthyThresholdCount: int = None,
        UnhealthyThresholdCount: int = None,
        Matcher: ClientModifyTargetGroupMatcherTypeDef = None,
    ) -> ClientModifyTargetGroupResponseTypeDef:
        """
        Modifies the health checks used when evaluating the health state of the targets in the specified
        target group.

        To monitor the health of the targets, use  DescribeTargetHealth .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup>`_

        **Request Syntax**
        ::

          response = client.modify_target_group(
              TargetGroupArn='string',
              HealthCheckProtocol='HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
              HealthCheckPort='string',
              HealthCheckPath='string',
              HealthCheckEnabled=True|False,
              HealthCheckIntervalSeconds=123,
              HealthCheckTimeoutSeconds=123,
              HealthyThresholdCount=123,
              UnhealthyThresholdCount=123,
              Matcher={
                  'HttpCode': 'string'
              }
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :type HealthCheckProtocol: string
        :param HealthCheckProtocol:

          The protocol the load balancer uses when performing health checks on targets. The TCP protocol is
          supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or
          TCP_UDP. The TLS, UDP, and TCP_UDP protocols are not supported for health checks.

          With Network Load Balancers, you can't modify this setting.

        :type HealthCheckPort: string
        :param HealthCheckPort:

          The port the load balancer uses when performing health checks on targets.

        :type HealthCheckPath: string
        :param HealthCheckPath:

          [HTTP/HTTPS health checks] The ping path that is the destination for the health check request.

        :type HealthCheckEnabled: boolean
        :param HealthCheckEnabled:

          Indicates whether health checks are enabled.

        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds:

          The approximate amount of time, in seconds, between health checks of an individual target. For
          Application Load Balancers, the range is 5 to 300 seconds. For Network Load Balancers, the
          supported values are 10 or 30 seconds.

          With Network Load Balancers, you can't modify this setting.

        :type HealthCheckTimeoutSeconds: integer
        :param HealthCheckTimeoutSeconds:

          [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a
          failed health check.

          With Network Load Balancers, you can't modify this setting.

        :type HealthyThresholdCount: integer
        :param HealthyThresholdCount:

          The number of consecutive health checks successes required before considering an unhealthy target
          healthy.

        :type UnhealthyThresholdCount: integer
        :param UnhealthyThresholdCount:

          The number of consecutive health check failures required before considering the target unhealthy.
          For Network Load Balancers, this value must be the same as the healthy threshold count.

        :type Matcher: dict
        :param Matcher:

          [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a
          target.

          With Network Load Balancers, you can't modify this setting.

          - **HttpCode** *(string) --* **[REQUIRED]**

            The HTTP codes.

            For Application Load Balancers, you can specify values between 200 and 499, and the default
            value is 200. You can specify multiple values (for example, "200,202") or a range of values
            (for example, "200-299").

            For Network Load Balancers, this is 200–399.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TargetGroups': [
                    {
                        'TargetGroupArn': 'string',
                        'TargetGroupName': 'string',
                        'Protocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'Port': 123,
                        'VpcId': 'string',
                        'HealthCheckProtocol': 'HTTP'|'HTTPS'|'TCP'|'TLS'|'UDP'|'TCP_UDP',
                        'HealthCheckPort': 'string',
                        'HealthCheckEnabled': True|False,
                        'HealthCheckIntervalSeconds': 123,
                        'HealthCheckTimeoutSeconds': 123,
                        'HealthyThresholdCount': 123,
                        'UnhealthyThresholdCount': 123,
                        'HealthCheckPath': 'string',
                        'Matcher': {
                            'HttpCode': 'string'
                        },
                        'LoadBalancerArns': [
                            'string',
                        ],
                        'TargetType': 'instance'|'ip'|'lambda'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_target_group_attributes(
        self,
        TargetGroupArn: str,
        Attributes: List[ClientModifyTargetGroupAttributesAttributesTypeDef],
    ) -> ClientModifyTargetGroupAttributesResponseTypeDef:
        """
        Modifies the specified attributes of the specified target group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes>`_

        **Request Syntax**
        ::

          response = client.modify_target_group_attributes(
              TargetGroupArn='string',
              Attributes=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :type Attributes: list
        :param Attributes: **[REQUIRED]**

          The attributes.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_targets(
        self, TargetGroupArn: str, Targets: List[ClientRegisterTargetsTargetsTypeDef]
    ) -> Dict[str, Any]:
        """
        Registers the specified targets with the specified target group.

        If the target is an EC2 instance, it must be in the ``running`` state when you register it.

        By default, the load balancer routes requests to registered targets using the protocol and port for
        the target group. Alternatively, you can override the port for a target when you register it. You
        can register each EC2 instance or IP address with the same target group multiple times using
        different ports.

        With a Network Load Balancer, you cannot register instances by instance ID if they have the
        following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1.
        You can register instances of these types by IP address.

        To remove a target from a target group, use  DeregisterTargets .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RegisterTargets>`_

        **Request Syntax**
        ::

          response = client.register_targets(
              TargetGroupArn='string',
              Targets=[
                  {
                      'Id': 'string',
                      'Port': 123,
                      'AvailabilityZone': 'string'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the target group.

        :type Targets: list
        :param Targets: **[REQUIRED]**

          The targets.

          To register a target by instance ID, specify the instance ID. To register a target by IP address,
          specify the IP address. To register a Lambda function, specify the ARN of the Lambda function.

          - *(dict) --*

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_listener_certificates(
        self,
        ListenerArn: str,
        Certificates: List[ClientRemoveListenerCertificatesCertificatesTypeDef],
    ) -> Dict[str, Any]:
        """
        Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.

        You can't remove the default certificate for a listener. To replace the default certificate, call
        ModifyListener .

        To list the certificates for your listener, use  DescribeListenerCertificates .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates>`_

        **Request Syntax**
        ::

          response = client.remove_listener_certificates(
              ListenerArn='string',
              Certificates=[
                  {
                      'CertificateArn': 'string',
                      'IsDefault': True|False
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the listener.

        :type Certificates: list
        :param Certificates: **[REQUIRED]**

          The certificate to remove. You can specify one certificate per call. Set ``CertificateArn`` to
          the certificate ARN but do not set ``IsDefault`` .

          - *(dict) --*

            Information about an SSL server certificate.

            - **CertificateArn** *(string) --*

              The Amazon Resource Name (ARN) of the certificate.

            - **IsDefault** *(boolean) --*

              Indicates whether the certificate is the default certificate. Do not set this value when
              specifying a certificate as an input. This value is not included in the output when
              describing a listener, but is included when describing listener certificates.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags(
        self, ResourceArns: List[str], TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Elastic Load Balancing resource.

        To list the current tags for your resources, use  DescribeTags .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveTags>`_

        **Request Syntax**
        ::

          response = client.remove_tags(
              ResourceArns=[
                  'string',
              ],
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

          - *(string) --*

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The tag keys for the tags to remove.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_ip_address_type(
        self, LoadBalancerArn: str, IpAddressType: str
    ) -> ClientSetIpAddressTypeResponseTypeDef:
        """
        Sets the type of IP addresses used by the subnets of the specified Application Load Balancer or
        Network Load Balancer.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetIpAddressType>`_

        **Request Syntax**
        ::

          response = client.set_ip_address_type(
              LoadBalancerArn='string',
              IpAddressType='ipv4'|'dualstack'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :type IpAddressType: string
        :param IpAddressType: **[REQUIRED]**

          The IP address type. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for
          IPv4 and IPv6 addresses). Internal load balancers must use ``ipv4`` . Network Load Balancers must
          use ``ipv4`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IpAddressType': 'ipv4'|'dualstack'
            }
          **Response Structure**

          - *(dict) --*

            - **IpAddressType** *(string) --*

              The IP address type.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_rule_priorities(
        self, RulePriorities: List[ClientSetRulePrioritiesRulePrioritiesTypeDef]
    ) -> ClientSetRulePrioritiesResponseTypeDef:
        """
        Sets the priorities of the specified rules.

        You can reorder the rules as long as there are no priority conflicts in the new order. Any existing
        rules that you do not specify retain their current priority.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetRulePriorities>`_

        **Request Syntax**
        ::

          response = client.set_rule_priorities(
              RulePriorities=[
                  {
                      'RuleArn': 'string',
                      'Priority': 123
                  },
              ]
          )
        :type RulePriorities: list
        :param RulePriorities: **[REQUIRED]**

          The rule priorities.

          - *(dict) --*

            Information about the priorities for the rules for a listener.

            - **RuleArn** *(string) --*

              The Amazon Resource Name (ARN) of the rule.

            - **Priority** *(integer) --*

              The rule priority.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Rules': [
                    {
                        'RuleArn': 'string',
                        'Priority': 'string',
                        'Conditions': [
                            {
                                'Field': 'string',
                                'Values': [
                                    'string',
                                ],
                                'HostHeaderConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'PathPatternConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'HttpHeaderConfig': {
                                    'HttpHeaderName': 'string',
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'QueryStringConfig': {
                                    'Values': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                                'HttpRequestMethodConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                },
                                'SourceIpConfig': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            },
                        ],
                        'Actions': [
                            {
                                'Type':
                                'forward'|'authenticate-oidc'|'authenticate-cognito'|'redirect'
                                |'fixed-response',
                                'TargetGroupArn': 'string',
                                'AuthenticateOidcConfig': {
                                    'Issuer': 'string',
                                    'AuthorizationEndpoint': 'string',
                                    'TokenEndpoint': 'string',
                                    'UserInfoEndpoint': 'string',
                                    'ClientId': 'string',
                                    'ClientSecret': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate',
                                    'UseExistingClientSecret': True|False
                                },
                                'AuthenticateCognitoConfig': {
                                    'UserPoolArn': 'string',
                                    'UserPoolClientId': 'string',
                                    'UserPoolDomain': 'string',
                                    'SessionCookieName': 'string',
                                    'Scope': 'string',
                                    'SessionTimeout': 123,
                                    'AuthenticationRequestExtraParams': {
                                        'string': 'string'
                                    },
                                    'OnUnauthenticatedRequest': 'deny'|'allow'|'authenticate'
                                },
                                'Order': 123,
                                'RedirectConfig': {
                                    'Protocol': 'string',
                                    'Port': 'string',
                                    'Host': 'string',
                                    'Path': 'string',
                                    'Query': 'string',
                                    'StatusCode': 'HTTP_301'|'HTTP_302'
                                },
                                'FixedResponseConfig': {
                                    'MessageBody': 'string',
                                    'StatusCode': 'string',
                                    'ContentType': 'string'
                                },
                                'ForwardConfig': {
                                    'TargetGroups': [
                                        {
                                            'TargetGroupArn': 'string',
                                            'Weight': 123
                                        },
                                    ],
                                    'TargetGroupStickinessConfig': {
                                        'Enabled': True|False,
                                        'DurationSeconds': 123
                                    }
                                }
                            },
                        ],
                        'IsDefault': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_security_groups(
        self, LoadBalancerArn: str, SecurityGroups: List[str]
    ) -> ClientSetSecurityGroupsResponseTypeDef:
        """
        Associates the specified security groups with the specified Application Load Balancer. The
        specified security groups override the previously associated security groups.

        You can't specify a security group for a Network Load Balancer.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSecurityGroups>`_

        **Request Syntax**
        ::

          response = client.set_security_groups(
              LoadBalancerArn='string',
              SecurityGroups=[
                  'string',
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :type SecurityGroups: list
        :param SecurityGroups: **[REQUIRED]**

          The IDs of the security groups.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SecurityGroupIds': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **SecurityGroupIds** *(list) --*

              The IDs of the security groups associated with the load balancer.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_subnets(
        self,
        LoadBalancerArn: str,
        Subnets: List[str] = None,
        SubnetMappings: List[ClientSetSubnetsSubnetMappingsTypeDef] = None,
    ) -> ClientSetSubnetsResponseTypeDef:
        """
        Enables the Availability Zone for the specified public subnets for the specified Application Load
        Balancer. The specified subnets replace the previously enabled subnets.

        You can't change the subnets for a Network Load Balancer.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSubnets>`_

        **Request Syntax**
        ::

          response = client.set_subnets(
              LoadBalancerArn='string',
              Subnets=[
                  'string',
              ],
              SubnetMappings=[
                  {
                      'SubnetId': 'string',
                      'AllocationId': 'string'
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the load balancer.

        :type Subnets: list
        :param Subnets:

          The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You
          can specify only one subnet per Availability Zone. You must specify either subnets or subnet
          mappings.

          - *(string) --*

        :type SubnetMappings: list
        :param SubnetMappings:

          The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You
          can specify only one subnet per Availability Zone. You must specify either subnets or subnet
          mappings.

          You cannot specify Elastic IP addresses for your subnets.

          - *(dict) --*

            Information about a subnet mapping.

            - **SubnetId** *(string) --*

              The ID of the subnet.

            - **AllocationId** *(string) --*

              [Network Load Balancers] The allocation ID of the Elastic IP address.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AvailabilityZones': [
                    {
                        'ZoneName': 'string',
                        'SubnetId': 'string',
                        'LoadBalancerAddresses': [
                            {
                                'IpAddress': 'string',
                                'AllocationId': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> paginator_scope.DescribeAccountLimitsPaginator:
        """
        Get Paginator for `describe_account_limits` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_listener_certificates"]
    ) -> paginator_scope.DescribeListenerCertificatesPaginator:
        """
        Get Paginator for `describe_listener_certificates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_listeners"]
    ) -> paginator_scope.DescribeListenersPaginator:
        """
        Get Paginator for `describe_listeners` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_load_balancers"]
    ) -> paginator_scope.DescribeLoadBalancersPaginator:
        """
        Get Paginator for `describe_load_balancers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_rules"]
    ) -> paginator_scope.DescribeRulesPaginator:
        """
        Get Paginator for `describe_rules` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_ssl_policies"]
    ) -> paginator_scope.DescribeSSLPoliciesPaginator:
        """
        Get Paginator for `describe_ssl_policies` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_target_groups"]
    ) -> paginator_scope.DescribeTargetGroupsPaginator:
        """
        Get Paginator for `describe_target_groups` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancer_available"]
    ) -> waiter_scope.LoadBalancerAvailableWaiter:
        """
        Get Waiter `load_balancer_available`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancer_exists"]
    ) -> waiter_scope.LoadBalancerExistsWaiter:
        """
        Get Waiter `load_balancer_exists`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["load_balancers_deleted"]
    ) -> waiter_scope.LoadBalancersDeletedWaiter:
        """
        Get Waiter `load_balancers_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["target_deregistered"]
    ) -> waiter_scope.TargetDeregisteredWaiter:
        """
        Get Waiter `target_deregistered`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["target_in_service"]
    ) -> waiter_scope.TargetInServiceWaiter:
        """
        Get Waiter `target_in_service`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    AllocationIdNotFoundException: Boto3ClientError
    AvailabilityZoneNotSupportedException: Boto3ClientError
    CertificateNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    DuplicateListenerException: Boto3ClientError
    DuplicateLoadBalancerNameException: Boto3ClientError
    DuplicateTagKeysException: Boto3ClientError
    DuplicateTargetGroupNameException: Boto3ClientError
    HealthUnavailableException: Boto3ClientError
    IncompatibleProtocolsException: Boto3ClientError
    InvalidConfigurationRequestException: Boto3ClientError
    InvalidLoadBalancerActionException: Boto3ClientError
    InvalidSchemeException: Boto3ClientError
    InvalidSecurityGroupException: Boto3ClientError
    InvalidSubnetException: Boto3ClientError
    InvalidTargetException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
    LoadBalancerNotFoundException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    PriorityInUseException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    RuleNotFoundException: Boto3ClientError
    SSLPolicyNotFoundException: Boto3ClientError
    SubnetNotFoundException: Boto3ClientError
    TargetGroupAssociationLimitException: Boto3ClientError
    TargetGroupNotFoundException: Boto3ClientError
    TooManyActionsException: Boto3ClientError
    TooManyCertificatesException: Boto3ClientError
    TooManyListenersException: Boto3ClientError
    TooManyLoadBalancersException: Boto3ClientError
    TooManyRegistrationsForTargetIdException: Boto3ClientError
    TooManyRulesException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
    TooManyTargetGroupsException: Boto3ClientError
    TooManyTargetsException: Boto3ClientError
    TooManyUniqueTargetGroupsPerLoadBalancerException: Boto3ClientError
    UnsupportedProtocolException: Boto3ClientError
