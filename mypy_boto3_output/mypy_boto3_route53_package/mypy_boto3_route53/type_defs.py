"Main interface for route53 type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    "ClientAssociateVpcWithHostedZoneResponseTypeDef",
    "ClientAssociateVpcWithHostedZoneVPCTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    "ClientChangeResourceRecordSetsChangeBatchTypeDef",
    "ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    "ClientChangeResourceRecordSetsResponseTypeDef",
    "ClientChangeTagsForResourceAddTagsTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientCreateHealthCheckResponseHealthCheckTypeDef",
    "ClientCreateHealthCheckResponseTypeDef",
    "ClientCreateHostedZoneHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseChangeInfoTypeDef",
    "ClientCreateHostedZoneResponseDelegationSetTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientCreateHostedZoneResponseHostedZoneTypeDef",
    "ClientCreateHostedZoneResponseVPCTypeDef",
    "ClientCreateHostedZoneResponseTypeDef",
    "ClientCreateHostedZoneVPCTypeDef",
    "ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientCreateQueryLoggingConfigResponseTypeDef",
    "ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientCreateReusableDelegationSetResponseTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientCreateTrafficPolicyInstanceResponseTypeDef",
    "ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyResponseTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    "ClientCreateTrafficPolicyVersionResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    "ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    "ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    "ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    "ClientDeleteHostedZoneResponseTypeDef",
    "ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    "ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    "ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    "ClientGetAccountLimitResponseLimitTypeDef",
    "ClientGetAccountLimitResponseTypeDef",
    "ClientGetChangeResponseChangeInfoTypeDef",
    "ClientGetChangeResponseTypeDef",
    "ClientGetCheckerIpRangesResponseTypeDef",
    "ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    "ClientGetGeoLocationResponseTypeDef",
    "ClientGetHealthCheckCountResponseTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientGetHealthCheckResponseHealthCheckTypeDef",
    "ClientGetHealthCheckResponseTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    "ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    "ClientGetHealthCheckStatusResponseTypeDef",
    "ClientGetHostedZoneCountResponseTypeDef",
    "ClientGetHostedZoneLimitResponseLimitTypeDef",
    "ClientGetHostedZoneLimitResponseTypeDef",
    "ClientGetHostedZoneResponseDelegationSetTypeDef",
    "ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    "ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    "ClientGetHostedZoneResponseHostedZoneTypeDef",
    "ClientGetHostedZoneResponseVPCsTypeDef",
    "ClientGetHostedZoneResponseTypeDef",
    "ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    "ClientGetQueryLoggingConfigResponseTypeDef",
    "ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    "ClientGetReusableDelegationSetLimitResponseTypeDef",
    "ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    "ClientGetReusableDelegationSetResponseTypeDef",
    "ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientGetTrafficPolicyInstanceResponseTypeDef",
    "ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    "ClientGetTrafficPolicyResponseTypeDef",
    "ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    "ClientListGeoLocationsResponseTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    "ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    "ClientListHealthChecksResponseHealthChecksTypeDef",
    "ClientListHealthChecksResponseTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    "ClientListHostedZonesByNameResponseTypeDef",
    "ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    "ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    "ClientListHostedZonesResponseHostedZonesTypeDef",
    "ClientListHostedZonesResponseTypeDef",
    "ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    "ClientListQueryLoggingConfigsResponseTypeDef",
    "ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    "ClientListReusableDelegationSetsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    "ClientListTagsForResourceResponseResourceTagSetTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    "ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    "ClientListTagsForResourcesResponseTypeDef",
    "ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    "ClientListTrafficPoliciesResponseTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    "ClientListTrafficPolicyInstancesResponseTypeDef",
    "ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    "ClientListTrafficPolicyVersionsResponseTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    "ClientListVpcAssociationAuthorizationsResponseTypeDef",
    "ClientTestDnsAnswerResponseTypeDef",
    "ClientUpdateHealthCheckAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    "ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    "ClientUpdateHealthCheckResponseTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    "ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    "ClientUpdateHostedZoneCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    "ClientUpdateTrafficPolicyCommentResponseTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    "ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    "ListHealthChecksPaginatePaginationConfigTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef",
    "ListHealthChecksPaginateResponseHealthChecksTypeDef",
    "ListHealthChecksPaginateResponseTypeDef",
    "ListHostedZonesPaginatePaginationConfigTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesConfigTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef",
    "ListHostedZonesPaginateResponseHostedZonesTypeDef",
    "ListHostedZonesPaginateResponseTypeDef",
    "ListQueryLoggingConfigsPaginatePaginationConfigTypeDef",
    "ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef",
    "ListQueryLoggingConfigsPaginateResponseTypeDef",
    "ListResourceRecordSetsPaginatePaginationConfigTypeDef",
    "ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef",
    "ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef",
    "ListVPCAssociationAuthorizationsPaginateResponseTypeDef",
    "ResourceRecordSetsChangedWaitWaiterConfigTypeDef",
)


_ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef(
    _ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientAssociateVpcWithHostedZoneResponse` `ChangeInfo`

    A complex type that describes the changes made to your hosted zone.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientAssociateVpcWithHostedZoneResponseTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientAssociateVpcWithHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientAssociateVpcWithHostedZoneResponseTypeDef(
    _ClientAssociateVpcWithHostedZoneResponseTypeDef
):
    """
    Type definition for `ClientAssociateVpcWithHostedZone` `Response`

    A complex type that contains the response information for the ``AssociateVPCWithHostedZone``
    request.

    - **ChangeInfo** *(dict) --*

      A complex type that describes the changes made to your hosted zone.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
    """


_ClientAssociateVpcWithHostedZoneVPCTypeDef = TypedDict(
    "_ClientAssociateVpcWithHostedZoneVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientAssociateVpcWithHostedZoneVPCTypeDef(
    _ClientAssociateVpcWithHostedZoneVPCTypeDef
):
    """
    Type definition for `ClientAssociateVpcWithHostedZone` `VPC`

    A complex type that contains information about the VPC that you want to associate with a private
    hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef",
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef
):
    """
    Type definition for `ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSet` `GeoLocation`

     *Geolocation resource record sets only:* A complex type that lets you control how Amazon
     Route 53 responds to DNS queries based on the geographic origin of the query. For
     example, if you want all queries from Africa to be routed to a web server with an IP
     address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a
     ``ContinentCode`` of ``AF`` .

    .. note::

      Creating geolocation and geolocation alias resource record sets in private hosted zones
      is not supported.

    If you create separate resource record sets for overlapping geographic regions (for
    example, one resource record set for a continent and one for a country on the same
    continent), priority goes to the smallest geographic region. This allows you to route
    most queries for a continent to one resource and to route queries for a country on that
    continent to a different resource.

    You can't create two geolocation resource record sets that specify the same geographic
    location.

    The value ``*`` in the ``CountryCode`` element matches all geographic locations that
    aren't specified in other geolocation resource record sets that have the same values for
    the ``Name`` and ``Type`` elements.

    .. warning::

      Geolocation works by mapping IP addresses to locations. However, some IP addresses
      aren't mapped to geographic locations, so even if you create geolocation resource
      record sets that cover all seven continents, Route 53 will receive some DNS queries
      from locations that it can't identify. We recommend that you create a resource record
      set for which the value of ``CountryCode`` is ``*`` , which handles both queries that
      come from locations for which you haven't created geolocation resource record sets and
      queries from IP addresses that aren't mapped to a location. If you don't create a ``*``
      resource record set, Route 53 returns a "no answer" response for queries from those
      locations.

    You can't create non-geolocation resource record sets that have the same values for the
    ``Name`` and ``Type`` elements as geolocation resource record sets.

    - **ContinentCode** *(string) --*

      The two-letter code for the continent.

      Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``

      Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or
      ``SubdivisionCode`` returns an ``InvalidInput`` error.

    - **CountryCode** *(string) --*

      The two-letter code for the country.

    - **SubdivisionCode** *(string) --*

      The code for the subdivision. Route 53 currently supports only states in the United
      States.
    """


_RequiredClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef = TypedDict(
    "_RequiredClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    {"Name": str, "Type": str},
)
_OptionalClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef = TypedDict(
    "_OptionalClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": str,
        "GeoLocation": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetGeoLocationTypeDef,
        "Failover": str,
    },
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef(
    _RequiredClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef,
    _OptionalClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef,
):
    """
    Type definition for `ClientChangeResourceRecordSetsChangeBatchChanges` `ResourceRecordSet`

    Information about the resource record set to create, delete, or update.

    - **Name** *(string) --* **[REQUIRED]**

      For ``ChangeResourceRecordSets`` requests, the name of the record that you want to
      create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record
      in the specified hosted zone.

       **ChangeResourceRecordSets Only**

      Enter a fully qualified domain name, for example, ``www.example.com`` . You can
      optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes
      that the domain name that you specify is fully qualified. This means that Route 53 treats
      ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing
      dot) as identical.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
      the *Amazon Route 53 Developer Guide* .

      You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for
      example, ``*.example.com`` . Note the following:

      * The * must replace the entire label. For example, you can't specify
      ``*prod.example.com`` or ``prod*.example.com`` .

      * The * can't replace any of the middle labels, for example, marketing.*.example.com.

      * If you include * in any position other than the leftmost label in a domain name, DNS
      treats it as an * character (ASCII 42), not as a wildcard.

      .. warning::

         You can't use the * wildcard for resource records sets that have a type of NS.

      You can use the * wildcard as the leftmost label in a domain name, for example,
      ``*.example.com`` . You can't use an * for one of the middle labels, for example,
      ``marketing.*.example.com`` . In addition, the * must replace the entire label; for
      example, you can't specify ``prod*.example.com`` .

    - **Type** *(string) --* **[REQUIRED]**

      The DNS record type. For information about different record types and how data is encoded
      for them, see `Supported DNS Resource Record Types
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in
      the *Amazon Route 53 Developer Guide* .

      Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` |
      ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``

      Values for weighted, latency, geolocation, and failover resource record sets: ``A`` |
      ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` |
      ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource
      record sets, specify the same value for all of the resource record sets in the group.

      Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` |
      ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``

      .. note::

        SPF records were formerly used to verify the identity of the sender of email messages.
        However, we no longer recommend that you create resource record sets for which the
        value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing
        Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and
        mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly,
        its use is no longer appropriate for SPF version 1; implementations are not to use it."
        In RFC 7208, see section 14.1, `The SPF DNS Record Type
        <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

      Values for alias resource record sets:

      * **Amazon API Gateway custom regional APIs and edge-optimized APIs:**  ``A``

      * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create
      two resource record sets to route traffic to your distribution, one with a value of ``A``
      and one with a value of ``AAAA`` .

      * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``

      * **ELB load balancers:**  ``A`` | ``AAAA``

      * **Amazon S3 buckets:**  ``A``

      * **Amazon Virtual Private Cloud interface VPC endpoints**  ``A``

      * **Another resource record set in this hosted zone:** Specify the type of the resource
      record set that you're creating the alias for. All values are supported except ``NS`` and
      ``SOA`` .

      .. note::

         If you're creating an alias record that has the same name as the hosted zone (known as
         the zone apex), you can't route traffic to a record for which the value of ``Type`` is
         ``CNAME`` . This is because the alias record must have the same type as the record
         you're routing traffic to, and creating a CNAME record for the zone apex isn't
         supported even for an alias record.

    - **SetIdentifier** *(string) --*

       *Resource record sets that have a routing policy other than simple:* An identifier that
       differentiates among multiple resource record sets that have the same combination of
       name and type, such as multiple weighted resource record sets named acme.example.com
       that have a type of A. In a group of resource record sets that have the same name and
       type, the value of ``SetIdentifier`` must be unique for each resource record set.

      For information about routing policies, see `Choosing a Routing Policy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`__ in the
      *Amazon Route 53 Developer Guide* .

    - **Weight** *(integer) --*

       *Weighted resource record sets only:* Among resource record sets that have the same
       combination of DNS name and type, a value that determines the proportion of DNS queries
       that Amazon Route 53 responds to using the current resource record set. Route 53
       calculates the sum of the weights for the resource record sets that have the same
       combination of DNS name and type. Route 53 then responds to queries based on the ratio
       of a resource's weight to the total. Note the following:

      * You must specify a value for the ``Weight`` element for every weighted resource record
      set.

      * You can only specify one ``ResourceRecord`` per weighted resource record set.

      * You can't create latency, failover, or geolocation resource record sets that have the
      same values for the ``Name`` and ``Type`` elements as weighted resource record sets.

      * You can create a maximum of 100 weighted resource record sets that have the same values
      for the ``Name`` and ``Type`` elements.

      * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to
      ``0`` for a resource record set, Route 53 never responds to queries with the applicable
      value for that resource record set. However, if you set ``Weight`` to ``0`` for all
      resource record sets that have the same combination of DNS name and type, traffic is
      routed to all resources with equal probability. The effect of setting ``Weight`` to ``0``
      is different when you associate health checks with weighted resource record sets. For
      more information, see `Options for Configuring Route 53 Active-Active and Active-Passive
      Failover
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **Region** *(string) --*

       *Latency-based resource record sets only:* The Amazon EC2 Region where you created the
       resource that this resource record set refers to. The resource typically is an AWS
       resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP
       address or a DNS domain name, depending on the record type.

      .. note::

        Creating latency and latency alias resource record sets in private hosted zones is not
        supported.

      When Amazon Route 53 receives a DNS query for a domain name and type for which you have
      created latency resource record sets, Route 53 selects the latency resource record set
      that has the lowest latency between the end user and the associated Amazon EC2 Region.
      Route 53 then returns the value that is associated with the selected resource record set.

      Note the following:

      * You can only specify one ``ResourceRecord`` per latency resource record set.

      * You can only create one latency resource record set for each Amazon EC2 Region.

      * You aren't required to create latency resource record sets for all Amazon EC2 Regions.
      Route 53 will choose the region with the best latency from among the regions that you
      create latency resource record sets for.

      * You can't create non-latency resource record sets that have the same values for the
      ``Name`` and ``Type`` elements as latency resource record sets.

    - **GeoLocation** *(dict) --*

       *Geolocation resource record sets only:* A complex type that lets you control how Amazon
       Route 53 responds to DNS queries based on the geographic origin of the query. For
       example, if you want all queries from Africa to be routed to a web server with an IP
       address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a
       ``ContinentCode`` of ``AF`` .

      .. note::

        Creating geolocation and geolocation alias resource record sets in private hosted zones
        is not supported.

      If you create separate resource record sets for overlapping geographic regions (for
      example, one resource record set for a continent and one for a country on the same
      continent), priority goes to the smallest geographic region. This allows you to route
      most queries for a continent to one resource and to route queries for a country on that
      continent to a different resource.

      You can't create two geolocation resource record sets that specify the same geographic
      location.

      The value ``*`` in the ``CountryCode`` element matches all geographic locations that
      aren't specified in other geolocation resource record sets that have the same values for
      the ``Name`` and ``Type`` elements.

      .. warning::

        Geolocation works by mapping IP addresses to locations. However, some IP addresses
        aren't mapped to geographic locations, so even if you create geolocation resource
        record sets that cover all seven continents, Route 53 will receive some DNS queries
        from locations that it can't identify. We recommend that you create a resource record
        set for which the value of ``CountryCode`` is ``*`` , which handles both queries that
        come from locations for which you haven't created geolocation resource record sets and
        queries from IP addresses that aren't mapped to a location. If you don't create a ``*``
        resource record set, Route 53 returns a "no answer" response for queries from those
        locations.

      You can't create non-geolocation resource record sets that have the same values for the
      ``Name`` and ``Type`` elements as geolocation resource record sets.

      - **ContinentCode** *(string) --*

        The two-letter code for the continent.

        Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``

        Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or
        ``SubdivisionCode`` returns an ``InvalidInput`` error.

      - **CountryCode** *(string) --*

        The two-letter code for the country.

      - **SubdivisionCode** *(string) --*

        The code for the subdivision. Route 53 currently supports only states in the United
        States.

    - **Failover** *(string) --*

       *Failover resource record sets only:* To configure failover, you add the ``Failover``
       element to two resource record sets. For one resource record set, you specify
       ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you
       specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and
       specify the health check that you want Amazon Route 53 to perform for each resource
       record set.

      Except where noted, the following failover behaviors assume that you have included the
      ``HealthCheckId`` element in both resource record sets:

      * When the primary resource record set is healthy, Route 53 responds to DNS queries with
      the applicable value from the primary resource record set regardless of the health of the
      secondary resource record set.

      * When the primary resource record set is unhealthy and the secondary resource record set
      is healthy, Route 53 responds to DNS queries with the applicable value from the secondary
      resource record set.

      * When the secondary resource record set is unhealthy, Route 53 responds to DNS queries
      with the applicable value from the primary resource record set regardless of the health
      of the primary resource record set.

      * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if
      the primary resource record set is unhealthy, Route 53 always responds to DNS queries
      with the applicable value from the secondary resource record set. This is true regardless
      of the health of the associated endpoint.

      You can't create non-failover resource record sets that have the same values for the
      ``Name`` and ``Type`` elements as failover resource record sets.

      For failover alias resource record sets, you must also include the
      ``EvaluateTargetHealth`` element and set the value to true.

      For more information about configuring failover for Route 53, see the following topics in
      the *Amazon Route 53 Developer Guide* :

      * `Route 53 Health Checks and DNS Failover
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__

      * `Configuring Failover in a Private Hosted Zone
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__
    """


_ClientChangeResourceRecordSetsChangeBatchChangesTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsChangeBatchChangesTypeDef",
    {
        "Action": str,
        "ResourceRecordSet": ClientChangeResourceRecordSetsChangeBatchChangesResourceRecordSetTypeDef,
    },
)


class ClientChangeResourceRecordSetsChangeBatchChangesTypeDef(
    _ClientChangeResourceRecordSetsChangeBatchChangesTypeDef
):
    """
    Type definition for `ClientChangeResourceRecordSetsChangeBatch` `Changes`

    The information for each resource record set that you want to change.

    - **Action** *(string) --* **[REQUIRED]**

      The action to perform:

      * ``CREATE`` : Creates a resource record set that has the specified values.

      * ``DELETE`` : Deletes a existing resource record set.

      .. warning::

         To delete the resource record set that is associated with a traffic policy instance, use
         `DeleteTrafficPolicyInstance
         <https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html>`__
         . Amazon Route 53 will delete the resource record set automatically. If you delete the
         resource record set by using ``ChangeResourceRecordSets`` , Route 53 doesn't
         automatically delete the traffic policy instance, and you'll continue to be charged for
         it even though it's no longer in use.

      * ``UPSERT`` : If a resource record set doesn't already exist, Route 53 creates it. If a
      resource record set does exist, Route 53 updates it with the values in the request.

    - **ResourceRecordSet** *(dict) --* **[REQUIRED]**

      Information about the resource record set to create, delete, or update.

      - **Name** *(string) --* **[REQUIRED]**

        For ``ChangeResourceRecordSets`` requests, the name of the record that you want to
        create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record
        in the specified hosted zone.

         **ChangeResourceRecordSets Only**

        Enter a fully qualified domain name, for example, ``www.example.com`` . You can
        optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes
        that the domain name that you specify is fully qualified. This means that Route 53 treats
        ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing
        dot) as identical.

        For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
        (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
        the *Amazon Route 53 Developer Guide* .

        You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for
        example, ``*.example.com`` . Note the following:

        * The * must replace the entire label. For example, you can't specify
        ``*prod.example.com`` or ``prod*.example.com`` .

        * The * can't replace any of the middle labels, for example, marketing.*.example.com.

        * If you include * in any position other than the leftmost label in a domain name, DNS
        treats it as an * character (ASCII 42), not as a wildcard.

        .. warning::

           You can't use the * wildcard for resource records sets that have a type of NS.

        You can use the * wildcard as the leftmost label in a domain name, for example,
        ``*.example.com`` . You can't use an * for one of the middle labels, for example,
        ``marketing.*.example.com`` . In addition, the * must replace the entire label; for
        example, you can't specify ``prod*.example.com`` .

      - **Type** *(string) --* **[REQUIRED]**

        The DNS record type. For information about different record types and how data is encoded
        for them, see `Supported DNS Resource Record Types
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in
        the *Amazon Route 53 Developer Guide* .

        Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` |
        ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``

        Values for weighted, latency, geolocation, and failover resource record sets: ``A`` |
        ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` |
        ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource
        record sets, specify the same value for all of the resource record sets in the group.

        Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` |
        ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``

        .. note::

          SPF records were formerly used to verify the identity of the sender of email messages.
          However, we no longer recommend that you create resource record sets for which the
          value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing
          Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and
          mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly,
          its use is no longer appropriate for SPF version 1; implementations are not to use it."
          In RFC 7208, see section 14.1, `The SPF DNS Record Type
          <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

        Values for alias resource record sets:

        * **Amazon API Gateway custom regional APIs and edge-optimized APIs:**  ``A``

        * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create
        two resource record sets to route traffic to your distribution, one with a value of ``A``
        and one with a value of ``AAAA`` .

        * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``

        * **ELB load balancers:**  ``A`` | ``AAAA``

        * **Amazon S3 buckets:**  ``A``

        * **Amazon Virtual Private Cloud interface VPC endpoints**  ``A``

        * **Another resource record set in this hosted zone:** Specify the type of the resource
        record set that you're creating the alias for. All values are supported except ``NS`` and
        ``SOA`` .

        .. note::

           If you're creating an alias record that has the same name as the hosted zone (known as
           the zone apex), you can't route traffic to a record for which the value of ``Type`` is
           ``CNAME`` . This is because the alias record must have the same type as the record
           you're routing traffic to, and creating a CNAME record for the zone apex isn't
           supported even for an alias record.

      - **SetIdentifier** *(string) --*

         *Resource record sets that have a routing policy other than simple:* An identifier that
         differentiates among multiple resource record sets that have the same combination of
         name and type, such as multiple weighted resource record sets named acme.example.com
         that have a type of A. In a group of resource record sets that have the same name and
         type, the value of ``SetIdentifier`` must be unique for each resource record set.

        For information about routing policies, see `Choosing a Routing Policy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`__ in the
        *Amazon Route 53 Developer Guide* .

      - **Weight** *(integer) --*

         *Weighted resource record sets only:* Among resource record sets that have the same
         combination of DNS name and type, a value that determines the proportion of DNS queries
         that Amazon Route 53 responds to using the current resource record set. Route 53
         calculates the sum of the weights for the resource record sets that have the same
         combination of DNS name and type. Route 53 then responds to queries based on the ratio
         of a resource's weight to the total. Note the following:

        * You must specify a value for the ``Weight`` element for every weighted resource record
        set.

        * You can only specify one ``ResourceRecord`` per weighted resource record set.

        * You can't create latency, failover, or geolocation resource record sets that have the
        same values for the ``Name`` and ``Type`` elements as weighted resource record sets.

        * You can create a maximum of 100 weighted resource record sets that have the same values
        for the ``Name`` and ``Type`` elements.

        * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to
        ``0`` for a resource record set, Route 53 never responds to queries with the applicable
        value for that resource record set. However, if you set ``Weight`` to ``0`` for all
        resource record sets that have the same combination of DNS name and type, traffic is
        routed to all resources with equal probability. The effect of setting ``Weight`` to ``0``
        is different when you associate health checks with weighted resource record sets. For
        more information, see `Options for Configuring Route 53 Active-Active and Active-Passive
        Failover
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **Region** *(string) --*

         *Latency-based resource record sets only:* The Amazon EC2 Region where you created the
         resource that this resource record set refers to. The resource typically is an AWS
         resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP
         address or a DNS domain name, depending on the record type.

        .. note::

          Creating latency and latency alias resource record sets in private hosted zones is not
          supported.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have
        created latency resource record sets, Route 53 selects the latency resource record set
        that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        Note the following:

        * You can only specify one ``ResourceRecord`` per latency resource record set.

        * You can only create one latency resource record set for each Amazon EC2 Region.

        * You aren't required to create latency resource record sets for all Amazon EC2 Regions.
        Route 53 will choose the region with the best latency from among the regions that you
        create latency resource record sets for.

        * You can't create non-latency resource record sets that have the same values for the
        ``Name`` and ``Type`` elements as latency resource record sets.

      - **GeoLocation** *(dict) --*

         *Geolocation resource record sets only:* A complex type that lets you control how Amazon
         Route 53 responds to DNS queries based on the geographic origin of the query. For
         example, if you want all queries from Africa to be routed to a web server with an IP
         address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a
         ``ContinentCode`` of ``AF`` .

        .. note::

          Creating geolocation and geolocation alias resource record sets in private hosted zones
          is not supported.

        If you create separate resource record sets for overlapping geographic regions (for
        example, one resource record set for a continent and one for a country on the same
        continent), priority goes to the smallest geographic region. This allows you to route
        most queries for a continent to one resource and to route queries for a country on that
        continent to a different resource.

        You can't create two geolocation resource record sets that specify the same geographic
        location.

        The value ``*`` in the ``CountryCode`` element matches all geographic locations that
        aren't specified in other geolocation resource record sets that have the same values for
        the ``Name`` and ``Type`` elements.

        .. warning::

          Geolocation works by mapping IP addresses to locations. However, some IP addresses
          aren't mapped to geographic locations, so even if you create geolocation resource
          record sets that cover all seven continents, Route 53 will receive some DNS queries
          from locations that it can't identify. We recommend that you create a resource record
          set for which the value of ``CountryCode`` is ``*`` , which handles both queries that
          come from locations for which you haven't created geolocation resource record sets and
          queries from IP addresses that aren't mapped to a location. If you don't create a ``*``
          resource record set, Route 53 returns a "no answer" response for queries from those
          locations.

        You can't create non-geolocation resource record sets that have the same values for the
        ``Name`` and ``Type`` elements as geolocation resource record sets.

        - **ContinentCode** *(string) --*

          The two-letter code for the continent.

          Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``

          Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or
          ``SubdivisionCode`` returns an ``InvalidInput`` error.

        - **CountryCode** *(string) --*

          The two-letter code for the country.

        - **SubdivisionCode** *(string) --*

          The code for the subdivision. Route 53 currently supports only states in the United
          States.

      - **Failover** *(string) --*

         *Failover resource record sets only:* To configure failover, you add the ``Failover``
         element to two resource record sets. For one resource record set, you specify
         ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you
         specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and
         specify the health check that you want Amazon Route 53 to perform for each resource
         record set.

        Except where noted, the following failover behaviors assume that you have included the
        ``HealthCheckId`` element in both resource record sets:

        * When the primary resource record set is healthy, Route 53 responds to DNS queries with
        the applicable value from the primary resource record set regardless of the health of the
        secondary resource record set.

        * When the primary resource record set is unhealthy and the secondary resource record set
        is healthy, Route 53 responds to DNS queries with the applicable value from the secondary
        resource record set.

        * When the secondary resource record set is unhealthy, Route 53 responds to DNS queries
        with the applicable value from the primary resource record set regardless of the health
        of the primary resource record set.

        * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if
        the primary resource record set is unhealthy, Route 53 always responds to DNS queries
        with the applicable value from the secondary resource record set. This is true regardless
        of the health of the associated endpoint.

        You can't create non-failover resource record sets that have the same values for the
        ``Name`` and ``Type`` elements as failover resource record sets.

        For failover alias resource record sets, you must also include the
        ``EvaluateTargetHealth`` element and set the value to true.

        For more information about configuring failover for Route 53, see the following topics in
        the *Amazon Route 53 Developer Guide* :

        * `Route 53 Health Checks and DNS Failover
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__

        * `Configuring Failover in a Private Hosted Zone
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__
    """


_RequiredClientChangeResourceRecordSetsChangeBatchTypeDef = TypedDict(
    "_RequiredClientChangeResourceRecordSetsChangeBatchTypeDef",
    {"Changes": List[ClientChangeResourceRecordSetsChangeBatchChangesTypeDef]},
)
_OptionalClientChangeResourceRecordSetsChangeBatchTypeDef = TypedDict(
    "_OptionalClientChangeResourceRecordSetsChangeBatchTypeDef",
    {"Comment": str},
    total=False,
)


class ClientChangeResourceRecordSetsChangeBatchTypeDef(
    _RequiredClientChangeResourceRecordSetsChangeBatchTypeDef,
    _OptionalClientChangeResourceRecordSetsChangeBatchTypeDef,
):
    """
    Type definition for `ClientChangeResourceRecordSets` `ChangeBatch`

    A complex type that contains an optional comment and the ``Changes`` element.

    - **Comment** *(string) --*

       *Optional:* Any comments you want to include about a change batch request.

    - **Changes** *(list) --* **[REQUIRED]**

      Information about the changes to make to the record sets.

      - *(dict) --*

        The information for each resource record set that you want to change.

        - **Action** *(string) --* **[REQUIRED]**

          The action to perform:

          * ``CREATE`` : Creates a resource record set that has the specified values.

          * ``DELETE`` : Deletes a existing resource record set.

          .. warning::

             To delete the resource record set that is associated with a traffic policy instance, use
             `DeleteTrafficPolicyInstance
             <https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html>`__
             . Amazon Route 53 will delete the resource record set automatically. If you delete the
             resource record set by using ``ChangeResourceRecordSets`` , Route 53 doesn't
             automatically delete the traffic policy instance, and you'll continue to be charged for
             it even though it's no longer in use.

          * ``UPSERT`` : If a resource record set doesn't already exist, Route 53 creates it. If a
          resource record set does exist, Route 53 updates it with the values in the request.

        - **ResourceRecordSet** *(dict) --* **[REQUIRED]**

          Information about the resource record set to create, delete, or update.

          - **Name** *(string) --* **[REQUIRED]**

            For ``ChangeResourceRecordSets`` requests, the name of the record that you want to
            create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record
            in the specified hosted zone.

             **ChangeResourceRecordSets Only**

            Enter a fully qualified domain name, for example, ``www.example.com`` . You can
            optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes
            that the domain name that you specify is fully qualified. This means that Route 53 treats
            ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing
            dot) as identical.

            For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
            (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
            the *Amazon Route 53 Developer Guide* .

            You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for
            example, ``*.example.com`` . Note the following:

            * The * must replace the entire label. For example, you can't specify
            ``*prod.example.com`` or ``prod*.example.com`` .

            * The * can't replace any of the middle labels, for example, marketing.*.example.com.

            * If you include * in any position other than the leftmost label in a domain name, DNS
            treats it as an * character (ASCII 42), not as a wildcard.

            .. warning::

               You can't use the * wildcard for resource records sets that have a type of NS.

            You can use the * wildcard as the leftmost label in a domain name, for example,
            ``*.example.com`` . You can't use an * for one of the middle labels, for example,
            ``marketing.*.example.com`` . In addition, the * must replace the entire label; for
            example, you can't specify ``prod*.example.com`` .

          - **Type** *(string) --* **[REQUIRED]**

            The DNS record type. For information about different record types and how data is encoded
            for them, see `Supported DNS Resource Record Types
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in
            the *Amazon Route 53 Developer Guide* .

            Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` |
            ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``

            Values for weighted, latency, geolocation, and failover resource record sets: ``A`` |
            ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` |
            ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource
            record sets, specify the same value for all of the resource record sets in the group.

            Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` |
            ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``

            .. note::

              SPF records were formerly used to verify the identity of the sender of email messages.
              However, we no longer recommend that you create resource record sets for which the
              value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing
              Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and
              mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly,
              its use is no longer appropriate for SPF version 1; implementations are not to use it."
              In RFC 7208, see section 14.1, `The SPF DNS Record Type
              <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .

            Values for alias resource record sets:

            * **Amazon API Gateway custom regional APIs and edge-optimized APIs:**  ``A``

            * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create
            two resource record sets to route traffic to your distribution, one with a value of ``A``
            and one with a value of ``AAAA`` .

            * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``

            * **ELB load balancers:**  ``A`` | ``AAAA``

            * **Amazon S3 buckets:**  ``A``

            * **Amazon Virtual Private Cloud interface VPC endpoints**  ``A``

            * **Another resource record set in this hosted zone:** Specify the type of the resource
            record set that you're creating the alias for. All values are supported except ``NS`` and
            ``SOA`` .

            .. note::

               If you're creating an alias record that has the same name as the hosted zone (known as
               the zone apex), you can't route traffic to a record for which the value of ``Type`` is
               ``CNAME`` . This is because the alias record must have the same type as the record
               you're routing traffic to, and creating a CNAME record for the zone apex isn't
               supported even for an alias record.

          - **SetIdentifier** *(string) --*

             *Resource record sets that have a routing policy other than simple:* An identifier that
             differentiates among multiple resource record sets that have the same combination of
             name and type, such as multiple weighted resource record sets named acme.example.com
             that have a type of A. In a group of resource record sets that have the same name and
             type, the value of ``SetIdentifier`` must be unique for each resource record set.

            For information about routing policies, see `Choosing a Routing Policy
            <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`__ in the
            *Amazon Route 53 Developer Guide* .

          - **Weight** *(integer) --*

             *Weighted resource record sets only:* Among resource record sets that have the same
             combination of DNS name and type, a value that determines the proportion of DNS queries
             that Amazon Route 53 responds to using the current resource record set. Route 53
             calculates the sum of the weights for the resource record sets that have the same
             combination of DNS name and type. Route 53 then responds to queries based on the ratio
             of a resource's weight to the total. Note the following:

            * You must specify a value for the ``Weight`` element for every weighted resource record
            set.

            * You can only specify one ``ResourceRecord`` per weighted resource record set.

            * You can't create latency, failover, or geolocation resource record sets that have the
            same values for the ``Name`` and ``Type`` elements as weighted resource record sets.

            * You can create a maximum of 100 weighted resource record sets that have the same values
            for the ``Name`` and ``Type`` elements.

            * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to
            ``0`` for a resource record set, Route 53 never responds to queries with the applicable
            value for that resource record set. However, if you set ``Weight`` to ``0`` for all
            resource record sets that have the same combination of DNS name and type, traffic is
            routed to all resources with equal probability. The effect of setting ``Weight`` to ``0``
            is different when you associate health checks with weighted resource record sets. For
            more information, see `Options for Configuring Route 53 Active-Active and Active-Passive
            Failover
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__
            in the *Amazon Route 53 Developer Guide* .

          - **Region** *(string) --*

             *Latency-based resource record sets only:* The Amazon EC2 Region where you created the
             resource that this resource record set refers to. The resource typically is an AWS
             resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP
             address or a DNS domain name, depending on the record type.

            .. note::

              Creating latency and latency alias resource record sets in private hosted zones is not
              supported.

            When Amazon Route 53 receives a DNS query for a domain name and type for which you have
            created latency resource record sets, Route 53 selects the latency resource record set
            that has the lowest latency between the end user and the associated Amazon EC2 Region.
            Route 53 then returns the value that is associated with the selected resource record set.

            Note the following:

            * You can only specify one ``ResourceRecord`` per latency resource record set.

            * You can only create one latency resource record set for each Amazon EC2 Region.

            * You aren't required to create latency resource record sets for all Amazon EC2 Regions.
            Route 53 will choose the region with the best latency from among the regions that you
            create latency resource record sets for.

            * You can't create non-latency resource record sets that have the same values for the
            ``Name`` and ``Type`` elements as latency resource record sets.

          - **GeoLocation** *(dict) --*

             *Geolocation resource record sets only:* A complex type that lets you control how Amazon
             Route 53 responds to DNS queries based on the geographic origin of the query. For
             example, if you want all queries from Africa to be routed to a web server with an IP
             address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a
             ``ContinentCode`` of ``AF`` .

            .. note::

              Creating geolocation and geolocation alias resource record sets in private hosted zones
              is not supported.

            If you create separate resource record sets for overlapping geographic regions (for
            example, one resource record set for a continent and one for a country on the same
            continent), priority goes to the smallest geographic region. This allows you to route
            most queries for a continent to one resource and to route queries for a country on that
            continent to a different resource.

            You can't create two geolocation resource record sets that specify the same geographic
            location.

            The value ``*`` in the ``CountryCode`` element matches all geographic locations that
            aren't specified in other geolocation resource record sets that have the same values for
            the ``Name`` and ``Type`` elements.

            .. warning::

              Geolocation works by mapping IP addresses to locations. However, some IP addresses
              aren't mapped to geographic locations, so even if you create geolocation resource
              record sets that cover all seven continents, Route 53 will receive some DNS queries
              from locations that it can't identify. We recommend that you create a resource record
              set for which the value of ``CountryCode`` is ``*`` , which handles both queries that
              come from locations for which you haven't created geolocation resource record sets and
              queries from IP addresses that aren't mapped to a location. If you don't create a ``*``
              resource record set, Route 53 returns a "no answer" response for queries from those
              locations.

            You can't create non-geolocation resource record sets that have the same values for the
            ``Name`` and ``Type`` elements as geolocation resource record sets.

            - **ContinentCode** *(string) --*

              The two-letter code for the continent.

              Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``

              Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or
              ``SubdivisionCode`` returns an ``InvalidInput`` error.

            - **CountryCode** *(string) --*

              The two-letter code for the country.

            - **SubdivisionCode** *(string) --*

              The code for the subdivision. Route 53 currently supports only states in the United
              States.

          - **Failover** *(string) --*

             *Failover resource record sets only:* To configure failover, you add the ``Failover``
             element to two resource record sets. For one resource record set, you specify
             ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you
             specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and
             specify the health check that you want Amazon Route 53 to perform for each resource
             record set.

            Except where noted, the following failover behaviors assume that you have included the
            ``HealthCheckId`` element in both resource record sets:

            * When the primary resource record set is healthy, Route 53 responds to DNS queries with
            the applicable value from the primary resource record set regardless of the health of the
            secondary resource record set.

            * When the primary resource record set is unhealthy and the secondary resource record set
            is healthy, Route 53 responds to DNS queries with the applicable value from the secondary
            resource record set.

            * When the secondary resource record set is unhealthy, Route 53 responds to DNS queries
            with the applicable value from the primary resource record set regardless of the health
            of the primary resource record set.

            * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if
            the primary resource record set is unhealthy, Route 53 always responds to DNS queries
            with the applicable value from the secondary resource record set. This is true regardless
            of the health of the associated endpoint.

            You can't create non-failover resource record sets that have the same values for the
            ``Name`` and ``Type`` elements as failover resource record sets.

            For failover alias resource record sets, you must also include the
            ``EvaluateTargetHealth`` element and set the value to true.

            For more information about configuring failover for Route 53, see the following topics in
            the *Amazon Route 53 Developer Guide* :

            * `Route 53 Health Checks and DNS Failover
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__

            * `Configuring Failover in a Private Hosted Zone
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__
    """


_ClientChangeResourceRecordSetsResponseChangeInfoTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientChangeResourceRecordSetsResponseChangeInfoTypeDef(
    _ClientChangeResourceRecordSetsResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientChangeResourceRecordSetsResponse` `ChangeInfo`

    A complex type that contains information about changes made to your hosted zone.

    This element contains an ID that you use when performing a `GetChange
    <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to get
    detailed information about the change.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "_ClientChangeResourceRecordSetsResponseTypeDef",
    {"ChangeInfo": ClientChangeResourceRecordSetsResponseChangeInfoTypeDef},
    total=False,
)


class ClientChangeResourceRecordSetsResponseTypeDef(
    _ClientChangeResourceRecordSetsResponseTypeDef
):
    """
    Type definition for `ClientChangeResourceRecordSets` `Response`

    A complex type containing the response for the request.

    - **ChangeInfo** *(dict) --*

      A complex type that contains information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to get
      detailed information about the change.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
    """


_ClientChangeTagsForResourceAddTagsTypeDef = TypedDict(
    "_ClientChangeTagsForResourceAddTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientChangeTagsForResourceAddTagsTypeDef(
    _ClientChangeTagsForResourceAddTagsTypeDef
):
    """
    Type definition for `ClientChangeTagsForResource` `AddTags`

    A complex type that contains information about a tag that you want to add or edit for the
    specified health check or hosted zone.

    - **Key** *(string) --*

      The value of ``Key`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to give
      the new tag.

      * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value`` for.

      * **Delete a key** : ``Key`` is the name of the tag you want to remove.

      * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon Route 53
      console, the list of your health checks includes a **Name** column that lets you see the name
      that you've given to each health check.

    - **Value** *(string) --*

      The value of ``Value`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want to
      give the new tag.

      * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
)


class ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
    checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --* **[REQUIRED]**

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether
      this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions
      and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to
      determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't
        supported.
    """


_RequiredClientCreateHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_RequiredClientCreateHealthCheckHealthCheckConfigTypeDef", {"Type": str}
)
_OptionalClientCreateHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_OptionalClientCreateHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ClientCreateHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ClientCreateHealthCheckHealthCheckConfigTypeDef(
    _RequiredClientCreateHealthCheckHealthCheckConfigTypeDef,
    _OptionalClientCreateHealthCheckHealthCheckConfigTypeDef,
):
    """
    Type definition for `ClientCreateHealthCheck` `HealthCheckConfig`

    A complex type that contains settings for a new health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health
      checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS request to
      resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that
      you specify in ``RequestInterval`` . Using an IP address returned by DNS, Route 53 then checks
      the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example,
      ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for
      example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as
      described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` .
      This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is in local,
      private, non-routable, or multicast ranges. For more information about IP addresses for which
      you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a
      value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --* **[REQUIRED]**

      The type of health check that you want to create, which indicates how Amazon Route 53
      determines whether an endpoint is healthy.

      .. warning::

        You can't change the value of ``Type`` after you create a health check.

      You can create the following types of health checks:

      * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
      HTTP request and waits for an HTTP status code of 200 or greater and less than 400.

      * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an
      HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

      .. warning::

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or
         later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an HTTP request and searches the first 5,120 bytes of the response body for the string
      that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53
      submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the
      string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state
      of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` ,
      the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to
      determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the
      setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or
      ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks, Route 53
      adds up the number of health checks that Route 53 health checkers consider to be healthy and
      compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health checks. The
      path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx
      when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can
      also include query string parameters, for example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes
      the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except
      TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you
      want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type``
      , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the
      ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Route
      53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the value
      of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at
      the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns,
      Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
        checks to the endpoint. If there's no resource record set with a type of A for the name that
        you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution
        failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets and you
      choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you
      create a separate health check for each endpoint. For example, create a health check for each
      HTTP server that is serving content for www.example.com. For the value of
      ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
      us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
        associate the health check with those resource record sets, health check results will be
        unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for
      ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want
      Amazon Route 53 to search for in the response body from the specified resource. If the string
      appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your endpoint
      and the time that it sends the next health check request. Each Route 53 health checker makes
      requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53
      to change the current status of the endpoint from unhealthy to healthy or vice versa. For more
      information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three health
      checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers in
      multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the
      **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for example,
      to consider a health check unhealthy when it otherwise would be considered healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's what
      happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting requests to
      your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced health
      checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the corresponding
      CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to always
      be healthy. If you configured DNS failover, Route 53 continues to route traffic to the
      corresponding resources. If you want to stop routing traffic to a resource, change the value of
      `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more information,
      see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health check that
      Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered
      healthy. To specify the child health checks that you want to associate with a ``CALCULATED``
      health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53 always
      considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element
      for each health check that you want to associate with a ``CALCULATED`` health check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to
      the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint
      to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello``
      message. If you don't enable SNI, the status of the health check will be ``SSL alert
      handshake_failure`` . A health check can also have that status for other reasons. If SNI is
      enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint
      and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field
      and possibly several more in the ``Subject Alternative Names`` field. One of the domain names
      in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` .
      If the endpoint responds to the ``client_hello`` message with a certificate that does not
      include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker
      will retry the handshake. In the second attempt, the health checker will omit
      ``FullyQualifiedDomainName`` from the ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want Amazon
      Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs checks from
      all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks, Route
      53 will briefly continue to perform checks from that region to ensure that some health checkers
      are always checking the endpoint (for example, if you replace three regions with four different
      regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
      checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --* **[REQUIRED]**

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether
        this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions
        and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --* **[REQUIRED]**

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to
        determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't
          supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state, the status
      that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time that
      CloudWatch had sufficient data to determine the alarm state. For new health checks that have no
      last known status, the default status for the health check is healthy.
    """


_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfiguration` `Dimensions`

    For the metric that the CloudWatch alarm is associated with, a complex type that
    contains information about one dimension.

    - **Name** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the name of one
      dimension.

    - **Value** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the value of one
      dimension.
    """


_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "Dimensions": List[
            ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponseHealthCheck` `CloudWatchAlarmConfiguration`

    A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
    monitoring for this health check.

    - **EvaluationPeriods** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the number of periods that
      the metric is compared to the threshold.

    - **Threshold** *(float) --*

      For the metric that the CloudWatch alarm is associated with, the value the metric is
      compared with.

    - **ComparisonOperator** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the arithmetic operation
      that is used for the comparison.

    - **Period** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the duration of one
      evaluation period in seconds.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that the alarm is associated with.

    - **Namespace** *(string) --*

      The namespace of the metric that the alarm is associated with. For more information, see
      `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

    - **Statistic** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the statistic that is
      applied to the metric.

    - **Dimensions** *(list) --*

      For the metric that the CloudWatch alarm is associated with, a complex type that contains
      information about the dimensions for the metric. For information, see `Amazon CloudWatch
      Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

      - *(dict) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about one dimension.

        - **Name** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the name of one
          dimension.

        - **Value** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the value of one
          dimension.
    """


_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponseHealthCheckHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
    checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --*

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine
      whether this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
      Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --*

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
      to determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
        aren't supported.
    """


_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": str,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponseHealthCheck` `HealthCheckConfig`

    A complex type that contains detailed information about one health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
      health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
      request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
      the interval that you specify in ``RequestInterval`` . Using an IP address returned by
      DNS, Route 53 then checks the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
      example, ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
      for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
      addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
      . This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is in
      local, private, non-routable, or multicast ranges. For more information about IP
      addresses for which you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
      ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.
      Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Amazon Route 53
      determines whether an endpoint is healthy.

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

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
         v1.0 or later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
      53 submits an HTTP request and searches the first 5,120 bytes of the response body for
      the string that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
      body for the string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
      state of the alarm is ``OK`` , the health check is considered healthy. If the state is
      ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
      sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
      status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
      ``Unhealthy`` , or ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks,
      Route 53 adds up the number of health checks that Route 53 health checkers consider to be
      healthy and compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health checks.
      The path can be any value for which your endpoint will return an HTTP status code of 2xx
      or 3xx when the endpoint is healthy, for example, the file
      /docs/route53-health-check.html. You can also include query string parameters, for
      example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
      passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
      checks except TCP health checks. This is typically the fully qualified DNS name of the
      endpoint on which you want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
      header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
      Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
      value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for
      ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
      Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
        checks to the endpoint. If there's no resource record set with a type of A for the name
        that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
        resolution failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets
      and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
      recommend that you create a separate health check for each endpoint. For example, create
      a health check for each HTTP server that is serving content for www.example.com. For the
      value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
      us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
        associate the health check with those resource record sets, health check results will
        be unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
      for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
      ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
      want Amazon Route 53 to search for in the response body from the specified resource. If
      the string appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your
      endpoint and the time that it sends the next health check request. Each Route 53 health
      checker makes requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30``
      seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon
      Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
      versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
      Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three health
      checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers
      in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
      the **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for
      example, to consider a health check unhealthy when it otherwise would be considered
      healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's
      what happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting
      requests to your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
      health checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
      corresponding CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to
      always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
      the corresponding resources. If you want to stop routing traffic to a resource, change
      the value of `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more
      information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health check
      that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
      considered healthy. To specify the child health checks that you want to associate with a
      ``CALCULATED`` health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53 always
      considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
      element for each health check that you want to associate with a ``CALCULATED`` health
      check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of
      ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
      negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
      the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the
      ``client_hello`` message. If you don't enable SNI, the status of the health check will be
      ``SSL alert handshake_failure`` . A health check can also have that status for other
      reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
      configuration on your endpoint and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
      field and possibly several more in the ``Subject Alternative Names`` field. One of the
      domain names in the certificate should match the value that you specify for
      ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
      with a certificate that does not include the domain name that you specified in
      ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
      attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
      ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want
      Amazon Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs checks
      from all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks,
      Route 53 will briefly continue to perform checks from that region to ensure that some
      health checkers are always checking the endpoint (for example, if you replace three
      regions with four different regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
      checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --*

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine
        whether this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
        Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --*

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
        to determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
          aren't supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state, the
      status that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
      that CloudWatch had sufficient data to determine the alarm state. For new health checks
      that have no last known status, the default status for the health check is healthy.
    """


_ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponseHealthCheck` `LinkedService`

    If the health check was created by another service, the service that created the health
    check. When a health check is created by another service, you can't edit or delete it using
    Amazon Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientCreateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientCreateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientCreateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientCreateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateHealthCheckResponseHealthCheckTypeDef(
    _ClientCreateHealthCheckResponseHealthCheckTypeDef
):
    """
    Type definition for `ClientCreateHealthCheckResponse` `HealthCheck`

    A complex type that contains identifying information about the health check.

    - **Id** *(string) --*

      The identifier that Amazon Route 53assigned to the health check when you created it. When
      you add or update a resource record set, you use this value to specify which health check
      to use. The value can be up to 64 characters long.

    - **CallerReference** *(string) --*

      A unique string that you specified when you created the health check.

    - **LinkedService** *(dict) --*

      If the health check was created by another service, the service that created the health
      check. When a health check is created by another service, you can't edit or delete it using
      Amazon Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.

    - **HealthCheckConfig** *(dict) --*

      A complex type that contains detailed information about one health check.

      - **IPAddress** *(string) --*

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
        health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
        request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
        the interval that you specify in ``RequestInterval`` . Using an IP address returned by
        DNS, Route 53 then checks the health of the endpoint.

        Use one of the following formats for the value of ``IPAddress`` :

        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
        example, ``192.0.2.44`` .

        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
        for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
        addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
        associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
        . This ensures that the IP address of your instance will never change.

        For more information, see `FullyQualifiedDomainName
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
        .

        Constraints: Route 53 can't check the health of endpoints for which the IP address is in
        local, private, non-routable, or multicast ranges. For more information about IP
        addresses for which you can't create health checks, see the following documents:

        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
        <https://tools.ietf.org/html/rfc6598>`__

        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
        ``IPAddress`` .

      - **Port** *(integer) --*

        The port on the endpoint on which you want Amazon Route 53 to perform health checks.
        Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Amazon Route 53
        determines whether an endpoint is healthy.

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

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
           v1.0 or later.

        * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
        53 submits an HTTP request and searches the first 5,120 bytes of the response body for
        the string that you specify in ``SearchString`` .

        * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
        body for the string that you specify in ``SearchString`` .

        * **TCP** : Route 53 tries to establish a TCP connection.

        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
        state of the alarm is ``OK`` , the health check is considered healthy. If the state is
        ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
        sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
        status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
        ``Unhealthy`` , or ``LastKnownStatus`` .

        * **CALCULATED** : For health checks that monitor the status of other health checks,
        Route 53 adds up the number of health checks that Route 53 health checkers consider to be
        healthy and compares that number with the value of ``HealthThreshold`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path, if any, that you want Amazon Route 53 to request when performing health checks.
        The path can be any value for which your endpoint will return an HTTP status code of 2xx
        or 3xx when the endpoint is healthy, for example, the file
        /docs/route53-health-check.html. You can also include query string parameters, for
        example, ``/welcome.html?language=jp&login=y`` .

      - **FullyQualifiedDomainName** *(string) --*

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         **If you specify a value for**  ``IPAddress`` :

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
        passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
        checks except TCP health checks. This is typically the fully qualified DNS name of the
        endpoint on which you want Route 53 to perform health checks.

        When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
        header:

        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the Host header.

        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the ``Host`` header.

        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
        Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

        If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
        value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         **If you don't specify a value for ``IPAddress`` ** :

        Route 53 sends a DNS request to the domain that you specify for
        ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
        Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

        .. note::

          If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
          checks to the endpoint. If there's no resource record set with a type of A for the name
          that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
          resolution failed" error.

        If you want to check the health of weighted, latency, or failover resource record sets
        and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
        recommend that you create a separate health check for each endpoint. For example, create
        a health check for each HTTP server that is serving content for www.example.com. For the
        value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
        us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

        .. warning::

          In this configuration, if you create a health check for which the value of
          ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
          associate the health check with those resource record sets, health check results will
          be unpredictable.

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
        ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
        ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
        for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
        ``Host`` header.

      - **SearchString** *(string) --*

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
        want Amazon Route 53 to search for in the response body from the specified resource. If
        the string appears in the response body, Route 53 considers the resource healthy.

        Route 53 considers case when searching for ``SearchString`` in the response body.

      - **RequestInterval** *(integer) --*

        The number of seconds between the time that Amazon Route 53 gets a response from your
        endpoint and the time that it sends the next health check request. Each Route 53 health
        checker makes requests at this interval.

        .. warning::

          You can't change the value of ``RequestInterval`` after you create a health check.

        If you don't specify a value for ``RequestInterval`` , the default value is ``30``
        seconds.

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Amazon
        Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
        versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
        Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

        If you don't specify a value for ``FailureThreshold`` , the default value is three health
        checks.

      - **MeasureLatency** *(boolean) --*

        Specify whether you want Amazon Route 53 to measure the latency between health checkers
        in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
        the **Health Checks** page in the Route 53 console.

        .. warning::

          You can't change the value of ``MeasureLatency`` after you create a health check.

      - **Inverted** *(boolean) --*

        Specify whether you want Amazon Route 53 to invert the status of a health check, for
        example, to consider a health check unhealthy when it otherwise would be considered
        healthy.

      - **Disabled** *(boolean) --*

        Stops Route 53 from performing health checks. When you disable a health check, here's
        what happens:

        * **Health checks that check the health of endpoints:** Route 53 stops submitting
        requests to your application, server, or other resource.

        * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
        health checks.

        * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
        corresponding CloudWatch metrics.

        After you disable a health check, Route 53 considers the status of the health check to
        always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
        the corresponding resources. If you want to stop routing traffic to a resource, change
        the value of `Inverted
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
        .

        Charges for a health check still apply when the health check is disabled. For more
        information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

      - **HealthThreshold** *(integer) --*

        The number of child health checks that are associated with a ``CALCULATED`` health check
        that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
        considered healthy. To specify the child health checks that you want to associate with a
        ``CALCULATED`` health check, use the `ChildHealthChecks
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
        element.

        Note the following:

        * If you specify a number greater than the number of child health checks, Route 53 always
        considers this health check to be unhealthy.

        * If you specify ``0`` , Route 53 always considers this health check to be healthy.

      - **ChildHealthChecks** *(list) --*

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
        element for each health check that you want to associate with a ``CALCULATED`` health
        check.

        - *(string) --*

      - **EnableSNI** *(boolean) --*

        Specify whether you want Amazon Route 53 to send the value of
        ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
        negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
        the applicable SSL/TLS certificate.

        Some endpoints require that ``HTTPS`` requests include the host name in the
        ``client_hello`` message. If you don't enable SNI, the status of the health check will be
        ``SSL alert handshake_failure`` . A health check can also have that status for other
        reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
        configuration on your endpoint and confirm that your certificate is valid.

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
        field and possibly several more in the ``Subject Alternative Names`` field. One of the
        domain names in the certificate should match the value that you specify for
        ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
        with a certificate that does not include the domain name that you specified in
        ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
        attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
        ``client_hello`` message.

      - **Regions** *(list) --*

        A complex type that contains one ``Region`` element for each region from which you want
        Amazon Route 53 health checkers to check the specified endpoint.

        If you don't specify any regions, Route 53 health checkers automatically performs checks
        from all of the regions that are listed under **Valid Values** .

        If you update a health check to remove a region that has been performing health checks,
        Route 53 will briefly continue to perform checks from that region to ensure that some
        health checkers are always checking the endpoint (for example, if you replace three
        regions with four different regions).

        - *(string) --*

      - **AlarmIdentifier** *(dict) --*

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
        checkers to use to determine whether the specified health check is healthy.

        - **Region** *(string) --*

          For the CloudWatch alarm that you want Route 53 health checkers to use to determine
          whether this health check is healthy, the region that the alarm was created in.

          For the current list of CloudWatch regions, see `Amazon CloudWatch
          <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
          Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        - **Name** *(string) --*

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
          to determine whether this health check is healthy.

          .. note::

            Route 53 supports CloudWatch alarms with the following features:

            * Standard-resolution metrics. High-resolution metrics aren't supported. For more
            information, see `High-Resolution Metrics
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
            in the *Amazon CloudWatch User Guide* .

            * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
            aren't supported.

      - **InsufficientDataHealthStatus** *(string) --*

        When CloudWatch has insufficient data about the metric to determine the alarm state, the
        status that you want Amazon Route 53 to assign to the health check:

        * ``Healthy`` : Route 53 considers the health check to be healthy.

        * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

        * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
        that CloudWatch had sufficient data to determine the alarm state. For new health checks
        that have no last known status, the default status for the health check is healthy.

    - **HealthCheckVersion** *(integer) --*

      The version of the health check. You can optionally pass this value in a call to
      ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

    - **CloudWatchAlarmConfiguration** *(dict) --*

      A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
      monitoring for this health check.

      - **EvaluationPeriods** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the number of periods that
        the metric is compared to the threshold.

      - **Threshold** *(float) --*

        For the metric that the CloudWatch alarm is associated with, the value the metric is
        compared with.

      - **ComparisonOperator** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the arithmetic operation
        that is used for the comparison.

      - **Period** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the duration of one
        evaluation period in seconds.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that the alarm is associated with.

      - **Namespace** *(string) --*

        The namespace of the metric that the alarm is associated with. For more information, see
        `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

      - **Statistic** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the statistic that is
        applied to the metric.

      - **Dimensions** *(list) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that contains
        information about the dimensions for the metric. For information, see `Amazon CloudWatch
        Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        - *(dict) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that
          contains information about one dimension.

          - **Name** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the name of one
            dimension.

          - **Value** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the value of one
            dimension.
    """


_ClientCreateHealthCheckResponseTypeDef = TypedDict(
    "_ClientCreateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientCreateHealthCheckResponseHealthCheckTypeDef, "Location": str},
    total=False,
)


class ClientCreateHealthCheckResponseTypeDef(_ClientCreateHealthCheckResponseTypeDef):
    """
    Type definition for `ClientCreateHealthCheck` `Response`

    A complex type containing the response information for the new health check.

    - **HealthCheck** *(dict) --*

      A complex type that contains identifying information about the health check.

      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check
        to use. The value can be up to 64 characters long.

      - **CallerReference** *(string) --*

        A unique string that you specified when you created the health check.

      - **LinkedService** *(dict) --*

        If the health check was created by another service, the service that created the health
        check. When a health check is created by another service, you can't edit or delete it using
        Amazon Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.

      - **HealthCheckConfig** *(dict) --*

        A complex type that contains detailed information about one health check.

        - **IPAddress** *(string) --*

          The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
          health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
          request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
          the interval that you specify in ``RequestInterval`` . Using an IP address returned by
          DNS, Route 53 then checks the health of the endpoint.

          Use one of the following formats for the value of ``IPAddress`` :

          * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
          example, ``192.0.2.44`` .

          * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
          for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
          addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

          If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
          associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
          . This ensures that the IP address of your instance will never change.

          For more information, see `FullyQualifiedDomainName
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
          .

          Constraints: Route 53 can't check the health of endpoints for which the IP address is in
          local, private, non-routable, or multicast ranges. For more information about IP
          addresses for which you can't create health checks, see the following documents:

          * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

          * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
          <https://tools.ietf.org/html/rfc6598>`__

          * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

          When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
          ``IPAddress`` .

        - **Port** *(integer) --*

          The port on the endpoint on which you want Amazon Route 53 to perform health checks.
          Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

        - **Type** *(string) --*

          The type of health check that you want to create, which indicates how Amazon Route 53
          determines whether an endpoint is healthy.

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

             If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
             v1.0 or later.

          * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
          53 submits an HTTP request and searches the first 5,120 bytes of the response body for
          the string that you specify in ``SearchString`` .

          * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
          Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
          body for the string that you specify in ``SearchString`` .

          * **TCP** : Route 53 tries to establish a TCP connection.

          * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
          state of the alarm is ``OK`` , the health check is considered healthy. If the state is
          ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
          sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
          status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
          ``Unhealthy`` , or ``LastKnownStatus`` .

          * **CALCULATED** : For health checks that monitor the status of other health checks,
          Route 53 adds up the number of health checks that Route 53 health checkers consider to be
          healthy and compares that number with the value of ``HealthThreshold`` .

          For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

        - **ResourcePath** *(string) --*

          The path, if any, that you want Amazon Route 53 to request when performing health checks.
          The path can be any value for which your endpoint will return an HTTP status code of 2xx
          or 3xx when the endpoint is healthy, for example, the file
          /docs/route53-health-check.html. You can also include query string parameters, for
          example, ``/welcome.html?language=jp&login=y`` .

        - **FullyQualifiedDomainName** *(string) --*

          Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

           **If you specify a value for**  ``IPAddress`` :

          Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
          passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
          checks except TCP health checks. This is typically the fully qualified DNS name of the
          endpoint on which you want Route 53 to perform health checks.

          When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
          header:

          * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the Host header.

          * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the ``Host`` header.

          * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
          Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

          If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
          value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

           **If you don't specify a value for ``IPAddress`` ** :

          Route 53 sends a DNS request to the domain that you specify for
          ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
          Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

          .. note::

            If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
            checks to the endpoint. If there's no resource record set with a type of A for the name
            that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
            resolution failed" error.

          If you want to check the health of weighted, latency, or failover resource record sets
          and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
          recommend that you create a separate health check for each endpoint. For example, create
          a health check for each HTTP server that is serving content for www.example.com. For the
          value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
          us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

          .. warning::

            In this configuration, if you create a health check for which the value of
            ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
            associate the health check with those resource record sets, health check results will
            be unpredictable.

          In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
          ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
          ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
          for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
          ``Host`` header.

        - **SearchString** *(string) --*

          If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
          want Amazon Route 53 to search for in the response body from the specified resource. If
          the string appears in the response body, Route 53 considers the resource healthy.

          Route 53 considers case when searching for ``SearchString`` in the response body.

        - **RequestInterval** *(integer) --*

          The number of seconds between the time that Amazon Route 53 gets a response from your
          endpoint and the time that it sends the next health check request. Each Route 53 health
          checker makes requests at this interval.

          .. warning::

            You can't change the value of ``RequestInterval`` after you create a health check.

          If you don't specify a value for ``RequestInterval`` , the default value is ``30``
          seconds.

        - **FailureThreshold** *(integer) --*

          The number of consecutive health checks that an endpoint must pass or fail for Amazon
          Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
          versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
          Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

          If you don't specify a value for ``FailureThreshold`` , the default value is three health
          checks.

        - **MeasureLatency** *(boolean) --*

          Specify whether you want Amazon Route 53 to measure the latency between health checkers
          in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
          the **Health Checks** page in the Route 53 console.

          .. warning::

            You can't change the value of ``MeasureLatency`` after you create a health check.

        - **Inverted** *(boolean) --*

          Specify whether you want Amazon Route 53 to invert the status of a health check, for
          example, to consider a health check unhealthy when it otherwise would be considered
          healthy.

        - **Disabled** *(boolean) --*

          Stops Route 53 from performing health checks. When you disable a health check, here's
          what happens:

          * **Health checks that check the health of endpoints:** Route 53 stops submitting
          requests to your application, server, or other resource.

          * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
          health checks.

          * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
          corresponding CloudWatch metrics.

          After you disable a health check, Route 53 considers the status of the health check to
          always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
          the corresponding resources. If you want to stop routing traffic to a resource, change
          the value of `Inverted
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
          .

          Charges for a health check still apply when the health check is disabled. For more
          information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

        - **HealthThreshold** *(integer) --*

          The number of child health checks that are associated with a ``CALCULATED`` health check
          that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
          considered healthy. To specify the child health checks that you want to associate with a
          ``CALCULATED`` health check, use the `ChildHealthChecks
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
          element.

          Note the following:

          * If you specify a number greater than the number of child health checks, Route 53 always
          considers this health check to be unhealthy.

          * If you specify ``0`` , Route 53 always considers this health check to be healthy.

        - **ChildHealthChecks** *(list) --*

          (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
          element for each health check that you want to associate with a ``CALCULATED`` health
          check.

          - *(string) --*

        - **EnableSNI** *(boolean) --*

          Specify whether you want Amazon Route 53 to send the value of
          ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
          negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
          the applicable SSL/TLS certificate.

          Some endpoints require that ``HTTPS`` requests include the host name in the
          ``client_hello`` message. If you don't enable SNI, the status of the health check will be
          ``SSL alert handshake_failure`` . A health check can also have that status for other
          reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
          configuration on your endpoint and confirm that your certificate is valid.

          The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
          field and possibly several more in the ``Subject Alternative Names`` field. One of the
          domain names in the certificate should match the value that you specify for
          ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
          with a certificate that does not include the domain name that you specified in
          ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
          attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
          ``client_hello`` message.

        - **Regions** *(list) --*

          A complex type that contains one ``Region`` element for each region from which you want
          Amazon Route 53 health checkers to check the specified endpoint.

          If you don't specify any regions, Route 53 health checkers automatically performs checks
          from all of the regions that are listed under **Valid Values** .

          If you update a health check to remove a region that has been performing health checks,
          Route 53 will briefly continue to perform checks from that region to ensure that some
          health checkers are always checking the endpoint (for example, if you replace three
          regions with four different regions).

          - *(string) --*

        - **AlarmIdentifier** *(dict) --*

          A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
          checkers to use to determine whether the specified health check is healthy.

          - **Region** *(string) --*

            For the CloudWatch alarm that you want Route 53 health checkers to use to determine
            whether this health check is healthy, the region that the alarm was created in.

            For the current list of CloudWatch regions, see `Amazon CloudWatch
            <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
            Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

          - **Name** *(string) --*

            The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
            to determine whether this health check is healthy.

            .. note::

              Route 53 supports CloudWatch alarms with the following features:

              * Standard-resolution metrics. High-resolution metrics aren't supported. For more
              information, see `High-Resolution Metrics
              <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
              in the *Amazon CloudWatch User Guide* .

              * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
              aren't supported.

        - **InsufficientDataHealthStatus** *(string) --*

          When CloudWatch has insufficient data about the metric to determine the alarm state, the
          status that you want Amazon Route 53 to assign to the health check:

          * ``Healthy`` : Route 53 considers the health check to be healthy.

          * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

          * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
          that CloudWatch had sufficient data to determine the alarm state. For new health checks
          that have no last known status, the default status for the health check is healthy.

      - **HealthCheckVersion** *(integer) --*

        The version of the health check. You can optionally pass this value in a call to
        ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

      - **CloudWatchAlarmConfiguration** *(dict) --*

        A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
        monitoring for this health check.

        - **EvaluationPeriods** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the number of periods that
          the metric is compared to the threshold.

        - **Threshold** *(float) --*

          For the metric that the CloudWatch alarm is associated with, the value the metric is
          compared with.

        - **ComparisonOperator** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the arithmetic operation
          that is used for the comparison.

        - **Period** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the duration of one
          evaluation period in seconds.

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that the alarm is associated with.

        - **Namespace** *(string) --*

          The namespace of the metric that the alarm is associated with. For more information, see
          `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

        - **Statistic** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the statistic that is
          applied to the metric.

        - **Dimensions** *(list) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that contains
          information about the dimensions for the metric. For information, see `Amazon CloudWatch
          Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

          - *(dict) --*

            For the metric that the CloudWatch alarm is associated with, a complex type that
            contains information about one dimension.

            - **Name** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the name of one
              dimension.

            - **Value** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the value of one
              dimension.

    - **Location** *(string) --*

      The unique URL representing the new health check.
    """


_ClientCreateHostedZoneHostedZoneConfigTypeDef = TypedDict(
    "_ClientCreateHostedZoneHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientCreateHostedZoneHostedZoneConfigTypeDef(
    _ClientCreateHostedZoneHostedZoneConfigTypeDef
):
    """
    Type definition for `ClientCreateHostedZone` `HostedZoneConfig`

    (Optional) A complex type that contains the following optional values:

    * For public and private hosted zones, an optional comment

    * For private hosted zones, an optional ``PrivateZone`` element

    If you don't specify a comment or the ``PrivateZone`` element, omit ``HostedZoneConfig`` and the
    other elements.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientCreateHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientCreateHostedZoneResponseChangeInfoTypeDef(
    _ClientCreateHostedZoneResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponse` `ChangeInfo`

    A complex type that contains information about the ``CreateHostedZone`` request.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientCreateHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientCreateHostedZoneResponseDelegationSetTypeDef(
    _ClientCreateHostedZoneResponseDelegationSetTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponse` `DelegationSet`

    A complex type that describes the name servers for this hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigns to a reusable delegation set.

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the reusable
      delegation set.

    - **NameServers** *(list) --*

      A complex type that contains a list of the authoritative name servers for a hosted zone or
      for a reusable delegation set.

      - *(string) --*
    """


_ClientCreateHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneConfigTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneConfigTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponseHostedZone` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponseHostedZone` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientCreateHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientCreateHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientCreateHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientCreateHostedZoneResponseHostedZoneTypeDef(
    _ClientCreateHostedZoneResponseHostedZoneTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponse` `HostedZone`

    A complex type that contains general information about the hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have registered
      with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientCreateHostedZoneResponseVPCTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientCreateHostedZoneResponseVPCTypeDef(
    _ClientCreateHostedZoneResponseVPCTypeDef
):
    """
    Type definition for `ClientCreateHostedZoneResponse` `VPC`

    A complex type that contains information about an Amazon VPC that you associated with this
    hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientCreateHostedZoneResponseTypeDef = TypedDict(
    "_ClientCreateHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientCreateHostedZoneResponseHostedZoneTypeDef,
        "ChangeInfo": ClientCreateHostedZoneResponseChangeInfoTypeDef,
        "DelegationSet": ClientCreateHostedZoneResponseDelegationSetTypeDef,
        "VPC": ClientCreateHostedZoneResponseVPCTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateHostedZoneResponseTypeDef(_ClientCreateHostedZoneResponseTypeDef):
    """
    Type definition for `ClientCreateHostedZone` `Response`

    A complex type containing the response information for the hosted zone.

    - **HostedZone** *(dict) --*

      A complex type that contains general information about the hosted zone.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.

      - **Name** *(string) --*

        The name of the domain. For public hosted zones, this is the name that you have registered
        with your DNS registrar.

        For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
        (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the hosted zone.

      - **Config** *(dict) --*

        A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
        the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
        ``Comment`` elements don't appear in the response.

        - **Comment** *(string) --*

          Any comments that you want to include about the hosted zone.

        - **PrivateZone** *(boolean) --*

          A value that indicates whether this is a private hosted zone.

      - **ResourceRecordSetCount** *(integer) --*

        The number of resource record sets in the hosted zone.

      - **LinkedService** *(dict) --*

        If the hosted zone was created by another service, the service that created the hosted
        zone. When a hosted zone is created by another service, you can't edit or delete it using
        Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.

    - **ChangeInfo** *(dict) --*

      A complex type that contains information about the ``CreateHostedZone`` request.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.

    - **DelegationSet** *(dict) --*

      A complex type that describes the name servers for this hosted zone.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the reusable
        delegation set.

      - **NameServers** *(list) --*

        A complex type that contains a list of the authoritative name servers for a hosted zone or
        for a reusable delegation set.

        - *(string) --*

    - **VPC** *(dict) --*

      A complex type that contains information about an Amazon VPC that you associated with this
      hosted zone.

      - **VPCRegion** *(string) --*

        (Private hosted zones only) The region that an Amazon VPC was created in.

      - **VPCId** *(string) --*

        (Private hosted zones only) The ID of an Amazon VPC.

    - **Location** *(string) --*

      The unique URL representing the new hosted zone.
    """


_ClientCreateHostedZoneVPCTypeDef = TypedDict(
    "_ClientCreateHostedZoneVPCTypeDef", {"VPCRegion": str, "VPCId": str}, total=False
)


class ClientCreateHostedZoneVPCTypeDef(_ClientCreateHostedZoneVPCTypeDef):
    """
    Type definition for `ClientCreateHostedZone` `VPC`

    (Private hosted zones only) A complex type that contains information about the Amazon VPC that
    you're associating with this hosted zone.

    You can specify only one Amazon VPC when you create a private hosted zone. To associate
    additional Amazon VPCs with the hosted zone, use `AssociateVPCWithHostedZone
    <https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html>`__
    after you create a hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "_ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef(
    _ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef
):
    """
    Type definition for `ClientCreateQueryLoggingConfigResponse` `QueryLoggingConfig`

    A complex type that contains the ID for a query logging configuration, the ID of the hosted
    zone that you want to log queries for, and the ARN for the log group that you want Amazon
    Route 53 to send query logs to.

    - **Id** *(string) --*

      The ID for a configuration for DNS query logging.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that CloudWatch Logs is logging queries for.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
      publishing logs to.
    """


_ClientCreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "_ClientCreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": ClientCreateQueryLoggingConfigResponseQueryLoggingConfigTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateQueryLoggingConfigResponseTypeDef(
    _ClientCreateQueryLoggingConfigResponseTypeDef
):
    """
    Type definition for `ClientCreateQueryLoggingConfig` `Response`

    - **QueryLoggingConfig** *(dict) --*

      A complex type that contains the ID for a query logging configuration, the ID of the hosted
      zone that you want to log queries for, and the ARN for the log group that you want Amazon
      Route 53 to send query logs to.

      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.

      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that CloudWatch Logs is logging queries for.

      - **CloudWatchLogsLogGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
        publishing logs to.

    - **Location** *(string) --*

      The unique URL representing the new query logging configuration.
    """


_ClientCreateReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "_ClientCreateReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientCreateReusableDelegationSetResponseDelegationSetTypeDef(
    _ClientCreateReusableDelegationSetResponseDelegationSetTypeDef
):
    """
    Type definition for `ClientCreateReusableDelegationSetResponse` `DelegationSet`

    A complex type that contains name server information.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigns to a reusable delegation set.

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the reusable
      delegation set.

    - **NameServers** *(list) --*

      A complex type that contains a list of the authoritative name servers for a hosted zone or
      for a reusable delegation set.

      - *(string) --*
    """


_ClientCreateReusableDelegationSetResponseTypeDef = TypedDict(
    "_ClientCreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": ClientCreateReusableDelegationSetResponseDelegationSetTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateReusableDelegationSetResponseTypeDef(
    _ClientCreateReusableDelegationSetResponseTypeDef
):
    """
    Type definition for `ClientCreateReusableDelegationSet` `Response`

    - **DelegationSet** *(dict) --*

      A complex type that contains name server information.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the reusable
        delegation set.

      - **NameServers** *(list) --*

        A complex type that contains a list of the authoritative name servers for a hosted zone or
        for a reusable delegation set.

        - *(string) --*

    - **Location** *(string) --*

      The unique URL representing the new reusable delegation set.
    """


_ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicyInstanceResponse` `TrafficPolicyInstance`

    A complex type that contains settings for the new traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
      the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated to
      all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
      that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
      fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
      another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record sets
      in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientCreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientCreateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyInstanceResponseTypeDef(
    _ClientCreateTrafficPolicyInstanceResponseTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicyInstance` `Response`

    A complex type that contains the response information for the ``CreateTrafficPolicyInstance``
    request.

    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the new traffic policy instance.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.

      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that Amazon Route 53 created resource record sets in.

      - **Name** *(string) --*

        The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
        using the resource record sets that are associated with this traffic policy instance.

      - **TTL** *(integer) --*

        The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
        the specified hosted zone.

      - **State** *(string) --*

        The value of ``State`` is one of the following values:

          Applied

        Amazon Route 53 has finished creating resource record sets, and changes have propagated to
        all Route 53 edge locations.

          Creating

        Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
        that the ``CreateTrafficPolicyInstance`` request completed successfully.

          Failed

        Route 53 wasn't able to create or update the resource record sets. When the value of
        ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
        fail.

      - **Message** *(string) --*

        If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
        another value, ``Message`` is empty.

      - **TrafficPolicyId** *(string) --*

        The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
        the specified hosted zone.

      - **TrafficPolicyVersion** *(integer) --*

        The version of the traffic policy that Amazon Route 53 used to create resource record sets
        in the specified hosted zone.

      - **TrafficPolicyType** *(string) --*

        The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
        created for this traffic policy instance.

    - **Location** *(string) --*

      A unique URL that represents a new traffic policy instance.
    """


_ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": str,
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef(
    _ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicyResponse` `TrafficPolicy`

    A complex type that contains settings for the new traffic policy.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to a traffic policy when you created it.

    - **Version** *(integer) --*

      The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
      policy, the value of ``Version`` is always 1.

    - **Name** *(string) --*

      The name that you specified when you created the traffic policy.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **Document** *(string) --*

      The definition of a traffic policy in JSON format. You specify the JSON document to use for
      a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
      JSON format, see `Traffic Policy Document Format
      <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
      .

    - **Comment** *(string) --*

      The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientCreateTrafficPolicyResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": ClientCreateTrafficPolicyResponseTrafficPolicyTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyResponseTypeDef(
    _ClientCreateTrafficPolicyResponseTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicy` `Response`

    A complex type that contains the response information for the ``CreateTrafficPolicy`` request.

    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the new traffic policy.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.

      - **Version** *(integer) --*

        The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
        policy, the value of ``Version`` is always 1.

      - **Name** *(string) --*

        The name that you specified when you created the traffic policy.

      - **Type** *(string) --*

        The DNS type of the resource record sets that Amazon Route 53 creates when you use a
        traffic policy to create a traffic policy instance.

      - **Document** *(string) --*

        The definition of a traffic policy in JSON format. You specify the JSON document to use for
        a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
        JSON format, see `Traffic Policy Document Format
        <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
        .

      - **Comment** *(string) --*

        The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

    - **Location** *(string) --*

      A unique URL that represents a new traffic policy.
    """


_ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": str,
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef(
    _ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicyVersionResponse` `TrafficPolicy`

    A complex type that contains settings for the new version of the traffic policy.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to a traffic policy when you created it.

    - **Version** *(integer) --*

      The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
      policy, the value of ``Version`` is always 1.

    - **Name** *(string) --*

      The name that you specified when you created the traffic policy.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **Document** *(string) --*

      The definition of a traffic policy in JSON format. You specify the JSON document to use for
      a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
      JSON format, see `Traffic Policy Document Format
      <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
      .

    - **Comment** *(string) --*

      The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientCreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": ClientCreateTrafficPolicyVersionResponseTrafficPolicyTypeDef,
        "Location": str,
    },
    total=False,
)


class ClientCreateTrafficPolicyVersionResponseTypeDef(
    _ClientCreateTrafficPolicyVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateTrafficPolicyVersion` `Response`

    A complex type that contains the response information for the ``CreateTrafficPolicyVersion``
    request.

    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the new version of the traffic policy.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.

      - **Version** *(integer) --*

        The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
        policy, the value of ``Version`` is always 1.

      - **Name** *(string) --*

        The name that you specified when you created the traffic policy.

      - **Type** *(string) --*

        The DNS type of the resource record sets that Amazon Route 53 creates when you use a
        traffic policy to create a traffic policy instance.

      - **Document** *(string) --*

        The definition of a traffic policy in JSON format. You specify the JSON document to use for
        a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
        JSON format, see `Traffic Policy Document Format
        <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
        .

      - **Comment** *(string) --*

        The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

    - **Location** *(string) --*

      A unique URL that represents a new traffic policy version.
    """


_ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef(
    _ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef
):
    """
    Type definition for `ClientCreateVpcAssociationAuthorizationResponse` `VPC`

    The VPC that you authorized associating with a hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientCreateVpcAssociationAuthorizationResponseTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": ClientCreateVpcAssociationAuthorizationResponseVPCTypeDef,
    },
    total=False,
)


class ClientCreateVpcAssociationAuthorizationResponseTypeDef(
    _ClientCreateVpcAssociationAuthorizationResponseTypeDef
):
    """
    Type definition for `ClientCreateVpcAssociationAuthorization` `Response`

    A complex type that contains the response information from a
    ``CreateVPCAssociationAuthorization`` request.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that you authorized associating a VPC with.

    - **VPC** *(dict) --*

      The VPC that you authorized associating with a hosted zone.

      - **VPCRegion** *(string) --*

        (Private hosted zones only) The region that an Amazon VPC was created in.

      - **VPCId** *(string) --*

        (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientCreateVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "_ClientCreateVpcAssociationAuthorizationVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientCreateVpcAssociationAuthorizationVPCTypeDef(
    _ClientCreateVpcAssociationAuthorizationVPCTypeDef
):
    """
    Type definition for `ClientCreateVpcAssociationAuthorization` `VPC`

    A complex type that contains the VPC ID and region for the VPC that you want to authorize
    associating with your hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientDeleteHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientDeleteHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientDeleteHostedZoneResponseChangeInfoTypeDef(
    _ClientDeleteHostedZoneResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientDeleteHostedZoneResponse` `ChangeInfo`

    A complex type that contains the ID, the status, and the date and time of a request to delete
    a hosted zone.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientDeleteHostedZoneResponseTypeDef = TypedDict(
    "_ClientDeleteHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDeleteHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientDeleteHostedZoneResponseTypeDef(_ClientDeleteHostedZoneResponseTypeDef):
    """
    Type definition for `ClientDeleteHostedZone` `Response`

    A complex type that contains the response to a ``DeleteHostedZone`` request.

    - **ChangeInfo** *(dict) --*

      A complex type that contains the ID, the status, and the date and time of a request to delete
      a hosted zone.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
    """


_ClientDeleteVpcAssociationAuthorizationVPCTypeDef = TypedDict(
    "_ClientDeleteVpcAssociationAuthorizationVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientDeleteVpcAssociationAuthorizationVPCTypeDef(
    _ClientDeleteVpcAssociationAuthorizationVPCTypeDef
):
    """
    Type definition for `ClientDeleteVpcAssociationAuthorization` `VPC`

    When removing authorization to associate a VPC that was created by one AWS account with a hosted
    zone that was created with a different AWS account, a complex type that includes the ID and
    region of the VPC.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef(
    _ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientDisassociateVpcFromHostedZoneResponse` `ChangeInfo`

    A complex type that describes the changes made to the specified private hosted zone.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientDisassociateVpcFromHostedZoneResponseTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneResponseTypeDef",
    {"ChangeInfo": ClientDisassociateVpcFromHostedZoneResponseChangeInfoTypeDef},
    total=False,
)


class ClientDisassociateVpcFromHostedZoneResponseTypeDef(
    _ClientDisassociateVpcFromHostedZoneResponseTypeDef
):
    """
    Type definition for `ClientDisassociateVpcFromHostedZone` `Response`

    A complex type that contains the response information for the disassociate request.

    - **ChangeInfo** *(dict) --*

      A complex type that describes the changes made to the specified private hosted zone.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
    """


_ClientDisassociateVpcFromHostedZoneVPCTypeDef = TypedDict(
    "_ClientDisassociateVpcFromHostedZoneVPCTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientDisassociateVpcFromHostedZoneVPCTypeDef(
    _ClientDisassociateVpcFromHostedZoneVPCTypeDef
):
    """
    Type definition for `ClientDisassociateVpcFromHostedZone` `VPC`

    A complex type that contains information about the VPC that you're disassociating from the
    specified hosted zone.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientGetAccountLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetAccountLimitResponseLimitTypeDef",
    {"Type": str, "Value": int},
    total=False,
)


class ClientGetAccountLimitResponseLimitTypeDef(
    _ClientGetAccountLimitResponseLimitTypeDef
):
    """
    Type definition for `ClientGetAccountLimitResponse` `Limit`

    The current setting for the specified limit. For example, if you specified
    ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of
    ``Limit`` is the maximum number of health checks that you can create using the current
    account.

    - **Type** *(string) --*

      The limit that you requested. Valid values include the following:

      * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create
      using the current account.

      * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create
      using the current account.

      * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation
      sets that you can create using the current account.

      * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can
      create using the current account.

      * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy
      instances that you can create using the current account. (Traffic policy instances are
      referred to as traffic flow policy records in the Amazon Route 53 console.)

    - **Value** *(integer) --*

      The current value for the limit that is specified by `Type
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html#Route53-Type-AccountLimit-Type>`__
      .
    """


_ClientGetAccountLimitResponseTypeDef = TypedDict(
    "_ClientGetAccountLimitResponseTypeDef",
    {"Limit": ClientGetAccountLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetAccountLimitResponseTypeDef(_ClientGetAccountLimitResponseTypeDef):
    """
    Type definition for `ClientGetAccountLimit` `Response`

    A complex type that contains the requested limit.

    - **Limit** *(dict) --*

      The current setting for the specified limit. For example, if you specified
      ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the value of
      ``Limit`` is the maximum number of health checks that you can create using the current
      account.

      - **Type** *(string) --*

        The limit that you requested. Valid values include the following:

        * **MAX_HEALTH_CHECKS_BY_OWNER** : The maximum number of health checks that you can create
        using the current account.

        * **MAX_HOSTED_ZONES_BY_OWNER** : The maximum number of hosted zones that you can create
        using the current account.

        * **MAX_REUSABLE_DELEGATION_SETS_BY_OWNER** : The maximum number of reusable delegation
        sets that you can create using the current account.

        * **MAX_TRAFFIC_POLICIES_BY_OWNER** : The maximum number of traffic policies that you can
        create using the current account.

        * **MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER** : The maximum number of traffic policy
        instances that you can create using the current account. (Traffic policy instances are
        referred to as traffic flow policy records in the Amazon Route 53 console.)

      - **Value** *(integer) --*

        The current value for the limit that is specified by `Type
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html#Route53-Type-AccountLimit-Type>`__
        .

    - **Count** *(integer) --*

      The current number of entities that you have created of the specified type. For example, if
      you specified ``MAX_HEALTH_CHECKS_BY_OWNER`` for the value of ``Type`` in the request, the
      value of ``Count`` is the current number of health checks that you have created using the
      current account.
    """


_ClientGetChangeResponseChangeInfoTypeDef = TypedDict(
    "_ClientGetChangeResponseChangeInfoTypeDef",
    {"Id": str, "Status": str, "SubmittedAt": datetime, "Comment": str},
    total=False,
)


class ClientGetChangeResponseChangeInfoTypeDef(
    _ClientGetChangeResponseChangeInfoTypeDef
):
    """
    Type definition for `ClientGetChangeResponse` `ChangeInfo`

    A complex type that contains information about the specified change batch.

    - **Id** *(string) --*

      The ID of the request.

    - **Status** *(string) --*

      The current state of the request. ``PENDING`` indicates that this request has not yet been
      applied to all Amazon Route 53 DNS servers.

    - **SubmittedAt** *(datetime) --*

      The date and time that the change request was submitted in `ISO 8601 format
      <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
      example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
      UTC.

    - **Comment** *(string) --*

      A complex type that describes change information about changes made to your hosted zone.

      This element contains an ID that you use when performing a `GetChange
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
      get detailed information about the change.
    """


_ClientGetChangeResponseTypeDef = TypedDict(
    "_ClientGetChangeResponseTypeDef",
    {"ChangeInfo": ClientGetChangeResponseChangeInfoTypeDef},
    total=False,
)


class ClientGetChangeResponseTypeDef(_ClientGetChangeResponseTypeDef):
    """
    Type definition for `ClientGetChange` `Response`

    A complex type that contains the ``ChangeInfo`` element.

    - **ChangeInfo** *(dict) --*

      A complex type that contains information about the specified change batch.

      - **Id** *(string) --*

        The ID of the request.

      - **Status** *(string) --*

        The current state of the request. ``PENDING`` indicates that this request has not yet been
        applied to all Amazon Route 53 DNS servers.

      - **SubmittedAt** *(datetime) --*

        The date and time that the change request was submitted in `ISO 8601 format
        <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time (UTC). For
        example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at 17:48:16.751
        UTC.

      - **Comment** *(string) --*

        A complex type that describes change information about changes made to your hosted zone.

        This element contains an ID that you use when performing a `GetChange
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html>`__ action to
        get detailed information about the change.
    """


_ClientGetCheckerIpRangesResponseTypeDef = TypedDict(
    "_ClientGetCheckerIpRangesResponseTypeDef",
    {"CheckerIpRanges": List[str]},
    total=False,
)


class ClientGetCheckerIpRangesResponseTypeDef(_ClientGetCheckerIpRangesResponseTypeDef):
    """
    Type definition for `ClientGetCheckerIpRanges` `Response`

    A complex type that contains the ``CheckerIpRanges`` element.

    - **CheckerIpRanges** *(list) --*

      A complex type that contains sorted list of IP ranges in CIDR format for Amazon Route 53
      health checkers.

      - *(string) --*
    """


_ClientGetGeoLocationResponseGeoLocationDetailsTypeDef = TypedDict(
    "_ClientGetGeoLocationResponseGeoLocationDetailsTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)


class ClientGetGeoLocationResponseGeoLocationDetailsTypeDef(
    _ClientGetGeoLocationResponseGeoLocationDetailsTypeDef
):
    """
    Type definition for `ClientGetGeoLocationResponse` `GeoLocationDetails`

    A complex type that contains the codes and full continent, country, and subdivision names for
    the specified geolocation code.

    - **ContinentCode** *(string) --*

      The two-letter code for the continent.

    - **ContinentName** *(string) --*

      The full name of the continent.

    - **CountryCode** *(string) --*

      The two-letter code for the country.

    - **CountryName** *(string) --*

      The name of the country.

    - **SubdivisionCode** *(string) --*

      The code for the subdivision. Route 53 currently supports only states in the United States.

    - **SubdivisionName** *(string) --*

      The full name of the subdivision. Route 53 currently supports only states in the United
      States.
    """


_ClientGetGeoLocationResponseTypeDef = TypedDict(
    "_ClientGetGeoLocationResponseTypeDef",
    {"GeoLocationDetails": ClientGetGeoLocationResponseGeoLocationDetailsTypeDef},
    total=False,
)


class ClientGetGeoLocationResponseTypeDef(_ClientGetGeoLocationResponseTypeDef):
    """
    Type definition for `ClientGetGeoLocation` `Response`

    A complex type that contains the response information for the specified geolocation code.

    - **GeoLocationDetails** *(dict) --*

      A complex type that contains the codes and full continent, country, and subdivision names for
      the specified geolocation code.

      - **ContinentCode** *(string) --*

        The two-letter code for the continent.

      - **ContinentName** *(string) --*

        The full name of the continent.

      - **CountryCode** *(string) --*

        The two-letter code for the country.

      - **CountryName** *(string) --*

        The name of the country.

      - **SubdivisionCode** *(string) --*

        The code for the subdivision. Route 53 currently supports only states in the United States.

      - **SubdivisionName** *(string) --*

        The full name of the subdivision. Route 53 currently supports only states in the United
        States.
    """


_ClientGetHealthCheckCountResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckCountResponseTypeDef", {"HealthCheckCount": int}, total=False
)


class ClientGetHealthCheckCountResponseTypeDef(
    _ClientGetHealthCheckCountResponseTypeDef
):
    """
    Type definition for `ClientGetHealthCheckCount` `Response`

    A complex type that contains the response to a ``GetHealthCheckCount`` request.

    - **HealthCheckCount** *(integer) --*

      The number of health checks associated with the current AWS account.
    """


_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef
):
    """
    Type definition for `ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservations` `StatusReport`

    A complex type that contains the last failure reason as reported by one Amazon Route 53
    health checker and the time of the failed health check.

    - **Status** *(string) --*

      A description of the status of the health check endpoint as reported by one of the
      Amazon Route 53 health checkers.

    - **CheckedTime** *(datetime) --*

      The date and time that the health checker performed the health check in `ISO 8601
      format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
      (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
      17:48:16.751 UTC.
    """


_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef",
    {
        "Region": str,
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef
):
    """
    Type definition for `ClientGetHealthCheckLastFailureReasonResponse` `HealthCheckObservations`

    A complex type that contains the last failure reason as reported by one Amazon Route 53
    health checker.

    - **Region** *(string) --*

      The region of the Amazon Route 53 health checker that provided the status in
      ``StatusReport`` .

    - **IPAddress** *(string) --*

      The IP address of the Amazon Route 53 health checker that provided the failure reason in
      ``StatusReport`` .

    - **StatusReport** *(dict) --*

      A complex type that contains the last failure reason as reported by one Amazon Route 53
      health checker and the time of the failed health check.

      - **Status** *(string) --*

        A description of the status of the health check endpoint as reported by one of the
        Amazon Route 53 health checkers.

      - **CheckedTime** *(datetime) --*

        The date and time that the health checker performed the health check in `ISO 8601
        format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
        (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
        17:48:16.751 UTC.
    """


_ClientGetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckLastFailureReasonResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)


class ClientGetHealthCheckLastFailureReasonResponseTypeDef(
    _ClientGetHealthCheckLastFailureReasonResponseTypeDef
):
    """
    Type definition for `ClientGetHealthCheckLastFailureReason` `Response`

    A complex type that contains the response to a ``GetHealthCheckLastFailureReason`` request.

    - **HealthCheckObservations** *(list) --*

      A list that contains one ``Observation`` element for each Amazon Route 53 health checker that
      is reporting a last failure reason.

      - *(dict) --*

        A complex type that contains the last failure reason as reported by one Amazon Route 53
        health checker.

        - **Region** *(string) --*

          The region of the Amazon Route 53 health checker that provided the status in
          ``StatusReport`` .

        - **IPAddress** *(string) --*

          The IP address of the Amazon Route 53 health checker that provided the failure reason in
          ``StatusReport`` .

        - **StatusReport** *(dict) --*

          A complex type that contains the last failure reason as reported by one Amazon Route 53
          health checker and the time of the failed health check.

          - **Status** *(string) --*

            A description of the status of the health check endpoint as reported by one of the
            Amazon Route 53 health checkers.

          - **CheckedTime** *(datetime) --*

            The date and time that the health checker performed the health check in `ISO 8601
            format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
            (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
            17:48:16.751 UTC.
    """


_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfiguration` `Dimensions`

    For the metric that the CloudWatch alarm is associated with, a complex type that
    contains information about one dimension.

    - **Name** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the name of one
      dimension.

    - **Value** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the value of one
      dimension.
    """


_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "Dimensions": List[
            ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponseHealthCheck` `CloudWatchAlarmConfiguration`

    A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
    monitoring for this health check.

    - **EvaluationPeriods** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the number of periods that
      the metric is compared to the threshold.

    - **Threshold** *(float) --*

      For the metric that the CloudWatch alarm is associated with, the value the metric is
      compared with.

    - **ComparisonOperator** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the arithmetic operation
      that is used for the comparison.

    - **Period** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the duration of one
      evaluation period in seconds.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that the alarm is associated with.

    - **Namespace** *(string) --*

      The namespace of the metric that the alarm is associated with. For more information, see
      `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

    - **Statistic** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the statistic that is
      applied to the metric.

    - **Dimensions** *(list) --*

      For the metric that the CloudWatch alarm is associated with, a complex type that contains
      information about the dimensions for the metric. For information, see `Amazon CloudWatch
      Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

      - *(dict) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about one dimension.

        - **Name** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the name of one
          dimension.

        - **Value** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the value of one
          dimension.
    """


_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponseHealthCheckHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
    checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --*

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine
      whether this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
      Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --*

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
      to determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
        aren't supported.
    """


_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": str,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponseHealthCheck` `HealthCheckConfig`

    A complex type that contains detailed information about one health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
      health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
      request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
      the interval that you specify in ``RequestInterval`` . Using an IP address returned by
      DNS, Route 53 then checks the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
      example, ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
      for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
      addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
      . This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is in
      local, private, non-routable, or multicast ranges. For more information about IP
      addresses for which you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
      ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.
      Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Amazon Route 53
      determines whether an endpoint is healthy.

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

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
         v1.0 or later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
      53 submits an HTTP request and searches the first 5,120 bytes of the response body for
      the string that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
      body for the string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
      state of the alarm is ``OK`` , the health check is considered healthy. If the state is
      ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
      sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
      status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
      ``Unhealthy`` , or ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks,
      Route 53 adds up the number of health checks that Route 53 health checkers consider to be
      healthy and compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health checks.
      The path can be any value for which your endpoint will return an HTTP status code of 2xx
      or 3xx when the endpoint is healthy, for example, the file
      /docs/route53-health-check.html. You can also include query string parameters, for
      example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
      passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
      checks except TCP health checks. This is typically the fully qualified DNS name of the
      endpoint on which you want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
      header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
      Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
      value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for
      ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
      Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
        checks to the endpoint. If there's no resource record set with a type of A for the name
        that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
        resolution failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets
      and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
      recommend that you create a separate health check for each endpoint. For example, create
      a health check for each HTTP server that is serving content for www.example.com. For the
      value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
      us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
        associate the health check with those resource record sets, health check results will
        be unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
      for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
      ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
      want Amazon Route 53 to search for in the response body from the specified resource. If
      the string appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your
      endpoint and the time that it sends the next health check request. Each Route 53 health
      checker makes requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30``
      seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon
      Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
      versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
      Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three health
      checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers
      in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
      the **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for
      example, to consider a health check unhealthy when it otherwise would be considered
      healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's
      what happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting
      requests to your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
      health checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
      corresponding CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to
      always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
      the corresponding resources. If you want to stop routing traffic to a resource, change
      the value of `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more
      information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health check
      that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
      considered healthy. To specify the child health checks that you want to associate with a
      ``CALCULATED`` health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53 always
      considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
      element for each health check that you want to associate with a ``CALCULATED`` health
      check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of
      ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
      negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
      the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the
      ``client_hello`` message. If you don't enable SNI, the status of the health check will be
      ``SSL alert handshake_failure`` . A health check can also have that status for other
      reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
      configuration on your endpoint and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
      field and possibly several more in the ``Subject Alternative Names`` field. One of the
      domain names in the certificate should match the value that you specify for
      ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
      with a certificate that does not include the domain name that you specified in
      ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
      attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
      ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want
      Amazon Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs checks
      from all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks,
      Route 53 will briefly continue to perform checks from that region to ensure that some
      health checkers are always checking the endpoint (for example, if you replace three
      regions with four different regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
      checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --*

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine
        whether this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
        Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --*

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
        to determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
          aren't supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state, the
      status that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
      that CloudWatch had sufficient data to determine the alarm state. For new health checks
      that have no last known status, the default status for the health check is healthy.
    """


_ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponseHealthCheck` `LinkedService`

    If the health check was created by another service, the service that created the health
    check. When a health check is created by another service, you can't edit or delete it using
    Amazon Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientGetHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientGetHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientGetHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientGetHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckResponseHealthCheckTypeDef(
    _ClientGetHealthCheckResponseHealthCheckTypeDef
):
    """
    Type definition for `ClientGetHealthCheckResponse` `HealthCheck`

    A complex type that contains information about one health check that is associated with the
    current AWS account.

    - **Id** *(string) --*

      The identifier that Amazon Route 53assigned to the health check when you created it. When
      you add or update a resource record set, you use this value to specify which health check
      to use. The value can be up to 64 characters long.

    - **CallerReference** *(string) --*

      A unique string that you specified when you created the health check.

    - **LinkedService** *(dict) --*

      If the health check was created by another service, the service that created the health
      check. When a health check is created by another service, you can't edit or delete it using
      Amazon Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.

    - **HealthCheckConfig** *(dict) --*

      A complex type that contains detailed information about one health check.

      - **IPAddress** *(string) --*

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
        health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
        request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
        the interval that you specify in ``RequestInterval`` . Using an IP address returned by
        DNS, Route 53 then checks the health of the endpoint.

        Use one of the following formats for the value of ``IPAddress`` :

        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
        example, ``192.0.2.44`` .

        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
        for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
        addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
        associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
        . This ensures that the IP address of your instance will never change.

        For more information, see `FullyQualifiedDomainName
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
        .

        Constraints: Route 53 can't check the health of endpoints for which the IP address is in
        local, private, non-routable, or multicast ranges. For more information about IP
        addresses for which you can't create health checks, see the following documents:

        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
        <https://tools.ietf.org/html/rfc6598>`__

        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
        ``IPAddress`` .

      - **Port** *(integer) --*

        The port on the endpoint on which you want Amazon Route 53 to perform health checks.
        Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Amazon Route 53
        determines whether an endpoint is healthy.

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

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
           v1.0 or later.

        * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
        53 submits an HTTP request and searches the first 5,120 bytes of the response body for
        the string that you specify in ``SearchString`` .

        * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
        body for the string that you specify in ``SearchString`` .

        * **TCP** : Route 53 tries to establish a TCP connection.

        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
        state of the alarm is ``OK`` , the health check is considered healthy. If the state is
        ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
        sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
        status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
        ``Unhealthy`` , or ``LastKnownStatus`` .

        * **CALCULATED** : For health checks that monitor the status of other health checks,
        Route 53 adds up the number of health checks that Route 53 health checkers consider to be
        healthy and compares that number with the value of ``HealthThreshold`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path, if any, that you want Amazon Route 53 to request when performing health checks.
        The path can be any value for which your endpoint will return an HTTP status code of 2xx
        or 3xx when the endpoint is healthy, for example, the file
        /docs/route53-health-check.html. You can also include query string parameters, for
        example, ``/welcome.html?language=jp&login=y`` .

      - **FullyQualifiedDomainName** *(string) --*

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         **If you specify a value for**  ``IPAddress`` :

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
        passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
        checks except TCP health checks. This is typically the fully qualified DNS name of the
        endpoint on which you want Route 53 to perform health checks.

        When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
        header:

        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the Host header.

        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the ``Host`` header.

        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
        Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

        If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
        value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         **If you don't specify a value for ``IPAddress`` ** :

        Route 53 sends a DNS request to the domain that you specify for
        ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
        Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

        .. note::

          If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
          checks to the endpoint. If there's no resource record set with a type of A for the name
          that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
          resolution failed" error.

        If you want to check the health of weighted, latency, or failover resource record sets
        and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
        recommend that you create a separate health check for each endpoint. For example, create
        a health check for each HTTP server that is serving content for www.example.com. For the
        value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
        us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

        .. warning::

          In this configuration, if you create a health check for which the value of
          ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
          associate the health check with those resource record sets, health check results will
          be unpredictable.

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
        ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
        ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
        for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
        ``Host`` header.

      - **SearchString** *(string) --*

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
        want Amazon Route 53 to search for in the response body from the specified resource. If
        the string appears in the response body, Route 53 considers the resource healthy.

        Route 53 considers case when searching for ``SearchString`` in the response body.

      - **RequestInterval** *(integer) --*

        The number of seconds between the time that Amazon Route 53 gets a response from your
        endpoint and the time that it sends the next health check request. Each Route 53 health
        checker makes requests at this interval.

        .. warning::

          You can't change the value of ``RequestInterval`` after you create a health check.

        If you don't specify a value for ``RequestInterval`` , the default value is ``30``
        seconds.

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Amazon
        Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
        versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
        Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

        If you don't specify a value for ``FailureThreshold`` , the default value is three health
        checks.

      - **MeasureLatency** *(boolean) --*

        Specify whether you want Amazon Route 53 to measure the latency between health checkers
        in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
        the **Health Checks** page in the Route 53 console.

        .. warning::

          You can't change the value of ``MeasureLatency`` after you create a health check.

      - **Inverted** *(boolean) --*

        Specify whether you want Amazon Route 53 to invert the status of a health check, for
        example, to consider a health check unhealthy when it otherwise would be considered
        healthy.

      - **Disabled** *(boolean) --*

        Stops Route 53 from performing health checks. When you disable a health check, here's
        what happens:

        * **Health checks that check the health of endpoints:** Route 53 stops submitting
        requests to your application, server, or other resource.

        * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
        health checks.

        * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
        corresponding CloudWatch metrics.

        After you disable a health check, Route 53 considers the status of the health check to
        always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
        the corresponding resources. If you want to stop routing traffic to a resource, change
        the value of `Inverted
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
        .

        Charges for a health check still apply when the health check is disabled. For more
        information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

      - **HealthThreshold** *(integer) --*

        The number of child health checks that are associated with a ``CALCULATED`` health check
        that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
        considered healthy. To specify the child health checks that you want to associate with a
        ``CALCULATED`` health check, use the `ChildHealthChecks
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
        element.

        Note the following:

        * If you specify a number greater than the number of child health checks, Route 53 always
        considers this health check to be unhealthy.

        * If you specify ``0`` , Route 53 always considers this health check to be healthy.

      - **ChildHealthChecks** *(list) --*

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
        element for each health check that you want to associate with a ``CALCULATED`` health
        check.

        - *(string) --*

      - **EnableSNI** *(boolean) --*

        Specify whether you want Amazon Route 53 to send the value of
        ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
        negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
        the applicable SSL/TLS certificate.

        Some endpoints require that ``HTTPS`` requests include the host name in the
        ``client_hello`` message. If you don't enable SNI, the status of the health check will be
        ``SSL alert handshake_failure`` . A health check can also have that status for other
        reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
        configuration on your endpoint and confirm that your certificate is valid.

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
        field and possibly several more in the ``Subject Alternative Names`` field. One of the
        domain names in the certificate should match the value that you specify for
        ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
        with a certificate that does not include the domain name that you specified in
        ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
        attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
        ``client_hello`` message.

      - **Regions** *(list) --*

        A complex type that contains one ``Region`` element for each region from which you want
        Amazon Route 53 health checkers to check the specified endpoint.

        If you don't specify any regions, Route 53 health checkers automatically performs checks
        from all of the regions that are listed under **Valid Values** .

        If you update a health check to remove a region that has been performing health checks,
        Route 53 will briefly continue to perform checks from that region to ensure that some
        health checkers are always checking the endpoint (for example, if you replace three
        regions with four different regions).

        - *(string) --*

      - **AlarmIdentifier** *(dict) --*

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
        checkers to use to determine whether the specified health check is healthy.

        - **Region** *(string) --*

          For the CloudWatch alarm that you want Route 53 health checkers to use to determine
          whether this health check is healthy, the region that the alarm was created in.

          For the current list of CloudWatch regions, see `Amazon CloudWatch
          <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
          Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        - **Name** *(string) --*

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
          to determine whether this health check is healthy.

          .. note::

            Route 53 supports CloudWatch alarms with the following features:

            * Standard-resolution metrics. High-resolution metrics aren't supported. For more
            information, see `High-Resolution Metrics
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
            in the *Amazon CloudWatch User Guide* .

            * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
            aren't supported.

      - **InsufficientDataHealthStatus** *(string) --*

        When CloudWatch has insufficient data about the metric to determine the alarm state, the
        status that you want Amazon Route 53 to assign to the health check:

        * ``Healthy`` : Route 53 considers the health check to be healthy.

        * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

        * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
        that CloudWatch had sufficient data to determine the alarm state. For new health checks
        that have no last known status, the default status for the health check is healthy.

    - **HealthCheckVersion** *(integer) --*

      The version of the health check. You can optionally pass this value in a call to
      ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

    - **CloudWatchAlarmConfiguration** *(dict) --*

      A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
      monitoring for this health check.

      - **EvaluationPeriods** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the number of periods that
        the metric is compared to the threshold.

      - **Threshold** *(float) --*

        For the metric that the CloudWatch alarm is associated with, the value the metric is
        compared with.

      - **ComparisonOperator** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the arithmetic operation
        that is used for the comparison.

      - **Period** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the duration of one
        evaluation period in seconds.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that the alarm is associated with.

      - **Namespace** *(string) --*

        The namespace of the metric that the alarm is associated with. For more information, see
        `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

      - **Statistic** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the statistic that is
        applied to the metric.

      - **Dimensions** *(list) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that contains
        information about the dimensions for the metric. For information, see `Amazon CloudWatch
        Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        - *(dict) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that
          contains information about one dimension.

          - **Name** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the name of one
            dimension.

          - **Value** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the value of one
            dimension.
    """


_ClientGetHealthCheckResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckResponseTypeDef",
    {"HealthCheck": ClientGetHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientGetHealthCheckResponseTypeDef(_ClientGetHealthCheckResponseTypeDef):
    """
    Type definition for `ClientGetHealthCheck` `Response`

    A complex type that contains the response to a ``GetHealthCheck`` request.

    - **HealthCheck** *(dict) --*

      A complex type that contains information about one health check that is associated with the
      current AWS account.

      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check
        to use. The value can be up to 64 characters long.

      - **CallerReference** *(string) --*

        A unique string that you specified when you created the health check.

      - **LinkedService** *(dict) --*

        If the health check was created by another service, the service that created the health
        check. When a health check is created by another service, you can't edit or delete it using
        Amazon Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.

      - **HealthCheckConfig** *(dict) --*

        A complex type that contains detailed information about one health check.

        - **IPAddress** *(string) --*

          The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
          health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
          request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
          the interval that you specify in ``RequestInterval`` . Using an IP address returned by
          DNS, Route 53 then checks the health of the endpoint.

          Use one of the following formats for the value of ``IPAddress`` :

          * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
          example, ``192.0.2.44`` .

          * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
          for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
          addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

          If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
          associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
          . This ensures that the IP address of your instance will never change.

          For more information, see `FullyQualifiedDomainName
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
          .

          Constraints: Route 53 can't check the health of endpoints for which the IP address is in
          local, private, non-routable, or multicast ranges. For more information about IP
          addresses for which you can't create health checks, see the following documents:

          * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

          * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
          <https://tools.ietf.org/html/rfc6598>`__

          * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

          When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
          ``IPAddress`` .

        - **Port** *(integer) --*

          The port on the endpoint on which you want Amazon Route 53 to perform health checks.
          Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

        - **Type** *(string) --*

          The type of health check that you want to create, which indicates how Amazon Route 53
          determines whether an endpoint is healthy.

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

             If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
             v1.0 or later.

          * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
          53 submits an HTTP request and searches the first 5,120 bytes of the response body for
          the string that you specify in ``SearchString`` .

          * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
          Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
          body for the string that you specify in ``SearchString`` .

          * **TCP** : Route 53 tries to establish a TCP connection.

          * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
          state of the alarm is ``OK`` , the health check is considered healthy. If the state is
          ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
          sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
          status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
          ``Unhealthy`` , or ``LastKnownStatus`` .

          * **CALCULATED** : For health checks that monitor the status of other health checks,
          Route 53 adds up the number of health checks that Route 53 health checkers consider to be
          healthy and compares that number with the value of ``HealthThreshold`` .

          For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

        - **ResourcePath** *(string) --*

          The path, if any, that you want Amazon Route 53 to request when performing health checks.
          The path can be any value for which your endpoint will return an HTTP status code of 2xx
          or 3xx when the endpoint is healthy, for example, the file
          /docs/route53-health-check.html. You can also include query string parameters, for
          example, ``/welcome.html?language=jp&login=y`` .

        - **FullyQualifiedDomainName** *(string) --*

          Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

           **If you specify a value for**  ``IPAddress`` :

          Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
          passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
          checks except TCP health checks. This is typically the fully qualified DNS name of the
          endpoint on which you want Route 53 to perform health checks.

          When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
          header:

          * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the Host header.

          * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the ``Host`` header.

          * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
          Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

          If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
          value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

           **If you don't specify a value for ``IPAddress`` ** :

          Route 53 sends a DNS request to the domain that you specify for
          ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
          Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

          .. note::

            If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
            checks to the endpoint. If there's no resource record set with a type of A for the name
            that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
            resolution failed" error.

          If you want to check the health of weighted, latency, or failover resource record sets
          and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
          recommend that you create a separate health check for each endpoint. For example, create
          a health check for each HTTP server that is serving content for www.example.com. For the
          value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
          us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

          .. warning::

            In this configuration, if you create a health check for which the value of
            ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
            associate the health check with those resource record sets, health check results will
            be unpredictable.

          In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
          ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
          ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
          for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
          ``Host`` header.

        - **SearchString** *(string) --*

          If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
          want Amazon Route 53 to search for in the response body from the specified resource. If
          the string appears in the response body, Route 53 considers the resource healthy.

          Route 53 considers case when searching for ``SearchString`` in the response body.

        - **RequestInterval** *(integer) --*

          The number of seconds between the time that Amazon Route 53 gets a response from your
          endpoint and the time that it sends the next health check request. Each Route 53 health
          checker makes requests at this interval.

          .. warning::

            You can't change the value of ``RequestInterval`` after you create a health check.

          If you don't specify a value for ``RequestInterval`` , the default value is ``30``
          seconds.

        - **FailureThreshold** *(integer) --*

          The number of consecutive health checks that an endpoint must pass or fail for Amazon
          Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
          versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
          Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

          If you don't specify a value for ``FailureThreshold`` , the default value is three health
          checks.

        - **MeasureLatency** *(boolean) --*

          Specify whether you want Amazon Route 53 to measure the latency between health checkers
          in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
          the **Health Checks** page in the Route 53 console.

          .. warning::

            You can't change the value of ``MeasureLatency`` after you create a health check.

        - **Inverted** *(boolean) --*

          Specify whether you want Amazon Route 53 to invert the status of a health check, for
          example, to consider a health check unhealthy when it otherwise would be considered
          healthy.

        - **Disabled** *(boolean) --*

          Stops Route 53 from performing health checks. When you disable a health check, here's
          what happens:

          * **Health checks that check the health of endpoints:** Route 53 stops submitting
          requests to your application, server, or other resource.

          * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
          health checks.

          * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
          corresponding CloudWatch metrics.

          After you disable a health check, Route 53 considers the status of the health check to
          always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
          the corresponding resources. If you want to stop routing traffic to a resource, change
          the value of `Inverted
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
          .

          Charges for a health check still apply when the health check is disabled. For more
          information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

        - **HealthThreshold** *(integer) --*

          The number of child health checks that are associated with a ``CALCULATED`` health check
          that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
          considered healthy. To specify the child health checks that you want to associate with a
          ``CALCULATED`` health check, use the `ChildHealthChecks
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
          element.

          Note the following:

          * If you specify a number greater than the number of child health checks, Route 53 always
          considers this health check to be unhealthy.

          * If you specify ``0`` , Route 53 always considers this health check to be healthy.

        - **ChildHealthChecks** *(list) --*

          (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
          element for each health check that you want to associate with a ``CALCULATED`` health
          check.

          - *(string) --*

        - **EnableSNI** *(boolean) --*

          Specify whether you want Amazon Route 53 to send the value of
          ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
          negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
          the applicable SSL/TLS certificate.

          Some endpoints require that ``HTTPS`` requests include the host name in the
          ``client_hello`` message. If you don't enable SNI, the status of the health check will be
          ``SSL alert handshake_failure`` . A health check can also have that status for other
          reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
          configuration on your endpoint and confirm that your certificate is valid.

          The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
          field and possibly several more in the ``Subject Alternative Names`` field. One of the
          domain names in the certificate should match the value that you specify for
          ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
          with a certificate that does not include the domain name that you specified in
          ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
          attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
          ``client_hello`` message.

        - **Regions** *(list) --*

          A complex type that contains one ``Region`` element for each region from which you want
          Amazon Route 53 health checkers to check the specified endpoint.

          If you don't specify any regions, Route 53 health checkers automatically performs checks
          from all of the regions that are listed under **Valid Values** .

          If you update a health check to remove a region that has been performing health checks,
          Route 53 will briefly continue to perform checks from that region to ensure that some
          health checkers are always checking the endpoint (for example, if you replace three
          regions with four different regions).

          - *(string) --*

        - **AlarmIdentifier** *(dict) --*

          A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
          checkers to use to determine whether the specified health check is healthy.

          - **Region** *(string) --*

            For the CloudWatch alarm that you want Route 53 health checkers to use to determine
            whether this health check is healthy, the region that the alarm was created in.

            For the current list of CloudWatch regions, see `Amazon CloudWatch
            <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
            Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

          - **Name** *(string) --*

            The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
            to determine whether this health check is healthy.

            .. note::

              Route 53 supports CloudWatch alarms with the following features:

              * Standard-resolution metrics. High-resolution metrics aren't supported. For more
              information, see `High-Resolution Metrics
              <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
              in the *Amazon CloudWatch User Guide* .

              * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
              aren't supported.

        - **InsufficientDataHealthStatus** *(string) --*

          When CloudWatch has insufficient data about the metric to determine the alarm state, the
          status that you want Amazon Route 53 to assign to the health check:

          * ``Healthy`` : Route 53 considers the health check to be healthy.

          * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

          * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
          that CloudWatch had sufficient data to determine the alarm state. For new health checks
          that have no last known status, the default status for the health check is healthy.

      - **HealthCheckVersion** *(integer) --*

        The version of the health check. You can optionally pass this value in a call to
        ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

      - **CloudWatchAlarmConfiguration** *(dict) --*

        A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
        monitoring for this health check.

        - **EvaluationPeriods** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the number of periods that
          the metric is compared to the threshold.

        - **Threshold** *(float) --*

          For the metric that the CloudWatch alarm is associated with, the value the metric is
          compared with.

        - **ComparisonOperator** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the arithmetic operation
          that is used for the comparison.

        - **Period** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the duration of one
          evaluation period in seconds.

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that the alarm is associated with.

        - **Namespace** *(string) --*

          The namespace of the metric that the alarm is associated with. For more information, see
          `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

        - **Statistic** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the statistic that is
          applied to the metric.

        - **Dimensions** *(list) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that contains
          information about the dimensions for the metric. For information, see `Amazon CloudWatch
          Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

          - *(dict) --*

            For the metric that the CloudWatch alarm is associated with, a complex type that
            contains information about one dimension.

            - **Name** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the name of one
              dimension.

            - **Value** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the value of one
              dimension.
    """


_ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef",
    {"Status": str, "CheckedTime": datetime},
    total=False,
)


class ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef(
    _ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef
):
    """
    Type definition for `ClientGetHealthCheckStatusResponseHealthCheckObservations` `StatusReport`

    A complex type that contains the last failure reason as reported by one Amazon Route 53
    health checker and the time of the failed health check.

    - **Status** *(string) --*

      A description of the status of the health check endpoint as reported by one of the
      Amazon Route 53 health checkers.

    - **CheckedTime** *(datetime) --*

      The date and time that the health checker performed the health check in `ISO 8601
      format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
      (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
      17:48:16.751 UTC.
    """


_ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef",
    {
        "Region": str,
        "IPAddress": str,
        "StatusReport": ClientGetHealthCheckStatusResponseHealthCheckObservationsStatusReportTypeDef,
    },
    total=False,
)


class ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef(
    _ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef
):
    """
    Type definition for `ClientGetHealthCheckStatusResponse` `HealthCheckObservations`

    A complex type that contains the last failure reason as reported by one Amazon Route 53
    health checker.

    - **Region** *(string) --*

      The region of the Amazon Route 53 health checker that provided the status in
      ``StatusReport`` .

    - **IPAddress** *(string) --*

      The IP address of the Amazon Route 53 health checker that provided the failure reason in
      ``StatusReport`` .

    - **StatusReport** *(dict) --*

      A complex type that contains the last failure reason as reported by one Amazon Route 53
      health checker and the time of the failed health check.

      - **Status** *(string) --*

        A description of the status of the health check endpoint as reported by one of the
        Amazon Route 53 health checkers.

      - **CheckedTime** *(datetime) --*

        The date and time that the health checker performed the health check in `ISO 8601
        format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
        (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
        17:48:16.751 UTC.
    """


_ClientGetHealthCheckStatusResponseTypeDef = TypedDict(
    "_ClientGetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List[
            ClientGetHealthCheckStatusResponseHealthCheckObservationsTypeDef
        ]
    },
    total=False,
)


class ClientGetHealthCheckStatusResponseTypeDef(
    _ClientGetHealthCheckStatusResponseTypeDef
):
    """
    Type definition for `ClientGetHealthCheckStatus` `Response`

    A complex type that contains the response to a ``GetHealthCheck`` request.

    - **HealthCheckObservations** *(list) --*

      A list that contains one ``HealthCheckObservation`` element for each Amazon Route 53 health
      checker that is reporting a status about the health check endpoint.

      - *(dict) --*

        A complex type that contains the last failure reason as reported by one Amazon Route 53
        health checker.

        - **Region** *(string) --*

          The region of the Amazon Route 53 health checker that provided the status in
          ``StatusReport`` .

        - **IPAddress** *(string) --*

          The IP address of the Amazon Route 53 health checker that provided the failure reason in
          ``StatusReport`` .

        - **StatusReport** *(dict) --*

          A complex type that contains the last failure reason as reported by one Amazon Route 53
          health checker and the time of the failed health check.

          - **Status** *(string) --*

            A description of the status of the health check endpoint as reported by one of the
            Amazon Route 53 health checkers.

          - **CheckedTime** *(datetime) --*

            The date and time that the health checker performed the health check in `ISO 8601
            format <https://en.wikipedia.org/wiki/ISO_8601>`__ and Coordinated Universal Time
            (UTC). For example, the value ``2017-03-27T17:48:16.751Z`` represents March 27, 2017 at
            17:48:16.751 UTC.
    """


_ClientGetHostedZoneCountResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneCountResponseTypeDef", {"HostedZoneCount": int}, total=False
)


class ClientGetHostedZoneCountResponseTypeDef(_ClientGetHostedZoneCountResponseTypeDef):
    """
    Type definition for `ClientGetHostedZoneCount` `Response`

    A complex type that contains the response to a ``GetHostedZoneCount`` request.

    - **HostedZoneCount** *(integer) --*

      The total number of public and private hosted zones that are associated with the current AWS
      account.
    """


_ClientGetHostedZoneLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetHostedZoneLimitResponseLimitTypeDef",
    {"Type": str, "Value": int},
    total=False,
)


class ClientGetHostedZoneLimitResponseLimitTypeDef(
    _ClientGetHostedZoneLimitResponseLimitTypeDef
):
    """
    Type definition for `ClientGetHostedZoneLimitResponse` `Limit`

    The current setting for the specified limit. For example, if you specified
    ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Limit`` is
    the maximum number of records that you can create in the specified hosted zone.

    - **Type** *(string) --*

      The limit that you requested. Valid values include the following:

      * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the
      specified hosted zone.

      * **MAX_VPCS_ASSOCIATED_BY_ZONE** : The maximum number of Amazon VPCs that you can
      associate with the specified private hosted zone.

    - **Value** *(integer) --*

      The current value for the limit that is specified by ``Type`` .
    """


_ClientGetHostedZoneLimitResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneLimitResponseTypeDef",
    {"Limit": ClientGetHostedZoneLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetHostedZoneLimitResponseTypeDef(_ClientGetHostedZoneLimitResponseTypeDef):
    """
    Type definition for `ClientGetHostedZoneLimit` `Response`

    A complex type that contains the requested limit.

    - **Limit** *(dict) --*

      The current setting for the specified limit. For example, if you specified
      ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of ``Limit`` is
      the maximum number of records that you can create in the specified hosted zone.

      - **Type** *(string) --*

        The limit that you requested. Valid values include the following:

        * **MAX_RRSETS_BY_ZONE** : The maximum number of records that you can create in the
        specified hosted zone.

        * **MAX_VPCS_ASSOCIATED_BY_ZONE** : The maximum number of Amazon VPCs that you can
        associate with the specified private hosted zone.

      - **Value** *(integer) --*

        The current value for the limit that is specified by ``Type`` .

    - **Count** *(integer) --*

      The current number of entities that you have created of the specified type. For example, if
      you specified ``MAX_RRSETS_BY_ZONE`` for the value of ``Type`` in the request, the value of
      ``Count`` is the current number of records that you have created in the specified hosted zone.
    """


_ClientGetHostedZoneResponseDelegationSetTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientGetHostedZoneResponseDelegationSetTypeDef(
    _ClientGetHostedZoneResponseDelegationSetTypeDef
):
    """
    Type definition for `ClientGetHostedZoneResponse` `DelegationSet`

    A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigns to a reusable delegation set.

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the reusable
      delegation set.

    - **NameServers** *(list) --*

      A complex type that contains a list of the authoritative name servers for a hosted zone or
      for a reusable delegation set.

      - *(string) --*
    """


_ClientGetHostedZoneResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneConfigTypeDef(
    _ClientGetHostedZoneResponseHostedZoneConfigTypeDef
):
    """
    Type definition for `ClientGetHostedZoneResponseHostedZone` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef(
    _ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef
):
    """
    Type definition for `ClientGetHostedZoneResponseHostedZone` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientGetHostedZoneResponseHostedZoneTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientGetHostedZoneResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientGetHostedZoneResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientGetHostedZoneResponseHostedZoneTypeDef(
    _ClientGetHostedZoneResponseHostedZoneTypeDef
):
    """
    Type definition for `ClientGetHostedZoneResponse` `HostedZone`

    A complex type that contains general information about the specified hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have registered
      with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientGetHostedZoneResponseVPCsTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseVPCsTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientGetHostedZoneResponseVPCsTypeDef(_ClientGetHostedZoneResponseVPCsTypeDef):
    """
    Type definition for `ClientGetHostedZoneResponse` `VPCs`

    (Private hosted zones only) A complex type that contains information about an Amazon VPC.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientGetHostedZoneResponseTypeDef = TypedDict(
    "_ClientGetHostedZoneResponseTypeDef",
    {
        "HostedZone": ClientGetHostedZoneResponseHostedZoneTypeDef,
        "DelegationSet": ClientGetHostedZoneResponseDelegationSetTypeDef,
        "VPCs": List[ClientGetHostedZoneResponseVPCsTypeDef],
    },
    total=False,
)


class ClientGetHostedZoneResponseTypeDef(_ClientGetHostedZoneResponseTypeDef):
    """
    Type definition for `ClientGetHostedZone` `Response`

    A complex type that contain the response to a ``GetHostedZone`` request.

    - **HostedZone** *(dict) --*

      A complex type that contains general information about the specified hosted zone.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.

      - **Name** *(string) --*

        The name of the domain. For public hosted zones, this is the name that you have registered
        with your DNS registrar.

        For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
        (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the hosted zone.

      - **Config** *(dict) --*

        A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
        the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
        ``Comment`` elements don't appear in the response.

        - **Comment** *(string) --*

          Any comments that you want to include about the hosted zone.

        - **PrivateZone** *(boolean) --*

          A value that indicates whether this is a private hosted zone.

      - **ResourceRecordSetCount** *(integer) --*

        The number of resource record sets in the hosted zone.

      - **LinkedService** *(dict) --*

        If the hosted zone was created by another service, the service that created the hosted
        zone. When a hosted zone is created by another service, you can't edit or delete it using
        Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.

    - **DelegationSet** *(dict) --*

      A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the reusable
        delegation set.

      - **NameServers** *(list) --*

        A complex type that contains a list of the authoritative name servers for a hosted zone or
        for a reusable delegation set.

        - *(string) --*

    - **VPCs** *(list) --*

      A complex type that contains information about the VPCs that are associated with the
      specified hosted zone.

      - *(dict) --*

        (Private hosted zones only) A complex type that contains information about an Amazon VPC.

        - **VPCRegion** *(string) --*

          (Private hosted zones only) The region that an Amazon VPC was created in.

        - **VPCId** *(string) --*

          (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef = TypedDict(
    "_ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef(
    _ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef
):
    """
    Type definition for `ClientGetQueryLoggingConfigResponse` `QueryLoggingConfig`

    A complex type that contains information about the query logging configuration that you
    specified in a `GetQueryLoggingConfig
    <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html>`__
    request.

    - **Id** *(string) --*

      The ID for a configuration for DNS query logging.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that CloudWatch Logs is logging queries for.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
      publishing logs to.
    """


_ClientGetQueryLoggingConfigResponseTypeDef = TypedDict(
    "_ClientGetQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": ClientGetQueryLoggingConfigResponseQueryLoggingConfigTypeDef
    },
    total=False,
)


class ClientGetQueryLoggingConfigResponseTypeDef(
    _ClientGetQueryLoggingConfigResponseTypeDef
):
    """
    Type definition for `ClientGetQueryLoggingConfig` `Response`

    - **QueryLoggingConfig** *(dict) --*

      A complex type that contains information about the query logging configuration that you
      specified in a `GetQueryLoggingConfig
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html>`__
      request.

      - **Id** *(string) --*

        The ID for a configuration for DNS query logging.

      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that CloudWatch Logs is logging queries for.

      - **CloudWatchLogsLogGroupArn** *(string) --*

        The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
        publishing logs to.
    """


_ClientGetReusableDelegationSetLimitResponseLimitTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetLimitResponseLimitTypeDef",
    {"Type": str, "Value": int},
    total=False,
)


class ClientGetReusableDelegationSetLimitResponseLimitTypeDef(
    _ClientGetReusableDelegationSetLimitResponseLimitTypeDef
):
    """
    Type definition for `ClientGetReusableDelegationSetLimitResponse` `Limit`

    The current setting for the limit on hosted zones that you can associate with the specified
    reusable delegation set.

    - **Type** *(string) --*

      The limit that you requested: ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` , the maximum number
      of hosted zones that you can associate with the specified reusable delegation set.

    - **Value** *(integer) --*

      The current value for the ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` limit.
    """


_ClientGetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetLimitResponseTypeDef",
    {"Limit": ClientGetReusableDelegationSetLimitResponseLimitTypeDef, "Count": int},
    total=False,
)


class ClientGetReusableDelegationSetLimitResponseTypeDef(
    _ClientGetReusableDelegationSetLimitResponseTypeDef
):
    """
    Type definition for `ClientGetReusableDelegationSetLimit` `Response`

    A complex type that contains the requested limit.

    - **Limit** *(dict) --*

      The current setting for the limit on hosted zones that you can associate with the specified
      reusable delegation set.

      - **Type** *(string) --*

        The limit that you requested: ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` , the maximum number
        of hosted zones that you can associate with the specified reusable delegation set.

      - **Value** *(integer) --*

        The current value for the ``MAX_ZONES_BY_REUSABLE_DELEGATION_SET`` limit.

    - **Count** *(integer) --*

      The current number of hosted zones that you can associate with the specified reusable
      delegation set.
    """


_ClientGetReusableDelegationSetResponseDelegationSetTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetResponseDelegationSetTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientGetReusableDelegationSetResponseDelegationSetTypeDef(
    _ClientGetReusableDelegationSetResponseDelegationSetTypeDef
):
    """
    Type definition for `ClientGetReusableDelegationSetResponse` `DelegationSet`

    A complex type that contains information about the reusable delegation set.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigns to a reusable delegation set.

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the reusable
      delegation set.

    - **NameServers** *(list) --*

      A complex type that contains a list of the authoritative name servers for a hosted zone or
      for a reusable delegation set.

      - *(string) --*
    """


_ClientGetReusableDelegationSetResponseTypeDef = TypedDict(
    "_ClientGetReusableDelegationSetResponseTypeDef",
    {"DelegationSet": ClientGetReusableDelegationSetResponseDelegationSetTypeDef},
    total=False,
)


class ClientGetReusableDelegationSetResponseTypeDef(
    _ClientGetReusableDelegationSetResponseTypeDef
):
    """
    Type definition for `ClientGetReusableDelegationSet` `Response`

    A complex type that contains the response to the ``GetReusableDelegationSet`` request.

    - **DelegationSet** *(dict) --*

      A complex type that contains information about the reusable delegation set.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigns to a reusable delegation set.

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the reusable
        delegation set.

      - **NameServers** *(list) --*

        A complex type that contains a list of the authoritative name servers for a hosted zone or
        for a reusable delegation set.

        - *(string) --*
    """


_ClientGetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceCountResponseTypeDef",
    {"TrafficPolicyInstanceCount": int},
    total=False,
)


class ClientGetTrafficPolicyInstanceCountResponseTypeDef(
    _ClientGetTrafficPolicyInstanceCountResponseTypeDef
):
    """
    Type definition for `ClientGetTrafficPolicyInstanceCount` `Response`

    A complex type that contains information about the resource record sets that Amazon Route 53
    created based on a specified traffic policy.

    - **TrafficPolicyInstanceCount** *(integer) --*

      The number of traffic policy instances that are associated with the current AWS account.
    """


_ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    Type definition for `ClientGetTrafficPolicyInstanceResponse` `TrafficPolicyInstance`

    A complex type that contains settings for the traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
      the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated to
      all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
      that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
      fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
      another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record sets
      in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientGetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientGetTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
    },
    total=False,
)


class ClientGetTrafficPolicyInstanceResponseTypeDef(
    _ClientGetTrafficPolicyInstanceResponseTypeDef
):
    """
    Type definition for `ClientGetTrafficPolicyInstance` `Response`

    A complex type that contains information about the resource record sets that Amazon Route 53
    created based on a specified traffic policy.

    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the traffic policy instance.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.

      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that Amazon Route 53 created resource record sets in.

      - **Name** *(string) --*

        The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
        using the resource record sets that are associated with this traffic policy instance.

      - **TTL** *(integer) --*

        The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
        the specified hosted zone.

      - **State** *(string) --*

        The value of ``State`` is one of the following values:

          Applied

        Amazon Route 53 has finished creating resource record sets, and changes have propagated to
        all Route 53 edge locations.

          Creating

        Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
        that the ``CreateTrafficPolicyInstance`` request completed successfully.

          Failed

        Route 53 wasn't able to create or update the resource record sets. When the value of
        ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
        fail.

      - **Message** *(string) --*

        If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
        another value, ``Message`` is empty.

      - **TrafficPolicyId** *(string) --*

        The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
        the specified hosted zone.

      - **TrafficPolicyVersion** *(integer) --*

        The version of the traffic policy that Amazon Route 53 used to create resource record sets
        in the specified hosted zone.

      - **TrafficPolicyType** *(string) --*

        The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
        created for this traffic policy instance.
    """


_ClientGetTrafficPolicyResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientGetTrafficPolicyResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": str,
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientGetTrafficPolicyResponseTrafficPolicyTypeDef(
    _ClientGetTrafficPolicyResponseTrafficPolicyTypeDef
):
    """
    Type definition for `ClientGetTrafficPolicyResponse` `TrafficPolicy`

    A complex type that contains settings for the specified traffic policy.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to a traffic policy when you created it.

    - **Version** *(integer) --*

      The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
      policy, the value of ``Version`` is always 1.

    - **Name** *(string) --*

      The name that you specified when you created the traffic policy.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **Document** *(string) --*

      The definition of a traffic policy in JSON format. You specify the JSON document to use for
      a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
      JSON format, see `Traffic Policy Document Format
      <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
      .

    - **Comment** *(string) --*

      The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientGetTrafficPolicyResponseTypeDef = TypedDict(
    "_ClientGetTrafficPolicyResponseTypeDef",
    {"TrafficPolicy": ClientGetTrafficPolicyResponseTrafficPolicyTypeDef},
    total=False,
)


class ClientGetTrafficPolicyResponseTypeDef(_ClientGetTrafficPolicyResponseTypeDef):
    """
    Type definition for `ClientGetTrafficPolicy` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the specified traffic policy.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.

      - **Version** *(integer) --*

        The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
        policy, the value of ``Version`` is always 1.

      - **Name** *(string) --*

        The name that you specified when you created the traffic policy.

      - **Type** *(string) --*

        The DNS type of the resource record sets that Amazon Route 53 creates when you use a
        traffic policy to create a traffic policy instance.

      - **Document** *(string) --*

        The definition of a traffic policy in JSON format. You specify the JSON document to use for
        a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
        JSON format, see `Traffic Policy Document Format
        <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
        .

      - **Comment** *(string) --*

        The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef = TypedDict(
    "_ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)


class ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef(
    _ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef
):
    """
    Type definition for `ClientListGeoLocationsResponse` `GeoLocationDetailsList`

    A complex type that contains the codes and full continent, country, and subdivision names
    for the specified ``geolocation`` code.

    - **ContinentCode** *(string) --*

      The two-letter code for the continent.

    - **ContinentName** *(string) --*

      The full name of the continent.

    - **CountryCode** *(string) --*

      The two-letter code for the country.

    - **CountryName** *(string) --*

      The name of the country.

    - **SubdivisionCode** *(string) --*

      The code for the subdivision. Route 53 currently supports only states in the United
      States.

    - **SubdivisionName** *(string) --*

      The full name of the subdivision. Route 53 currently supports only states in the United
      States.
    """


_ClientListGeoLocationsResponseTypeDef = TypedDict(
    "_ClientListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List[
            ClientListGeoLocationsResponseGeoLocationDetailsListTypeDef
        ],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListGeoLocationsResponseTypeDef(_ClientListGeoLocationsResponseTypeDef):
    """
    Type definition for `ClientListGeoLocations` `Response`

    A complex type containing the response information for the request.

    - **GeoLocationDetailsList** *(list) --*

      A complex type that contains one ``GeoLocationDetails`` element for each location that Amazon
      Route 53 supports for geolocation.

      - *(dict) --*

        A complex type that contains the codes and full continent, country, and subdivision names
        for the specified ``geolocation`` code.

        - **ContinentCode** *(string) --*

          The two-letter code for the continent.

        - **ContinentName** *(string) --*

          The full name of the continent.

        - **CountryCode** *(string) --*

          The two-letter code for the country.

        - **CountryName** *(string) --*

          The name of the country.

        - **SubdivisionCode** *(string) --*

          The code for the subdivision. Route 53 currently supports only states in the United
          States.

        - **SubdivisionName** *(string) --*

          The full name of the subdivision. Route 53 currently supports only states in the United
          States.

    - **IsTruncated** *(boolean) --*

      A value that indicates whether more locations remain to be listed after the last location in
      this response. If so, the value of ``IsTruncated`` is ``true`` . To get more values, submit
      another request and include the values of ``NextContinentCode`` , ``NextCountryCode`` , and
      ``NextSubdivisionCode`` in the ``startcontinentcode`` , ``startcountrycode`` , and
      ``startsubdivisioncode`` , as applicable.

    - **NextContinentCode** *(string) --*

      If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations.
      Enter the value of ``NextContinentCode`` in the ``startcontinentcode`` parameter in another
      ``ListGeoLocations`` request.

    - **NextCountryCode** *(string) --*

      If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations.
      Enter the value of ``NextCountryCode`` in the ``startcountrycode`` parameter in another
      ``ListGeoLocations`` request.

    - **NextSubdivisionCode** *(string) --*

      If ``IsTruncated`` is ``true`` , you can make a follow-up request to display more locations.
      Enter the value of ``NextSubdivisionCode`` in the ``startsubdivisioncode`` parameter in
      another ``ListGeoLocations`` request.

    - **MaxItems** *(string) --*

      The value that you specified for ``MaxItems`` in the request.
    """


_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfiguration` `Dimensions`

    For the metric that the CloudWatch alarm is associated with, a complex type that
    contains information about one dimension.

    - **Name** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the name of one
      dimension.

    - **Value** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the value of one
      dimension.
    """


_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "Dimensions": List[
            ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef(
    _ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponseHealthChecks` `CloudWatchAlarmConfiguration`

    A complex type that contains information about the CloudWatch alarm that Amazon Route 53
    is monitoring for this health check.

    - **EvaluationPeriods** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the number of periods that
      the metric is compared to the threshold.

    - **Threshold** *(float) --*

      For the metric that the CloudWatch alarm is associated with, the value the metric is
      compared with.

    - **ComparisonOperator** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the arithmetic operation
      that is used for the comparison.

    - **Period** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the duration of one
      evaluation period in seconds.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that the alarm is associated with.

    - **Namespace** *(string) --*

      The namespace of the metric that the alarm is associated with. For more information,
      see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

    - **Statistic** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the statistic that is
      applied to the metric.

    - **Dimensions** *(list) --*

      For the metric that the CloudWatch alarm is associated with, a complex type that
      contains information about the dimensions for the metric. For information, see `Amazon
      CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

      - *(dict) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about one dimension.

        - **Name** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the name of one
          dimension.

        - **Value** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the value of one
          dimension.
    """


_ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
    total=False,
)


class ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponseHealthChecksHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
    health checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --*

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine
      whether this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
      Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --*

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
      to determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
        aren't supported.
    """


_ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": str,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ClientListHealthChecksResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef(
    _ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponseHealthChecks` `HealthCheckConfig`

    A complex type that contains detailed information about one health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
      health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
      request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
      the interval that you specify in ``RequestInterval`` . Using an IP address returned by
      DNS, Route 53 then checks the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
      example, ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
      for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
      addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for
      ``IPAddress`` . This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is
      in local, private, non-routable, or multicast ranges. For more information about IP
      addresses for which you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
      ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.
      Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Amazon Route 53
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

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
         v1.0 or later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
      body for the string that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
      response body for the string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
      the state of the alarm is ``OK`` , the health check is considered healthy. If the state
      is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
      sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
      check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
      , ``Unhealthy`` , or ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks,
      Route 53 adds up the number of health checks that Route 53 health checkers consider to
      be healthy and compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health
      checks. The path can be any value for which your endpoint will return an HTTP status
      code of 2xx or 3xx when the endpoint is healthy, for example, the file
      /docs/route53-health-check.html. You can also include query string parameters, for
      example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
      passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
      checks except TCP health checks. This is typically the fully qualified DNS name of the
      endpoint on which you want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
      header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
      for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
      endpoint in the ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
      Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
      header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
      the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for
      ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
      Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
        health checks to the endpoint. If there's no resource record set with a type of A for
        the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
        with a "DNS resolution failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets
      and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
      recommend that you create a separate health check for each endpoint. For example,
      create a health check for each HTTP server that is serving content for www.example.com.
      For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
      (such as us-east-2-www.example.com), not the name of the resource record sets
      (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
        then associate the health check with those resource record sets, health check results
        will be unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
      value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
      ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
      want Amazon Route 53 to search for in the response body from the specified resource. If
      the string appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your
      endpoint and the time that it sends the next health check request. Each Route 53 health
      checker makes requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30``
      seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon
      Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
      versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
      Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three
      health checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers
      in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
      the **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for
      example, to consider a health check unhealthy when it otherwise would be considered
      healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's
      what happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting
      requests to your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
      health checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
      corresponding CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to
      always be healthy. If you configured DNS failover, Route 53 continues to route traffic
      to the corresponding resources. If you want to stop routing traffic to a resource,
      change the value of `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more
      information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health
      check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
      be considered healthy. To specify the child health checks that you want to associate
      with a ``CALCULATED`` health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53
      always considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
      element for each health check that you want to associate with a ``CALCULATED`` health
      check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of
      ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
      negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
      with the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the
      ``client_hello`` message. If you don't enable SNI, the status of the health check will
      be ``SSL alert handshake_failure`` . A health check can also have that status for other
      reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
      configuration on your endpoint and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
      field and possibly several more in the ``Subject Alternative Names`` field. One of the
      domain names in the certificate should match the value that you specify for
      ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
      with a certificate that does not include the domain name that you specified in
      ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
      attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
      ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want
      Amazon Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs
      checks from all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks,
      Route 53 will briefly continue to perform checks from that region to ensure that some
      health checkers are always checking the endpoint (for example, if you replace three
      regions with four different regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
      health checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --*

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine
        whether this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
        Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --*

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
        to determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
          aren't supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state,
      the status that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
      that CloudWatch had sufficient data to determine the alarm state. For new health checks
      that have no last known status, the default status for the health check is healthy.
    """


_ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef(
    _ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponseHealthChecks` `LinkedService`

    If the health check was created by another service, the service that created the health
    check. When a health check is created by another service, you can't edit or delete it
    using Amazon Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientListHealthChecksResponseHealthChecksTypeDef = TypedDict(
    "_ClientListHealthChecksResponseHealthChecksTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientListHealthChecksResponseHealthChecksLinkedServiceTypeDef,
        "HealthCheckConfig": ClientListHealthChecksResponseHealthChecksHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientListHealthChecksResponseHealthChecksCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientListHealthChecksResponseHealthChecksTypeDef(
    _ClientListHealthChecksResponseHealthChecksTypeDef
):
    """
    Type definition for `ClientListHealthChecksResponse` `HealthChecks`

    A complex type that contains information about one health check that is associated with the
    current AWS account.

    - **Id** *(string) --*

      The identifier that Amazon Route 53assigned to the health check when you created it. When
      you add or update a resource record set, you use this value to specify which health check
      to use. The value can be up to 64 characters long.

    - **CallerReference** *(string) --*

      A unique string that you specified when you created the health check.

    - **LinkedService** *(dict) --*

      If the health check was created by another service, the service that created the health
      check. When a health check is created by another service, you can't edit or delete it
      using Amazon Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.

    - **HealthCheckConfig** *(dict) --*

      A complex type that contains detailed information about one health check.

      - **IPAddress** *(string) --*

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
        health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
        request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
        the interval that you specify in ``RequestInterval`` . Using an IP address returned by
        DNS, Route 53 then checks the health of the endpoint.

        Use one of the following formats for the value of ``IPAddress`` :

        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
        example, ``192.0.2.44`` .

        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
        for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
        addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
        associate it with your EC2 instance, and specify the Elastic IP address for
        ``IPAddress`` . This ensures that the IP address of your instance will never change.

        For more information, see `FullyQualifiedDomainName
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
        .

        Constraints: Route 53 can't check the health of endpoints for which the IP address is
        in local, private, non-routable, or multicast ranges. For more information about IP
        addresses for which you can't create health checks, see the following documents:

        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
        <https://tools.ietf.org/html/rfc6598>`__

        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
        ``IPAddress`` .

      - **Port** *(integer) --*

        The port on the endpoint on which you want Amazon Route 53 to perform health checks.
        Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Amazon Route 53
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

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
           v1.0 or later.

        * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
        body for the string that you specify in ``SearchString`` .

        * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
        response body for the string that you specify in ``SearchString`` .

        * **TCP** : Route 53 tries to establish a TCP connection.

        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
        the state of the alarm is ``OK`` , the health check is considered healthy. If the state
        is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
        sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
        check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
        , ``Unhealthy`` , or ``LastKnownStatus`` .

        * **CALCULATED** : For health checks that monitor the status of other health checks,
        Route 53 adds up the number of health checks that Route 53 health checkers consider to
        be healthy and compares that number with the value of ``HealthThreshold`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path, if any, that you want Amazon Route 53 to request when performing health
        checks. The path can be any value for which your endpoint will return an HTTP status
        code of 2xx or 3xx when the endpoint is healthy, for example, the file
        /docs/route53-health-check.html. You can also include query string parameters, for
        example, ``/welcome.html?language=jp&login=y`` .

      - **FullyQualifiedDomainName** *(string) --*

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         **If you specify a value for**  ``IPAddress`` :

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
        passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
        checks except TCP health checks. This is typically the fully qualified DNS name of the
        endpoint on which you want Route 53 to perform health checks.

        When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
        header:

        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the Host header.

        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
        for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
        endpoint in the ``Host`` header.

        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
        Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
        header.

        If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
        the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         **If you don't specify a value for ``IPAddress`` ** :

        Route 53 sends a DNS request to the domain that you specify for
        ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
        Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

        .. note::

          If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
          health checks to the endpoint. If there's no resource record set with a type of A for
          the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
          with a "DNS resolution failed" error.

        If you want to check the health of weighted, latency, or failover resource record sets
        and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
        recommend that you create a separate health check for each endpoint. For example,
        create a health check for each HTTP server that is serving content for www.example.com.
        For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
        (such as us-east-2-www.example.com), not the name of the resource record sets
        (www.example.com).

        .. warning::

          In this configuration, if you create a health check for which the value of
          ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
          then associate the health check with those resource record sets, health check results
          will be unpredictable.

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
        ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
        ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
        value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
        ``Host`` header.

      - **SearchString** *(string) --*

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
        want Amazon Route 53 to search for in the response body from the specified resource. If
        the string appears in the response body, Route 53 considers the resource healthy.

        Route 53 considers case when searching for ``SearchString`` in the response body.

      - **RequestInterval** *(integer) --*

        The number of seconds between the time that Amazon Route 53 gets a response from your
        endpoint and the time that it sends the next health check request. Each Route 53 health
        checker makes requests at this interval.

        .. warning::

          You can't change the value of ``RequestInterval`` after you create a health check.

        If you don't specify a value for ``RequestInterval`` , the default value is ``30``
        seconds.

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Amazon
        Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
        versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
        Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

        If you don't specify a value for ``FailureThreshold`` , the default value is three
        health checks.

      - **MeasureLatency** *(boolean) --*

        Specify whether you want Amazon Route 53 to measure the latency between health checkers
        in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
        the **Health Checks** page in the Route 53 console.

        .. warning::

          You can't change the value of ``MeasureLatency`` after you create a health check.

      - **Inverted** *(boolean) --*

        Specify whether you want Amazon Route 53 to invert the status of a health check, for
        example, to consider a health check unhealthy when it otherwise would be considered
        healthy.

      - **Disabled** *(boolean) --*

        Stops Route 53 from performing health checks. When you disable a health check, here's
        what happens:

        * **Health checks that check the health of endpoints:** Route 53 stops submitting
        requests to your application, server, or other resource.

        * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
        health checks.

        * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
        corresponding CloudWatch metrics.

        After you disable a health check, Route 53 considers the status of the health check to
        always be healthy. If you configured DNS failover, Route 53 continues to route traffic
        to the corresponding resources. If you want to stop routing traffic to a resource,
        change the value of `Inverted
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
        .

        Charges for a health check still apply when the health check is disabled. For more
        information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

      - **HealthThreshold** *(integer) --*

        The number of child health checks that are associated with a ``CALCULATED`` health
        check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
        be considered healthy. To specify the child health checks that you want to associate
        with a ``CALCULATED`` health check, use the `ChildHealthChecks
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
        element.

        Note the following:

        * If you specify a number greater than the number of child health checks, Route 53
        always considers this health check to be unhealthy.

        * If you specify ``0`` , Route 53 always considers this health check to be healthy.

      - **ChildHealthChecks** *(list) --*

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
        element for each health check that you want to associate with a ``CALCULATED`` health
        check.

        - *(string) --*

      - **EnableSNI** *(boolean) --*

        Specify whether you want Amazon Route 53 to send the value of
        ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
        negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
        with the applicable SSL/TLS certificate.

        Some endpoints require that ``HTTPS`` requests include the host name in the
        ``client_hello`` message. If you don't enable SNI, the status of the health check will
        be ``SSL alert handshake_failure`` . A health check can also have that status for other
        reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
        configuration on your endpoint and confirm that your certificate is valid.

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
        field and possibly several more in the ``Subject Alternative Names`` field. One of the
        domain names in the certificate should match the value that you specify for
        ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
        with a certificate that does not include the domain name that you specified in
        ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
        attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
        ``client_hello`` message.

      - **Regions** *(list) --*

        A complex type that contains one ``Region`` element for each region from which you want
        Amazon Route 53 health checkers to check the specified endpoint.

        If you don't specify any regions, Route 53 health checkers automatically performs
        checks from all of the regions that are listed under **Valid Values** .

        If you update a health check to remove a region that has been performing health checks,
        Route 53 will briefly continue to perform checks from that region to ensure that some
        health checkers are always checking the endpoint (for example, if you replace three
        regions with four different regions).

        - *(string) --*

      - **AlarmIdentifier** *(dict) --*

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
        health checkers to use to determine whether the specified health check is healthy.

        - **Region** *(string) --*

          For the CloudWatch alarm that you want Route 53 health checkers to use to determine
          whether this health check is healthy, the region that the alarm was created in.

          For the current list of CloudWatch regions, see `Amazon CloudWatch
          <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
          Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        - **Name** *(string) --*

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
          to determine whether this health check is healthy.

          .. note::

            Route 53 supports CloudWatch alarms with the following features:

            * Standard-resolution metrics. High-resolution metrics aren't supported. For more
            information, see `High-Resolution Metrics
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
            in the *Amazon CloudWatch User Guide* .

            * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
            aren't supported.

      - **InsufficientDataHealthStatus** *(string) --*

        When CloudWatch has insufficient data about the metric to determine the alarm state,
        the status that you want Amazon Route 53 to assign to the health check:

        * ``Healthy`` : Route 53 considers the health check to be healthy.

        * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

        * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
        that CloudWatch had sufficient data to determine the alarm state. For new health checks
        that have no last known status, the default status for the health check is healthy.

    - **HealthCheckVersion** *(integer) --*

      The version of the health check. You can optionally pass this value in a call to
      ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

    - **CloudWatchAlarmConfiguration** *(dict) --*

      A complex type that contains information about the CloudWatch alarm that Amazon Route 53
      is monitoring for this health check.

      - **EvaluationPeriods** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the number of periods that
        the metric is compared to the threshold.

      - **Threshold** *(float) --*

        For the metric that the CloudWatch alarm is associated with, the value the metric is
        compared with.

      - **ComparisonOperator** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the arithmetic operation
        that is used for the comparison.

      - **Period** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the duration of one
        evaluation period in seconds.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that the alarm is associated with.

      - **Namespace** *(string) --*

        The namespace of the metric that the alarm is associated with. For more information,
        see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

      - **Statistic** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the statistic that is
        applied to the metric.

      - **Dimensions** *(list) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about the dimensions for the metric. For information, see `Amazon
        CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        - *(dict) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that
          contains information about one dimension.

          - **Name** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the name of one
            dimension.

          - **Value** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the value of one
            dimension.
    """


_ClientListHealthChecksResponseTypeDef = TypedDict(
    "_ClientListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List[ClientListHealthChecksResponseHealthChecksTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHealthChecksResponseTypeDef(_ClientListHealthChecksResponseTypeDef):
    """
    Type definition for `ClientListHealthChecks` `Response`

    A complex type that contains the response to a ``ListHealthChecks`` request.

    - **HealthChecks** *(list) --*

      A complex type that contains one ``HealthCheck`` element for each health check that is
      associated with the current AWS account.

      - *(dict) --*

        A complex type that contains information about one health check that is associated with the
        current AWS account.

        - **Id** *(string) --*

          The identifier that Amazon Route 53assigned to the health check when you created it. When
          you add or update a resource record set, you use this value to specify which health check
          to use. The value can be up to 64 characters long.

        - **CallerReference** *(string) --*

          A unique string that you specified when you created the health check.

        - **LinkedService** *(dict) --*

          If the health check was created by another service, the service that created the health
          check. When a health check is created by another service, you can't edit or delete it
          using Amazon Route 53.

          - **ServicePrincipal** *(string) --*

            If the health check or hosted zone was created by another service, the service that
            created the resource. When a resource is created by another service, you can't edit or
            delete it using Amazon Route 53.

          - **Description** *(string) --*

            If the health check or hosted zone was created by another service, an optional
            description that can be provided by the other service. When a resource is created by
            another service, you can't edit or delete it using Amazon Route 53.

        - **HealthCheckConfig** *(dict) --*

          A complex type that contains detailed information about one health check.

          - **IPAddress** *(string) --*

            The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
            health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
            request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
            the interval that you specify in ``RequestInterval`` . Using an IP address returned by
            DNS, Route 53 then checks the health of the endpoint.

            Use one of the following formats for the value of ``IPAddress`` :

            * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
            example, ``192.0.2.44`` .

            * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
            for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
            addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

            If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
            associate it with your EC2 instance, and specify the Elastic IP address for
            ``IPAddress`` . This ensures that the IP address of your instance will never change.

            For more information, see `FullyQualifiedDomainName
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
            .

            Constraints: Route 53 can't check the health of endpoints for which the IP address is
            in local, private, non-routable, or multicast ranges. For more information about IP
            addresses for which you can't create health checks, see the following documents:

            * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

            * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
            <https://tools.ietf.org/html/rfc6598>`__

            * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

            When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
            ``IPAddress`` .

          - **Port** *(integer) --*

            The port on the endpoint on which you want Amazon Route 53 to perform health checks.
            Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

          - **Type** *(string) --*

            The type of health check that you want to create, which indicates how Amazon Route 53
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

               If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
               v1.0 or later.

            * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
            Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
            body for the string that you specify in ``SearchString`` .

            * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
            Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
            response body for the string that you specify in ``SearchString`` .

            * **TCP** : Route 53 tries to establish a TCP connection.

            * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
            the state of the alarm is ``OK`` , the health check is considered healthy. If the state
            is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
            sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
            check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
            , ``Unhealthy`` , or ``LastKnownStatus`` .

            * **CALCULATED** : For health checks that monitor the status of other health checks,
            Route 53 adds up the number of health checks that Route 53 health checkers consider to
            be healthy and compares that number with the value of ``HealthThreshold`` .

            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Amazon Route 53 Developer Guide* .

          - **ResourcePath** *(string) --*

            The path, if any, that you want Amazon Route 53 to request when performing health
            checks. The path can be any value for which your endpoint will return an HTTP status
            code of 2xx or 3xx when the endpoint is healthy, for example, the file
            /docs/route53-health-check.html. You can also include query string parameters, for
            example, ``/welcome.html?language=jp&login=y`` .

          - **FullyQualifiedDomainName** *(string) --*

            Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

             **If you specify a value for**  ``IPAddress`` :

            Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
            passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
            checks except TCP health checks. This is typically the fully qualified DNS name of the
            endpoint on which you want Route 53 to perform health checks.

            When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
            header:

            * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
            ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
            the Host header.

            * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
            for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
            endpoint in the ``Host`` header.

            * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
            Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
            header.

            If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
            the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

             **If you don't specify a value for ``IPAddress`` ** :

            Route 53 sends a DNS request to the domain that you specify for
            ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
            Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

            .. note::

              If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
              health checks to the endpoint. If there's no resource record set with a type of A for
              the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
              with a "DNS resolution failed" error.

            If you want to check the health of weighted, latency, or failover resource record sets
            and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
            recommend that you create a separate health check for each endpoint. For example,
            create a health check for each HTTP server that is serving content for www.example.com.
            For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
            (such as us-east-2-www.example.com), not the name of the resource record sets
            (www.example.com).

            .. warning::

              In this configuration, if you create a health check for which the value of
              ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
              then associate the health check with those resource record sets, health check results
              will be unpredictable.

            In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
            ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
            ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
            value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
            ``Host`` header.

          - **SearchString** *(string) --*

            If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
            want Amazon Route 53 to search for in the response body from the specified resource. If
            the string appears in the response body, Route 53 considers the resource healthy.

            Route 53 considers case when searching for ``SearchString`` in the response body.

          - **RequestInterval** *(integer) --*

            The number of seconds between the time that Amazon Route 53 gets a response from your
            endpoint and the time that it sends the next health check request. Each Route 53 health
            checker makes requests at this interval.

            .. warning::

              You can't change the value of ``RequestInterval`` after you create a health check.

            If you don't specify a value for ``RequestInterval`` , the default value is ``30``
            seconds.

          - **FailureThreshold** *(integer) --*

            The number of consecutive health checks that an endpoint must pass or fail for Amazon
            Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
            versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
            Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Amazon Route 53 Developer Guide* .

            If you don't specify a value for ``FailureThreshold`` , the default value is three
            health checks.

          - **MeasureLatency** *(boolean) --*

            Specify whether you want Amazon Route 53 to measure the latency between health checkers
            in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
            the **Health Checks** page in the Route 53 console.

            .. warning::

              You can't change the value of ``MeasureLatency`` after you create a health check.

          - **Inverted** *(boolean) --*

            Specify whether you want Amazon Route 53 to invert the status of a health check, for
            example, to consider a health check unhealthy when it otherwise would be considered
            healthy.

          - **Disabled** *(boolean) --*

            Stops Route 53 from performing health checks. When you disable a health check, here's
            what happens:

            * **Health checks that check the health of endpoints:** Route 53 stops submitting
            requests to your application, server, or other resource.

            * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
            health checks.

            * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
            corresponding CloudWatch metrics.

            After you disable a health check, Route 53 considers the status of the health check to
            always be healthy. If you configured DNS failover, Route 53 continues to route traffic
            to the corresponding resources. If you want to stop routing traffic to a resource,
            change the value of `Inverted
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
            .

            Charges for a health check still apply when the health check is disabled. For more
            information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

          - **HealthThreshold** *(integer) --*

            The number of child health checks that are associated with a ``CALCULATED`` health
            check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
            be considered healthy. To specify the child health checks that you want to associate
            with a ``CALCULATED`` health check, use the `ChildHealthChecks
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
            element.

            Note the following:

            * If you specify a number greater than the number of child health checks, Route 53
            always considers this health check to be unhealthy.

            * If you specify ``0`` , Route 53 always considers this health check to be healthy.

          - **ChildHealthChecks** *(list) --*

            (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
            element for each health check that you want to associate with a ``CALCULATED`` health
            check.

            - *(string) --*

          - **EnableSNI** *(boolean) --*

            Specify whether you want Amazon Route 53 to send the value of
            ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
            negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
            with the applicable SSL/TLS certificate.

            Some endpoints require that ``HTTPS`` requests include the host name in the
            ``client_hello`` message. If you don't enable SNI, the status of the health check will
            be ``SSL alert handshake_failure`` . A health check can also have that status for other
            reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
            configuration on your endpoint and confirm that your certificate is valid.

            The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
            field and possibly several more in the ``Subject Alternative Names`` field. One of the
            domain names in the certificate should match the value that you specify for
            ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
            with a certificate that does not include the domain name that you specified in
            ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
            attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
            ``client_hello`` message.

          - **Regions** *(list) --*

            A complex type that contains one ``Region`` element for each region from which you want
            Amazon Route 53 health checkers to check the specified endpoint.

            If you don't specify any regions, Route 53 health checkers automatically performs
            checks from all of the regions that are listed under **Valid Values** .

            If you update a health check to remove a region that has been performing health checks,
            Route 53 will briefly continue to perform checks from that region to ensure that some
            health checkers are always checking the endpoint (for example, if you replace three
            regions with four different regions).

            - *(string) --*

          - **AlarmIdentifier** *(dict) --*

            A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
            health checkers to use to determine whether the specified health check is healthy.

            - **Region** *(string) --*

              For the CloudWatch alarm that you want Route 53 health checkers to use to determine
              whether this health check is healthy, the region that the alarm was created in.

              For the current list of CloudWatch regions, see `Amazon CloudWatch
              <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
              Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

            - **Name** *(string) --*

              The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
              to determine whether this health check is healthy.

              .. note::

                Route 53 supports CloudWatch alarms with the following features:

                * Standard-resolution metrics. High-resolution metrics aren't supported. For more
                information, see `High-Resolution Metrics
                <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
                in the *Amazon CloudWatch User Guide* .

                * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
                aren't supported.

          - **InsufficientDataHealthStatus** *(string) --*

            When CloudWatch has insufficient data about the metric to determine the alarm state,
            the status that you want Amazon Route 53 to assign to the health check:

            * ``Healthy`` : Route 53 considers the health check to be healthy.

            * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

            * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
            that CloudWatch had sufficient data to determine the alarm state. For new health checks
            that have no last known status, the default status for the health check is healthy.

        - **HealthCheckVersion** *(integer) --*

          The version of the health check. You can optionally pass this value in a call to
          ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

        - **CloudWatchAlarmConfiguration** *(dict) --*

          A complex type that contains information about the CloudWatch alarm that Amazon Route 53
          is monitoring for this health check.

          - **EvaluationPeriods** *(integer) --*

            For the metric that the CloudWatch alarm is associated with, the number of periods that
            the metric is compared to the threshold.

          - **Threshold** *(float) --*

            For the metric that the CloudWatch alarm is associated with, the value the metric is
            compared with.

          - **ComparisonOperator** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the arithmetic operation
            that is used for the comparison.

          - **Period** *(integer) --*

            For the metric that the CloudWatch alarm is associated with, the duration of one
            evaluation period in seconds.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that the alarm is associated with.

          - **Namespace** *(string) --*

            The namespace of the metric that the alarm is associated with. For more information,
            see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
            in the *Amazon CloudWatch User Guide* .

          - **Statistic** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the statistic that is
            applied to the metric.

          - **Dimensions** *(list) --*

            For the metric that the CloudWatch alarm is associated with, a complex type that
            contains information about the dimensions for the metric. For information, see `Amazon
            CloudWatch Namespaces, Dimensions, and Metrics Reference
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
            in the *Amazon CloudWatch User Guide* .

            - *(dict) --*

              For the metric that the CloudWatch alarm is associated with, a complex type that
              contains information about one dimension.

              - **Name** *(string) --*

                For the metric that the CloudWatch alarm is associated with, the name of one
                dimension.

              - **Value** *(string) --*

                For the metric that the CloudWatch alarm is associated with, the value of one
                dimension.

    - **Marker** *(string) --*

      For the second and subsequent calls to ``ListHealthChecks`` , ``Marker`` is the value that
      you specified for the ``marker`` parameter in the previous request.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more health checks to be listed. If the response was
      truncated, you can get the next group of health checks by submitting another
      ``ListHealthChecks`` request and specifying the value of ``NextMarker`` in the ``marker``
      parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the first health
      check that Amazon Route 53 returns if you submit another ``ListHealthChecks`` request and
      specify the value of ``NextMarker`` in the ``marker`` parameter.

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListHealthChecks`` that produced the current response.
    """


_ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef
):
    """
    Type definition for `ClientListHostedZonesByNameResponseHostedZones` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef
):
    """
    Type definition for `ClientListHostedZonesByNameResponseHostedZones` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientListHostedZonesByNameResponseHostedZonesTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesByNameResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesByNameResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ClientListHostedZonesByNameResponseHostedZonesTypeDef(
    _ClientListHostedZonesByNameResponseHostedZonesTypeDef
):
    """
    Type definition for `ClientListHostedZonesByNameResponse` `HostedZones`

    A complex type that contains general information about the hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have
      registered with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientListHostedZonesByNameResponseTypeDef = TypedDict(
    "_ClientListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesByNameResponseHostedZonesTypeDef],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHostedZonesByNameResponseTypeDef(
    _ClientListHostedZonesByNameResponseTypeDef
):
    """
    Type definition for `ClientListHostedZonesByName` `Response`

    A complex type that contains the response information for the request.

    - **HostedZones** *(list) --*

      A complex type that contains general information about the hosted zone.

      - *(dict) --*

        A complex type that contains general information about the hosted zone.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.

        - **Name** *(string) --*

          The name of the domain. For public hosted zones, this is the name that you have
          registered with your DNS registrar.

          For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
          (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

        - **CallerReference** *(string) --*

          The value that you specified for ``CallerReference`` when you created the hosted zone.

        - **Config** *(dict) --*

          A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
          the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
          ``Comment`` elements don't appear in the response.

          - **Comment** *(string) --*

            Any comments that you want to include about the hosted zone.

          - **PrivateZone** *(boolean) --*

            A value that indicates whether this is a private hosted zone.

        - **ResourceRecordSetCount** *(integer) --*

          The number of resource record sets in the hosted zone.

        - **LinkedService** *(dict) --*

          If the hosted zone was created by another service, the service that created the hosted
          zone. When a hosted zone is created by another service, you can't edit or delete it using
          Route 53.

          - **ServicePrincipal** *(string) --*

            If the health check or hosted zone was created by another service, the service that
            created the resource. When a resource is created by another service, you can't edit or
            delete it using Amazon Route 53.

          - **Description** *(string) --*

            If the health check or hosted zone was created by another service, an optional
            description that can be provided by the other service. When a resource is created by
            another service, you can't edit or delete it using Amazon Route 53.

    - **DNSName** *(string) --*

      For the second and subsequent calls to ``ListHostedZonesByName`` , ``DNSName`` is the value
      that you specified for the ``dnsname`` parameter in the request that produced the current
      response.

    - **HostedZoneId** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more hosted zones to be listed. If the response was
      truncated, you can get the next group of ``maxitems`` hosted zones by calling
      ``ListHostedZonesByName`` again and specifying the values of ``NextDNSName`` and
      ``NextHostedZoneId`` elements in the ``dnsname`` and ``hostedzoneid`` parameters.

    - **NextDNSName** *(string) --*

      If ``IsTruncated`` is true, the value of ``NextDNSName`` is the name of the first hosted zone
      in the next group of ``maxitems`` hosted zones. Call ``ListHostedZonesByName`` again and
      specify the value of ``NextDNSName`` and ``NextHostedZoneId`` in the ``dnsname`` and
      ``hostedzoneid`` parameters, respectively.

      This element is present only if ``IsTruncated`` is ``true`` .

    - **NextHostedZoneId** *(string) --*

      If ``IsTruncated`` is ``true`` , the value of ``NextHostedZoneId`` identifies the first
      hosted zone in the next group of ``maxitems`` hosted zones. Call ``ListHostedZonesByName``
      again and specify the value of ``NextDNSName`` and ``NextHostedZoneId`` in the ``dnsname``
      and ``hostedzoneid`` parameters, respectively.

      This element is present only if ``IsTruncated`` is ``true`` .

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListHostedZonesByName`` that produced the current response.
    """


_ClientListHostedZonesResponseHostedZonesConfigTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientListHostedZonesResponseHostedZonesConfigTypeDef(
    _ClientListHostedZonesResponseHostedZonesConfigTypeDef
):
    """
    Type definition for `ClientListHostedZonesResponseHostedZones` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef(
    _ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef
):
    """
    Type definition for `ClientListHostedZonesResponseHostedZones` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientListHostedZonesResponseHostedZonesTypeDef = TypedDict(
    "_ClientListHostedZonesResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientListHostedZonesResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientListHostedZonesResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ClientListHostedZonesResponseHostedZonesTypeDef(
    _ClientListHostedZonesResponseHostedZonesTypeDef
):
    """
    Type definition for `ClientListHostedZonesResponse` `HostedZones`

    A complex type that contains general information about the hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have
      registered with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientListHostedZonesResponseTypeDef = TypedDict(
    "_ClientListHostedZonesResponseTypeDef",
    {
        "HostedZones": List[ClientListHostedZonesResponseHostedZonesTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListHostedZonesResponseTypeDef(_ClientListHostedZonesResponseTypeDef):
    """
    Type definition for `ClientListHostedZones` `Response`

    - **HostedZones** *(list) --*

      A complex type that contains general information about the hosted zone.

      - *(dict) --*

        A complex type that contains general information about the hosted zone.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.

        - **Name** *(string) --*

          The name of the domain. For public hosted zones, this is the name that you have
          registered with your DNS registrar.

          For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
          (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

        - **CallerReference** *(string) --*

          The value that you specified for ``CallerReference`` when you created the hosted zone.

        - **Config** *(dict) --*

          A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
          the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
          ``Comment`` elements don't appear in the response.

          - **Comment** *(string) --*

            Any comments that you want to include about the hosted zone.

          - **PrivateZone** *(boolean) --*

            A value that indicates whether this is a private hosted zone.

        - **ResourceRecordSetCount** *(integer) --*

          The number of resource record sets in the hosted zone.

        - **LinkedService** *(dict) --*

          If the hosted zone was created by another service, the service that created the hosted
          zone. When a hosted zone is created by another service, you can't edit or delete it using
          Route 53.

          - **ServicePrincipal** *(string) --*

            If the health check or hosted zone was created by another service, the service that
            created the resource. When a resource is created by another service, you can't edit or
            delete it using Amazon Route 53.

          - **Description** *(string) --*

            If the health check or hosted zone was created by another service, an optional
            description that can be provided by the other service. When a resource is created by
            another service, you can't edit or delete it using Amazon Route 53.

    - **Marker** *(string) --*

      For the second and subsequent calls to ``ListHostedZones`` , ``Marker`` is the value that you
      specified for the ``marker`` parameter in the request that produced the current response.

    - **IsTruncated** *(boolean) --*

      A flag indicating whether there are more hosted zones to be listed. If the response was
      truncated, you can get more hosted zones by submitting another ``ListHostedZones`` request
      and specifying the value of ``NextMarker`` in the ``marker`` parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the first hosted zone
      in the next group of hosted zones. Submit another ``ListHostedZones`` request, and specify
      the value of ``NextMarker`` from the response in the ``marker`` parameter.

      This element is present only if ``IsTruncated`` is ``true`` .

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListHostedZones`` that produced the current response.
    """


_ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef = TypedDict(
    "_ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef(
    _ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef
):
    """
    Type definition for `ClientListQueryLoggingConfigsResponse` `QueryLoggingConfigs`

    A complex type that contains information about a configuration for DNS query logging.

    - **Id** *(string) --*

      The ID for a configuration for DNS query logging.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that CloudWatch Logs is logging queries for.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
      publishing logs to.
    """


_ClientListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_ClientListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List[
            ClientListQueryLoggingConfigsResponseQueryLoggingConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListQueryLoggingConfigsResponseTypeDef(
    _ClientListQueryLoggingConfigsResponseTypeDef
):
    """
    Type definition for `ClientListQueryLoggingConfigs` `Response`

    - **QueryLoggingConfigs** *(list) --*

      An array that contains one `QueryLoggingConfig
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html>`__
      element for each configuration for DNS query logging that is associated with the current AWS
      account.

      - *(dict) --*

        A complex type that contains information about a configuration for DNS query logging.

        - **Id** *(string) --*

          The ID for a configuration for DNS query logging.

        - **HostedZoneId** *(string) --*

          The ID of the hosted zone that CloudWatch Logs is logging queries for.

        - **CloudWatchLogsLogGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
          publishing logs to.

    - **NextToken** *(string) --*

      If a response includes the last of the query logging configurations that are associated with
      the current AWS account, ``NextToken`` doesn't appear in the response.

      If a response doesn't include the last of the configurations, you can get more configurations
      by submitting another `ListQueryLoggingConfigs
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html>`__
      request. Get the value of ``NextToken`` that Amazon Route 53 returned in the previous
      response and include it in ``NextToken`` in the next request.
    """


_ClientListReusableDelegationSetsResponseDelegationSetsTypeDef = TypedDict(
    "_ClientListReusableDelegationSetsResponseDelegationSetsTypeDef",
    {"Id": str, "CallerReference": str, "NameServers": List[str]},
    total=False,
)


class ClientListReusableDelegationSetsResponseDelegationSetsTypeDef(
    _ClientListReusableDelegationSetsResponseDelegationSetsTypeDef
):
    """
    Type definition for `ClientListReusableDelegationSetsResponse` `DelegationSets`

    A complex type that lists the name servers in a delegation set, as well as the
    ``CallerReference`` and the ``ID`` for the delegation set.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigns to a reusable delegation set.

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the reusable
      delegation set.

    - **NameServers** *(list) --*

      A complex type that contains a list of the authoritative name servers for a hosted zone
      or for a reusable delegation set.

      - *(string) --*
    """


_ClientListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_ClientListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List[
            ClientListReusableDelegationSetsResponseDelegationSetsTypeDef
        ],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListReusableDelegationSetsResponseTypeDef(
    _ClientListReusableDelegationSetsResponseTypeDef
):
    """
    Type definition for `ClientListReusableDelegationSets` `Response`

    A complex type that contains information about the reusable delegation sets that are associated
    with the current AWS account.

    - **DelegationSets** *(list) --*

      A complex type that contains one ``DelegationSet`` element for each reusable delegation set
      that was created by the current AWS account.

      - *(dict) --*

        A complex type that lists the name servers in a delegation set, as well as the
        ``CallerReference`` and the ``ID`` for the delegation set.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigns to a reusable delegation set.

        - **CallerReference** *(string) --*

          The value that you specified for ``CallerReference`` when you created the reusable
          delegation set.

        - **NameServers** *(list) --*

          A complex type that contains a list of the authoritative name servers for a hosted zone
          or for a reusable delegation set.

          - *(string) --*

    - **Marker** *(string) --*

      For the second and subsequent calls to ``ListReusableDelegationSets`` , ``Marker`` is the
      value that you specified for the ``marker`` parameter in the request that produced the
      current response.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more reusable delegation sets to be listed.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , the value of ``NextMarker`` identifies the next reusable
      delegation set that Amazon Route 53 will return if you submit another
      ``ListReusableDelegationSets`` request and specify the value of ``NextMarker`` in the
      ``marker`` parameter.

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListReusableDelegationSets`` that produced the current response.
    """


_ClientListTagsForResourceResponseResourceTagSetTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagSetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseResourceTagSetTagsTypeDef(
    _ClientListTagsForResourceResponseResourceTagSetTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponseResourceTagSet` `Tags`

    A complex type that contains information about a tag that you want to add or edit for the
    specified health check or hosted zone.

    - **Key** *(string) --*

      The value of ``Key`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to
      give the new tag.

      * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value``
      for.

      * **Delete a key** : ``Key`` is the name of the tag you want to remove.

      * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
      Route 53 console, the list of your health checks includes a **Name** column that lets
      you see the name that you've given to each health check.

    - **Value** *(string) --*

      The value of ``Value`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want
      to give the new tag.

      * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTagsForResourceResponseResourceTagSetTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagSetTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourceResponseResourceTagSetTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseResourceTagSetTypeDef(
    _ClientListTagsForResourceResponseResourceTagSetTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `ResourceTagSet`

    A ``ResourceTagSet`` containing tags associated with the specified resource.

    - **ResourceType** *(string) --*

      The type of the resource.

      * The resource type for health checks is ``healthcheck`` .

      * The resource type for hosted zones is ``hostedzone`` .

    - **ResourceId** *(string) --*

      The ID for the specified resource.

    - **Tags** *(list) --*

      The tags associated with the specified resource.

      - *(dict) --*

        A complex type that contains information about a tag that you want to add or edit for the
        specified health check or hosted zone.

        - **Key** *(string) --*

          The value of ``Key`` depends on the operation that you want to perform:

          * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to
          give the new tag.

          * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value``
          for.

          * **Delete a key** : ``Key`` is the name of the tag you want to remove.

          * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
          Route 53 console, the list of your health checks includes a **Name** column that lets
          you see the name that you've given to each health check.

        - **Value** *(string) --*

          The value of ``Value`` depends on the operation that you want to perform:

          * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want
          to give the new tag.

          * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"ResourceTagSet": ClientListTagsForResourceResponseResourceTagSetTypeDef},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    A complex type that contains information about the health checks or hosted zones for which you
    want to list tags.

    - **ResourceTagSet** *(dict) --*

      A ``ResourceTagSet`` containing tags associated with the specified resource.

      - **ResourceType** *(string) --*

        The type of the resource.

        * The resource type for health checks is ``healthcheck`` .

        * The resource type for hosted zones is ``hostedzone`` .

      - **ResourceId** *(string) --*

        The ID for the specified resource.

      - **Tags** *(list) --*

        The tags associated with the specified resource.

        - *(dict) --*

          A complex type that contains information about a tag that you want to add or edit for the
          specified health check or hosted zone.

          - **Key** *(string) --*

            The value of ``Key`` depends on the operation that you want to perform:

            * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want to
            give the new tag.

            * **Edit a tag** : ``Key`` is the name of the tag that you want to change the ``Value``
            for.

            * **Delete a key** : ``Key`` is the name of the tag you want to remove.

            * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
            Route 53 console, the list of your health checks includes a **Name** column that lets
            you see the name that you've given to each health check.

          - **Value** *(string) --*

            The value of ``Value`` depends on the operation that you want to perform:

            * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you want
            to give the new tag.

            * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef(
    _ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourcesResponseResourceTagSets` `Tags`

    A complex type that contains information about a tag that you want to add or edit for
    the specified health check or hosted zone.

    - **Key** *(string) --*

      The value of ``Key`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want
      to give the new tag.

      * **Edit a tag** : ``Key`` is the name of the tag that you want to change the
      ``Value`` for.

      * **Delete a key** : ``Key`` is the name of the tag you want to remove.

      * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
      Route 53 console, the list of your health checks includes a **Name** column that lets
      you see the name that you've given to each health check.

    - **Value** *(string) --*

      The value of ``Value`` depends on the operation that you want to perform:

      * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you
      want to give the new tag.

      * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTagsForResourcesResponseResourceTagSetsTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseResourceTagSetsTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Tags": List[ClientListTagsForResourcesResponseResourceTagSetsTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourcesResponseResourceTagSetsTypeDef(
    _ClientListTagsForResourcesResponseResourceTagSetsTypeDef
):
    """
    Type definition for `ClientListTagsForResourcesResponse` `ResourceTagSets`

    A complex type containing a resource and its associated tags.

    - **ResourceType** *(string) --*

      The type of the resource.

      * The resource type for health checks is ``healthcheck`` .

      * The resource type for hosted zones is ``hostedzone`` .

    - **ResourceId** *(string) --*

      The ID for the specified resource.

    - **Tags** *(list) --*

      The tags associated with the specified resource.

      - *(dict) --*

        A complex type that contains information about a tag that you want to add or edit for
        the specified health check or hosted zone.

        - **Key** *(string) --*

          The value of ``Key`` depends on the operation that you want to perform:

          * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want
          to give the new tag.

          * **Edit a tag** : ``Key`` is the name of the tag that you want to change the
          ``Value`` for.

          * **Delete a key** : ``Key`` is the name of the tag you want to remove.

          * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
          Route 53 console, the list of your health checks includes a **Name** column that lets
          you see the name that you've given to each health check.

        - **Value** *(string) --*

          The value of ``Value`` depends on the operation that you want to perform:

          * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you
          want to give the new tag.

          * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTagsForResourcesResponseTypeDef = TypedDict(
    "_ClientListTagsForResourcesResponseTypeDef",
    {"ResourceTagSets": List[ClientListTagsForResourcesResponseResourceTagSetsTypeDef]},
    total=False,
)


class ClientListTagsForResourcesResponseTypeDef(
    _ClientListTagsForResourcesResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResources` `Response`

    A complex type containing tags for the specified resources.

    - **ResourceTagSets** *(list) --*

      A list of ``ResourceTagSet`` s containing tags associated with the specified resources.

      - *(dict) --*

        A complex type containing a resource and its associated tags.

        - **ResourceType** *(string) --*

          The type of the resource.

          * The resource type for health checks is ``healthcheck`` .

          * The resource type for hosted zones is ``hostedzone`` .

        - **ResourceId** *(string) --*

          The ID for the specified resource.

        - **Tags** *(list) --*

          The tags associated with the specified resource.

          - *(dict) --*

            A complex type that contains information about a tag that you want to add or edit for
            the specified health check or hosted zone.

            - **Key** *(string) --*

              The value of ``Key`` depends on the operation that you want to perform:

              * **Add a tag to a health check or hosted zone** : ``Key`` is the name that you want
              to give the new tag.

              * **Edit a tag** : ``Key`` is the name of the tag that you want to change the
              ``Value`` for.

              * **Delete a key** : ``Key`` is the name of the tag you want to remove.

              * **Give a name to a health check** : Edit the default ``Name`` tag. In the Amazon
              Route 53 console, the list of your health checks includes a **Name** column that lets
              you see the name that you've given to each health check.

            - **Value** *(string) --*

              The value of ``Value`` depends on the operation that you want to perform:

              * **Add a tag to a health check or hosted zone** : ``Value`` is the value that you
              want to give the new tag.

              * **Edit a tag** : ``Value`` is the new value that you want to assign the tag.
    """


_ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef = TypedDict(
    "_ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": str,
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
    total=False,
)


class ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef(
    _ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef
):
    """
    Type definition for `ClientListTrafficPoliciesResponse` `TrafficPolicySummaries`

    A complex type that contains information about the latest version of one traffic policy
    that is associated with the current AWS account.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the traffic policy when you created it.

    - **Name** *(string) --*

      The name that you specified for the traffic policy when you created it.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **LatestVersion** *(integer) --*

      The version number of the latest version of the traffic policy.

    - **TrafficPolicyCount** *(integer) --*

      The number of traffic policies that are associated with the current AWS account.
    """


_ClientListTrafficPoliciesResponseTypeDef = TypedDict(
    "_ClientListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List[
            ClientListTrafficPoliciesResponseTrafficPolicySummariesTypeDef
        ],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPoliciesResponseTypeDef(
    _ClientListTrafficPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListTrafficPolicies` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicySummaries** *(list) --*

      A list that contains one ``TrafficPolicySummary`` element for each traffic policy that was
      created by the current AWS account.

      - *(dict) --*

        A complex type that contains information about the latest version of one traffic policy
        that is associated with the current AWS account.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the traffic policy when you created it.

        - **Name** *(string) --*

          The name that you specified for the traffic policy when you created it.

        - **Type** *(string) --*

          The DNS type of the resource record sets that Amazon Route 53 creates when you use a
          traffic policy to create a traffic policy instance.

        - **LatestVersion** *(integer) --*

          The version number of the latest version of the traffic policy.

        - **TrafficPolicyCount** *(integer) --*

          The number of traffic policies that are associated with the current AWS account.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more traffic policies to be listed. If the response
      was truncated, you can get the next group of traffic policies by submitting another
      ``ListTrafficPolicies`` request and specifying the value of ``TrafficPolicyIdMarker`` in the
      ``TrafficPolicyIdMarker`` request parameter.

    - **TrafficPolicyIdMarker** *(string) --*

      If the value of ``IsTruncated`` is ``true`` , ``TrafficPolicyIdMarker`` is the ID of the
      first traffic policy in the next group of ``MaxItems`` traffic policies.

    - **MaxItems** *(string) --*

      The value that you specified for the ``MaxItems`` parameter in the ``ListTrafficPolicies``
      request that produced the current response.
    """


_ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstancesByHostedZoneResponse` `TrafficPolicyInstances`

    A complex type that contains settings for the new traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
      in the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated
      to all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
      confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
      to fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
      is another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record
      sets in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByHostedZoneResponseTrafficPolicyInstancesTypeDef
        ],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef(
    _ClientListTrafficPolicyInstancesByHostedZoneResponseTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstancesByHostedZone` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicyInstances** *(list) --*

      A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
      that matches the elements in the request.

      - *(dict) --*

        A complex type that contains settings for the new traffic policy instance.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.

        - **HostedZoneId** *(string) --*

          The ID of the hosted zone that Amazon Route 53 created resource record sets in.

        - **Name** *(string) --*

          The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
          using the resource record sets that are associated with this traffic policy instance.

        - **TTL** *(integer) --*

          The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
          in the specified hosted zone.

        - **State** *(string) --*

          The value of ``State`` is one of the following values:

            Applied

          Amazon Route 53 has finished creating resource record sets, and changes have propagated
          to all Route 53 edge locations.

            Creating

          Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
          confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

            Failed

          Route 53 wasn't able to create or update the resource record sets. When the value of
          ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
          to fail.

        - **Message** *(string) --*

          If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
          is another value, ``Message`` is empty.

        - **TrafficPolicyId** *(string) --*

          The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
          the specified hosted zone.

        - **TrafficPolicyVersion** *(integer) --*

          The version of the traffic policy that Amazon Route 53 used to create resource record
          sets in the specified hosted zone.

        - **TrafficPolicyType** *(string) --*

          The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
          created for this traffic policy instance.

    - **TrafficPolicyInstanceNameMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first
      traffic policy instance in the next group of traffic policy instances.

    - **TrafficPolicyInstanceTypeMarker** *(string) --*

      If ``IsTruncated`` is true, ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the
      resource record sets that are associated with the first traffic policy instance in the next
      group of traffic policy instances.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more traffic policy instances to be listed. If the
      response was truncated, you can get the next group of traffic policy instances by submitting
      another ``ListTrafficPolicyInstancesByHostedZone`` request and specifying the values of
      ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and
      ``TrafficPolicyInstanceTypeMarker`` in the corresponding request parameters.

    - **MaxItems** *(string) --*

      The value that you specified for the ``MaxItems`` parameter in the
      ``ListTrafficPolicyInstancesByHostedZone`` request that produced the current response.
    """


_ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstancesByPolicyResponse` `TrafficPolicyInstances`

    A complex type that contains settings for the new traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
      in the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated
      to all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
      confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
      to fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
      is another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record
      sets in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesByPolicyResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesByPolicyResponseTypeDef(
    _ClientListTrafficPolicyInstancesByPolicyResponseTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstancesByPolicy` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicyInstances** *(list) --*

      A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
      that matches the elements in the request.

      - *(dict) --*

        A complex type that contains settings for the new traffic policy instance.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.

        - **HostedZoneId** *(string) --*

          The ID of the hosted zone that Amazon Route 53 created resource record sets in.

        - **Name** *(string) --*

          The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
          using the resource record sets that are associated with this traffic policy instance.

        - **TTL** *(integer) --*

          The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
          in the specified hosted zone.

        - **State** *(string) --*

          The value of ``State`` is one of the following values:

            Applied

          Amazon Route 53 has finished creating resource record sets, and changes have propagated
          to all Route 53 edge locations.

            Creating

          Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
          confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

            Failed

          Route 53 wasn't able to create or update the resource record sets. When the value of
          ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
          to fail.

        - **Message** *(string) --*

          If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
          is another value, ``Message`` is empty.

        - **TrafficPolicyId** *(string) --*

          The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
          the specified hosted zone.

        - **TrafficPolicyVersion** *(integer) --*

          The version of the traffic policy that Amazon Route 53 used to create resource record
          sets in the specified hosted zone.

        - **TrafficPolicyType** *(string) --*

          The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
          created for this traffic policy instance.

    - **HostedZoneIdMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``HostedZoneIdMarker`` is the ID of the hosted zone of the
      first traffic policy instance in the next group of traffic policy instances.

    - **TrafficPolicyInstanceNameMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first
      traffic policy instance in the next group of ``MaxItems`` traffic policy instances.

    - **TrafficPolicyInstanceTypeMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the
      resource record sets that are associated with the first traffic policy instance in the next
      group of ``MaxItems`` traffic policy instances.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more traffic policy instances to be listed. If the
      response was truncated, you can get the next group of traffic policy instances by calling
      ``ListTrafficPolicyInstancesByPolicy`` again and specifying the values of the
      ``HostedZoneIdMarker`` , ``TrafficPolicyInstanceNameMarker`` , and
      ``TrafficPolicyInstanceTypeMarker`` elements in the corresponding request parameters.

    - **MaxItems** *(string) --*

      The value that you specified for the ``MaxItems`` parameter in the call to
      ``ListTrafficPolicyInstancesByPolicy`` that produced the current response.
    """


_ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef(
    _ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstancesResponse` `TrafficPolicyInstances`

    A complex type that contains settings for the new traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
      in the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated
      to all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
      confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
      to fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
      is another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record
      sets in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List[
            ClientListTrafficPolicyInstancesResponseTrafficPolicyInstancesTypeDef
        ],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyInstancesResponseTypeDef(
    _ClientListTrafficPolicyInstancesResponseTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyInstances` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicyInstances** *(list) --*

      A list that contains one ``TrafficPolicyInstance`` element for each traffic policy instance
      that matches the elements in the request.

      - *(dict) --*

        A complex type that contains settings for the new traffic policy instance.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the new traffic policy instance.

        - **HostedZoneId** *(string) --*

          The ID of the hosted zone that Amazon Route 53 created resource record sets in.

        - **Name** *(string) --*

          The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
          using the resource record sets that are associated with this traffic policy instance.

        - **TTL** *(integer) --*

          The TTL that Amazon Route 53 assigned to all of the resource record sets that it created
          in the specified hosted zone.

        - **State** *(string) --*

          The value of ``State`` is one of the following values:

            Applied

          Amazon Route 53 has finished creating resource record sets, and changes have propagated
          to all Route 53 edge locations.

            Creating

          Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to
          confirm that the ``CreateTrafficPolicyInstance`` request completed successfully.

            Failed

          Route 53 wasn't able to create or update the resource record sets. When the value of
          ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request
          to fail.

        - **Message** *(string) --*

          If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State``
          is another value, ``Message`` is empty.

        - **TrafficPolicyId** *(string) --*

          The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
          the specified hosted zone.

        - **TrafficPolicyVersion** *(integer) --*

          The version of the traffic policy that Amazon Route 53 used to create resource record
          sets in the specified hosted zone.

        - **TrafficPolicyType** *(string) --*

          The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
          created for this traffic policy instance.

    - **HostedZoneIdMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``HostedZoneIdMarker`` is the ID of the hosted zone of the
      first traffic policy instance that Route 53 will return if you submit another
      ``ListTrafficPolicyInstances`` request.

    - **TrafficPolicyInstanceNameMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceNameMarker`` is the name of the first
      traffic policy instance that Route 53 will return if you submit another
      ``ListTrafficPolicyInstances`` request.

    - **TrafficPolicyInstanceTypeMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , ``TrafficPolicyInstanceTypeMarker`` is the DNS type of the
      resource record sets that are associated with the first traffic policy instance that Amazon
      Route 53 will return if you submit another ``ListTrafficPolicyInstances`` request.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more traffic policy instances to be listed. If the
      response was truncated, you can get more traffic policy instances by calling
      ``ListTrafficPolicyInstances`` again and specifying the values of the ``HostedZoneIdMarker``
      , ``TrafficPolicyInstanceNameMarker`` , and ``TrafficPolicyInstanceTypeMarker`` in the
      corresponding request parameters.

    - **MaxItems** *(string) --*

      The value that you specified for the ``MaxItems`` parameter in the call to
      ``ListTrafficPolicyInstances`` that produced the current response.
    """


_ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef = TypedDict(
    "_ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": str,
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef(
    _ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyVersionsResponse` `TrafficPolicies`

    A complex type that contains settings for a traffic policy.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to a traffic policy when you created it.

    - **Version** *(integer) --*

      The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
      policy, the value of ``Version`` is always 1.

    - **Name** *(string) --*

      The name that you specified when you created the traffic policy.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **Document** *(string) --*

      The definition of a traffic policy in JSON format. You specify the JSON document to use
      for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information
      about the JSON format, see `Traffic Policy Document Format
      <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
      .

    - **Comment** *(string) --*

      The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List[
            ClientListTrafficPolicyVersionsResponseTrafficPoliciesTypeDef
        ],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
    total=False,
)


class ClientListTrafficPolicyVersionsResponseTypeDef(
    _ClientListTrafficPolicyVersionsResponseTypeDef
):
    """
    Type definition for `ClientListTrafficPolicyVersions` `Response`

    A complex type that contains the response information for the request.

    - **TrafficPolicies** *(list) --*

      A list that contains one ``TrafficPolicy`` element for each traffic policy version that is
      associated with the specified traffic policy.

      - *(dict) --*

        A complex type that contains settings for a traffic policy.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to a traffic policy when you created it.

        - **Version** *(integer) --*

          The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
          policy, the value of ``Version`` is always 1.

        - **Name** *(string) --*

          The name that you specified when you created the traffic policy.

        - **Type** *(string) --*

          The DNS type of the resource record sets that Amazon Route 53 creates when you use a
          traffic policy to create a traffic policy instance.

        - **Document** *(string) --*

          The definition of a traffic policy in JSON format. You specify the JSON document to use
          for a new traffic policy in the ``CreateTrafficPolicy`` request. For more information
          about the JSON format, see `Traffic Policy Document Format
          <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
          .

        - **Comment** *(string) --*

          The comment that you specify in the ``CreateTrafficPolicy`` request, if any.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more traffic policies to be listed. If the response
      was truncated, you can get the next group of traffic policies by submitting another
      ``ListTrafficPolicyVersions`` request and specifying the value of ``NextMarker`` in the
      ``marker`` parameter.

    - **TrafficPolicyVersionMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , the value of ``TrafficPolicyVersionMarker`` identifies the
      first traffic policy that Amazon Route 53 will return if you submit another request. Call
      ``ListTrafficPolicyVersions`` again and specify the value of ``TrafficPolicyVersionMarker``
      in the ``TrafficPolicyVersionMarker`` request parameter.

      This element is present only if ``IsTruncated`` is ``true`` .

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the
      ``ListTrafficPolicyVersions`` request that produced the current response.
    """


_ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef = TypedDict(
    "_ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef(
    _ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef
):
    """
    Type definition for `ClientListVpcAssociationAuthorizationsResponse` `VPCs`

    (Private hosted zones only) A complex type that contains information about an Amazon VPC.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientListVpcAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_ClientListVpcAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List[ClientListVpcAssociationAuthorizationsResponseVPCsTypeDef],
    },
    total=False,
)


class ClientListVpcAssociationAuthorizationsResponseTypeDef(
    _ClientListVpcAssociationAuthorizationsResponseTypeDef
):
    """
    Type definition for `ClientListVpcAssociationAuthorizations` `Response`

    A complex type that contains the response information for the request.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that you can associate the listed VPCs with.

    - **NextToken** *(string) --*

      When the response includes a ``NextToken`` element, there are more VPCs that can be
      associated with the specified hosted zone. To get the next page of VPCs, submit another
      ``ListVPCAssociationAuthorizations`` request, and include the value of the ``NextToken``
      element from the response in the ``nexttoken`` request parameter.

    - **VPCs** *(list) --*

      The list of VPCs that are authorized to be associated with the specified hosted zone.

      - *(dict) --*

        (Private hosted zones only) A complex type that contains information about an Amazon VPC.

        - **VPCRegion** *(string) --*

          (Private hosted zones only) The region that an Amazon VPC was created in.

        - **VPCId** *(string) --*

          (Private hosted zones only) The ID of an Amazon VPC.
    """


_ClientTestDnsAnswerResponseTypeDef = TypedDict(
    "_ClientTestDnsAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": str,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
    total=False,
)


class ClientTestDnsAnswerResponseTypeDef(_ClientTestDnsAnswerResponseTypeDef):
    """
    Type definition for `ClientTestDnsAnswer` `Response`

    A complex type that contains the response to a ``TestDNSAnswer`` request.

    - **Nameserver** *(string) --*

      The Amazon Route 53 name server used to respond to the request.

    - **RecordName** *(string) --*

      The name of the resource record set that you submitted a request for.

    - **RecordType** *(string) --*

      The type of the resource record set that you submitted a request for.

    - **RecordData** *(list) --*

      A list that contains values that Amazon Route 53 returned for this resource record set.

      - *(string) --*

        A value that Amazon Route 53 returned for this resource record set. A ``RecordDataEntry``
        element is one of the following:

        * For non-alias resource record sets, a ``RecordDataEntry`` element contains one value in
        the resource record set. If the resource record set contains multiple values, the response
        includes one ``RecordDataEntry`` element for each value.

        * For multiple resource record sets that have the same name and type, which includes
        weighted, latency, geolocation, and failover, a ``RecordDataEntry`` element contains the
        value from the appropriate resource record set based on the request.

        * For alias resource record sets that refer to AWS resources other than another resource
        record set, the ``RecordDataEntry`` element contains an IP address or a domain name for the
        AWS resource, depending on the type of resource.

        * For alias resource record sets that refer to other resource record sets, a
        ``RecordDataEntry`` element contains one value from the referenced resource record set. If
        the referenced resource record set contains multiple values, the response includes one
        ``RecordDataEntry`` element for each value.

    - **ResponseCode** *(string) --*

      A code that indicates whether the request is valid or not. The most common response code is
      ``NOERROR`` , meaning that the request is valid. If the response is not valid, Amazon Route
      53 returns a response code that describes the error. For a list of possible response codes,
      see `DNS RCODES
      <http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6>`__ on
      the IANA website.

    - **Protocol** *(string) --*

      The protocol that Amazon Route 53 used to respond to the request, either ``UDP`` or ``TCP`` .
    """


_ClientUpdateHealthCheckAlarmIdentifierTypeDef = TypedDict(
    "_ClientUpdateHealthCheckAlarmIdentifierTypeDef", {"Region": str, "Name": str}
)


class ClientUpdateHealthCheckAlarmIdentifierTypeDef(
    _ClientUpdateHealthCheckAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheck` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers
    to use to determine whether the specified health check is healthy.

    - **Region** *(string) --* **[REQUIRED]**

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether
      this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and
      Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to
      determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't
        supported.
    """


_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfiguration` `Dimensions`

    For the metric that the CloudWatch alarm is associated with, a complex type that
    contains information about one dimension.

    - **Name** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the name of one
      dimension.

    - **Value** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the value of one
      dimension.
    """


_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "Dimensions": List[
            ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponseHealthCheck` `CloudWatchAlarmConfiguration`

    A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
    monitoring for this health check.

    - **EvaluationPeriods** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the number of periods that
      the metric is compared to the threshold.

    - **Threshold** *(float) --*

      For the metric that the CloudWatch alarm is associated with, the value the metric is
      compared with.

    - **ComparisonOperator** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the arithmetic operation
      that is used for the comparison.

    - **Period** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the duration of one
      evaluation period in seconds.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that the alarm is associated with.

    - **Namespace** *(string) --*

      The namespace of the metric that the alarm is associated with. For more information, see
      `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

    - **Statistic** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the statistic that is
      applied to the metric.

    - **Dimensions** *(list) --*

      For the metric that the CloudWatch alarm is associated with, a complex type that contains
      information about the dimensions for the metric. For information, see `Amazon CloudWatch
      Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

      - *(dict) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about one dimension.

        - **Name** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the name of one
          dimension.

        - **Value** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the value of one
          dimension.
    """


_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
    checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --*

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine
      whether this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
      Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --*

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
      to determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
        aren't supported.
    """


_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": str,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponseHealthCheck` `HealthCheckConfig`

    A complex type that contains detailed information about one health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
      health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
      request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
      the interval that you specify in ``RequestInterval`` . Using an IP address returned by
      DNS, Route 53 then checks the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
      example, ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
      for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
      addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
      . This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is in
      local, private, non-routable, or multicast ranges. For more information about IP
      addresses for which you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
      ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.
      Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Amazon Route 53
      determines whether an endpoint is healthy.

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

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
         v1.0 or later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
      53 submits an HTTP request and searches the first 5,120 bytes of the response body for
      the string that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
      body for the string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
      state of the alarm is ``OK`` , the health check is considered healthy. If the state is
      ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
      sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
      status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
      ``Unhealthy`` , or ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks,
      Route 53 adds up the number of health checks that Route 53 health checkers consider to be
      healthy and compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health checks.
      The path can be any value for which your endpoint will return an HTTP status code of 2xx
      or 3xx when the endpoint is healthy, for example, the file
      /docs/route53-health-check.html. You can also include query string parameters, for
      example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
      passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
      checks except TCP health checks. This is typically the fully qualified DNS name of the
      endpoint on which you want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
      header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
      Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
      value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for
      ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
      Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
        checks to the endpoint. If there's no resource record set with a type of A for the name
        that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
        resolution failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets
      and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
      recommend that you create a separate health check for each endpoint. For example, create
      a health check for each HTTP server that is serving content for www.example.com. For the
      value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
      us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
        associate the health check with those resource record sets, health check results will
        be unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
      for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
      ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
      want Amazon Route 53 to search for in the response body from the specified resource. If
      the string appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your
      endpoint and the time that it sends the next health check request. Each Route 53 health
      checker makes requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30``
      seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon
      Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
      versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
      Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three health
      checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers
      in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
      the **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for
      example, to consider a health check unhealthy when it otherwise would be considered
      healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's
      what happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting
      requests to your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
      health checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
      corresponding CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to
      always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
      the corresponding resources. If you want to stop routing traffic to a resource, change
      the value of `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more
      information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health check
      that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
      considered healthy. To specify the child health checks that you want to associate with a
      ``CALCULATED`` health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53 always
      considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
      element for each health check that you want to associate with a ``CALCULATED`` health
      check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of
      ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
      negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
      the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the
      ``client_hello`` message. If you don't enable SNI, the status of the health check will be
      ``SSL alert handshake_failure`` . A health check can also have that status for other
      reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
      configuration on your endpoint and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
      field and possibly several more in the ``Subject Alternative Names`` field. One of the
      domain names in the certificate should match the value that you specify for
      ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
      with a certificate that does not include the domain name that you specified in
      ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
      attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
      ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want
      Amazon Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs checks
      from all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks,
      Route 53 will briefly continue to perform checks from that region to ensure that some
      health checkers are always checking the endpoint (for example, if you replace three
      regions with four different regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
      checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --*

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine
        whether this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
        Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --*

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
        to determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
          aren't supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state, the
      status that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
      that CloudWatch had sufficient data to determine the alarm state. For new health checks
      that have no last known status, the default status for the health check is healthy.
    """


_ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponseHealthCheck` `LinkedService`

    If the health check was created by another service, the service that created the health
    check. When a health check is created by another service, you can't edit or delete it using
    Amazon Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientUpdateHealthCheckResponseHealthCheckTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ClientUpdateHealthCheckResponseHealthCheckLinkedServiceTypeDef,
        "HealthCheckConfig": ClientUpdateHealthCheckResponseHealthCheckHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ClientUpdateHealthCheckResponseHealthCheckCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateHealthCheckResponseHealthCheckTypeDef(
    _ClientUpdateHealthCheckResponseHealthCheckTypeDef
):
    """
    Type definition for `ClientUpdateHealthCheckResponse` `HealthCheck`

    A complex type that contains the response to an ``UpdateHealthCheck`` request.

    - **Id** *(string) --*

      The identifier that Amazon Route 53assigned to the health check when you created it. When
      you add or update a resource record set, you use this value to specify which health check
      to use. The value can be up to 64 characters long.

    - **CallerReference** *(string) --*

      A unique string that you specified when you created the health check.

    - **LinkedService** *(dict) --*

      If the health check was created by another service, the service that created the health
      check. When a health check is created by another service, you can't edit or delete it using
      Amazon Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.

    - **HealthCheckConfig** *(dict) --*

      A complex type that contains detailed information about one health check.

      - **IPAddress** *(string) --*

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
        health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
        request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
        the interval that you specify in ``RequestInterval`` . Using an IP address returned by
        DNS, Route 53 then checks the health of the endpoint.

        Use one of the following formats for the value of ``IPAddress`` :

        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
        example, ``192.0.2.44`` .

        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
        for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
        addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
        associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
        . This ensures that the IP address of your instance will never change.

        For more information, see `FullyQualifiedDomainName
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
        .

        Constraints: Route 53 can't check the health of endpoints for which the IP address is in
        local, private, non-routable, or multicast ranges. For more information about IP
        addresses for which you can't create health checks, see the following documents:

        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
        <https://tools.ietf.org/html/rfc6598>`__

        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
        ``IPAddress`` .

      - **Port** *(integer) --*

        The port on the endpoint on which you want Amazon Route 53 to perform health checks.
        Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Amazon Route 53
        determines whether an endpoint is healthy.

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

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
           v1.0 or later.

        * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
        53 submits an HTTP request and searches the first 5,120 bytes of the response body for
        the string that you specify in ``SearchString`` .

        * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
        body for the string that you specify in ``SearchString`` .

        * **TCP** : Route 53 tries to establish a TCP connection.

        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
        state of the alarm is ``OK`` , the health check is considered healthy. If the state is
        ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
        sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
        status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
        ``Unhealthy`` , or ``LastKnownStatus`` .

        * **CALCULATED** : For health checks that monitor the status of other health checks,
        Route 53 adds up the number of health checks that Route 53 health checkers consider to be
        healthy and compares that number with the value of ``HealthThreshold`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path, if any, that you want Amazon Route 53 to request when performing health checks.
        The path can be any value for which your endpoint will return an HTTP status code of 2xx
        or 3xx when the endpoint is healthy, for example, the file
        /docs/route53-health-check.html. You can also include query string parameters, for
        example, ``/welcome.html?language=jp&login=y`` .

      - **FullyQualifiedDomainName** *(string) --*

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         **If you specify a value for**  ``IPAddress`` :

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
        passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
        checks except TCP health checks. This is typically the fully qualified DNS name of the
        endpoint on which you want Route 53 to perform health checks.

        When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
        header:

        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the Host header.

        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the ``Host`` header.

        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
        Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

        If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
        value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         **If you don't specify a value for ``IPAddress`` ** :

        Route 53 sends a DNS request to the domain that you specify for
        ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
        Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

        .. note::

          If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
          checks to the endpoint. If there's no resource record set with a type of A for the name
          that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
          resolution failed" error.

        If you want to check the health of weighted, latency, or failover resource record sets
        and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
        recommend that you create a separate health check for each endpoint. For example, create
        a health check for each HTTP server that is serving content for www.example.com. For the
        value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
        us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

        .. warning::

          In this configuration, if you create a health check for which the value of
          ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
          associate the health check with those resource record sets, health check results will
          be unpredictable.

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
        ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
        ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
        for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
        ``Host`` header.

      - **SearchString** *(string) --*

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
        want Amazon Route 53 to search for in the response body from the specified resource. If
        the string appears in the response body, Route 53 considers the resource healthy.

        Route 53 considers case when searching for ``SearchString`` in the response body.

      - **RequestInterval** *(integer) --*

        The number of seconds between the time that Amazon Route 53 gets a response from your
        endpoint and the time that it sends the next health check request. Each Route 53 health
        checker makes requests at this interval.

        .. warning::

          You can't change the value of ``RequestInterval`` after you create a health check.

        If you don't specify a value for ``RequestInterval`` , the default value is ``30``
        seconds.

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Amazon
        Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
        versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
        Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

        If you don't specify a value for ``FailureThreshold`` , the default value is three health
        checks.

      - **MeasureLatency** *(boolean) --*

        Specify whether you want Amazon Route 53 to measure the latency between health checkers
        in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
        the **Health Checks** page in the Route 53 console.

        .. warning::

          You can't change the value of ``MeasureLatency`` after you create a health check.

      - **Inverted** *(boolean) --*

        Specify whether you want Amazon Route 53 to invert the status of a health check, for
        example, to consider a health check unhealthy when it otherwise would be considered
        healthy.

      - **Disabled** *(boolean) --*

        Stops Route 53 from performing health checks. When you disable a health check, here's
        what happens:

        * **Health checks that check the health of endpoints:** Route 53 stops submitting
        requests to your application, server, or other resource.

        * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
        health checks.

        * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
        corresponding CloudWatch metrics.

        After you disable a health check, Route 53 considers the status of the health check to
        always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
        the corresponding resources. If you want to stop routing traffic to a resource, change
        the value of `Inverted
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
        .

        Charges for a health check still apply when the health check is disabled. For more
        information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

      - **HealthThreshold** *(integer) --*

        The number of child health checks that are associated with a ``CALCULATED`` health check
        that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
        considered healthy. To specify the child health checks that you want to associate with a
        ``CALCULATED`` health check, use the `ChildHealthChecks
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
        element.

        Note the following:

        * If you specify a number greater than the number of child health checks, Route 53 always
        considers this health check to be unhealthy.

        * If you specify ``0`` , Route 53 always considers this health check to be healthy.

      - **ChildHealthChecks** *(list) --*

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
        element for each health check that you want to associate with a ``CALCULATED`` health
        check.

        - *(string) --*

      - **EnableSNI** *(boolean) --*

        Specify whether you want Amazon Route 53 to send the value of
        ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
        negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
        the applicable SSL/TLS certificate.

        Some endpoints require that ``HTTPS`` requests include the host name in the
        ``client_hello`` message. If you don't enable SNI, the status of the health check will be
        ``SSL alert handshake_failure`` . A health check can also have that status for other
        reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
        configuration on your endpoint and confirm that your certificate is valid.

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
        field and possibly several more in the ``Subject Alternative Names`` field. One of the
        domain names in the certificate should match the value that you specify for
        ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
        with a certificate that does not include the domain name that you specified in
        ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
        attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
        ``client_hello`` message.

      - **Regions** *(list) --*

        A complex type that contains one ``Region`` element for each region from which you want
        Amazon Route 53 health checkers to check the specified endpoint.

        If you don't specify any regions, Route 53 health checkers automatically performs checks
        from all of the regions that are listed under **Valid Values** .

        If you update a health check to remove a region that has been performing health checks,
        Route 53 will briefly continue to perform checks from that region to ensure that some
        health checkers are always checking the endpoint (for example, if you replace three
        regions with four different regions).

        - *(string) --*

      - **AlarmIdentifier** *(dict) --*

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
        checkers to use to determine whether the specified health check is healthy.

        - **Region** *(string) --*

          For the CloudWatch alarm that you want Route 53 health checkers to use to determine
          whether this health check is healthy, the region that the alarm was created in.

          For the current list of CloudWatch regions, see `Amazon CloudWatch
          <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
          Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        - **Name** *(string) --*

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
          to determine whether this health check is healthy.

          .. note::

            Route 53 supports CloudWatch alarms with the following features:

            * Standard-resolution metrics. High-resolution metrics aren't supported. For more
            information, see `High-Resolution Metrics
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
            in the *Amazon CloudWatch User Guide* .

            * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
            aren't supported.

      - **InsufficientDataHealthStatus** *(string) --*

        When CloudWatch has insufficient data about the metric to determine the alarm state, the
        status that you want Amazon Route 53 to assign to the health check:

        * ``Healthy`` : Route 53 considers the health check to be healthy.

        * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

        * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
        that CloudWatch had sufficient data to determine the alarm state. For new health checks
        that have no last known status, the default status for the health check is healthy.

    - **HealthCheckVersion** *(integer) --*

      The version of the health check. You can optionally pass this value in a call to
      ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

    - **CloudWatchAlarmConfiguration** *(dict) --*

      A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
      monitoring for this health check.

      - **EvaluationPeriods** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the number of periods that
        the metric is compared to the threshold.

      - **Threshold** *(float) --*

        For the metric that the CloudWatch alarm is associated with, the value the metric is
        compared with.

      - **ComparisonOperator** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the arithmetic operation
        that is used for the comparison.

      - **Period** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the duration of one
        evaluation period in seconds.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that the alarm is associated with.

      - **Namespace** *(string) --*

        The namespace of the metric that the alarm is associated with. For more information, see
        `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

      - **Statistic** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the statistic that is
        applied to the metric.

      - **Dimensions** *(list) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that contains
        information about the dimensions for the metric. For information, see `Amazon CloudWatch
        Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        - *(dict) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that
          contains information about one dimension.

          - **Name** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the name of one
            dimension.

          - **Value** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the value of one
            dimension.
    """


_ClientUpdateHealthCheckResponseTypeDef = TypedDict(
    "_ClientUpdateHealthCheckResponseTypeDef",
    {"HealthCheck": ClientUpdateHealthCheckResponseHealthCheckTypeDef},
    total=False,
)


class ClientUpdateHealthCheckResponseTypeDef(_ClientUpdateHealthCheckResponseTypeDef):
    """
    Type definition for `ClientUpdateHealthCheck` `Response`

    A complex type that contains the response to the ``UpdateHealthCheck`` request.

    - **HealthCheck** *(dict) --*

      A complex type that contains the response to an ``UpdateHealthCheck`` request.

      - **Id** *(string) --*

        The identifier that Amazon Route 53assigned to the health check when you created it. When
        you add or update a resource record set, you use this value to specify which health check
        to use. The value can be up to 64 characters long.

      - **CallerReference** *(string) --*

        A unique string that you specified when you created the health check.

      - **LinkedService** *(dict) --*

        If the health check was created by another service, the service that created the health
        check. When a health check is created by another service, you can't edit or delete it using
        Amazon Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.

      - **HealthCheckConfig** *(dict) --*

        A complex type that contains detailed information about one health check.

        - **IPAddress** *(string) --*

          The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
          health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
          request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
          the interval that you specify in ``RequestInterval`` . Using an IP address returned by
          DNS, Route 53 then checks the health of the endpoint.

          Use one of the following formats for the value of ``IPAddress`` :

          * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
          example, ``192.0.2.44`` .

          * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
          for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
          addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

          If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
          associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress``
          . This ensures that the IP address of your instance will never change.

          For more information, see `FullyQualifiedDomainName
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
          .

          Constraints: Route 53 can't check the health of endpoints for which the IP address is in
          local, private, non-routable, or multicast ranges. For more information about IP
          addresses for which you can't create health checks, see the following documents:

          * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

          * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
          <https://tools.ietf.org/html/rfc6598>`__

          * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

          When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
          ``IPAddress`` .

        - **Port** *(integer) --*

          The port on the endpoint on which you want Amazon Route 53 to perform health checks.
          Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

        - **Type** *(string) --*

          The type of health check that you want to create, which indicates how Amazon Route 53
          determines whether an endpoint is healthy.

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

             If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
             v1.0 or later.

          * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route
          53 submits an HTTP request and searches the first 5,120 bytes of the response body for
          the string that you specify in ``SearchString`` .

          * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
          Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response
          body for the string that you specify in ``SearchString`` .

          * **TCP** : Route 53 tries to establish a TCP connection.

          * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the
          state of the alarm is ``OK`` , the health check is considered healthy. If the state is
          ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
          sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check
          status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` ,
          ``Unhealthy`` , or ``LastKnownStatus`` .

          * **CALCULATED** : For health checks that monitor the status of other health checks,
          Route 53 adds up the number of health checks that Route 53 health checkers consider to be
          healthy and compares that number with the value of ``HealthThreshold`` .

          For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
          <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

        - **ResourcePath** *(string) --*

          The path, if any, that you want Amazon Route 53 to request when performing health checks.
          The path can be any value for which your endpoint will return an HTTP status code of 2xx
          or 3xx when the endpoint is healthy, for example, the file
          /docs/route53-health-check.html. You can also include query string parameters, for
          example, ``/welcome.html?language=jp&login=y`` .

        - **FullyQualifiedDomainName** *(string) --*

          Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

           **If you specify a value for**  ``IPAddress`` :

          Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
          passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
          checks except TCP health checks. This is typically the fully qualified DNS name of the
          endpoint on which you want Route 53 to perform health checks.

          When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
          header:

          * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the Host header.

          * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for
          ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
          the ``Host`` header.

          * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
          Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

          If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the
          value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

           **If you don't specify a value for ``IPAddress`` ** :

          Route 53 sends a DNS request to the domain that you specify for
          ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
          Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

          .. note::

            If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health
            checks to the endpoint. If there's no resource record set with a type of A for the name
            that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS
            resolution failed" error.

          If you want to check the health of weighted, latency, or failover resource record sets
          and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
          recommend that you create a separate health check for each endpoint. For example, create
          a health check for each HTTP server that is serving content for www.example.com. For the
          value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as
          us-east-2-www.example.com), not the name of the resource record sets (www.example.com).

          .. warning::

            In this configuration, if you create a health check for which the value of
            ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then
            associate the health check with those resource record sets, health check results will
            be unpredictable.

          In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
          ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
          ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value
          for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
          ``Host`` header.

        - **SearchString** *(string) --*

          If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
          want Amazon Route 53 to search for in the response body from the specified resource. If
          the string appears in the response body, Route 53 considers the resource healthy.

          Route 53 considers case when searching for ``SearchString`` in the response body.

        - **RequestInterval** *(integer) --*

          The number of seconds between the time that Amazon Route 53 gets a response from your
          endpoint and the time that it sends the next health check request. Each Route 53 health
          checker makes requests at this interval.

          .. warning::

            You can't change the value of ``RequestInterval`` after you create a health check.

          If you don't specify a value for ``RequestInterval`` , the default value is ``30``
          seconds.

        - **FailureThreshold** *(integer) --*

          The number of consecutive health checks that an endpoint must pass or fail for Amazon
          Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
          versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
          Healthy
          <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
          in the *Amazon Route 53 Developer Guide* .

          If you don't specify a value for ``FailureThreshold`` , the default value is three health
          checks.

        - **MeasureLatency** *(boolean) --*

          Specify whether you want Amazon Route 53 to measure the latency between health checkers
          in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
          the **Health Checks** page in the Route 53 console.

          .. warning::

            You can't change the value of ``MeasureLatency`` after you create a health check.

        - **Inverted** *(boolean) --*

          Specify whether you want Amazon Route 53 to invert the status of a health check, for
          example, to consider a health check unhealthy when it otherwise would be considered
          healthy.

        - **Disabled** *(boolean) --*

          Stops Route 53 from performing health checks. When you disable a health check, here's
          what happens:

          * **Health checks that check the health of endpoints:** Route 53 stops submitting
          requests to your application, server, or other resource.

          * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
          health checks.

          * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
          corresponding CloudWatch metrics.

          After you disable a health check, Route 53 considers the status of the health check to
          always be healthy. If you configured DNS failover, Route 53 continues to route traffic to
          the corresponding resources. If you want to stop routing traffic to a resource, change
          the value of `Inverted
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
          .

          Charges for a health check still apply when the health check is disabled. For more
          information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

        - **HealthThreshold** *(integer) --*

          The number of child health checks that are associated with a ``CALCULATED`` health check
          that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be
          considered healthy. To specify the child health checks that you want to associate with a
          ``CALCULATED`` health check, use the `ChildHealthChecks
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
          element.

          Note the following:

          * If you specify a number greater than the number of child health checks, Route 53 always
          considers this health check to be unhealthy.

          * If you specify ``0`` , Route 53 always considers this health check to be healthy.

        - **ChildHealthChecks** *(list) --*

          (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
          element for each health check that you want to associate with a ``CALCULATED`` health
          check.

          - *(string) --*

        - **EnableSNI** *(boolean) --*

          Specify whether you want Amazon Route 53 to send the value of
          ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
          negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with
          the applicable SSL/TLS certificate.

          Some endpoints require that ``HTTPS`` requests include the host name in the
          ``client_hello`` message. If you don't enable SNI, the status of the health check will be
          ``SSL alert handshake_failure`` . A health check can also have that status for other
          reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
          configuration on your endpoint and confirm that your certificate is valid.

          The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
          field and possibly several more in the ``Subject Alternative Names`` field. One of the
          domain names in the certificate should match the value that you specify for
          ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
          with a certificate that does not include the domain name that you specified in
          ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
          attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
          ``client_hello`` message.

        - **Regions** *(list) --*

          A complex type that contains one ``Region`` element for each region from which you want
          Amazon Route 53 health checkers to check the specified endpoint.

          If you don't specify any regions, Route 53 health checkers automatically performs checks
          from all of the regions that are listed under **Valid Values** .

          If you update a health check to remove a region that has been performing health checks,
          Route 53 will briefly continue to perform checks from that region to ensure that some
          health checkers are always checking the endpoint (for example, if you replace three
          regions with four different regions).

          - *(string) --*

        - **AlarmIdentifier** *(dict) --*

          A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health
          checkers to use to determine whether the specified health check is healthy.

          - **Region** *(string) --*

            For the CloudWatch alarm that you want Route 53 health checkers to use to determine
            whether this health check is healthy, the region that the alarm was created in.

            For the current list of CloudWatch regions, see `Amazon CloudWatch
            <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
            Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

          - **Name** *(string) --*

            The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
            to determine whether this health check is healthy.

            .. note::

              Route 53 supports CloudWatch alarms with the following features:

              * Standard-resolution metrics. High-resolution metrics aren't supported. For more
              information, see `High-Resolution Metrics
              <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
              in the *Amazon CloudWatch User Guide* .

              * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
              aren't supported.

        - **InsufficientDataHealthStatus** *(string) --*

          When CloudWatch has insufficient data about the metric to determine the alarm state, the
          status that you want Amazon Route 53 to assign to the health check:

          * ``Healthy`` : Route 53 considers the health check to be healthy.

          * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

          * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
          that CloudWatch had sufficient data to determine the alarm state. For new health checks
          that have no last known status, the default status for the health check is healthy.

      - **HealthCheckVersion** *(integer) --*

        The version of the health check. You can optionally pass this value in a call to
        ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

      - **CloudWatchAlarmConfiguration** *(dict) --*

        A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is
        monitoring for this health check.

        - **EvaluationPeriods** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the number of periods that
          the metric is compared to the threshold.

        - **Threshold** *(float) --*

          For the metric that the CloudWatch alarm is associated with, the value the metric is
          compared with.

        - **ComparisonOperator** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the arithmetic operation
          that is used for the comparison.

        - **Period** *(integer) --*

          For the metric that the CloudWatch alarm is associated with, the duration of one
          evaluation period in seconds.

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that the alarm is associated with.

        - **Namespace** *(string) --*

          The namespace of the metric that the alarm is associated with. For more information, see
          `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

        - **Statistic** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the statistic that is
          applied to the metric.

        - **Dimensions** *(list) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that contains
          information about the dimensions for the metric. For information, see `Amazon CloudWatch
          Namespaces, Dimensions, and Metrics Reference
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
          in the *Amazon CloudWatch User Guide* .

          - *(dict) --*

            For the metric that the CloudWatch alarm is associated with, a complex type that
            contains information about one dimension.

            - **Name** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the name of one
              dimension.

            - **Value** *(string) --*

              For the metric that the CloudWatch alarm is associated with, the value of one
              dimension.
    """


_ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef
):
    """
    Type definition for `ClientUpdateHostedZoneCommentResponseHostedZone` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef
):
    """
    Type definition for `ClientUpdateHostedZoneCommentResponseHostedZone` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ClientUpdateHostedZoneCommentResponseHostedZoneConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ClientUpdateHostedZoneCommentResponseHostedZoneLinkedServiceTypeDef,
    },
    total=False,
)


class ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef(
    _ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef
):
    """
    Type definition for `ClientUpdateHostedZoneCommentResponse` `HostedZone`

    A complex type that contains the response to the ``UpdateHostedZoneComment`` request.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have registered
      with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientUpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "_ClientUpdateHostedZoneCommentResponseTypeDef",
    {"HostedZone": ClientUpdateHostedZoneCommentResponseHostedZoneTypeDef},
    total=False,
)


class ClientUpdateHostedZoneCommentResponseTypeDef(
    _ClientUpdateHostedZoneCommentResponseTypeDef
):
    """
    Type definition for `ClientUpdateHostedZoneComment` `Response`

    A complex type that contains the response to the ``UpdateHostedZoneComment`` request.

    - **HostedZone** *(dict) --*

      A complex type that contains the response to the ``UpdateHostedZoneComment`` request.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the hosted zone when you created it.

      - **Name** *(string) --*

        The name of the domain. For public hosted zones, this is the name that you have registered
        with your DNS registrar.

        For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
        (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

      - **CallerReference** *(string) --*

        The value that you specified for ``CallerReference`` when you created the hosted zone.

      - **Config** *(dict) --*

        A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
        the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
        ``Comment`` elements don't appear in the response.

        - **Comment** *(string) --*

          Any comments that you want to include about the hosted zone.

        - **PrivateZone** *(boolean) --*

          A value that indicates whether this is a private hosted zone.

      - **ResourceRecordSetCount** *(integer) --*

        The number of resource record sets in the hosted zone.

      - **LinkedService** *(dict) --*

        If the hosted zone was created by another service, the service that created the hosted
        zone. When a hosted zone is created by another service, you can't edit or delete it using
        Route 53.

        - **ServicePrincipal** *(string) --*

          If the health check or hosted zone was created by another service, the service that
          created the resource. When a resource is created by another service, you can't edit or
          delete it using Amazon Route 53.

        - **Description** *(string) --*

          If the health check or hosted zone was created by another service, an optional
          description that can be provided by the other service. When a resource is created by
          another service, you can't edit or delete it using Amazon Route 53.
    """


_ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": str,
        "Document": str,
        "Comment": str,
    },
    total=False,
)


class ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef(
    _ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef
):
    """
    Type definition for `ClientUpdateTrafficPolicyCommentResponse` `TrafficPolicy`

    A complex type that contains settings for the specified traffic policy.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to a traffic policy when you created it.

    - **Version** *(integer) --*

      The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
      policy, the value of ``Version`` is always 1.

    - **Name** *(string) --*

      The name that you specified when you created the traffic policy.

    - **Type** *(string) --*

      The DNS type of the resource record sets that Amazon Route 53 creates when you use a
      traffic policy to create a traffic policy instance.

    - **Document** *(string) --*

      The definition of a traffic policy in JSON format. You specify the JSON document to use for
      a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
      JSON format, see `Traffic Policy Document Format
      <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
      .

    - **Comment** *(string) --*

      The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientUpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyCommentResponseTypeDef",
    {"TrafficPolicy": ClientUpdateTrafficPolicyCommentResponseTrafficPolicyTypeDef},
    total=False,
)


class ClientUpdateTrafficPolicyCommentResponseTypeDef(
    _ClientUpdateTrafficPolicyCommentResponseTypeDef
):
    """
    Type definition for `ClientUpdateTrafficPolicyComment` `Response`

    A complex type that contains the response information for the traffic policy.

    - **TrafficPolicy** *(dict) --*

      A complex type that contains settings for the specified traffic policy.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to a traffic policy when you created it.

      - **Version** *(integer) --*

        The version number that Amazon Route 53 assigns to a traffic policy. For a new traffic
        policy, the value of ``Version`` is always 1.

      - **Name** *(string) --*

        The name that you specified when you created the traffic policy.

      - **Type** *(string) --*

        The DNS type of the resource record sets that Amazon Route 53 creates when you use a
        traffic policy to create a traffic policy instance.

      - **Document** *(string) --*

        The definition of a traffic policy in JSON format. You specify the JSON document to use for
        a new traffic policy in the ``CreateTrafficPolicy`` request. For more information about the
        JSON format, see `Traffic Policy Document Format
        <https://docs.aws.amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html>`__
        .

      - **Comment** *(string) --*

        The comment that you specify in the ``CreateTrafficPolicy`` request, if any.
    """


_ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": str,
    },
    total=False,
)


class ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef(
    _ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
):
    """
    Type definition for `ClientUpdateTrafficPolicyInstanceResponse` `TrafficPolicyInstance`

    A complex type that contains settings for the updated traffic policy instance.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the new traffic policy instance.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that Amazon Route 53 created resource record sets in.

    - **Name** *(string) --*

      The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
      using the resource record sets that are associated with this traffic policy instance.

    - **TTL** *(integer) --*

      The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
      the specified hosted zone.

    - **State** *(string) --*

      The value of ``State`` is one of the following values:

        Applied

      Amazon Route 53 has finished creating resource record sets, and changes have propagated to
      all Route 53 edge locations.

        Creating

      Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
      that the ``CreateTrafficPolicyInstance`` request completed successfully.

        Failed

      Route 53 wasn't able to create or update the resource record sets. When the value of
      ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
      fail.

    - **Message** *(string) --*

      If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
      another value, ``Message`` is empty.

    - **TrafficPolicyId** *(string) --*

      The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
      the specified hosted zone.

    - **TrafficPolicyVersion** *(integer) --*

      The version of the traffic policy that Amazon Route 53 used to create resource record sets
      in the specified hosted zone.

    - **TrafficPolicyType** *(string) --*

      The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
      created for this traffic policy instance.
    """


_ClientUpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "_ClientUpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": ClientUpdateTrafficPolicyInstanceResponseTrafficPolicyInstanceTypeDef
    },
    total=False,
)


class ClientUpdateTrafficPolicyInstanceResponseTypeDef(
    _ClientUpdateTrafficPolicyInstanceResponseTypeDef
):
    """
    Type definition for `ClientUpdateTrafficPolicyInstance` `Response`

    A complex type that contains information about the resource record sets that Amazon Route 53
    created based on a specified traffic policy.

    - **TrafficPolicyInstance** *(dict) --*

      A complex type that contains settings for the updated traffic policy instance.

      - **Id** *(string) --*

        The ID that Amazon Route 53 assigned to the new traffic policy instance.

      - **HostedZoneId** *(string) --*

        The ID of the hosted zone that Amazon Route 53 created resource record sets in.

      - **Name** *(string) --*

        The DNS name, such as www.example.com, for which Amazon Route 53 responds to queries by
        using the resource record sets that are associated with this traffic policy instance.

      - **TTL** *(integer) --*

        The TTL that Amazon Route 53 assigned to all of the resource record sets that it created in
        the specified hosted zone.

      - **State** *(string) --*

        The value of ``State`` is one of the following values:

          Applied

        Amazon Route 53 has finished creating resource record sets, and changes have propagated to
        all Route 53 edge locations.

          Creating

        Route 53 is creating the resource record sets. Use ``GetTrafficPolicyInstance`` to confirm
        that the ``CreateTrafficPolicyInstance`` request completed successfully.

          Failed

        Route 53 wasn't able to create or update the resource record sets. When the value of
        ``State`` is ``Failed`` , see ``Message`` for an explanation of what caused the request to
        fail.

      - **Message** *(string) --*

        If ``State`` is ``Failed`` , an explanation of the reason for the failure. If ``State`` is
        another value, ``Message`` is empty.

      - **TrafficPolicyId** *(string) --*

        The ID of the traffic policy that Amazon Route 53 used to create resource record sets in
        the specified hosted zone.

      - **TrafficPolicyVersion** *(integer) --*

        The version of the traffic policy that Amazon Route 53 used to create resource record sets
        in the specified hosted zone.

      - **TrafficPolicyType** *(string) --*

        The DNS type that Amazon Route 53 assigned to all of the resource record sets that it
        created for this traffic policy instance.
    """


_ListHealthChecksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHealthChecksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHealthChecksPaginatePaginationConfigTypeDef(
    _ListHealthChecksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHealthChecksPaginate` `PaginationConfig`

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


_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfiguration` `Dimensions`

    For the metric that the CloudWatch alarm is associated with, a complex type that
    contains information about one dimension.

    - **Name** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the name of one
      dimension.

    - **Value** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the value of one
      dimension.
    """


_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": str,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": str,
        "Dimensions": List[
            ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationDimensionsTypeDef
        ],
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponseHealthChecks` `CloudWatchAlarmConfiguration`

    A complex type that contains information about the CloudWatch alarm that Amazon Route 53
    is monitoring for this health check.

    - **EvaluationPeriods** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the number of periods that
      the metric is compared to the threshold.

    - **Threshold** *(float) --*

      For the metric that the CloudWatch alarm is associated with, the value the metric is
      compared with.

    - **ComparisonOperator** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the arithmetic operation
      that is used for the comparison.

    - **Period** *(integer) --*

      For the metric that the CloudWatch alarm is associated with, the duration of one
      evaluation period in seconds.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that the alarm is associated with.

    - **Namespace** *(string) --*

      The namespace of the metric that the alarm is associated with. For more information,
      see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

    - **Statistic** *(string) --*

      For the metric that the CloudWatch alarm is associated with, the statistic that is
      applied to the metric.

    - **Dimensions** *(list) --*

      For the metric that the CloudWatch alarm is associated with, a complex type that
      contains information about the dimensions for the metric. For information, see `Amazon
      CloudWatch Namespaces, Dimensions, and Metrics Reference
      <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
      in the *Amazon CloudWatch User Guide* .

      - *(dict) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about one dimension.

        - **Name** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the name of one
          dimension.

        - **Value** *(string) --*

          For the metric that the CloudWatch alarm is associated with, the value of one
          dimension.
    """


_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef",
    {"Region": str, "Name": str},
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponseHealthChecksHealthCheckConfig` `AlarmIdentifier`

    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
    health checkers to use to determine whether the specified health check is healthy.

    - **Region** *(string) --*

      For the CloudWatch alarm that you want Route 53 health checkers to use to determine
      whether this health check is healthy, the region that the alarm was created in.

      For the current list of CloudWatch regions, see `Amazon CloudWatch
      <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
      Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

    - **Name** *(string) --*

      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
      to determine whether this health check is healthy.

      .. note::

        Route 53 supports CloudWatch alarms with the following features:

        * Standard-resolution metrics. High-resolution metrics aren't supported. For more
        information, see `High-Resolution Metrics
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
        in the *Amazon CloudWatch User Guide* .

        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
        aren't supported.
    """


_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "Type": str,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[str],
        "AlarmIdentifier": ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigAlarmIdentifierTypeDef,
        "InsufficientDataHealthStatus": str,
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponseHealthChecks` `HealthCheckConfig`

    A complex type that contains detailed information about one health check.

    - **IPAddress** *(string) --*

      The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
      health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
      request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
      the interval that you specify in ``RequestInterval`` . Using an IP address returned by
      DNS, Route 53 then checks the health of the endpoint.

      Use one of the following formats for the value of ``IPAddress`` :

      * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
      example, ``192.0.2.44`` .

      * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
      for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
      addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

      If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
      associate it with your EC2 instance, and specify the Elastic IP address for
      ``IPAddress`` . This ensures that the IP address of your instance will never change.

      For more information, see `FullyQualifiedDomainName
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
      .

      Constraints: Route 53 can't check the health of endpoints for which the IP address is
      in local, private, non-routable, or multicast ranges. For more information about IP
      addresses for which you can't create health checks, see the following documents:

      * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

      * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
      <https://tools.ietf.org/html/rfc6598>`__

      * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

      When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
      ``IPAddress`` .

    - **Port** *(integer) --*

      The port on the endpoint on which you want Amazon Route 53 to perform health checks.
      Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

    - **Type** *(string) --*

      The type of health check that you want to create, which indicates how Amazon Route 53
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

         If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
         v1.0 or later.

      * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
      body for the string that you specify in ``SearchString`` .

      * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
      Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
      response body for the string that you specify in ``SearchString`` .

      * **TCP** : Route 53 tries to establish a TCP connection.

      * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
      the state of the alarm is ``OK`` , the health check is considered healthy. If the state
      is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
      sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
      check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
      , ``Unhealthy`` , or ``LastKnownStatus`` .

      * **CALCULATED** : For health checks that monitor the status of other health checks,
      Route 53 adds up the number of health checks that Route 53 health checkers consider to
      be healthy and compares that number with the value of ``HealthThreshold`` .

      For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
      <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

    - **ResourcePath** *(string) --*

      The path, if any, that you want Amazon Route 53 to request when performing health
      checks. The path can be any value for which your endpoint will return an HTTP status
      code of 2xx or 3xx when the endpoint is healthy, for example, the file
      /docs/route53-health-check.html. You can also include query string parameters, for
      example, ``/welcome.html?language=jp&login=y`` .

    - **FullyQualifiedDomainName** *(string) --*

      Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

       **If you specify a value for**  ``IPAddress`` :

      Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
      passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
      checks except TCP health checks. This is typically the fully qualified DNS name of the
      endpoint on which you want Route 53 to perform health checks.

      When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
      header:

      * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
      ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
      the Host header.

      * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
      for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
      endpoint in the ``Host`` header.

      * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
      Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
      header.

      If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
      the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

       **If you don't specify a value for ``IPAddress`` ** :

      Route 53 sends a DNS request to the domain that you specify for
      ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
      Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

      .. note::

        If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
        health checks to the endpoint. If there's no resource record set with a type of A for
        the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
        with a "DNS resolution failed" error.

      If you want to check the health of weighted, latency, or failover resource record sets
      and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
      recommend that you create a separate health check for each endpoint. For example,
      create a health check for each HTTP server that is serving content for www.example.com.
      For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
      (such as us-east-2-www.example.com), not the name of the resource record sets
      (www.example.com).

      .. warning::

        In this configuration, if you create a health check for which the value of
        ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
        then associate the health check with those resource record sets, health check results
        will be unpredictable.

      In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
      ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
      ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
      value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
      ``Host`` header.

    - **SearchString** *(string) --*

      If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
      want Amazon Route 53 to search for in the response body from the specified resource. If
      the string appears in the response body, Route 53 considers the resource healthy.

      Route 53 considers case when searching for ``SearchString`` in the response body.

    - **RequestInterval** *(integer) --*

      The number of seconds between the time that Amazon Route 53 gets a response from your
      endpoint and the time that it sends the next health check request. Each Route 53 health
      checker makes requests at this interval.

      .. warning::

        You can't change the value of ``RequestInterval`` after you create a health check.

      If you don't specify a value for ``RequestInterval`` , the default value is ``30``
      seconds.

    - **FailureThreshold** *(integer) --*

      The number of consecutive health checks that an endpoint must pass or fail for Amazon
      Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
      versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
      Healthy
      <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
      in the *Amazon Route 53 Developer Guide* .

      If you don't specify a value for ``FailureThreshold`` , the default value is three
      health checks.

    - **MeasureLatency** *(boolean) --*

      Specify whether you want Amazon Route 53 to measure the latency between health checkers
      in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
      the **Health Checks** page in the Route 53 console.

      .. warning::

        You can't change the value of ``MeasureLatency`` after you create a health check.

    - **Inverted** *(boolean) --*

      Specify whether you want Amazon Route 53 to invert the status of a health check, for
      example, to consider a health check unhealthy when it otherwise would be considered
      healthy.

    - **Disabled** *(boolean) --*

      Stops Route 53 from performing health checks. When you disable a health check, here's
      what happens:

      * **Health checks that check the health of endpoints:** Route 53 stops submitting
      requests to your application, server, or other resource.

      * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
      health checks.

      * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
      corresponding CloudWatch metrics.

      After you disable a health check, Route 53 considers the status of the health check to
      always be healthy. If you configured DNS failover, Route 53 continues to route traffic
      to the corresponding resources. If you want to stop routing traffic to a resource,
      change the value of `Inverted
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
      .

      Charges for a health check still apply when the health check is disabled. For more
      information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

    - **HealthThreshold** *(integer) --*

      The number of child health checks that are associated with a ``CALCULATED`` health
      check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
      be considered healthy. To specify the child health checks that you want to associate
      with a ``CALCULATED`` health check, use the `ChildHealthChecks
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
      element.

      Note the following:

      * If you specify a number greater than the number of child health checks, Route 53
      always considers this health check to be unhealthy.

      * If you specify ``0`` , Route 53 always considers this health check to be healthy.

    - **ChildHealthChecks** *(list) --*

      (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
      element for each health check that you want to associate with a ``CALCULATED`` health
      check.

      - *(string) --*

    - **EnableSNI** *(boolean) --*

      Specify whether you want Amazon Route 53 to send the value of
      ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
      negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
      with the applicable SSL/TLS certificate.

      Some endpoints require that ``HTTPS`` requests include the host name in the
      ``client_hello`` message. If you don't enable SNI, the status of the health check will
      be ``SSL alert handshake_failure`` . A health check can also have that status for other
      reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
      configuration on your endpoint and confirm that your certificate is valid.

      The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
      field and possibly several more in the ``Subject Alternative Names`` field. One of the
      domain names in the certificate should match the value that you specify for
      ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
      with a certificate that does not include the domain name that you specified in
      ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
      attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
      ``client_hello`` message.

    - **Regions** *(list) --*

      A complex type that contains one ``Region`` element for each region from which you want
      Amazon Route 53 health checkers to check the specified endpoint.

      If you don't specify any regions, Route 53 health checkers automatically performs
      checks from all of the regions that are listed under **Valid Values** .

      If you update a health check to remove a region that has been performing health checks,
      Route 53 will briefly continue to perform checks from that region to ensure that some
      health checkers are always checking the endpoint (for example, if you replace three
      regions with four different regions).

      - *(string) --*

    - **AlarmIdentifier** *(dict) --*

      A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
      health checkers to use to determine whether the specified health check is healthy.

      - **Region** *(string) --*

        For the CloudWatch alarm that you want Route 53 health checkers to use to determine
        whether this health check is healthy, the region that the alarm was created in.

        For the current list of CloudWatch regions, see `Amazon CloudWatch
        <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
        Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

      - **Name** *(string) --*

        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
        to determine whether this health check is healthy.

        .. note::

          Route 53 supports CloudWatch alarms with the following features:

          * Standard-resolution metrics. High-resolution metrics aren't supported. For more
          information, see `High-Resolution Metrics
          <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
          in the *Amazon CloudWatch User Guide* .

          * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
          aren't supported.

    - **InsufficientDataHealthStatus** *(string) --*

      When CloudWatch has insufficient data about the metric to determine the alarm state,
      the status that you want Amazon Route 53 to assign to the health check:

      * ``Healthy`` : Route 53 considers the health check to be healthy.

      * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

      * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
      that CloudWatch had sufficient data to determine the alarm state. For new health checks
      that have no last known status, the default status for the health check is healthy.
    """


_ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponseHealthChecks` `LinkedService`

    If the health check was created by another service, the service that created the health
    check. When a health check is created by another service, you can't edit or delete it
    using Amazon Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ListHealthChecksPaginateResponseHealthChecksTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseHealthChecksTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "LinkedService": ListHealthChecksPaginateResponseHealthChecksLinkedServiceTypeDef,
        "HealthCheckConfig": ListHealthChecksPaginateResponseHealthChecksHealthCheckConfigTypeDef,
        "HealthCheckVersion": int,
        "CloudWatchAlarmConfiguration": ListHealthChecksPaginateResponseHealthChecksCloudWatchAlarmConfigurationTypeDef,
    },
    total=False,
)


class ListHealthChecksPaginateResponseHealthChecksTypeDef(
    _ListHealthChecksPaginateResponseHealthChecksTypeDef
):
    """
    Type definition for `ListHealthChecksPaginateResponse` `HealthChecks`

    A complex type that contains information about one health check that is associated with the
    current AWS account.

    - **Id** *(string) --*

      The identifier that Amazon Route 53assigned to the health check when you created it. When
      you add or update a resource record set, you use this value to specify which health check
      to use. The value can be up to 64 characters long.

    - **CallerReference** *(string) --*

      A unique string that you specified when you created the health check.

    - **LinkedService** *(dict) --*

      If the health check was created by another service, the service that created the health
      check. When a health check is created by another service, you can't edit or delete it
      using Amazon Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.

    - **HealthCheckConfig** *(dict) --*

      A complex type that contains detailed information about one health check.

      - **IPAddress** *(string) --*

        The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
        health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
        request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
        the interval that you specify in ``RequestInterval`` . Using an IP address returned by
        DNS, Route 53 then checks the health of the endpoint.

        Use one of the following formats for the value of ``IPAddress`` :

        * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
        example, ``192.0.2.44`` .

        * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
        for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
        addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

        If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
        associate it with your EC2 instance, and specify the Elastic IP address for
        ``IPAddress`` . This ensures that the IP address of your instance will never change.

        For more information, see `FullyQualifiedDomainName
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
        .

        Constraints: Route 53 can't check the health of endpoints for which the IP address is
        in local, private, non-routable, or multicast ranges. For more information about IP
        addresses for which you can't create health checks, see the following documents:

        * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

        * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
        <https://tools.ietf.org/html/rfc6598>`__

        * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

        When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
        ``IPAddress`` .

      - **Port** *(integer) --*

        The port on the endpoint on which you want Amazon Route 53 to perform health checks.
        Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

      - **Type** *(string) --*

        The type of health check that you want to create, which indicates how Amazon Route 53
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

           If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
           v1.0 or later.

        * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
        body for the string that you specify in ``SearchString`` .

        * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
        Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
        response body for the string that you specify in ``SearchString`` .

        * **TCP** : Route 53 tries to establish a TCP connection.

        * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
        the state of the alarm is ``OK`` , the health check is considered healthy. If the state
        is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
        sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
        check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
        , ``Unhealthy`` , or ``LastKnownStatus`` .

        * **CALCULATED** : For health checks that monitor the status of other health checks,
        Route 53 adds up the number of health checks that Route 53 health checkers consider to
        be healthy and compares that number with the value of ``HealthThreshold`` .

        For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
        <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

      - **ResourcePath** *(string) --*

        The path, if any, that you want Amazon Route 53 to request when performing health
        checks. The path can be any value for which your endpoint will return an HTTP status
        code of 2xx or 3xx when the endpoint is healthy, for example, the file
        /docs/route53-health-check.html. You can also include query string parameters, for
        example, ``/welcome.html?language=jp&login=y`` .

      - **FullyQualifiedDomainName** *(string) --*

        Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

         **If you specify a value for**  ``IPAddress`` :

        Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
        passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
        checks except TCP health checks. This is typically the fully qualified DNS name of the
        endpoint on which you want Route 53 to perform health checks.

        When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
        header:

        * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
        ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
        the Host header.

        * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
        for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
        endpoint in the ``Host`` header.

        * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
        Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
        header.

        If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
        the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

         **If you don't specify a value for ``IPAddress`` ** :

        Route 53 sends a DNS request to the domain that you specify for
        ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
        Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

        .. note::

          If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
          health checks to the endpoint. If there's no resource record set with a type of A for
          the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
          with a "DNS resolution failed" error.

        If you want to check the health of weighted, latency, or failover resource record sets
        and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
        recommend that you create a separate health check for each endpoint. For example,
        create a health check for each HTTP server that is serving content for www.example.com.
        For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
        (such as us-east-2-www.example.com), not the name of the resource record sets
        (www.example.com).

        .. warning::

          In this configuration, if you create a health check for which the value of
          ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
          then associate the health check with those resource record sets, health check results
          will be unpredictable.

        In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
        ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
        ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
        value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
        ``Host`` header.

      - **SearchString** *(string) --*

        If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
        want Amazon Route 53 to search for in the response body from the specified resource. If
        the string appears in the response body, Route 53 considers the resource healthy.

        Route 53 considers case when searching for ``SearchString`` in the response body.

      - **RequestInterval** *(integer) --*

        The number of seconds between the time that Amazon Route 53 gets a response from your
        endpoint and the time that it sends the next health check request. Each Route 53 health
        checker makes requests at this interval.

        .. warning::

          You can't change the value of ``RequestInterval`` after you create a health check.

        If you don't specify a value for ``RequestInterval`` , the default value is ``30``
        seconds.

      - **FailureThreshold** *(integer) --*

        The number of consecutive health checks that an endpoint must pass or fail for Amazon
        Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
        versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
        Healthy
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
        in the *Amazon Route 53 Developer Guide* .

        If you don't specify a value for ``FailureThreshold`` , the default value is three
        health checks.

      - **MeasureLatency** *(boolean) --*

        Specify whether you want Amazon Route 53 to measure the latency between health checkers
        in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
        the **Health Checks** page in the Route 53 console.

        .. warning::

          You can't change the value of ``MeasureLatency`` after you create a health check.

      - **Inverted** *(boolean) --*

        Specify whether you want Amazon Route 53 to invert the status of a health check, for
        example, to consider a health check unhealthy when it otherwise would be considered
        healthy.

      - **Disabled** *(boolean) --*

        Stops Route 53 from performing health checks. When you disable a health check, here's
        what happens:

        * **Health checks that check the health of endpoints:** Route 53 stops submitting
        requests to your application, server, or other resource.

        * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
        health checks.

        * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
        corresponding CloudWatch metrics.

        After you disable a health check, Route 53 considers the status of the health check to
        always be healthy. If you configured DNS failover, Route 53 continues to route traffic
        to the corresponding resources. If you want to stop routing traffic to a resource,
        change the value of `Inverted
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
        .

        Charges for a health check still apply when the health check is disabled. For more
        information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

      - **HealthThreshold** *(integer) --*

        The number of child health checks that are associated with a ``CALCULATED`` health
        check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
        be considered healthy. To specify the child health checks that you want to associate
        with a ``CALCULATED`` health check, use the `ChildHealthChecks
        <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
        element.

        Note the following:

        * If you specify a number greater than the number of child health checks, Route 53
        always considers this health check to be unhealthy.

        * If you specify ``0`` , Route 53 always considers this health check to be healthy.

      - **ChildHealthChecks** *(list) --*

        (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
        element for each health check that you want to associate with a ``CALCULATED`` health
        check.

        - *(string) --*

      - **EnableSNI** *(boolean) --*

        Specify whether you want Amazon Route 53 to send the value of
        ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
        negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
        with the applicable SSL/TLS certificate.

        Some endpoints require that ``HTTPS`` requests include the host name in the
        ``client_hello`` message. If you don't enable SNI, the status of the health check will
        be ``SSL alert handshake_failure`` . A health check can also have that status for other
        reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
        configuration on your endpoint and confirm that your certificate is valid.

        The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
        field and possibly several more in the ``Subject Alternative Names`` field. One of the
        domain names in the certificate should match the value that you specify for
        ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
        with a certificate that does not include the domain name that you specified in
        ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
        attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
        ``client_hello`` message.

      - **Regions** *(list) --*

        A complex type that contains one ``Region`` element for each region from which you want
        Amazon Route 53 health checkers to check the specified endpoint.

        If you don't specify any regions, Route 53 health checkers automatically performs
        checks from all of the regions that are listed under **Valid Values** .

        If you update a health check to remove a region that has been performing health checks,
        Route 53 will briefly continue to perform checks from that region to ensure that some
        health checkers are always checking the endpoint (for example, if you replace three
        regions with four different regions).

        - *(string) --*

      - **AlarmIdentifier** *(dict) --*

        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
        health checkers to use to determine whether the specified health check is healthy.

        - **Region** *(string) --*

          For the CloudWatch alarm that you want Route 53 health checkers to use to determine
          whether this health check is healthy, the region that the alarm was created in.

          For the current list of CloudWatch regions, see `Amazon CloudWatch
          <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
          Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

        - **Name** *(string) --*

          The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
          to determine whether this health check is healthy.

          .. note::

            Route 53 supports CloudWatch alarms with the following features:

            * Standard-resolution metrics. High-resolution metrics aren't supported. For more
            information, see `High-Resolution Metrics
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
            in the *Amazon CloudWatch User Guide* .

            * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
            aren't supported.

      - **InsufficientDataHealthStatus** *(string) --*

        When CloudWatch has insufficient data about the metric to determine the alarm state,
        the status that you want Amazon Route 53 to assign to the health check:

        * ``Healthy`` : Route 53 considers the health check to be healthy.

        * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

        * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
        that CloudWatch had sufficient data to determine the alarm state. For new health checks
        that have no last known status, the default status for the health check is healthy.

    - **HealthCheckVersion** *(integer) --*

      The version of the health check. You can optionally pass this value in a call to
      ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

    - **CloudWatchAlarmConfiguration** *(dict) --*

      A complex type that contains information about the CloudWatch alarm that Amazon Route 53
      is monitoring for this health check.

      - **EvaluationPeriods** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the number of periods that
        the metric is compared to the threshold.

      - **Threshold** *(float) --*

        For the metric that the CloudWatch alarm is associated with, the value the metric is
        compared with.

      - **ComparisonOperator** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the arithmetic operation
        that is used for the comparison.

      - **Period** *(integer) --*

        For the metric that the CloudWatch alarm is associated with, the duration of one
        evaluation period in seconds.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that the alarm is associated with.

      - **Namespace** *(string) --*

        The namespace of the metric that the alarm is associated with. For more information,
        see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

      - **Statistic** *(string) --*

        For the metric that the CloudWatch alarm is associated with, the statistic that is
        applied to the metric.

      - **Dimensions** *(list) --*

        For the metric that the CloudWatch alarm is associated with, a complex type that
        contains information about the dimensions for the metric. For information, see `Amazon
        CloudWatch Namespaces, Dimensions, and Metrics Reference
        <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
        in the *Amazon CloudWatch User Guide* .

        - *(dict) --*

          For the metric that the CloudWatch alarm is associated with, a complex type that
          contains information about one dimension.

          - **Name** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the name of one
            dimension.

          - **Value** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the value of one
            dimension.
    """


_ListHealthChecksPaginateResponseTypeDef = TypedDict(
    "_ListHealthChecksPaginateResponseTypeDef",
    {
        "HealthChecks": List[ListHealthChecksPaginateResponseHealthChecksTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListHealthChecksPaginateResponseTypeDef(_ListHealthChecksPaginateResponseTypeDef):
    """
    Type definition for `ListHealthChecksPaginate` `Response`

    A complex type that contains the response to a ``ListHealthChecks`` request.

    - **HealthChecks** *(list) --*

      A complex type that contains one ``HealthCheck`` element for each health check that is
      associated with the current AWS account.

      - *(dict) --*

        A complex type that contains information about one health check that is associated with the
        current AWS account.

        - **Id** *(string) --*

          The identifier that Amazon Route 53assigned to the health check when you created it. When
          you add or update a resource record set, you use this value to specify which health check
          to use. The value can be up to 64 characters long.

        - **CallerReference** *(string) --*

          A unique string that you specified when you created the health check.

        - **LinkedService** *(dict) --*

          If the health check was created by another service, the service that created the health
          check. When a health check is created by another service, you can't edit or delete it
          using Amazon Route 53.

          - **ServicePrincipal** *(string) --*

            If the health check or hosted zone was created by another service, the service that
            created the resource. When a resource is created by another service, you can't edit or
            delete it using Amazon Route 53.

          - **Description** *(string) --*

            If the health check or hosted zone was created by another service, an optional
            description that can be provided by the other service. When a resource is created by
            another service, you can't edit or delete it using Amazon Route 53.

        - **HealthCheckConfig** *(dict) --*

          A complex type that contains detailed information about one health check.

          - **IPAddress** *(string) --*

            The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform
            health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS
            request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at
            the interval that you specify in ``RequestInterval`` . Using an IP address returned by
            DNS, Route 53 then checks the health of the endpoint.

            Use one of the following formats for the value of ``IPAddress`` :

            * **IPv4 address** : four values between 0 and 255, separated by periods (.), for
            example, ``192.0.2.44`` .

            * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:),
            for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6
            addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

            If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address,
            associate it with your EC2 instance, and specify the Elastic IP address for
            ``IPAddress`` . This ensures that the IP address of your instance will never change.

            For more information, see `FullyQualifiedDomainName
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`__
            .

            Constraints: Route 53 can't check the health of endpoints for which the IP address is
            in local, private, non-routable, or multicast ranges. For more information about IP
            addresses for which you can't create health checks, see the following documents:

            * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__

            * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space
            <https://tools.ietf.org/html/rfc6598>`__

            * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__

            When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit
            ``IPAddress`` .

          - **Port** *(integer) --*

            The port on the endpoint on which you want Amazon Route 53 to perform health checks.
            Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .

          - **Type** *(string) --*

            The type of health check that you want to create, which indicates how Amazon Route 53
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

               If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS
               v1.0 or later.

            * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
            Route 53 submits an HTTP request and searches the first 5,120 bytes of the response
            body for the string that you specify in ``SearchString`` .

            * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful,
            Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the
            response body for the string that you specify in ``SearchString`` .

            * **TCP** : Route 53 tries to establish a TCP connection.

            * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If
            the state of the alarm is ``OK`` , the health check is considered healthy. If the state
            is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have
            sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health
            check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy``
            , ``Unhealthy`` , or ``LastKnownStatus`` .

            * **CALCULATED** : For health checks that monitor the status of other health checks,
            Route 53 adds up the number of health checks that Route 53 health checkers consider to
            be healthy and compares that number with the value of ``HealthThreshold`` .

            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy
            <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Amazon Route 53 Developer Guide* .

          - **ResourcePath** *(string) --*

            The path, if any, that you want Amazon Route 53 to request when performing health
            checks. The path can be any value for which your endpoint will return an HTTP status
            code of 2xx or 3xx when the endpoint is healthy, for example, the file
            /docs/route53-health-check.html. You can also include query string parameters, for
            example, ``/welcome.html?language=jp&login=y`` .

          - **FullyQualifiedDomainName** *(string) --*

            Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

             **If you specify a value for**  ``IPAddress`` :

            Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and
            passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health
            checks except TCP health checks. This is typically the fully qualified DNS name of the
            endpoint on which you want Route 53 to perform health checks.

            When Route 53 checks the health of an endpoint, here is how it constructs the ``Host``
            header:

            * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for
            ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in
            the Host header.

            * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH``
            for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the
            endpoint in the ``Host`` header.

            * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` ,
            Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host``
            header.

            If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes
            the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

             **If you don't specify a value for ``IPAddress`` ** :

            Route 53 sends a DNS request to the domain that you specify for
            ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` .
            Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.

            .. note::

              If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send
              health checks to the endpoint. If there's no resource record set with a type of A for
              the name that you specify for ``FullyQualifiedDomainName`` , the health check fails
              with a "DNS resolution failed" error.

            If you want to check the health of weighted, latency, or failover resource record sets
            and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we
            recommend that you create a separate health check for each endpoint. For example,
            create a health check for each HTTP server that is serving content for www.example.com.
            For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server
            (such as us-east-2-www.example.com), not the name of the resource record sets
            (www.example.com).

            .. warning::

              In this configuration, if you create a health check for which the value of
              ``FullyQualifiedDomainName`` matches the name of the resource record sets and you
              then associate the health check with those resource record sets, health check results
              will be unpredictable.

            In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` ,
            ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of
            ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a
            value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a
            ``Host`` header.

          - **SearchString** *(string) --*

            If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you
            want Amazon Route 53 to search for in the response body from the specified resource. If
            the string appears in the response body, Route 53 considers the resource healthy.

            Route 53 considers case when searching for ``SearchString`` in the response body.

          - **RequestInterval** *(integer) --*

            The number of seconds between the time that Amazon Route 53 gets a response from your
            endpoint and the time that it sends the next health check request. Each Route 53 health
            checker makes requests at this interval.

            .. warning::

              You can't change the value of ``RequestInterval`` after you create a health check.

            If you don't specify a value for ``RequestInterval`` , the default value is ``30``
            seconds.

          - **FailureThreshold** *(integer) --*

            The number of consecutive health checks that an endpoint must pass or fail for Amazon
            Route 53 to change the current status of the endpoint from unhealthy to healthy or vice
            versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is
            Healthy
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__
            in the *Amazon Route 53 Developer Guide* .

            If you don't specify a value for ``FailureThreshold`` , the default value is three
            health checks.

          - **MeasureLatency** *(boolean) --*

            Specify whether you want Amazon Route 53 to measure the latency between health checkers
            in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on
            the **Health Checks** page in the Route 53 console.

            .. warning::

              You can't change the value of ``MeasureLatency`` after you create a health check.

          - **Inverted** *(boolean) --*

            Specify whether you want Amazon Route 53 to invert the status of a health check, for
            example, to consider a health check unhealthy when it otherwise would be considered
            healthy.

          - **Disabled** *(boolean) --*

            Stops Route 53 from performing health checks. When you disable a health check, here's
            what happens:

            * **Health checks that check the health of endpoints:** Route 53 stops submitting
            requests to your application, server, or other resource.

            * **Calculated health checks:** Route 53 stops aggregating the status of the referenced
            health checks.

            * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the
            corresponding CloudWatch metrics.

            After you disable a health check, Route 53 considers the status of the health check to
            always be healthy. If you configured DNS failover, Route 53 continues to route traffic
            to the corresponding resources. If you want to stop routing traffic to a resource,
            change the value of `Inverted
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-Inverted>`__
            .

            Charges for a health check still apply when the health check is disabled. For more
            information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .

          - **HealthThreshold** *(integer) --*

            The number of child health checks that are associated with a ``CALCULATED`` health
            check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to
            be considered healthy. To specify the child health checks that you want to associate
            with a ``CALCULATED`` health check, use the `ChildHealthChecks
            <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`__
            element.

            Note the following:

            * If you specify a number greater than the number of child health checks, Route 53
            always considers this health check to be unhealthy.

            * If you specify ``0`` , Route 53 always considers this health check to be healthy.

          - **ChildHealthChecks** *(list) --*

            (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck``
            element for each health check that you want to associate with a ``CALCULATED`` health
            check.

            - *(string) --*

          - **EnableSNI** *(boolean) --*

            Specify whether you want Amazon Route 53 to send the value of
            ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS
            negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests
            with the applicable SSL/TLS certificate.

            Some endpoints require that ``HTTPS`` requests include the host name in the
            ``client_hello`` message. If you don't enable SNI, the status of the health check will
            be ``SSL alert handshake_failure`` . A health check can also have that status for other
            reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS
            configuration on your endpoint and confirm that your certificate is valid.

            The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name``
            field and possibly several more in the ``Subject Alternative Names`` field. One of the
            domain names in the certificate should match the value that you specify for
            ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message
            with a certificate that does not include the domain name that you specified in
            ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second
            attempt, the health checker will omit ``FullyQualifiedDomainName`` from the
            ``client_hello`` message.

          - **Regions** *(list) --*

            A complex type that contains one ``Region`` element for each region from which you want
            Amazon Route 53 health checkers to check the specified endpoint.

            If you don't specify any regions, Route 53 health checkers automatically performs
            checks from all of the regions that are listed under **Valid Values** .

            If you update a health check to remove a region that has been performing health checks,
            Route 53 will briefly continue to perform checks from that region to ensure that some
            health checkers are always checking the endpoint (for example, if you replace three
            regions with four different regions).

            - *(string) --*

          - **AlarmIdentifier** *(dict) --*

            A complex type that identifies the CloudWatch alarm that you want Amazon Route 53
            health checkers to use to determine whether the specified health check is healthy.

            - **Region** *(string) --*

              For the CloudWatch alarm that you want Route 53 health checkers to use to determine
              whether this health check is healthy, the region that the alarm was created in.

              For the current list of CloudWatch regions, see `Amazon CloudWatch
              <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS
              Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .

            - **Name** *(string) --*

              The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use
              to determine whether this health check is healthy.

              .. note::

                Route 53 supports CloudWatch alarms with the following features:

                * Standard-resolution metrics. High-resolution metrics aren't supported. For more
                information, see `High-Resolution Metrics
                <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__
                in the *Amazon CloudWatch User Guide* .

                * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics
                aren't supported.

          - **InsufficientDataHealthStatus** *(string) --*

            When CloudWatch has insufficient data about the metric to determine the alarm state,
            the status that you want Amazon Route 53 to assign to the health check:

            * ``Healthy`` : Route 53 considers the health check to be healthy.

            * ``Unhealthy`` : Route 53 considers the health check to be unhealthy.

            * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time
            that CloudWatch had sufficient data to determine the alarm state. For new health checks
            that have no last known status, the default status for the health check is healthy.

        - **HealthCheckVersion** *(integer) --*

          The version of the health check. You can optionally pass this value in a call to
          ``UpdateHealthCheck`` to prevent overwriting another change to the health check.

        - **CloudWatchAlarmConfiguration** *(dict) --*

          A complex type that contains information about the CloudWatch alarm that Amazon Route 53
          is monitoring for this health check.

          - **EvaluationPeriods** *(integer) --*

            For the metric that the CloudWatch alarm is associated with, the number of periods that
            the metric is compared to the threshold.

          - **Threshold** *(float) --*

            For the metric that the CloudWatch alarm is associated with, the value the metric is
            compared with.

          - **ComparisonOperator** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the arithmetic operation
            that is used for the comparison.

          - **Period** *(integer) --*

            For the metric that the CloudWatch alarm is associated with, the duration of one
            evaluation period in seconds.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that the alarm is associated with.

          - **Namespace** *(string) --*

            The namespace of the metric that the alarm is associated with. For more information,
            see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
            in the *Amazon CloudWatch User Guide* .

          - **Statistic** *(string) --*

            For the metric that the CloudWatch alarm is associated with, the statistic that is
            applied to the metric.

          - **Dimensions** *(list) --*

            For the metric that the CloudWatch alarm is associated with, a complex type that
            contains information about the dimensions for the metric. For information, see `Amazon
            CloudWatch Namespaces, Dimensions, and Metrics Reference
            <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__
            in the *Amazon CloudWatch User Guide* .

            - *(dict) --*

              For the metric that the CloudWatch alarm is associated with, a complex type that
              contains information about one dimension.

              - **Name** *(string) --*

                For the metric that the CloudWatch alarm is associated with, the name of one
                dimension.

              - **Value** *(string) --*

                For the metric that the CloudWatch alarm is associated with, the value of one
                dimension.

    - **Marker** *(string) --*

      For the second and subsequent calls to ``ListHealthChecks`` , ``Marker`` is the value that
      you specified for the ``marker`` parameter in the previous request.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether there are more health checks to be listed. If the response was
      truncated, you can get the next group of health checks by submitting another
      ``ListHealthChecks`` request and specifying the value of ``NextMarker`` in the ``marker``
      parameter.

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListHealthChecks`` that produced the current response.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListHostedZonesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHostedZonesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHostedZonesPaginatePaginationConfigTypeDef(
    _ListHostedZonesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHostedZonesPaginate` `PaginationConfig`

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


_ListHostedZonesPaginateResponseHostedZonesConfigTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesConfigTypeDef",
    {"Comment": str, "PrivateZone": bool},
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesConfigTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesConfigTypeDef
):
    """
    Type definition for `ListHostedZonesPaginateResponseHostedZones` `Config`

    A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
    the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
    ``Comment`` elements don't appear in the response.

    - **Comment** *(string) --*

      Any comments that you want to include about the hosted zone.

    - **PrivateZone** *(boolean) --*

      A value that indicates whether this is a private hosted zone.
    """


_ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef",
    {"ServicePrincipal": str, "Description": str},
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef
):
    """
    Type definition for `ListHostedZonesPaginateResponseHostedZones` `LinkedService`

    If the hosted zone was created by another service, the service that created the hosted
    zone. When a hosted zone is created by another service, you can't edit or delete it using
    Route 53.

    - **ServicePrincipal** *(string) --*

      If the health check or hosted zone was created by another service, the service that
      created the resource. When a resource is created by another service, you can't edit or
      delete it using Amazon Route 53.

    - **Description** *(string) --*

      If the health check or hosted zone was created by another service, an optional
      description that can be provided by the other service. When a resource is created by
      another service, you can't edit or delete it using Amazon Route 53.
    """


_ListHostedZonesPaginateResponseHostedZonesTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseHostedZonesTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
        "Config": ListHostedZonesPaginateResponseHostedZonesConfigTypeDef,
        "ResourceRecordSetCount": int,
        "LinkedService": ListHostedZonesPaginateResponseHostedZonesLinkedServiceTypeDef,
    },
    total=False,
)


class ListHostedZonesPaginateResponseHostedZonesTypeDef(
    _ListHostedZonesPaginateResponseHostedZonesTypeDef
):
    """
    Type definition for `ListHostedZonesPaginateResponse` `HostedZones`

    A complex type that contains general information about the hosted zone.

    - **Id** *(string) --*

      The ID that Amazon Route 53 assigned to the hosted zone when you created it.

    - **Name** *(string) --*

      The name of the domain. For public hosted zones, this is the name that you have
      registered with your DNS registrar.

      For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
      (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

    - **CallerReference** *(string) --*

      The value that you specified for ``CallerReference`` when you created the hosted zone.

    - **Config** *(dict) --*

      A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
      the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
      ``Comment`` elements don't appear in the response.

      - **Comment** *(string) --*

        Any comments that you want to include about the hosted zone.

      - **PrivateZone** *(boolean) --*

        A value that indicates whether this is a private hosted zone.

    - **ResourceRecordSetCount** *(integer) --*

      The number of resource record sets in the hosted zone.

    - **LinkedService** *(dict) --*

      If the hosted zone was created by another service, the service that created the hosted
      zone. When a hosted zone is created by another service, you can't edit or delete it using
      Route 53.

      - **ServicePrincipal** *(string) --*

        If the health check or hosted zone was created by another service, the service that
        created the resource. When a resource is created by another service, you can't edit or
        delete it using Amazon Route 53.

      - **Description** *(string) --*

        If the health check or hosted zone was created by another service, an optional
        description that can be provided by the other service. When a resource is created by
        another service, you can't edit or delete it using Amazon Route 53.
    """


_ListHostedZonesPaginateResponseTypeDef = TypedDict(
    "_ListHostedZonesPaginateResponseTypeDef",
    {
        "HostedZones": List[ListHostedZonesPaginateResponseHostedZonesTypeDef],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)


class ListHostedZonesPaginateResponseTypeDef(_ListHostedZonesPaginateResponseTypeDef):
    """
    Type definition for `ListHostedZonesPaginate` `Response`

    - **HostedZones** *(list) --*

      A complex type that contains general information about the hosted zone.

      - *(dict) --*

        A complex type that contains general information about the hosted zone.

        - **Id** *(string) --*

          The ID that Amazon Route 53 assigned to the hosted zone when you created it.

        - **Name** *(string) --*

          The name of the domain. For public hosted zones, this is the name that you have
          registered with your DNS registrar.

          For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-``
          (hyphen) and how to specify internationalized domain names, see `CreateHostedZone
          <https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html>`__ .

        - **CallerReference** *(string) --*

          The value that you specified for ``CallerReference`` when you created the hosted zone.

        - **Config** *(dict) --*

          A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted
          the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and
          ``Comment`` elements don't appear in the response.

          - **Comment** *(string) --*

            Any comments that you want to include about the hosted zone.

          - **PrivateZone** *(boolean) --*

            A value that indicates whether this is a private hosted zone.

        - **ResourceRecordSetCount** *(integer) --*

          The number of resource record sets in the hosted zone.

        - **LinkedService** *(dict) --*

          If the hosted zone was created by another service, the service that created the hosted
          zone. When a hosted zone is created by another service, you can't edit or delete it using
          Route 53.

          - **ServicePrincipal** *(string) --*

            If the health check or hosted zone was created by another service, the service that
            created the resource. When a resource is created by another service, you can't edit or
            delete it using Amazon Route 53.

          - **Description** *(string) --*

            If the health check or hosted zone was created by another service, an optional
            description that can be provided by the other service. When a resource is created by
            another service, you can't edit or delete it using Amazon Route 53.

    - **Marker** *(string) --*

      For the second and subsequent calls to ``ListHostedZones`` , ``Marker`` is the value that you
      specified for the ``marker`` parameter in the request that produced the current response.

    - **IsTruncated** *(boolean) --*

      A flag indicating whether there are more hosted zones to be listed. If the response was
      truncated, you can get more hosted zones by submitting another ``ListHostedZones`` request
      and specifying the value of ``NextMarker`` in the ``marker`` parameter.

    - **MaxItems** *(string) --*

      The value that you specified for the ``maxitems`` parameter in the call to
      ``ListHostedZones`` that produced the current response.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListQueryLoggingConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueryLoggingConfigsPaginatePaginationConfigTypeDef(
    _ListQueryLoggingConfigsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListQueryLoggingConfigsPaginate` `PaginationConfig`

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


_ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef",
    {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str},
    total=False,
)


class ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef(
    _ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef
):
    """
    Type definition for `ListQueryLoggingConfigsPaginateResponse` `QueryLoggingConfigs`

    A complex type that contains information about a configuration for DNS query logging.

    - **Id** *(string) --*

      The ID for a configuration for DNS query logging.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that CloudWatch Logs is logging queries for.

    - **CloudWatchLogsLogGroupArn** *(string) --*

      The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
      publishing logs to.
    """


_ListQueryLoggingConfigsPaginateResponseTypeDef = TypedDict(
    "_ListQueryLoggingConfigsPaginateResponseTypeDef",
    {
        "QueryLoggingConfigs": List[
            ListQueryLoggingConfigsPaginateResponseQueryLoggingConfigsTypeDef
        ]
    },
    total=False,
)


class ListQueryLoggingConfigsPaginateResponseTypeDef(
    _ListQueryLoggingConfigsPaginateResponseTypeDef
):
    """
    Type definition for `ListQueryLoggingConfigsPaginate` `Response`

    - **QueryLoggingConfigs** *(list) --*

      An array that contains one `QueryLoggingConfig
      <https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html>`__
      element for each configuration for DNS query logging that is associated with the current AWS
      account.

      - *(dict) --*

        A complex type that contains information about a configuration for DNS query logging.

        - **Id** *(string) --*

          The ID for a configuration for DNS query logging.

        - **HostedZoneId** *(string) --*

          The ID of the hosted zone that CloudWatch Logs is logging queries for.

        - **CloudWatchLogsLogGroupArn** *(string) --*

          The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is
          publishing logs to.
    """


_ListResourceRecordSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceRecordSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceRecordSetsPaginatePaginationConfigTypeDef(
    _ListResourceRecordSetsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourceRecordSetsPaginate` `PaginationConfig`

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


_ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef(
    _ListVPCAssociationAuthorizationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListVPCAssociationAuthorizationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef",
    {"VPCRegion": str, "VPCId": str},
    total=False,
)


class ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef(
    _ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef
):
    """
    Type definition for `ListVPCAssociationAuthorizationsPaginateResponse` `VPCs`

    (Private hosted zones only) A complex type that contains information about an Amazon VPC.

    - **VPCRegion** *(string) --*

      (Private hosted zones only) The region that an Amazon VPC was created in.

    - **VPCId** *(string) --*

      (Private hosted zones only) The ID of an Amazon VPC.
    """


_ListVPCAssociationAuthorizationsPaginateResponseTypeDef = TypedDict(
    "_ListVPCAssociationAuthorizationsPaginateResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPCs": List[ListVPCAssociationAuthorizationsPaginateResponseVPCsTypeDef],
    },
    total=False,
)


class ListVPCAssociationAuthorizationsPaginateResponseTypeDef(
    _ListVPCAssociationAuthorizationsPaginateResponseTypeDef
):
    """
    Type definition for `ListVPCAssociationAuthorizationsPaginate` `Response`

    A complex type that contains the response information for the request.

    - **HostedZoneId** *(string) --*

      The ID of the hosted zone that you can associate the listed VPCs with.

    - **VPCs** *(list) --*

      The list of VPCs that are authorized to be associated with the specified hosted zone.

      - *(dict) --*

        (Private hosted zones only) A complex type that contains information about an Amazon VPC.

        - **VPCRegion** *(string) --*

          (Private hosted zones only) The region that an Amazon VPC was created in.

        - **VPCId** *(string) --*

          (Private hosted zones only) The ID of an Amazon VPC.
    """


_ResourceRecordSetsChangedWaitWaiterConfigTypeDef = TypedDict(
    "_ResourceRecordSetsChangedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ResourceRecordSetsChangedWaitWaiterConfigTypeDef(
    _ResourceRecordSetsChangedWaitWaiterConfigTypeDef
):
    """
    Type definition for `ResourceRecordSetsChangedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 60
    """
