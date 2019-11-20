"Main interface for elbv2 Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elbv2.type_defs import (
    DescribeAccountLimitsPaginatePaginationConfigTypeDef,
    DescribeAccountLimitsPaginateResponseTypeDef,
    DescribeListenerCertificatesPaginatePaginationConfigTypeDef,
    DescribeListenerCertificatesPaginateResponseTypeDef,
    DescribeListenersPaginatePaginationConfigTypeDef,
    DescribeListenersPaginateResponseTypeDef,
    DescribeLoadBalancersPaginatePaginationConfigTypeDef,
    DescribeLoadBalancersPaginateResponseTypeDef,
    DescribeRulesPaginatePaginationConfigTypeDef,
    DescribeRulesPaginateResponseTypeDef,
    DescribeSSLPoliciesPaginatePaginationConfigTypeDef,
    DescribeSSLPoliciesPaginateResponseTypeDef,
    DescribeTargetGroupsPaginatePaginationConfigTypeDef,
    DescribeTargetGroupsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    Paginator for `describe_account_limits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribeAccountLimitsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAccountLimitsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_account_limits`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeListenerCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_listener_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: DescribeListenerCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeListenerCertificatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_listener_certificates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ListenerArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**

          The Amazon Resource Names (ARN) of the listener.

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeListenersPaginator(Boto3Paginator):
    """
    Paginator for `describe_listeners`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        PaginationConfig: DescribeListenersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeListenersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_listeners`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LoadBalancerArn='string',
              ListenerArns=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn:

          The Amazon Resource Name (ARN) of the load balancer.

        :type ListenerArns: list
        :param ListenerArns:

          The Amazon Resource Names (ARN) of the listeners.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    Paginator for `describe_load_balancers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: DescribeLoadBalancersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLoadBalancersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_load_balancers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LoadBalancerArns=[
                  'string',
              ],
              Names=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        PaginationConfig: DescribeRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRulesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_rules`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeRules>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ListenerArn='string',
              RuleArns=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ListenerArn: string
        :param ListenerArn:

          The Amazon Resource Name (ARN) of the listener.

        :type RuleArns: list
        :param RuleArns:

          The Amazon Resource Names (ARN) of the rules.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeSSLPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `describe_ssl_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeSSLPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSSLPoliciesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_ssl_policies`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Names=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Names: list
        :param Names:

          The names of the policies.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class DescribeTargetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_target_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: DescribeTargetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTargetGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ElasticLoadBalancingv2.Client.describe_target_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              LoadBalancerArn='string',
              TargetGroupArns=[
                  'string',
              ],
              Names=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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

        :type PaginationConfig: dict
        :param PaginationConfig:

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
                'NextToken': 'string'
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

            - **NextToken** *(string) --*

              A token to resume pagination.

        """
