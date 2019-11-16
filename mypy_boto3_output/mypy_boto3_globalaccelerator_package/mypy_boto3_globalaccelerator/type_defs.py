"Main interface for globalaccelerator type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientCreateAcceleratorResponseAcceleratorTypeDef",
    "ClientCreateAcceleratorResponseTypeDef",
    "ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientCreateEndpointGroupResponseTypeDef",
    "ClientCreateListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerPortRangesTypeDef",
    "ClientCreateListenerResponseListenerTypeDef",
    "ClientCreateListenerResponseTypeDef",
    "ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientDescribeAcceleratorAttributesResponseTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    "ClientDescribeAcceleratorResponseTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    "ClientDescribeEndpointGroupResponseTypeDef",
    "ClientDescribeListenerResponseListenerPortRangesTypeDef",
    "ClientDescribeListenerResponseListenerTypeDef",
    "ClientDescribeListenerResponseTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    "ClientListAcceleratorsResponseAcceleratorsTypeDef",
    "ClientListAcceleratorsResponseTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    "ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    "ClientListEndpointGroupsResponseTypeDef",
    "ClientListListenersResponseListenersPortRangesTypeDef",
    "ClientListListenersResponseListenersTypeDef",
    "ClientListListenersResponseTypeDef",
    "ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    "ClientUpdateAcceleratorAttributesResponseTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    "ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    "ClientUpdateAcceleratorResponseTypeDef",
    "ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    "ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    "ClientUpdateEndpointGroupResponseTypeDef",
    "ClientUpdateListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerPortRangesTypeDef",
    "ClientUpdateListenerResponseListenerTypeDef",
    "ClientUpdateListenerResponseTypeDef",
    "ListAcceleratorsPaginatePaginationConfigTypeDef",
    "ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef",
    "ListAcceleratorsPaginateResponseAcceleratorsTypeDef",
    "ListAcceleratorsPaginateResponseTypeDef",
    "ListEndpointGroupsPaginatePaginationConfigTypeDef",
    "ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef",
    "ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef",
    "ListEndpointGroupsPaginateResponseTypeDef",
    "ListListenersPaginatePaginationConfigTypeDef",
    "ListListenersPaginateResponseListenersPortRangesTypeDef",
    "ListListenersPaginateResponseListenersTypeDef",
    "ListListenersPaginateResponseTypeDef",
)


_ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef
):
    """
    Type definition for `ClientCreateAcceleratorResponseAccelerator` `IpSets`

    A complex type for the set of IP addresses for an accelerator.

    - **IpFamily** *(string) --*

      The types of IP addresses included in this IP set.

    - **IpAddresses** *(list) --*

      The array of IP addresses in the IP address set. An IP address set can have a maximum
      of two IP addresses.

      - *(string) --*
    """


_ClientCreateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientCreateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientCreateAcceleratorResponseAcceleratorTypeDef(
    _ClientCreateAcceleratorResponseAcceleratorTypeDef
):
    """
    Type definition for `ClientCreateAcceleratorResponse` `Accelerator`

    The accelerator that is created by specifying a listener and the supported IP address types.

    - **AcceleratorArn** *(string) --*

      The Amazon Resource Name (ARN) of the accelerator.

    - **Name** *(string) --*

      The name of the accelerator. The name must contain only alphanumeric characters or hyphens
      (-), and must not begin or end with a hyphen.

    - **IpAddressType** *(string) --*

      The value for the address type must be IPv4.

    - **Enabled** *(boolean) --*

      Indicates whether the accelerator is enabled. The value is true or false. The default value
      is true.

      If the value is set to true, the accelerator cannot be deleted. If set to false,
      accelerator can be deleted.

    - **IpSets** *(list) --*

      The static IP addresses that Global Accelerator associates with the accelerator.

      - *(dict) --*

        A complex type for the set of IP addresses for an accelerator.

        - **IpFamily** *(string) --*

          The types of IP addresses included in this IP set.

        - **IpAddresses** *(list) --*

          The array of IP addresses in the IP address set. An IP address set can have a maximum
          of two IP addresses.

          - *(string) --*

    - **DnsName** *(string) --*

      The Domain Name System (DNS) name that Global Accelerator creates that points to your
      accelerator's static IP addresses.

      The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
      random hex string, followed by .awsglobalaccelerator.com. For example:
      a1234567890abcdef.awsglobalaccelerator.com.

      For more information about the default DNS name, see `Support for DNS Addressing in Global
      Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **Status** *(string) --*

      Describes the deployment status of the accelerator.

    - **CreatedTime** *(datetime) --*

      The date and time that the accelerator was created.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the accelerator was last modified.
    """


_ClientCreateAcceleratorResponseTypeDef = TypedDict(
    "_ClientCreateAcceleratorResponseTypeDef",
    {"Accelerator": ClientCreateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientCreateAcceleratorResponseTypeDef(_ClientCreateAcceleratorResponseTypeDef):
    """
    Type definition for `ClientCreateAccelerator` `Response`

    - **Accelerator** *(dict) --*

      The accelerator that is created by specifying a listener and the supported IP address types.

      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.

      - **Name** *(string) --*

        The name of the accelerator. The name must contain only alphanumeric characters or hyphens
        (-), and must not begin or end with a hyphen.

      - **IpAddressType** *(string) --*

        The value for the address type must be IPv4.

      - **Enabled** *(boolean) --*

        Indicates whether the accelerator is enabled. The value is true or false. The default value
        is true.

        If the value is set to true, the accelerator cannot be deleted. If set to false,
        accelerator can be deleted.

      - **IpSets** *(list) --*

        The static IP addresses that Global Accelerator associates with the accelerator.

        - *(dict) --*

          A complex type for the set of IP addresses for an accelerator.

          - **IpFamily** *(string) --*

            The types of IP addresses included in this IP set.

          - **IpAddresses** *(list) --*

            The array of IP addresses in the IP address set. An IP address set can have a maximum
            of two IP addresses.

            - *(string) --*

      - **DnsName** *(string) --*

        The Domain Name System (DNS) name that Global Accelerator creates that points to your
        accelerator's static IP addresses.

        The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
        random hex string, followed by .awsglobalaccelerator.com. For example:
        a1234567890abcdef.awsglobalaccelerator.com.

        For more information about the default DNS name, see `Support for DNS Addressing in Global
        Accelerator
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
        in the *AWS Global Accelerator Developer Guide* .

      - **Status** *(string) --*

        Describes the deployment status of the accelerator.

      - **CreatedTime** *(datetime) --*

        The date and time that the accelerator was created.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the accelerator was last modified.
    """


_ClientCreateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "_ClientCreateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)


class ClientCreateEndpointGroupEndpointConfigurationsTypeDef(
    _ClientCreateEndpointGroupEndpointConfigurationsTypeDef
):
    """
    Type definition for `ClientCreateEndpointGroup` `EndpointConfigurations`

    A complex type for endpoints.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
      Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
      Elastic IP address, this is the Elastic IP address allocation ID.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you configure AWS
      Global Accelerator to route traffic based on proportions that you specify. For example, you
      might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your
      traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and
      third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint
      Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load Balancer
      endpoint. The value is true or false. The default value is true for new accelerators.

      If the value is set to true, the client's IP address is preserved in the ``X-Forwarded-For``
      request header as traffic travels to applications on the Application Load Balancer endpoint
      fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": str,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    """
    Type definition for `ClientCreateEndpointGroupResponseEndpointGroup` `EndpointDescriptions`

    A complex type for an endpoint. Each endpoint group can include one or more endpoints,
    such as load balancers.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
      Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
      Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
      Balancer can be either internal or internet-facing.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you
      configure AWS Global Accelerator to route traffic based on proportions that you
      specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
      The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
      5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
      endpoint. For more information, see `Endpoint Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **HealthState** *(string) --*

      The health status of the endpoint.

    - **HealthReason** *(string) --*

      The reason code associated with why the endpoint is not healthy. If the endpoint state
      is healthy, a reason code is not provided.

      If the endpoint state is **unhealthy** , the reason code can be one of the following
      values:

      * **Timeout** : The health check requests to the endpoint are timing out before
      returning a status.

      * **Failed** : The health check failed, for example because the endpoint response was
      invalid (malformed).

      If the endpoint state is **initial** , the reason code can be one of the following
      values:

      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
      of health checks for the endpoint that are required to determine its health status.

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load
      Balancer endpoint. The value is true or false. The default value is true for new
      accelerators.

      If the value is set to true, the client's IP address is preserved in the
      ``X-Forwarded-For`` request header as traffic travels to applications on the
      Application Load Balancer endpoint fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientCreateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientCreateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": str,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientCreateEndpointGroupResponseEndpointGroupTypeDef(
    _ClientCreateEndpointGroupResponseEndpointGroupTypeDef
):
    """
    Type definition for `ClientCreateEndpointGroupResponse` `EndpointGroup`

    The information about the endpoint group that was created.

    - **EndpointGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the endpoint group.

    - **EndpointGroupRegion** *(string) --*

      The AWS Region that this endpoint group belongs.

    - **EndpointDescriptions** *(list) --*

      The list of endpoint objects.

      - *(dict) --*

        A complex type for an endpoint. Each endpoint group can include one or more endpoints,
        such as load balancers.

        - **EndpointId** *(string) --*

          An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
          Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
          Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
          Balancer can be either internal or internet-facing.

        - **Weight** *(integer) --*

          The weight associated with the endpoint. When you add weights to endpoints, you
          configure AWS Global Accelerator to route traffic based on proportions that you
          specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
          The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
          5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
          endpoint. For more information, see `Endpoint Weights
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **HealthState** *(string) --*

          The health status of the endpoint.

        - **HealthReason** *(string) --*

          The reason code associated with why the endpoint is not healthy. If the endpoint state
          is healthy, a reason code is not provided.

          If the endpoint state is **unhealthy** , the reason code can be one of the following
          values:

          * **Timeout** : The health check requests to the endpoint are timing out before
          returning a status.

          * **Failed** : The health check failed, for example because the endpoint response was
          invalid (malformed).

          If the endpoint state is **initial** , the reason code can be one of the following
          values:

          * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

          * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
          of health checks for the endpoint that are required to determine its health status.

        - **ClientIPPreservationEnabled** *(boolean) --*

          Indicates whether client IP address preservation is enabled for an Application Load
          Balancer endpoint. The value is true or false. The default value is true for new
          accelerators.

          If the value is set to true, the client's IP address is preserved in the
          ``X-Forwarded-For`` request header as traffic travels to applications on the
          Application Load Balancer endpoint fronted by the accelerator.

          For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
          in the *AWS Global Accelerator Developer Guide* .

    - **TrafficDialPercentage** *(float) --*

      The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
      other endpoint groups for this listener.

      Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
      The percentage is applied to the traffic that would otherwise have been routed to the
      Region based on optimal routing.

      The default value is 100.

    - **HealthCheckPort** *(integer) --*

      The port that Global Accelerator uses to perform health checks on endpoints that are part
      of this endpoint group.

      The default port is the port for the listener that this endpoint group is associated with.
      If the listener port is a list, Global Accelerator uses the first specified port in the
      list of ports.

    - **HealthCheckProtocol** *(string) --*

      The protocol that Global Accelerator uses to perform health checks on endpoints that are
      part of this endpoint group. The default value is TCP.

    - **HealthCheckPath** *(string) --*

      If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
      uses for the destination on the endpoints for health checks. The default is slash (/).

    - **HealthCheckIntervalSeconds** *(integer) --*

      The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
      value is 30.

    - **ThresholdCount** *(integer) --*

      The number of consecutive health checks required to set the state of a healthy endpoint to
      unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientCreateEndpointGroupResponseTypeDef = TypedDict(
    "_ClientCreateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientCreateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientCreateEndpointGroupResponseTypeDef(
    _ClientCreateEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateEndpointGroup` `Response`

    - **EndpointGroup** *(dict) --*

      The information about the endpoint group that was created.

      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.

      - **EndpointGroupRegion** *(string) --*

        The AWS Region that this endpoint group belongs.

      - **EndpointDescriptions** *(list) --*

        The list of endpoint objects.

        - *(dict) --*

          A complex type for an endpoint. Each endpoint group can include one or more endpoints,
          such as load balancers.

          - **EndpointId** *(string) --*

            An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
            Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
            Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
            Balancer can be either internal or internet-facing.

          - **Weight** *(integer) --*

            The weight associated with the endpoint. When you add weights to endpoints, you
            configure AWS Global Accelerator to route traffic based on proportions that you
            specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
            The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
            5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
            endpoint. For more information, see `Endpoint Weights
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
            in the *AWS Global Accelerator Developer Guide* .

          - **HealthState** *(string) --*

            The health status of the endpoint.

          - **HealthReason** *(string) --*

            The reason code associated with why the endpoint is not healthy. If the endpoint state
            is healthy, a reason code is not provided.

            If the endpoint state is **unhealthy** , the reason code can be one of the following
            values:

            * **Timeout** : The health check requests to the endpoint are timing out before
            returning a status.

            * **Failed** : The health check failed, for example because the endpoint response was
            invalid (malformed).

            If the endpoint state is **initial** , the reason code can be one of the following
            values:

            * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

            * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
            of health checks for the endpoint that are required to determine its health status.

          - **ClientIPPreservationEnabled** *(boolean) --*

            Indicates whether client IP address preservation is enabled for an Application Load
            Balancer endpoint. The value is true or false. The default value is true for new
            accelerators.

            If the value is set to true, the client's IP address is preserved in the
            ``X-Forwarded-For`` request header as traffic travels to applications on the
            Application Load Balancer endpoint fronted by the accelerator.

            For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
            in the *AWS Global Accelerator Developer Guide* .

      - **TrafficDialPercentage** *(float) --*

        The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
        other endpoint groups for this listener.

        Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
        The percentage is applied to the traffic that would otherwise have been routed to the
        Region based on optimal routing.

        The default value is 100.

      - **HealthCheckPort** *(integer) --*

        The port that Global Accelerator uses to perform health checks on endpoints that are part
        of this endpoint group.

        The default port is the port for the listener that this endpoint group is associated with.
        If the listener port is a list, Global Accelerator uses the first specified port in the
        list of ports.

      - **HealthCheckProtocol** *(string) --*

        The protocol that Global Accelerator uses to perform health checks on endpoints that are
        part of this endpoint group. The default value is TCP.

      - **HealthCheckPath** *(string) --*

        If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
        uses for the destination on the endpoints for health checks. The default is slash (/).

      - **HealthCheckIntervalSeconds** *(integer) --*

        The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
        value is 30.

      - **ThresholdCount** *(integer) --*

        The number of consecutive health checks required to set the state of a healthy endpoint to
        unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientCreateListenerPortRangesTypeDef = TypedDict(
    "_ClientCreateListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientCreateListenerPortRangesTypeDef(_ClientCreateListenerPortRangesTypeDef):
    """
    Type definition for `ClientCreateListener` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientCreateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientCreateListenerResponseListenerPortRangesTypeDef(
    _ClientCreateListenerResponseListenerPortRangesTypeDef
):
    """
    Type definition for `ClientCreateListenerResponseListener` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientCreateListenerResponseListenerTypeDef = TypedDict(
    "_ClientCreateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientCreateListenerResponseListenerPortRangesTypeDef],
        "Protocol": str,
        "ClientAffinity": str,
    },
    total=False,
)


class ClientCreateListenerResponseListenerTypeDef(
    _ClientCreateListenerResponseListenerTypeDef
):
    """
    Type definition for `ClientCreateListenerResponse` `Listener`

    The listener that you've created.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **PortRanges** *(list) --*

      The list of port ranges for the connections from clients to the accelerator.

      - *(dict) --*

        A complex type for a range of ports for a listener.

        - **FromPort** *(integer) --*

          The first port in the range of ports, inclusive.

        - **ToPort** *(integer) --*

          The last port in the range of ports, inclusive.

    - **Protocol** *(string) --*

      The protocol for the connections from clients to the accelerator.

    - **ClientAffinity** *(string) --*

      Client affinity lets you direct all requests from a user to the same endpoint, if you have
      stateful applications, regardless of the port and protocol of the client request. Clienty
      affinity gives you control over whether to always route each client to the same specific
      endpoint.

      AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
      endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
      "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
      destination port, and protocol—to select the hash value, and then chooses the best
      endpoint. However, with this setting, if someone uses different ports to connect to Global
      Accelerator, their connections might not be always routed to the same endpoint because the
      hash value changes.

      If you want a given client to always be routed to the same endpoint, set client affinity to
      ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
      "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
      select the hash value.

      The default value is ``NONE`` .
    """


_ClientCreateListenerResponseTypeDef = TypedDict(
    "_ClientCreateListenerResponseTypeDef",
    {"Listener": ClientCreateListenerResponseListenerTypeDef},
    total=False,
)


class ClientCreateListenerResponseTypeDef(_ClientCreateListenerResponseTypeDef):
    """
    Type definition for `ClientCreateListener` `Response`

    - **Listener** *(dict) --*

      The listener that you've created.

      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.

      - **PortRanges** *(list) --*

        The list of port ranges for the connections from clients to the accelerator.

        - *(dict) --*

          A complex type for a range of ports for a listener.

          - **FromPort** *(integer) --*

            The first port in the range of ports, inclusive.

          - **ToPort** *(integer) --*

            The last port in the range of ports, inclusive.

      - **Protocol** *(string) --*

        The protocol for the connections from clients to the accelerator.

      - **ClientAffinity** *(string) --*

        Client affinity lets you direct all requests from a user to the same endpoint, if you have
        stateful applications, regardless of the port and protocol of the client request. Clienty
        affinity gives you control over whether to always route each client to the same specific
        endpoint.

        AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
        endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
        "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
        destination port, and protocol—to select the hash value, and then chooses the best
        endpoint. However, with this setting, if someone uses different ports to connect to Global
        Accelerator, their connections might not be always routed to the same endpoint because the
        hash value changes.

        If you want a given client to always be routed to the same endpoint, set client affinity to
        ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
        "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
        select the hash value.

        The default value is ``NONE`` .
    """


_ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "_ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)


class ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef(
    _ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef
):
    """
    Type definition for `ClientDescribeAcceleratorAttributesResponse` `AcceleratorAttributes`

    The attributes of the accelerator.

    - **FlowLogsEnabled** *(boolean) --*

      Indicates whether flow logs are enabled. The default value is false. If the value is true,
      ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.

      For more information, see `Flow Logs
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **FlowLogsS3Bucket** *(string) --*

      The name of the Amazon S3 bucket for the flow logs. Attribute is required if
      ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that
      grants AWS Global Accelerator permission to write to the bucket.

    - **FlowLogsS3Prefix** *(string) --*

      The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is
      required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs
      are stored in the root of the bucket.
    """


_ClientDescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientDescribeAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)


class ClientDescribeAcceleratorAttributesResponseTypeDef(
    _ClientDescribeAcceleratorAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAcceleratorAttributes` `Response`

    - **AcceleratorAttributes** *(dict) --*

      The attributes of the accelerator.

      - **FlowLogsEnabled** *(boolean) --*

        Indicates whether flow logs are enabled. The default value is false. If the value is true,
        ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.

        For more information, see `Flow Logs
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
        in the *AWS Global Accelerator Developer Guide* .

      - **FlowLogsS3Bucket** *(string) --*

        The name of the Amazon S3 bucket for the flow logs. Attribute is required if
        ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that
        grants AWS Global Accelerator permission to write to the bucket.

      - **FlowLogsS3Prefix** *(string) --*

        The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is
        required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs
        are stored in the root of the bucket.
    """


_ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef
):
    """
    Type definition for `ClientDescribeAcceleratorResponseAccelerator` `IpSets`

    A complex type for the set of IP addresses for an accelerator.

    - **IpFamily** *(string) --*

      The types of IP addresses included in this IP set.

    - **IpAddresses** *(list) --*

      The array of IP addresses in the IP address set. An IP address set can have a maximum
      of two IP addresses.

      - *(string) --*
    """


_ClientDescribeAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientDescribeAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientDescribeAcceleratorResponseAcceleratorTypeDef(
    _ClientDescribeAcceleratorResponseAcceleratorTypeDef
):
    """
    Type definition for `ClientDescribeAcceleratorResponse` `Accelerator`

    The description of the accelerator.

    - **AcceleratorArn** *(string) --*

      The Amazon Resource Name (ARN) of the accelerator.

    - **Name** *(string) --*

      The name of the accelerator. The name must contain only alphanumeric characters or hyphens
      (-), and must not begin or end with a hyphen.

    - **IpAddressType** *(string) --*

      The value for the address type must be IPv4.

    - **Enabled** *(boolean) --*

      Indicates whether the accelerator is enabled. The value is true or false. The default value
      is true.

      If the value is set to true, the accelerator cannot be deleted. If set to false,
      accelerator can be deleted.

    - **IpSets** *(list) --*

      The static IP addresses that Global Accelerator associates with the accelerator.

      - *(dict) --*

        A complex type for the set of IP addresses for an accelerator.

        - **IpFamily** *(string) --*

          The types of IP addresses included in this IP set.

        - **IpAddresses** *(list) --*

          The array of IP addresses in the IP address set. An IP address set can have a maximum
          of two IP addresses.

          - *(string) --*

    - **DnsName** *(string) --*

      The Domain Name System (DNS) name that Global Accelerator creates that points to your
      accelerator's static IP addresses.

      The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
      random hex string, followed by .awsglobalaccelerator.com. For example:
      a1234567890abcdef.awsglobalaccelerator.com.

      For more information about the default DNS name, see `Support for DNS Addressing in Global
      Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **Status** *(string) --*

      Describes the deployment status of the accelerator.

    - **CreatedTime** *(datetime) --*

      The date and time that the accelerator was created.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the accelerator was last modified.
    """


_ClientDescribeAcceleratorResponseTypeDef = TypedDict(
    "_ClientDescribeAcceleratorResponseTypeDef",
    {"Accelerator": ClientDescribeAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientDescribeAcceleratorResponseTypeDef(
    _ClientDescribeAcceleratorResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccelerator` `Response`

    - **Accelerator** *(dict) --*

      The description of the accelerator.

      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.

      - **Name** *(string) --*

        The name of the accelerator. The name must contain only alphanumeric characters or hyphens
        (-), and must not begin or end with a hyphen.

      - **IpAddressType** *(string) --*

        The value for the address type must be IPv4.

      - **Enabled** *(boolean) --*

        Indicates whether the accelerator is enabled. The value is true or false. The default value
        is true.

        If the value is set to true, the accelerator cannot be deleted. If set to false,
        accelerator can be deleted.

      - **IpSets** *(list) --*

        The static IP addresses that Global Accelerator associates with the accelerator.

        - *(dict) --*

          A complex type for the set of IP addresses for an accelerator.

          - **IpFamily** *(string) --*

            The types of IP addresses included in this IP set.

          - **IpAddresses** *(list) --*

            The array of IP addresses in the IP address set. An IP address set can have a maximum
            of two IP addresses.

            - *(string) --*

      - **DnsName** *(string) --*

        The Domain Name System (DNS) name that Global Accelerator creates that points to your
        accelerator's static IP addresses.

        The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
        random hex string, followed by .awsglobalaccelerator.com. For example:
        a1234567890abcdef.awsglobalaccelerator.com.

        For more information about the default DNS name, see `Support for DNS Addressing in Global
        Accelerator
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
        in the *AWS Global Accelerator Developer Guide* .

      - **Status** *(string) --*

        Describes the deployment status of the accelerator.

      - **CreatedTime** *(datetime) --*

        The date and time that the accelerator was created.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the accelerator was last modified.
    """


_ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": str,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    """
    Type definition for `ClientDescribeEndpointGroupResponseEndpointGroup` `EndpointDescriptions`

    A complex type for an endpoint. Each endpoint group can include one or more endpoints,
    such as load balancers.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
      Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
      Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
      Balancer can be either internal or internet-facing.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you
      configure AWS Global Accelerator to route traffic based on proportions that you
      specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
      The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
      5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
      endpoint. For more information, see `Endpoint Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **HealthState** *(string) --*

      The health status of the endpoint.

    - **HealthReason** *(string) --*

      The reason code associated with why the endpoint is not healthy. If the endpoint state
      is healthy, a reason code is not provided.

      If the endpoint state is **unhealthy** , the reason code can be one of the following
      values:

      * **Timeout** : The health check requests to the endpoint are timing out before
      returning a status.

      * **Failed** : The health check failed, for example because the endpoint response was
      invalid (malformed).

      If the endpoint state is **initial** , the reason code can be one of the following
      values:

      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
      of health checks for the endpoint that are required to determine its health status.

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load
      Balancer endpoint. The value is true or false. The default value is true for new
      accelerators.

      If the value is set to true, the client's IP address is preserved in the
      ``X-Forwarded-For`` request header as traffic travels to applications on the
      Application Load Balancer endpoint fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientDescribeEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientDescribeEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": str,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientDescribeEndpointGroupResponseEndpointGroupTypeDef(
    _ClientDescribeEndpointGroupResponseEndpointGroupTypeDef
):
    """
    Type definition for `ClientDescribeEndpointGroupResponse` `EndpointGroup`

    The description of an endpoint group.

    - **EndpointGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the endpoint group.

    - **EndpointGroupRegion** *(string) --*

      The AWS Region that this endpoint group belongs.

    - **EndpointDescriptions** *(list) --*

      The list of endpoint objects.

      - *(dict) --*

        A complex type for an endpoint. Each endpoint group can include one or more endpoints,
        such as load balancers.

        - **EndpointId** *(string) --*

          An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
          Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
          Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
          Balancer can be either internal or internet-facing.

        - **Weight** *(integer) --*

          The weight associated with the endpoint. When you add weights to endpoints, you
          configure AWS Global Accelerator to route traffic based on proportions that you
          specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
          The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
          5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
          endpoint. For more information, see `Endpoint Weights
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **HealthState** *(string) --*

          The health status of the endpoint.

        - **HealthReason** *(string) --*

          The reason code associated with why the endpoint is not healthy. If the endpoint state
          is healthy, a reason code is not provided.

          If the endpoint state is **unhealthy** , the reason code can be one of the following
          values:

          * **Timeout** : The health check requests to the endpoint are timing out before
          returning a status.

          * **Failed** : The health check failed, for example because the endpoint response was
          invalid (malformed).

          If the endpoint state is **initial** , the reason code can be one of the following
          values:

          * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

          * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
          of health checks for the endpoint that are required to determine its health status.

        - **ClientIPPreservationEnabled** *(boolean) --*

          Indicates whether client IP address preservation is enabled for an Application Load
          Balancer endpoint. The value is true or false. The default value is true for new
          accelerators.

          If the value is set to true, the client's IP address is preserved in the
          ``X-Forwarded-For`` request header as traffic travels to applications on the
          Application Load Balancer endpoint fronted by the accelerator.

          For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
          in the *AWS Global Accelerator Developer Guide* .

    - **TrafficDialPercentage** *(float) --*

      The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
      other endpoint groups for this listener.

      Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
      The percentage is applied to the traffic that would otherwise have been routed to the
      Region based on optimal routing.

      The default value is 100.

    - **HealthCheckPort** *(integer) --*

      The port that Global Accelerator uses to perform health checks on endpoints that are part
      of this endpoint group.

      The default port is the port for the listener that this endpoint group is associated with.
      If the listener port is a list, Global Accelerator uses the first specified port in the
      list of ports.

    - **HealthCheckProtocol** *(string) --*

      The protocol that Global Accelerator uses to perform health checks on endpoints that are
      part of this endpoint group. The default value is TCP.

    - **HealthCheckPath** *(string) --*

      If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
      uses for the destination on the endpoints for health checks. The default is slash (/).

    - **HealthCheckIntervalSeconds** *(integer) --*

      The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
      value is 30.

    - **ThresholdCount** *(integer) --*

      The number of consecutive health checks required to set the state of a healthy endpoint to
      unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientDescribeEndpointGroupResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientDescribeEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientDescribeEndpointGroupResponseTypeDef(
    _ClientDescribeEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientDescribeEndpointGroup` `Response`

    - **EndpointGroup** *(dict) --*

      The description of an endpoint group.

      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.

      - **EndpointGroupRegion** *(string) --*

        The AWS Region that this endpoint group belongs.

      - **EndpointDescriptions** *(list) --*

        The list of endpoint objects.

        - *(dict) --*

          A complex type for an endpoint. Each endpoint group can include one or more endpoints,
          such as load balancers.

          - **EndpointId** *(string) --*

            An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
            Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
            Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
            Balancer can be either internal or internet-facing.

          - **Weight** *(integer) --*

            The weight associated with the endpoint. When you add weights to endpoints, you
            configure AWS Global Accelerator to route traffic based on proportions that you
            specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
            The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
            5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
            endpoint. For more information, see `Endpoint Weights
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
            in the *AWS Global Accelerator Developer Guide* .

          - **HealthState** *(string) --*

            The health status of the endpoint.

          - **HealthReason** *(string) --*

            The reason code associated with why the endpoint is not healthy. If the endpoint state
            is healthy, a reason code is not provided.

            If the endpoint state is **unhealthy** , the reason code can be one of the following
            values:

            * **Timeout** : The health check requests to the endpoint are timing out before
            returning a status.

            * **Failed** : The health check failed, for example because the endpoint response was
            invalid (malformed).

            If the endpoint state is **initial** , the reason code can be one of the following
            values:

            * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

            * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
            of health checks for the endpoint that are required to determine its health status.

          - **ClientIPPreservationEnabled** *(boolean) --*

            Indicates whether client IP address preservation is enabled for an Application Load
            Balancer endpoint. The value is true or false. The default value is true for new
            accelerators.

            If the value is set to true, the client's IP address is preserved in the
            ``X-Forwarded-For`` request header as traffic travels to applications on the
            Application Load Balancer endpoint fronted by the accelerator.

            For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
            in the *AWS Global Accelerator Developer Guide* .

      - **TrafficDialPercentage** *(float) --*

        The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
        other endpoint groups for this listener.

        Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
        The percentage is applied to the traffic that would otherwise have been routed to the
        Region based on optimal routing.

        The default value is 100.

      - **HealthCheckPort** *(integer) --*

        The port that Global Accelerator uses to perform health checks on endpoints that are part
        of this endpoint group.

        The default port is the port for the listener that this endpoint group is associated with.
        If the listener port is a list, Global Accelerator uses the first specified port in the
        list of ports.

      - **HealthCheckProtocol** *(string) --*

        The protocol that Global Accelerator uses to perform health checks on endpoints that are
        part of this endpoint group. The default value is TCP.

      - **HealthCheckPath** *(string) --*

        If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
        uses for the destination on the endpoints for health checks. The default is slash (/).

      - **HealthCheckIntervalSeconds** *(integer) --*

        The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
        value is 30.

      - **ThresholdCount** *(integer) --*

        The number of consecutive health checks required to set the state of a healthy endpoint to
        unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientDescribeListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientDescribeListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientDescribeListenerResponseListenerPortRangesTypeDef(
    _ClientDescribeListenerResponseListenerPortRangesTypeDef
):
    """
    Type definition for `ClientDescribeListenerResponseListener` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientDescribeListenerResponseListenerTypeDef = TypedDict(
    "_ClientDescribeListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientDescribeListenerResponseListenerPortRangesTypeDef],
        "Protocol": str,
        "ClientAffinity": str,
    },
    total=False,
)


class ClientDescribeListenerResponseListenerTypeDef(
    _ClientDescribeListenerResponseListenerTypeDef
):
    """
    Type definition for `ClientDescribeListenerResponse` `Listener`

    The description of a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **PortRanges** *(list) --*

      The list of port ranges for the connections from clients to the accelerator.

      - *(dict) --*

        A complex type for a range of ports for a listener.

        - **FromPort** *(integer) --*

          The first port in the range of ports, inclusive.

        - **ToPort** *(integer) --*

          The last port in the range of ports, inclusive.

    - **Protocol** *(string) --*

      The protocol for the connections from clients to the accelerator.

    - **ClientAffinity** *(string) --*

      Client affinity lets you direct all requests from a user to the same endpoint, if you have
      stateful applications, regardless of the port and protocol of the client request. Clienty
      affinity gives you control over whether to always route each client to the same specific
      endpoint.

      AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
      endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
      "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
      destination port, and protocol—to select the hash value, and then chooses the best
      endpoint. However, with this setting, if someone uses different ports to connect to Global
      Accelerator, their connections might not be always routed to the same endpoint because the
      hash value changes.

      If you want a given client to always be routed to the same endpoint, set client affinity to
      ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
      "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
      select the hash value.

      The default value is ``NONE`` .
    """


_ClientDescribeListenerResponseTypeDef = TypedDict(
    "_ClientDescribeListenerResponseTypeDef",
    {"Listener": ClientDescribeListenerResponseListenerTypeDef},
    total=False,
)


class ClientDescribeListenerResponseTypeDef(_ClientDescribeListenerResponseTypeDef):
    """
    Type definition for `ClientDescribeListener` `Response`

    - **Listener** *(dict) --*

      The description of a listener.

      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.

      - **PortRanges** *(list) --*

        The list of port ranges for the connections from clients to the accelerator.

        - *(dict) --*

          A complex type for a range of ports for a listener.

          - **FromPort** *(integer) --*

            The first port in the range of ports, inclusive.

          - **ToPort** *(integer) --*

            The last port in the range of ports, inclusive.

      - **Protocol** *(string) --*

        The protocol for the connections from clients to the accelerator.

      - **ClientAffinity** *(string) --*

        Client affinity lets you direct all requests from a user to the same endpoint, if you have
        stateful applications, regardless of the port and protocol of the client request. Clienty
        affinity gives you control over whether to always route each client to the same specific
        endpoint.

        AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
        endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
        "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
        destination port, and protocol—to select the hash value, and then chooses the best
        endpoint. However, with this setting, if someone uses different ports to connect to Global
        Accelerator, their connections might not be always routed to the same endpoint because the
        hash value changes.

        If you want a given client to always be routed to the same endpoint, set client affinity to
        ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
        "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
        select the hash value.

        The default value is ``NONE`` .
    """


_ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef(
    _ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef
):
    """
    Type definition for `ClientListAcceleratorsResponseAccelerators` `IpSets`

    A complex type for the set of IP addresses for an accelerator.

    - **IpFamily** *(string) --*

      The types of IP addresses included in this IP set.

    - **IpAddresses** *(list) --*

      The array of IP addresses in the IP address set. An IP address set can have a maximum
      of two IP addresses.

      - *(string) --*
    """


_ClientListAcceleratorsResponseAcceleratorsTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseAcceleratorsTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientListAcceleratorsResponseAcceleratorsIpSetsTypeDef],
        "DnsName": str,
        "Status": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientListAcceleratorsResponseAcceleratorsTypeDef(
    _ClientListAcceleratorsResponseAcceleratorsTypeDef
):
    """
    Type definition for `ClientListAcceleratorsResponse` `Accelerators`

    An accelerator is a complex type that includes one or more listeners that process inbound
    connections and then direct traffic to one or more endpoint groups, each of which includes
    endpoints, such as load balancers.

    - **AcceleratorArn** *(string) --*

      The Amazon Resource Name (ARN) of the accelerator.

    - **Name** *(string) --*

      The name of the accelerator. The name must contain only alphanumeric characters or
      hyphens (-), and must not begin or end with a hyphen.

    - **IpAddressType** *(string) --*

      The value for the address type must be IPv4.

    - **Enabled** *(boolean) --*

      Indicates whether the accelerator is enabled. The value is true or false. The default
      value is true.

      If the value is set to true, the accelerator cannot be deleted. If set to false,
      accelerator can be deleted.

    - **IpSets** *(list) --*

      The static IP addresses that Global Accelerator associates with the accelerator.

      - *(dict) --*

        A complex type for the set of IP addresses for an accelerator.

        - **IpFamily** *(string) --*

          The types of IP addresses included in this IP set.

        - **IpAddresses** *(list) --*

          The array of IP addresses in the IP address set. An IP address set can have a maximum
          of two IP addresses.

          - *(string) --*

    - **DnsName** *(string) --*

      The Domain Name System (DNS) name that Global Accelerator creates that points to your
      accelerator's static IP addresses.

      The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
      random hex string, followed by .awsglobalaccelerator.com. For example:
      a1234567890abcdef.awsglobalaccelerator.com.

      For more information about the default DNS name, see `Support for DNS Addressing in
      Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **Status** *(string) --*

      Describes the deployment status of the accelerator.

    - **CreatedTime** *(datetime) --*

      The date and time that the accelerator was created.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the accelerator was last modified.
    """


_ClientListAcceleratorsResponseTypeDef = TypedDict(
    "_ClientListAcceleratorsResponseTypeDef",
    {
        "Accelerators": List[ClientListAcceleratorsResponseAcceleratorsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListAcceleratorsResponseTypeDef(_ClientListAcceleratorsResponseTypeDef):
    """
    Type definition for `ClientListAccelerators` `Response`

    - **Accelerators** *(list) --*

      The list of accelerators for a customer account.

      - *(dict) --*

        An accelerator is a complex type that includes one or more listeners that process inbound
        connections and then direct traffic to one or more endpoint groups, each of which includes
        endpoints, such as load balancers.

        - **AcceleratorArn** *(string) --*

          The Amazon Resource Name (ARN) of the accelerator.

        - **Name** *(string) --*

          The name of the accelerator. The name must contain only alphanumeric characters or
          hyphens (-), and must not begin or end with a hyphen.

        - **IpAddressType** *(string) --*

          The value for the address type must be IPv4.

        - **Enabled** *(boolean) --*

          Indicates whether the accelerator is enabled. The value is true or false. The default
          value is true.

          If the value is set to true, the accelerator cannot be deleted. If set to false,
          accelerator can be deleted.

        - **IpSets** *(list) --*

          The static IP addresses that Global Accelerator associates with the accelerator.

          - *(dict) --*

            A complex type for the set of IP addresses for an accelerator.

            - **IpFamily** *(string) --*

              The types of IP addresses included in this IP set.

            - **IpAddresses** *(list) --*

              The array of IP addresses in the IP address set. An IP address set can have a maximum
              of two IP addresses.

              - *(string) --*

        - **DnsName** *(string) --*

          The Domain Name System (DNS) name that Global Accelerator creates that points to your
          accelerator's static IP addresses.

          The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
          random hex string, followed by .awsglobalaccelerator.com. For example:
          a1234567890abcdef.awsglobalaccelerator.com.

          For more information about the default DNS name, see `Support for DNS Addressing in
          Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **Status** *(string) --*

          Describes the deployment status of the accelerator.

        - **CreatedTime** *(datetime) --*

          The date and time that the accelerator was created.

        - **LastModifiedTime** *(datetime) --*

          The date and time that the accelerator was last modified.

    - **NextToken** *(string) --*

      The token for the next set of results. You receive this token from a previous call.
    """


_ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": str,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef(
    _ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef
):
    """
    Type definition for `ClientListEndpointGroupsResponseEndpointGroups` `EndpointDescriptions`

    A complex type for an endpoint. Each endpoint group can include one or more endpoints,
    such as load balancers.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
      Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
      endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
      Application Load Balancer can be either internal or internet-facing.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you
      configure AWS Global Accelerator to route traffic based on proportions that you
      specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
      The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
      5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
      endpoint. For more information, see `Endpoint Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **HealthState** *(string) --*

      The health status of the endpoint.

    - **HealthReason** *(string) --*

      The reason code associated with why the endpoint is not healthy. If the endpoint
      state is healthy, a reason code is not provided.

      If the endpoint state is **unhealthy** , the reason code can be one of the following
      values:

      * **Timeout** : The health check requests to the endpoint are timing out before
      returning a status.

      * **Failed** : The health check failed, for example because the endpoint response was
      invalid (malformed).

      If the endpoint state is **initial** , the reason code can be one of the following
      values:

      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
      number of health checks for the endpoint that are required to determine its health
      status.

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load
      Balancer endpoint. The value is true or false. The default value is true for new
      accelerators.

      If the value is set to true, the client's IP address is preserved in the
      ``X-Forwarded-For`` request header as traffic travels to applications on the
      Application Load Balancer endpoint fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientListEndpointGroupsResponseEndpointGroupsTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseEndpointGroupsTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientListEndpointGroupsResponseEndpointGroupsEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": str,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientListEndpointGroupsResponseEndpointGroupsTypeDef(
    _ClientListEndpointGroupsResponseEndpointGroupsTypeDef
):
    """
    Type definition for `ClientListEndpointGroupsResponse` `EndpointGroups`

    A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
    specific listener.

    - **EndpointGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the endpoint group.

    - **EndpointGroupRegion** *(string) --*

      The AWS Region that this endpoint group belongs.

    - **EndpointDescriptions** *(list) --*

      The list of endpoint objects.

      - *(dict) --*

        A complex type for an endpoint. Each endpoint group can include one or more endpoints,
        such as load balancers.

        - **EndpointId** *(string) --*

          An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
          Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
          endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
          Application Load Balancer can be either internal or internet-facing.

        - **Weight** *(integer) --*

          The weight associated with the endpoint. When you add weights to endpoints, you
          configure AWS Global Accelerator to route traffic based on proportions that you
          specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
          The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
          5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
          endpoint. For more information, see `Endpoint Weights
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **HealthState** *(string) --*

          The health status of the endpoint.

        - **HealthReason** *(string) --*

          The reason code associated with why the endpoint is not healthy. If the endpoint
          state is healthy, a reason code is not provided.

          If the endpoint state is **unhealthy** , the reason code can be one of the following
          values:

          * **Timeout** : The health check requests to the endpoint are timing out before
          returning a status.

          * **Failed** : The health check failed, for example because the endpoint response was
          invalid (malformed).

          If the endpoint state is **initial** , the reason code can be one of the following
          values:

          * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

          * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
          number of health checks for the endpoint that are required to determine its health
          status.

        - **ClientIPPreservationEnabled** *(boolean) --*

          Indicates whether client IP address preservation is enabled for an Application Load
          Balancer endpoint. The value is true or false. The default value is true for new
          accelerators.

          If the value is set to true, the client's IP address is preserved in the
          ``X-Forwarded-For`` request header as traffic travels to applications on the
          Application Load Balancer endpoint fronted by the accelerator.

          For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
          in the *AWS Global Accelerator Developer Guide* .

    - **TrafficDialPercentage** *(float) --*

      The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
      other endpoint groups for this listener.

      Use this action to increase (dial up) or decrease (dial down) traffic to a specific
      Region. The percentage is applied to the traffic that would otherwise have been routed to
      the Region based on optimal routing.

      The default value is 100.

    - **HealthCheckPort** *(integer) --*

      The port that Global Accelerator uses to perform health checks on endpoints that are part
      of this endpoint group.

      The default port is the port for the listener that this endpoint group is associated
      with. If the listener port is a list, Global Accelerator uses the first specified port in
      the list of ports.

    - **HealthCheckProtocol** *(string) --*

      The protocol that Global Accelerator uses to perform health checks on endpoints that are
      part of this endpoint group. The default value is TCP.

    - **HealthCheckPath** *(string) --*

      If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
      uses for the destination on the endpoints for health checks. The default is slash (/).

    - **HealthCheckIntervalSeconds** *(integer) --*

      The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
      value is 30.

    - **ThresholdCount** *(integer) --*

      The number of consecutive health checks required to set the state of a healthy endpoint
      to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientListEndpointGroupsResponseTypeDef = TypedDict(
    "_ClientListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List[ClientListEndpointGroupsResponseEndpointGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEndpointGroupsResponseTypeDef(_ClientListEndpointGroupsResponseTypeDef):
    """
    Type definition for `ClientListEndpointGroups` `Response`

    - **EndpointGroups** *(list) --*

      The list of the endpoint groups associated with a listener.

      - *(dict) --*

        A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
        specific listener.

        - **EndpointGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the endpoint group.

        - **EndpointGroupRegion** *(string) --*

          The AWS Region that this endpoint group belongs.

        - **EndpointDescriptions** *(list) --*

          The list of endpoint objects.

          - *(dict) --*

            A complex type for an endpoint. Each endpoint group can include one or more endpoints,
            such as load balancers.

            - **EndpointId** *(string) --*

              An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
              Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
              endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
              Application Load Balancer can be either internal or internet-facing.

            - **Weight** *(integer) --*

              The weight associated with the endpoint. When you add weights to endpoints, you
              configure AWS Global Accelerator to route traffic based on proportions that you
              specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
              The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
              5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
              endpoint. For more information, see `Endpoint Weights
              <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
              in the *AWS Global Accelerator Developer Guide* .

            - **HealthState** *(string) --*

              The health status of the endpoint.

            - **HealthReason** *(string) --*

              The reason code associated with why the endpoint is not healthy. If the endpoint
              state is healthy, a reason code is not provided.

              If the endpoint state is **unhealthy** , the reason code can be one of the following
              values:

              * **Timeout** : The health check requests to the endpoint are timing out before
              returning a status.

              * **Failed** : The health check failed, for example because the endpoint response was
              invalid (malformed).

              If the endpoint state is **initial** , the reason code can be one of the following
              values:

              * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

              * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
              number of health checks for the endpoint that are required to determine its health
              status.

            - **ClientIPPreservationEnabled** *(boolean) --*

              Indicates whether client IP address preservation is enabled for an Application Load
              Balancer endpoint. The value is true or false. The default value is true for new
              accelerators.

              If the value is set to true, the client's IP address is preserved in the
              ``X-Forwarded-For`` request header as traffic travels to applications on the
              Application Load Balancer endpoint fronted by the accelerator.

              For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
              <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
              in the *AWS Global Accelerator Developer Guide* .

        - **TrafficDialPercentage** *(float) --*

          The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
          other endpoint groups for this listener.

          Use this action to increase (dial up) or decrease (dial down) traffic to a specific
          Region. The percentage is applied to the traffic that would otherwise have been routed to
          the Region based on optimal routing.

          The default value is 100.

        - **HealthCheckPort** *(integer) --*

          The port that Global Accelerator uses to perform health checks on endpoints that are part
          of this endpoint group.

          The default port is the port for the listener that this endpoint group is associated
          with. If the listener port is a list, Global Accelerator uses the first specified port in
          the list of ports.

        - **HealthCheckProtocol** *(string) --*

          The protocol that Global Accelerator uses to perform health checks on endpoints that are
          part of this endpoint group. The default value is TCP.

        - **HealthCheckPath** *(string) --*

          If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
          uses for the destination on the endpoints for health checks. The default is slash (/).

        - **HealthCheckIntervalSeconds** *(integer) --*

          The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
          value is 30.

        - **ThresholdCount** *(integer) --*

          The number of consecutive health checks required to set the state of a healthy endpoint
          to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.

    - **NextToken** *(string) --*

      The token for the next set of results. You receive this token from a previous call.
    """


_ClientListListenersResponseListenersPortRangesTypeDef = TypedDict(
    "_ClientListListenersResponseListenersPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientListListenersResponseListenersPortRangesTypeDef(
    _ClientListListenersResponseListenersPortRangesTypeDef
):
    """
    Type definition for `ClientListListenersResponseListeners` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientListListenersResponseListenersTypeDef = TypedDict(
    "_ClientListListenersResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientListListenersResponseListenersPortRangesTypeDef],
        "Protocol": str,
        "ClientAffinity": str,
    },
    total=False,
)


class ClientListListenersResponseListenersTypeDef(
    _ClientListListenersResponseListenersTypeDef
):
    """
    Type definition for `ClientListListenersResponse` `Listeners`

    A complex type for a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **PortRanges** *(list) --*

      The list of port ranges for the connections from clients to the accelerator.

      - *(dict) --*

        A complex type for a range of ports for a listener.

        - **FromPort** *(integer) --*

          The first port in the range of ports, inclusive.

        - **ToPort** *(integer) --*

          The last port in the range of ports, inclusive.

    - **Protocol** *(string) --*

      The protocol for the connections from clients to the accelerator.

    - **ClientAffinity** *(string) --*

      Client affinity lets you direct all requests from a user to the same endpoint, if you
      have stateful applications, regardless of the port and protocol of the client request.
      Clienty affinity gives you control over whether to always route each client to the same
      specific endpoint.

      AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
      endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
      "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
      destination port, and protocol—to select the hash value, and then chooses the best
      endpoint. However, with this setting, if someone uses different ports to connect to
      Global Accelerator, their connections might not be always routed to the same endpoint
      because the hash value changes.

      If you want a given client to always be routed to the same endpoint, set client affinity
      to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses
      the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP
      address—to select the hash value.

      The default value is ``NONE`` .
    """


_ClientListListenersResponseTypeDef = TypedDict(
    "_ClientListListenersResponseTypeDef",
    {"Listeners": List[ClientListListenersResponseListenersTypeDef], "NextToken": str},
    total=False,
)


class ClientListListenersResponseTypeDef(_ClientListListenersResponseTypeDef):
    """
    Type definition for `ClientListListeners` `Response`

    - **Listeners** *(list) --*

      The list of listeners for an accelerator.

      - *(dict) --*

        A complex type for a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **PortRanges** *(list) --*

          The list of port ranges for the connections from clients to the accelerator.

          - *(dict) --*

            A complex type for a range of ports for a listener.

            - **FromPort** *(integer) --*

              The first port in the range of ports, inclusive.

            - **ToPort** *(integer) --*

              The last port in the range of ports, inclusive.

        - **Protocol** *(string) --*

          The protocol for the connections from clients to the accelerator.

        - **ClientAffinity** *(string) --*

          Client affinity lets you direct all requests from a user to the same endpoint, if you
          have stateful applications, regardless of the port and protocol of the client request.
          Clienty affinity gives you control over whether to always route each client to the same
          specific endpoint.

          AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
          endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
          "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
          destination port, and protocol—to select the hash value, and then chooses the best
          endpoint. However, with this setting, if someone uses different ports to connect to
          Global Accelerator, their connections might not be always routed to the same endpoint
          because the hash value changes.

          If you want a given client to always be routed to the same endpoint, set client affinity
          to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses
          the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP
          address—to select the hash value.

          The default value is ``NONE`` .

    - **NextToken** *(string) --*

      The token for the next set of results. You receive this token from a previous call.
    """


_ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef = TypedDict(
    "_ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef",
    {"FlowLogsEnabled": bool, "FlowLogsS3Bucket": str, "FlowLogsS3Prefix": str},
    total=False,
)


class ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef(
    _ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef
):
    """
    Type definition for `ClientUpdateAcceleratorAttributesResponse` `AcceleratorAttributes`

    Updated attributes for the accelerator.

    - **FlowLogsEnabled** *(boolean) --*

      Indicates whether flow logs are enabled. The default value is false. If the value is true,
      ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.

      For more information, see `Flow Logs
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **FlowLogsS3Bucket** *(string) --*

      The name of the Amazon S3 bucket for the flow logs. Attribute is required if
      ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that
      grants AWS Global Accelerator permission to write to the bucket.

    - **FlowLogsS3Prefix** *(string) --*

      The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is
      required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs
      are stored in the root of the bucket.
    """


_ClientUpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": ClientUpdateAcceleratorAttributesResponseAcceleratorAttributesTypeDef
    },
    total=False,
)


class ClientUpdateAcceleratorAttributesResponseTypeDef(
    _ClientUpdateAcceleratorAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateAcceleratorAttributes` `Response`

    - **AcceleratorAttributes** *(dict) --*

      Updated attributes for the accelerator.

      - **FlowLogsEnabled** *(boolean) --*

        Indicates whether flow logs are enabled. The default value is false. If the value is true,
        ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.

        For more information, see `Flow Logs
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__
        in the *AWS Global Accelerator Developer Guide* .

      - **FlowLogsS3Bucket** *(string) --*

        The name of the Amazon S3 bucket for the flow logs. Attribute is required if
        ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that
        grants AWS Global Accelerator permission to write to the bucket.

      - **FlowLogsS3Prefix** *(string) --*

        The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is
        required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs
        are stored in the root of the bucket.
    """


_ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef(
    _ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef
):
    """
    Type definition for `ClientUpdateAcceleratorResponseAccelerator` `IpSets`

    A complex type for the set of IP addresses for an accelerator.

    - **IpFamily** *(string) --*

      The types of IP addresses included in this IP set.

    - **IpAddresses** *(list) --*

      The array of IP addresses in the IP address set. An IP address set can have a maximum
      of two IP addresses.

      - *(string) --*
    """


_ClientUpdateAcceleratorResponseAcceleratorTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ClientUpdateAcceleratorResponseAcceleratorIpSetsTypeDef],
        "DnsName": str,
        "Status": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ClientUpdateAcceleratorResponseAcceleratorTypeDef(
    _ClientUpdateAcceleratorResponseAcceleratorTypeDef
):
    """
    Type definition for `ClientUpdateAcceleratorResponse` `Accelerator`

    Information about the updated accelerator.

    - **AcceleratorArn** *(string) --*

      The Amazon Resource Name (ARN) of the accelerator.

    - **Name** *(string) --*

      The name of the accelerator. The name must contain only alphanumeric characters or hyphens
      (-), and must not begin or end with a hyphen.

    - **IpAddressType** *(string) --*

      The value for the address type must be IPv4.

    - **Enabled** *(boolean) --*

      Indicates whether the accelerator is enabled. The value is true or false. The default value
      is true.

      If the value is set to true, the accelerator cannot be deleted. If set to false,
      accelerator can be deleted.

    - **IpSets** *(list) --*

      The static IP addresses that Global Accelerator associates with the accelerator.

      - *(dict) --*

        A complex type for the set of IP addresses for an accelerator.

        - **IpFamily** *(string) --*

          The types of IP addresses included in this IP set.

        - **IpAddresses** *(list) --*

          The array of IP addresses in the IP address set. An IP address set can have a maximum
          of two IP addresses.

          - *(string) --*

    - **DnsName** *(string) --*

      The Domain Name System (DNS) name that Global Accelerator creates that points to your
      accelerator's static IP addresses.

      The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
      random hex string, followed by .awsglobalaccelerator.com. For example:
      a1234567890abcdef.awsglobalaccelerator.com.

      For more information about the default DNS name, see `Support for DNS Addressing in Global
      Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **Status** *(string) --*

      Describes the deployment status of the accelerator.

    - **CreatedTime** *(datetime) --*

      The date and time that the accelerator was created.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the accelerator was last modified.
    """


_ClientUpdateAcceleratorResponseTypeDef = TypedDict(
    "_ClientUpdateAcceleratorResponseTypeDef",
    {"Accelerator": ClientUpdateAcceleratorResponseAcceleratorTypeDef},
    total=False,
)


class ClientUpdateAcceleratorResponseTypeDef(_ClientUpdateAcceleratorResponseTypeDef):
    """
    Type definition for `ClientUpdateAccelerator` `Response`

    - **Accelerator** *(dict) --*

      Information about the updated accelerator.

      - **AcceleratorArn** *(string) --*

        The Amazon Resource Name (ARN) of the accelerator.

      - **Name** *(string) --*

        The name of the accelerator. The name must contain only alphanumeric characters or hyphens
        (-), and must not begin or end with a hyphen.

      - **IpAddressType** *(string) --*

        The value for the address type must be IPv4.

      - **Enabled** *(boolean) --*

        Indicates whether the accelerator is enabled. The value is true or false. The default value
        is true.

        If the value is set to true, the accelerator cannot be deleted. If set to false,
        accelerator can be deleted.

      - **IpSets** *(list) --*

        The static IP addresses that Global Accelerator associates with the accelerator.

        - *(dict) --*

          A complex type for the set of IP addresses for an accelerator.

          - **IpFamily** *(string) --*

            The types of IP addresses included in this IP set.

          - **IpAddresses** *(list) --*

            The array of IP addresses in the IP address set. An IP address set can have a maximum
            of two IP addresses.

            - *(string) --*

      - **DnsName** *(string) --*

        The Domain Name System (DNS) name that Global Accelerator creates that points to your
        accelerator's static IP addresses.

        The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
        random hex string, followed by .awsglobalaccelerator.com. For example:
        a1234567890abcdef.awsglobalaccelerator.com.

        For more information about the default DNS name, see `Support for DNS Addressing in Global
        Accelerator
        <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
        in the *AWS Global Accelerator Developer Guide* .

      - **Status** *(string) --*

        Describes the deployment status of the accelerator.

      - **CreatedTime** *(datetime) --*

        The date and time that the accelerator was created.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the accelerator was last modified.
    """


_ClientUpdateEndpointGroupEndpointConfigurationsTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupEndpointConfigurationsTypeDef",
    {"EndpointId": str, "Weight": int, "ClientIPPreservationEnabled": bool},
    total=False,
)


class ClientUpdateEndpointGroupEndpointConfigurationsTypeDef(
    _ClientUpdateEndpointGroupEndpointConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateEndpointGroup` `EndpointConfigurations`

    A complex type for endpoints.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
      Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
      Elastic IP address, this is the Elastic IP address allocation ID.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you configure AWS
      Global Accelerator to route traffic based on proportions that you specify. For example, you
      might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your
      traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and
      third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint
      Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load Balancer
      endpoint. The value is true or false. The default value is true for new accelerators.

      If the value is set to true, the client's IP address is preserved in the ``X-Forwarded-For``
      request header as traffic travels to applications on the Application Load Balancer endpoint
      fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": str,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef(
    _ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
):
    """
    Type definition for `ClientUpdateEndpointGroupResponseEndpointGroup` `EndpointDescriptions`

    A complex type for an endpoint. Each endpoint group can include one or more endpoints,
    such as load balancers.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
      Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
      Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
      Balancer can be either internal or internet-facing.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you
      configure AWS Global Accelerator to route traffic based on proportions that you
      specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
      The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
      5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
      endpoint. For more information, see `Endpoint Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **HealthState** *(string) --*

      The health status of the endpoint.

    - **HealthReason** *(string) --*

      The reason code associated with why the endpoint is not healthy. If the endpoint state
      is healthy, a reason code is not provided.

      If the endpoint state is **unhealthy** , the reason code can be one of the following
      values:

      * **Timeout** : The health check requests to the endpoint are timing out before
      returning a status.

      * **Failed** : The health check failed, for example because the endpoint response was
      invalid (malformed).

      If the endpoint state is **initial** , the reason code can be one of the following
      values:

      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
      of health checks for the endpoint that are required to determine its health status.

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load
      Balancer endpoint. The value is true or false. The default value is true for new
      accelerators.

      If the value is set to true, the client's IP address is preserved in the
      ``X-Forwarded-For`` request header as traffic travels to applications on the
      Application Load Balancer endpoint fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ClientUpdateEndpointGroupResponseEndpointGroupTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ClientUpdateEndpointGroupResponseEndpointGroupEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": str,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ClientUpdateEndpointGroupResponseEndpointGroupTypeDef(
    _ClientUpdateEndpointGroupResponseEndpointGroupTypeDef
):
    """
    Type definition for `ClientUpdateEndpointGroupResponse` `EndpointGroup`

    The information about the endpoint group that was updated.

    - **EndpointGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the endpoint group.

    - **EndpointGroupRegion** *(string) --*

      The AWS Region that this endpoint group belongs.

    - **EndpointDescriptions** *(list) --*

      The list of endpoint objects.

      - *(dict) --*

        A complex type for an endpoint. Each endpoint group can include one or more endpoints,
        such as load balancers.

        - **EndpointId** *(string) --*

          An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
          Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
          Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
          Balancer can be either internal or internet-facing.

        - **Weight** *(integer) --*

          The weight associated with the endpoint. When you add weights to endpoints, you
          configure AWS Global Accelerator to route traffic based on proportions that you
          specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
          The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
          5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
          endpoint. For more information, see `Endpoint Weights
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **HealthState** *(string) --*

          The health status of the endpoint.

        - **HealthReason** *(string) --*

          The reason code associated with why the endpoint is not healthy. If the endpoint state
          is healthy, a reason code is not provided.

          If the endpoint state is **unhealthy** , the reason code can be one of the following
          values:

          * **Timeout** : The health check requests to the endpoint are timing out before
          returning a status.

          * **Failed** : The health check failed, for example because the endpoint response was
          invalid (malformed).

          If the endpoint state is **initial** , the reason code can be one of the following
          values:

          * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

          * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
          of health checks for the endpoint that are required to determine its health status.

        - **ClientIPPreservationEnabled** *(boolean) --*

          Indicates whether client IP address preservation is enabled for an Application Load
          Balancer endpoint. The value is true or false. The default value is true for new
          accelerators.

          If the value is set to true, the client's IP address is preserved in the
          ``X-Forwarded-For`` request header as traffic travels to applications on the
          Application Load Balancer endpoint fronted by the accelerator.

          For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
          in the *AWS Global Accelerator Developer Guide* .

    - **TrafficDialPercentage** *(float) --*

      The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
      other endpoint groups for this listener.

      Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
      The percentage is applied to the traffic that would otherwise have been routed to the
      Region based on optimal routing.

      The default value is 100.

    - **HealthCheckPort** *(integer) --*

      The port that Global Accelerator uses to perform health checks on endpoints that are part
      of this endpoint group.

      The default port is the port for the listener that this endpoint group is associated with.
      If the listener port is a list, Global Accelerator uses the first specified port in the
      list of ports.

    - **HealthCheckProtocol** *(string) --*

      The protocol that Global Accelerator uses to perform health checks on endpoints that are
      part of this endpoint group. The default value is TCP.

    - **HealthCheckPath** *(string) --*

      If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
      uses for the destination on the endpoints for health checks. The default is slash (/).

    - **HealthCheckIntervalSeconds** *(integer) --*

      The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
      value is 30.

    - **ThresholdCount** *(integer) --*

      The number of consecutive health checks required to set the state of a healthy endpoint to
      unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientUpdateEndpointGroupResponseTypeDef = TypedDict(
    "_ClientUpdateEndpointGroupResponseTypeDef",
    {"EndpointGroup": ClientUpdateEndpointGroupResponseEndpointGroupTypeDef},
    total=False,
)


class ClientUpdateEndpointGroupResponseTypeDef(
    _ClientUpdateEndpointGroupResponseTypeDef
):
    """
    Type definition for `ClientUpdateEndpointGroup` `Response`

    - **EndpointGroup** *(dict) --*

      The information about the endpoint group that was updated.

      - **EndpointGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the endpoint group.

      - **EndpointGroupRegion** *(string) --*

        The AWS Region that this endpoint group belongs.

      - **EndpointDescriptions** *(list) --*

        The list of endpoint objects.

        - *(dict) --*

          A complex type for an endpoint. Each endpoint group can include one or more endpoints,
          such as load balancers.

          - **EndpointId** *(string) --*

            An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load
            Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an
            Elastic IP address, this is the Elastic IP address allocation ID. An Application Load
            Balancer can be either internal or internet-facing.

          - **Weight** *(integer) --*

            The weight associated with the endpoint. When you add weights to endpoints, you
            configure AWS Global Accelerator to route traffic based on proportions that you
            specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
            The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
            5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
            endpoint. For more information, see `Endpoint Weights
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
            in the *AWS Global Accelerator Developer Guide* .

          - **HealthState** *(string) --*

            The health status of the endpoint.

          - **HealthReason** *(string) --*

            The reason code associated with why the endpoint is not healthy. If the endpoint state
            is healthy, a reason code is not provided.

            If the endpoint state is **unhealthy** , the reason code can be one of the following
            values:

            * **Timeout** : The health check requests to the endpoint are timing out before
            returning a status.

            * **Failed** : The health check failed, for example because the endpoint response was
            invalid (malformed).

            If the endpoint state is **initial** , the reason code can be one of the following
            values:

            * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

            * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number
            of health checks for the endpoint that are required to determine its health status.

          - **ClientIPPreservationEnabled** *(boolean) --*

            Indicates whether client IP address preservation is enabled for an Application Load
            Balancer endpoint. The value is true or false. The default value is true for new
            accelerators.

            If the value is set to true, the client's IP address is preserved in the
            ``X-Forwarded-For`` request header as traffic travels to applications on the
            Application Load Balancer endpoint fronted by the accelerator.

            For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
            <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
            in the *AWS Global Accelerator Developer Guide* .

      - **TrafficDialPercentage** *(float) --*

        The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
        other endpoint groups for this listener.

        Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region.
        The percentage is applied to the traffic that would otherwise have been routed to the
        Region based on optimal routing.

        The default value is 100.

      - **HealthCheckPort** *(integer) --*

        The port that Global Accelerator uses to perform health checks on endpoints that are part
        of this endpoint group.

        The default port is the port for the listener that this endpoint group is associated with.
        If the listener port is a list, Global Accelerator uses the first specified port in the
        list of ports.

      - **HealthCheckProtocol** *(string) --*

        The protocol that Global Accelerator uses to perform health checks on endpoints that are
        part of this endpoint group. The default value is TCP.

      - **HealthCheckPath** *(string) --*

        If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
        uses for the destination on the endpoints for health checks. The default is slash (/).

      - **HealthCheckIntervalSeconds** *(integer) --*

        The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
        value is 30.

      - **ThresholdCount** *(integer) --*

        The number of consecutive health checks required to set the state of a healthy endpoint to
        unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ClientUpdateListenerPortRangesTypeDef = TypedDict(
    "_ClientUpdateListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientUpdateListenerPortRangesTypeDef(_ClientUpdateListenerPortRangesTypeDef):
    """
    Type definition for `ClientUpdateListener` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientUpdateListenerResponseListenerPortRangesTypeDef = TypedDict(
    "_ClientUpdateListenerResponseListenerPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ClientUpdateListenerResponseListenerPortRangesTypeDef(
    _ClientUpdateListenerResponseListenerPortRangesTypeDef
):
    """
    Type definition for `ClientUpdateListenerResponseListener` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ClientUpdateListenerResponseListenerTypeDef = TypedDict(
    "_ClientUpdateListenerResponseListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ClientUpdateListenerResponseListenerPortRangesTypeDef],
        "Protocol": str,
        "ClientAffinity": str,
    },
    total=False,
)


class ClientUpdateListenerResponseListenerTypeDef(
    _ClientUpdateListenerResponseListenerTypeDef
):
    """
    Type definition for `ClientUpdateListenerResponse` `Listener`

    Information for the updated listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **PortRanges** *(list) --*

      The list of port ranges for the connections from clients to the accelerator.

      - *(dict) --*

        A complex type for a range of ports for a listener.

        - **FromPort** *(integer) --*

          The first port in the range of ports, inclusive.

        - **ToPort** *(integer) --*

          The last port in the range of ports, inclusive.

    - **Protocol** *(string) --*

      The protocol for the connections from clients to the accelerator.

    - **ClientAffinity** *(string) --*

      Client affinity lets you direct all requests from a user to the same endpoint, if you have
      stateful applications, regardless of the port and protocol of the client request. Clienty
      affinity gives you control over whether to always route each client to the same specific
      endpoint.

      AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
      endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
      "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
      destination port, and protocol—to select the hash value, and then chooses the best
      endpoint. However, with this setting, if someone uses different ports to connect to Global
      Accelerator, their connections might not be always routed to the same endpoint because the
      hash value changes.

      If you want a given client to always be routed to the same endpoint, set client affinity to
      ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
      "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
      select the hash value.

      The default value is ``NONE`` .
    """


_ClientUpdateListenerResponseTypeDef = TypedDict(
    "_ClientUpdateListenerResponseTypeDef",
    {"Listener": ClientUpdateListenerResponseListenerTypeDef},
    total=False,
)


class ClientUpdateListenerResponseTypeDef(_ClientUpdateListenerResponseTypeDef):
    """
    Type definition for `ClientUpdateListener` `Response`

    - **Listener** *(dict) --*

      Information for the updated listener.

      - **ListenerArn** *(string) --*

        The Amazon Resource Name (ARN) of the listener.

      - **PortRanges** *(list) --*

        The list of port ranges for the connections from clients to the accelerator.

        - *(dict) --*

          A complex type for a range of ports for a listener.

          - **FromPort** *(integer) --*

            The first port in the range of ports, inclusive.

          - **ToPort** *(integer) --*

            The last port in the range of ports, inclusive.

      - **Protocol** *(string) --*

        The protocol for the connections from clients to the accelerator.

      - **ClientAffinity** *(string) --*

        Client affinity lets you direct all requests from a user to the same endpoint, if you have
        stateful applications, regardless of the port and protocol of the client request. Clienty
        affinity gives you control over whether to always route each client to the same specific
        endpoint.

        AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
        endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
        "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
        destination port, and protocol—to select the hash value, and then chooses the best
        endpoint. However, with this setting, if someone uses different ports to connect to Global
        Accelerator, their connections might not be always routed to the same endpoint because the
        hash value changes.

        If you want a given client to always be routed to the same endpoint, set client affinity to
        ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the
        "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to
        select the hash value.

        The default value is ``NONE`` .
    """


_ListAcceleratorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAcceleratorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAcceleratorsPaginatePaginationConfigTypeDef(
    _ListAcceleratorsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAcceleratorsPaginate` `PaginationConfig`

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


_ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef",
    {"IpFamily": str, "IpAddresses": List[str]},
    total=False,
)


class ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef(
    _ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef
):
    """
    Type definition for `ListAcceleratorsPaginateResponseAccelerators` `IpSets`

    A complex type for the set of IP addresses for an accelerator.

    - **IpFamily** *(string) --*

      The types of IP addresses included in this IP set.

    - **IpAddresses** *(list) --*

      The array of IP addresses in the IP address set. An IP address set can have a maximum
      of two IP addresses.

      - *(string) --*
    """


_ListAcceleratorsPaginateResponseAcceleratorsTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseAcceleratorsTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": str,
        "Enabled": bool,
        "IpSets": List[ListAcceleratorsPaginateResponseAcceleratorsIpSetsTypeDef],
        "DnsName": str,
        "Status": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)


class ListAcceleratorsPaginateResponseAcceleratorsTypeDef(
    _ListAcceleratorsPaginateResponseAcceleratorsTypeDef
):
    """
    Type definition for `ListAcceleratorsPaginateResponse` `Accelerators`

    An accelerator is a complex type that includes one or more listeners that process inbound
    connections and then direct traffic to one or more endpoint groups, each of which includes
    endpoints, such as load balancers.

    - **AcceleratorArn** *(string) --*

      The Amazon Resource Name (ARN) of the accelerator.

    - **Name** *(string) --*

      The name of the accelerator. The name must contain only alphanumeric characters or
      hyphens (-), and must not begin or end with a hyphen.

    - **IpAddressType** *(string) --*

      The value for the address type must be IPv4.

    - **Enabled** *(boolean) --*

      Indicates whether the accelerator is enabled. The value is true or false. The default
      value is true.

      If the value is set to true, the accelerator cannot be deleted. If set to false,
      accelerator can be deleted.

    - **IpSets** *(list) --*

      The static IP addresses that Global Accelerator associates with the accelerator.

      - *(dict) --*

        A complex type for the set of IP addresses for an accelerator.

        - **IpFamily** *(string) --*

          The types of IP addresses included in this IP set.

        - **IpAddresses** *(list) --*

          The array of IP addresses in the IP address set. An IP address set can have a maximum
          of two IP addresses.

          - *(string) --*

    - **DnsName** *(string) --*

      The Domain Name System (DNS) name that Global Accelerator creates that points to your
      accelerator's static IP addresses.

      The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
      random hex string, followed by .awsglobalaccelerator.com. For example:
      a1234567890abcdef.awsglobalaccelerator.com.

      For more information about the default DNS name, see `Support for DNS Addressing in
      Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **Status** *(string) --*

      Describes the deployment status of the accelerator.

    - **CreatedTime** *(datetime) --*

      The date and time that the accelerator was created.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the accelerator was last modified.
    """


_ListAcceleratorsPaginateResponseTypeDef = TypedDict(
    "_ListAcceleratorsPaginateResponseTypeDef",
    {"Accelerators": List[ListAcceleratorsPaginateResponseAcceleratorsTypeDef]},
    total=False,
)


class ListAcceleratorsPaginateResponseTypeDef(_ListAcceleratorsPaginateResponseTypeDef):
    """
    Type definition for `ListAcceleratorsPaginate` `Response`

    - **Accelerators** *(list) --*

      The list of accelerators for a customer account.

      - *(dict) --*

        An accelerator is a complex type that includes one or more listeners that process inbound
        connections and then direct traffic to one or more endpoint groups, each of which includes
        endpoints, such as load balancers.

        - **AcceleratorArn** *(string) --*

          The Amazon Resource Name (ARN) of the accelerator.

        - **Name** *(string) --*

          The name of the accelerator. The name must contain only alphanumeric characters or
          hyphens (-), and must not begin or end with a hyphen.

        - **IpAddressType** *(string) --*

          The value for the address type must be IPv4.

        - **Enabled** *(boolean) --*

          Indicates whether the accelerator is enabled. The value is true or false. The default
          value is true.

          If the value is set to true, the accelerator cannot be deleted. If set to false,
          accelerator can be deleted.

        - **IpSets** *(list) --*

          The static IP addresses that Global Accelerator associates with the accelerator.

          - *(dict) --*

            A complex type for the set of IP addresses for an accelerator.

            - **IpFamily** *(string) --*

              The types of IP addresses included in this IP set.

            - **IpAddresses** *(list) --*

              The array of IP addresses in the IP address set. An IP address set can have a maximum
              of two IP addresses.

              - *(string) --*

        - **DnsName** *(string) --*

          The Domain Name System (DNS) name that Global Accelerator creates that points to your
          accelerator's static IP addresses.

          The naming convention for the DNS name is: a lower case letter a, followed by a 16-bit
          random hex string, followed by .awsglobalaccelerator.com. For example:
          a1234567890abcdef.awsglobalaccelerator.com.

          For more information about the default DNS name, see `Support for DNS Addressing in
          Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **Status** *(string) --*

          Describes the deployment status of the accelerator.

        - **CreatedTime** *(datetime) --*

          The date and time that the accelerator was created.

        - **LastModifiedTime** *(datetime) --*

          The date and time that the accelerator was last modified.
    """


_ListEndpointGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEndpointGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEndpointGroupsPaginatePaginationConfigTypeDef(
    _ListEndpointGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEndpointGroupsPaginate` `PaginationConfig`

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


_ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": str,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)


class ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef(
    _ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef
):
    """
    Type definition for `ListEndpointGroupsPaginateResponseEndpointGroups` `EndpointDescriptions`

    A complex type for an endpoint. Each endpoint group can include one or more endpoints,
    such as load balancers.

    - **EndpointId** *(string) --*

      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
      Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
      endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
      Application Load Balancer can be either internal or internet-facing.

    - **Weight** *(integer) --*

      The weight associated with the endpoint. When you add weights to endpoints, you
      configure AWS Global Accelerator to route traffic based on proportions that you
      specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
      The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
      5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
      endpoint. For more information, see `Endpoint Weights
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
      in the *AWS Global Accelerator Developer Guide* .

    - **HealthState** *(string) --*

      The health status of the endpoint.

    - **HealthReason** *(string) --*

      The reason code associated with why the endpoint is not healthy. If the endpoint
      state is healthy, a reason code is not provided.

      If the endpoint state is **unhealthy** , the reason code can be one of the following
      values:

      * **Timeout** : The health check requests to the endpoint are timing out before
      returning a status.

      * **Failed** : The health check failed, for example because the endpoint response was
      invalid (malformed).

      If the endpoint state is **initial** , the reason code can be one of the following
      values:

      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
      number of health checks for the endpoint that are required to determine its health
      status.

    - **ClientIPPreservationEnabled** *(boolean) --*

      Indicates whether client IP address preservation is enabled for an Application Load
      Balancer endpoint. The value is true or false. The default value is true for new
      accelerators.

      If the value is set to true, the client's IP address is preserved in the
      ``X-Forwarded-For`` request header as traffic travels to applications on the
      Application Load Balancer endpoint fronted by the accelerator.

      For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
      <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
      in the *AWS Global Accelerator Developer Guide* .
    """


_ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List[
            ListEndpointGroupsPaginateResponseEndpointGroupsEndpointDescriptionsTypeDef
        ],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": str,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
    },
    total=False,
)


class ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef(
    _ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef
):
    """
    Type definition for `ListEndpointGroupsPaginateResponse` `EndpointGroups`

    A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
    specific listener.

    - **EndpointGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the endpoint group.

    - **EndpointGroupRegion** *(string) --*

      The AWS Region that this endpoint group belongs.

    - **EndpointDescriptions** *(list) --*

      The list of endpoint objects.

      - *(dict) --*

        A complex type for an endpoint. Each endpoint group can include one or more endpoints,
        such as load balancers.

        - **EndpointId** *(string) --*

          An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
          Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
          endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
          Application Load Balancer can be either internal or internet-facing.

        - **Weight** *(integer) --*

          The weight associated with the endpoint. When you add weights to endpoints, you
          configure AWS Global Accelerator to route traffic based on proportions that you
          specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
          The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
          5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
          endpoint. For more information, see `Endpoint Weights
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
          in the *AWS Global Accelerator Developer Guide* .

        - **HealthState** *(string) --*

          The health status of the endpoint.

        - **HealthReason** *(string) --*

          The reason code associated with why the endpoint is not healthy. If the endpoint
          state is healthy, a reason code is not provided.

          If the endpoint state is **unhealthy** , the reason code can be one of the following
          values:

          * **Timeout** : The health check requests to the endpoint are timing out before
          returning a status.

          * **Failed** : The health check failed, for example because the endpoint response was
          invalid (malformed).

          If the endpoint state is **initial** , the reason code can be one of the following
          values:

          * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

          * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
          number of health checks for the endpoint that are required to determine its health
          status.

        - **ClientIPPreservationEnabled** *(boolean) --*

          Indicates whether client IP address preservation is enabled for an Application Load
          Balancer endpoint. The value is true or false. The default value is true for new
          accelerators.

          If the value is set to true, the client's IP address is preserved in the
          ``X-Forwarded-For`` request header as traffic travels to applications on the
          Application Load Balancer endpoint fronted by the accelerator.

          For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
          <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
          in the *AWS Global Accelerator Developer Guide* .

    - **TrafficDialPercentage** *(float) --*

      The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
      other endpoint groups for this listener.

      Use this action to increase (dial up) or decrease (dial down) traffic to a specific
      Region. The percentage is applied to the traffic that would otherwise have been routed to
      the Region based on optimal routing.

      The default value is 100.

    - **HealthCheckPort** *(integer) --*

      The port that Global Accelerator uses to perform health checks on endpoints that are part
      of this endpoint group.

      The default port is the port for the listener that this endpoint group is associated
      with. If the listener port is a list, Global Accelerator uses the first specified port in
      the list of ports.

    - **HealthCheckProtocol** *(string) --*

      The protocol that Global Accelerator uses to perform health checks on endpoints that are
      part of this endpoint group. The default value is TCP.

    - **HealthCheckPath** *(string) --*

      If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
      uses for the destination on the endpoints for health checks. The default is slash (/).

    - **HealthCheckIntervalSeconds** *(integer) --*

      The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
      value is 30.

    - **ThresholdCount** *(integer) --*

      The number of consecutive health checks required to set the state of a healthy endpoint
      to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ListEndpointGroupsPaginateResponseTypeDef = TypedDict(
    "_ListEndpointGroupsPaginateResponseTypeDef",
    {"EndpointGroups": List[ListEndpointGroupsPaginateResponseEndpointGroupsTypeDef]},
    total=False,
)


class ListEndpointGroupsPaginateResponseTypeDef(
    _ListEndpointGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListEndpointGroupsPaginate` `Response`

    - **EndpointGroups** *(list) --*

      The list of the endpoint groups associated with a listener.

      - *(dict) --*

        A complex type for the endpoint group. An AWS Region can have only one endpoint group for a
        specific listener.

        - **EndpointGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the endpoint group.

        - **EndpointGroupRegion** *(string) --*

          The AWS Region that this endpoint group belongs.

        - **EndpointDescriptions** *(list) --*

          The list of endpoint objects.

          - *(dict) --*

            A complex type for an endpoint. Each endpoint group can include one or more endpoints,
            such as load balancers.

            - **EndpointId** *(string) --*

              An ID for the endpoint. If the endpoint is a Network Load Balancer or Application
              Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the
              endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. An
              Application Load Balancer can be either internal or internet-facing.

            - **Weight** *(integer) --*

              The weight associated with the endpoint. When you add weights to endpoints, you
              configure AWS Global Accelerator to route traffic based on proportions that you
              specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20).
              The result is that 4/20 of your traffic, on average, is routed to the first endpoint,
              5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last
              endpoint. For more information, see `Endpoint Weights
              <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__
              in the *AWS Global Accelerator Developer Guide* .

            - **HealthState** *(string) --*

              The health status of the endpoint.

            - **HealthReason** *(string) --*

              The reason code associated with why the endpoint is not healthy. If the endpoint
              state is healthy, a reason code is not provided.

              If the endpoint state is **unhealthy** , the reason code can be one of the following
              values:

              * **Timeout** : The health check requests to the endpoint are timing out before
              returning a status.

              * **Failed** : The health check failed, for example because the endpoint response was
              invalid (malformed).

              If the endpoint state is **initial** , the reason code can be one of the following
              values:

              * **ProvisioningInProgress** : The endpoint is in the process of being provisioned.

              * **InitialHealthChecking** : Global Accelerator is still setting up the minimum
              number of health checks for the endpoint that are required to determine its health
              status.

            - **ClientIPPreservationEnabled** *(boolean) --*

              Indicates whether client IP address preservation is enabled for an Application Load
              Balancer endpoint. The value is true or false. The default value is true for new
              accelerators.

              If the value is set to true, the client's IP address is preserved in the
              ``X-Forwarded-For`` request header as traffic travels to applications on the
              Application Load Balancer endpoint fronted by the accelerator.

              For more information, see `Viewing Client IP Addresses in AWS Global Accelerator
              <https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works-client-ip.html>`__
              in the *AWS Global Accelerator Developer Guide* .

        - **TrafficDialPercentage** *(float) --*

          The percentage of traffic to send to an AWS Region. Additional traffic is distributed to
          other endpoint groups for this listener.

          Use this action to increase (dial up) or decrease (dial down) traffic to a specific
          Region. The percentage is applied to the traffic that would otherwise have been routed to
          the Region based on optimal routing.

          The default value is 100.

        - **HealthCheckPort** *(integer) --*

          The port that Global Accelerator uses to perform health checks on endpoints that are part
          of this endpoint group.

          The default port is the port for the listener that this endpoint group is associated
          with. If the listener port is a list, Global Accelerator uses the first specified port in
          the list of ports.

        - **HealthCheckProtocol** *(string) --*

          The protocol that Global Accelerator uses to perform health checks on endpoints that are
          part of this endpoint group. The default value is TCP.

        - **HealthCheckPath** *(string) --*

          If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator
          uses for the destination on the endpoints for health checks. The default is slash (/).

        - **HealthCheckIntervalSeconds** *(integer) --*

          The time—10 seconds or 30 seconds—between health checks for each endpoint. The default
          value is 30.

        - **ThresholdCount** *(integer) --*

          The number of consecutive health checks required to set the state of a healthy endpoint
          to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
    """


_ListListenersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListListenersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListListenersPaginatePaginationConfigTypeDef(
    _ListListenersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListListenersPaginate` `PaginationConfig`

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


_ListListenersPaginateResponseListenersPortRangesTypeDef = TypedDict(
    "_ListListenersPaginateResponseListenersPortRangesTypeDef",
    {"FromPort": int, "ToPort": int},
    total=False,
)


class ListListenersPaginateResponseListenersPortRangesTypeDef(
    _ListListenersPaginateResponseListenersPortRangesTypeDef
):
    """
    Type definition for `ListListenersPaginateResponseListeners` `PortRanges`

    A complex type for a range of ports for a listener.

    - **FromPort** *(integer) --*

      The first port in the range of ports, inclusive.

    - **ToPort** *(integer) --*

      The last port in the range of ports, inclusive.
    """


_ListListenersPaginateResponseListenersTypeDef = TypedDict(
    "_ListListenersPaginateResponseListenersTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List[ListListenersPaginateResponseListenersPortRangesTypeDef],
        "Protocol": str,
        "ClientAffinity": str,
    },
    total=False,
)


class ListListenersPaginateResponseListenersTypeDef(
    _ListListenersPaginateResponseListenersTypeDef
):
    """
    Type definition for `ListListenersPaginateResponse` `Listeners`

    A complex type for a listener.

    - **ListenerArn** *(string) --*

      The Amazon Resource Name (ARN) of the listener.

    - **PortRanges** *(list) --*

      The list of port ranges for the connections from clients to the accelerator.

      - *(dict) --*

        A complex type for a range of ports for a listener.

        - **FromPort** *(integer) --*

          The first port in the range of ports, inclusive.

        - **ToPort** *(integer) --*

          The last port in the range of ports, inclusive.

    - **Protocol** *(string) --*

      The protocol for the connections from clients to the accelerator.

    - **ClientAffinity** *(string) --*

      Client affinity lets you direct all requests from a user to the same endpoint, if you
      have stateful applications, regardless of the port and protocol of the client request.
      Clienty affinity gives you control over whether to always route each client to the same
      specific endpoint.

      AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
      endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
      "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
      destination port, and protocol—to select the hash value, and then chooses the best
      endpoint. However, with this setting, if someone uses different ports to connect to
      Global Accelerator, their connections might not be always routed to the same endpoint
      because the hash value changes.

      If you want a given client to always be routed to the same endpoint, set client affinity
      to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses
      the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP
      address—to select the hash value.

      The default value is ``NONE`` .
    """


_ListListenersPaginateResponseTypeDef = TypedDict(
    "_ListListenersPaginateResponseTypeDef",
    {"Listeners": List[ListListenersPaginateResponseListenersTypeDef]},
    total=False,
)


class ListListenersPaginateResponseTypeDef(_ListListenersPaginateResponseTypeDef):
    """
    Type definition for `ListListenersPaginate` `Response`

    - **Listeners** *(list) --*

      The list of listeners for an accelerator.

      - *(dict) --*

        A complex type for a listener.

        - **ListenerArn** *(string) --*

          The Amazon Resource Name (ARN) of the listener.

        - **PortRanges** *(list) --*

          The list of port ranges for the connections from clients to the accelerator.

          - *(dict) --*

            A complex type for a range of ports for a listener.

            - **FromPort** *(integer) --*

              The first port in the range of ports, inclusive.

            - **ToPort** *(integer) --*

              The last port in the range of ports, inclusive.

        - **Protocol** *(string) --*

          The protocol for the connections from clients to the accelerator.

        - **ClientAffinity** *(string) --*

          Client affinity lets you direct all requests from a user to the same endpoint, if you
          have stateful applications, regardless of the port and protocol of the client request.
          Clienty affinity gives you control over whether to always route each client to the same
          specific endpoint.

          AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal
          endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the
          "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address,
          destination port, and protocol—to select the hash value, and then chooses the best
          endpoint. However, with this setting, if someone uses different ports to connect to
          Global Accelerator, their connections might not be always routed to the same endpoint
          because the hash value changes.

          If you want a given client to always be routed to the same endpoint, set client affinity
          to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses
          the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP
          address—to select the hash value.

          The default value is ``NONE`` .
    """
