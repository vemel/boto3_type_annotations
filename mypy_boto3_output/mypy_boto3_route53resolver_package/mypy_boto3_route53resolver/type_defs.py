"Main interface for route53resolver type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    "ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientAssociateResolverRuleResponseTypeDef",
    "ClientCreateResolverEndpointIpAddressesTypeDef",
    "ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientCreateResolverEndpointResponseTypeDef",
    "ClientCreateResolverEndpointTagsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTypeDef",
    "ClientCreateResolverRuleResponseTypeDef",
    "ClientCreateResolverRuleTagsTypeDef",
    "ClientCreateResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    "ClientDeleteResolverEndpointResponseTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    "ClientDeleteResolverRuleResponseTypeDef",
    "ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    "ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientDisassociateResolverRuleResponseTypeDef",
    "ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    "ClientGetResolverEndpointResponseTypeDef",
    "ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    "ClientGetResolverRuleAssociationResponseTypeDef",
    "ClientGetResolverRulePolicyResponseTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTypeDef",
    "ClientGetResolverRuleResponseTypeDef",
    "ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    "ClientListResolverEndpointIpAddressesResponseTypeDef",
    "ClientListResolverEndpointsFiltersTypeDef",
    "ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    "ClientListResolverEndpointsResponseTypeDef",
    "ClientListResolverRuleAssociationsFiltersTypeDef",
    "ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    "ClientListResolverRuleAssociationsResponseTypeDef",
    "ClientListResolverRulesFiltersTypeDef",
    "ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    "ClientListResolverRulesResponseResolverRulesTypeDef",
    "ClientListResolverRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutResolverRulePolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientUpdateResolverEndpointResponseTypeDef",
    "ClientUpdateResolverRuleConfigTargetIpsTypeDef",
    "ClientUpdateResolverRuleConfigTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    "ClientUpdateResolverRuleResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientAssociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)


class ClientAssociateResolverEndpointIpAddressIpAddressTypeDef(
    _ClientAssociateResolverEndpointIpAddressIpAddressTypeDef
):
    """
    Type definition for `ClientAssociateResolverEndpointIpAddress` `IpAddress`

    Either the IPv4 address that you want to add to a resolver endpoint or a subnet ID. If you
    specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the
    specified subnet.

    - **IpId** *(string) --*

       *Only when removing an IP address from a resolver endpoint* : The ID of the IP address that
       you want to remove. To get this ID, use  GetResolverEndpoint .

    - **SubnetId** *(string) --*

      The ID of the subnet that includes the IP address that you want to update. To get this ID, use
      GetResolverEndpoint .

    - **Ip** *(string) --*

      The new IP address.
    """


_ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef(
    _ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientAssociateResolverEndpointIpAddressResponse` `ResolverEndpoint`

    The response to an ``AssociateResolverEndpointIpAddress`` request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientAssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
    },
    total=False,
)


class ClientAssociateResolverEndpointIpAddressResponseTypeDef(
    _ClientAssociateResolverEndpointIpAddressResponseTypeDef
):
    """
    Type definition for `ClientAssociateResolverEndpointIpAddress` `Response`

    - **ResolverEndpoint** *(dict) --*

      The response to an ``AssociateResolverEndpointIpAddress`` request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef(
    _ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef
):
    """
    Type definition for `ClientAssociateResolverRuleResponse` `ResolverRuleAssociation`

    Information about the ``AssociateResolverRule`` request, including the status of the request.

    - **Id** *(string) --*

      The ID of the association between a resolver rule and a VPC. Resolver assigns this value
      when you submit an  AssociateResolverRule request.

    - **ResolverRuleId** *(string) --*

      The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
      .

    - **Name** *(string) --*

      The name of an association between a resolver rule and a VPC.

    - **VPCId** *(string) --*

      The ID of the VPC that you associated the resolver rule with.

    - **Status** *(string) --*

      A code that specifies the current status of the association between a resolver rule and a
      VPC.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientAssociateResolverRuleResponseTypeDef = TypedDict(
    "_ClientAssociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef
    },
    total=False,
)


class ClientAssociateResolverRuleResponseTypeDef(
    _ClientAssociateResolverRuleResponseTypeDef
):
    """
    Type definition for `ClientAssociateResolverRule` `Response`

    - **ResolverRuleAssociation** *(dict) --*

      Information about the ``AssociateResolverRule`` request, including the status of the request.

      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.

      - **ResolverRuleId** *(string) --*

        The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
        .

      - **Name** *(string) --*

        The name of an association between a resolver rule and a VPC.

      - **VPCId** *(string) --*

        The ID of the VPC that you associated the resolver rule with.

      - **Status** *(string) --*

        A code that specifies the current status of the association between a resolver rule and a
        VPC.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the association between a resolver rule and a VPC.
    """


_RequiredClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_RequiredClientCreateResolverEndpointIpAddressesTypeDef", {"SubnetId": str}
)
_OptionalClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_OptionalClientCreateResolverEndpointIpAddressesTypeDef", {"Ip": str}, total=False
)


class ClientCreateResolverEndpointIpAddressesTypeDef(
    _RequiredClientCreateResolverEndpointIpAddressesTypeDef,
    _OptionalClientCreateResolverEndpointIpAddressesTypeDef,
):
    """
    Type definition for `ClientCreateResolverEndpoint` `IpAddresses`

    In an  CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS
    queries.

    - **SubnetId** *(string) --* **[REQUIRED]**

      The subnet that contains the IP address.

    - **Ip** *(string) --*

      The IP address that you want to use for DNS queries.
    """


_ClientCreateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientCreateResolverEndpointResponseResolverEndpointTypeDef(
    _ClientCreateResolverEndpointResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientCreateResolverEndpointResponse` `ResolverEndpoint`

    Information about the ``CreateResolverEndpoint`` request, including the status of the request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientCreateResolverEndpointResponseTypeDef = TypedDict(
    "_ClientCreateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientCreateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientCreateResolverEndpointResponseTypeDef(
    _ClientCreateResolverEndpointResponseTypeDef
):
    """
    Type definition for `ClientCreateResolverEndpoint` `Response`

    - **ResolverEndpoint** *(dict) --*

      Information about the ``CreateResolverEndpoint`` request, including the status of the request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_ClientCreateResolverEndpointTagsTypeDef = TypedDict(
    "_ClientCreateResolverEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateResolverEndpointTagsTypeDef(_ClientCreateResolverEndpointTagsTypeDef):
    """
    Type definition for `ClientCreateResolverEndpoint` `Tags`

    One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name for
    the tag) and a ``Value`` .

    - **Key** *(string) --*

      The name for the tag. For example, if you want to associate Resolver resources with the
      account IDs of your customers for billing purposes, the value of ``Key`` might be
      ``account-id`` .

    - **Value** *(string) --*

      The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might be
      the ID of the customer account that you're creating the resource for.
    """


_ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    """
    Type definition for `ClientCreateResolverRuleResponseResolverRule` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
    queries to.

    - **Ip** *(string) --*

      One IP address that you want to forward DNS queries to. You can specify only IPv4
      addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientCreateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": str,
        "StatusMessage": str,
        "RuleType": str,
        "Name": str,
        "TargetIps": List[ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": str,
    },
    total=False,
)


class ClientCreateResolverRuleResponseResolverRuleTypeDef(
    _ClientCreateResolverRuleResponseResolverRuleTypeDef
):
    """
    Type definition for `ClientCreateResolverRuleResponse` `ResolverRule`

    Information about the ``CreateResolverRule`` request, including the status of the request.

    - **Id** *(string) --*

      The ID that Resolver assigned to the resolver rule when you created it.

    - **CreatorRequestId** *(string) --*

      A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
      identifies the request and allows failed requests to be retried without the risk of
      executing the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

    - **DomainName** *(string) --*

      DNS queries for this domain name are forwarded to the IP addresses that are specified in
      ``TargetIps`` . If a query matches multiple resolver rules (example.com and
      www.example.com), the query is routed using the resolver rule that contains the most
      specific domain name (www.example.com).

    - **Status** *(string) --*

      A code that specifies the current status of the resolver rule.

    - **StatusMessage** *(string) --*

      A detailed description of the status of a resolver rule.

    - **RuleType** *(string) --*

      This value is always ``FORWARD`` . Other resolver rule types aren't supported.

    - **Name** *(string) --*

      The name for the resolver rule, which you specified when you created the resolver rule.

    - **TargetIps** *(list) --*

      An array that contains the IP addresses and ports that you want to forward

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
        queries to.

        - **Ip** *(string) --*

          One IP address that you want to forward DNS queries to. You can specify only IPv4
          addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the endpoint that the rule is associated with.

    - **OwnerId** *(string) --*

      When a rule is shared with another AWS account, the account ID of the account that the rule
      is shared with.

    - **ShareStatus** *(string) --*

      Whether the rules is shared and, if so, whether the current account is sharing the rule
      with another account, or another account is sharing the rule with the current account.
    """


_ClientCreateResolverRuleResponseTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientCreateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientCreateResolverRuleResponseTypeDef(_ClientCreateResolverRuleResponseTypeDef):
    """
    Type definition for `ClientCreateResolverRule` `Response`

    - **ResolverRule** *(dict) --*

      Information about the ``CreateResolverRule`` request, including the status of the request.

      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.

      - **CreatorRequestId** *(string) --*

        A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
        identifies the request and allows failed requests to be retried without the risk of
        executing the operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

      - **DomainName** *(string) --*

        DNS queries for this domain name are forwarded to the IP addresses that are specified in
        ``TargetIps`` . If a query matches multiple resolver rules (example.com and
        www.example.com), the query is routed using the resolver rule that contains the most
        specific domain name (www.example.com).

      - **Status** *(string) --*

        A code that specifies the current status of the resolver rule.

      - **StatusMessage** *(string) --*

        A detailed description of the status of a resolver rule.

      - **RuleType** *(string) --*

        This value is always ``FORWARD`` . Other resolver rule types aren't supported.

      - **Name** *(string) --*

        The name for the resolver rule, which you specified when you created the resolver rule.

      - **TargetIps** *(list) --*

        An array that contains the IP addresses and ports that you want to forward

        - *(dict) --*

          In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
          queries to.

          - **Ip** *(string) --*

            One IP address that you want to forward DNS queries to. You can specify only IPv4
            addresses.

          - **Port** *(integer) --*

            The port at ``Ip`` that you want to forward DNS queries to.

      - **ResolverEndpointId** *(string) --*

        The ID of the endpoint that the rule is associated with.

      - **OwnerId** *(string) --*

        When a rule is shared with another AWS account, the account ID of the account that the rule
        is shared with.

      - **ShareStatus** *(string) --*

        Whether the rules is shared and, if so, whether the current account is sharing the rule
        with another account, or another account is sharing the rule with the current account.
    """


_ClientCreateResolverRuleTagsTypeDef = TypedDict(
    "_ClientCreateResolverRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateResolverRuleTagsTypeDef(_ClientCreateResolverRuleTagsTypeDef):
    """
    Type definition for `ClientCreateResolverRule` `Tags`

    One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name for
    the tag) and a ``Value`` .

    - **Key** *(string) --*

      The name for the tag. For example, if you want to associate Resolver resources with the
      account IDs of your customers for billing purposes, the value of ``Key`` might be
      ``account-id`` .

    - **Value** *(string) --*

      The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might be
      the ID of the customer account that you're creating the resource for.
    """


_RequiredClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_RequiredClientCreateResolverRuleTargetIpsTypeDef", {"Ip": str}
)
_OptionalClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_OptionalClientCreateResolverRuleTargetIpsTypeDef", {"Port": int}, total=False
)


class ClientCreateResolverRuleTargetIpsTypeDef(
    _RequiredClientCreateResolverRuleTargetIpsTypeDef,
    _OptionalClientCreateResolverRuleTargetIpsTypeDef,
):
    """
    Type definition for `ClientCreateResolverRule` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

    - **Ip** *(string) --* **[REQUIRED]**

      One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientDeleteResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientDeleteResolverEndpointResponseResolverEndpointTypeDef(
    _ClientDeleteResolverEndpointResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientDeleteResolverEndpointResponse` `ResolverEndpoint`

    Information about the ``DeleteResolverEndpoint`` request, including the status of the request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientDeleteResolverEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientDeleteResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientDeleteResolverEndpointResponseTypeDef(
    _ClientDeleteResolverEndpointResponseTypeDef
):
    """
    Type definition for `ClientDeleteResolverEndpoint` `Response`

    - **ResolverEndpoint** *(dict) --*

      Information about the ``DeleteResolverEndpoint`` request, including the status of the request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    """
    Type definition for `ClientDeleteResolverRuleResponseResolverRule` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
    queries to.

    - **Ip** *(string) --*

      One IP address that you want to forward DNS queries to. You can specify only IPv4
      addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientDeleteResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": str,
        "StatusMessage": str,
        "RuleType": str,
        "Name": str,
        "TargetIps": List[ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": str,
    },
    total=False,
)


class ClientDeleteResolverRuleResponseResolverRuleTypeDef(
    _ClientDeleteResolverRuleResponseResolverRuleTypeDef
):
    """
    Type definition for `ClientDeleteResolverRuleResponse` `ResolverRule`

    Information about the ``DeleteResolverRule`` request, including the status of the request.

    - **Id** *(string) --*

      The ID that Resolver assigned to the resolver rule when you created it.

    - **CreatorRequestId** *(string) --*

      A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
      identifies the request and allows failed requests to be retried without the risk of
      executing the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

    - **DomainName** *(string) --*

      DNS queries for this domain name are forwarded to the IP addresses that are specified in
      ``TargetIps`` . If a query matches multiple resolver rules (example.com and
      www.example.com), the query is routed using the resolver rule that contains the most
      specific domain name (www.example.com).

    - **Status** *(string) --*

      A code that specifies the current status of the resolver rule.

    - **StatusMessage** *(string) --*

      A detailed description of the status of a resolver rule.

    - **RuleType** *(string) --*

      This value is always ``FORWARD`` . Other resolver rule types aren't supported.

    - **Name** *(string) --*

      The name for the resolver rule, which you specified when you created the resolver rule.

    - **TargetIps** *(list) --*

      An array that contains the IP addresses and ports that you want to forward

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
        queries to.

        - **Ip** *(string) --*

          One IP address that you want to forward DNS queries to. You can specify only IPv4
          addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the endpoint that the rule is associated with.

    - **OwnerId** *(string) --*

      When a rule is shared with another AWS account, the account ID of the account that the rule
      is shared with.

    - **ShareStatus** *(string) --*

      Whether the rules is shared and, if so, whether the current account is sharing the rule
      with another account, or another account is sharing the rule with the current account.
    """


_ClientDeleteResolverRuleResponseTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseTypeDef",
    {"ResolverRule": ClientDeleteResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientDeleteResolverRuleResponseTypeDef(_ClientDeleteResolverRuleResponseTypeDef):
    """
    Type definition for `ClientDeleteResolverRule` `Response`

    - **ResolverRule** *(dict) --*

      Information about the ``DeleteResolverRule`` request, including the status of the request.

      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.

      - **CreatorRequestId** *(string) --*

        A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
        identifies the request and allows failed requests to be retried without the risk of
        executing the operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

      - **DomainName** *(string) --*

        DNS queries for this domain name are forwarded to the IP addresses that are specified in
        ``TargetIps`` . If a query matches multiple resolver rules (example.com and
        www.example.com), the query is routed using the resolver rule that contains the most
        specific domain name (www.example.com).

      - **Status** *(string) --*

        A code that specifies the current status of the resolver rule.

      - **StatusMessage** *(string) --*

        A detailed description of the status of a resolver rule.

      - **RuleType** *(string) --*

        This value is always ``FORWARD`` . Other resolver rule types aren't supported.

      - **Name** *(string) --*

        The name for the resolver rule, which you specified when you created the resolver rule.

      - **TargetIps** *(list) --*

        An array that contains the IP addresses and ports that you want to forward

        - *(dict) --*

          In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
          queries to.

          - **Ip** *(string) --*

            One IP address that you want to forward DNS queries to. You can specify only IPv4
            addresses.

          - **Port** *(integer) --*

            The port at ``Ip`` that you want to forward DNS queries to.

      - **ResolverEndpointId** *(string) --*

        The ID of the endpoint that the rule is associated with.

      - **OwnerId** *(string) --*

        When a rule is shared with another AWS account, the account ID of the account that the rule
        is shared with.

      - **ShareStatus** *(string) --*

        Whether the rules is shared and, if so, whether the current account is sharing the rule
        with another account, or another account is sharing the rule with the current account.
    """


_ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef(
    _ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef
):
    """
    Type definition for `ClientDisassociateResolverEndpointIpAddress` `IpAddress`

    The IPv4 address that you want to remove from a resolver endpoint.

    - **IpId** *(string) --*

       *Only when removing an IP address from a resolver endpoint* : The ID of the IP address that
       you want to remove. To get this ID, use  GetResolverEndpoint .

    - **SubnetId** *(string) --*

      The ID of the subnet that includes the IP address that you want to update. To get this ID, use
      GetResolverEndpoint .

    - **Ip** *(string) --*

      The new IP address.
    """


_ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef(
    _ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientDisassociateResolverEndpointIpAddressResponse` `ResolverEndpoint`

    The response to an ``DisassociateResolverEndpointIpAddress`` request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientDisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
    },
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressResponseTypeDef(
    _ClientDisassociateResolverEndpointIpAddressResponseTypeDef
):
    """
    Type definition for `ClientDisassociateResolverEndpointIpAddress` `Response`

    - **ResolverEndpoint** *(dict) --*

      The response to an ``DisassociateResolverEndpointIpAddress`` request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef(
    _ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef
):
    """
    Type definition for `ClientDisassociateResolverRuleResponse` `ResolverRuleAssociation`

    Information about the ``DisassociateResolverRule`` request, including the status of the
    request.

    - **Id** *(string) --*

      The ID of the association between a resolver rule and a VPC. Resolver assigns this value
      when you submit an  AssociateResolverRule request.

    - **ResolverRuleId** *(string) --*

      The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
      .

    - **Name** *(string) --*

      The name of an association between a resolver rule and a VPC.

    - **VPCId** *(string) --*

      The ID of the VPC that you associated the resolver rule with.

    - **Status** *(string) --*

      A code that specifies the current status of the association between a resolver rule and a
      VPC.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientDisassociateResolverRuleResponseTypeDef = TypedDict(
    "_ClientDisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef
    },
    total=False,
)


class ClientDisassociateResolverRuleResponseTypeDef(
    _ClientDisassociateResolverRuleResponseTypeDef
):
    """
    Type definition for `ClientDisassociateResolverRule` `Response`

    - **ResolverRuleAssociation** *(dict) --*

      Information about the ``DisassociateResolverRule`` request, including the status of the
      request.

      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.

      - **ResolverRuleId** *(string) --*

        The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
        .

      - **Name** *(string) --*

        The name of an association between a resolver rule and a VPC.

      - **VPCId** *(string) --*

        The ID of the VPC that you associated the resolver rule with.

      - **Status** *(string) --*

        A code that specifies the current status of the association between a resolver rule and a
        VPC.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientGetResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientGetResolverEndpointResponseResolverEndpointTypeDef(
    _ClientGetResolverEndpointResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientGetResolverEndpointResponse` `ResolverEndpoint`

    Information about the resolver endpoint that you specified in a ``GetResolverEndpoint``
    request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientGetResolverEndpointResponseTypeDef = TypedDict(
    "_ClientGetResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientGetResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientGetResolverEndpointResponseTypeDef(
    _ClientGetResolverEndpointResponseTypeDef
):
    """
    Type definition for `ClientGetResolverEndpoint` `Response`

    - **ResolverEndpoint** *(dict) --*

      Information about the resolver endpoint that you specified in a ``GetResolverEndpoint``
      request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef(
    _ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef
):
    """
    Type definition for `ClientGetResolverRuleAssociationResponse` `ResolverRuleAssociation`

    Information about the resolver rule association that you specified in a
    ``GetResolverRuleAssociation`` request.

    - **Id** *(string) --*

      The ID of the association between a resolver rule and a VPC. Resolver assigns this value
      when you submit an  AssociateResolverRule request.

    - **ResolverRuleId** *(string) --*

      The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
      .

    - **Name** *(string) --*

      The name of an association between a resolver rule and a VPC.

    - **VPCId** *(string) --*

      The ID of the VPC that you associated the resolver rule with.

    - **Status** *(string) --*

      A code that specifies the current status of the association between a resolver rule and a
      VPC.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientGetResolverRuleAssociationResponseTypeDef = TypedDict(
    "_ClientGetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef
    },
    total=False,
)


class ClientGetResolverRuleAssociationResponseTypeDef(
    _ClientGetResolverRuleAssociationResponseTypeDef
):
    """
    Type definition for `ClientGetResolverRuleAssociation` `Response`

    - **ResolverRuleAssociation** *(dict) --*

      Information about the resolver rule association that you specified in a
      ``GetResolverRuleAssociation`` request.

      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.

      - **ResolverRuleId** *(string) --*

        The ID of the resolver rule that you associated with the VPC that is specified by ``VPCId``
        .

      - **Name** *(string) --*

        The name of an association between a resolver rule and a VPC.

      - **VPCId** *(string) --*

        The ID of the VPC that you associated the resolver rule with.

      - **Status** *(string) --*

        A code that specifies the current status of the association between a resolver rule and a
        VPC.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientGetResolverRulePolicyResponseTypeDef = TypedDict(
    "_ClientGetResolverRulePolicyResponseTypeDef",
    {"ResolverRulePolicy": str},
    total=False,
)


class ClientGetResolverRulePolicyResponseTypeDef(
    _ClientGetResolverRulePolicyResponseTypeDef
):
    """
    Type definition for `ClientGetResolverRulePolicy` `Response`

    - **ResolverRulePolicy** *(string) --*

      Information about the resolver rule policy that you specified in a ``GetResolverRulePolicy``
      request.
    """


_ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    """
    Type definition for `ClientGetResolverRuleResponseResolverRule` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
    queries to.

    - **Ip** *(string) --*

      One IP address that you want to forward DNS queries to. You can specify only IPv4
      addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientGetResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": str,
        "StatusMessage": str,
        "RuleType": str,
        "Name": str,
        "TargetIps": List[ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": str,
    },
    total=False,
)


class ClientGetResolverRuleResponseResolverRuleTypeDef(
    _ClientGetResolverRuleResponseResolverRuleTypeDef
):
    """
    Type definition for `ClientGetResolverRuleResponse` `ResolverRule`

    Information about the resolver rule that you specified in a ``GetResolverRule`` request.

    - **Id** *(string) --*

      The ID that Resolver assigned to the resolver rule when you created it.

    - **CreatorRequestId** *(string) --*

      A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
      identifies the request and allows failed requests to be retried without the risk of
      executing the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

    - **DomainName** *(string) --*

      DNS queries for this domain name are forwarded to the IP addresses that are specified in
      ``TargetIps`` . If a query matches multiple resolver rules (example.com and
      www.example.com), the query is routed using the resolver rule that contains the most
      specific domain name (www.example.com).

    - **Status** *(string) --*

      A code that specifies the current status of the resolver rule.

    - **StatusMessage** *(string) --*

      A detailed description of the status of a resolver rule.

    - **RuleType** *(string) --*

      This value is always ``FORWARD`` . Other resolver rule types aren't supported.

    - **Name** *(string) --*

      The name for the resolver rule, which you specified when you created the resolver rule.

    - **TargetIps** *(list) --*

      An array that contains the IP addresses and ports that you want to forward

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
        queries to.

        - **Ip** *(string) --*

          One IP address that you want to forward DNS queries to. You can specify only IPv4
          addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the endpoint that the rule is associated with.

    - **OwnerId** *(string) --*

      When a rule is shared with another AWS account, the account ID of the account that the rule
      is shared with.

    - **ShareStatus** *(string) --*

      Whether the rules is shared and, if so, whether the current account is sharing the rule
      with another account, or another account is sharing the rule with the current account.
    """


_ClientGetResolverRuleResponseTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseTypeDef",
    {"ResolverRule": ClientGetResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientGetResolverRuleResponseTypeDef(_ClientGetResolverRuleResponseTypeDef):
    """
    Type definition for `ClientGetResolverRule` `Response`

    - **ResolverRule** *(dict) --*

      Information about the resolver rule that you specified in a ``GetResolverRule`` request.

      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.

      - **CreatorRequestId** *(string) --*

        A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
        identifies the request and allows failed requests to be retried without the risk of
        executing the operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

      - **DomainName** *(string) --*

        DNS queries for this domain name are forwarded to the IP addresses that are specified in
        ``TargetIps`` . If a query matches multiple resolver rules (example.com and
        www.example.com), the query is routed using the resolver rule that contains the most
        specific domain name (www.example.com).

      - **Status** *(string) --*

        A code that specifies the current status of the resolver rule.

      - **StatusMessage** *(string) --*

        A detailed description of the status of a resolver rule.

      - **RuleType** *(string) --*

        This value is always ``FORWARD`` . Other resolver rule types aren't supported.

      - **Name** *(string) --*

        The name for the resolver rule, which you specified when you created the resolver rule.

      - **TargetIps** *(list) --*

        An array that contains the IP addresses and ports that you want to forward

        - *(dict) --*

          In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
          queries to.

          - **Ip** *(string) --*

            One IP address that you want to forward DNS queries to. You can specify only IPv4
            addresses.

          - **Port** *(integer) --*

            The port at ``Ip`` that you want to forward DNS queries to.

      - **ResolverEndpointId** *(string) --*

        The ID of the endpoint that the rule is associated with.

      - **OwnerId** *(string) --*

        When a rule is shared with another AWS account, the account ID of the account that the rule
        is shared with.

      - **ShareStatus** *(string) --*

        Whether the rules is shared and, if so, whether the current account is sharing the rule
        with another account, or another account is sharing the rule with the current account.
    """


_ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef = TypedDict(
    "_ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef(
    _ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef
):
    """
    Type definition for `ClientListResolverEndpointIpAddressesResponse` `IpAddresses`

    In the response to a  GetResolverEndpoint request, information about the IP addresses that
    the resolver endpoint uses for DNS queries.

    - **IpId** *(string) --*

      The ID of one IP address.

    - **SubnetId** *(string) --*

      The ID of one subnet.

    - **Ip** *(string) --*

      One IP address that the resolver endpoint uses for DNS queries.

    - **Status** *(string) --*

      A status code that gives the current status of the request.

    - **StatusMessage** *(string) --*

      A message that provides additional information about the status of the request.

    - **CreationTime** *(string) --*

      The date and time that the IP address was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the IP address was last modified, in Unix time format and
      Coordinated Universal Time (UTC).
    """


_ClientListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "_ClientListResolverEndpointIpAddressesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List[
            ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef
        ],
    },
    total=False,
)


class ClientListResolverEndpointIpAddressesResponseTypeDef(
    _ClientListResolverEndpointIpAddressesResponseTypeDef
):
    """
    Type definition for `ClientListResolverEndpointIpAddresses` `Response`

    - **NextToken** *(string) --*

      If the specified endpoint has more than ``MaxResults`` IP addresses, you can submit another
      ``ListResolverEndpointIpAddresses`` request to get the next group of IP addresses. In the
      next request, specify the value of ``NextToken`` from the previous response.

    - **MaxResults** *(integer) --*

      The value that you specified for ``MaxResults`` in the request.

    - **IpAddresses** *(list) --*

      The IP addresses that DNS queries pass through on their way to your network (outbound
      endpoint) or on the way to Resolver (inbound endpoint).

      - *(dict) --*

        In the response to a  GetResolverEndpoint request, information about the IP addresses that
        the resolver endpoint uses for DNS queries.

        - **IpId** *(string) --*

          The ID of one IP address.

        - **SubnetId** *(string) --*

          The ID of one subnet.

        - **Ip** *(string) --*

          One IP address that the resolver endpoint uses for DNS queries.

        - **Status** *(string) --*

          A status code that gives the current status of the request.

        - **StatusMessage** *(string) --*

          A message that provides additional information about the status of the request.

        - **CreationTime** *(string) --*

          The date and time that the IP address was created, in Unix time format and Coordinated
          Universal Time (UTC).

        - **ModificationTime** *(string) --*

          The date and time that the IP address was last modified, in Unix time format and
          Coordinated Universal Time (UTC).
    """


_ClientListResolverEndpointsFiltersTypeDef = TypedDict(
    "_ClientListResolverEndpointsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListResolverEndpointsFiltersTypeDef(
    _ClientListResolverEndpointsFiltersTypeDef
):
    """
    Type definition for `ClientListResolverEndpoints` `Filters`

    For ``List`` operations, an optional specification to return a subset of objects, such as
    resolver endpoints or resolver rules.

    - **Name** *(string) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the name of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``Direction`` for the value of ``Name`` .

    - **Values** *(list) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the value of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``INBOUND`` for the value of ``Values`` .

      - *(string) --*
    """


_ClientListResolverEndpointsResponseResolverEndpointsTypeDef = TypedDict(
    "_ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientListResolverEndpointsResponseResolverEndpointsTypeDef(
    _ClientListResolverEndpointsResponseResolverEndpointsTypeDef
):
    """
    Type definition for `ClientListResolverEndpointsResponse` `ResolverEndpoints`

    In the response to a  CreateResolverEndpoint ,  DeleteResolverEndpoint ,
    GetResolverEndpoint ,  ListResolverEndpoints , or  UpdateResolverEndpoint request, a
    complex type that contains settings for an existing inbound or outbound resolver endpoint.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing
      the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and
      Coordinated Universal Time (UTC).
    """


_ClientListResolverEndpointsResponseTypeDef = TypedDict(
    "_ClientListResolverEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List[
            ClientListResolverEndpointsResponseResolverEndpointsTypeDef
        ],
    },
    total=False,
)


class ClientListResolverEndpointsResponseTypeDef(
    _ClientListResolverEndpointsResponseTypeDef
):
    """
    Type definition for `ClientListResolverEndpoints` `Response`

    - **NextToken** *(string) --*

      If more than ``MaxResults`` IP addresses match the specified criteria, you can submit another
      ``ListResolverEndpoint`` request to get the next group of results. In the next request,
      specify the value of ``NextToken`` from the previous response.

    - **MaxResults** *(integer) --*

      The value that you specified for ``MaxResults`` in the request.

    - **ResolverEndpoints** *(list) --*

      The resolver endpoints that were created by using the current AWS account, and that match the
      specified filters, if any.

      - *(dict) --*

        In the response to a  CreateResolverEndpoint ,  DeleteResolverEndpoint ,
        GetResolverEndpoint ,  ListResolverEndpoints , or  UpdateResolverEndpoint request, a
        complex type that contains settings for an existing inbound or outbound resolver endpoint.

        - **Id** *(string) --*

          The ID of the resolver endpoint.

        - **CreatorRequestId** *(string) --*

          A unique string that identifies the request that created the resolver endpoint. The
          ``CreatorRequestId`` allows failed requests to be retried without the risk of executing
          the operation twice.

        - **Arn** *(string) --*

          The ARN (Amazon Resource Name) for the resolver endpoint.

        - **Name** *(string) --*

          The name that you assigned to the resolver endpoint when you submitted a
          CreateResolverEndpoint request.

        - **SecurityGroupIds** *(list) --*

          The ID of one or more security groups that control access to this VPC. The security group
          must include one or more inbound resolver rules.

          - *(string) --*

        - **Direction** *(string) --*

          Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

          * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

          * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

        - **IpAddressCount** *(integer) --*

          The number of IP addresses that the resolver endpoint can use for DNS queries.

        - **HostVPCId** *(string) --*

          The ID of the VPC that you want to create the resolver endpoint in.

        - **Status** *(string) --*

          A code that specifies the current status of the resolver endpoint.

        - **StatusMessage** *(string) --*

          A detailed description of the status of the resolver endpoint.

        - **CreationTime** *(string) --*

          The date and time that the endpoint was created, in Unix time format and Coordinated
          Universal Time (UTC).

        - **ModificationTime** *(string) --*

          The date and time that the endpoint was last modified, in Unix time format and
          Coordinated Universal Time (UTC).
    """


_ClientListResolverRuleAssociationsFiltersTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListResolverRuleAssociationsFiltersTypeDef(
    _ClientListResolverRuleAssociationsFiltersTypeDef
):
    """
    Type definition for `ClientListResolverRuleAssociations` `Filters`

    For ``List`` operations, an optional specification to return a subset of objects, such as
    resolver endpoints or resolver rules.

    - **Name** *(string) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the name of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``Direction`` for the value of ``Name`` .

    - **Values** *(list) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the value of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``INBOUND`` for the value of ``Values`` .

      - *(string) --*
    """


_ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)


class ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef(
    _ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef
):
    """
    Type definition for `ClientListResolverRuleAssociationsResponse` `ResolverRuleAssociations`

    In the response to an  AssociateResolverRule ,  DisassociateResolverRule , or
    ListResolverRuleAssociations request, information about an association between a resolver
    rule and a VPC.

    - **Id** *(string) --*

      The ID of the association between a resolver rule and a VPC. Resolver assigns this value
      when you submit an  AssociateResolverRule request.

    - **ResolverRuleId** *(string) --*

      The ID of the resolver rule that you associated with the VPC that is specified by
      ``VPCId`` .

    - **Name** *(string) --*

      The name of an association between a resolver rule and a VPC.

    - **VPCId** *(string) --*

      The ID of the VPC that you associated the resolver rule with.

    - **Status** *(string) --*

      A code that specifies the current status of the association between a resolver rule and a
      VPC.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List[
            ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientListResolverRuleAssociationsResponseTypeDef(
    _ClientListResolverRuleAssociationsResponseTypeDef
):
    """
    Type definition for `ClientListResolverRuleAssociations` `Response`

    - **NextToken** *(string) --*

      If more than ``MaxResults`` rule associations match the specified criteria, you can submit
      another ``ListResolverRuleAssociation`` request to get the next group of results. In the next
      request, specify the value of ``NextToken`` from the previous response.

    - **MaxResults** *(integer) --*

      The value that you specified for ``MaxResults`` in the request.

    - **ResolverRuleAssociations** *(list) --*

      The associations that were created between resolver rules and VPCs using the current AWS
      account, and that match the specified filters, if any.

      - *(dict) --*

        In the response to an  AssociateResolverRule ,  DisassociateResolverRule , or
        ListResolverRuleAssociations request, information about an association between a resolver
        rule and a VPC.

        - **Id** *(string) --*

          The ID of the association between a resolver rule and a VPC. Resolver assigns this value
          when you submit an  AssociateResolverRule request.

        - **ResolverRuleId** *(string) --*

          The ID of the resolver rule that you associated with the VPC that is specified by
          ``VPCId`` .

        - **Name** *(string) --*

          The name of an association between a resolver rule and a VPC.

        - **VPCId** *(string) --*

          The ID of the VPC that you associated the resolver rule with.

        - **Status** *(string) --*

          A code that specifies the current status of the association between a resolver rule and a
          VPC.

        - **StatusMessage** *(string) --*

          A detailed description of the status of the association between a resolver rule and a VPC.
    """


_ClientListResolverRulesFiltersTypeDef = TypedDict(
    "_ClientListResolverRulesFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListResolverRulesFiltersTypeDef(_ClientListResolverRulesFiltersTypeDef):
    """
    Type definition for `ClientListResolverRules` `Filters`

    For ``List`` operations, an optional specification to return a subset of objects, such as
    resolver endpoints or resolver rules.

    - **Name** *(string) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the name of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``Direction`` for the value of ``Name`` .

    - **Values** *(list) --*

      When you're using a ``List`` operation and you want the operation to return a subset of
      objects, such as resolver endpoints or resolver rules, the value of the parameter that you
      want to use to filter objects. For example, to list only inbound resolver endpoints, specify
      ``INBOUND`` for the value of ``Values`` .

      - *(string) --*
    """


_ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef = TypedDict(
    "_ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef(
    _ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef
):
    """
    Type definition for `ClientListResolverRulesResponseResolverRules` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
    queries to.

    - **Ip** *(string) --*

      One IP address that you want to forward DNS queries to. You can specify only IPv4
      addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientListResolverRulesResponseResolverRulesTypeDef = TypedDict(
    "_ClientListResolverRulesResponseResolverRulesTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": str,
        "StatusMessage": str,
        "RuleType": str,
        "Name": str,
        "TargetIps": List[ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": str,
    },
    total=False,
)


class ClientListResolverRulesResponseResolverRulesTypeDef(
    _ClientListResolverRulesResponseResolverRulesTypeDef
):
    """
    Type definition for `ClientListResolverRulesResponse` `ResolverRules`

    For queries that originate in your VPC, detailed information about a resolver rule, which
    specifies how to route DNS queries out of the VPC. The ``ResolverRule`` parameter appears
    in the response to a  CreateResolverRule ,  DeleteResolverRule ,  GetResolverRule ,
    ListResolverRules , or  UpdateResolverRule request.

    - **Id** *(string) --*

      The ID that Resolver assigned to the resolver rule when you created it.

    - **CreatorRequestId** *(string) --*

      A unique string that you specified when you created the resolver rule.
      ``CreatorRequestId`` identifies the request and allows failed requests to be retried
      without the risk of executing the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

    - **DomainName** *(string) --*

      DNS queries for this domain name are forwarded to the IP addresses that are specified in
      ``TargetIps`` . If a query matches multiple resolver rules (example.com and
      www.example.com), the query is routed using the resolver rule that contains the most
      specific domain name (www.example.com).

    - **Status** *(string) --*

      A code that specifies the current status of the resolver rule.

    - **StatusMessage** *(string) --*

      A detailed description of the status of a resolver rule.

    - **RuleType** *(string) --*

      This value is always ``FORWARD`` . Other resolver rule types aren't supported.

    - **Name** *(string) --*

      The name for the resolver rule, which you specified when you created the resolver rule.

    - **TargetIps** *(list) --*

      An array that contains the IP addresses and ports that you want to forward

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
        queries to.

        - **Ip** *(string) --*

          One IP address that you want to forward DNS queries to. You can specify only IPv4
          addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the endpoint that the rule is associated with.

    - **OwnerId** *(string) --*

      When a rule is shared with another AWS account, the account ID of the account that the
      rule is shared with.

    - **ShareStatus** *(string) --*

      Whether the rules is shared and, if so, whether the current account is sharing the rule
      with another account, or another account is sharing the rule with the current account.
    """


_ClientListResolverRulesResponseTypeDef = TypedDict(
    "_ClientListResolverRulesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List[ClientListResolverRulesResponseResolverRulesTypeDef],
    },
    total=False,
)


class ClientListResolverRulesResponseTypeDef(_ClientListResolverRulesResponseTypeDef):
    """
    Type definition for `ClientListResolverRules` `Response`

    - **NextToken** *(string) --*

      If more than ``MaxResults`` resolver rules match the specified criteria, you can submit
      another ``ListResolverRules`` request to get the next group of results. In the next request,
      specify the value of ``NextToken`` from the previous response.

    - **MaxResults** *(integer) --*

      The value that you specified for ``MaxResults`` in the request.

    - **ResolverRules** *(list) --*

      The resolver rules that were created using the current AWS account and that match the
      specified filters, if any.

      - *(dict) --*

        For queries that originate in your VPC, detailed information about a resolver rule, which
        specifies how to route DNS queries out of the VPC. The ``ResolverRule`` parameter appears
        in the response to a  CreateResolverRule ,  DeleteResolverRule ,  GetResolverRule ,
        ListResolverRules , or  UpdateResolverRule request.

        - **Id** *(string) --*

          The ID that Resolver assigned to the resolver rule when you created it.

        - **CreatorRequestId** *(string) --*

          A unique string that you specified when you created the resolver rule.
          ``CreatorRequestId`` identifies the request and allows failed requests to be retried
          without the risk of executing the operation twice.

        - **Arn** *(string) --*

          The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

        - **DomainName** *(string) --*

          DNS queries for this domain name are forwarded to the IP addresses that are specified in
          ``TargetIps`` . If a query matches multiple resolver rules (example.com and
          www.example.com), the query is routed using the resolver rule that contains the most
          specific domain name (www.example.com).

        - **Status** *(string) --*

          A code that specifies the current status of the resolver rule.

        - **StatusMessage** *(string) --*

          A detailed description of the status of a resolver rule.

        - **RuleType** *(string) --*

          This value is always ``FORWARD`` . Other resolver rule types aren't supported.

        - **Name** *(string) --*

          The name for the resolver rule, which you specified when you created the resolver rule.

        - **TargetIps** *(list) --*

          An array that contains the IP addresses and ports that you want to forward

          - *(dict) --*

            In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
            queries to.

            - **Ip** *(string) --*

              One IP address that you want to forward DNS queries to. You can specify only IPv4
              addresses.

            - **Port** *(integer) --*

              The port at ``Ip`` that you want to forward DNS queries to.

        - **ResolverEndpointId** *(string) --*

          The ID of the endpoint that the rule is associated with.

        - **OwnerId** *(string) --*

          When a rule is shared with another AWS account, the account ID of the account that the
          rule is shared with.

        - **ShareStatus** *(string) --*

          Whether the rules is shared and, if so, whether the current account is sharing the rule
          with another account, or another account is sharing the rule with the current account.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
    for the tag) and a ``Value`` .

    - **Key** *(string) --*

      The name for the tag. For example, if you want to associate Resolver resources with the
      account IDs of your customers for billing purposes, the value of ``Key`` might be
      ``account-id`` .

    - **Value** *(string) --*

      The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might
      be the ID of the customer account that you're creating the resource for.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      The tags that are associated with the resource that you specified in the
      ``ListTagsForResource`` request.

      - *(dict) --*

        One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
        for the tag) and a ``Value`` .

        - **Key** *(string) --*

          The name for the tag. For example, if you want to associate Resolver resources with the
          account IDs of your customers for billing purposes, the value of ``Key`` might be
          ``account-id`` .

        - **Value** *(string) --*

          The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might
          be the ID of the customer account that you're creating the resource for.

    - **NextToken** *(string) --*

      If more than ``MaxResults`` tags match the specified criteria, you can submit another
      ``ListTagsForResource`` request to get the next group of results. In the next request,
      specify the value of ``NextToken`` from the previous response.
    """


_ClientPutResolverRulePolicyResponseTypeDef = TypedDict(
    "_ClientPutResolverRulePolicyResponseTypeDef", {"ReturnValue": bool}, total=False
)


class ClientPutResolverRulePolicyResponseTypeDef(
    _ClientPutResolverRulePolicyResponseTypeDef
):
    """
    Type definition for `ClientPutResolverRulePolicy` `Response`

    The response to a ``PutResolverRulePolicy`` request.

    - **ReturnValue** *(boolean) --*

      Whether the ``PutResolverRulePolicy`` request was successful.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name for
    the tag) and a ``Value`` .

    - **Key** *(string) --*

      The name for the tag. For example, if you want to associate Resolver resources with the
      account IDs of your customers for billing purposes, the value of ``Key`` might be
      ``account-id`` .

    - **Value** *(string) --*

      The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might be
      the ID of the customer account that you're creating the resource for.
    """


_ClientUpdateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": str,
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": str,
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientUpdateResolverEndpointResponseResolverEndpointTypeDef(
    _ClientUpdateResolverEndpointResponseResolverEndpointTypeDef
):
    """
    Type definition for `ClientUpdateResolverEndpointResponse` `ResolverEndpoint`

    The response to an ``UpdateResolverEndpoint`` request.

    - **Id** *(string) --*

      The ID of the resolver endpoint.

    - **CreatorRequestId** *(string) --*

      A unique string that identifies the request that created the resolver endpoint. The
      ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
      operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver endpoint.

    - **Name** *(string) --*

      The name that you assigned to the resolver endpoint when you submitted a
      CreateResolverEndpoint request.

    - **SecurityGroupIds** *(list) --*

      The ID of one or more security groups that control access to this VPC. The security group
      must include one or more inbound resolver rules.

      - *(string) --*

    - **Direction** *(string) --*

      Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

      * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

      * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

    - **IpAddressCount** *(integer) --*

      The number of IP addresses that the resolver endpoint can use for DNS queries.

    - **HostVPCId** *(string) --*

      The ID of the VPC that you want to create the resolver endpoint in.

    - **Status** *(string) --*

      A code that specifies the current status of the resolver endpoint.

    - **StatusMessage** *(string) --*

      A detailed description of the status of the resolver endpoint.

    - **CreationTime** *(string) --*

      The date and time that the endpoint was created, in Unix time format and Coordinated
      Universal Time (UTC).

    - **ModificationTime** *(string) --*

      The date and time that the endpoint was last modified, in Unix time format and Coordinated
      Universal Time (UTC).
    """


_ClientUpdateResolverEndpointResponseTypeDef = TypedDict(
    "_ClientUpdateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientUpdateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientUpdateResolverEndpointResponseTypeDef(
    _ClientUpdateResolverEndpointResponseTypeDef
):
    """
    Type definition for `ClientUpdateResolverEndpoint` `Response`

    - **ResolverEndpoint** *(dict) --*

      The response to an ``UpdateResolverEndpoint`` request.

      - **Id** *(string) --*

        The ID of the resolver endpoint.

      - **CreatorRequestId** *(string) --*

        A unique string that identifies the request that created the resolver endpoint. The
        ``CreatorRequestId`` allows failed requests to be retried without the risk of executing the
        operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver endpoint.

      - **Name** *(string) --*

        The name that you assigned to the resolver endpoint when you submitted a
        CreateResolverEndpoint request.

      - **SecurityGroupIds** *(list) --*

        The ID of one or more security groups that control access to this VPC. The security group
        must include one or more inbound resolver rules.

        - *(string) --*

      - **Direction** *(string) --*

        Indicates whether the resolver endpoint allows inbound or outbound DNS queries:

        * ``INBOUND`` : allows DNS queries to your VPC from your network or another VPC

        * ``OUTBOUND`` : allows DNS queries from your VPC to your network or another VPC

      - **IpAddressCount** *(integer) --*

        The number of IP addresses that the resolver endpoint can use for DNS queries.

      - **HostVPCId** *(string) --*

        The ID of the VPC that you want to create the resolver endpoint in.

      - **Status** *(string) --*

        A code that specifies the current status of the resolver endpoint.

      - **StatusMessage** *(string) --*

        A detailed description of the status of the resolver endpoint.

      - **CreationTime** *(string) --*

        The date and time that the endpoint was created, in Unix time format and Coordinated
        Universal Time (UTC).

      - **ModificationTime** *(string) --*

        The date and time that the endpoint was last modified, in Unix time format and Coordinated
        Universal Time (UTC).
    """


_RequiredClientUpdateResolverRuleConfigTargetIpsTypeDef = TypedDict(
    "_RequiredClientUpdateResolverRuleConfigTargetIpsTypeDef", {"Ip": str}
)
_OptionalClientUpdateResolverRuleConfigTargetIpsTypeDef = TypedDict(
    "_OptionalClientUpdateResolverRuleConfigTargetIpsTypeDef",
    {"Port": int},
    total=False,
)


class ClientUpdateResolverRuleConfigTargetIpsTypeDef(
    _RequiredClientUpdateResolverRuleConfigTargetIpsTypeDef,
    _OptionalClientUpdateResolverRuleConfigTargetIpsTypeDef,
):
    """
    Type definition for `ClientUpdateResolverRuleConfig` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

    - **Ip** *(string) --* **[REQUIRED]**

      One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientUpdateResolverRuleConfigTypeDef = TypedDict(
    "_ClientUpdateResolverRuleConfigTypeDef",
    {
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleConfigTargetIpsTypeDef],
        "ResolverEndpointId": str,
    },
    total=False,
)


class ClientUpdateResolverRuleConfigTypeDef(_ClientUpdateResolverRuleConfigTypeDef):
    """
    Type definition for `ClientUpdateResolverRule` `Config`

    The new settings for the resolver rule.

    - **Name** *(string) --*

      The new name for the resolver rule. The name that you specify appears in the Resolver dashboard
      in the Route 53 console.

    - **TargetIps** *(list) --*

      For DNS queries that originate in your VPC, the new IP addresses that you want to route
      outbound DNS queries to.

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.

        - **Ip** *(string) --* **[REQUIRED]**

          One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the new outbound resolver endpoint that you want to use to route DNS queries to the
      IP addresses that you specify in ``TargetIps`` .
    """


_ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    """
    Type definition for `ClientUpdateResolverRuleResponseResolverRule` `TargetIps`

    In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
    queries to.

    - **Ip** *(string) --*

      One IP address that you want to forward DNS queries to. You can specify only IPv4
      addresses.

    - **Port** *(integer) --*

      The port at ``Ip`` that you want to forward DNS queries to.
    """


_ClientUpdateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": str,
        "StatusMessage": str,
        "RuleType": str,
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": str,
    },
    total=False,
)


class ClientUpdateResolverRuleResponseResolverRuleTypeDef(
    _ClientUpdateResolverRuleResponseResolverRuleTypeDef
):
    """
    Type definition for `ClientUpdateResolverRuleResponse` `ResolverRule`

    The response to an ``UpdateResolverRule`` request.

    - **Id** *(string) --*

      The ID that Resolver assigned to the resolver rule when you created it.

    - **CreatorRequestId** *(string) --*

      A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
      identifies the request and allows failed requests to be retried without the risk of
      executing the operation twice.

    - **Arn** *(string) --*

      The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

    - **DomainName** *(string) --*

      DNS queries for this domain name are forwarded to the IP addresses that are specified in
      ``TargetIps`` . If a query matches multiple resolver rules (example.com and
      www.example.com), the query is routed using the resolver rule that contains the most
      specific domain name (www.example.com).

    - **Status** *(string) --*

      A code that specifies the current status of the resolver rule.

    - **StatusMessage** *(string) --*

      A detailed description of the status of a resolver rule.

    - **RuleType** *(string) --*

      This value is always ``FORWARD`` . Other resolver rule types aren't supported.

    - **Name** *(string) --*

      The name for the resolver rule, which you specified when you created the resolver rule.

    - **TargetIps** *(list) --*

      An array that contains the IP addresses and ports that you want to forward

      - *(dict) --*

        In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
        queries to.

        - **Ip** *(string) --*

          One IP address that you want to forward DNS queries to. You can specify only IPv4
          addresses.

        - **Port** *(integer) --*

          The port at ``Ip`` that you want to forward DNS queries to.

    - **ResolverEndpointId** *(string) --*

      The ID of the endpoint that the rule is associated with.

    - **OwnerId** *(string) --*

      When a rule is shared with another AWS account, the account ID of the account that the rule
      is shared with.

    - **ShareStatus** *(string) --*

      Whether the rules is shared and, if so, whether the current account is sharing the rule
      with another account, or another account is sharing the rule with the current account.
    """


_ClientUpdateResolverRuleResponseTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientUpdateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientUpdateResolverRuleResponseTypeDef(_ClientUpdateResolverRuleResponseTypeDef):
    """
    Type definition for `ClientUpdateResolverRule` `Response`

    - **ResolverRule** *(dict) --*

      The response to an ``UpdateResolverRule`` request.

      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.

      - **CreatorRequestId** *(string) --*

        A unique string that you specified when you created the resolver rule. ``CreatorRequestId``
        identifies the request and allows failed requests to be retried without the risk of
        executing the operation twice.

      - **Arn** *(string) --*

        The ARN (Amazon Resource Name) for the resolver rule specified by ``Id`` .

      - **DomainName** *(string) --*

        DNS queries for this domain name are forwarded to the IP addresses that are specified in
        ``TargetIps`` . If a query matches multiple resolver rules (example.com and
        www.example.com), the query is routed using the resolver rule that contains the most
        specific domain name (www.example.com).

      - **Status** *(string) --*

        A code that specifies the current status of the resolver rule.

      - **StatusMessage** *(string) --*

        A detailed description of the status of a resolver rule.

      - **RuleType** *(string) --*

        This value is always ``FORWARD`` . Other resolver rule types aren't supported.

      - **Name** *(string) --*

        The name for the resolver rule, which you specified when you created the resolver rule.

      - **TargetIps** *(list) --*

        An array that contains the IP addresses and ports that you want to forward

        - *(dict) --*

          In a  CreateResolverRule request, an array of the IPs that you want to forward DNS
          queries to.

          - **Ip** *(string) --*

            One IP address that you want to forward DNS queries to. You can specify only IPv4
            addresses.

          - **Port** *(integer) --*

            The port at ``Ip`` that you want to forward DNS queries to.

      - **ResolverEndpointId** *(string) --*

        The ID of the endpoint that the rule is associated with.

      - **OwnerId** *(string) --*

        When a rule is shared with another AWS account, the account ID of the account that the rule
        is shared with.

      - **ShareStatus** *(string) --*

        Whether the rules is shared and, if so, whether the current account is sharing the rule
        with another account, or another account is sharing the rule with the current account.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

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


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

    One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
    for the tag) and a ``Value`` .

    - **Key** *(string) --*

      The name for the tag. For example, if you want to associate Resolver resources with the
      account IDs of your customers for billing purposes, the value of ``Key`` might be
      ``account-id`` .

    - **Value** *(string) --*

      The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might
      be the ID of the customer account that you're creating the resource for.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **Tags** *(list) --*

      The tags that are associated with the resource that you specified in the
      ``ListTagsForResource`` request.

      - *(dict) --*

        One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
        for the tag) and a ``Value`` .

        - **Key** *(string) --*

          The name for the tag. For example, if you want to associate Resolver resources with the
          account IDs of your customers for billing purposes, the value of ``Key`` might be
          ``account-id`` .

        - **Value** *(string) --*

          The value for the tag. For example, if ``Key`` is ``account-id`` , then ``Value`` might
          be the ID of the customer account that you're creating the resource for.
    """
