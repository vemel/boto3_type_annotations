"Main interface for elb type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "AnyInstanceInServiceWaitInstancesTypeDef",
    "AnyInstanceInServiceWaitWaiterConfigTypeDef",
    "ClientAddTagsTagsTypeDef",
    "ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    "ClientAttachLoadBalancerToSubnetsResponseTypeDef",
    "ClientConfigureHealthCheckHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    "ClientConfigureHealthCheckResponseTypeDef",
    "ClientCreateLoadBalancerListenersListenersTypeDef",
    "ClientCreateLoadBalancerListenersTypeDef",
    "ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    "ClientCreateLoadBalancerResponseTypeDef",
    "ClientCreateLoadBalancerTagsTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    "ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    "ClientDescribeAccountLimitsResponseLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeInstanceHealthInstancesTypeDef",
    "ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    "ClientDescribeInstanceHealthResponseTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientDescribeLoadBalancerAttributesResponseTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    "ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    "ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    "ClientDescribeLoadBalancersResponseTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTagsTypeDef",
    "ClientDescribeTagsResponseTagDescriptionsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDetachLoadBalancerFromSubnetsResponseTypeDef",
    "ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    "ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    "ClientModifyLoadBalancerAttributesResponseTypeDef",
    "ClientRegisterInstancesWithLoadBalancerInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    "ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    "ClientRemoveTagsTagsTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeLoadBalancersPaginatePaginationConfigTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    "DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef",
    "DescribeLoadBalancersPaginateResponseTypeDef",
    "InstanceDeregisteredWaitInstancesTypeDef",
    "InstanceDeregisteredWaitWaiterConfigTypeDef",
    "InstanceInServiceWaitInstancesTypeDef",
    "InstanceInServiceWaitWaiterConfigTypeDef",
)


_AnyInstanceInServiceWaitInstancesTypeDef = TypedDict(
    "_AnyInstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class AnyInstanceInServiceWaitInstancesTypeDef(
    _AnyInstanceInServiceWaitInstancesTypeDef
):
    """
    Type definition for `AnyInstanceInServiceWait` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_AnyInstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_AnyInstanceInServiceWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class AnyInstanceInServiceWaitWaiterConfigTypeDef(
    _AnyInstanceInServiceWaitWaiterConfigTypeDef
):
    """
    Type definition for `AnyInstanceInServiceWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
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


_ClientApplySecurityGroupsToLoadBalancerResponseTypeDef = TypedDict(
    "_ClientApplySecurityGroupsToLoadBalancerResponseTypeDef",
    {"SecurityGroups": List[str]},
    total=False,
)


class ClientApplySecurityGroupsToLoadBalancerResponseTypeDef(
    _ClientApplySecurityGroupsToLoadBalancerResponseTypeDef
):
    """
    Type definition for `ClientApplySecurityGroupsToLoadBalancer` `Response`

    Contains the output of ApplySecurityGroupsToLoadBalancer.

    - **SecurityGroups** *(list) --*

      The IDs of the security groups associated with the load balancer.

      - *(string) --*
    """


_ClientAttachLoadBalancerToSubnetsResponseTypeDef = TypedDict(
    "_ClientAttachLoadBalancerToSubnetsResponseTypeDef",
    {"Subnets": List[str]},
    total=False,
)


class ClientAttachLoadBalancerToSubnetsResponseTypeDef(
    _ClientAttachLoadBalancerToSubnetsResponseTypeDef
):
    """
    Type definition for `ClientAttachLoadBalancerToSubnets` `Response`

    Contains the output of AttachLoadBalancerToSubnets.

    - **Subnets** *(list) --*

      The IDs of the subnets attached to the load balancer.

      - *(string) --*
    """


_ClientConfigureHealthCheckHealthCheckTypeDef = TypedDict(
    "_ClientConfigureHealthCheckHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)


class ClientConfigureHealthCheckHealthCheckTypeDef(
    _ClientConfigureHealthCheckHealthCheckTypeDef
):
    """
    Type definition for `ClientConfigureHealthCheck` `HealthCheck`

    The configuration information.

    - **Target** *(string) --* **[REQUIRED]**

      The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid
      ports is one (1) through 65535.

      TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
      health check simply attempts to open a TCP connection to the instance on the specified port.
      Failure to connect within the configured timeout is considered unhealthy.

      SSL is also specified as SSL: port pair, for example, SSL:5000.

      For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
      HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this case, a
      HTTP GET request is issued to the instance on the given port and path. Any answer other than
      "200 OK" within the timeout period is considered unhealthy.

      The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

    - **Interval** *(integer) --* **[REQUIRED]**

      The approximate interval, in seconds, between health checks of an individual instance.

    - **Timeout** *(integer) --* **[REQUIRED]**

      The amount of time, in seconds, during which no response means a failed health check.

      This value must be less than the ``Interval`` value.

    - **UnhealthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive health check failures required before moving the instance to the
      ``Unhealthy`` state.

    - **HealthyThreshold** *(integer) --* **[REQUIRED]**

      The number of consecutive health checks successes required before moving the instance to the
      ``Healthy`` state.
    """


_ClientConfigureHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientConfigureHealthCheckResponseHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class ClientConfigureHealthCheckResponseHealthCheckTypeDef(
    _ClientConfigureHealthCheckResponseHealthCheckTypeDef
):
    """
    Type definition for `ClientConfigureHealthCheckResponse` `HealthCheck`

    The updated health check.

    - **Target** *(string) --*

      The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of
      valid ports is one (1) through 65535.

      TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
      health check simply attempts to open a TCP connection to the instance on the specified
      port. Failure to connect within the configured timeout is considered unhealthy.

      SSL is also specified as SSL: port pair, for example, SSL:5000.

      For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
      HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
      case, a HTTP GET request is issued to the instance on the given port and path. Any answer
      other than "200 OK" within the timeout period is considered unhealthy.

      The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

    - **Interval** *(integer) --*

      The approximate interval, in seconds, between health checks of an individual instance.

    - **Timeout** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

      This value must be less than the ``Interval`` value.

    - **UnhealthyThreshold** *(integer) --*

      The number of consecutive health check failures required before moving the instance to the
      ``Unhealthy`` state.

    - **HealthyThreshold** *(integer) --*

      The number of consecutive health checks successes required before moving the instance to
      the ``Healthy`` state.
    """


_ClientConfigureHealthCheckResponseTypeDef = TypedDict(
    "_ClientConfigureHealthCheckResponseTypeDef",
    {"HealthCheck": ClientConfigureHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientConfigureHealthCheckResponseTypeDef(
    _ClientConfigureHealthCheckResponseTypeDef
):
    """
    Type definition for `ClientConfigureHealthCheck` `Response`

    Contains the output of ConfigureHealthCheck.

    - **HealthCheck** *(dict) --*

      The updated health check.

      - **Target** *(string) --*

        The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of
        valid ports is one (1) through 65535.

        TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this case, a
        health check simply attempts to open a TCP connection to the instance on the specified
        port. Failure to connect within the configured timeout is considered unhealthy.

        SSL is also specified as SSL: port pair, for example, SSL:5000.

        For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
        HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
        case, a HTTP GET request is issued to the instance on the given port and path. Any answer
        other than "200 OK" within the timeout period is considered unhealthy.

        The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

      - **Interval** *(integer) --*

        The approximate interval, in seconds, between health checks of an individual instance.

      - **Timeout** *(integer) --*

        The amount of time, in seconds, during which no response means a failed health check.

        This value must be less than the ``Interval`` value.

      - **UnhealthyThreshold** *(integer) --*

        The number of consecutive health check failures required before moving the instance to the
        ``Unhealthy`` state.

      - **HealthyThreshold** *(integer) --*

        The number of consecutive health checks successes required before moving the instance to
        the ``Healthy`` state.
    """


_RequiredClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersListenersTypeDef",
    {"Protocol": str, "LoadBalancerPort": int, "InstancePort": int},
)
_OptionalClientCreateLoadBalancerListenersListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersListenersTypeDef",
    {"InstanceProtocol": str, "SSLCertificateId": str},
    total=False,
)


class ClientCreateLoadBalancerListenersListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersListenersTypeDef,
):
    """
    Type definition for `ClientCreateLoadBalancerListeners` `Listeners`

    Information about a listener.

    For information about the protocols and the ports supported by Elastic Load Balancing, see
    `Listeners for Your Classic Load Balancer
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in
    the *Classic Load Balancers Guide* .

    - **Protocol** *(string) --* **[REQUIRED]**

      The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

    - **LoadBalancerPort** *(integer) --* **[REQUIRED]**

      The port on which the load balancer is listening. On EC2-VPC, you can specify any port from
      the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80,
      443, 465, 587, 1024-65535.

    - **InstanceProtocol** *(string) --*

      The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

      If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be at the
      same protocol.

      If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is
      secure, (HTTPS or SSL), the listener's ``InstanceProtocol`` must also be secure.

      If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is
      HTTP or TCP, the listener's ``InstanceProtocol`` must be HTTP or TCP.

    - **InstancePort** *(integer) --* **[REQUIRED]**

      The port on which the instance is listening.

    - **SSLCertificateId** *(string) --*

      The Amazon Resource Name (ARN) of the server certificate.
    """


_RequiredClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_RequiredClientCreateLoadBalancerListenersTypeDef",
    {"Protocol": str, "LoadBalancerPort": int, "InstancePort": int},
)
_OptionalClientCreateLoadBalancerListenersTypeDef = TypedDict(
    "_OptionalClientCreateLoadBalancerListenersTypeDef",
    {"InstanceProtocol": str, "SSLCertificateId": str},
    total=False,
)


class ClientCreateLoadBalancerListenersTypeDef(
    _RequiredClientCreateLoadBalancerListenersTypeDef,
    _OptionalClientCreateLoadBalancerListenersTypeDef,
):
    """
    Type definition for `ClientCreateLoadBalancer` `Listeners`

    Information about a listener.

    For information about the protocols and the ports supported by Elastic Load Balancing, see
    `Listeners for Your Classic Load Balancer
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in
    the *Classic Load Balancers Guide* .

    - **Protocol** *(string) --* **[REQUIRED]**

      The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

    - **LoadBalancerPort** *(integer) --* **[REQUIRED]**

      The port on which the load balancer is listening. On EC2-VPC, you can specify any port from
      the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80,
      443, 465, 587, 1024-65535.

    - **InstanceProtocol** *(string) --*

      The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

      If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be at the
      same protocol.

      If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is
      secure, (HTTPS or SSL), the listener's ``InstanceProtocol`` must also be secure.

      If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is
      HTTP or TCP, the listener's ``InstanceProtocol`` must be HTTP or TCP.

    - **InstancePort** *(integer) --* **[REQUIRED]**

      The port on which the instance is listening.

    - **SSLCertificateId** *(string) --*

      The Amazon Resource Name (ARN) of the server certificate.
    """


_ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef = TypedDict(
    "_ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)


class ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef(
    _ClientCreateLoadBalancerPolicyPolicyAttributesTypeDef
):
    """
    Type definition for `ClientCreateLoadBalancerPolicy` `PolicyAttributes`

    Information about a policy attribute.

    - **AttributeName** *(string) --*

      The name of the attribute.

    - **AttributeValue** *(string) --*

      The value of the attribute.
    """


_ClientCreateLoadBalancerResponseTypeDef = TypedDict(
    "_ClientCreateLoadBalancerResponseTypeDef", {"DNSName": str}, total=False
)


class ClientCreateLoadBalancerResponseTypeDef(_ClientCreateLoadBalancerResponseTypeDef):
    """
    Type definition for `ClientCreateLoadBalancer` `Response`

    Contains the output for CreateLoadBalancer.

    - **DNSName** *(string) --*

      The DNS name of the load balancer.
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


_ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerInstancesTypeDef
):
    """
    Type definition for `ClientDeregisterInstancesFromLoadBalancer` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef
):
    """
    Type definition for `ClientDeregisterInstancesFromLoadBalancerResponse` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientDeregisterInstancesFromLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDeregisterInstancesFromLoadBalancerResponseTypeDef",
    {
        "Instances": List[
            ClientDeregisterInstancesFromLoadBalancerResponseInstancesTypeDef
        ]
    },
    total=False,
)


class ClientDeregisterInstancesFromLoadBalancerResponseTypeDef(
    _ClientDeregisterInstancesFromLoadBalancerResponseTypeDef
):
    """
    Type definition for `ClientDeregisterInstancesFromLoadBalancer` `Response`

    Contains the output of DeregisterInstancesFromLoadBalancer.

    - **Instances** *(list) --*

      The remaining instances registered with the load balancer.

      - *(dict) --*

        The ID of an EC2 instance.

        - **InstanceId** *(string) --*

          The instance ID.
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

      * classic-listeners

      * classic-load-balancers

      * classic-registered-instances

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

          * classic-listeners

          * classic-load-balancers

          * classic-registered-instances

        - **Max** *(string) --*

          The maximum value of the limit.

    - **NextMarker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
    """


_ClientDescribeInstanceHealthInstancesTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthInstancesTypeDef", {"InstanceId": str}, total=False
)


class ClientDescribeInstanceHealthInstancesTypeDef(
    _ClientDescribeInstanceHealthInstancesTypeDef
):
    """
    Type definition for `ClientDescribeInstanceHealth` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientDescribeInstanceHealthResponseInstanceStatesTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthResponseInstanceStatesTypeDef",
    {"InstanceId": str, "State": str, "ReasonCode": str, "Description": str},
    total=False,
)


class ClientDescribeInstanceHealthResponseInstanceStatesTypeDef(
    _ClientDescribeInstanceHealthResponseInstanceStatesTypeDef
):
    """
    Type definition for `ClientDescribeInstanceHealthResponse` `InstanceStates`

    Information about the state of an EC2 instance.

    - **InstanceId** *(string) --*

      The ID of the instance.

    - **State** *(string) --*

      The current state of the instance.

      Valid values: ``InService`` | ``OutOfService`` | ``Unknown``

    - **ReasonCode** *(string) --*

      Information about the cause of ``OutOfService`` instances. Specifically, whether the
      cause is Elastic Load Balancing or the instance.

      Valid values: ``ELB`` | ``Instance`` | ``N/A``

    - **Description** *(string) --*

      A description of the instance state. This string can contain one or more of the following
      messages.

      * ``N/A``

      * ``A transient error occurred. Please try again later.``

      * ``Instance has failed at least the UnhealthyThreshold number of health checks
      consecutively.``

      * ``Instance has not passed the configured HealthyThreshold number of health checks
      consecutively.``

      * ``Instance registration is still in progress.``

      * ``Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to
      route traffic to.``

      * ``Instance is not currently registered with the LoadBalancer.``

      * ``Instance deregistration currently in progress.``

      * ``Disable Availability Zone is currently in progress.``

      * ``Instance is in pending state.``

      * ``Instance is in stopped state.``

      * ``Instance is in terminated state.``
    """


_ClientDescribeInstanceHealthResponseTypeDef = TypedDict(
    "_ClientDescribeInstanceHealthResponseTypeDef",
    {"InstanceStates": List[ClientDescribeInstanceHealthResponseInstanceStatesTypeDef]},
    total=False,
)


class ClientDescribeInstanceHealthResponseTypeDef(
    _ClientDescribeInstanceHealthResponseTypeDef
):
    """
    Type definition for `ClientDescribeInstanceHealth` `Response`

    Contains the output for DescribeInstanceHealth.

    - **InstanceStates** *(list) --*

      Information about the health of the instances.

      - *(dict) --*

        Information about the state of an EC2 instance.

        - **InstanceId** *(string) --*

          The ID of the instance.

        - **State** *(string) --*

          The current state of the instance.

          Valid values: ``InService`` | ``OutOfService`` | ``Unknown``

        - **ReasonCode** *(string) --*

          Information about the cause of ``OutOfService`` instances. Specifically, whether the
          cause is Elastic Load Balancing or the instance.

          Valid values: ``ELB`` | ``Instance`` | ``N/A``

        - **Description** *(string) --*

          A description of the instance state. This string can contain one or more of the following
          messages.

          * ``N/A``

          * ``A transient error occurred. Please try again later.``

          * ``Instance has failed at least the UnhealthyThreshold number of health checks
          consecutively.``

          * ``Instance has not passed the configured HealthyThreshold number of health checks
          consecutively.``

          * ``Instance registration is still in progress.``

          * ``Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to
          route traffic to.``

          * ``Instance is not currently registered with the LoadBalancer.``

          * ``Instance deregistration currently in progress.``

          * ``Disable Availability Zone is currently in progress.``

          * ``Instance is in pending state.``

          * ``Instance is in stopped state.``

          * ``Instance is in terminated state.``
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributes` `AccessLog`

    If enabled, the load balancer captures detailed information of all requests and delivers
    the information to the Amazon S3 bucket that you specify.

    For more information, see `Enable Access Logs
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether access logs are enabled for the load balancer.

    - **S3BucketName** *(string) --*

      The name of the Amazon S3 bucket where the access logs are stored.

    - **EmitInterval** *(integer) --*

      The interval for publishing the access logs. You can specify an interval of either 5
      minutes or 60 minutes.

      Default: 60 minutes

    - **S3BucketPrefix** *(string) --*

      The logical hierarchy you created for your Amazon S3 bucket, for example
      ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
      level of the bucket.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributes` `AdditionalAttributes`

    This data type is reserved.

    - **Key** *(string) --*

      This parameter is reserved.

    - **Value** *(string) --*

      This parameter is reserved.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributes` `ConnectionDraining`

    If enabled, the load balancer allows existing requests to complete before the load balancer
    shifts traffic away from a deregistered or unhealthy instance.

    For more information, see `Configure Connection Draining
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether connection draining is enabled for the load balancer.

    - **Timeout** *(integer) --*

      The maximum time, in seconds, to keep the existing connections open before deregistering
      the instances.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributes` `ConnectionSettings`

    If enabled, the load balancer allows the connections to remain idle (no data is sent over
    the connection) for the specified duration.

    By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
    front-end and back-end connections of your load balancer. For more information, see
    `Configure Idle Connection Timeout
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
    in the *Classic Load Balancers Guide* .

    - **IdleTimeout** *(integer) --*

      The time, in seconds, that the connection is allowed to be idle (no data has been sent
      over the connection) before it is closed by the load balancer.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributes` `CrossZoneLoadBalancing`

    If enabled, the load balancer routes the request traffic evenly across all instances
    regardless of the Availability Zones.

    For more information, see `Configure Cross-Zone Load Balancing
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributesResponse` `LoadBalancerAttributes`

    Information about the load balancer attributes.

    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances
      regardless of the Availability Zones.

      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether cross-zone load balancing is enabled for the load balancer.

    - **AccessLog** *(dict) --*

      If enabled, the load balancer captures detailed information of all requests and delivers
      the information to the Amazon S3 bucket that you specify.

      For more information, see `Enable Access Logs
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether access logs are enabled for the load balancer.

      - **S3BucketName** *(string) --*

        The name of the Amazon S3 bucket where the access logs are stored.

      - **EmitInterval** *(integer) --*

        The interval for publishing the access logs. You can specify an interval of either 5
        minutes or 60 minutes.

        Default: 60 minutes

      - **S3BucketPrefix** *(string) --*

        The logical hierarchy you created for your Amazon S3 bucket, for example
        ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
        level of the bucket.

    - **ConnectionDraining** *(dict) --*

      If enabled, the load balancer allows existing requests to complete before the load balancer
      shifts traffic away from a deregistered or unhealthy instance.

      For more information, see `Configure Connection Draining
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether connection draining is enabled for the load balancer.

      - **Timeout** *(integer) --*

        The maximum time, in seconds, to keep the existing connections open before deregistering
        the instances.

    - **ConnectionSettings** *(dict) --*

      If enabled, the load balancer allows the connections to remain idle (no data is sent over
      the connection) for the specified duration.

      By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
      front-end and back-end connections of your load balancer. For more information, see
      `Configure Idle Connection Timeout
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
      in the *Classic Load Balancers Guide* .

      - **IdleTimeout** *(integer) --*

        The time, in seconds, that the connection is allowed to be idle (no data has been sent
        over the connection) before it is closed by the load balancer.

    - **AdditionalAttributes** *(list) --*

      This parameter is reserved.

      - *(dict) --*

        This data type is reserved.

        - **Key** *(string) --*

          This parameter is reserved.

        - **Value** *(string) --*

          This parameter is reserved.
    """


_ClientDescribeLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerAttributes": ClientDescribeLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
    },
    total=False,
)


class ClientDescribeLoadBalancerAttributesResponseTypeDef(
    _ClientDescribeLoadBalancerAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerAttributes` `Response`

    Contains the output of DescribeLoadBalancerAttributes.

    - **LoadBalancerAttributes** *(dict) --*

      Information about the load balancer attributes.

      - **CrossZoneLoadBalancing** *(dict) --*

        If enabled, the load balancer routes the request traffic evenly across all instances
        regardless of the Availability Zones.

        For more information, see `Configure Cross-Zone Load Balancing
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether cross-zone load balancing is enabled for the load balancer.

      - **AccessLog** *(dict) --*

        If enabled, the load balancer captures detailed information of all requests and delivers
        the information to the Amazon S3 bucket that you specify.

        For more information, see `Enable Access Logs
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether access logs are enabled for the load balancer.

        - **S3BucketName** *(string) --*

          The name of the Amazon S3 bucket where the access logs are stored.

        - **EmitInterval** *(integer) --*

          The interval for publishing the access logs. You can specify an interval of either 5
          minutes or 60 minutes.

          Default: 60 minutes

        - **S3BucketPrefix** *(string) --*

          The logical hierarchy you created for your Amazon S3 bucket, for example
          ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
          level of the bucket.

      - **ConnectionDraining** *(dict) --*

        If enabled, the load balancer allows existing requests to complete before the load balancer
        shifts traffic away from a deregistered or unhealthy instance.

        For more information, see `Configure Connection Draining
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether connection draining is enabled for the load balancer.

        - **Timeout** *(integer) --*

          The maximum time, in seconds, to keep the existing connections open before deregistering
          the instances.

      - **ConnectionSettings** *(dict) --*

        If enabled, the load balancer allows the connections to remain idle (no data is sent over
        the connection) for the specified duration.

        By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
        front-end and back-end connections of your load balancer. For more information, see
        `Configure Idle Connection Timeout
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
        in the *Classic Load Balancers Guide* .

        - **IdleTimeout** *(integer) --*

          The time, in seconds, that the connection is allowed to be idle (no data has been sent
          over the connection) before it is closed by the load balancer.

      - **AdditionalAttributes** *(list) --*

        This parameter is reserved.

        - *(dict) --*

          This data type is reserved.

          - **Key** *(string) --*

            This parameter is reserved.

          - **Value** *(string) --*

            This parameter is reserved.
    """


_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef",
    {"AttributeName": str, "AttributeValue": str},
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptions` `PolicyAttributeDescriptions`

    Information about a policy attribute.

    - **AttributeName** *(string) --*

      The name of the attribute.

    - **AttributeValue** *(string) --*

      The value of the attribute.
    """


_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsPolicyAttributeDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPoliciesResponse` `PolicyDescriptions`

    Information about a policy.

    - **PolicyName** *(string) --*

      The name of the policy.

    - **PolicyTypeName** *(string) --*

      The name of the policy type.

    - **PolicyAttributeDescriptions** *(list) --*

      The policy attributes.

      - *(dict) --*

        Information about a policy attribute.

        - **AttributeName** *(string) --*

          The name of the attribute.

        - **AttributeValue** *(string) --*

          The value of the attribute.
    """


_ClientDescribeLoadBalancerPoliciesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPoliciesResponseTypeDef",
    {
        "PolicyDescriptions": List[
            ClientDescribeLoadBalancerPoliciesResponsePolicyDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBalancerPoliciesResponseTypeDef(
    _ClientDescribeLoadBalancerPoliciesResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPolicies` `Response`

    Contains the output of DescribeLoadBalancerPolicies.

    - **PolicyDescriptions** *(list) --*

      Information about the policies.

      - *(dict) --*

        Information about a policy.

        - **PolicyName** *(string) --*

          The name of the policy.

        - **PolicyTypeName** *(string) --*

          The name of the policy type.

        - **PolicyAttributeDescriptions** *(list) --*

          The policy attributes.

          - *(dict) --*

            Information about a policy attribute.

            - **AttributeName** *(string) --*

              The name of the attribute.

            - **AttributeValue** *(string) --*

              The value of the attribute.
    """


_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptions` `PolicyAttributeTypeDescriptions`

    Information about a policy attribute type.

    - **AttributeName** *(string) --*

      The name of the attribute.

    - **AttributeType** *(string) --*

      The type of the attribute. For example, ``Boolean`` or ``Integer`` .

    - **Description** *(string) --*

      A description of the attribute.

    - **DefaultValue** *(string) --*

      The default value of the attribute, if applicable.

    - **Cardinality** *(string) --*

      The cardinality of the attribute.

      Valid values:

      * ONE(1) : Single value required

      * ZERO_OR_ONE(0..1) : Up to one value is allowed

      * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed

      * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    """


_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsPolicyAttributeTypeDescriptionsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPolicyTypesResponse` `PolicyTypeDescriptions`

    Information about a policy type.

    - **PolicyTypeName** *(string) --*

      The name of the policy type.

    - **Description** *(string) --*

      A description of the policy type.

    - **PolicyAttributeTypeDescriptions** *(list) --*

      The description of the policy attributes associated with the policies defined by Elastic
      Load Balancing.

      - *(dict) --*

        Information about a policy attribute type.

        - **AttributeName** *(string) --*

          The name of the attribute.

        - **AttributeType** *(string) --*

          The type of the attribute. For example, ``Boolean`` or ``Integer`` .

        - **Description** *(string) --*

          A description of the attribute.

        - **DefaultValue** *(string) --*

          The default value of the attribute, if applicable.

        - **Cardinality** *(string) --*

          The cardinality of the attribute.

          Valid values:

          * ONE(1) : Single value required

          * ZERO_OR_ONE(0..1) : Up to one value is allowed

          * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed

          * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    """


_ClientDescribeLoadBalancerPolicyTypesResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancerPolicyTypesResponseTypeDef",
    {
        "PolicyTypeDescriptions": List[
            ClientDescribeLoadBalancerPolicyTypesResponsePolicyTypeDescriptionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeLoadBalancerPolicyTypesResponseTypeDef(
    _ClientDescribeLoadBalancerPolicyTypesResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancerPolicyTypes` `Response`

    Contains the output of DescribeLoadBalancerPolicyTypes.

    - **PolicyTypeDescriptions** *(list) --*

      Information about the policy types.

      - *(dict) --*

        Information about a policy type.

        - **PolicyTypeName** *(string) --*

          The name of the policy type.

        - **Description** *(string) --*

          A description of the policy type.

        - **PolicyAttributeTypeDescriptions** *(list) --*

          The description of the policy attributes associated with the policies defined by Elastic
          Load Balancing.

          - *(dict) --*

            Information about a policy attribute type.

            - **AttributeName** *(string) --*

              The name of the attribute.

            - **AttributeType** *(string) --*

              The type of the attribute. For example, ``Boolean`` or ``Integer`` .

            - **Description** *(string) --*

              A description of the attribute.

            - **DefaultValue** *(string) --*

              The default value of the attribute, if applicable.

            - **Cardinality** *(string) --*

              The cardinality of the attribute.

              Valid values:

              * ONE(1) : Single value required

              * ZERO_OR_ONE(0..1) : Up to one value is allowed

              * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed

              * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `BackendServerDescriptions`

    Information about the configuration of an EC2 instance.

    - **InstancePort** *(integer) --*

      The port on which the EC2 instance is listening.

    - **PolicyNames** *(list) --*

      The names of the policies enabled for the EC2 instance.

      - *(string) --*
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `HealthCheck`

    Information about the health checks conducted on the load balancer.

    - **Target** *(string) --*

      The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
      of valid ports is one (1) through 65535.

      TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
      case, a health check simply attempts to open a TCP connection to the instance on the
      specified port. Failure to connect within the configured timeout is considered
      unhealthy.

      SSL is also specified as SSL: port pair, for example, SSL:5000.

      For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
      HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
      case, a HTTP GET request is issued to the instance on the given port and path. Any
      answer other than "200 OK" within the timeout period is considered unhealthy.

      The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

    - **Interval** *(integer) --*

      The approximate interval, in seconds, between health checks of an individual instance.

    - **Timeout** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

      This value must be less than the ``Interval`` value.

    - **UnhealthyThreshold** *(integer) --*

      The number of consecutive health check failures required before moving the instance to
      the ``Unhealthy`` state.

    - **HealthyThreshold** *(integer) --*

      The number of consecutive health checks successes required before moving the instance
      to the ``Healthy`` state.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptions` `Listener`

    The listener.

    - **Protocol** *(string) --*

      The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

    - **LoadBalancerPort** *(integer) --*

      The port on which the load balancer is listening. On EC2-VPC, you can specify any
      port from the range 1-65535. On EC2-Classic, you can specify any port from the
      following list: 25, 80, 443, 465, 587, 1024-65535.

    - **InstanceProtocol** *(string) --*

      The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

      If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
      at the same protocol.

      If there is another listener with the same ``InstancePort`` whose
      ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
      must also be secure.

      If there is another listener with the same ``InstancePort`` whose
      ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
      HTTP or TCP.

    - **InstancePort** *(integer) --*

      The port on which the instance is listening.

    - **SSLCertificateId** *(string) --*

      The Amazon Resource Name (ARN) of the server certificate.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `ListenerDescriptions`

    The policies enabled for a listener.

    - **Listener** *(dict) --*

      The listener.

      - **Protocol** *(string) --*

        The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

      - **LoadBalancerPort** *(integer) --*

        The port on which the load balancer is listening. On EC2-VPC, you can specify any
        port from the range 1-65535. On EC2-Classic, you can specify any port from the
        following list: 25, 80, 443, 465, 587, 1024-65535.

      - **InstanceProtocol** *(string) --*

        The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

        If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
        at the same protocol.

        If there is another listener with the same ``InstancePort`` whose
        ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
        must also be secure.

        If there is another listener with the same ``InstancePort`` whose
        ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
        HTTP or TCP.

      - **InstancePort** *(integer) --*

        The port on which the instance is listening.

      - **SSLCertificateId** *(string) --*

        The Amazon Resource Name (ARN) of the server certificate.

    - **PolicyNames** *(list) --*

      The policies. If there are no policies enabled, the list is empty.

      - *(string) --*
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPolicies` `AppCookieStickinessPolicies`

    Information about a policy for application-controlled session stickiness.

    - **PolicyName** *(string) --*

      The mnemonic name for the policy being created. The name must be unique within a
      set of policies for this load balancer.

    - **CookieName** *(string) --*

      The name of the application cookie used for stickiness.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPolicies` `LBCookieStickinessPolicies`

    Information about a policy for duration-based session stickiness.

    - **PolicyName** *(string) --*

      The name of the policy. This name must be unique within the set of policies for
      this load balancer.

    - **CookieExpirationPeriod** *(integer) --*

      The time period, in seconds, after which the cookie should be considered stale. If
      this parameter is not specified, the stickiness session lasts for the duration of
      the browser session.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
        ],
        "LBCookieStickinessPolicies": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
        ],
        "OtherPolicies": List[str],
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `Policies`

    The policies defined for the load balancer.

    - **AppCookieStickinessPolicies** *(list) --*

      The stickiness policies created using  CreateAppCookieStickinessPolicy .

      - *(dict) --*

        Information about a policy for application-controlled session stickiness.

        - **PolicyName** *(string) --*

          The mnemonic name for the policy being created. The name must be unique within a
          set of policies for this load balancer.

        - **CookieName** *(string) --*

          The name of the application cookie used for stickiness.

    - **LBCookieStickinessPolicies** *(list) --*

      The stickiness policies created using  CreateLBCookieStickinessPolicy .

      - *(dict) --*

        Information about a policy for duration-based session stickiness.

        - **PolicyName** *(string) --*

          The name of the policy. This name must be unique within the set of policies for
          this load balancer.

        - **CookieExpirationPeriod** *(integer) --*

          The time period, in seconds, after which the cookie should be considered stale. If
          this parameter is not specified, the stickiness session lasts for the duration of
          the browser session.

    - **OtherPolicies** *(list) --*

      The policies other than the stickiness policies.

      - *(string) --*
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponseLoadBalancerDescriptions` `SourceSecurityGroup`

    The security group for the load balancer, which you can use as part of your inbound rules
    for your registered instances. To only allow traffic from load balancers, add a security
    group rule that specifies this source security group as the inbound source.

    - **OwnerAlias** *(string) --*

      The owner of the security group.

    - **GroupName** *(string) --*

      The name of the security group.
    """


_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
        ],
        "Policies": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsPoliciesTypeDef,
        "BackendServerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
        ],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsInstancesTypeDef
        ],
        "HealthCheck": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsHealthCheckTypeDef,
        "SourceSecurityGroup": ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef(
    _ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancersResponse` `LoadBalancerDescriptions`

    Information about a load balancer.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **DNSName** *(string) --*

      The DNS name of the load balancer.

    - **CanonicalHostedZoneName** *(string) --*

      The DNS name of the load balancer.

      For more information, see `Configure a Custom Domain Name
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html>`__
      in the *Classic Load Balancers Guide* .

    - **CanonicalHostedZoneNameID** *(string) --*

      The ID of the Amazon Route 53 hosted zone for the load balancer.

    - **ListenerDescriptions** *(list) --*

      The listeners for the load balancer.

      - *(dict) --*

        The policies enabled for a listener.

        - **Listener** *(dict) --*

          The listener.

          - **Protocol** *(string) --*

            The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

          - **LoadBalancerPort** *(integer) --*

            The port on which the load balancer is listening. On EC2-VPC, you can specify any
            port from the range 1-65535. On EC2-Classic, you can specify any port from the
            following list: 25, 80, 443, 465, 587, 1024-65535.

          - **InstanceProtocol** *(string) --*

            The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
            at the same protocol.

            If there is another listener with the same ``InstancePort`` whose
            ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
            must also be secure.

            If there is another listener with the same ``InstancePort`` whose
            ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
            HTTP or TCP.

          - **InstancePort** *(integer) --*

            The port on which the instance is listening.

          - **SSLCertificateId** *(string) --*

            The Amazon Resource Name (ARN) of the server certificate.

        - **PolicyNames** *(list) --*

          The policies. If there are no policies enabled, the list is empty.

          - *(string) --*

    - **Policies** *(dict) --*

      The policies defined for the load balancer.

      - **AppCookieStickinessPolicies** *(list) --*

        The stickiness policies created using  CreateAppCookieStickinessPolicy .

        - *(dict) --*

          Information about a policy for application-controlled session stickiness.

          - **PolicyName** *(string) --*

            The mnemonic name for the policy being created. The name must be unique within a
            set of policies for this load balancer.

          - **CookieName** *(string) --*

            The name of the application cookie used for stickiness.

      - **LBCookieStickinessPolicies** *(list) --*

        The stickiness policies created using  CreateLBCookieStickinessPolicy .

        - *(dict) --*

          Information about a policy for duration-based session stickiness.

          - **PolicyName** *(string) --*

            The name of the policy. This name must be unique within the set of policies for
            this load balancer.

          - **CookieExpirationPeriod** *(integer) --*

            The time period, in seconds, after which the cookie should be considered stale. If
            this parameter is not specified, the stickiness session lasts for the duration of
            the browser session.

      - **OtherPolicies** *(list) --*

        The policies other than the stickiness policies.

        - *(string) --*

    - **BackendServerDescriptions** *(list) --*

      Information about your EC2 instances.

      - *(dict) --*

        Information about the configuration of an EC2 instance.

        - **InstancePort** *(integer) --*

          The port on which the EC2 instance is listening.

        - **PolicyNames** *(list) --*

          The names of the policies enabled for the EC2 instance.

          - *(string) --*

    - **AvailabilityZones** *(list) --*

      The Availability Zones for the load balancer.

      - *(string) --*

    - **Subnets** *(list) --*

      The IDs of the subnets for the load balancer.

      - *(string) --*

    - **VPCId** *(string) --*

      The ID of the VPC for the load balancer.

    - **Instances** *(list) --*

      The IDs of the instances for the load balancer.

      - *(dict) --*

        The ID of an EC2 instance.

        - **InstanceId** *(string) --*

          The instance ID.

    - **HealthCheck** *(dict) --*

      Information about the health checks conducted on the load balancer.

      - **Target** *(string) --*

        The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
        of valid ports is one (1) through 65535.

        TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
        case, a health check simply attempts to open a TCP connection to the instance on the
        specified port. Failure to connect within the configured timeout is considered
        unhealthy.

        SSL is also specified as SSL: port pair, for example, SSL:5000.

        For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
        HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
        case, a HTTP GET request is issued to the instance on the given port and path. Any
        answer other than "200 OK" within the timeout period is considered unhealthy.

        The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

      - **Interval** *(integer) --*

        The approximate interval, in seconds, between health checks of an individual instance.

      - **Timeout** *(integer) --*

        The amount of time, in seconds, during which no response means a failed health check.

        This value must be less than the ``Interval`` value.

      - **UnhealthyThreshold** *(integer) --*

        The number of consecutive health check failures required before moving the instance to
        the ``Unhealthy`` state.

      - **HealthyThreshold** *(integer) --*

        The number of consecutive health checks successes required before moving the instance
        to the ``Healthy`` state.

    - **SourceSecurityGroup** *(dict) --*

      The security group for the load balancer, which you can use as part of your inbound rules
      for your registered instances. To only allow traffic from load balancers, add a security
      group rule that specifies this source security group as the inbound source.

      - **OwnerAlias** *(string) --*

        The owner of the security group.

      - **GroupName** *(string) --*

        The name of the security group.

    - **SecurityGroups** *(list) --*

      The security groups for the load balancer. Valid only for load balancers in a VPC.

      - *(string) --*

    - **CreatedTime** *(datetime) --*

      The date and time the load balancer was created.

    - **Scheme** *(string) --*

      The type of load balancer. Valid only for load balancers in a VPC.

      If ``Scheme`` is ``internet-facing`` , the load balancer has a public DNS name that
      resolves to a public IP address.

      If ``Scheme`` is ``internal`` , the load balancer has a public DNS name that resolves to
      a private IP address.
    """


_ClientDescribeLoadBalancersResponseTypeDef = TypedDict(
    "_ClientDescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            ClientDescribeLoadBalancersResponseLoadBalancerDescriptionsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientDescribeLoadBalancersResponseTypeDef(
    _ClientDescribeLoadBalancersResponseTypeDef
):
    """
    Type definition for `ClientDescribeLoadBalancers` `Response`

    Contains the parameters for DescribeLoadBalancers.

    - **LoadBalancerDescriptions** *(list) --*

      Information about the load balancers.

      - *(dict) --*

        Information about a load balancer.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **DNSName** *(string) --*

          The DNS name of the load balancer.

        - **CanonicalHostedZoneName** *(string) --*

          The DNS name of the load balancer.

          For more information, see `Configure a Custom Domain Name
          <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html>`__
          in the *Classic Load Balancers Guide* .

        - **CanonicalHostedZoneNameID** *(string) --*

          The ID of the Amazon Route 53 hosted zone for the load balancer.

        - **ListenerDescriptions** *(list) --*

          The listeners for the load balancer.

          - *(dict) --*

            The policies enabled for a listener.

            - **Listener** *(dict) --*

              The listener.

              - **Protocol** *(string) --*

                The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

              - **LoadBalancerPort** *(integer) --*

                The port on which the load balancer is listening. On EC2-VPC, you can specify any
                port from the range 1-65535. On EC2-Classic, you can specify any port from the
                following list: 25, 80, 443, 465, 587, 1024-65535.

              - **InstanceProtocol** *(string) --*

                The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

                If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
                at the same protocol.

                If there is another listener with the same ``InstancePort`` whose
                ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
                must also be secure.

                If there is another listener with the same ``InstancePort`` whose
                ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
                HTTP or TCP.

              - **InstancePort** *(integer) --*

                The port on which the instance is listening.

              - **SSLCertificateId** *(string) --*

                The Amazon Resource Name (ARN) of the server certificate.

            - **PolicyNames** *(list) --*

              The policies. If there are no policies enabled, the list is empty.

              - *(string) --*

        - **Policies** *(dict) --*

          The policies defined for the load balancer.

          - **AppCookieStickinessPolicies** *(list) --*

            The stickiness policies created using  CreateAppCookieStickinessPolicy .

            - *(dict) --*

              Information about a policy for application-controlled session stickiness.

              - **PolicyName** *(string) --*

                The mnemonic name for the policy being created. The name must be unique within a
                set of policies for this load balancer.

              - **CookieName** *(string) --*

                The name of the application cookie used for stickiness.

          - **LBCookieStickinessPolicies** *(list) --*

            The stickiness policies created using  CreateLBCookieStickinessPolicy .

            - *(dict) --*

              Information about a policy for duration-based session stickiness.

              - **PolicyName** *(string) --*

                The name of the policy. This name must be unique within the set of policies for
                this load balancer.

              - **CookieExpirationPeriod** *(integer) --*

                The time period, in seconds, after which the cookie should be considered stale. If
                this parameter is not specified, the stickiness session lasts for the duration of
                the browser session.

          - **OtherPolicies** *(list) --*

            The policies other than the stickiness policies.

            - *(string) --*

        - **BackendServerDescriptions** *(list) --*

          Information about your EC2 instances.

          - *(dict) --*

            Information about the configuration of an EC2 instance.

            - **InstancePort** *(integer) --*

              The port on which the EC2 instance is listening.

            - **PolicyNames** *(list) --*

              The names of the policies enabled for the EC2 instance.

              - *(string) --*

        - **AvailabilityZones** *(list) --*

          The Availability Zones for the load balancer.

          - *(string) --*

        - **Subnets** *(list) --*

          The IDs of the subnets for the load balancer.

          - *(string) --*

        - **VPCId** *(string) --*

          The ID of the VPC for the load balancer.

        - **Instances** *(list) --*

          The IDs of the instances for the load balancer.

          - *(dict) --*

            The ID of an EC2 instance.

            - **InstanceId** *(string) --*

              The instance ID.

        - **HealthCheck** *(dict) --*

          Information about the health checks conducted on the load balancer.

          - **Target** *(string) --*

            The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
            of valid ports is one (1) through 65535.

            TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
            case, a health check simply attempts to open a TCP connection to the instance on the
            specified port. Failure to connect within the configured timeout is considered
            unhealthy.

            SSL is also specified as SSL: port pair, for example, SSL:5000.

            For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
            HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
            case, a HTTP GET request is issued to the instance on the given port and path. Any
            answer other than "200 OK" within the timeout period is considered unhealthy.

            The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

          - **Interval** *(integer) --*

            The approximate interval, in seconds, between health checks of an individual instance.

          - **Timeout** *(integer) --*

            The amount of time, in seconds, during which no response means a failed health check.

            This value must be less than the ``Interval`` value.

          - **UnhealthyThreshold** *(integer) --*

            The number of consecutive health check failures required before moving the instance to
            the ``Unhealthy`` state.

          - **HealthyThreshold** *(integer) --*

            The number of consecutive health checks successes required before moving the instance
            to the ``Healthy`` state.

        - **SourceSecurityGroup** *(dict) --*

          The security group for the load balancer, which you can use as part of your inbound rules
          for your registered instances. To only allow traffic from load balancers, add a security
          group rule that specifies this source security group as the inbound source.

          - **OwnerAlias** *(string) --*

            The owner of the security group.

          - **GroupName** *(string) --*

            The name of the security group.

        - **SecurityGroups** *(list) --*

          The security groups for the load balancer. Valid only for load balancers in a VPC.

          - *(string) --*

        - **CreatedTime** *(datetime) --*

          The date and time the load balancer was created.

        - **Scheme** *(string) --*

          The type of load balancer. Valid only for load balancers in a VPC.

          If ``Scheme`` is ``internet-facing`` , the load balancer has a public DNS name that
          resolves to a public IP address.

          If ``Scheme`` is ``internal`` , the load balancer has a public DNS name that resolves to
          a private IP address.

    - **NextMarker** *(string) --*

      The marker to use when requesting the next set of results. If there are no additional
      results, the string is empty.
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
        "LoadBalancerName": str,
        "Tags": List[ClientDescribeTagsResponseTagDescriptionsTagsTypeDef],
    },
    total=False,
)


class ClientDescribeTagsResponseTagDescriptionsTypeDef(
    _ClientDescribeTagsResponseTagDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeTagsResponse` `TagDescriptions`

    The tags associated with a load balancer.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **Tags** *(list) --*

      The tags.

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

    Contains the output for DescribeTags.

    - **TagDescriptions** *(list) --*

      Information about the tags.

      - *(dict) --*

        The tags associated with a load balancer.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **Tags** *(list) --*

          The tags.

          - *(dict) --*

            Information about a tag.

            - **Key** *(string) --*

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.
    """


_ClientDetachLoadBalancerFromSubnetsResponseTypeDef = TypedDict(
    "_ClientDetachLoadBalancerFromSubnetsResponseTypeDef",
    {"Subnets": List[str]},
    total=False,
)


class ClientDetachLoadBalancerFromSubnetsResponseTypeDef(
    _ClientDetachLoadBalancerFromSubnetsResponseTypeDef
):
    """
    Type definition for `ClientDetachLoadBalancerFromSubnets` `Response`

    Contains the output of DetachLoadBalancerFromSubnets.

    - **Subnets** *(list) --*

      The IDs of the remaining subnets for the load balancer.

      - *(string) --*
    """


_ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "_ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)


class ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef(
    _ClientDisableAvailabilityZonesForLoadBalancerResponseTypeDef
):
    """
    Type definition for `ClientDisableAvailabilityZonesForLoadBalancer` `Response`

    Contains the output for DisableAvailabilityZonesForLoadBalancer.

    - **AvailabilityZones** *(list) --*

      The remaining Availability Zones for the load balancer.

      - *(string) --*
    """


_ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef = TypedDict(
    "_ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef",
    {"AvailabilityZones": List[str]},
    total=False,
)


class ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef(
    _ClientEnableAvailabilityZonesForLoadBalancerResponseTypeDef
):
    """
    Type definition for `ClientEnableAvailabilityZonesForLoadBalancer` `Response`

    Contains the output of EnableAvailabilityZonesForLoadBalancer.

    - **AvailabilityZones** *(list) --*

      The updated list of Availability Zones for the load balancer.

      - *(string) --*
    """


_RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool},
)
_OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef",
    {"S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef(
    _RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef,
    _OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef,
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesLoadBalancerAttributes` `AccessLog`

    If enabled, the load balancer captures detailed information of all requests and delivers the
    information to the Amazon S3 bucket that you specify.

    For more information, see `Enable Access Logs
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__ in
    the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether access logs are enabled for the load balancer.

    - **S3BucketName** *(string) --*

      The name of the Amazon S3 bucket where the access logs are stored.

    - **EmitInterval** *(integer) --*

      The interval for publishing the access logs. You can specify an interval of either 5 minutes
      or 60 minutes.

      Default: 60 minutes

    - **S3BucketPrefix** *(string) --*

      The logical hierarchy you created for your Amazon S3 bucket, for example
      ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
      level of the bucket.
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesLoadBalancerAttributes` `AdditionalAttributes`

    This data type is reserved.

    - **Key** *(string) --*

      This parameter is reserved.

    - **Value** *(string) --*

      This parameter is reserved.
    """


_RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool},
)
_OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Timeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef(
    _RequiredClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef,
    _OptionalClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef,
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesLoadBalancerAttributes` `ConnectionDraining`

    If enabled, the load balancer allows existing requests to complete before the load balancer
    shifts traffic away from a deregistered or unhealthy instance.

    For more information, see `Configure Connection Draining
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__ in
    the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether connection draining is enabled for the load balancer.

    - **Timeout** *(integer) --*

      The maximum time, in seconds, to keep the existing connections open before deregistering the
      instances.
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesLoadBalancerAttributes` `ConnectionSettings`

    If enabled, the load balancer allows the connections to remain idle (no data is sent over the
    connection) for the specified duration.

    By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
    front-end and back-end connections of your load balancer. For more information, see `Configure
    Idle Connection Timeout
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__ in
    the *Classic Load Balancers Guide* .

    - **IdleTimeout** *(integer) --* **[REQUIRED]**

      The time, in seconds, that the connection is allowed to be idle (no data has been sent over
      the connection) before it is closed by the load balancer.
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesLoadBalancerAttributes` `CrossZoneLoadBalancing`

    If enabled, the load balancer routes the request traffic evenly across all instances regardless
    of the Availability Zones.

    For more information, see `Configure Cross-Zone Load Balancing
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesLoadBalancerAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributes` `LoadBalancerAttributes`

    The attributes for the load balancer.

    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances regardless
      of the Availability Zones.

      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether cross-zone load balancing is enabled for the load balancer.

    - **AccessLog** *(dict) --*

      If enabled, the load balancer captures detailed information of all requests and delivers the
      information to the Amazon S3 bucket that you specify.

      For more information, see `Enable Access Logs
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__ in
      the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether access logs are enabled for the load balancer.

      - **S3BucketName** *(string) --*

        The name of the Amazon S3 bucket where the access logs are stored.

      - **EmitInterval** *(integer) --*

        The interval for publishing the access logs. You can specify an interval of either 5 minutes
        or 60 minutes.

        Default: 60 minutes

      - **S3BucketPrefix** *(string) --*

        The logical hierarchy you created for your Amazon S3 bucket, for example
        ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
        level of the bucket.

    - **ConnectionDraining** *(dict) --*

      If enabled, the load balancer allows existing requests to complete before the load balancer
      shifts traffic away from a deregistered or unhealthy instance.

      For more information, see `Configure Connection Draining
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__ in
      the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether connection draining is enabled for the load balancer.

      - **Timeout** *(integer) --*

        The maximum time, in seconds, to keep the existing connections open before deregistering the
        instances.

    - **ConnectionSettings** *(dict) --*

      If enabled, the load balancer allows the connections to remain idle (no data is sent over the
      connection) for the specified duration.

      By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
      front-end and back-end connections of your load balancer. For more information, see `Configure
      Idle Connection Timeout
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__ in
      the *Classic Load Balancers Guide* .

      - **IdleTimeout** *(integer) --* **[REQUIRED]**

        The time, in seconds, that the connection is allowed to be idle (no data has been sent over
        the connection) before it is closed by the load balancer.

    - **AdditionalAttributes** *(list) --*

      This parameter is reserved.

      - *(dict) --*

        This data type is reserved.

        - **Key** *(string) --*

          This parameter is reserved.

        - **Value** *(string) --*

          This parameter is reserved.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef",
    {"Enabled": bool, "S3BucketName": str, "EmitInterval": int, "S3BucketPrefix": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributes` `AccessLog`

    If enabled, the load balancer captures detailed information of all requests and delivers
    the information to the Amazon S3 bucket that you specify.

    For more information, see `Enable Access Logs
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether access logs are enabled for the load balancer.

    - **S3BucketName** *(string) --*

      The name of the Amazon S3 bucket where the access logs are stored.

    - **EmitInterval** *(integer) --*

      The interval for publishing the access logs. You can specify an interval of either 5
      minutes or 60 minutes.

      Default: 60 minutes

    - **S3BucketPrefix** *(string) --*

      The logical hierarchy you created for your Amazon S3 bucket, for example
      ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
      level of the bucket.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributes` `AdditionalAttributes`

    This data type is reserved.

    - **Key** *(string) --*

      This parameter is reserved.

    - **Value** *(string) --*

      This parameter is reserved.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef",
    {"Enabled": bool, "Timeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributes` `ConnectionDraining`

    If enabled, the load balancer allows existing requests to complete before the load balancer
    shifts traffic away from a deregistered or unhealthy instance.

    For more information, see `Configure Connection Draining
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether connection draining is enabled for the load balancer.

    - **Timeout** *(integer) --*

      The maximum time, in seconds, to keep the existing connections open before deregistering
      the instances.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef",
    {"IdleTimeout": int},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributes` `ConnectionSettings`

    If enabled, the load balancer allows the connections to remain idle (no data is sent over
    the connection) for the specified duration.

    By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
    front-end and back-end connections of your load balancer. For more information, see
    `Configure Idle Connection Timeout
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
    in the *Classic Load Balancers Guide* .

    - **IdleTimeout** *(integer) --*

      The time, in seconds, that the connection is allowed to be idle (no data has been sent
      over the connection) before it is closed by the load balancer.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributes` `CrossZoneLoadBalancing`

    If enabled, the load balancer routes the request traffic evenly across all instances
    regardless of the Availability Zones.

    For more information, see `Configure Cross-Zone Load Balancing
    <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
    in the *Classic Load Balancers Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether cross-zone load balancing is enabled for the load balancer.
    """


_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesCrossZoneLoadBalancingTypeDef,
        "AccessLog": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAccessLogTypeDef,
        "ConnectionDraining": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionDrainingTypeDef,
        "ConnectionSettings": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesConnectionSettingsTypeDef,
        "AdditionalAttributes": List[
            ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesAdditionalAttributesTypeDef
        ],
    },
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef(
    _ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributesResponse` `LoadBalancerAttributes`

    Information about the load balancer attributes.

    - **CrossZoneLoadBalancing** *(dict) --*

      If enabled, the load balancer routes the request traffic evenly across all instances
      regardless of the Availability Zones.

      For more information, see `Configure Cross-Zone Load Balancing
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether cross-zone load balancing is enabled for the load balancer.

    - **AccessLog** *(dict) --*

      If enabled, the load balancer captures detailed information of all requests and delivers
      the information to the Amazon S3 bucket that you specify.

      For more information, see `Enable Access Logs
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether access logs are enabled for the load balancer.

      - **S3BucketName** *(string) --*

        The name of the Amazon S3 bucket where the access logs are stored.

      - **EmitInterval** *(integer) --*

        The interval for publishing the access logs. You can specify an interval of either 5
        minutes or 60 minutes.

        Default: 60 minutes

      - **S3BucketPrefix** *(string) --*

        The logical hierarchy you created for your Amazon S3 bucket, for example
        ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
        level of the bucket.

    - **ConnectionDraining** *(dict) --*

      If enabled, the load balancer allows existing requests to complete before the load balancer
      shifts traffic away from a deregistered or unhealthy instance.

      For more information, see `Configure Connection Draining
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
      in the *Classic Load Balancers Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether connection draining is enabled for the load balancer.

      - **Timeout** *(integer) --*

        The maximum time, in seconds, to keep the existing connections open before deregistering
        the instances.

    - **ConnectionSettings** *(dict) --*

      If enabled, the load balancer allows the connections to remain idle (no data is sent over
      the connection) for the specified duration.

      By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
      front-end and back-end connections of your load balancer. For more information, see
      `Configure Idle Connection Timeout
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
      in the *Classic Load Balancers Guide* .

      - **IdleTimeout** *(integer) --*

        The time, in seconds, that the connection is allowed to be idle (no data has been sent
        over the connection) before it is closed by the load balancer.

    - **AdditionalAttributes** *(list) --*

      This parameter is reserved.

      - *(dict) --*

        This data type is reserved.

        - **Key** *(string) --*

          This parameter is reserved.

        - **Value** *(string) --*

          This parameter is reserved.
    """


_ClientModifyLoadBalancerAttributesResponseTypeDef = TypedDict(
    "_ClientModifyLoadBalancerAttributesResponseTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": ClientModifyLoadBalancerAttributesResponseLoadBalancerAttributesTypeDef,
    },
    total=False,
)


class ClientModifyLoadBalancerAttributesResponseTypeDef(
    _ClientModifyLoadBalancerAttributesResponseTypeDef
):
    """
    Type definition for `ClientModifyLoadBalancerAttributes` `Response`

    Contains the output of ModifyLoadBalancerAttributes.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **LoadBalancerAttributes** *(dict) --*

      Information about the load balancer attributes.

      - **CrossZoneLoadBalancing** *(dict) --*

        If enabled, the load balancer routes the request traffic evenly across all instances
        regardless of the Availability Zones.

        For more information, see `Configure Cross-Zone Load Balancing
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether cross-zone load balancing is enabled for the load balancer.

      - **AccessLog** *(dict) --*

        If enabled, the load balancer captures detailed information of all requests and delivers
        the information to the Amazon S3 bucket that you specify.

        For more information, see `Enable Access Logs
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether access logs are enabled for the load balancer.

        - **S3BucketName** *(string) --*

          The name of the Amazon S3 bucket where the access logs are stored.

        - **EmitInterval** *(integer) --*

          The interval for publishing the access logs. You can specify an interval of either 5
          minutes or 60 minutes.

          Default: 60 minutes

        - **S3BucketPrefix** *(string) --*

          The logical hierarchy you created for your Amazon S3 bucket, for example
          ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root
          level of the bucket.

      - **ConnectionDraining** *(dict) --*

        If enabled, the load balancer allows existing requests to complete before the load balancer
        shifts traffic away from a deregistered or unhealthy instance.

        For more information, see `Configure Connection Draining
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__
        in the *Classic Load Balancers Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether connection draining is enabled for the load balancer.

        - **Timeout** *(integer) --*

          The maximum time, in seconds, to keep the existing connections open before deregistering
          the instances.

      - **ConnectionSettings** *(dict) --*

        If enabled, the load balancer allows the connections to remain idle (no data is sent over
        the connection) for the specified duration.

        By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both
        front-end and back-end connections of your load balancer. For more information, see
        `Configure Idle Connection Timeout
        <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__
        in the *Classic Load Balancers Guide* .

        - **IdleTimeout** *(integer) --*

          The time, in seconds, that the connection is allowed to be idle (no data has been sent
          over the connection) before it is closed by the load balancer.

      - **AdditionalAttributes** *(list) --*

        This parameter is reserved.

        - *(dict) --*

          This data type is reserved.

          - **Key** *(string) --*

            This parameter is reserved.

          - **Value** *(string) --*

            This parameter is reserved.
    """


_ClientRegisterInstancesWithLoadBalancerInstancesTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientRegisterInstancesWithLoadBalancerInstancesTypeDef(
    _ClientRegisterInstancesWithLoadBalancerInstancesTypeDef
):
    """
    Type definition for `ClientRegisterInstancesWithLoadBalancer` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef(
    _ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef
):
    """
    Type definition for `ClientRegisterInstancesWithLoadBalancerResponse` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_ClientRegisterInstancesWithLoadBalancerResponseTypeDef = TypedDict(
    "_ClientRegisterInstancesWithLoadBalancerResponseTypeDef",
    {
        "Instances": List[
            ClientRegisterInstancesWithLoadBalancerResponseInstancesTypeDef
        ]
    },
    total=False,
)


class ClientRegisterInstancesWithLoadBalancerResponseTypeDef(
    _ClientRegisterInstancesWithLoadBalancerResponseTypeDef
):
    """
    Type definition for `ClientRegisterInstancesWithLoadBalancer` `Response`

    Contains the output of RegisterInstancesWithLoadBalancer.

    - **Instances** *(list) --*

      The updated list of instances for the load balancer.

      - *(dict) --*

        The ID of an EC2 instance.

        - **InstanceId** *(string) --*

          The instance ID.
    """


_ClientRemoveTagsTagsTypeDef = TypedDict(
    "_ClientRemoveTagsTagsTypeDef", {"Key": str}, total=False
)


class ClientRemoveTagsTagsTypeDef(_ClientRemoveTagsTagsTypeDef):
    """
    Type definition for `ClientRemoveTags` `Tags`

    The key of a tag.

    - **Key** *(string) --*

      The name of the key.
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

      * classic-listeners

      * classic-load-balancers

      * classic-registered-instances

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

          * classic-listeners

          * classic-load-balancers

          * classic-registered-instances

        - **Max** *(string) --*

          The maximum value of the limit.

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


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef",
    {"InstancePort": int, "PolicyNames": List[str]},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `BackendServerDescriptions`

    Information about the configuration of an EC2 instance.

    - **InstancePort** *(integer) --*

      The port on which the EC2 instance is listening.

    - **PolicyNames** *(list) --*

      The names of the policies enabled for the EC2 instance.

      - *(string) --*
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `HealthCheck`

    Information about the health checks conducted on the load balancer.

    - **Target** *(string) --*

      The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
      of valid ports is one (1) through 65535.

      TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
      case, a health check simply attempts to open a TCP connection to the instance on the
      specified port. Failure to connect within the configured timeout is considered
      unhealthy.

      SSL is also specified as SSL: port pair, for example, SSL:5000.

      For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
      HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
      case, a HTTP GET request is issued to the instance on the given port and path. Any
      answer other than "200 OK" within the timeout period is considered unhealthy.

      The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

    - **Interval** *(integer) --*

      The approximate interval, in seconds, between health checks of an individual instance.

    - **Timeout** *(integer) --*

      The amount of time, in seconds, during which no response means a failed health check.

      This value must be less than the ``Interval`` value.

    - **UnhealthyThreshold** *(integer) --*

      The number of consecutive health check failures required before moving the instance to
      the ``Unhealthy`` state.

    - **HealthyThreshold** *(integer) --*

      The number of consecutive health checks successes required before moving the instance
      to the ``Healthy`` state.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef",
    {"InstanceId": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstanceProtocol": str,
        "InstancePort": int,
        "SSLCertificateId": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptions` `Listener`

    The listener.

    - **Protocol** *(string) --*

      The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

    - **LoadBalancerPort** *(integer) --*

      The port on which the load balancer is listening. On EC2-VPC, you can specify any
      port from the range 1-65535. On EC2-Classic, you can specify any port from the
      following list: 25, 80, 443, 465, 587, 1024-65535.

    - **InstanceProtocol** *(string) --*

      The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

      If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
      at the same protocol.

      If there is another listener with the same ``InstancePort`` whose
      ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
      must also be secure.

      If there is another listener with the same ``InstancePort`` whose
      ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
      HTTP or TCP.

    - **InstancePort** *(integer) --*

      The port on which the instance is listening.

    - **SSLCertificateId** *(string) --*

      The Amazon Resource Name (ARN) of the server certificate.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef",
    {
        "Listener": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsListenerTypeDef,
        "PolicyNames": List[str],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `ListenerDescriptions`

    The policies enabled for a listener.

    - **Listener** *(dict) --*

      The listener.

      - **Protocol** *(string) --*

        The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

      - **LoadBalancerPort** *(integer) --*

        The port on which the load balancer is listening. On EC2-VPC, you can specify any
        port from the range 1-65535. On EC2-Classic, you can specify any port from the
        following list: 25, 80, 443, 465, 587, 1024-65535.

      - **InstanceProtocol** *(string) --*

        The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

        If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
        at the same protocol.

        If there is another listener with the same ``InstancePort`` whose
        ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
        must also be secure.

        If there is another listener with the same ``InstancePort`` whose
        ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
        HTTP or TCP.

      - **InstancePort** *(integer) --*

        The port on which the instance is listening.

      - **SSLCertificateId** *(string) --*

        The Amazon Resource Name (ARN) of the server certificate.

    - **PolicyNames** *(list) --*

      The policies. If there are no policies enabled, the list is empty.

      - *(string) --*
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieName": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPolicies` `AppCookieStickinessPolicies`

    Information about a policy for application-controlled session stickiness.

    - **PolicyName** *(string) --*

      The mnemonic name for the policy being created. The name must be unique within a
      set of policies for this load balancer.

    - **CookieName** *(string) --*

      The name of the application cookie used for stickiness.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef",
    {"PolicyName": str, "CookieExpirationPeriod": int},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPolicies` `LBCookieStickinessPolicies`

    Information about a policy for duration-based session stickiness.

    - **PolicyName** *(string) --*

      The name of the policy. This name must be unique within the set of policies for
      this load balancer.

    - **CookieExpirationPeriod** *(integer) --*

      The time period, in seconds, after which the cookie should be considered stale. If
      this parameter is not specified, the stickiness session lasts for the duration of
      the browser session.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesAppCookieStickinessPoliciesTypeDef
        ],
        "LBCookieStickinessPolicies": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesLBCookieStickinessPoliciesTypeDef
        ],
        "OtherPolicies": List[str],
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `Policies`

    The policies defined for the load balancer.

    - **AppCookieStickinessPolicies** *(list) --*

      The stickiness policies created using  CreateAppCookieStickinessPolicy .

      - *(dict) --*

        Information about a policy for application-controlled session stickiness.

        - **PolicyName** *(string) --*

          The mnemonic name for the policy being created. The name must be unique within a
          set of policies for this load balancer.

        - **CookieName** *(string) --*

          The name of the application cookie used for stickiness.

    - **LBCookieStickinessPolicies** *(list) --*

      The stickiness policies created using  CreateLBCookieStickinessPolicy .

      - *(dict) --*

        Information about a policy for duration-based session stickiness.

        - **PolicyName** *(string) --*

          The name of the policy. This name must be unique within the set of policies for
          this load balancer.

        - **CookieExpirationPeriod** *(integer) --*

          The time period, in seconds, after which the cookie should be considered stale. If
          this parameter is not specified, the stickiness session lasts for the duration of
          the browser session.

    - **OtherPolicies** *(list) --*

      The policies other than the stickiness policies.

      - *(string) --*
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef",
    {"OwnerAlias": str, "GroupName": str},
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponseLoadBalancerDescriptions` `SourceSecurityGroup`

    The security group for the load balancer, which you can use as part of your inbound rules
    for your registered instances. To only allow traffic from load balancers, add a security
    group rule that specifies this source security group as the inbound source.

    - **OwnerAlias** *(string) --*

      The owner of the security group.

    - **GroupName** *(string) --*

      The name of the security group.
    """


_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsListenerDescriptionsTypeDef
        ],
        "Policies": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsPoliciesTypeDef,
        "BackendServerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsBackendServerDescriptionsTypeDef
        ],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsInstancesTypeDef
        ],
        "HealthCheck": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsHealthCheckTypeDef,
        "SourceSecurityGroup": DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsSourceSecurityGroupTypeDef,
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)


class DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef(
    _DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef
):
    """
    Type definition for `DescribeLoadBalancersPaginateResponse` `LoadBalancerDescriptions`

    Information about a load balancer.

    - **LoadBalancerName** *(string) --*

      The name of the load balancer.

    - **DNSName** *(string) --*

      The DNS name of the load balancer.

    - **CanonicalHostedZoneName** *(string) --*

      The DNS name of the load balancer.

      For more information, see `Configure a Custom Domain Name
      <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html>`__
      in the *Classic Load Balancers Guide* .

    - **CanonicalHostedZoneNameID** *(string) --*

      The ID of the Amazon Route 53 hosted zone for the load balancer.

    - **ListenerDescriptions** *(list) --*

      The listeners for the load balancer.

      - *(dict) --*

        The policies enabled for a listener.

        - **Listener** *(dict) --*

          The listener.

          - **Protocol** *(string) --*

            The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

          - **LoadBalancerPort** *(integer) --*

            The port on which the load balancer is listening. On EC2-VPC, you can specify any
            port from the range 1-65535. On EC2-Classic, you can specify any port from the
            following list: 25, 80, 443, 465, 587, 1024-65535.

          - **InstanceProtocol** *(string) --*

            The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

            If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
            at the same protocol.

            If there is another listener with the same ``InstancePort`` whose
            ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
            must also be secure.

            If there is another listener with the same ``InstancePort`` whose
            ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
            HTTP or TCP.

          - **InstancePort** *(integer) --*

            The port on which the instance is listening.

          - **SSLCertificateId** *(string) --*

            The Amazon Resource Name (ARN) of the server certificate.

        - **PolicyNames** *(list) --*

          The policies. If there are no policies enabled, the list is empty.

          - *(string) --*

    - **Policies** *(dict) --*

      The policies defined for the load balancer.

      - **AppCookieStickinessPolicies** *(list) --*

        The stickiness policies created using  CreateAppCookieStickinessPolicy .

        - *(dict) --*

          Information about a policy for application-controlled session stickiness.

          - **PolicyName** *(string) --*

            The mnemonic name for the policy being created. The name must be unique within a
            set of policies for this load balancer.

          - **CookieName** *(string) --*

            The name of the application cookie used for stickiness.

      - **LBCookieStickinessPolicies** *(list) --*

        The stickiness policies created using  CreateLBCookieStickinessPolicy .

        - *(dict) --*

          Information about a policy for duration-based session stickiness.

          - **PolicyName** *(string) --*

            The name of the policy. This name must be unique within the set of policies for
            this load balancer.

          - **CookieExpirationPeriod** *(integer) --*

            The time period, in seconds, after which the cookie should be considered stale. If
            this parameter is not specified, the stickiness session lasts for the duration of
            the browser session.

      - **OtherPolicies** *(list) --*

        The policies other than the stickiness policies.

        - *(string) --*

    - **BackendServerDescriptions** *(list) --*

      Information about your EC2 instances.

      - *(dict) --*

        Information about the configuration of an EC2 instance.

        - **InstancePort** *(integer) --*

          The port on which the EC2 instance is listening.

        - **PolicyNames** *(list) --*

          The names of the policies enabled for the EC2 instance.

          - *(string) --*

    - **AvailabilityZones** *(list) --*

      The Availability Zones for the load balancer.

      - *(string) --*

    - **Subnets** *(list) --*

      The IDs of the subnets for the load balancer.

      - *(string) --*

    - **VPCId** *(string) --*

      The ID of the VPC for the load balancer.

    - **Instances** *(list) --*

      The IDs of the instances for the load balancer.

      - *(dict) --*

        The ID of an EC2 instance.

        - **InstanceId** *(string) --*

          The instance ID.

    - **HealthCheck** *(dict) --*

      Information about the health checks conducted on the load balancer.

      - **Target** *(string) --*

        The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
        of valid ports is one (1) through 65535.

        TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
        case, a health check simply attempts to open a TCP connection to the instance on the
        specified port. Failure to connect within the configured timeout is considered
        unhealthy.

        SSL is also specified as SSL: port pair, for example, SSL:5000.

        For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
        HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
        case, a HTTP GET request is issued to the instance on the given port and path. Any
        answer other than "200 OK" within the timeout period is considered unhealthy.

        The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

      - **Interval** *(integer) --*

        The approximate interval, in seconds, between health checks of an individual instance.

      - **Timeout** *(integer) --*

        The amount of time, in seconds, during which no response means a failed health check.

        This value must be less than the ``Interval`` value.

      - **UnhealthyThreshold** *(integer) --*

        The number of consecutive health check failures required before moving the instance to
        the ``Unhealthy`` state.

      - **HealthyThreshold** *(integer) --*

        The number of consecutive health checks successes required before moving the instance
        to the ``Healthy`` state.

    - **SourceSecurityGroup** *(dict) --*

      The security group for the load balancer, which you can use as part of your inbound rules
      for your registered instances. To only allow traffic from load balancers, add a security
      group rule that specifies this source security group as the inbound source.

      - **OwnerAlias** *(string) --*

        The owner of the security group.

      - **GroupName** *(string) --*

        The name of the security group.

    - **SecurityGroups** *(list) --*

      The security groups for the load balancer. Valid only for load balancers in a VPC.

      - *(string) --*

    - **CreatedTime** *(datetime) --*

      The date and time the load balancer was created.

    - **Scheme** *(string) --*

      The type of load balancer. Valid only for load balancers in a VPC.

      If ``Scheme`` is ``internet-facing`` , the load balancer has a public DNS name that
      resolves to a public IP address.

      If ``Scheme`` is ``internal`` , the load balancer has a public DNS name that resolves to
      a private IP address.
    """


_DescribeLoadBalancersPaginateResponseTypeDef = TypedDict(
    "_DescribeLoadBalancersPaginateResponseTypeDef",
    {
        "LoadBalancerDescriptions": List[
            DescribeLoadBalancersPaginateResponseLoadBalancerDescriptionsTypeDef
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

    Contains the parameters for DescribeLoadBalancers.

    - **LoadBalancerDescriptions** *(list) --*

      Information about the load balancers.

      - *(dict) --*

        Information about a load balancer.

        - **LoadBalancerName** *(string) --*

          The name of the load balancer.

        - **DNSName** *(string) --*

          The DNS name of the load balancer.

        - **CanonicalHostedZoneName** *(string) --*

          The DNS name of the load balancer.

          For more information, see `Configure a Custom Domain Name
          <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html>`__
          in the *Classic Load Balancers Guide* .

        - **CanonicalHostedZoneNameID** *(string) --*

          The ID of the Amazon Route 53 hosted zone for the load balancer.

        - **ListenerDescriptions** *(list) --*

          The listeners for the load balancer.

          - *(dict) --*

            The policies enabled for a listener.

            - **Listener** *(dict) --*

              The listener.

              - **Protocol** *(string) --*

                The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

              - **LoadBalancerPort** *(integer) --*

                The port on which the load balancer is listening. On EC2-VPC, you can specify any
                port from the range 1-65535. On EC2-Classic, you can specify any port from the
                following list: 25, 80, 443, 465, 587, 1024-65535.

              - **InstanceProtocol** *(string) --*

                The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.

                If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be
                at the same protocol.

                If there is another listener with the same ``InstancePort`` whose
                ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener's ``InstanceProtocol``
                must also be secure.

                If there is another listener with the same ``InstancePort`` whose
                ``InstanceProtocol`` is HTTP or TCP, the listener's ``InstanceProtocol`` must be
                HTTP or TCP.

              - **InstancePort** *(integer) --*

                The port on which the instance is listening.

              - **SSLCertificateId** *(string) --*

                The Amazon Resource Name (ARN) of the server certificate.

            - **PolicyNames** *(list) --*

              The policies. If there are no policies enabled, the list is empty.

              - *(string) --*

        - **Policies** *(dict) --*

          The policies defined for the load balancer.

          - **AppCookieStickinessPolicies** *(list) --*

            The stickiness policies created using  CreateAppCookieStickinessPolicy .

            - *(dict) --*

              Information about a policy for application-controlled session stickiness.

              - **PolicyName** *(string) --*

                The mnemonic name for the policy being created. The name must be unique within a
                set of policies for this load balancer.

              - **CookieName** *(string) --*

                The name of the application cookie used for stickiness.

          - **LBCookieStickinessPolicies** *(list) --*

            The stickiness policies created using  CreateLBCookieStickinessPolicy .

            - *(dict) --*

              Information about a policy for duration-based session stickiness.

              - **PolicyName** *(string) --*

                The name of the policy. This name must be unique within the set of policies for
                this load balancer.

              - **CookieExpirationPeriod** *(integer) --*

                The time period, in seconds, after which the cookie should be considered stale. If
                this parameter is not specified, the stickiness session lasts for the duration of
                the browser session.

          - **OtherPolicies** *(list) --*

            The policies other than the stickiness policies.

            - *(string) --*

        - **BackendServerDescriptions** *(list) --*

          Information about your EC2 instances.

          - *(dict) --*

            Information about the configuration of an EC2 instance.

            - **InstancePort** *(integer) --*

              The port on which the EC2 instance is listening.

            - **PolicyNames** *(list) --*

              The names of the policies enabled for the EC2 instance.

              - *(string) --*

        - **AvailabilityZones** *(list) --*

          The Availability Zones for the load balancer.

          - *(string) --*

        - **Subnets** *(list) --*

          The IDs of the subnets for the load balancer.

          - *(string) --*

        - **VPCId** *(string) --*

          The ID of the VPC for the load balancer.

        - **Instances** *(list) --*

          The IDs of the instances for the load balancer.

          - *(dict) --*

            The ID of an EC2 instance.

            - **InstanceId** *(string) --*

              The instance ID.

        - **HealthCheck** *(dict) --*

          Information about the health checks conducted on the load balancer.

          - **Target** *(string) --*

            The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range
            of valid ports is one (1) through 65535.

            TCP is the default, specified as a TCP: port pair, for example "TCP:5000". In this
            case, a health check simply attempts to open a TCP connection to the instance on the
            specified port. Failure to connect within the configured timeout is considered
            unhealthy.

            SSL is also specified as SSL: port pair, for example, SSL:5000.

            For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a
            HTTP:port;/;PathToPing; grouping, for example "HTTP:80/weather/us/wa/seattle". In this
            case, a HTTP GET request is issued to the instance on the given port and path. Any
            answer other than "200 OK" within the timeout period is considered unhealthy.

            The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.

          - **Interval** *(integer) --*

            The approximate interval, in seconds, between health checks of an individual instance.

          - **Timeout** *(integer) --*

            The amount of time, in seconds, during which no response means a failed health check.

            This value must be less than the ``Interval`` value.

          - **UnhealthyThreshold** *(integer) --*

            The number of consecutive health check failures required before moving the instance to
            the ``Unhealthy`` state.

          - **HealthyThreshold** *(integer) --*

            The number of consecutive health checks successes required before moving the instance
            to the ``Healthy`` state.

        - **SourceSecurityGroup** *(dict) --*

          The security group for the load balancer, which you can use as part of your inbound rules
          for your registered instances. To only allow traffic from load balancers, add a security
          group rule that specifies this source security group as the inbound source.

          - **OwnerAlias** *(string) --*

            The owner of the security group.

          - **GroupName** *(string) --*

            The name of the security group.

        - **SecurityGroups** *(list) --*

          The security groups for the load balancer. Valid only for load balancers in a VPC.

          - *(string) --*

        - **CreatedTime** *(datetime) --*

          The date and time the load balancer was created.

        - **Scheme** *(string) --*

          The type of load balancer. Valid only for load balancers in a VPC.

          If ``Scheme`` is ``internet-facing`` , the load balancer has a public DNS name that
          resolves to a public IP address.

          If ``Scheme`` is ``internal`` , the load balancer has a public DNS name that resolves to
          a private IP address.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_InstanceDeregisteredWaitInstancesTypeDef = TypedDict(
    "_InstanceDeregisteredWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class InstanceDeregisteredWaitInstancesTypeDef(
    _InstanceDeregisteredWaitInstancesTypeDef
):
    """
    Type definition for `InstanceDeregisteredWait` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_InstanceDeregisteredWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceDeregisteredWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceDeregisteredWaitWaiterConfigTypeDef(
    _InstanceDeregisteredWaitWaiterConfigTypeDef
):
    """
    Type definition for `InstanceDeregisteredWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """


_InstanceInServiceWaitInstancesTypeDef = TypedDict(
    "_InstanceInServiceWaitInstancesTypeDef", {"InstanceId": str}, total=False
)


class InstanceInServiceWaitInstancesTypeDef(_InstanceInServiceWaitInstancesTypeDef):
    """
    Type definition for `InstanceInServiceWait` `Instances`

    The ID of an EC2 instance.

    - **InstanceId** *(string) --*

      The instance ID.
    """


_InstanceInServiceWaitWaiterConfigTypeDef = TypedDict(
    "_InstanceInServiceWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InstanceInServiceWaitWaiterConfigTypeDef(
    _InstanceInServiceWaitWaiterConfigTypeDef
):
    """
    Type definition for `InstanceInServiceWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 15

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 40
    """
