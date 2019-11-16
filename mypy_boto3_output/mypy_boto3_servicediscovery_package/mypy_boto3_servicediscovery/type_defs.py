"Main interface for servicediscovery type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateHttpNamespaceResponseTypeDef",
    "ClientCreatePrivateDnsNamespaceResponseTypeDef",
    "ClientCreatePublicDnsNamespaceResponseTypeDef",
    "ClientCreateServiceDnsConfigDnsRecordsTypeDef",
    "ClientCreateServiceDnsConfigTypeDef",
    "ClientCreateServiceHealthCheckConfigTypeDef",
    "ClientCreateServiceHealthCheckCustomConfigTypeDef",
    "ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    "ClientCreateServiceResponseServiceDnsConfigTypeDef",
    "ClientCreateServiceResponseServiceHealthCheckConfigTypeDef",
    "ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef",
    "ClientCreateServiceResponseServiceTypeDef",
    "ClientCreateServiceResponseTypeDef",
    "ClientDeleteNamespaceResponseTypeDef",
    "ClientDeregisterInstanceResponseTypeDef",
    "ClientDiscoverInstancesResponseInstancesTypeDef",
    "ClientDiscoverInstancesResponseTypeDef",
    "ClientGetInstanceResponseInstanceTypeDef",
    "ClientGetInstanceResponseTypeDef",
    "ClientGetInstancesHealthStatusResponseTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesTypeDef",
    "ClientGetNamespaceResponseNamespaceTypeDef",
    "ClientGetNamespaceResponseTypeDef",
    "ClientGetOperationResponseOperationTypeDef",
    "ClientGetOperationResponseTypeDef",
    "ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    "ClientGetServiceResponseServiceDnsConfigTypeDef",
    "ClientGetServiceResponseServiceHealthCheckConfigTypeDef",
    "ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef",
    "ClientGetServiceResponseServiceTypeDef",
    "ClientGetServiceResponseTypeDef",
    "ClientListInstancesResponseInstancesTypeDef",
    "ClientListInstancesResponseTypeDef",
    "ClientListNamespacesFiltersTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesTypeDef",
    "ClientListNamespacesResponseTypeDef",
    "ClientListOperationsFiltersTypeDef",
    "ClientListOperationsResponseOperationsTypeDef",
    "ClientListOperationsResponseTypeDef",
    "ClientListServicesFiltersTypeDef",
    "ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef",
    "ClientListServicesResponseServicesDnsConfigTypeDef",
    "ClientListServicesResponseServicesHealthCheckConfigTypeDef",
    "ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef",
    "ClientListServicesResponseServicesTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientRegisterInstanceResponseTypeDef",
    "ClientUpdateServiceResponseTypeDef",
    "ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef",
    "ClientUpdateServiceServiceDnsConfigTypeDef",
    "ClientUpdateServiceServiceHealthCheckConfigTypeDef",
    "ClientUpdateServiceServiceTypeDef",
    "ListInstancesPaginatePaginationConfigTypeDef",
    "ListInstancesPaginateResponseInstancesTypeDef",
    "ListInstancesPaginateResponseTypeDef",
    "ListNamespacesPaginateFiltersTypeDef",
    "ListNamespacesPaginatePaginationConfigTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesTypeDef",
    "ListNamespacesPaginateResponseTypeDef",
    "ListOperationsPaginateFiltersTypeDef",
    "ListOperationsPaginatePaginationConfigTypeDef",
    "ListOperationsPaginateResponseOperationsTypeDef",
    "ListOperationsPaginateResponseTypeDef",
    "ListServicesPaginateFiltersTypeDef",
    "ListServicesPaginatePaginationConfigTypeDef",
    "ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef",
    "ListServicesPaginateResponseServicesDnsConfigTypeDef",
    "ListServicesPaginateResponseServicesHealthCheckConfigTypeDef",
    "ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef",
    "ListServicesPaginateResponseServicesTypeDef",
    "ListServicesPaginateResponseTypeDef",
)


_ClientCreateHttpNamespaceResponseTypeDef = TypedDict(
    "_ClientCreateHttpNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreateHttpNamespaceResponseTypeDef(
    _ClientCreateHttpNamespaceResponseTypeDef
):
    """
    Type definition for `ClientCreateHttpNamespace` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientCreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "_ClientCreatePrivateDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreatePrivateDnsNamespaceResponseTypeDef(
    _ClientCreatePrivateDnsNamespaceResponseTypeDef
):
    """
    Type definition for `ClientCreatePrivateDnsNamespace` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientCreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "_ClientCreatePublicDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreatePublicDnsNamespaceResponseTypeDef(
    _ClientCreatePublicDnsNamespaceResponseTypeDef
):
    """
    Type definition for `ClientCreatePublicDnsNamespace` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientCreateServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientCreateServiceDnsConfigDnsRecordsTypeDef", {"Type": str, "TTL": int}
)


class ClientCreateServiceDnsConfigDnsRecordsTypeDef(
    _ClientCreateServiceDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ClientCreateServiceDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want AWS
    Cloud Map to create when you register an instance.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the resource, which indicates the type of value that Route 53 returns in
      response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one AAAA,
      and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other
      records. This is a limitation of DNS: you can't create a CNAME record and any other type of
      record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you
      register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register
      an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register an
      instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If
      you do, the request will fail with an ``InvalidInput`` error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.

      * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT``
      attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
      ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the
      same name as the value of ``service-hostname`` in the SRV record. You can ignore these
      records.

    - **TTL** *(integer) --* **[REQUIRED]**

      The amount of time, in seconds, that you want DNS resolvers to cache the settings for this
      record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that
        an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute
        when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify
        a TTL for the service; you can use a service to register instances that create either
        alias or non-alias records.
    """


_RequiredClientCreateServiceDnsConfigTypeDef = TypedDict(
    "_RequiredClientCreateServiceDnsConfigTypeDef",
    {"DnsRecords": List[ClientCreateServiceDnsConfigDnsRecordsTypeDef]},
)
_OptionalClientCreateServiceDnsConfigTypeDef = TypedDict(
    "_OptionalClientCreateServiceDnsConfigTypeDef",
    {"NamespaceId": str, "RoutingPolicy": str},
    total=False,
)


class ClientCreateServiceDnsConfigTypeDef(
    _RequiredClientCreateServiceDnsConfigTypeDef,
    _OptionalClientCreateServiceDnsConfigTypeDef,
):
    """
    Type definition for `ClientCreateService` `DnsConfig`

    A complex type that contains information about the Amazon Route 53 records that you want AWS
    Cloud Map to create when you register an instance.

    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.

    - **RoutingPolicy** *(string) --*

      The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
      creates when you register an instance and specify this service.

      .. note::

        If you want to use this service to register instances that create alias records, specify
        ``WEIGHTED`` for the routing policy.

      You can specify the following values:

       **MULTIVALUE**

      If you define a health check for the service and the health check is healthy, Route 53 returns
      the applicable value for up to eight instances.

      For example, suppose the service includes configurations for one A record and a health check,
      and you use the service to register 10 instances. Route 53 responds to DNS queries with IP
      addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route
      53 responds to every DNS query with the IP addresses for all of the healthy instances.

      If you don't define a health check for the service, Route 53 assumes that all instances are
      healthy and returns the values for up to eight instances.

      For more information about the multivalue routing policy, see `Multivalue Answer Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
      in the *Route 53 Developer Guide* .

       **WEIGHTED**

      Route 53 returns the applicable value from one randomly selected instance from among the
      instances that you registered using the same service. Currently, all records have the same
      weight, so you can't route more or less traffic to any instances.

      For example, suppose the service includes configurations for one A record and a health check,
      and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP
      address for one randomly selected instance from among the healthy instances. If no instances
      are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.

      If you don't define a health check for the service, Route 53 assumes that all instances are
      healthy and returns the applicable value for one randomly selected instance.

      For more information about the weighted routing policy, see `Weighted Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
      in the *Route 53 Developer Guide* .

    - **DnsRecords** *(list) --* **[REQUIRED]**

      An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you want AWS
      Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want AWS
        Cloud Map to create when you register an instance.

        - **Type** *(string) --* **[REQUIRED]**

          The type of the resource, which indicates the type of value that Route 53 returns in
          response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one AAAA,
          and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other
          records. This is a limitation of DNS: you can't create a CNAME record and any other type of
          record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you
          register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register
          an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register an
          instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If
          you do, the request will fail with an ``InvalidInput`` error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.

          * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT``
          attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
          ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the
          same name as the value of ``service-hostname`` in the SRV record. You can ignore these
          records.

        - **TTL** *(integer) --* **[REQUIRED]**

          The amount of time, in seconds, that you want DNS resolvers to cache the settings for this
          record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that
            an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute
            when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify
            a TTL for the service; you can use a service to register instances that create either
            alias or non-alias records.
    """


_RequiredClientCreateServiceHealthCheckConfigTypeDef = TypedDict(
    "_RequiredClientCreateServiceHealthCheckConfigTypeDef", {"Type": str}
)
_OptionalClientCreateServiceHealthCheckConfigTypeDef = TypedDict(
    "_OptionalClientCreateServiceHealthCheckConfigTypeDef",
    {"ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientCreateServiceHealthCheckConfigTypeDef(
    _RequiredClientCreateServiceHealthCheckConfigTypeDef,
    _OptionalClientCreateServiceHealthCheckConfigTypeDef,
):
    """
    Type definition for `ClientCreateService` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional Route 53
     health check. If you specify settings for a health check, AWS Cloud Map associates the health
     check with all the Route 53 DNS records that you specify in ``DnsConfig`` .

    .. warning::

      If you specify a health check configuration, you can specify either ``HealthCheckCustomConfig``
      or ``HealthCheckConfig`` but not both.

    For information about the charges for health checks, see `AWS Cloud Map Pricing
    <http://aws.amazon.com/cloud-map/pricing/>`__ .

    - **Type** *(string) --* **[REQUIRED]**

      The type of health check that you want to create, which indicates how Route 53 determines
      whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
      HTTP request and waits for an HTTP status code of 200 or greater and less than 400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
      HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for ``Type`` ,
      don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can be any
      value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint
      is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds
      the DNS name for the service. If you don't specify a value for ``ResourcePath`` , the default
      value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath`` .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53 to
      change the current status of the endpoint from unhealthy to healthy or vice versa. For more
      information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_ClientCreateServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientCreateServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientCreateServiceHealthCheckCustomConfigTypeDef(
    _ClientCreateServiceHealthCheckCustomConfigTypeDef
):
    """
    Type definition for `ClientCreateService` `HealthCheckCustomConfig`

    A complex type that contains information about an optional custom health check.

    .. warning::

      If you specify a health check configuration, you can specify either ``HealthCheckCustomConfig``
      or ``HealthCheckConfig`` but not both.

    - **FailureThreshold** *(integer) --*

      The number of 30-second intervals that you want Cloud Map to wait after receiving an
      ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a service
      instance. For example, suppose you specify a value of ``2`` for ``FailureTheshold`` , and then
      your application sends an ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for
      approximately 60 seconds (2 x 30) before changing the status of the service instance based on
      that request.

      Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same value
      before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change. Cloud Map
      still waits ``FailureThreshold x 30`` seconds after the first request to make the change.
    """


_ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": str, "TTL": int},
    total=False,
)


class ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef(
    _ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ClientCreateServiceResponseServiceDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want
    AWS Cloud Map to create when you register an instance.

    - **Type** *(string) --*

      The type of the resource, which indicates the type of value that Route 53 returns in
      response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
      AAAA, and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
      other records. This is a limitation of DNS: you can't create a CNAME record and any
      other type of record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
      you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
      register an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register an
      instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for
      ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
      error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
      changed.

      * The value of ``port`` comes from the value that you specify for the
      ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
      ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
      the same name as the value of ``service-hostname`` in the SRV record. You can ignore
      these records.

    - **TTL** *(integer) --*

      The amount of time, in seconds, that you want DNS resolvers to cache the settings for
      this record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS
        resource that an alias record routes traffic to. If you include the
        ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
        ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
        service to register instances that create either alias or non-alias records.
    """


_ClientCreateServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": str,
        "DnsRecords": List[
            ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef
        ],
    },
    total=False,
)


class ClientCreateServiceResponseServiceDnsConfigTypeDef(
    _ClientCreateServiceResponseServiceDnsConfigTypeDef
):
    """
    Type definition for `ClientCreateServiceResponseService` `DnsConfig`

    A complex type that contains information about the Route 53 DNS records that you want AWS
    Cloud Map to create when you register an instance.

    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.

    - **RoutingPolicy** *(string) --*

      The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
      creates when you register an instance and specify this service.

      .. note::

        If you want to use this service to register instances that create alias records,
        specify ``WEIGHTED`` for the routing policy.

      You can specify the following values:

       **MULTIVALUE**

      If you define a health check for the service and the health check is healthy, Route 53
      returns the applicable value for up to eight instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS queries
      with IP addresses for up to eight healthy instances. If fewer than eight instances are
      healthy, Route 53 responds to every DNS query with the IP addresses for all of the
      healthy instances.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the values for up to eight instances.

      For more information about the multivalue routing policy, see `Multivalue Answer Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
      in the *Route 53 Developer Guide* .

       **WEIGHTED**

      Route 53 returns the applicable value from one randomly selected instance from among the
      instances that you registered using the same service. Currently, all records have the
      same weight, so you can't route more or less traffic to any instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS queries
      with the IP address for one randomly selected instance from among the healthy instances.
      If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
      were healthy.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the applicable value for one randomly selected instance.

      For more information about the weighted routing policy, see `Weighted Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
      in the *Route 53 Developer Guide* .

    - **DnsRecords** *(list) --*

      An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
      want AWS Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want
        AWS Cloud Map to create when you register an instance.

        - **Type** *(string) --*

          The type of the resource, which indicates the type of value that Route 53 returns in
          response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
          AAAA, and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
          other records. This is a limitation of DNS: you can't create a CNAME record and any
          other type of record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
          you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
          register an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register an
          instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for
          ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
          error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
          changed.

          * The value of ``port`` comes from the value that you specify for the
          ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
          ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
          the same name as the value of ``service-hostname`` in the SRV record. You can ignore
          these records.

        - **TTL** *(integer) --*

          The amount of time, in seconds, that you want DNS resolvers to cache the settings for
          this record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS
            resource that an alias record routes traffic to. If you include the
            ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
            ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
            service to register instances that create either alias or non-alias records.
    """


_ClientCreateServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": str, "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientCreateServiceResponseServiceHealthCheckConfigTypeDef(
    _ClientCreateServiceResponseServiceHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientCreateServiceResponseService` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional health
     check. If you specify settings for a health check, AWS Cloud Map associates the health
     check with the records that you specify in ``DnsConfig`` .

    For information about the charges for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Route 53 determines
      whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
      400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
      than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
         later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
      ``Type`` , don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can be
      any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
      endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
      automatically adds the DNS name for the service. If you don't specify a value for
      ``ResourcePath`` , the default value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
      .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53
      to change the current status of the endpoint from unhealthy to healthy or vice versa. For
      more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef(
    _ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef
):
    """
    Type definition for `ClientCreateServiceResponseService` `HealthCheckCustomConfig`

    A complex type that contains information about an optional custom health check.

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    - **FailureThreshold** *(integer) --*

      The number of 30-second intervals that you want Cloud Map to wait after receiving an
      ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
      service instance. For example, suppose you specify a value of ``2`` for
      ``FailureTheshold`` , and then your application sends an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
      seconds (2 x 30) before changing the status of the service instance based on that request.

      Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
      value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
      Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
      the change.
    """


_ClientCreateServiceResponseServiceTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientCreateServiceResponseServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientCreateServiceResponseServiceHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientCreateServiceResponseServiceTypeDef(
    _ClientCreateServiceResponseServiceTypeDef
):
    """
    Type definition for `ClientCreateServiceResponse` `Service`

    A complex type that contains information about the new service.

    - **Id** *(string) --*

      The ID that AWS Cloud Map assigned to the service when you created it.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.

    - **Name** *(string) --*

      The name of the service.

    - **NamespaceId** *(string) --*

      The ID of the namespace that was used to create the service.

    - **Description** *(string) --*

      The description of the service.

    - **InstanceCount** *(integer) --*

      The number of instances that are currently associated with the service. Instances that were
      previously associated with the service but that have been deleted are not included in the
      count.

    - **DnsConfig** *(dict) --*

      A complex type that contains information about the Route 53 DNS records that you want AWS
      Cloud Map to create when you register an instance.

      - **NamespaceId** *(string) --*

        The ID of the namespace to use for DNS configuration.

      - **RoutingPolicy** *(string) --*

        The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
        creates when you register an instance and specify this service.

        .. note::

          If you want to use this service to register instances that create alias records,
          specify ``WEIGHTED`` for the routing policy.

        You can specify the following values:

         **MULTIVALUE**

        If you define a health check for the service and the health check is healthy, Route 53
        returns the applicable value for up to eight instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS queries
        with IP addresses for up to eight healthy instances. If fewer than eight instances are
        healthy, Route 53 responds to every DNS query with the IP addresses for all of the
        healthy instances.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the values for up to eight instances.

        For more information about the multivalue routing policy, see `Multivalue Answer Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
        in the *Route 53 Developer Guide* .

         **WEIGHTED**

        Route 53 returns the applicable value from one randomly selected instance from among the
        instances that you registered using the same service. Currently, all records have the
        same weight, so you can't route more or less traffic to any instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS queries
        with the IP address for one randomly selected instance from among the healthy instances.
        If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
        were healthy.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the applicable value for one randomly selected instance.

        For more information about the weighted routing policy, see `Weighted Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
        in the *Route 53 Developer Guide* .

      - **DnsRecords** *(list) --*

        An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
        want AWS Cloud Map to create when you register an instance.

        - *(dict) --*

          A complex type that contains information about the Route 53 DNS records that you want
          AWS Cloud Map to create when you register an instance.

          - **Type** *(string) --*

            The type of the resource, which indicates the type of value that Route 53 returns in
            response to DNS queries.

            Note the following:

            * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
            AAAA, and one SRV record. You can specify them in any combination.

            * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
            other records. This is a limitation of DNS: you can't create a CNAME record and any
            other type of record that has the same name as a CNAME record.

            * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
            you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

            * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
            register an instance.

            The following values are supported:

             **A**

            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

             **AAAA**

            Route 53 returns the IP address of the resource in IPv6 format, such as
            2001:0db8:85a3:0000:0000:abcd:0001:2345.

             **CNAME**

            Route 53 returns the domain name of the resource, such as www.example.com. Note the
            following:

            * You specify the domain name that you want to route traffic to when you register an
            instance. For more information, see  RegisterInstanceRequest$Attributes .

            * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

            * You can't specify both ``CNAME`` for ``Type`` and settings for
            ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
            error.

             **SRV**

            Route 53 returns the value for an SRV record. The value for an SRV record uses the
            following values:

             ``priority weight port service-hostname``

            Note the following about the values:

            * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
            changed.

            * The value of ``port`` comes from the value that you specify for the
            ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

            * The value of ``service-hostname`` is a concatenation of the following values:

              * The value that you specify for ``InstanceId`` when you register an instance.

              * The name of the service.

              * The name of the namespace.

            For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
            ``backend`` , and the name of the namespace is ``example.com`` , the value of
            ``service-hostname`` is:

             ``test.backend.example.com``

            If you specify settings for an SRV record and if you specify values for
            ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
            request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
            the same name as the value of ``service-hostname`` in the SRV record. You can ignore
            these records.

          - **TTL** *(integer) --*

            The amount of time, in seconds, that you want DNS resolvers to cache the settings for
            this record.

            .. note::

              Alias records don't include a TTL because Route 53 uses the TTL for the AWS
              resource that an alias record routes traffic to. If you include the
              ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
              ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
              service to register instances that create either alias or non-alias records.

    - **HealthCheckConfig** *(dict) --*

       *Public DNS namespaces only.* A complex type that contains settings for an optional health
       check. If you specify settings for a health check, AWS Cloud Map associates the health
       check with the records that you specify in ``DnsConfig`` .

      For information about the charges for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Route 53 determines
        whether an endpoint is healthy.

        .. warning::

          You can't change the value of ``Type`` after you create a health check.

        You can create the following types of health checks:

        * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
        400.

        * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
        than 400.

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
           later.

        * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
        ``Type`` , don't specify a value for ``ResourcePath`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path that you want Route 53 to request when performing health checks. The path can be
        any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
        endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
        automatically adds the DNS name for the service. If you don't specify a value for
        ``ResourcePath`` , the default value is ``/`` .

        If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
        .

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Route 53
        to change the current status of the endpoint from unhealthy to healthy or vice versa. For
        more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

    - **HealthCheckCustomConfig** *(dict) --*

      A complex type that contains information about an optional custom health check.

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      - **FailureThreshold** *(integer) --*

        The number of 30-second intervals that you want Cloud Map to wait after receiving an
        ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
        service instance. For example, suppose you specify a value of ``2`` for
        ``FailureTheshold`` , and then your application sends an
        ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
        seconds (2 x 30) before changing the status of the service instance based on that request.

        Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
        value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
        Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
        the change.

    - **CreateDate** *(datetime) --*

      The date and time that the service was created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
      ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and that allows failed requests to be retried
      without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique
      string, for example, a date/time stamp.
    """


_ClientCreateServiceResponseTypeDef = TypedDict(
    "_ClientCreateServiceResponseTypeDef",
    {"Service": ClientCreateServiceResponseServiceTypeDef},
    total=False,
)


class ClientCreateServiceResponseTypeDef(_ClientCreateServiceResponseTypeDef):
    """
    Type definition for `ClientCreateService` `Response`

    - **Service** *(dict) --*

      A complex type that contains information about the new service.

      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.

      - **Name** *(string) --*

        The name of the service.

      - **NamespaceId** *(string) --*

        The ID of the namespace that was used to create the service.

      - **Description** *(string) --*

        The description of the service.

      - **InstanceCount** *(integer) --*

        The number of instances that are currently associated with the service. Instances that were
        previously associated with the service but that have been deleted are not included in the
        count.

      - **DnsConfig** *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want AWS
        Cloud Map to create when you register an instance.

        - **NamespaceId** *(string) --*

          The ID of the namespace to use for DNS configuration.

        - **RoutingPolicy** *(string) --*

          The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
          creates when you register an instance and specify this service.

          .. note::

            If you want to use this service to register instances that create alias records,
            specify ``WEIGHTED`` for the routing policy.

          You can specify the following values:

           **MULTIVALUE**

          If you define a health check for the service and the health check is healthy, Route 53
          returns the applicable value for up to eight instances.

          For example, suppose the service includes configurations for one A record and a health
          check, and you use the service to register 10 instances. Route 53 responds to DNS queries
          with IP addresses for up to eight healthy instances. If fewer than eight instances are
          healthy, Route 53 responds to every DNS query with the IP addresses for all of the
          healthy instances.

          If you don't define a health check for the service, Route 53 assumes that all instances
          are healthy and returns the values for up to eight instances.

          For more information about the multivalue routing policy, see `Multivalue Answer Routing
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
          in the *Route 53 Developer Guide* .

           **WEIGHTED**

          Route 53 returns the applicable value from one randomly selected instance from among the
          instances that you registered using the same service. Currently, all records have the
          same weight, so you can't route more or less traffic to any instances.

          For example, suppose the service includes configurations for one A record and a health
          check, and you use the service to register 10 instances. Route 53 responds to DNS queries
          with the IP address for one randomly selected instance from among the healthy instances.
          If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
          were healthy.

          If you don't define a health check for the service, Route 53 assumes that all instances
          are healthy and returns the applicable value for one randomly selected instance.

          For more information about the weighted routing policy, see `Weighted Routing
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
          in the *Route 53 Developer Guide* .

        - **DnsRecords** *(list) --*

          An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
          want AWS Cloud Map to create when you register an instance.

          - *(dict) --*

            A complex type that contains information about the Route 53 DNS records that you want
            AWS Cloud Map to create when you register an instance.

            - **Type** *(string) --*

              The type of the resource, which indicates the type of value that Route 53 returns in
              response to DNS queries.

              Note the following:

              * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
              AAAA, and one SRV record. You can specify them in any combination.

              * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
              other records. This is a limitation of DNS: you can't create a CNAME record and any
              other type of record that has the same name as a CNAME record.

              * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
              you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

              * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
              register an instance.

              The following values are supported:

               **A**

              Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

               **AAAA**

              Route 53 returns the IP address of the resource in IPv6 format, such as
              2001:0db8:85a3:0000:0000:abcd:0001:2345.

               **CNAME**

              Route 53 returns the domain name of the resource, such as www.example.com. Note the
              following:

              * You specify the domain name that you want to route traffic to when you register an
              instance. For more information, see  RegisterInstanceRequest$Attributes .

              * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

              * You can't specify both ``CNAME`` for ``Type`` and settings for
              ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
              error.

               **SRV**

              Route 53 returns the value for an SRV record. The value for an SRV record uses the
              following values:

               ``priority weight port service-hostname``

              Note the following about the values:

              * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
              changed.

              * The value of ``port`` comes from the value that you specify for the
              ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

              * The value of ``service-hostname`` is a concatenation of the following values:

                * The value that you specify for ``InstanceId`` when you register an instance.

                * The name of the service.

                * The name of the namespace.

              For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
              ``backend`` , and the name of the namespace is ``example.com`` , the value of
              ``service-hostname`` is:

               ``test.backend.example.com``

              If you specify settings for an SRV record and if you specify values for
              ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
              request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
              the same name as the value of ``service-hostname`` in the SRV record. You can ignore
              these records.

            - **TTL** *(integer) --*

              The amount of time, in seconds, that you want DNS resolvers to cache the settings for
              this record.

              .. note::

                Alias records don't include a TTL because Route 53 uses the TTL for the AWS
                resource that an alias record routes traffic to. If you include the
                ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
                ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
                service to register instances that create either alias or non-alias records.

      - **HealthCheckConfig** *(dict) --*

         *Public DNS namespaces only.* A complex type that contains settings for an optional health
         check. If you specify settings for a health check, AWS Cloud Map associates the health
         check with the records that you specify in ``DnsConfig`` .

        For information about the charges for health checks, see `Amazon Route 53 Pricing
        <http://aws.amazon.com/route53/pricing/>`__ .

        - **Type** *(string) --*

          The type of health check that you want to create, which indicates how Route 53 determines
          whether an endpoint is healthy.

          .. warning::

            You can't change the value of ``Type`` after you create a health check.

          You can create the following types of health checks:

          * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
          submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
          400.

          * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
          submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
          than 400.

          .. warning::

             If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
             later.

          * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
          ``Type`` , don't specify a value for ``ResourcePath`` .

          For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Route 53 Developer Guide* .

        - **ResourcePath** *(string) --*

          The path that you want Route 53 to request when performing health checks. The path can be
          any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
          endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
          automatically adds the DNS name for the service. If you don't specify a value for
          ``ResourcePath`` , the default value is ``/`` .

          If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
          .

        - **FailureThreshold** *(integer) --*

          The number of consecutive health checks that an endpoint must pass or fail for Route 53
          to change the current status of the endpoint from unhealthy to healthy or vice versa. For
          more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Route 53 Developer Guide* .

      - **HealthCheckCustomConfig** *(dict) --*

        A complex type that contains information about an optional custom health check.

        .. warning::

          If you specify a health check configuration, you can specify either
          ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

        - **FailureThreshold** *(integer) --*

          The number of 30-second intervals that you want Cloud Map to wait after receiving an
          ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
          service instance. For example, suppose you specify a value of ``2`` for
          ``FailureTheshold`` , and then your application sends an
          ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
          seconds (2 x 30) before changing the status of the service instance based on that request.

          Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
          value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
          Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
          the change.

      - **CreateDate** *(datetime) --*

        The date and time that the service was created, in Unix format and Coordinated Universal
        Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
        ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request and that allows failed requests to be retried
        without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique
        string, for example, a date/time stamp.
    """


_ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "_ClientDeleteNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeleteNamespaceResponseTypeDef(_ClientDeleteNamespaceResponseTypeDef):
    """
    Type definition for `ClientDeleteNamespace` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientDeregisterInstanceResponseTypeDef = TypedDict(
    "_ClientDeregisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeregisterInstanceResponseTypeDef(_ClientDeregisterInstanceResponseTypeDef):
    """
    Type definition for `ClientDeregisterInstance` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. For more
      information, see  GetOperation .
    """


_ClientDiscoverInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientDiscoverInstancesResponseInstancesTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientDiscoverInstancesResponseInstancesTypeDef(
    _ClientDiscoverInstancesResponseInstancesTypeDef
):
    """
    Type definition for `ClientDiscoverInstancesResponse` `Instances`

    In a response to a  DiscoverInstance request, ``HttpInstanceSummary`` contains information
    about one instance that matches the values that you specified in the request.

    - **InstanceId** *(string) --*

      The ID of an instance that matches the values that you specified in the request.

    - **NamespaceName** *(string) --*

      The name of the namespace that you specified when you registered the instance.

    - **ServiceName** *(string) --*

      The name of the service that you specified when you registered the instance.

    - **HealthStatus** *(string) --*

      If you configured health checking in the service, the current health status of the
      service instance.

    - **Attributes** *(dict) --*

      If you included any attributes when you registered the instance, the values of those
      attributes.

      - *(string) --*

        - *(string) --*
    """


_ClientDiscoverInstancesResponseTypeDef = TypedDict(
    "_ClientDiscoverInstancesResponseTypeDef",
    {"Instances": List[ClientDiscoverInstancesResponseInstancesTypeDef]},
    total=False,
)


class ClientDiscoverInstancesResponseTypeDef(_ClientDiscoverInstancesResponseTypeDef):
    """
    Type definition for `ClientDiscoverInstances` `Response`

    - **Instances** *(list) --*

      A complex type that contains one ``HttpInstanceSummary`` for each registered instance.

      - *(dict) --*

        In a response to a  DiscoverInstance request, ``HttpInstanceSummary`` contains information
        about one instance that matches the values that you specified in the request.

        - **InstanceId** *(string) --*

          The ID of an instance that matches the values that you specified in the request.

        - **NamespaceName** *(string) --*

          The name of the namespace that you specified when you registered the instance.

        - **ServiceName** *(string) --*

          The name of the service that you specified when you registered the instance.

        - **HealthStatus** *(string) --*

          If you configured health checking in the service, the current health status of the
          service instance.

        - **Attributes** *(dict) --*

          If you included any attributes when you registered the instance, the values of those
          attributes.

          - *(string) --*

            - *(string) --*
    """


_ClientGetInstanceResponseInstanceTypeDef = TypedDict(
    "_ClientGetInstanceResponseInstanceTypeDef",
    {"Id": str, "CreatorRequestId": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientGetInstanceResponseInstanceTypeDef(
    _ClientGetInstanceResponseInstanceTypeDef
):
    """
    Type definition for `ClientGetInstanceResponse` `Instance`

    A complex type that contains information about a specified instance.

    - **Id** *(string) --*

      An identifier that you want to associate with the instance. Note the following:

      * If the service that is specified by ``ServiceId`` includes settings for an SRV record,
      the value of ``InstanceId`` is automatically included as part of the value for the SRV
      record. For more information, see  DnsRecord$Type .

      * You can use this value to update an existing instance.

      * To register a new instance, you must specify a value that is unique among instances that
      you register by using the same service.

      * If you specify an existing ``InstanceId`` and ``ServiceId`` , AWS Cloud Map updates the
      existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the
      old health check and creates a new one.

      .. note::

         The health check isn't deleted immediately, so it will still appear for a while if you
         submit a ``ListHealthChecks`` request, for example.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and that allows failed ``RegisterInstance``
      requests to be retried without the risk of executing the operation twice. You must use a
      unique ``CreatorRequestId`` string every time you submit a ``RegisterInstance`` request if
      you're registering additional instances for the same namespace and service.
      ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.

    - **Attributes** *(dict) --*

      A string map that contains the following information for the service that you specify in
      ``ServiceId`` :

      * The attributes that apply to the records that are defined in the service.

      * For each attribute, the applicable value.

      Supported attribute keys include the following:

       **AWS_ALIAS_DNS_NAME**

      If you want AWS Cloud Map to create a Route 53 alias record that routes traffic to an
      Elastic Load Balancing load balancer, specify the DNS name that is associated with the load
      balancer. For information about how to get the DNS name, see "DNSName" in the topic
      `AliasTarget
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html>`__ .

      Note the following:

      * The configuration for the service that is specified by ``ServiceId`` must include
      settings for an A record, an AAAA record, or both.

      * In the service that is specified by ``ServiceId`` , the value of ``RoutingPolicy`` must
      be ``WEIGHTED`` .

      * If the service that is specified by ``ServiceId`` includes ``HealthCheckConfig``
      settings, AWS Cloud Map will create the health check, but it won't associate the health
      check with the alias record.

      * Auto naming currently doesn't support creating alias records that route traffic to AWS
      resources other than ELB load balancers.

      * If you specify a value for ``AWS_ALIAS_DNS_NAME`` , don't specify values for any of the
      ``AWS_INSTANCE`` attributes.

       **AWS_INSTANCE_CNAME**

      If the service configuration includes a CNAME record, the domain name that you want Route
      53 to return in response to DNS queries, for example, ``example.com`` .

      This value is required if the service specified by ``ServiceId`` includes settings for an
      CNAME record.

       **AWS_INSTANCE_IPV4**

      If the service configuration includes an A record, the IPv4 address that you want Route 53
      to return in response to DNS queries, for example, ``192.0.2.44`` .

      This value is required if the service specified by ``ServiceId`` includes settings for an A
      record. If the service includes settings for an SRV record, you must specify a value for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.

       **AWS_INSTANCE_IPV6**

      If the service configuration includes an AAAA record, the IPv6 address that you want Route
      53 to return in response to DNS queries, for example,
      ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

      This value is required if the service specified by ``ServiceId`` includes settings for an
      AAAA record. If the service includes settings for an SRV record, you must specify a value
      for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.

       **AWS_INSTANCE_PORT**

      If the service includes an SRV record, the value that you want Route 53 to return for the
      port.

      If the service includes ``HealthCheckConfig`` , the port on the endpoint that you want
      Route 53 to send requests to.

      This value is required if you specified settings for an SRV record when you created the
      service.

      - *(string) --*

        - *(string) --*
    """


_ClientGetInstanceResponseTypeDef = TypedDict(
    "_ClientGetInstanceResponseTypeDef",
    {"Instance": ClientGetInstanceResponseInstanceTypeDef},
    total=False,
)


class ClientGetInstanceResponseTypeDef(_ClientGetInstanceResponseTypeDef):
    """
    Type definition for `ClientGetInstance` `Response`

    - **Instance** *(dict) --*

      A complex type that contains information about a specified instance.

      - **Id** *(string) --*

        An identifier that you want to associate with the instance. Note the following:

        * If the service that is specified by ``ServiceId`` includes settings for an SRV record,
        the value of ``InstanceId`` is automatically included as part of the value for the SRV
        record. For more information, see  DnsRecord$Type .

        * You can use this value to update an existing instance.

        * To register a new instance, you must specify a value that is unique among instances that
        you register by using the same service.

        * If you specify an existing ``InstanceId`` and ``ServiceId`` , AWS Cloud Map updates the
        existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the
        old health check and creates a new one.

        .. note::

           The health check isn't deleted immediately, so it will still appear for a while if you
           submit a ``ListHealthChecks`` request, for example.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request and that allows failed ``RegisterInstance``
        requests to be retried without the risk of executing the operation twice. You must use a
        unique ``CreatorRequestId`` string every time you submit a ``RegisterInstance`` request if
        you're registering additional instances for the same namespace and service.
        ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.

      - **Attributes** *(dict) --*

        A string map that contains the following information for the service that you specify in
        ``ServiceId`` :

        * The attributes that apply to the records that are defined in the service.

        * For each attribute, the applicable value.

        Supported attribute keys include the following:

         **AWS_ALIAS_DNS_NAME**

        If you want AWS Cloud Map to create a Route 53 alias record that routes traffic to an
        Elastic Load Balancing load balancer, specify the DNS name that is associated with the load
        balancer. For information about how to get the DNS name, see "DNSName" in the topic
        `AliasTarget
        <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html>`__ .

        Note the following:

        * The configuration for the service that is specified by ``ServiceId`` must include
        settings for an A record, an AAAA record, or both.

        * In the service that is specified by ``ServiceId`` , the value of ``RoutingPolicy`` must
        be ``WEIGHTED`` .

        * If the service that is specified by ``ServiceId`` includes ``HealthCheckConfig``
        settings, AWS Cloud Map will create the health check, but it won't associate the health
        check with the alias record.

        * Auto naming currently doesn't support creating alias records that route traffic to AWS
        resources other than ELB load balancers.

        * If you specify a value for ``AWS_ALIAS_DNS_NAME`` , don't specify values for any of the
        ``AWS_INSTANCE`` attributes.

         **AWS_INSTANCE_CNAME**

        If the service configuration includes a CNAME record, the domain name that you want Route
        53 to return in response to DNS queries, for example, ``example.com`` .

        This value is required if the service specified by ``ServiceId`` includes settings for an
        CNAME record.

         **AWS_INSTANCE_IPV4**

        If the service configuration includes an A record, the IPv4 address that you want Route 53
        to return in response to DNS queries, for example, ``192.0.2.44`` .

        This value is required if the service specified by ``ServiceId`` includes settings for an A
        record. If the service includes settings for an SRV record, you must specify a value for
        ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.

         **AWS_INSTANCE_IPV6**

        If the service configuration includes an AAAA record, the IPv6 address that you want Route
        53 to return in response to DNS queries, for example,
        ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

        This value is required if the service specified by ``ServiceId`` includes settings for an
        AAAA record. If the service includes settings for an SRV record, you must specify a value
        for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.

         **AWS_INSTANCE_PORT**

        If the service includes an SRV record, the value that you want Route 53 to return for the
        port.

        If the service includes ``HealthCheckConfig`` , the port on the endpoint that you want
        Route 53 to send requests to.

        This value is required if you specified settings for an SRV record when you created the
        service.

        - *(string) --*

          - *(string) --*
    """


_ClientGetInstancesHealthStatusResponseTypeDef = TypedDict(
    "_ClientGetInstancesHealthStatusResponseTypeDef",
    {"Status": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientGetInstancesHealthStatusResponseTypeDef(
    _ClientGetInstancesHealthStatusResponseTypeDef
):
    """
    Type definition for `ClientGetInstancesHealthStatus` `Response`

    - **Status** *(dict) --*

      A complex type that contains the IDs and the health status of the instances that you
      specified in the ``GetInstancesHealthStatus`` request.

      - *(string) --*

        - *(string) --*

    - **NextToken** *(string) --*

      If more than ``MaxResults`` instances match the specified criteria, you can submit another
      ``GetInstancesHealthStatus`` request to get the next group of results. Specify the value of
      ``NextToken`` from the previous response in the next request.
    """


_ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef
):
    """
    Type definition for `ClientGetNamespaceResponseNamespaceProperties` `DnsProperties`

    A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
    creates when you create a namespace.

    - **HostedZoneId** *(string) --*

      The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
      namespace.
    """


_ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef
):
    """
    Type definition for `ClientGetNamespaceResponseNamespaceProperties` `HttpProperties`

    A complex type that contains the name of an HTTP namespace.

    - **HttpName** *(string) --*

      The name of an HTTP namespace.
    """


_ClientGetNamespaceResponseNamespacePropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesTypeDef",
    {
        "DnsProperties": ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesTypeDef
):
    """
    Type definition for `ClientGetNamespaceResponseNamespace` `Properties`

    A complex type that contains information that's specific to the type of the namespace.

    - **DnsProperties** *(dict) --*

      A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
      creates when you create a namespace.

      - **HostedZoneId** *(string) --*

        The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
        namespace.

    - **HttpProperties** *(dict) --*

      A complex type that contains the name of an HTTP namespace.

      - **HttpName** *(string) --*

        The name of an HTTP namespace.
    """


_ClientGetNamespaceResponseNamespaceTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespaceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": str,
        "Description": str,
        "ServiceCount": int,
        "Properties": ClientGetNamespaceResponseNamespacePropertiesTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetNamespaceResponseNamespaceTypeDef(
    _ClientGetNamespaceResponseNamespaceTypeDef
):
    """
    Type definition for `ClientGetNamespaceResponse` `Namespace`

    A complex type that contains information about the specified namespace.

    - **Id** *(string) --*

      The ID of a namespace.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you create
      it.

    - **Name** *(string) --*

      The name of the namespace, such as ``example.com`` .

    - **Type** *(string) --*

      The type of the namespace. Valid values are ``DNS_PUBLIC`` and ``DNS_PRIVATE`` .

    - **Description** *(string) --*

      The description that you specify for the namespace when you create it.

    - **ServiceCount** *(integer) --*

      The number of services that are associated with the namespace.

    - **Properties** *(dict) --*

      A complex type that contains information that's specific to the type of the namespace.

      - **DnsProperties** *(dict) --*

        A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
        creates when you create a namespace.

        - **HostedZoneId** *(string) --*

          The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
          namespace.

      - **HttpProperties** *(dict) --*

        A complex type that contains the name of an HTTP namespace.

        - **HttpName** *(string) --*

          The name of an HTTP namespace.

    - **CreateDate** *(datetime) --*

      The date that the namespace was created, in Unix date/time format and Coordinated Universal
      Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
      ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and that allows failed requests to be retried
      without the risk of executing an operation twice.
    """


_ClientGetNamespaceResponseTypeDef = TypedDict(
    "_ClientGetNamespaceResponseTypeDef",
    {"Namespace": ClientGetNamespaceResponseNamespaceTypeDef},
    total=False,
)


class ClientGetNamespaceResponseTypeDef(_ClientGetNamespaceResponseTypeDef):
    """
    Type definition for `ClientGetNamespace` `Response`

    - **Namespace** *(dict) --*

      A complex type that contains information about the specified namespace.

      - **Id** *(string) --*

        The ID of a namespace.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you create
        it.

      - **Name** *(string) --*

        The name of the namespace, such as ``example.com`` .

      - **Type** *(string) --*

        The type of the namespace. Valid values are ``DNS_PUBLIC`` and ``DNS_PRIVATE`` .

      - **Description** *(string) --*

        The description that you specify for the namespace when you create it.

      - **ServiceCount** *(integer) --*

        The number of services that are associated with the namespace.

      - **Properties** *(dict) --*

        A complex type that contains information that's specific to the type of the namespace.

        - **DnsProperties** *(dict) --*

          A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
          creates when you create a namespace.

          - **HostedZoneId** *(string) --*

            The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
            namespace.

        - **HttpProperties** *(dict) --*

          A complex type that contains the name of an HTTP namespace.

          - **HttpName** *(string) --*

            The name of an HTTP namespace.

      - **CreateDate** *(datetime) --*

        The date that the namespace was created, in Unix date/time format and Coordinated Universal
        Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
        ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request and that allows failed requests to be retried
        without the risk of executing an operation twice.
    """


_ClientGetOperationResponseOperationTypeDef = TypedDict(
    "_ClientGetOperationResponseOperationTypeDef",
    {
        "Id": str,
        "Type": str,
        "Status": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[str, str],
    },
    total=False,
)


class ClientGetOperationResponseOperationTypeDef(
    _ClientGetOperationResponseOperationTypeDef
):
    """
    Type definition for `ClientGetOperationResponse` `Operation`

    A complex type that contains information about the operation.

    - **Id** *(string) --*

      The ID of the operation that you want to get information about.

    - **Type** *(string) --*

      The name of the operation that is associated with the specified ID.

    - **Status** *(string) --*

      The status of the operation. Values include the following:

      * **SUBMITTED** : This is the initial state immediately after you submit a request.

      * **PENDING** : AWS Cloud Map is performing the operation.

      * **SUCCESS** : The operation succeeded.

      * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .

    - **ErrorMessage** *(string) --*

      If the value of ``Status`` is ``FAIL`` , the reason that the operation failed.

    - **ErrorCode** *(string) --*

      The code associated with ``ErrorMessage`` . Values for ``ErrorCode`` include the following:

      * ``ACCESS_DENIED``

      * ``CANNOT_CREATE_HOSTED_ZONE``

      * ``EXPIRED_TOKEN``

      * ``HOSTED_ZONE_NOT_FOUND``

      * ``INTERNAL_FAILURE``

      * ``INVALID_CHANGE_BATCH``

      * ``THROTTLED_REQUEST``

    - **CreateDate** *(datetime) --*

      The date and time that the request was submitted, in Unix date/time format and Coordinated
      Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example,
      the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

    - **UpdateDate** *(datetime) --*

      The date and time that the value of ``Status`` changed to the current value, in Unix
      date/time format and Coordinated Universal Time (UTC). The value of ``UpdateDate`` is
      accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday,
      January 26, 2018 12:11:30.087 AM.

    - **Targets** *(dict) --*

      The name of the target entity that is associated with the operation:

      * **NAMESPACE** : The namespace ID is returned in the ``ResourceId`` property.

      * **SERVICE** : The service ID is returned in the ``ResourceId`` property.

      * **INSTANCE** : The instance ID is returned in the ``ResourceId`` property.

      - *(string) --*

        - *(string) --*
    """


_ClientGetOperationResponseTypeDef = TypedDict(
    "_ClientGetOperationResponseTypeDef",
    {"Operation": ClientGetOperationResponseOperationTypeDef},
    total=False,
)


class ClientGetOperationResponseTypeDef(_ClientGetOperationResponseTypeDef):
    """
    Type definition for `ClientGetOperation` `Response`

    - **Operation** *(dict) --*

      A complex type that contains information about the operation.

      - **Id** *(string) --*

        The ID of the operation that you want to get information about.

      - **Type** *(string) --*

        The name of the operation that is associated with the specified ID.

      - **Status** *(string) --*

        The status of the operation. Values include the following:

        * **SUBMITTED** : This is the initial state immediately after you submit a request.

        * **PENDING** : AWS Cloud Map is performing the operation.

        * **SUCCESS** : The operation succeeded.

        * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .

      - **ErrorMessage** *(string) --*

        If the value of ``Status`` is ``FAIL`` , the reason that the operation failed.

      - **ErrorCode** *(string) --*

        The code associated with ``ErrorMessage`` . Values for ``ErrorCode`` include the following:

        * ``ACCESS_DENIED``

        * ``CANNOT_CREATE_HOSTED_ZONE``

        * ``EXPIRED_TOKEN``

        * ``HOSTED_ZONE_NOT_FOUND``

        * ``INTERNAL_FAILURE``

        * ``INVALID_CHANGE_BATCH``

        * ``THROTTLED_REQUEST``

      - **CreateDate** *(datetime) --*

        The date and time that the request was submitted, in Unix date/time format and Coordinated
        Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example,
        the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

      - **UpdateDate** *(datetime) --*

        The date and time that the value of ``Status`` changed to the current value, in Unix
        date/time format and Coordinated Universal Time (UTC). The value of ``UpdateDate`` is
        accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday,
        January 26, 2018 12:11:30.087 AM.

      - **Targets** *(dict) --*

        The name of the target entity that is associated with the operation:

        * **NAMESPACE** : The namespace ID is returned in the ``ResourceId`` property.

        * **SERVICE** : The service ID is returned in the ``ResourceId`` property.

        * **INSTANCE** : The instance ID is returned in the ``ResourceId`` property.

        - *(string) --*

          - *(string) --*
    """


_ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": str, "TTL": int},
    total=False,
)


class ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef(
    _ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ClientGetServiceResponseServiceDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want
    AWS Cloud Map to create when you register an instance.

    - **Type** *(string) --*

      The type of the resource, which indicates the type of value that Route 53 returns in
      response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
      AAAA, and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
      other records. This is a limitation of DNS: you can't create a CNAME record and any
      other type of record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
      you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
      register an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register an
      instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for
      ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
      error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
      changed.

      * The value of ``port`` comes from the value that you specify for the
      ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
      ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
      the same name as the value of ``service-hostname`` in the SRV record. You can ignore
      these records.

    - **TTL** *(integer) --*

      The amount of time, in seconds, that you want DNS resolvers to cache the settings for
      this record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS
        resource that an alias record routes traffic to. If you include the
        ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
        ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
        service to register instances that create either alias or non-alias records.
    """


_ClientGetServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": str,
        "DnsRecords": List[ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ClientGetServiceResponseServiceDnsConfigTypeDef(
    _ClientGetServiceResponseServiceDnsConfigTypeDef
):
    """
    Type definition for `ClientGetServiceResponseService` `DnsConfig`

    A complex type that contains information about the Route 53 DNS records that you want AWS
    Cloud Map to create when you register an instance.

    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.

    - **RoutingPolicy** *(string) --*

      The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
      creates when you register an instance and specify this service.

      .. note::

        If you want to use this service to register instances that create alias records,
        specify ``WEIGHTED`` for the routing policy.

      You can specify the following values:

       **MULTIVALUE**

      If you define a health check for the service and the health check is healthy, Route 53
      returns the applicable value for up to eight instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS queries
      with IP addresses for up to eight healthy instances. If fewer than eight instances are
      healthy, Route 53 responds to every DNS query with the IP addresses for all of the
      healthy instances.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the values for up to eight instances.

      For more information about the multivalue routing policy, see `Multivalue Answer Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
      in the *Route 53 Developer Guide* .

       **WEIGHTED**

      Route 53 returns the applicable value from one randomly selected instance from among the
      instances that you registered using the same service. Currently, all records have the
      same weight, so you can't route more or less traffic to any instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS queries
      with the IP address for one randomly selected instance from among the healthy instances.
      If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
      were healthy.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the applicable value for one randomly selected instance.

      For more information about the weighted routing policy, see `Weighted Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
      in the *Route 53 Developer Guide* .

    - **DnsRecords** *(list) --*

      An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
      want AWS Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want
        AWS Cloud Map to create when you register an instance.

        - **Type** *(string) --*

          The type of the resource, which indicates the type of value that Route 53 returns in
          response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
          AAAA, and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
          other records. This is a limitation of DNS: you can't create a CNAME record and any
          other type of record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
          you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
          register an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register an
          instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for
          ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
          error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
          changed.

          * The value of ``port`` comes from the value that you specify for the
          ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
          ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
          the same name as the value of ``service-hostname`` in the SRV record. You can ignore
          these records.

        - **TTL** *(integer) --*

          The amount of time, in seconds, that you want DNS resolvers to cache the settings for
          this record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS
            resource that an alias record routes traffic to. If you include the
            ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
            ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
            service to register instances that create either alias or non-alias records.
    """


_ClientGetServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": str, "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientGetServiceResponseServiceHealthCheckConfigTypeDef(
    _ClientGetServiceResponseServiceHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientGetServiceResponseService` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional health
     check. If you specify settings for a health check, AWS Cloud Map associates the health
     check with the records that you specify in ``DnsConfig`` .

    For information about the charges for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Route 53 determines
      whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
      400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
      than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
         later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
      ``Type`` , don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can be
      any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
      endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
      automatically adds the DNS name for the service. If you don't specify a value for
      ``ResourcePath`` , the default value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
      .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53
      to change the current status of the endpoint from unhealthy to healthy or vice versa. For
      more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef(
    _ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef
):
    """
    Type definition for `ClientGetServiceResponseService` `HealthCheckCustomConfig`

    A complex type that contains information about an optional custom health check.

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    - **FailureThreshold** *(integer) --*

      The number of 30-second intervals that you want Cloud Map to wait after receiving an
      ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
      service instance. For example, suppose you specify a value of ``2`` for
      ``FailureTheshold`` , and then your application sends an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
      seconds (2 x 30) before changing the status of the service instance based on that request.

      Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
      value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
      Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
      the change.
    """


_ClientGetServiceResponseServiceTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientGetServiceResponseServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientGetServiceResponseServiceHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetServiceResponseServiceTypeDef(_ClientGetServiceResponseServiceTypeDef):
    """
    Type definition for `ClientGetServiceResponse` `Service`

    A complex type that contains information about the service.

    - **Id** *(string) --*

      The ID that AWS Cloud Map assigned to the service when you created it.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.

    - **Name** *(string) --*

      The name of the service.

    - **NamespaceId** *(string) --*

      The ID of the namespace that was used to create the service.

    - **Description** *(string) --*

      The description of the service.

    - **InstanceCount** *(integer) --*

      The number of instances that are currently associated with the service. Instances that were
      previously associated with the service but that have been deleted are not included in the
      count.

    - **DnsConfig** *(dict) --*

      A complex type that contains information about the Route 53 DNS records that you want AWS
      Cloud Map to create when you register an instance.

      - **NamespaceId** *(string) --*

        The ID of the namespace to use for DNS configuration.

      - **RoutingPolicy** *(string) --*

        The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
        creates when you register an instance and specify this service.

        .. note::

          If you want to use this service to register instances that create alias records,
          specify ``WEIGHTED`` for the routing policy.

        You can specify the following values:

         **MULTIVALUE**

        If you define a health check for the service and the health check is healthy, Route 53
        returns the applicable value for up to eight instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS queries
        with IP addresses for up to eight healthy instances. If fewer than eight instances are
        healthy, Route 53 responds to every DNS query with the IP addresses for all of the
        healthy instances.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the values for up to eight instances.

        For more information about the multivalue routing policy, see `Multivalue Answer Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
        in the *Route 53 Developer Guide* .

         **WEIGHTED**

        Route 53 returns the applicable value from one randomly selected instance from among the
        instances that you registered using the same service. Currently, all records have the
        same weight, so you can't route more or less traffic to any instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS queries
        with the IP address for one randomly selected instance from among the healthy instances.
        If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
        were healthy.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the applicable value for one randomly selected instance.

        For more information about the weighted routing policy, see `Weighted Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
        in the *Route 53 Developer Guide* .

      - **DnsRecords** *(list) --*

        An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
        want AWS Cloud Map to create when you register an instance.

        - *(dict) --*

          A complex type that contains information about the Route 53 DNS records that you want
          AWS Cloud Map to create when you register an instance.

          - **Type** *(string) --*

            The type of the resource, which indicates the type of value that Route 53 returns in
            response to DNS queries.

            Note the following:

            * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
            AAAA, and one SRV record. You can specify them in any combination.

            * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
            other records. This is a limitation of DNS: you can't create a CNAME record and any
            other type of record that has the same name as a CNAME record.

            * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
            you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

            * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
            register an instance.

            The following values are supported:

             **A**

            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

             **AAAA**

            Route 53 returns the IP address of the resource in IPv6 format, such as
            2001:0db8:85a3:0000:0000:abcd:0001:2345.

             **CNAME**

            Route 53 returns the domain name of the resource, such as www.example.com. Note the
            following:

            * You specify the domain name that you want to route traffic to when you register an
            instance. For more information, see  RegisterInstanceRequest$Attributes .

            * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

            * You can't specify both ``CNAME`` for ``Type`` and settings for
            ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
            error.

             **SRV**

            Route 53 returns the value for an SRV record. The value for an SRV record uses the
            following values:

             ``priority weight port service-hostname``

            Note the following about the values:

            * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
            changed.

            * The value of ``port`` comes from the value that you specify for the
            ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

            * The value of ``service-hostname`` is a concatenation of the following values:

              * The value that you specify for ``InstanceId`` when you register an instance.

              * The name of the service.

              * The name of the namespace.

            For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
            ``backend`` , and the name of the namespace is ``example.com`` , the value of
            ``service-hostname`` is:

             ``test.backend.example.com``

            If you specify settings for an SRV record and if you specify values for
            ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
            request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
            the same name as the value of ``service-hostname`` in the SRV record. You can ignore
            these records.

          - **TTL** *(integer) --*

            The amount of time, in seconds, that you want DNS resolvers to cache the settings for
            this record.

            .. note::

              Alias records don't include a TTL because Route 53 uses the TTL for the AWS
              resource that an alias record routes traffic to. If you include the
              ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
              ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
              service to register instances that create either alias or non-alias records.

    - **HealthCheckConfig** *(dict) --*

       *Public DNS namespaces only.* A complex type that contains settings for an optional health
       check. If you specify settings for a health check, AWS Cloud Map associates the health
       check with the records that you specify in ``DnsConfig`` .

      For information about the charges for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Route 53 determines
        whether an endpoint is healthy.

        .. warning::

          You can't change the value of ``Type`` after you create a health check.

        You can create the following types of health checks:

        * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
        400.

        * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
        than 400.

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
           later.

        * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
        ``Type`` , don't specify a value for ``ResourcePath`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path that you want Route 53 to request when performing health checks. The path can be
        any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
        endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
        automatically adds the DNS name for the service. If you don't specify a value for
        ``ResourcePath`` , the default value is ``/`` .

        If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
        .

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Route 53
        to change the current status of the endpoint from unhealthy to healthy or vice versa. For
        more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

    - **HealthCheckCustomConfig** *(dict) --*

      A complex type that contains information about an optional custom health check.

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      - **FailureThreshold** *(integer) --*

        The number of 30-second intervals that you want Cloud Map to wait after receiving an
        ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
        service instance. For example, suppose you specify a value of ``2`` for
        ``FailureTheshold`` , and then your application sends an
        ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
        seconds (2 x 30) before changing the status of the service instance based on that request.

        Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
        value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
        Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
        the change.

    - **CreateDate** *(datetime) --*

      The date and time that the service was created, in Unix format and Coordinated Universal
      Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
      ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request and that allows failed requests to be retried
      without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique
      string, for example, a date/time stamp.
    """


_ClientGetServiceResponseTypeDef = TypedDict(
    "_ClientGetServiceResponseTypeDef",
    {"Service": ClientGetServiceResponseServiceTypeDef},
    total=False,
)


class ClientGetServiceResponseTypeDef(_ClientGetServiceResponseTypeDef):
    """
    Type definition for `ClientGetService` `Response`

    - **Service** *(dict) --*

      A complex type that contains information about the service.

      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.

      - **Name** *(string) --*

        The name of the service.

      - **NamespaceId** *(string) --*

        The ID of the namespace that was used to create the service.

      - **Description** *(string) --*

        The description of the service.

      - **InstanceCount** *(integer) --*

        The number of instances that are currently associated with the service. Instances that were
        previously associated with the service but that have been deleted are not included in the
        count.

      - **DnsConfig** *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want AWS
        Cloud Map to create when you register an instance.

        - **NamespaceId** *(string) --*

          The ID of the namespace to use for DNS configuration.

        - **RoutingPolicy** *(string) --*

          The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map
          creates when you register an instance and specify this service.

          .. note::

            If you want to use this service to register instances that create alias records,
            specify ``WEIGHTED`` for the routing policy.

          You can specify the following values:

           **MULTIVALUE**

          If you define a health check for the service and the health check is healthy, Route 53
          returns the applicable value for up to eight instances.

          For example, suppose the service includes configurations for one A record and a health
          check, and you use the service to register 10 instances. Route 53 responds to DNS queries
          with IP addresses for up to eight healthy instances. If fewer than eight instances are
          healthy, Route 53 responds to every DNS query with the IP addresses for all of the
          healthy instances.

          If you don't define a health check for the service, Route 53 assumes that all instances
          are healthy and returns the values for up to eight instances.

          For more information about the multivalue routing policy, see `Multivalue Answer Routing
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
          in the *Route 53 Developer Guide* .

           **WEIGHTED**

          Route 53 returns the applicable value from one randomly selected instance from among the
          instances that you registered using the same service. Currently, all records have the
          same weight, so you can't route more or less traffic to any instances.

          For example, suppose the service includes configurations for one A record and a health
          check, and you use the service to register 10 instances. Route 53 responds to DNS queries
          with the IP address for one randomly selected instance from among the healthy instances.
          If no instances are healthy, Route 53 responds to DNS queries as if all of the instances
          were healthy.

          If you don't define a health check for the service, Route 53 assumes that all instances
          are healthy and returns the applicable value for one randomly selected instance.

          For more information about the weighted routing policy, see `Weighted Routing
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
          in the *Route 53 Developer Guide* .

        - **DnsRecords** *(list) --*

          An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
          want AWS Cloud Map to create when you register an instance.

          - *(dict) --*

            A complex type that contains information about the Route 53 DNS records that you want
            AWS Cloud Map to create when you register an instance.

            - **Type** *(string) --*

              The type of the resource, which indicates the type of value that Route 53 returns in
              response to DNS queries.

              Note the following:

              * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
              AAAA, and one SRV record. You can specify them in any combination.

              * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
              other records. This is a limitation of DNS: you can't create a CNAME record and any
              other type of record that has the same name as a CNAME record.

              * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when
              you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

              * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
              register an instance.

              The following values are supported:

               **A**

              Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

               **AAAA**

              Route 53 returns the IP address of the resource in IPv6 format, such as
              2001:0db8:85a3:0000:0000:abcd:0001:2345.

               **CNAME**

              Route 53 returns the domain name of the resource, such as www.example.com. Note the
              following:

              * You specify the domain name that you want to route traffic to when you register an
              instance. For more information, see  RegisterInstanceRequest$Attributes .

              * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

              * You can't specify both ``CNAME`` for ``Type`` and settings for
              ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
              error.

               **SRV**

              Route 53 returns the value for an SRV record. The value for an SRV record uses the
              following values:

               ``priority weight port service-hostname``

              Note the following about the values:

              * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
              changed.

              * The value of ``port`` comes from the value that you specify for the
              ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

              * The value of ``service-hostname`` is a concatenation of the following values:

                * The value that you specify for ``InstanceId`` when you register an instance.

                * The name of the service.

                * The name of the namespace.

              For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
              ``backend`` , and the name of the namespace is ``example.com`` , the value of
              ``service-hostname`` is:

               ``test.backend.example.com``

              If you specify settings for an SRV record and if you specify values for
              ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
              request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have
              the same name as the value of ``service-hostname`` in the SRV record. You can ignore
              these records.

            - **TTL** *(integer) --*

              The amount of time, in seconds, that you want DNS resolvers to cache the settings for
              this record.

              .. note::

                Alias records don't include a TTL because Route 53 uses the TTL for the AWS
                resource that an alias record routes traffic to. If you include the
                ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
                ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
                service to register instances that create either alias or non-alias records.

      - **HealthCheckConfig** *(dict) --*

         *Public DNS namespaces only.* A complex type that contains settings for an optional health
         check. If you specify settings for a health check, AWS Cloud Map associates the health
         check with the records that you specify in ``DnsConfig`` .

        For information about the charges for health checks, see `Amazon Route 53 Pricing
        <http://aws.amazon.com/route53/pricing/>`__ .

        - **Type** *(string) --*

          The type of health check that you want to create, which indicates how Route 53 determines
          whether an endpoint is healthy.

          .. warning::

            You can't change the value of ``Type`` after you create a health check.

          You can create the following types of health checks:

          * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
          submits an HTTP request and waits for an HTTP status code of 200 or greater and less than
          400.

          * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
          submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
          than 400.

          .. warning::

             If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
             later.

          * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
          ``Type`` , don't specify a value for ``ResourcePath`` .

          For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Route 53 Developer Guide* .

        - **ResourcePath** *(string) --*

          The path that you want Route 53 to request when performing health checks. The path can be
          any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the
          endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53
          automatically adds the DNS name for the service. If you don't specify a value for
          ``ResourcePath`` , the default value is ``/`` .

          If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath``
          .

        - **FailureThreshold** *(integer) --*

          The number of consecutive health checks that an endpoint must pass or fail for Route 53
          to change the current status of the endpoint from unhealthy to healthy or vice versa. For
          more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Route 53 Developer Guide* .

      - **HealthCheckCustomConfig** *(dict) --*

        A complex type that contains information about an optional custom health check.

        .. warning::

          If you specify a health check configuration, you can specify either
          ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

        - **FailureThreshold** *(integer) --*

          The number of 30-second intervals that you want Cloud Map to wait after receiving an
          ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
          service instance. For example, suppose you specify a value of ``2`` for
          ``FailureTheshold`` , and then your application sends an
          ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
          seconds (2 x 30) before changing the status of the service instance based on that request.

          Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same
          value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change.
          Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make
          the change.

      - **CreateDate** *(datetime) --*

        The date and time that the service was created, in Unix format and Coordinated Universal
        Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value
        ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request and that allows failed requests to be retried
        without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique
        string, for example, a date/time stamp.
    """


_ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListInstancesResponseInstancesTypeDef(
    _ClientListInstancesResponseInstancesTypeDef
):
    """
    Type definition for `ClientListInstancesResponse` `Instances`

    A complex type that contains information about the instances that you registered by using a
    specified service.

    - **Id** *(string) --*

      The ID for an instance that you created by using a specified service.

    - **Attributes** *(dict) --*

      A string map that contains the following information:

      * The attributes that are associate with the instance.

      * For each attribute, the applicable value.

      Supported attribute keys include the following:

      * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load
      Balancing load balancer, the DNS name that is associated with the load balancer.

      * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in
      response to DNS queries, for example, ``example.com`` .

      * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in
      response to DNS queries, for example, ``192.0.2.44`` .

      * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in
      response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

      * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the
      port. In addition, if the service includes ``HealthCheckConfig`` , the port on the
      endpoint that Route 53 sends requests to.

      - *(string) --*

        - *(string) --*
    """


_ClientListInstancesResponseTypeDef = TypedDict(
    "_ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "NextToken": str},
    total=False,
)


class ClientListInstancesResponseTypeDef(_ClientListInstancesResponseTypeDef):
    """
    Type definition for `ClientListInstances` `Response`

    - **Instances** *(list) --*

      Summary information about the instances that are associated with the specified service.

      - *(dict) --*

        A complex type that contains information about the instances that you registered by using a
        specified service.

        - **Id** *(string) --*

          The ID for an instance that you created by using a specified service.

        - **Attributes** *(dict) --*

          A string map that contains the following information:

          * The attributes that are associate with the instance.

          * For each attribute, the applicable value.

          Supported attribute keys include the following:

          * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load
          Balancing load balancer, the DNS name that is associated with the load balancer.

          * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in
          response to DNS queries, for example, ``example.com`` .

          * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in
          response to DNS queries, for example, ``192.0.2.44`` .

          * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in
          response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

          * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the
          port. In addition, if the service includes ``HealthCheckConfig`` , the port on the
          endpoint that Route 53 sends requests to.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      If more than ``MaxResults`` instances match the specified criteria, you can submit another
      ``ListInstances`` request to get the next group of results. Specify the value of
      ``NextToken`` from the previous response in the next request.
    """


_RequiredClientListNamespacesFiltersTypeDef = TypedDict(
    "_RequiredClientListNamespacesFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalClientListNamespacesFiltersTypeDef = TypedDict(
    "_OptionalClientListNamespacesFiltersTypeDef", {"Condition": str}, total=False
)


class ClientListNamespacesFiltersTypeDef(
    _RequiredClientListNamespacesFiltersTypeDef,
    _OptionalClientListNamespacesFiltersTypeDef,
):
    """
    Type definition for `ClientListNamespaces` `Filters`

    A complex type that identifies the namespaces that you want to list. You can choose to list
    public or private namespaces.

    - **Name** *(string) --* **[REQUIRED]**

      Specify ``TYPE`` .

    - **Values** *(list) --* **[REQUIRED]**

      If you specify ``EQ`` for ``Condition`` , specify either ``DNS_PUBLIC`` or ``DNS_PRIVATE`` .

      If you specify ``IN`` for ``Condition`` , you can specify ``DNS_PUBLIC`` , ``DNS_PRIVATE`` ,
      or both.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether ``ListNamespaces`` returns a
      namespace. Valid values for ``condition`` include:

      * ``EQ`` : When you specify ``EQ`` for the condition, you can choose to list only public
      namespaces or private namespaces, but not both. ``EQ`` is the default condition and can be
      omitted.

      * ``IN`` : When you specify ``IN`` for the condition, you can choose to list public
      namespaces, private namespaces, or both.

      * ``BETWEEN`` : Not applicable
    """


_ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef
):
    """
    Type definition for `ClientListNamespacesResponseNamespacesProperties` `DnsProperties`

    A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
    creates when you create a namespace.

    - **HostedZoneId** *(string) --*

      The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
      namespace.
    """


_ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef
):
    """
    Type definition for `ClientListNamespacesResponseNamespacesProperties` `HttpProperties`

    A complex type that contains the name of an HTTP namespace.

    - **HttpName** *(string) --*

      The name of an HTTP namespace.
    """


_ClientListNamespacesResponseNamespacesPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesTypeDef
):
    """
    Type definition for `ClientListNamespacesResponseNamespaces` `Properties`

    A complex type that contains information that is specific to the namespace type.

    - **DnsProperties** *(dict) --*

      A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
      creates when you create a namespace.

      - **HostedZoneId** *(string) --*

        The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
        namespace.

    - **HttpProperties** *(dict) --*

      A complex type that contains the name of an HTTP namespace.

      - **HttpName** *(string) --*

        The name of an HTTP namespace.
    """


_ClientListNamespacesResponseNamespacesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": str,
        "Description": str,
        "ServiceCount": int,
        "Properties": ClientListNamespacesResponseNamespacesPropertiesTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListNamespacesResponseNamespacesTypeDef(
    _ClientListNamespacesResponseNamespacesTypeDef
):
    """
    Type definition for `ClientListNamespacesResponse` `Namespaces`

    A complex type that contains information about a namespace.

    - **Id** *(string) --*

      The ID of the namespace.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you
      create it.

    - **Name** *(string) --*

      The name of the namespace. When you create a namespace, AWS Cloud Map automatically
      creates a Route 53 hosted zone that has the same name as the namespace.

    - **Type** *(string) --*

      The type of the namespace, either public or private.

    - **Description** *(string) --*

      A description for the namespace.

    - **ServiceCount** *(integer) --*

      The number of services that were created using the namespace.

    - **Properties** *(dict) --*

      A complex type that contains information that is specific to the namespace type.

      - **DnsProperties** *(dict) --*

        A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
        creates when you create a namespace.

        - **HostedZoneId** *(string) --*

          The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
          namespace.

      - **HttpProperties** *(dict) --*

        A complex type that contains the name of an HTTP namespace.

        - **HttpName** *(string) --*

          The name of an HTTP namespace.

    - **CreateDate** *(datetime) --*

      The date and time that the namespace was created.
    """


_ClientListNamespacesResponseTypeDef = TypedDict(
    "_ClientListNamespacesResponseTypeDef",
    {
        "Namespaces": List[ClientListNamespacesResponseNamespacesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListNamespacesResponseTypeDef(_ClientListNamespacesResponseTypeDef):
    """
    Type definition for `ClientListNamespaces` `Response`

    - **Namespaces** *(list) --*

      An array that contains one ``NamespaceSummary`` object for each namespace that matches the
      specified filter criteria.

      - *(dict) --*

        A complex type that contains information about a namespace.

        - **Id** *(string) --*

          The ID of the namespace.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you
          create it.

        - **Name** *(string) --*

          The name of the namespace. When you create a namespace, AWS Cloud Map automatically
          creates a Route 53 hosted zone that has the same name as the namespace.

        - **Type** *(string) --*

          The type of the namespace, either public or private.

        - **Description** *(string) --*

          A description for the namespace.

        - **ServiceCount** *(integer) --*

          The number of services that were created using the namespace.

        - **Properties** *(dict) --*

          A complex type that contains information that is specific to the namespace type.

          - **DnsProperties** *(dict) --*

            A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
            creates when you create a namespace.

            - **HostedZoneId** *(string) --*

              The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
              namespace.

          - **HttpProperties** *(dict) --*

            A complex type that contains the name of an HTTP namespace.

            - **HttpName** *(string) --*

              The name of an HTTP namespace.

        - **CreateDate** *(datetime) --*

          The date and time that the namespace was created.

    - **NextToken** *(string) --*

      If the response contains ``NextToken`` , submit another ``ListNamespaces`` request to get the
      next group of results. Specify the value of ``NextToken`` from the previous response in the
      next request.

      .. note::

        AWS Cloud Map gets ``MaxResults`` namespaces and then filters them based on the specified
        criteria. It's possible that no namespaces in the first ``MaxResults`` namespaces matched
        the specified criteria but that subsequent groups of ``MaxResults`` namespaces do contain
        namespaces that match the criteria.
    """


_RequiredClientListOperationsFiltersTypeDef = TypedDict(
    "_RequiredClientListOperationsFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalClientListOperationsFiltersTypeDef = TypedDict(
    "_OptionalClientListOperationsFiltersTypeDef", {"Condition": str}, total=False
)


class ClientListOperationsFiltersTypeDef(
    _RequiredClientListOperationsFiltersTypeDef,
    _OptionalClientListOperationsFiltersTypeDef,
):
    """
    Type definition for `ClientListOperations` `Filters`

    A complex type that lets you select the operations that you want to list.

    - **Name** *(string) --* **[REQUIRED]**

      Specify the operations that you want to get:

      * **NAMESPACE_ID** : Gets operations related to specified namespaces.

      * **SERVICE_ID** : Gets operations related to specified services.

      * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` ,
      ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .

      * **TYPE** : Gets specified types of operation.

      * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.

    - **Values** *(list) --* **[REQUIRED]**

      Specify values that are applicable to the value that you specify for ``Name`` :

      * **NAMESPACE_ID** : Specify one namespace ID.

      * **SERVICE_ID** : Specify one service ID.

      * **STATUS** : Specify one or more statuses: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or
      ``FAIL`` .

      * **TYPE** : Specify one or more of the following types: ``CREATE_NAMESPACE`` ,
      ``DELETE_NAMESPACE`` , ``UPDATE_SERVICE`` , ``REGISTER_INSTANCE`` , or
      ``DEREGISTER_INSTANCE`` .

      * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and
      Coordinated Universal Time (UTC). The start date must be the first value.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether an operation matches the specified
      value. Valid values for condition include:

      * ``EQ`` : When you specify ``EQ`` for the condition, you can specify only one value. ``EQ``
      is supported for ``NAMESPACE_ID`` , ``SERVICE_ID`` , ``STATUS`` , and ``TYPE`` . ``EQ`` is
      the default condition and can be omitted.

      * ``IN`` : When you specify ``IN`` for the condition, you can specify a list of one or more
      values. ``IN`` is supported for ``STATUS`` and ``TYPE`` . An operation must match one of the
      specified values to be returned in the response.

      * ``BETWEEN`` : Specify a start date and an end date in Unix date/time format and Coordinated
      Universal Time (UTC). The start date must be the first value. ``BETWEEN`` is supported for
      ``UPDATE_DATE`` .
    """


_ClientListOperationsResponseOperationsTypeDef = TypedDict(
    "_ClientListOperationsResponseOperationsTypeDef",
    {"Id": str, "Status": str},
    total=False,
)


class ClientListOperationsResponseOperationsTypeDef(
    _ClientListOperationsResponseOperationsTypeDef
):
    """
    Type definition for `ClientListOperationsResponse` `Operations`

    A complex type that contains information about an operation that matches the criteria that
    you specified in a  ListOperations request.

    - **Id** *(string) --*

      The ID for an operation.

    - **Status** *(string) --*

      The status of the operation. Values include the following:

      * **SUBMITTED** : This is the initial state immediately after you submit a request.

      * **PENDING** : AWS Cloud Map is performing the operation.

      * **SUCCESS** : The operation succeeded.

      * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .
    """


_ClientListOperationsResponseTypeDef = TypedDict(
    "_ClientListOperationsResponseTypeDef",
    {
        "Operations": List[ClientListOperationsResponseOperationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListOperationsResponseTypeDef(_ClientListOperationsResponseTypeDef):
    """
    Type definition for `ClientListOperations` `Response`

    - **Operations** *(list) --*

      Summary information about the operations that match the specified criteria.

      - *(dict) --*

        A complex type that contains information about an operation that matches the criteria that
        you specified in a  ListOperations request.

        - **Id** *(string) --*

          The ID for an operation.

        - **Status** *(string) --*

          The status of the operation. Values include the following:

          * **SUBMITTED** : This is the initial state immediately after you submit a request.

          * **PENDING** : AWS Cloud Map is performing the operation.

          * **SUCCESS** : The operation succeeded.

          * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .

    - **NextToken** *(string) --*

      If the response contains ``NextToken`` , submit another ``ListOperations`` request to get the
      next group of results. Specify the value of ``NextToken`` from the previous response in the
      next request.

      .. note::

        AWS Cloud Map gets ``MaxResults`` operations and then filters them based on the specified
        criteria. It's possible that no operations in the first ``MaxResults`` operations matched
        the specified criteria but that subsequent groups of ``MaxResults`` operations do contain
        operations that match the criteria.
    """


_RequiredClientListServicesFiltersTypeDef = TypedDict(
    "_RequiredClientListServicesFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalClientListServicesFiltersTypeDef = TypedDict(
    "_OptionalClientListServicesFiltersTypeDef", {"Condition": str}, total=False
)


class ClientListServicesFiltersTypeDef(
    _RequiredClientListServicesFiltersTypeDef, _OptionalClientListServicesFiltersTypeDef
):
    """
    Type definition for `ClientListServices` `Filters`

    A complex type that lets you specify the namespaces that you want to list services for.

    - **Name** *(string) --* **[REQUIRED]**

      Specify ``NAMESPACE_ID`` .

    - **Values** *(list) --* **[REQUIRED]**

      The values that are applicable to the value that you specify for ``Condition`` to filter the
      list of services.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether a service is returned by
      ``ListServices`` . Valid values for ``Condition`` include the following:

      * ``EQ`` : When you specify ``EQ`` , specify one namespace ID for ``Values`` . ``EQ`` is the
      default condition and can be omitted.

      * ``IN`` : When you specify ``IN`` , specify a list of the IDs for the namespaces that you
      want ``ListServices`` to return a list of services for.

      * ``BETWEEN`` : Not applicable.
    """


_ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": str, "TTL": int},
    total=False,
)


class ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef(
    _ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ClientListServicesResponseServicesDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want
    AWS Cloud Map to create when you register an instance.

    - **Type** *(string) --*

      The type of the resource, which indicates the type of value that Route 53 returns
      in response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
      one AAAA, and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
      other records. This is a limitation of DNS: you can't create a CNAME record and any
      other type of record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
      when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
      register an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register
      an instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for
      ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
      error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
      changed.

      * The value of ``port`` comes from the value that you specify for the
      ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service
      is ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
      have the same name as the value of ``service-hostname`` in the SRV record. You can
      ignore these records.

    - **TTL** *(integer) --*

      The amount of time, in seconds, that you want DNS resolvers to cache the settings
      for this record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS
        resource that an alias record routes traffic to. If you include the
        ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
        ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
        service to register instances that create either alias or non-alias records.
    """


_ClientListServicesResponseServicesDnsConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": str,
        "DnsRecords": List[
            ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef
        ],
    },
    total=False,
)


class ClientListServicesResponseServicesDnsConfigTypeDef(
    _ClientListServicesResponseServicesDnsConfigTypeDef
):
    """
    Type definition for `ClientListServicesResponseServices` `DnsConfig`

    A complex type that contains information about the Amazon Route 53 DNS records that you
    want AWS Cloud Map to create when you register an instance.

    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.

    - **RoutingPolicy** *(string) --*

      The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
      Map creates when you register an instance and specify this service.

      .. note::

        If you want to use this service to register instances that create alias records,
        specify ``WEIGHTED`` for the routing policy.

      You can specify the following values:

       **MULTIVALUE**

      If you define a health check for the service and the health check is healthy, Route 53
      returns the applicable value for up to eight instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS
      queries with IP addresses for up to eight healthy instances. If fewer than eight
      instances are healthy, Route 53 responds to every DNS query with the IP addresses for
      all of the healthy instances.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the values for up to eight instances.

      For more information about the multivalue routing policy, see `Multivalue Answer
      Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
      in the *Route 53 Developer Guide* .

       **WEIGHTED**

      Route 53 returns the applicable value from one randomly selected instance from among
      the instances that you registered using the same service. Currently, all records have
      the same weight, so you can't route more or less traffic to any instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS
      queries with the IP address for one randomly selected instance from among the healthy
      instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
      the instances were healthy.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the applicable value for one randomly selected instance.

      For more information about the weighted routing policy, see `Weighted Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
      in the *Route 53 Developer Guide* .

    - **DnsRecords** *(list) --*

      An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
      want AWS Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want
        AWS Cloud Map to create when you register an instance.

        - **Type** *(string) --*

          The type of the resource, which indicates the type of value that Route 53 returns
          in response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
          one AAAA, and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
          other records. This is a limitation of DNS: you can't create a CNAME record and any
          other type of record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
          when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
          register an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register
          an instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for
          ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
          error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
          changed.

          * The value of ``port`` comes from the value that you specify for the
          ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service
          is ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
          have the same name as the value of ``service-hostname`` in the SRV record. You can
          ignore these records.

        - **TTL** *(integer) --*

          The amount of time, in seconds, that you want DNS resolvers to cache the settings
          for this record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS
            resource that an alias record routes traffic to. If you include the
            ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
            ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
            service to register instances that create either alias or non-alias records.
    """


_ClientListServicesResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesHealthCheckConfigTypeDef",
    {"Type": str, "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientListServicesResponseServicesHealthCheckConfigTypeDef(
    _ClientListServicesResponseServicesHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientListServicesResponseServices` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional
     health check. If you specify settings for a health check, AWS Cloud Map associates the
     health check with the records that you specify in ``DnsConfig`` .

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
    information about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    Note the following about configuring health checks.

     **A and AAAA records**

    If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
    creates a health check that uses the IPv4 address to check the health of the resource. If
    the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
    the A and AAAA records to be unhealthy.

     **CNAME records**

    You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
    ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
    with an ``InvalidInput`` error.

     **Request interval**

    A Route 53 health checker in each health-checking region sends a health check request to
    an endpoint every 30 seconds. On average, your endpoint receives a health check request
    about every two seconds. However, health checkers don't coordinate with one another, so
    you'll sometimes see several requests per second followed by a few seconds with no health
    checks at all.

     **Health checking regions**

    Health checkers perform checks from all Route 53 health-checking regions. For a list of
    the current regions, see `Regions
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
    .

     **Alias records**

    When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
    Cloud Map creates a Route 53 alias record. Note the following:

    * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
    ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
    AWS resource. such as an ELB load balancer. For more information, see
    `EvaluateTargetHealth
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
    .

    * If you include ``HealthCheckConfig`` and then use the service to register an instance
    that creates an alias record, Route 53 doesn't create the health check.

     **Charges for health checks**

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
    information about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Route 53
      determines whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTP request and waits for an HTTP status code of 200 or greater and less
      than 400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
      than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
         or later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
      ``Type`` , don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can
      be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
      the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
      53 automatically adds the DNS name for the service. If you don't specify a value for
      ``ResourcePath`` , the default value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
      ``ResourcePath`` .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53
      to change the current status of the endpoint from unhealthy to healthy or vice versa.
      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef(
    _ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef
):
    """
    Type definition for `ClientListServicesResponseServices` `HealthCheckCustomConfig`

    A complex type that contains information about an optional custom health check. A custom
    health check, which requires that you use a third-party health checker to evaluate the
    health of your resources, is useful in the following circumstances:

    * You can't use a health check that is defined by ``HealthCheckConfig`` because the
    resource isn't available over the internet. For example, you can use a custom health
    check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
    the health checker must also be in the VPC.)

    * You want to use a third-party health checker regardless of where your resources are.

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    To change the status of a custom health check, submit an
    ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
    resource, it just keeps a record of the status specified in the most recent
    ``UpdateInstanceCustomHealthStatus`` request.

    Here's how custom health checks work:

    * You create a service and specify a value for ``FailureThreshold`` .  The failure
    threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
    between the time that your application sends an  UpdateInstanceCustomHealthStatus request
    and the time that AWS Cloud Map stops routing internet traffic to the corresponding
    resource.

    * You register an instance.

    * You configure a third-party health checker to monitor the resource that is associated
    with the new instance.

    .. note::

       AWS Cloud Map doesn't check the health of the resource directly.

    * The third-party health-checker determines that the resource is unhealthy and notifies
    your application.

    * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

    * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

    * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
    to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

    Note the following about configuring custom health checks.

    - **FailureThreshold** *(integer) --*

      The number of 30-second intervals that you want Cloud Map to wait after receiving an
      ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
      service instance. For example, suppose you specify a value of ``2`` for
      ``FailureTheshold`` , and then your application sends an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
      seconds (2 x 30) before changing the status of the service instance based on that
      request.

      Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
      same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
      change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
      to make the change.
    """


_ClientListServicesResponseServicesTypeDef = TypedDict(
    "_ClientListServicesResponseServicesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientListServicesResponseServicesDnsConfigTypeDef,
        "HealthCheckConfig": ClientListServicesResponseServicesHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListServicesResponseServicesTypeDef(
    _ClientListServicesResponseServicesTypeDef
):
    """
    Type definition for `ClientListServicesResponse` `Services`

    A complex type that contains information about a specified service.

    - **Id** *(string) --*

      The ID that AWS Cloud Map assigned to the service when you created it.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create
      it.

    - **Name** *(string) --*

      The name of the service.

    - **Description** *(string) --*

      The description that you specify when you create the service.

    - **InstanceCount** *(integer) --*

      The number of instances that are currently associated with the service. Instances that
      were previously associated with the service but that have been deleted are not included
      in the count.

    - **DnsConfig** *(dict) --*

      A complex type that contains information about the Amazon Route 53 DNS records that you
      want AWS Cloud Map to create when you register an instance.

      - **NamespaceId** *(string) --*

        The ID of the namespace to use for DNS configuration.

      - **RoutingPolicy** *(string) --*

        The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
        Map creates when you register an instance and specify this service.

        .. note::

          If you want to use this service to register instances that create alias records,
          specify ``WEIGHTED`` for the routing policy.

        You can specify the following values:

         **MULTIVALUE**

        If you define a health check for the service and the health check is healthy, Route 53
        returns the applicable value for up to eight instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS
        queries with IP addresses for up to eight healthy instances. If fewer than eight
        instances are healthy, Route 53 responds to every DNS query with the IP addresses for
        all of the healthy instances.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the values for up to eight instances.

        For more information about the multivalue routing policy, see `Multivalue Answer
        Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
        in the *Route 53 Developer Guide* .

         **WEIGHTED**

        Route 53 returns the applicable value from one randomly selected instance from among
        the instances that you registered using the same service. Currently, all records have
        the same weight, so you can't route more or less traffic to any instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS
        queries with the IP address for one randomly selected instance from among the healthy
        instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
        the instances were healthy.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the applicable value for one randomly selected instance.

        For more information about the weighted routing policy, see `Weighted Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
        in the *Route 53 Developer Guide* .

      - **DnsRecords** *(list) --*

        An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
        want AWS Cloud Map to create when you register an instance.

        - *(dict) --*

          A complex type that contains information about the Route 53 DNS records that you want
          AWS Cloud Map to create when you register an instance.

          - **Type** *(string) --*

            The type of the resource, which indicates the type of value that Route 53 returns
            in response to DNS queries.

            Note the following:

            * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
            one AAAA, and one SRV record. You can specify them in any combination.

            * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
            other records. This is a limitation of DNS: you can't create a CNAME record and any
            other type of record that has the same name as a CNAME record.

            * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
            when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

            * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
            register an instance.

            The following values are supported:

             **A**

            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

             **AAAA**

            Route 53 returns the IP address of the resource in IPv6 format, such as
            2001:0db8:85a3:0000:0000:abcd:0001:2345.

             **CNAME**

            Route 53 returns the domain name of the resource, such as www.example.com. Note the
            following:

            * You specify the domain name that you want to route traffic to when you register
            an instance. For more information, see  RegisterInstanceRequest$Attributes .

            * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

            * You can't specify both ``CNAME`` for ``Type`` and settings for
            ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
            error.

             **SRV**

            Route 53 returns the value for an SRV record. The value for an SRV record uses the
            following values:

             ``priority weight port service-hostname``

            Note the following about the values:

            * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
            changed.

            * The value of ``port`` comes from the value that you specify for the
            ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

            * The value of ``service-hostname`` is a concatenation of the following values:

              * The value that you specify for ``InstanceId`` when you register an instance.

              * The name of the service.

              * The name of the namespace.

            For example, if the value of ``InstanceId`` is ``test`` , the name of the service
            is ``backend`` , and the name of the namespace is ``example.com`` , the value of
            ``service-hostname`` is:

             ``test.backend.example.com``

            If you specify settings for an SRV record and if you specify values for
            ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
            request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
            have the same name as the value of ``service-hostname`` in the SRV record. You can
            ignore these records.

          - **TTL** *(integer) --*

            The amount of time, in seconds, that you want DNS resolvers to cache the settings
            for this record.

            .. note::

              Alias records don't include a TTL because Route 53 uses the TTL for the AWS
              resource that an alias record routes traffic to. If you include the
              ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
              ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
              service to register instances that create either alias or non-alias records.

    - **HealthCheckConfig** *(dict) --*

       *Public DNS namespaces only.* A complex type that contains settings for an optional
       health check. If you specify settings for a health check, AWS Cloud Map associates the
       health check with the records that you specify in ``DnsConfig`` .

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
      information about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      Note the following about configuring health checks.

       **A and AAAA records**

      If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
      creates a health check that uses the IPv4 address to check the health of the resource. If
      the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
      the A and AAAA records to be unhealthy.

       **CNAME records**

      You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
      ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
      with an ``InvalidInput`` error.

       **Request interval**

      A Route 53 health checker in each health-checking region sends a health check request to
      an endpoint every 30 seconds. On average, your endpoint receives a health check request
      about every two seconds. However, health checkers don't coordinate with one another, so
      you'll sometimes see several requests per second followed by a few seconds with no health
      checks at all.

       **Health checking regions**

      Health checkers perform checks from all Route 53 health-checking regions. For a list of
      the current regions, see `Regions
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
      .

       **Alias records**

      When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
      Cloud Map creates a Route 53 alias record. Note the following:

      * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
      ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
      AWS resource. such as an ELB load balancer. For more information, see
      `EvaluateTargetHealth
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
      .

      * If you include ``HealthCheckConfig`` and then use the service to register an instance
      that creates an alias record, Route 53 doesn't create the health check.

       **Charges for health checks**

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
      information about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Route 53
        determines whether an endpoint is healthy.

        .. warning::

          You can't change the value of ``Type`` after you create a health check.

        You can create the following types of health checks:

        * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTP request and waits for an HTTP status code of 200 or greater and less
        than 400.

        * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
        than 400.

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
           or later.

        * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
        ``Type`` , don't specify a value for ``ResourcePath`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path that you want Route 53 to request when performing health checks. The path can
        be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
        the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
        53 automatically adds the DNS name for the service. If you don't specify a value for
        ``ResourcePath`` , the default value is ``/`` .

        If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
        ``ResourcePath`` .

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Route 53
        to change the current status of the endpoint from unhealthy to healthy or vice versa.
        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

    - **HealthCheckCustomConfig** *(dict) --*

      A complex type that contains information about an optional custom health check. A custom
      health check, which requires that you use a third-party health checker to evaluate the
      health of your resources, is useful in the following circumstances:

      * You can't use a health check that is defined by ``HealthCheckConfig`` because the
      resource isn't available over the internet. For example, you can use a custom health
      check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
      the health checker must also be in the VPC.)

      * You want to use a third-party health checker regardless of where your resources are.

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      To change the status of a custom health check, submit an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
      resource, it just keeps a record of the status specified in the most recent
      ``UpdateInstanceCustomHealthStatus`` request.

      Here's how custom health checks work:

      * You create a service and specify a value for ``FailureThreshold`` .  The failure
      threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
      between the time that your application sends an  UpdateInstanceCustomHealthStatus request
      and the time that AWS Cloud Map stops routing internet traffic to the corresponding
      resource.

      * You register an instance.

      * You configure a third-party health checker to monitor the resource that is associated
      with the new instance.

      .. note::

         AWS Cloud Map doesn't check the health of the resource directly.

      * The third-party health-checker determines that the resource is unhealthy and notifies
      your application.

      * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

      * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

      * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
      to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

      Note the following about configuring custom health checks.

      - **FailureThreshold** *(integer) --*

        The number of 30-second intervals that you want Cloud Map to wait after receiving an
        ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
        service instance. For example, suppose you specify a value of ``2`` for
        ``FailureTheshold`` , and then your application sends an
        ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
        seconds (2 x 30) before changing the status of the service instance based on that
        request.

        Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
        same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
        change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
        to make the change.

    - **CreateDate** *(datetime) --*

      The date and time that the service was created.
    """


_ClientListServicesResponseTypeDef = TypedDict(
    "_ClientListServicesResponseTypeDef",
    {"Services": List[ClientListServicesResponseServicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListServicesResponseTypeDef(_ClientListServicesResponseTypeDef):
    """
    Type definition for `ClientListServices` `Response`

    - **Services** *(list) --*

      An array that contains one ``ServiceSummary`` object for each service that matches the
      specified filter criteria.

      - *(dict) --*

        A complex type that contains information about a specified service.

        - **Id** *(string) --*

          The ID that AWS Cloud Map assigned to the service when you created it.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create
          it.

        - **Name** *(string) --*

          The name of the service.

        - **Description** *(string) --*

          The description that you specify when you create the service.

        - **InstanceCount** *(integer) --*

          The number of instances that are currently associated with the service. Instances that
          were previously associated with the service but that have been deleted are not included
          in the count.

        - **DnsConfig** *(dict) --*

          A complex type that contains information about the Amazon Route 53 DNS records that you
          want AWS Cloud Map to create when you register an instance.

          - **NamespaceId** *(string) --*

            The ID of the namespace to use for DNS configuration.

          - **RoutingPolicy** *(string) --*

            The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
            Map creates when you register an instance and specify this service.

            .. note::

              If you want to use this service to register instances that create alias records,
              specify ``WEIGHTED`` for the routing policy.

            You can specify the following values:

             **MULTIVALUE**

            If you define a health check for the service and the health check is healthy, Route 53
            returns the applicable value for up to eight instances.

            For example, suppose the service includes configurations for one A record and a health
            check, and you use the service to register 10 instances. Route 53 responds to DNS
            queries with IP addresses for up to eight healthy instances. If fewer than eight
            instances are healthy, Route 53 responds to every DNS query with the IP addresses for
            all of the healthy instances.

            If you don't define a health check for the service, Route 53 assumes that all instances
            are healthy and returns the values for up to eight instances.

            For more information about the multivalue routing policy, see `Multivalue Answer
            Routing
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
            in the *Route 53 Developer Guide* .

             **WEIGHTED**

            Route 53 returns the applicable value from one randomly selected instance from among
            the instances that you registered using the same service. Currently, all records have
            the same weight, so you can't route more or less traffic to any instances.

            For example, suppose the service includes configurations for one A record and a health
            check, and you use the service to register 10 instances. Route 53 responds to DNS
            queries with the IP address for one randomly selected instance from among the healthy
            instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
            the instances were healthy.

            If you don't define a health check for the service, Route 53 assumes that all instances
            are healthy and returns the applicable value for one randomly selected instance.

            For more information about the weighted routing policy, see `Weighted Routing
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
            in the *Route 53 Developer Guide* .

          - **DnsRecords** *(list) --*

            An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
            want AWS Cloud Map to create when you register an instance.

            - *(dict) --*

              A complex type that contains information about the Route 53 DNS records that you want
              AWS Cloud Map to create when you register an instance.

              - **Type** *(string) --*

                The type of the resource, which indicates the type of value that Route 53 returns
                in response to DNS queries.

                Note the following:

                * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
                one AAAA, and one SRV record. You can specify them in any combination.

                * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
                other records. This is a limitation of DNS: you can't create a CNAME record and any
                other type of record that has the same name as a CNAME record.

                * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
                when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

                * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
                register an instance.

                The following values are supported:

                 **A**

                Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

                 **AAAA**

                Route 53 returns the IP address of the resource in IPv6 format, such as
                2001:0db8:85a3:0000:0000:abcd:0001:2345.

                 **CNAME**

                Route 53 returns the domain name of the resource, such as www.example.com. Note the
                following:

                * You specify the domain name that you want to route traffic to when you register
                an instance. For more information, see  RegisterInstanceRequest$Attributes .

                * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

                * You can't specify both ``CNAME`` for ``Type`` and settings for
                ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
                error.

                 **SRV**

                Route 53 returns the value for an SRV record. The value for an SRV record uses the
                following values:

                 ``priority weight port service-hostname``

                Note the following about the values:

                * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
                changed.

                * The value of ``port`` comes from the value that you specify for the
                ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

                * The value of ``service-hostname`` is a concatenation of the following values:

                  * The value that you specify for ``InstanceId`` when you register an instance.

                  * The name of the service.

                  * The name of the namespace.

                For example, if the value of ``InstanceId`` is ``test`` , the name of the service
                is ``backend`` , and the name of the namespace is ``example.com`` , the value of
                ``service-hostname`` is:

                 ``test.backend.example.com``

                If you specify settings for an SRV record and if you specify values for
                ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
                request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
                have the same name as the value of ``service-hostname`` in the SRV record. You can
                ignore these records.

              - **TTL** *(integer) --*

                The amount of time, in seconds, that you want DNS resolvers to cache the settings
                for this record.

                .. note::

                  Alias records don't include a TTL because Route 53 uses the TTL for the AWS
                  resource that an alias record routes traffic to. If you include the
                  ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
                  ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
                  service to register instances that create either alias or non-alias records.

        - **HealthCheckConfig** *(dict) --*

           *Public DNS namespaces only.* A complex type that contains settings for an optional
           health check. If you specify settings for a health check, AWS Cloud Map associates the
           health check with the records that you specify in ``DnsConfig`` .

          .. warning::

            If you specify a health check configuration, you can specify either
            ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

          Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
          information about pricing for health checks, see `Amazon Route 53 Pricing
          <http://aws.amazon.com/route53/pricing/>`__ .

          Note the following about configuring health checks.

           **A and AAAA records**

          If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
          creates a health check that uses the IPv4 address to check the health of the resource. If
          the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
          the A and AAAA records to be unhealthy.

           **CNAME records**

          You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
          ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
          with an ``InvalidInput`` error.

           **Request interval**

          A Route 53 health checker in each health-checking region sends a health check request to
          an endpoint every 30 seconds. On average, your endpoint receives a health check request
          about every two seconds. However, health checkers don't coordinate with one another, so
          you'll sometimes see several requests per second followed by a few seconds with no health
          checks at all.

           **Health checking regions**

          Health checkers perform checks from all Route 53 health-checking regions. For a list of
          the current regions, see `Regions
          <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
          .

           **Alias records**

          When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
          Cloud Map creates a Route 53 alias record. Note the following:

          * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
          ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
          AWS resource. such as an ELB load balancer. For more information, see
          `EvaluateTargetHealth
          <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
          .

          * If you include ``HealthCheckConfig`` and then use the service to register an instance
          that creates an alias record, Route 53 doesn't create the health check.

           **Charges for health checks**

          Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
          information about pricing for health checks, see `Amazon Route 53 Pricing
          <http://aws.amazon.com/route53/pricing/>`__ .

          - **Type** *(string) --*

            The type of health check that you want to create, which indicates how Route 53
            determines whether an endpoint is healthy.

            .. warning::

              You can't change the value of ``Type`` after you create a health check.

            You can create the following types of health checks:

            * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
            submits an HTTP request and waits for an HTTP status code of 200 or greater and less
            than 400.

            * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
            submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
            than 400.

            .. warning::

               If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
               or later.

            * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
            ``Type`` , don't specify a value for ``ResourcePath`` .

            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Route 53 Developer Guide* .

          - **ResourcePath** *(string) --*

            The path that you want Route 53 to request when performing health checks. The path can
            be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
            the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
            53 automatically adds the DNS name for the service. If you don't specify a value for
            ``ResourcePath`` , the default value is ``/`` .

            If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
            ``ResourcePath`` .

          - **FailureThreshold** *(integer) --*

            The number of consecutive health checks that an endpoint must pass or fail for Route 53
            to change the current status of the endpoint from unhealthy to healthy or vice versa.
            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Route 53 Developer Guide* .

        - **HealthCheckCustomConfig** *(dict) --*

          A complex type that contains information about an optional custom health check. A custom
          health check, which requires that you use a third-party health checker to evaluate the
          health of your resources, is useful in the following circumstances:

          * You can't use a health check that is defined by ``HealthCheckConfig`` because the
          resource isn't available over the internet. For example, you can use a custom health
          check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
          the health checker must also be in the VPC.)

          * You want to use a third-party health checker regardless of where your resources are.

          .. warning::

            If you specify a health check configuration, you can specify either
            ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

          To change the status of a custom health check, submit an
          ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
          resource, it just keeps a record of the status specified in the most recent
          ``UpdateInstanceCustomHealthStatus`` request.

          Here's how custom health checks work:

          * You create a service and specify a value for ``FailureThreshold`` .  The failure
          threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
          between the time that your application sends an  UpdateInstanceCustomHealthStatus request
          and the time that AWS Cloud Map stops routing internet traffic to the corresponding
          resource.

          * You register an instance.

          * You configure a third-party health checker to monitor the resource that is associated
          with the new instance.

          .. note::

             AWS Cloud Map doesn't check the health of the resource directly.

          * The third-party health-checker determines that the resource is unhealthy and notifies
          your application.

          * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

          * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

          * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
          to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

          Note the following about configuring custom health checks.

          - **FailureThreshold** *(integer) --*

            The number of 30-second intervals that you want Cloud Map to wait after receiving an
            ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
            service instance. For example, suppose you specify a value of ``2`` for
            ``FailureTheshold`` , and then your application sends an
            ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
            seconds (2 x 30) before changing the status of the service instance based on that
            request.

            Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
            same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
            change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
            to make the change.

        - **CreateDate** *(datetime) --*

          The date and time that the service was created.

    - **NextToken** *(string) --*

      If the response contains ``NextToken`` , submit another ``ListServices`` request to get the
      next group of results. Specify the value of ``NextToken`` from the previous response in the
      next request.

      .. note::

        AWS Cloud Map gets ``MaxResults`` services and then filters them based on the specified
        criteria. It's possible that no services in the first ``MaxResults`` services matched the
        specified criteria but that subsequent groups of ``MaxResults`` services do contain
        services that match the criteria.
    """


_ClientRegisterInstanceResponseTypeDef = TypedDict(
    "_ClientRegisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRegisterInstanceResponseTypeDef(_ClientRegisterInstanceResponseTypeDef):
    """
    Type definition for `ClientRegisterInstance` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientUpdateServiceResponseTypeDef = TypedDict(
    "_ClientUpdateServiceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateServiceResponseTypeDef(_ClientUpdateServiceResponseTypeDef):
    """
    Type definition for `ClientUpdateService` `Response`

    - **OperationId** *(string) --*

      A value that you can use to determine whether the request completed successfully. To get the
      status of the operation, see  GetOperation .
    """


_ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef", {"Type": str, "TTL": int}
)


class ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef(
    _ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ClientUpdateServiceServiceDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want AWS
    Cloud Map to create when you register an instance.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the resource, which indicates the type of value that Route 53 returns in
      response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
      AAAA, and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other
      records. This is a limitation of DNS: you can't create a CNAME record and any other type
      of record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you
      register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register
      an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register an
      instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` .
      If you do, the request will fail with an ``InvalidInput`` error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.

      * The value of ``port`` comes from the value that you specify for the
      ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
      ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the
      same name as the value of ``service-hostname`` in the SRV record. You can ignore these
      records.

    - **TTL** *(integer) --* **[REQUIRED]**

      The amount of time, in seconds, that you want DNS resolvers to cache the settings for
      this record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource
        that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME``
        attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored.
        Always specify a TTL for the service; you can use a service to register instances that
        create either alias or non-alias records.
    """


_ClientUpdateServiceServiceDnsConfigTypeDef = TypedDict(
    "_ClientUpdateServiceServiceDnsConfigTypeDef",
    {"DnsRecords": List[ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef]},
)


class ClientUpdateServiceServiceDnsConfigTypeDef(
    _ClientUpdateServiceServiceDnsConfigTypeDef
):
    """
    Type definition for `ClientUpdateServiceService` `DnsConfig`

    A complex type that contains information about the Route 53 DNS records that you want AWS Cloud
    Map to create when you register an instance.

    - **DnsRecords** *(list) --* **[REQUIRED]**

      An array that contains one ``DnsRecord`` object for each Route 53 record that you want AWS
      Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want AWS
        Cloud Map to create when you register an instance.

        - **Type** *(string) --* **[REQUIRED]**

          The type of the resource, which indicates the type of value that Route 53 returns in
          response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
          AAAA, and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other
          records. This is a limitation of DNS: you can't create a CNAME record and any other type
          of record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you
          register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register
          an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register an
          instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` .
          If you do, the request will fail with an ``InvalidInput`` error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.

          * The value of ``port`` comes from the value that you specify for the
          ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
          ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the
          same name as the value of ``service-hostname`` in the SRV record. You can ignore these
          records.

        - **TTL** *(integer) --* **[REQUIRED]**

          The amount of time, in seconds, that you want DNS resolvers to cache the settings for
          this record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource
            that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME``
            attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored.
            Always specify a TTL for the service; you can use a service to register instances that
            create either alias or non-alias records.
    """


_RequiredClientUpdateServiceServiceHealthCheckConfigTypeDef = TypedDict(
    "_RequiredClientUpdateServiceServiceHealthCheckConfigTypeDef", {"Type": str}
)
_OptionalClientUpdateServiceServiceHealthCheckConfigTypeDef = TypedDict(
    "_OptionalClientUpdateServiceServiceHealthCheckConfigTypeDef",
    {"ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientUpdateServiceServiceHealthCheckConfigTypeDef(
    _RequiredClientUpdateServiceServiceHealthCheckConfigTypeDef,
    _OptionalClientUpdateServiceServiceHealthCheckConfigTypeDef,
):
    """
    Type definition for `ClientUpdateServiceService` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional health
     check. If you specify settings for a health check, AWS Cloud Map associates the health check
     with the records that you specify in ``DnsConfig`` .

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information
    about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    Note the following about configuring health checks.

     **A and AAAA records**

    If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map creates a
    health check that uses the IPv4 address to check the health of the resource. If the endpoint
    that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA
    records to be unhealthy.

     **CNAME records**

    You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes ``CNAME``
    for the value of ``Type`` . If you do, the ``CreateService`` request will fail with an
    ``InvalidInput`` error.

     **Request interval**

    A Route 53 health checker in each health-checking region sends a health check request to an
    endpoint every 30 seconds. On average, your endpoint receives a health check request about
    every two seconds. However, health checkers don't coordinate with one another, so you'll
    sometimes see several requests per second followed by a few seconds with no health checks at
    all.

     **Health checking regions**

    Health checkers perform checks from all Route 53 health-checking regions. For a list of the
    current regions, see `Regions
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
    .

     **Alias records**

    When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS Cloud
    Map creates a Route 53 alias record. Note the following:

    * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
    ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced AWS
    resource. such as an ELB load balancer. For more information, see `EvaluateTargetHealth
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
    .

    * If you include ``HealthCheckConfig`` and then use the service to register an instance that
    creates an alias record, Route 53 doesn't create the health check.

     **Charges for health checks**

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information
    about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    - **Type** *(string) --* **[REQUIRED]**

      The type of health check that you want to create, which indicates how Route 53 determines
      whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
      HTTP request and waits for an HTTP status code of 200 or greater and less than 400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits
      an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
         later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for ``Type``
      , don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can be any
      value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint
      is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically
      adds the DNS name for the service. If you don't specify a value for ``ResourcePath`` , the
      default value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath`` .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53 to
      change the current status of the endpoint from unhealthy to healthy or vice versa. For more
      information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_RequiredClientUpdateServiceServiceTypeDef = TypedDict(
    "_RequiredClientUpdateServiceServiceTypeDef",
    {"DnsConfig": ClientUpdateServiceServiceDnsConfigTypeDef},
)
_OptionalClientUpdateServiceServiceTypeDef = TypedDict(
    "_OptionalClientUpdateServiceServiceTypeDef",
    {
        "Description": str,
        "HealthCheckConfig": ClientUpdateServiceServiceHealthCheckConfigTypeDef,
    },
    total=False,
)


class ClientUpdateServiceServiceTypeDef(
    _RequiredClientUpdateServiceServiceTypeDef,
    _OptionalClientUpdateServiceServiceTypeDef,
):
    """
    Type definition for `ClientUpdateService` `Service`

    A complex type that contains the new settings for the service.

    - **Description** *(string) --*

      A description for the service.

    - **DnsConfig** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the Route 53 DNS records that you want AWS Cloud
      Map to create when you register an instance.

      - **DnsRecords** *(list) --* **[REQUIRED]**

        An array that contains one ``DnsRecord`` object for each Route 53 record that you want AWS
        Cloud Map to create when you register an instance.

        - *(dict) --*

          A complex type that contains information about the Route 53 DNS records that you want AWS
          Cloud Map to create when you register an instance.

          - **Type** *(string) --* **[REQUIRED]**

            The type of the resource, which indicates the type of value that Route 53 returns in
            response to DNS queries.

            Note the following:

            * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one
            AAAA, and one SRV record. You can specify them in any combination.

            * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other
            records. This is a limitation of DNS: you can't create a CNAME record and any other type
            of record that has the same name as a CNAME record.

            * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you
            register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

            * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register
            an instance.

            The following values are supported:

             **A**

            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

             **AAAA**

            Route 53 returns the IP address of the resource in IPv6 format, such as
            2001:0db8:85a3:0000:0000:abcd:0001:2345.

             **CNAME**

            Route 53 returns the domain name of the resource, such as www.example.com. Note the
            following:

            * You specify the domain name that you want to route traffic to when you register an
            instance. For more information, see  RegisterInstanceRequest$Attributes .

            * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

            * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` .
            If you do, the request will fail with an ``InvalidInput`` error.

             **SRV**

            Route 53 returns the value for an SRV record. The value for an SRV record uses the
            following values:

             ``priority weight port service-hostname``

            Note the following about the values:

            * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.

            * The value of ``port`` comes from the value that you specify for the
            ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

            * The value of ``service-hostname`` is a concatenation of the following values:

              * The value that you specify for ``InstanceId`` when you register an instance.

              * The name of the service.

              * The name of the namespace.

            For example, if the value of ``InstanceId`` is ``test`` , the name of the service is
            ``backend`` , and the name of the namespace is ``example.com`` , the value of
            ``service-hostname`` is:

             ``test.backend.example.com``

            If you specify settings for an SRV record and if you specify values for
            ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
            request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the
            same name as the value of ``service-hostname`` in the SRV record. You can ignore these
            records.

          - **TTL** *(integer) --* **[REQUIRED]**

            The amount of time, in seconds, that you want DNS resolvers to cache the settings for
            this record.

            .. note::

              Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource
              that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME``
              attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored.
              Always specify a TTL for the service; you can use a service to register instances that
              create either alias or non-alias records.

    - **HealthCheckConfig** *(dict) --*

       *Public DNS namespaces only.* A complex type that contains settings for an optional health
       check. If you specify settings for a health check, AWS Cloud Map associates the health check
       with the records that you specify in ``DnsConfig`` .

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information
      about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      Note the following about configuring health checks.

       **A and AAAA records**

      If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map creates a
      health check that uses the IPv4 address to check the health of the resource. If the endpoint
      that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA
      records to be unhealthy.

       **CNAME records**

      You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes ``CNAME``
      for the value of ``Type`` . If you do, the ``CreateService`` request will fail with an
      ``InvalidInput`` error.

       **Request interval**

      A Route 53 health checker in each health-checking region sends a health check request to an
      endpoint every 30 seconds. On average, your endpoint receives a health check request about
      every two seconds. However, health checkers don't coordinate with one another, so you'll
      sometimes see several requests per second followed by a few seconds with no health checks at
      all.

       **Health checking regions**

      Health checkers perform checks from all Route 53 health-checking regions. For a list of the
      current regions, see `Regions
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
      .

       **Alias records**

      When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS Cloud
      Map creates a Route 53 alias record. Note the following:

      * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
      ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced AWS
      resource. such as an ELB load balancer. For more information, see `EvaluateTargetHealth
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
      .

      * If you include ``HealthCheckConfig`` and then use the service to register an instance that
      creates an alias record, Route 53 doesn't create the health check.

       **Charges for health checks**

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information
      about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      - **Type** *(string) --* **[REQUIRED]**

        The type of health check that you want to create, which indicates how Route 53 determines
        whether an endpoint is healthy.

        .. warning::

          You can't change the value of ``Type`` after you create a health check.

        You can create the following types of health checks:

        * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
        HTTP request and waits for an HTTP status code of 200 or greater and less than 400.

        * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits
        an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or
           later.

        * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for ``Type``
        , don't specify a value for ``ResourcePath`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path that you want Route 53 to request when performing health checks. The path can be any
        value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint
        is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically
        adds the DNS name for the service. If you don't specify a value for ``ResourcePath`` , the
        default value is ``/`` .

        If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath`` .

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Route 53 to
        change the current status of the endpoint from unhealthy to healthy or vice versa. For more
        information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .
    """


_ListInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstancesPaginatePaginationConfigTypeDef(
    _ListInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInstancesPaginate` `PaginationConfig`

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


_ListInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListInstancesPaginateResponseInstancesTypeDef(
    _ListInstancesPaginateResponseInstancesTypeDef
):
    """
    Type definition for `ListInstancesPaginateResponse` `Instances`

    A complex type that contains information about the instances that you registered by using a
    specified service.

    - **Id** *(string) --*

      The ID for an instance that you created by using a specified service.

    - **Attributes** *(dict) --*

      A string map that contains the following information:

      * The attributes that are associate with the instance.

      * For each attribute, the applicable value.

      Supported attribute keys include the following:

      * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load
      Balancing load balancer, the DNS name that is associated with the load balancer.

      * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in
      response to DNS queries, for example, ``example.com`` .

      * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in
      response to DNS queries, for example, ``192.0.2.44`` .

      * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in
      response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

      * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the
      port. In addition, if the service includes ``HealthCheckConfig`` , the port on the
      endpoint that Route 53 sends requests to.

      - *(string) --*

        - *(string) --*
    """


_ListInstancesPaginateResponseTypeDef = TypedDict(
    "_ListInstancesPaginateResponseTypeDef",
    {"Instances": List[ListInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)


class ListInstancesPaginateResponseTypeDef(_ListInstancesPaginateResponseTypeDef):
    """
    Type definition for `ListInstancesPaginate` `Response`

    - **Instances** *(list) --*

      Summary information about the instances that are associated with the specified service.

      - *(dict) --*

        A complex type that contains information about the instances that you registered by using a
        specified service.

        - **Id** *(string) --*

          The ID for an instance that you created by using a specified service.

        - **Attributes** *(dict) --*

          A string map that contains the following information:

          * The attributes that are associate with the instance.

          * For each attribute, the applicable value.

          Supported attribute keys include the following:

          * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load
          Balancing load balancer, the DNS name that is associated with the load balancer.

          * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in
          response to DNS queries, for example, ``example.com`` .

          * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in
          response to DNS queries, for example, ``192.0.2.44`` .

          * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in
          response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .

          * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the
          port. In addition, if the service includes ``HealthCheckConfig`` , the port on the
          endpoint that Route 53 sends requests to.

          - *(string) --*

            - *(string) --*
    """


_RequiredListNamespacesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListNamespacesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalListNamespacesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListNamespacesPaginateFiltersTypeDef", {"Condition": str}, total=False
)


class ListNamespacesPaginateFiltersTypeDef(
    _RequiredListNamespacesPaginateFiltersTypeDef,
    _OptionalListNamespacesPaginateFiltersTypeDef,
):
    """
    Type definition for `ListNamespacesPaginate` `Filters`

    A complex type that identifies the namespaces that you want to list. You can choose to list
    public or private namespaces.

    - **Name** *(string) --* **[REQUIRED]**

      Specify ``TYPE`` .

    - **Values** *(list) --* **[REQUIRED]**

      If you specify ``EQ`` for ``Condition`` , specify either ``DNS_PUBLIC`` or ``DNS_PRIVATE`` .

      If you specify ``IN`` for ``Condition`` , you can specify ``DNS_PUBLIC`` , ``DNS_PRIVATE`` ,
      or both.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether ``ListNamespaces`` returns a
      namespace. Valid values for ``condition`` include:

      * ``EQ`` : When you specify ``EQ`` for the condition, you can choose to list only public
      namespaces or private namespaces, but not both. ``EQ`` is the default condition and can be
      omitted.

      * ``IN`` : When you specify ``IN`` for the condition, you can choose to list public
      namespaces, private namespaces, or both.

      * ``BETWEEN`` : Not applicable
    """


_ListNamespacesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNamespacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNamespacesPaginatePaginationConfigTypeDef(
    _ListNamespacesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListNamespacesPaginate` `PaginationConfig`

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


_ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef
):
    """
    Type definition for `ListNamespacesPaginateResponseNamespacesProperties` `DnsProperties`

    A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
    creates when you create a namespace.

    - **HostedZoneId** *(string) --*

      The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
      namespace.
    """


_ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef
):
    """
    Type definition for `ListNamespacesPaginateResponseNamespacesProperties` `HttpProperties`

    A complex type that contains the name of an HTTP namespace.

    - **HttpName** *(string) --*

      The name of an HTTP namespace.
    """


_ListNamespacesPaginateResponseNamespacesPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesTypeDef
):
    """
    Type definition for `ListNamespacesPaginateResponseNamespaces` `Properties`

    A complex type that contains information that is specific to the namespace type.

    - **DnsProperties** *(dict) --*

      A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
      creates when you create a namespace.

      - **HostedZoneId** *(string) --*

        The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
        namespace.

    - **HttpProperties** *(dict) --*

      A complex type that contains the name of an HTTP namespace.

      - **HttpName** *(string) --*

        The name of an HTTP namespace.
    """


_ListNamespacesPaginateResponseNamespacesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": str,
        "Description": str,
        "ServiceCount": int,
        "Properties": ListNamespacesPaginateResponseNamespacesPropertiesTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ListNamespacesPaginateResponseNamespacesTypeDef(
    _ListNamespacesPaginateResponseNamespacesTypeDef
):
    """
    Type definition for `ListNamespacesPaginateResponse` `Namespaces`

    A complex type that contains information about a namespace.

    - **Id** *(string) --*

      The ID of the namespace.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you
      create it.

    - **Name** *(string) --*

      The name of the namespace. When you create a namespace, AWS Cloud Map automatically
      creates a Route 53 hosted zone that has the same name as the namespace.

    - **Type** *(string) --*

      The type of the namespace, either public or private.

    - **Description** *(string) --*

      A description for the namespace.

    - **ServiceCount** *(integer) --*

      The number of services that were created using the namespace.

    - **Properties** *(dict) --*

      A complex type that contains information that is specific to the namespace type.

      - **DnsProperties** *(dict) --*

        A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
        creates when you create a namespace.

        - **HostedZoneId** *(string) --*

          The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
          namespace.

      - **HttpProperties** *(dict) --*

        A complex type that contains the name of an HTTP namespace.

        - **HttpName** *(string) --*

          The name of an HTTP namespace.

    - **CreateDate** *(datetime) --*

      The date and time that the namespace was created.
    """


_ListNamespacesPaginateResponseTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseTypeDef",
    {"Namespaces": List[ListNamespacesPaginateResponseNamespacesTypeDef]},
    total=False,
)


class ListNamespacesPaginateResponseTypeDef(_ListNamespacesPaginateResponseTypeDef):
    """
    Type definition for `ListNamespacesPaginate` `Response`

    - **Namespaces** *(list) --*

      An array that contains one ``NamespaceSummary`` object for each namespace that matches the
      specified filter criteria.

      - *(dict) --*

        A complex type that contains information about a namespace.

        - **Id** *(string) --*

          The ID of the namespace.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you
          create it.

        - **Name** *(string) --*

          The name of the namespace. When you create a namespace, AWS Cloud Map automatically
          creates a Route 53 hosted zone that has the same name as the namespace.

        - **Type** *(string) --*

          The type of the namespace, either public or private.

        - **Description** *(string) --*

          A description for the namespace.

        - **ServiceCount** *(integer) --*

          The number of services that were created using the namespace.

        - **Properties** *(dict) --*

          A complex type that contains information that is specific to the namespace type.

          - **DnsProperties** *(dict) --*

            A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map
            creates when you create a namespace.

            - **HostedZoneId** *(string) --*

              The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a
              namespace.

          - **HttpProperties** *(dict) --*

            A complex type that contains the name of an HTTP namespace.

            - **HttpName** *(string) --*

              The name of an HTTP namespace.

        - **CreateDate** *(datetime) --*

          The date and time that the namespace was created.
    """


_RequiredListOperationsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListOperationsPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalListOperationsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListOperationsPaginateFiltersTypeDef", {"Condition": str}, total=False
)


class ListOperationsPaginateFiltersTypeDef(
    _RequiredListOperationsPaginateFiltersTypeDef,
    _OptionalListOperationsPaginateFiltersTypeDef,
):
    """
    Type definition for `ListOperationsPaginate` `Filters`

    A complex type that lets you select the operations that you want to list.

    - **Name** *(string) --* **[REQUIRED]**

      Specify the operations that you want to get:

      * **NAMESPACE_ID** : Gets operations related to specified namespaces.

      * **SERVICE_ID** : Gets operations related to specified services.

      * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` ,
      ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .

      * **TYPE** : Gets specified types of operation.

      * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.

    - **Values** *(list) --* **[REQUIRED]**

      Specify values that are applicable to the value that you specify for ``Name`` :

      * **NAMESPACE_ID** : Specify one namespace ID.

      * **SERVICE_ID** : Specify one service ID.

      * **STATUS** : Specify one or more statuses: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or
      ``FAIL`` .

      * **TYPE** : Specify one or more of the following types: ``CREATE_NAMESPACE`` ,
      ``DELETE_NAMESPACE`` , ``UPDATE_SERVICE`` , ``REGISTER_INSTANCE`` , or
      ``DEREGISTER_INSTANCE`` .

      * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and
      Coordinated Universal Time (UTC). The start date must be the first value.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether an operation matches the specified
      value. Valid values for condition include:

      * ``EQ`` : When you specify ``EQ`` for the condition, you can specify only one value. ``EQ``
      is supported for ``NAMESPACE_ID`` , ``SERVICE_ID`` , ``STATUS`` , and ``TYPE`` . ``EQ`` is
      the default condition and can be omitted.

      * ``IN`` : When you specify ``IN`` for the condition, you can specify a list of one or more
      values. ``IN`` is supported for ``STATUS`` and ``TYPE`` . An operation must match one of the
      specified values to be returned in the response.

      * ``BETWEEN`` : Specify a start date and an end date in Unix date/time format and Coordinated
      Universal Time (UTC). The start date must be the first value. ``BETWEEN`` is supported for
      ``UPDATE_DATE`` .
    """


_ListOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOperationsPaginatePaginationConfigTypeDef(
    _ListOperationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOperationsPaginate` `PaginationConfig`

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


_ListOperationsPaginateResponseOperationsTypeDef = TypedDict(
    "_ListOperationsPaginateResponseOperationsTypeDef",
    {"Id": str, "Status": str},
    total=False,
)


class ListOperationsPaginateResponseOperationsTypeDef(
    _ListOperationsPaginateResponseOperationsTypeDef
):
    """
    Type definition for `ListOperationsPaginateResponse` `Operations`

    A complex type that contains information about an operation that matches the criteria that
    you specified in a  ListOperations request.

    - **Id** *(string) --*

      The ID for an operation.

    - **Status** *(string) --*

      The status of the operation. Values include the following:

      * **SUBMITTED** : This is the initial state immediately after you submit a request.

      * **PENDING** : AWS Cloud Map is performing the operation.

      * **SUCCESS** : The operation succeeded.

      * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .
    """


_ListOperationsPaginateResponseTypeDef = TypedDict(
    "_ListOperationsPaginateResponseTypeDef",
    {"Operations": List[ListOperationsPaginateResponseOperationsTypeDef]},
    total=False,
)


class ListOperationsPaginateResponseTypeDef(_ListOperationsPaginateResponseTypeDef):
    """
    Type definition for `ListOperationsPaginate` `Response`

    - **Operations** *(list) --*

      Summary information about the operations that match the specified criteria.

      - *(dict) --*

        A complex type that contains information about an operation that matches the criteria that
        you specified in a  ListOperations request.

        - **Id** *(string) --*

          The ID for an operation.

        - **Status** *(string) --*

          The status of the operation. Values include the following:

          * **SUBMITTED** : This is the initial state immediately after you submit a request.

          * **PENDING** : AWS Cloud Map is performing the operation.

          * **SUCCESS** : The operation succeeded.

          * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` .
    """


_RequiredListServicesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListServicesPaginateFiltersTypeDef", {"Name": str, "Values": List[str]}
)
_OptionalListServicesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListServicesPaginateFiltersTypeDef", {"Condition": str}, total=False
)


class ListServicesPaginateFiltersTypeDef(
    _RequiredListServicesPaginateFiltersTypeDef,
    _OptionalListServicesPaginateFiltersTypeDef,
):
    """
    Type definition for `ListServicesPaginate` `Filters`

    A complex type that lets you specify the namespaces that you want to list services for.

    - **Name** *(string) --* **[REQUIRED]**

      Specify ``NAMESPACE_ID`` .

    - **Values** *(list) --* **[REQUIRED]**

      The values that are applicable to the value that you specify for ``Condition`` to filter the
      list of services.

      - *(string) --*

    - **Condition** *(string) --*

      The operator that you want to use to determine whether a service is returned by
      ``ListServices`` . Valid values for ``Condition`` include the following:

      * ``EQ`` : When you specify ``EQ`` , specify one namespace ID for ``Values`` . ``EQ`` is the
      default condition and can be omitted.

      * ``IN`` : When you specify ``IN`` , specify a list of the IDs for the namespaces that you
      want ``ListServices`` to return a list of services for.

      * ``BETWEEN`` : Not applicable.
    """


_ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServicesPaginatePaginationConfigTypeDef(
    _ListServicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServicesPaginate` `PaginationConfig`

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


_ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": str, "TTL": int},
    total=False,
)


class ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef(
    _ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef
):
    """
    Type definition for `ListServicesPaginateResponseServicesDnsConfig` `DnsRecords`

    A complex type that contains information about the Route 53 DNS records that you want
    AWS Cloud Map to create when you register an instance.

    - **Type** *(string) --*

      The type of the resource, which indicates the type of value that Route 53 returns
      in response to DNS queries.

      Note the following:

      * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
      one AAAA, and one SRV record. You can specify them in any combination.

      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
      other records. This is a limitation of DNS: you can't create a CNAME record and any
      other type of record that has the same name as a CNAME record.

      * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
      when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

      * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
      register an instance.

      The following values are supported:

       **A**

      Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

       **AAAA**

      Route 53 returns the IP address of the resource in IPv6 format, such as
      2001:0db8:85a3:0000:0000:abcd:0001:2345.

       **CNAME**

      Route 53 returns the domain name of the resource, such as www.example.com. Note the
      following:

      * You specify the domain name that you want to route traffic to when you register
      an instance. For more information, see  RegisterInstanceRequest$Attributes .

      * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

      * You can't specify both ``CNAME`` for ``Type`` and settings for
      ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
      error.

       **SRV**

      Route 53 returns the value for an SRV record. The value for an SRV record uses the
      following values:

       ``priority weight port service-hostname``

      Note the following about the values:

      * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
      changed.

      * The value of ``port`` comes from the value that you specify for the
      ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

      * The value of ``service-hostname`` is a concatenation of the following values:

        * The value that you specify for ``InstanceId`` when you register an instance.

        * The name of the service.

        * The name of the namespace.

      For example, if the value of ``InstanceId`` is ``test`` , the name of the service
      is ``backend`` , and the name of the namespace is ``example.com`` , the value of
      ``service-hostname`` is:

       ``test.backend.example.com``

      If you specify settings for an SRV record and if you specify values for
      ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
      request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
      have the same name as the value of ``service-hostname`` in the SRV record. You can
      ignore these records.

    - **TTL** *(integer) --*

      The amount of time, in seconds, that you want DNS resolvers to cache the settings
      for this record.

      .. note::

        Alias records don't include a TTL because Route 53 uses the TTL for the AWS
        resource that an alias record routes traffic to. If you include the
        ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
        ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
        service to register instances that create either alias or non-alias records.
    """


_ListServicesPaginateResponseServicesDnsConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": str,
        "DnsRecords": List[
            ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef
        ],
    },
    total=False,
)


class ListServicesPaginateResponseServicesDnsConfigTypeDef(
    _ListServicesPaginateResponseServicesDnsConfigTypeDef
):
    """
    Type definition for `ListServicesPaginateResponseServices` `DnsConfig`

    A complex type that contains information about the Amazon Route 53 DNS records that you
    want AWS Cloud Map to create when you register an instance.

    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.

    - **RoutingPolicy** *(string) --*

      The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
      Map creates when you register an instance and specify this service.

      .. note::

        If you want to use this service to register instances that create alias records,
        specify ``WEIGHTED`` for the routing policy.

      You can specify the following values:

       **MULTIVALUE**

      If you define a health check for the service and the health check is healthy, Route 53
      returns the applicable value for up to eight instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS
      queries with IP addresses for up to eight healthy instances. If fewer than eight
      instances are healthy, Route 53 responds to every DNS query with the IP addresses for
      all of the healthy instances.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the values for up to eight instances.

      For more information about the multivalue routing policy, see `Multivalue Answer
      Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
      in the *Route 53 Developer Guide* .

       **WEIGHTED**

      Route 53 returns the applicable value from one randomly selected instance from among
      the instances that you registered using the same service. Currently, all records have
      the same weight, so you can't route more or less traffic to any instances.

      For example, suppose the service includes configurations for one A record and a health
      check, and you use the service to register 10 instances. Route 53 responds to DNS
      queries with the IP address for one randomly selected instance from among the healthy
      instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
      the instances were healthy.

      If you don't define a health check for the service, Route 53 assumes that all instances
      are healthy and returns the applicable value for one randomly selected instance.

      For more information about the weighted routing policy, see `Weighted Routing
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
      in the *Route 53 Developer Guide* .

    - **DnsRecords** *(list) --*

      An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
      want AWS Cloud Map to create when you register an instance.

      - *(dict) --*

        A complex type that contains information about the Route 53 DNS records that you want
        AWS Cloud Map to create when you register an instance.

        - **Type** *(string) --*

          The type of the resource, which indicates the type of value that Route 53 returns
          in response to DNS queries.

          Note the following:

          * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
          one AAAA, and one SRV record. You can specify them in any combination.

          * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
          other records. This is a limitation of DNS: you can't create a CNAME record and any
          other type of record that has the same name as a CNAME record.

          * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
          when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

          * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
          register an instance.

          The following values are supported:

           **A**

          Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

           **AAAA**

          Route 53 returns the IP address of the resource in IPv6 format, such as
          2001:0db8:85a3:0000:0000:abcd:0001:2345.

           **CNAME**

          Route 53 returns the domain name of the resource, such as www.example.com. Note the
          following:

          * You specify the domain name that you want to route traffic to when you register
          an instance. For more information, see  RegisterInstanceRequest$Attributes .

          * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

          * You can't specify both ``CNAME`` for ``Type`` and settings for
          ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
          error.

           **SRV**

          Route 53 returns the value for an SRV record. The value for an SRV record uses the
          following values:

           ``priority weight port service-hostname``

          Note the following about the values:

          * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
          changed.

          * The value of ``port`` comes from the value that you specify for the
          ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

          * The value of ``service-hostname`` is a concatenation of the following values:

            * The value that you specify for ``InstanceId`` when you register an instance.

            * The name of the service.

            * The name of the namespace.

          For example, if the value of ``InstanceId`` is ``test`` , the name of the service
          is ``backend`` , and the name of the namespace is ``example.com`` , the value of
          ``service-hostname`` is:

           ``test.backend.example.com``

          If you specify settings for an SRV record and if you specify values for
          ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
          request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
          have the same name as the value of ``service-hostname`` in the SRV record. You can
          ignore these records.

        - **TTL** *(integer) --*

          The amount of time, in seconds, that you want DNS resolvers to cache the settings
          for this record.

          .. note::

            Alias records don't include a TTL because Route 53 uses the TTL for the AWS
            resource that an alias record routes traffic to. If you include the
            ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
            ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
            service to register instances that create either alias or non-alias records.
    """


_ListServicesPaginateResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesHealthCheckConfigTypeDef",
    {"Type": str, "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ListServicesPaginateResponseServicesHealthCheckConfigTypeDef(
    _ListServicesPaginateResponseServicesHealthCheckConfigTypeDef
):
    """
    Type definition for `ListServicesPaginateResponseServices` `HealthCheckConfig`

     *Public DNS namespaces only.* A complex type that contains settings for an optional
     health check. If you specify settings for a health check, AWS Cloud Map associates the
     health check with the records that you specify in ``DnsConfig`` .

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
    information about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    Note the following about configuring health checks.

     **A and AAAA records**

    If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
    creates a health check that uses the IPv4 address to check the health of the resource. If
    the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
    the A and AAAA records to be unhealthy.

     **CNAME records**

    You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
    ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
    with an ``InvalidInput`` error.

     **Request interval**

    A Route 53 health checker in each health-checking region sends a health check request to
    an endpoint every 30 seconds. On average, your endpoint receives a health check request
    about every two seconds. However, health checkers don't coordinate with one another, so
    you'll sometimes see several requests per second followed by a few seconds with no health
    checks at all.

     **Health checking regions**

    Health checkers perform checks from all Route 53 health-checking regions. For a list of
    the current regions, see `Regions
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
    .

     **Alias records**

    When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
    Cloud Map creates a Route 53 alias record. Note the following:

    * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
    ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
    AWS resource. such as an ELB load balancer. For more information, see
    `EvaluateTargetHealth
    <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
    .

    * If you include ``HealthCheckConfig`` and then use the service to register an instance
    that creates an alias record, Route 53 doesn't create the health check.

     **Charges for health checks**

    Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
    information about pricing for health checks, see `Amazon Route 53 Pricing
    <http://aws.amazon.com/route53/pricing/>`__ .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Route 53
      determines whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTP request and waits for an HTTP status code of 200 or greater and less
      than 400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
      than 400.

      .. warning::

         If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
         or later.

      * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
      ``Type`` , don't specify a value for ``ResourcePath`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path that you want Route 53 to request when performing health checks. The path can
      be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
      the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
      53 automatically adds the DNS name for the service. If you don't specify a value for
      ``ResourcePath`` , the default value is ``/`` .

      If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
      ``ResourcePath`` .

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Route 53
      to change the current status of the endpoint from unhealthy to healthy or vice versa.
      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Route 53 Developer Guide* .
    """


_ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef(
    _ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef
):
    """
    Type definition for `ListServicesPaginateResponseServices` `HealthCheckCustomConfig`

    A complex type that contains information about an optional custom health check. A custom
    health check, which requires that you use a third-party health checker to evaluate the
    health of your resources, is useful in the following circumstances:

    * You can't use a health check that is defined by ``HealthCheckConfig`` because the
    resource isn't available over the internet. For example, you can use a custom health
    check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
    the health checker must also be in the VPC.)

    * You want to use a third-party health checker regardless of where your resources are.

    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

    To change the status of a custom health check, submit an
    ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
    resource, it just keeps a record of the status specified in the most recent
    ``UpdateInstanceCustomHealthStatus`` request.

    Here's how custom health checks work:

    * You create a service and specify a value for ``FailureThreshold`` .  The failure
    threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
    between the time that your application sends an  UpdateInstanceCustomHealthStatus request
    and the time that AWS Cloud Map stops routing internet traffic to the corresponding
    resource.

    * You register an instance.

    * You configure a third-party health checker to monitor the resource that is associated
    with the new instance.

    .. note::

       AWS Cloud Map doesn't check the health of the resource directly.

    * The third-party health-checker determines that the resource is unhealthy and notifies
    your application.

    * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

    * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

    * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
    to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

    Note the following about configuring custom health checks.

    - **FailureThreshold** *(integer) --*

      The number of 30-second intervals that you want Cloud Map to wait after receiving an
      ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
      service instance. For example, suppose you specify a value of ``2`` for
      ``FailureTheshold`` , and then your application sends an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
      seconds (2 x 30) before changing the status of the service instance based on that
      request.

      Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
      same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
      change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
      to make the change.
    """


_ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ListServicesPaginateResponseServicesDnsConfigTypeDef,
        "HealthCheckConfig": ListServicesPaginateResponseServicesHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ListServicesPaginateResponseServicesTypeDef(
    _ListServicesPaginateResponseServicesTypeDef
):
    """
    Type definition for `ListServicesPaginateResponse` `Services`

    A complex type that contains information about a specified service.

    - **Id** *(string) --*

      The ID that AWS Cloud Map assigned to the service when you created it.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create
      it.

    - **Name** *(string) --*

      The name of the service.

    - **Description** *(string) --*

      The description that you specify when you create the service.

    - **InstanceCount** *(integer) --*

      The number of instances that are currently associated with the service. Instances that
      were previously associated with the service but that have been deleted are not included
      in the count.

    - **DnsConfig** *(dict) --*

      A complex type that contains information about the Amazon Route 53 DNS records that you
      want AWS Cloud Map to create when you register an instance.

      - **NamespaceId** *(string) --*

        The ID of the namespace to use for DNS configuration.

      - **RoutingPolicy** *(string) --*

        The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
        Map creates when you register an instance and specify this service.

        .. note::

          If you want to use this service to register instances that create alias records,
          specify ``WEIGHTED`` for the routing policy.

        You can specify the following values:

         **MULTIVALUE**

        If you define a health check for the service and the health check is healthy, Route 53
        returns the applicable value for up to eight instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS
        queries with IP addresses for up to eight healthy instances. If fewer than eight
        instances are healthy, Route 53 responds to every DNS query with the IP addresses for
        all of the healthy instances.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the values for up to eight instances.

        For more information about the multivalue routing policy, see `Multivalue Answer
        Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
        in the *Route 53 Developer Guide* .

         **WEIGHTED**

        Route 53 returns the applicable value from one randomly selected instance from among
        the instances that you registered using the same service. Currently, all records have
        the same weight, so you can't route more or less traffic to any instances.

        For example, suppose the service includes configurations for one A record and a health
        check, and you use the service to register 10 instances. Route 53 responds to DNS
        queries with the IP address for one randomly selected instance from among the healthy
        instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
        the instances were healthy.

        If you don't define a health check for the service, Route 53 assumes that all instances
        are healthy and returns the applicable value for one randomly selected instance.

        For more information about the weighted routing policy, see `Weighted Routing
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
        in the *Route 53 Developer Guide* .

      - **DnsRecords** *(list) --*

        An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
        want AWS Cloud Map to create when you register an instance.

        - *(dict) --*

          A complex type that contains information about the Route 53 DNS records that you want
          AWS Cloud Map to create when you register an instance.

          - **Type** *(string) --*

            The type of the resource, which indicates the type of value that Route 53 returns
            in response to DNS queries.

            Note the following:

            * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
            one AAAA, and one SRV record. You can specify them in any combination.

            * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
            other records. This is a limitation of DNS: you can't create a CNAME record and any
            other type of record that has the same name as a CNAME record.

            * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
            when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

            * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
            register an instance.

            The following values are supported:

             **A**

            Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

             **AAAA**

            Route 53 returns the IP address of the resource in IPv6 format, such as
            2001:0db8:85a3:0000:0000:abcd:0001:2345.

             **CNAME**

            Route 53 returns the domain name of the resource, such as www.example.com. Note the
            following:

            * You specify the domain name that you want to route traffic to when you register
            an instance. For more information, see  RegisterInstanceRequest$Attributes .

            * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

            * You can't specify both ``CNAME`` for ``Type`` and settings for
            ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
            error.

             **SRV**

            Route 53 returns the value for an SRV record. The value for an SRV record uses the
            following values:

             ``priority weight port service-hostname``

            Note the following about the values:

            * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
            changed.

            * The value of ``port`` comes from the value that you specify for the
            ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

            * The value of ``service-hostname`` is a concatenation of the following values:

              * The value that you specify for ``InstanceId`` when you register an instance.

              * The name of the service.

              * The name of the namespace.

            For example, if the value of ``InstanceId`` is ``test`` , the name of the service
            is ``backend`` , and the name of the namespace is ``example.com`` , the value of
            ``service-hostname`` is:

             ``test.backend.example.com``

            If you specify settings for an SRV record and if you specify values for
            ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
            request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
            have the same name as the value of ``service-hostname`` in the SRV record. You can
            ignore these records.

          - **TTL** *(integer) --*

            The amount of time, in seconds, that you want DNS resolvers to cache the settings
            for this record.

            .. note::

              Alias records don't include a TTL because Route 53 uses the TTL for the AWS
              resource that an alias record routes traffic to. If you include the
              ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
              ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
              service to register instances that create either alias or non-alias records.

    - **HealthCheckConfig** *(dict) --*

       *Public DNS namespaces only.* A complex type that contains settings for an optional
       health check. If you specify settings for a health check, AWS Cloud Map associates the
       health check with the records that you specify in ``DnsConfig`` .

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
      information about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      Note the following about configuring health checks.

       **A and AAAA records**

      If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
      creates a health check that uses the IPv4 address to check the health of the resource. If
      the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
      the A and AAAA records to be unhealthy.

       **CNAME records**

      You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
      ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
      with an ``InvalidInput`` error.

       **Request interval**

      A Route 53 health checker in each health-checking region sends a health check request to
      an endpoint every 30 seconds. On average, your endpoint receives a health check request
      about every two seconds. However, health checkers don't coordinate with one another, so
      you'll sometimes see several requests per second followed by a few seconds with no health
      checks at all.

       **Health checking regions**

      Health checkers perform checks from all Route 53 health-checking regions. For a list of
      the current regions, see `Regions
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
      .

       **Alias records**

      When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
      Cloud Map creates a Route 53 alias record. Note the following:

      * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
      ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
      AWS resource. such as an ELB load balancer. For more information, see
      `EvaluateTargetHealth
      <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
      .

      * If you include ``HealthCheckConfig`` and then use the service to register an instance
      that creates an alias record, Route 53 doesn't create the health check.

       **Charges for health checks**

      Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
      information about pricing for health checks, see `Amazon Route 53 Pricing
      <http://aws.amazon.com/route53/pricing/>`__ .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Route 53
        determines whether an endpoint is healthy.

        .. warning::

          You can't change the value of ``Type`` after you create a health check.

        You can create the following types of health checks:

        * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTP request and waits for an HTTP status code of 200 or greater and less
        than 400.

        * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
        submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
        than 400.

        .. warning::

           If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
           or later.

        * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
        ``Type`` , don't specify a value for ``ResourcePath`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path that you want Route 53 to request when performing health checks. The path can
        be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
        the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
        53 automatically adds the DNS name for the service. If you don't specify a value for
        ``ResourcePath`` , the default value is ``/`` .

        If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
        ``ResourcePath`` .

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Route 53
        to change the current status of the endpoint from unhealthy to healthy or vice versa.
        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Route 53 Developer Guide* .

    - **HealthCheckCustomConfig** *(dict) --*

      A complex type that contains information about an optional custom health check. A custom
      health check, which requires that you use a third-party health checker to evaluate the
      health of your resources, is useful in the following circumstances:

      * You can't use a health check that is defined by ``HealthCheckConfig`` because the
      resource isn't available over the internet. For example, you can use a custom health
      check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
      the health checker must also be in the VPC.)

      * You want to use a third-party health checker regardless of where your resources are.

      .. warning::

        If you specify a health check configuration, you can specify either
        ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

      To change the status of a custom health check, submit an
      ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
      resource, it just keeps a record of the status specified in the most recent
      ``UpdateInstanceCustomHealthStatus`` request.

      Here's how custom health checks work:

      * You create a service and specify a value for ``FailureThreshold`` .  The failure
      threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
      between the time that your application sends an  UpdateInstanceCustomHealthStatus request
      and the time that AWS Cloud Map stops routing internet traffic to the corresponding
      resource.

      * You register an instance.

      * You configure a third-party health checker to monitor the resource that is associated
      with the new instance.

      .. note::

         AWS Cloud Map doesn't check the health of the resource directly.

      * The third-party health-checker determines that the resource is unhealthy and notifies
      your application.

      * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

      * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

      * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
      to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

      Note the following about configuring custom health checks.

      - **FailureThreshold** *(integer) --*

        The number of 30-second intervals that you want Cloud Map to wait after receiving an
        ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
        service instance. For example, suppose you specify a value of ``2`` for
        ``FailureTheshold`` , and then your application sends an
        ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
        seconds (2 x 30) before changing the status of the service instance based on that
        request.

        Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
        same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
        change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
        to make the change.

    - **CreateDate** *(datetime) --*

      The date and time that the service was created.
    """


_ListServicesPaginateResponseTypeDef = TypedDict(
    "_ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)


class ListServicesPaginateResponseTypeDef(_ListServicesPaginateResponseTypeDef):
    """
    Type definition for `ListServicesPaginate` `Response`

    - **Services** *(list) --*

      An array that contains one ``ServiceSummary`` object for each service that matches the
      specified filter criteria.

      - *(dict) --*

        A complex type that contains information about a specified service.

        - **Id** *(string) --*

          The ID that AWS Cloud Map assigned to the service when you created it.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create
          it.

        - **Name** *(string) --*

          The name of the service.

        - **Description** *(string) --*

          The description that you specify when you create the service.

        - **InstanceCount** *(integer) --*

          The number of instances that are currently associated with the service. Instances that
          were previously associated with the service but that have been deleted are not included
          in the count.

        - **DnsConfig** *(dict) --*

          A complex type that contains information about the Amazon Route 53 DNS records that you
          want AWS Cloud Map to create when you register an instance.

          - **NamespaceId** *(string) --*

            The ID of the namespace to use for DNS configuration.

          - **RoutingPolicy** *(string) --*

            The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud
            Map creates when you register an instance and specify this service.

            .. note::

              If you want to use this service to register instances that create alias records,
              specify ``WEIGHTED`` for the routing policy.

            You can specify the following values:

             **MULTIVALUE**

            If you define a health check for the service and the health check is healthy, Route 53
            returns the applicable value for up to eight instances.

            For example, suppose the service includes configurations for one A record and a health
            check, and you use the service to register 10 instances. Route 53 responds to DNS
            queries with IP addresses for up to eight healthy instances. If fewer than eight
            instances are healthy, Route 53 responds to every DNS query with the IP addresses for
            all of the healthy instances.

            If you don't define a health check for the service, Route 53 assumes that all instances
            are healthy and returns the values for up to eight instances.

            For more information about the multivalue routing policy, see `Multivalue Answer
            Routing
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__
            in the *Route 53 Developer Guide* .

             **WEIGHTED**

            Route 53 returns the applicable value from one randomly selected instance from among
            the instances that you registered using the same service. Currently, all records have
            the same weight, so you can't route more or less traffic to any instances.

            For example, suppose the service includes configurations for one A record and a health
            check, and you use the service to register 10 instances. Route 53 responds to DNS
            queries with the IP address for one randomly selected instance from among the healthy
            instances. If no instances are healthy, Route 53 responds to DNS queries as if all of
            the instances were healthy.

            If you don't define a health check for the service, Route 53 assumes that all instances
            are healthy and returns the applicable value for one randomly selected instance.

            For more information about the weighted routing policy, see `Weighted Routing
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__
            in the *Route 53 Developer Guide* .

          - **DnsRecords** *(list) --*

            An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you
            want AWS Cloud Map to create when you register an instance.

            - *(dict) --*

              A complex type that contains information about the Route 53 DNS records that you want
              AWS Cloud Map to create when you register an instance.

              - **Type** *(string) --*

                The type of the resource, which indicates the type of value that Route 53 returns
                in response to DNS queries.

                Note the following:

                * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A,
                one AAAA, and one SRV record. You can specify them in any combination.

                * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any
                other records. This is a limitation of DNS: you can't create a CNAME record and any
                other type of record that has the same name as a CNAME record.

                * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record
                when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` .

                * **All records:** You specify settings other than ``TTL`` and ``Type`` when you
                register an instance.

                The following values are supported:

                 **A**

                Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.

                 **AAAA**

                Route 53 returns the IP address of the resource in IPv6 format, such as
                2001:0db8:85a3:0000:0000:abcd:0001:2345.

                 **CNAME**

                Route 53 returns the domain name of the resource, such as www.example.com. Note the
                following:

                * You specify the domain name that you want to route traffic to when you register
                an instance. For more information, see  RegisterInstanceRequest$Attributes .

                * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` .

                * You can't specify both ``CNAME`` for ``Type`` and settings for
                ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput``
                error.

                 **SRV**

                Route 53 returns the value for an SRV record. The value for an SRV record uses the
                following values:

                 ``priority weight port service-hostname``

                Note the following about the values:

                * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be
                changed.

                * The value of ``port`` comes from the value that you specify for the
                ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.

                * The value of ``service-hostname`` is a concatenation of the following values:

                  * The value that you specify for ``InstanceId`` when you register an instance.

                  * The name of the service.

                  * The name of the namespace.

                For example, if the value of ``InstanceId`` is ``test`` , the name of the service
                is ``backend`` , and the name of the namespace is ``example.com`` , the value of
                ``service-hostname`` is:

                 ``test.backend.example.com``

                If you specify settings for an SRV record and if you specify values for
                ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance``
                request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that
                have the same name as the value of ``service-hostname`` in the SRV record. You can
                ignore these records.

              - **TTL** *(integer) --*

                The amount of time, in seconds, that you want DNS resolvers to cache the settings
                for this record.

                .. note::

                  Alias records don't include a TTL because Route 53 uses the TTL for the AWS
                  resource that an alias record routes traffic to. If you include the
                  ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the
                  ``TTL`` value is ignored. Always specify a TTL for the service; you can use a
                  service to register instances that create either alias or non-alias records.

        - **HealthCheckConfig** *(dict) --*

           *Public DNS namespaces only.* A complex type that contains settings for an optional
           health check. If you specify settings for a health check, AWS Cloud Map associates the
           health check with the records that you specify in ``DnsConfig`` .

          .. warning::

            If you specify a health check configuration, you can specify either
            ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

          Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
          information about pricing for health checks, see `Amazon Route 53 Pricing
          <http://aws.amazon.com/route53/pricing/>`__ .

          Note the following about configuring health checks.

           **A and AAAA records**

          If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map
          creates a health check that uses the IPv4 address to check the health of the resource. If
          the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both
          the A and AAAA records to be unhealthy.

           **CNAME records**

          You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes
          ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail
          with an ``InvalidInput`` error.

           **Request interval**

          A Route 53 health checker in each health-checking region sends a health check request to
          an endpoint every 30 seconds. On average, your endpoint receives a health check request
          about every two seconds. However, health checkers don't coordinate with one another, so
          you'll sometimes see several requests per second followed by a few seconds with no health
          checks at all.

           **Health checking regions**

          Health checkers perform checks from all Route 53 health-checking regions. For a list of
          the current regions, see `Regions
          <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__
          .

           **Alias records**

          When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS
          Cloud Map creates a Route 53 alias record. Note the following:

          * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When
          ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced
          AWS resource. such as an ELB load balancer. For more information, see
          `EvaluateTargetHealth
          <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__
          .

          * If you include ``HealthCheckConfig`` and then use the service to register an instance
          that creates an alias record, Route 53 doesn't create the health check.

           **Charges for health checks**

          Health checks are basic Route 53 health checks that monitor an AWS endpoint. For
          information about pricing for health checks, see `Amazon Route 53 Pricing
          <http://aws.amazon.com/route53/pricing/>`__ .

          - **Type** *(string) --*

            The type of health check that you want to create, which indicates how Route 53
            determines whether an endpoint is healthy.

            .. warning::

              You can't change the value of ``Type`` after you create a health check.

            You can create the following types of health checks:

            * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53
            submits an HTTP request and waits for an HTTP status code of 200 or greater and less
            than 400.

            * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53
            submits an HTTPS request and waits for an HTTP status code of 200 or greater and less
            than 400.

            .. warning::

               If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0
               or later.

            * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for
            ``Type`` , don't specify a value for ``ResourcePath`` .

            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Route 53 Developer Guide* .

          - **ResourcePath** *(string) --*

            The path that you want Route 53 to request when performing health checks. The path can
            be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when
            the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route
            53 automatically adds the DNS name for the service. If you don't specify a value for
            ``ResourcePath`` , the default value is ``/`` .

            If you specify ``TCP`` for ``Type`` , you must *not* specify a value for
            ``ResourcePath`` .

          - **FailureThreshold** *(integer) --*

            The number of consecutive health checks that an endpoint must pass or fail for Route 53
            to change the current status of the endpoint from unhealthy to healthy or vice versa.
            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Route 53 Developer Guide* .

        - **HealthCheckCustomConfig** *(dict) --*

          A complex type that contains information about an optional custom health check. A custom
          health check, which requires that you use a third-party health checker to evaluate the
          health of your resources, is useful in the following circumstances:

          * You can't use a health check that is defined by ``HealthCheckConfig`` because the
          resource isn't available over the internet. For example, you can use a custom health
          check when the instance is in an Amazon VPC. (To check the health of resources in a VPC,
          the health checker must also be in the VPC.)

          * You want to use a third-party health checker regardless of where your resources are.

          .. warning::

            If you specify a health check configuration, you can specify either
            ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.

          To change the status of a custom health check, submit an
          ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the
          resource, it just keeps a record of the status specified in the most recent
          ``UpdateInstanceCustomHealthStatus`` request.

          Here's how custom health checks work:

          * You create a service and specify a value for ``FailureThreshold`` .  The failure
          threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait
          between the time that your application sends an  UpdateInstanceCustomHealthStatus request
          and the time that AWS Cloud Map stops routing internet traffic to the corresponding
          resource.

          * You register an instance.

          * You configure a third-party health checker to monitor the resource that is associated
          with the new instance.

          .. note::

             AWS Cloud Map doesn't check the health of the resource directly.

          * The third-party health-checker determines that the resource is unhealthy and notifies
          your application.

          * Your application submits an ``UpdateInstanceCustomHealthStatus`` request.

          * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds.

          * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time
          to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource.

          Note the following about configuring custom health checks.

          - **FailureThreshold** *(integer) --*

            The number of 30-second intervals that you want Cloud Map to wait after receiving an
            ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a
            service instance. For example, suppose you specify a value of ``2`` for
            ``FailureTheshold`` , and then your application sends an
            ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60
            seconds (2 x 30) before changing the status of the service instance based on that
            request.

            Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the
            same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the
            change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request
            to make the change.

        - **CreateDate** *(datetime) --*

          The date and time that the service was created.
    """
